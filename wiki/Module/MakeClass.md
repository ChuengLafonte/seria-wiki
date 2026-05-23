-- <pre>
-- Modul MakeClass (Usang). Gunakan Module:Class sebagai gantinya.

local table, lu = require('Module:Table'), require('Module:LibU')
local p = {}

---------------------------------------------------------------------------------
-- function: isStaticClass(t: table)
-- 
-- Checks if a class is static.
---------------------------------------------------------------------------------
function p.isStaticClass(t)
	local mt = getmetatable(t)
	return type(t) == 'table' and mt and mt.__isClass and not mt.__constructorCalled
end

---------------------------------------------------------------------------------
-- function: isClass(t: table)
--
-- Determines if the table is a class.
---------------------------------------------------------------------------------
function p.isClass(t)
	return type(t) == 'table' and (getmetatable(t) or {}).__isClass or false
end

---------------------------------------------------------------------------------
-- Base helper methods for .makeClass()
---------------------------------------------------------------------------------
local baseMethods = {}
local baseStaticMethods = {}

function baseMethods:instanceof(class)
	lu.checkType('instanceof', 1, class, { 'table' })
	lu.assertTrue(p.isClass(class), 'class expected', 2)
	lu.assertTrue(p.isStaticClass(class), 'the class must be static', 2)
	
	if not self.parent then
		return false
	end
	
	local tmp = self
	while tmp.parent do
		if tmp.parent.static == class then
			return true
		else
			tmp = tmp.parent
		end
	end
	
	return false
end

function baseStaticMethods:checkSelf(toCheck)
	if type(toCheck) ~= 'table' or toCheck.static.constructor ~= self.constructor then
		local method = getStackName()
		
		error(string.format(
			'%sinvalid self object. Did you call .%s() with a dot instead of a colon, i.e. ' ..
			'%s%s(...) instead of %s%s(...), or did you call the method directly from the prototype?',
			self.name and self.name .. ': ' or '', method, self.name and self.name .. '.' or '.', method, self.name and self.name .. ':' or ':', method
		 ), 3)
	end
end

function baseStaticMethods:extendPrototype(methods)
	lu.checkType('extendPrototype', 1, methods, { 'table' })
	
	table.merge(self.prototype, methods)
	return self
end

---------------------------------------------------------------------------------
-- function: makeClass(constructor?: function, methods: table, parentClass?: table, options?: table)
--
-- Creates a class table.
---------------------------------------------------------------------------------
function p.makeClass(constructor, methods, parentClass, options)
	lu.checkType('makeClass', 1, constructor, { 'function', 'table', 'nil' })
	lu.checkType('makeClass', 2, methods, { 'table', 'nil' })
	lu.checkType('makeClass', 3, parentClass, { 'table', 'nil' })
	lu.checkType('makeClass', 4, options, 'table', true)
	
	local options = options or {}
	local ignoreTableRet = unpack{
			options.ignoreTableRet or options.ignoreTable or options.ignore,
		}
	local origConstructor = constructor
		
	function tmpFunc(t1)
		return t1
	end
	
	function tmpChildFunc(t1, ...)
		t1.super(...)
		return t1
	end
	
	local get, set = 'get', 'set'
	local methodIsClass = p.isClass(methods)
	local constructorIsClass = p.isClass(constructor)
	local tpConstructor = type(constructor)
	
	if tpConstructor == 'table' and (methodIsClass or (methods == nil and parentClass == nil and table.length(options) == 0)) and not constructorIsClass then
		parentClass = methods
		methods = constructor
		origConstructor, constructor = nil, nil
	elseif constructorIsClass then
		parentClass = constructor
		origConstructor, constructor = nil, nil
	elseif tpConstructor == 'table' and type(methods) == 'table' then
		options = methods
		methods = nil
		parentClass = nil
	elseif tpConstructor == 'function' and methodIsClass then
		parentClass = methods
		methods = nil
	end
	methods = methods ~= nil and methods or {}
	
	if methods.constructor then
		constructor = methods.constructor
	elseif not methods.constructor and type(origConstructor) == 'table' then
		constructor = parentClass and tmpChildFunc or tmpFunc
	end
	
	local util = {}
	local t2 = {}
	local staticReservedNames = table.sequenceToSet{
		'parent',
		'methods',
		'super',
		'__constructorCalled',
		'__isClass',
		'prototype',
		'name',
	}
	
	local reservedNames = table.sequenceToSet{
		'parent',
		'methods',
		'static',
		'__proto__',
		'super',
		'__constructorCalled',
		'__isClass',
		'name',
	}
	
	local allowedTypes = table.sequenceToSet{
		'static',
	}
	
	if constructor == nil then
		constructor = parentClass and tmpChildFunc or tmpFunc
	end
	
	function util:methodType(f, searchType)
		if searchType then
			searchType = searchType:lower()
		end
		
		if type(f) == 'function' then return 'function' end
		if type(f) ~= 'table' then return false end
		if type(f[2]) ~= 'function' then return false end
		
		local f1 = f[1]
		local tpF1 = type(f1)
		
		if tpF1 == 'table' then
			if #f1 == 1 then
				if searchType then
					return f1[1] == searchType
					and searchType
					or false
				else
					return f1[1]
				end
			else
				if searchType then
					return f1[1] == searchType
					and searchType
					or f1[2] == searchType
					and searchType
					or false
				else
					return unpack(f1)
				end
			end
		elseif tpF1 == 'string' and searchType then
			return f1 == searchType
			and searchType 
			or false
		else
			return f1
		end
	end
	
	function util:filterMethods(t, _type, invert)
		local ret = {}
		for k, v in pairs(t) do
			local tmp = util:methodType(v, _type) == _type
			
			local compare
			if invert then
				compare = not tmp
			else
				compare = tmp
			end
			
			if compare then
				ret[k] = v
			end
		end
		return ret
	end
	
	function util:new(...)
		local methods = util:filterMethods(methods, 'static', true)
		
		local mt = {
			methods = methods,
			parent = parentClass,
			static = t2,
			name = options.name,
			__isClass = true,
		}
		
		for k, v in pairs(t2.prototype) do
			methods[k] = v
		end
		
		local t1 = {}
		local metatableMethods = {}
		
		local nonFuncMethods = util:filterMethods(methods, false)
		for k, v in pairs(methods) do
			if not reservedNames[k] then
				t1[k] = nonFuncMethods[k]
			end
		end
			
		if parentClass and (getmetatable(parentClass) or {}).__constructorCalled == true then
			for k, v in pairs(parentClass) do
				if not reservedNames[k] then
					t1[k] = v
				end
			end
		end
		
		mt.__proto__ = mt.methods
		mt.super = function(...)
			if mt.parent == nil then
				error('the class must have a parent when calling the super constructor', 2)
			end
			for k, v in pairs(mt.parent) do
				if not reservedNames[k] then
					t1[k] = v
				end
			end
			
			mt.parent = mt.parent:constructor(...)
			return mt.parent
		end
		
		mt.methods.getmetatable = getmetatable
		table.merge(mt.methods, baseMethods)
		
		mt.__index = function(_, k)
			local value
			
			if reservedNames[k] then
				return mt[k]
			elseif reservedNames[k] and (k == '__isClass' or k == '__constructorCalled') then
				return nil
			end
			
			if parentClass then
				value = mt.methods[k] or (mt.parent.methods or {})[k]
			else
				value = mt.methods[k]
			end
			
			return value
		end
		
		mt.__newindex = function(_, k, v)
			local mType, mType2 = util:methodType(v)
			
			if metatableMethods[k] then
				rawset(mt.methods, k, metatableMethods[k])
				rawset(mt, k, metatableMethods[k])
				return mt.methods[k]
			elseif reservedNames[k] then
				formattedError('class property %q is readonly', 2, k)
			elseif mType == 'static' or mType2 == 'static' then
				return rawset(mt.static, k, v[2])
			else
				return rawset(t1, k, v)
			end
		end
		
		local function methodExists(index)
			local ind = mt.methods[index] or (mt.parent and mt.parent.methods or {})[index]
			if ind then
				return true
			end
		end
		
		metatableMethods.__tostring = function() return t1:__tostring(t1) end
		metatableMethods.__concat = function(a, b) return t1:__concat(a, b) end
		metatableMethods.__call = t1.__call
		metatableMethods.__pairs = function() return t1:__pairs(t1, t1.methods, t1.static) end
		metatableMethods.__ipairs = function() return t1:__ipairs(t1, t1.methods, t1.static) end
		metatableMethods.__add = function(a, b) return t1:__add(a, b) end
		metatableMethods.__sub = function(a, b) return t1:__sub(a, b) end
		metatableMethods.__mul = function(a, b) return t1:__mul(a, b) end
		metatableMethods.__div = function(a, b) return t1:__div(a, b) end
		metatableMethods.__mod = function(a, b) return t1:__mod(a, b) end
		metatableMethods.__pow = function(a, b) return t1:__pow(a, b) end
		metatableMethods.__unm = function(a, b) return t1:__unm(a, b) end
		
		-- Custom metamethods
		metatableMethods.__tonumber = function(a) return t1:__tonumber(a) end
		metatableMethods.__type = function(a, b) return t1:__type(a, b) end
		metatableMethods.__unpack = function(a, b) return t1:__type(a, b) end
		metatableMethods.__toboolean = function(a) return t1:__toboolean(a, b) end
		metatableMethods.__totable = function(a, b, c, d) return t1:__totable(a, b, c, d) end
		metatableMethods.__tconcat = function(a, b, c, d) return t1:__tconcat(a, b, c, d) end
		
		for k, v in pairs(metatableMethods) do
			if methodExists(k) then
				mt[k] = v
			elseif k == '__tostring' and t2.name then
				mt[k] = function(self)
					return '[class ' .. name .. ']'
				end
			end
		end
		
		mt.__metatable = mt 
		setmetatable(t1, mt)
		
		local constructorValue = constructor(t1, ...) 
		
		if t1.parent and p.isStaticClass(t1.parent) then
			error('makeClass(): parent class constructor must be called if the child constructor was called', 2)
		end
		mt.__constructorCalled = true
		
		local ret
		
		if ignoreTableRet or type(constuctorValue) == 'table' then
			ret = constructorValue
		else
			ret = t1
		end
		
		if ret == nil then
			ret = t1
		end
		
		return ret
	end
	
	local metatableMethods, mt = {}, {}
	mt.parent = (parentClass or {}).static
	mt.name = options.name
	mt.methods = util:filterMethods(methods, 'static') or {}
	mt.prototype = table.merge(util:filterMethods(methods, 'static', true), (parentClass or {}).prototype or {}) or {}
	mt.methods.constructor, mt.prototype.constructor = util.new, util.new
	
	table.merge(mt.methods, baseStaticMethods)
	
	mt.__isClass = true
	mt.__constructorCalled = false
	
	mt.__call = util.new
	mt.__index = function(_, k)
		local value
		if mt.parent ~= nil then
			value = mt.methods[k] or mt.parent[k] or (mt.parent.methods or {})[k]
		else
			value = mt.methods[k]
		end
		
		local mType, mType2 = util:methodType(value)
		
		if staticReservedNames[k] then
			return mt[k]
		elseif mType == 'static' or mType == 'static' then
			return value[2]
		else
			return value
		end
	end
	
	mt.__newindex = function(_, k, v)
		local function mType(type)
			return util:methodType(v, type)
		end
		
		if metatableMethods[k] then
			rawset(mt.methods, k, v)
			rawset(mt, k, metatableMethods[k])
		elseif staticReservedNames[k] then
			formattedError('class property %q is readonly', 2, k)
		elseif type(v) == 'function' then
			rawset(mt.methods, k, v)
		elseif util:methodType(v, 'static') then
			rawset(mt, k, v[2])
		else
			rawset(t2, k, v)
		end
		
		return t2[k]
	end
	
	local function methodExists(index)
		local ind = (mt.methods or {})[index] or ((mt.parent or {}).methods or {})[index]
		if ind then
			return true
		end
	end
	
	metatableMethods.__tostring = function() return t2:__tostring(t2) end
	metatableMethods.__concat = function(a, b) return t2:__concat(a, b) end
	metatableMethods.__pairs = function() return t2:__pairs(t2, t2.methods) end
	metatableMethods.__ipairs = function() return t2:__ipairs(t2, t2.methods) end
	metatableMethods.__add = function(a, b) return t2:__add(a, b) end
	metatableMethods.__sub = function(a, b) return t2:__sub(a, b) end
	metatableMethods.__mul = function(a, b) return t2:__mul(a, b) end
	metatableMethods.__div = function(a, b) return t2:__div(a, b) end
	metatableMethods.__mod = function(a, b) return t2:__mod(a, b) end
	metatableMethods.__pow = function(a, b) return t2:__pow(a, b) end
	metatableMethods.__unm = function(a, b) return t2:__unm(a, b) end
	
	-- Custom metamethods
	metatableMethods.__tonumber = function(a) return t2:__tonumber(a) end
	metatableMethods.__type = function(a, b) return t2:__type(a, b) end
	metatableMethods.__unpack = function(a, b) return t2:__type(a, b) end
	metatableMethods.__toboolean = function(a) return t2:__toboolean(a, b) end
	metatableMethods.__totable = function(a, b, c, d) return t2:__totable(a, b, c, d) end
	metatableMethods.__tconcat = function(a, b, c, d) return t2:__tconcat(a, b, c, d) end
	
	for k, v in pairs(metatableMethods) do
		if methodExists(k) then
			mt[k] = v
		end
	end
	
	mt.__metatable = {
		__isClass = true,
		__constructorCalled = false,
	}
	
	return setmetatable(t2, mt)
end

function p.test(...)
	local Class = p.makeClass{ '$', constructor = function() error() end }
	
	Class.prototype.test = function()
		return '$'
	end
	
	Class.prototype.__tostring = function()
		error()
	end
	
	return Class
end

return p

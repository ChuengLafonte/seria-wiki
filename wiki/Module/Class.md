local p = {}
local helpers = {}
local util = {}
local classMtFuncs = {}
local staticMtFuncs = {}
local protoMtFuncs = {}
local classCount = 0

_G._DEBUG = _G.DEBUG or false
local _DEBUG = _G._DEBUG
local getmetatable, setmetatable, string, table, select, error, ipairs, pairs, tostring, type, rawget, rawset, next, unpack = getmetatable, setmetatable, string, table, select, error, ipairs, pairs, tostring, type, rawget, rawset, next, unpack
local tinsert = table.insert
local sformat = string.format
local debug = debug

-- Currently missing features:
-- Super indexing (`self.super[k]`, `self.super:method()`)
-- Mixins

local MESSAGES = {
	INVALID_SUPER_CALL = "Invalid super constructor call. The class must have a parent to call the super constructor",
	GETTER_ONLY_ASSIGNMENT = 'Cannot set class property %q{property} which has only a getter',
	GETTER_ONLY_STATIC_ASSIGNMENT = 'Cannot set static class property %q{property} which has only a getter',
	STATIC_GETTER_ONLY_ASSIGNMENT = 'Cannot set static class property %q{property} which has only a getter',
	MUST_CALL_SUPER = "Invalid class construction. The child class constructor must call `self:super(...)`",
	INVALID_CLASS_ACCESSOR = "Invalid class %{accessor} %q{property}: class %{accessor}s must be functions, recived a %{type} (%q{value}) instead",
	INVALID_STATIC_CLASS_ACCESSOR = "Invalid static class %{accessor} %q{property}: class %{accessor}s must be functions, recived a %{type} (%q{value}) instead",
	INVAID_SELF_SUPER = ":super() was passed an invalid self object of type %{type} (%q{value}). Did you call :super() with a '.' instead of a ':', i.e `.super(...)` instead of `:super(...)`",
	CLASS_FIELD_RESERVED = "Cannot set class property %q{property} because it is reserved",
	STATIC_CLASS_FIELD_RESERVED = "Cannot set static class property %q{property} because it is reserved",
	PROTO_FIELD_RESERVED = "Cannot set class prototype property %q{property} because it is reserved",
	PROPERTIES_TYPE = 'Class properties must be of type table, recived type %q{type} instead',
	STATIC_PROPERTIES_TYPE = 'Class static properties must be of type table, recived type %q{type} instead',
	INVALID_PARENT_CLASS = "Invalid parent class. The parent class must be a class created by makeClass()",
	VALUE_NOT_CLASS = "bad argument #%{pos} to %q{name} (value of type %{type} (%q{value}) is not a class)",
	VALUE_NOT_INSTANCE = "bad argument #%{pos} to %q{name} (value of type %{type} (%q{value}) is not a class instance)",
	VALUE_NOT_CLASS_OR_INSTANCE = "bad argument #%{pos} to %q{name} (value of type %{type} (%q{value}) is not a class instance or class)",
	VALUE_NOT_CLASS_OR_INSTANCE_OR_PROTO = "Value of type %{type} (%q{value}) is not a class instance or class or a class prototype object",
	INVALID_SELF_OBJECT = "Class method :%{name}() was passed an invalid self object of type %{type} (%q{value}). Did you mean to use ':' instead of '.' to call this method (`:%{name}(...)` instead of `.%{name}(...)`)",
	INVALID_STATIC_SELF_OBJECT = "Static class method :%{name}() was passed an invalid self object of type %{type} (%q{value}). Did you mean to use ':' instead of '.' to call this method (`:%{name}(...)` instead of `.%{name}(...)`)",
	INVALID_PROTO_VALUE = "Cannot reassign the class prototype to a value whose type is not a table, recived a value of type %{type} (%q{value}) instead",
	INVALID_METHOD_ARG_TYPE = "bad argument #%{pos} to class method %q{name} (%{expected} expected, got %{type})",
	VALUE_EXPECTED = "bad argument #%{pos} to class method %q{name} (value expected)",
	INVALID_STATIC_METHOD_ARG_TYPE = "bad argument #%{pos} to static class method %q{name} (%{expected} expected, got %{type})",
	VALUE_EXPECTED_STATIC = "bad argument #%{pos} to static class method %q{name} (value expected)",
	INVAID_ARG_TYPE = "bad argument #%{pos} to %q{name} (%{expected} expected, got %{type})",
	INVALID_CONSTRUCTOR_VALUE = "Cannot set property 'constructor' to a value which is not a function",
}

-- Global list of classes
local classRegistry = setmetatable({}, { __mode="k" })
local instanceRegistry = setmetatable({}, { __mode="k" })
local prototypeRegistry = setmetatable({}, { __mode="k" })
---------------------------------------------------------------------------------
-- Helper functions
---------------------------------------------------------------------------------
-- Pack values
function helpers.pack(...)
	local n = select("#", ...)

	return { n = n, ... };
end

local function noop() end

function helpers.safetostring(v)
	local _, res = xpcall(function()
		return tostring(v)
	end, function()
		if p.isClass(v) then
			return "class"
		elseif p.isInstance(v) then
			return "class instance"
		elseif p.isPrototype(v) then
			return "class prototype"
		else
			return type(v)
		end
	end)

	return res
end

-- interpolate a formatted string, syntax is the same as `string.format(...)` except items are annotated with `%<format options>{<tableKey>}`
-- ex: helpers.interpolate("%q{test}", { test="Test1" }) -> "\"Test1\""
function helpers.interpolate(s, substutions)
	local items = {}
	local i = 0

	s = s:gsub('(%%([%d%.%#+%-]*)(%w?)%b{})', function(w, options, substutionType)
		i = i + 1
		local start, stop = 3 + (#(options .. substutionType)), -2
		tinsert(items, substutions[w:sub(start, stop)] or error("Missing interpolation parameter '" .. w:sub(start, stop) .. "'", 4))

		return "%" .. (substutionType ~= "" and substutionType or "s")
	end)

	return sformat(s, unpack(items, 1, i))
end

-- Bind a `self` value to a function
-- If in Debug mode, forbid tail call optimizations as that will obfuscate the function name in error stacks
if _DEBUG then
	function helpers.proxy(t, func)
		return function(...)
			local res = helpers.pack(({ ["<class internals>"] = func })["<class internals>"](t, ...))

			if t then return unpack(res, 1, res.n) end
		end
	end
else
	function helpers.proxy(t, func)
		return function(...)
			return func(t, ...)
		end
	end
end

-- Get table keys
function helpers.tableKeys(t)
	local ret = {}

	for k in pairs(t) do
		tinsert(ret, k)
	end

	return ret
end

-- Merge keys into table
function helpers.merge(t1, ...)
	if select('#', ...) > 1 then
		for _, t in ipairs{ ... } do
			for k, v in pairs(t) do
				t1[k] = v
			end
		end
	else
		for k, v in pairs(...) do
			t1[k] = v
		end
	end

	return t1
end

function helpers.clearTable(t)
	for k in pairs(t) do
		t[k] = nil
	end

	return t
end

function helpers.getMethodName(level)
	local methodName = mw.text.split(debug.traceback(), "\n")[(level or 0) + 3]:match("in function [\'\"](.-)[\'\"]")

	return methodName
end

function helpers.getName(value)
	local s

	if p.isInstance(value) then s = 'instance of class "' .. debug.getNameOf(value) .. '"'
	elseif p.isPrototype(value) then s = 'prototype of class "' .. debug.getNameOf(value) .. '"'
	elseif p.isClass(value) then s = 'class "' .. debug.getNameOf(value) .. '"' 
	else s = type(value) .. ' ("' .. helpers.safetostring(value) .. '")'
	end
	
	return s
end

-- Function to create a child class form a given parent
function helpers.createChildClass(parent, classData)
	helpers.assertStaticSelf(parent)
	classData = classData or {}
	
	if type(classData) == 'string' then
		return function(data)
			data = data or {}
			
			data.parent = parent
			data.__metadata = data.__metadata or {}
			data.__metadata.name = classData
			
			return p.makeClass(data)
		end
	else
		classData.parent = parent
		return p.makeClass(classData)
	end
end
---------------------------------------------------------------------------------
-- Assertion utilities
---------------------------------------------------------------------------------
function helpers.assertIsClass(v, pos)
	if not p.isClass(v) then error(helpers.interpolate(MESSAGES.VALUE_NOT_CLASS, { value = v ~= nil and helpers.safetostring(v) or "nil", type = type(v), pos = pos or 1, name = helpers.getMethodName(1) }), 3) end

	return v
end

function helpers.assertIsInstance(v, pos)
	if not p.isInstance(v) then error(helpers.interpolate(MESSAGES.VALUE_NOT_INSTANCE, { value = v ~= nil and helpers.safetostring(v) or "nil", type = type(v), pos = pos or 1, name = helpers.getMethodName(1) }), 3) end

	return v
end

function helpers.assertIsInstanceOrClass(v, pos)
	if not p.isInstance(v) and not p.isClass(v) then error(helpers.interpolate(MESSAGES.VALUE_NOT_CLASS_OR_INSTANCE, { value = v ~= nil and helpers.safetostring(v) or "nil", type = type(v), pos = pos or 1, name = helpers.getMethodName(1) }), 3) end

	return v
end

function helpers.assertIsInstanceOrClassOrProto(v, pos)
	if not p.isInstance(v) and not p.isClass(v) and not p.isPrototype(v) then error(helpers.interpolate(MESSAGES.VALUE_NOT_CLASS_OR_INSTANCE_OR_PROTO, { value = v ~= nil and helpers.safetostring(v) or "nil", type = type(v), pos = pos or 1, name = helpers.getMethodName(1) }), 3) end

	return v
end

function helpers.assertStaticSelf(v)
	if not p.isClass(v) then error(helpers.interpolate(MESSAGES.INVALID_STATIC_SELF_OBJECT, { name = helpers.getMethodName(1), value = helpers.safetostring(v), type = type(v) }), 3) end

	return v
end

---------------------------------------------------------------------------------
-- functions used inside of interals
---------------------------------------------------------------------------------
function helpers.defaultConstructor(self)
	return self
end

function helpers.defaultInheritedConstructor(self, ...)
	self:super(...)

	return self
end

function helpers.invalidSuperCall()
	error(MESSAGES.INVALID_SUPER_CALL, 2)
end

function helpers.ipairsFunc(t, i)
	i = i + 1

	local v = t[i]
	if v ~= nil then return i, v end
end

local oldLog = mw.log
---------------------------------------------------------------------------------
-- Overwrite mw.dumpObject to accept classes
---------------------------------------------------------------------------------
function mw.dumpObject(object)
	local doneTable = {}
	local doneObj = {}
	local ct = {}
	local function sorter(a, b)
		local ta, tb = type(a), type(b)
		if ta ~= tb then
			return ta < tb
		end
		if ta == 'string' or ta == 'number' then
			return a < b
		end
		if ta == 'boolean' then
			return tostring(a) < tostring(b)
		end
		return false -- Incomparable
	end
	local function _dumpObject(object, indent, expandTable)
		local tp = type(object)
		if tp == 'number' or tp == 'nil' or tp == 'boolean' then
			return tostring(object)
		elseif tp == 'string' then
			return string.format("%q", object)
		elseif tp == 'table' then
			local s = helpers.safetostring(object)

			if not doneObj[object] then
				if s == 'table' or classRegistry[object] or instanceRegistry[object] or prototypeRegistry[object] then
					if classRegistry[object] then s = 'class(' .. object.__metadata__.name .. ')'
					elseif instanceRegistry[object] then s = 'class instance('  .. object.__class__.__metadata__.name .. ')'
					elseif prototypeRegistry[object] then s = 'class prototype(' .. object.__holdingClass__.__metadata__.name .. ')'
					end

					ct[tp] = (ct[tp] or 0) + 1
					doneObj[object] = s .. '#' .. ct[tp]
				else
					doneObj[object] = s
					doneTable[object] = true
				end
			end
			if doneTable[object] or not expandTable then
				return doneObj[object]
			end
			doneTable[object] = true

			local ret = { doneObj[object], ' {\n' }
			local mt = getmetatable(object)
			if mt then
				ret[#ret + 1] = string.rep(" ", indent + 2)
				ret[#ret + 1] = 'metatable = '
				ret[#ret + 1] = _dumpObject(mt, indent + 2, false)
				ret[#ret + 1] = "\n"
			end

			local doneKeys = {}
			for key, value in ipairs(object) do
				doneKeys[key] = true
				ret[#ret + 1] = string.rep(" ", indent + 2)
				ret[#ret + 1] = _dumpObject(value, indent + 2, true)
				ret[#ret + 1] = ',\n'
			end
			local keys = {}
			for key in pairs(object) do
				if not doneKeys[key] then
					keys[#keys + 1] = key
				end
			end
			table.sort(keys, sorter)
			for i = 1, #keys do
				local key = keys[i]
				ret[#ret + 1] = string.rep(" ", indent + 2)
				ret[#ret + 1] = '['
				ret[#ret + 1] = _dumpObject(key, indent + 3, false)
				ret[#ret + 1] = '] = '
				ret[#ret + 1] = _dumpObject(object[key], indent + 2, true)
				ret[#ret + 1] = ",\n"
			end

			if p.isClass(object) or p.isPrototype(object) or p.isInstance(object) then
				local proto = object.__proto__

				if proto then
					ret[#ret + 1] = string.rep(" ", indent + 2)
					ret[#ret + 1] = '(Prototype) = '
					ret[#ret + 1] = _dumpObject(object.__proto__, indent + 2, true)
					ret[#ret + 1] = ",\n"
				end
			end

			ret[#ret + 1] = string.rep(" ", indent)
			ret[#ret + 1] = '}'

			return table.concat(ret)
		else
			if not doneObj[object] then
				ct[tp] = (ct[tp] or 0) + 1
				doneObj[object] = tostring(object) .. '#' .. ct[tp]
			end
			return doneObj[object]
		end
	end
	return _dumpObject(object, 0, true)
end

function mw.logObject(v, prefix)
	mw.log((prefix and prefix .. " " or "") .. mw.dumpObject(v))
end
p.dump = mw.dumpObject
p.dumpObject = mw.dumpObject
p.log = mw.logObject
p.logObject = mw.logObject

---------------------------------------------------------------------------------
-- Internal Data
---------------------------------------------------------------------------------
local metaProperties = {
	['__index'] = 1,
	['__newindex'] = 1,
	['__mode'] = 1,
	['__tostring'] = 1,
	['__concat'] = 1,
	['__metatable'] = 1,
	['__ipairs'] = 1,
	['__pairs'] = 1,
	['__pow'] = 1,
	['__add'] = 1,
	['__sub'] = 1,
	['__div'] = 1,
	['__mul'] = 1,
	['__unm'] = 1,
	['__eq'] = 1,
	['__lt'] = 1,
	['__le'] = 1,
}

-- TODO: Maybe add custom metamethods?
local customStaticMetaProperties = {
	['__getter'] = 1,
	['__setter'] = 1,
}

local customMetaProperties = {
	['__getter'] = 1,
	['__setter'] = 1,
	['__protoIndex'] = 1,
}

-- Properties that maybe added directly to the metatable without need for further modificiation
local contextSafeProperties = {
	['__tostring'] = 1,
	['__pairs'] = 1,
	['__ipairs'] = 1,
	["__unm"] = 1,
}

-- Relational operators
local relationalOperators = {
	['__add'] = 1,
	['__sub'] = 1,
	['__div'] = 1,
	['__mul'] = 1,
	['__pow'] = 1,
	['__le'] = 1,
	['__lt'] = 1,
	['__concat'] = 1,
}

local reservedProps = {
	["super"] = 1,
	["__proto__"] = 1,
	['__getters__'] = 1,
	['__setters__'] = 1,
	['__parent__'] = 1,
	['__class__'] = 1,
	['__static__'] = 1,
	['__metadata__'] = 1,
}

local reservedProtoProps = {
	['__proto__'] = 1,
	['__holdingClass__'] = 1,
	['__getters__'] = 1,
	['__setters__'] = 1,
	['__parent__'] = 1,
}

local reservedStaticProps = {
	['__parent__'] = 1,
	['__proto__'] = 1,
	['__setters__'] = 1,
	['__getters__'] = 1,
	['__children__'] = 1,
	['__parents__'] = 1,
	['__metadata__'] = 1,
	['constructor'] = 1,
	['super'] = 1,
	['childClass'] = 1,
}

---------------------------------------------------------------------------------
-- Class structure
--
-- Static class
--  * Static metatable
--	* Static Parent metatable
--  * Class prototype
--	* Class prototype metatable
-- * Class instance
--  * Class instance metatable
-- * Parent class (repeat above)
---------------------------------------------------------------------------------
function helpers:overwriteProto(t, isOverwriting)
	if isOverwriting and #helpers.tableKeys(self.__prototype) > 0 then
		helpers.clearTable(self.__prototype)
		helpers.clearTable(self.__classGetters)
		helpers.clearTable(self.__classSetters)
		helpers.clearTable(self.__classMetamethods)
	end

	for k, v in pairs(t) do
		if k ~= 'constructor' then self.__protoMt.__fakeTable[k] = v
		elseif k == 'constructor' then 
			if type(v) == 'function' then
				self.__origConstructor = v
			else
				error(helpers.interpolate(MESSAGES.INVALID_CONSTRUCTOR_VALUE), 2)
			end
		end
	end
end

function helpers.parseAccessorTable(k, v, setters, getters, len, static)
	static = static ~= false

	len = len or #helpers.tableKeys(v)
	local get = v.get
	local set = v.set
	if len > 0 and len <= 2 and (set or get) then
		if set ~= nil then
			if type(set) == "function" then
				setters[k] = set
			else
				return helpers.interpolate(
					static and MESSAGES.INVALID_STATIC_CLASS_ACCESSOR or MESSAGES.INVALID_CLASS_ACCESSOR,
					{ accessor = "setter", property = k, type = type(set), value = set }
				)
			end
		end
		if get ~= nil then
			if type(get) == "function" then
				getters[k] = get
			else
				return helpers.interpolate(
					static and MESSAGES.INVALID_STATIC_CLASS_ACCESSOR or MESSAGES.INVALID_CLASS_ACCESSOR,
					{ accessor = "getter", property = k, type = type(get), value = get }
				)
			end
		end
	end
end

---------------------------------------------------------------------------------
-- Class metatable methods
---------------------------------------------------------------------------------
function classMtFuncs.__index(t, k)
	local self = instanceRegistry[t]
	local staticMt = self.__staticMt

	if k == 'super' then return self.__super end		
	if reservedProps[k] then
		if k == '__getters__' then return staticMt.__classGetters
		elseif k == '__setters__' then return staticMt.__classSetters
		elseif k == '__static__'
		or k == '__class__' then return staticMt.__class 
		elseif k == '__proto__' then return staticMt.__protoMt.__fakeTable
		elseif k == '__parent__' then return staticMt.__parentStaticMt.__class
		end
	end
	
	local __index = staticMt.__classMetamethods.__index
	local protoProp = staticMt.__prototype[k]
	local getter = staticMt.__classGetters[k]

	-- If requested value does not exist in current prototype, repeat same step on parent prototypes
	if staticMt.__hasParent and protoProp == nil and getter == nil then
		local cur = staticMt.__parentStaticMt
		local curGetters = cur.__classGetters
		local curProto = cur.__prototype

		while cur do
			local value = curProto[k]
			local foundGetter = curGetters[k]

			if foundGetter ~= nil then
				getter = foundGetter
				break
			elseif value ~= nil then
				protoProp = value
				break
			end

			if not cur.__parentStaticMt then
				break
			end

			cur = cur.__parentStaticMt
			curProto = cur.__prototype
			curGetters = cur.__classGetters
		end
	end

	if getter ~= nil then
		-- If in Debug mode, forbid tail call optimizations as that will obfuscate the function name in error stacks
		if _DEBUG then
			local res = helpers.pack(({ ["<class getter>"] = getter })["<class getter>"](t))

			if getter then return unpack(res, 1, res.n) end
		else
			return getter(t)
		end
	end

	if protoProp ~= nil then
		return protoProp
	else
		if __index then
			-- If in Debug mode, forbid tail call optimizations as that will obfuscate the function name in error stack
			if _DEBUG then
				local res = helpers.pack(__index(t, k))
	
				if self then return unpack(res, 1, res.n) end
			else
				return __index(t, k)
			end
		end

		return nil
	end
end

function classMtFuncs.__newindex(t, k, v)
	if reservedProps[k] then error(helpers.interpolate(MESSAGES.CLASS_FIELD_RESERVED, { property = k }), 2) end

	local self = instanceRegistry[t]
	local staticMt = self.__staticMt
	local setter = staticMt.__classSetters[k]
	local getter = staticMt.__classGetters[k]
	local __newindex = staticMt.__classMetamethods.__newindex 

	-- Search for setter on parent classes
	if staticMt.__hasParent and setter == nil then
		local cur = staticMt.__parentStaticMt
		local curSetters = cur.__classSetters
		local curGetters = cur.__classGetters
		local curProto = cur.__prototype

		while cur do
			local foundSetter = curSetters[k]
			getter = curGetters[k]

			if foundSetter ~= nil then
				setter = foundSetter
				break
			end

			curProto = cur.__prototype
			curSetters = cur.__classSetters
			cur = cur.__parentStaticMt
		end
	end
	
	if getter and not setter then
		error(helpers.interpolate(MESSAGES.GETTER_ONLY_ASSIGNMENT, { property = k }), 3)
	elseif setter ~= nil then
		-- If in Debug mode, forbid tail call optimizations as that will obfuscate the function name in error stacks
		if _DEBUG then
			local res = helpers.pack(({ ["<class setter>"] = setter })["<class setter>"](t, v))

			if setter then return unpack(res, 1, res.n) end
		else
			return setter(t, v)
		end
	else
		if __newindex then
			-- If in Debug mode, forbid tail call optimizations as that will obfuscate the function name in error stacks
			if _DEBUG then
				local res = helpers.pack(__newindex(t, k, v))
	
				if self then return unpack(res, 1, res.n) end
			else
				return __newindex(t, k, v)
			end
		end

		return rawset(t, k, v)
	end
end

-- Override default pairs(), invoke class getters in the process
function classMtFuncs.__pairs(t)
	local self = instanceRegistry[t]
	local staticMt = self.__staticMt
	local getters = helpers.tableKeys(staticMt.__classGetters)
	local i = 0
	local onGetters = false
	local __pairs = staticMt.__classMetamethods.__pairs

	if __pairs then
		-- If in Debug mode, forbid tail call optimizations as that will obfuscate the function name in error stacks
		if _DEBUG then
			local res = helpers.pack(__pairs(t, k, v))

			if self then return unpack(res, 1, res.n) end
		else
			return __pairs(t, k, v)
		end
	end

	return function(t, k1)
		local k, v

		if not onGetters then
			k, v = next(t, k1)
		end

		-- Insert getters into results
		if k == nil then
			onGetters = true
			i = i + 1

			k, v = getters[i], t[getters[i]]
		end

		if k == nil then
			return nil, nil
		else
			return k, v
		end
	end, t, nil
end

function classMtFuncs.__ipairs(t)
	local self = instanceRegistry[t]
	local __ipairs = self.__staticMt.__classMetamethods.__ipairs

	if __ipairs then
		-- If in Debug mode, forbid tail call optimizations as that will obfuscate the function name in error stacks
		if _DEBUG then
			local res = helpers.pack(__ipairs(t, k, v))

			if self then return unpack(res, 1, res.n) end
		else
			return __ipairs(t, k, v)
		end
	end

	return function(t, i)
		i = i + 1

		local v = t[i]
		if v ~= nil then return i, v end
	end, t, 0
end


function classMtFuncs.__tostring(t)
	local self = instanceRegistry[t]
	local __tostring = self.__staticMt.__classMetamethods.__tostring

	if __tostring then
		-- If in Debug mode, forbid tail call optimizations as that will obfuscate the function name in error stacks
		if _DEBUG then
			local res = helpers.pack(__tostring(t, k, v))

			if self then return unpack(res, 1, res.n) end
		else
			return __tostring(t, k, v)
		end
	end


	return "class instance"
end

---------------------------------------------------------------------------------
-- Static class metamethods
---------------------------------------------------------------------------------
-- Construct class metadatatable
function helpers.createClassMt(staticMt)
	local classMt = {
		__staticMt = staticMt,
	}

	classMt.__metatable = { "instance metatable" }

	-- Set metamethods
	for k, v in pairs(classMtFuncs) do
		classMt[k] = v
	end

	return classMt
end

-- Called when actually constructing the class
function staticMtFuncs.__call(t, ...)
	local created = {}
	local self = classRegistry[t] or (instanceRegistry[t] and instanceRegistry[t].__staticMt) or error(helpers.interpolate(MESSAGES.INVALID_SELF_OBJECT, { name = helpers.getMethodName(), value = helpers.safetostring(t), type = type(t) }), 2)
	local classMt = helpers.createClassMt(self)
	local superCalled = false
	local done = false

	setmetatable(created, classMt)

	instanceRegistry[created] = classMt

	-- Set class properties
	for k, v in pairs(self.__initProps) do
		rawset(created, k, v)
	end

	-- set class metamethods
	for k, v in pairs(self.__classMetamethods) do
		if contextSafeProperties[k] or k == '__eq' or k == '__metatable' then
			classMt[k] = v
		elseif relationalOperators[k] then
			classMt[k] = v
		end
	end

	local i = 0
	local len = #self.__parents

	classMt.__constructorArgs = helpers.pack(...)

	-- TODO: Add super indexing support
	if self.__parentStaticMt then
		local curParent = self.__parents[1]

		local function superFunc(...)
			i = i + 1
			local passedSelf = ({ ... })[1]
			if not instanceRegistry[passedSelf] then error(MESSAGES.INVAID_SELF_SUPER, 2) end

			curParent = classRegistry[self.__parents[i]] or error(MESSAGES.INVALID_SUPER_CALL, 2)
			local constructor = curParent.__origConstructor
			
			local res = helpers.pack(constructor(...));
			
			if (res.n == 0 or res.n == 1) and res[1] ~= passedSelf then
				return passedSelf
			elseif res.n > 1 then
				if res[1] == nil then res[1] = passedSelf end
				
				return unpack(res, 1, res.n)
			else
				return passedSelf
			end
		end

		-- .super() is returned via `__index`
		classMt.__super = superFunc
	else
		classMt.__super = helpers.invalidSuperCall
	end
	local constructor = self.__origConstructor
	assert(constructor ~= staticMtFuncs.__call)
	local ret = helpers.pack(constructor(created, ...))

	if self.__parentStaticMt and i ~= len then
		error(MESSAGES.MUST_CALL_SUPER, 3);
	end

	if (ret.n == 0 or ret.n == 1) and ret[1] ~= created then
		return created
	elseif ret.n > 1 then
		if ret[1] ~= created then ret[1] = created end
		
		return unpack(ret, 1, ret.n)
	else
		return created
	end
end

function staticMtFuncs.__newindex(t, k, v)
	local self = classRegistry[t]
	if reservedStaticProps[k] then error(helpers.interpolate(MESSAGES.STATIC_CLASS_FIELD_RESERVED, { property = k }), 2) end

	-- If key is to Overwrite the prototype, clear any residual prototype keys and reset from new table
	if k == 'prototype' then
		if type(v) == 'table' then
			helpers.overwriteProto(self, v, true)

			return self.__protoMt.__fakeTable
		else
			error(helpers.interpolate(MESSAGES.INVALID_PROTO_VALUE, { type = type(v), value = helpers.safetostring(v) }), 2)
		end
	end

	local setter = self.__staticSetters[k]
	local __newindex = self.__staticMetamethods.__newindex

	-- Search for setter in parent classes
	if self.__hasParent and setter == nil then
		local cur = self.__parentStaticMt
		local curSetters = cur.__staticSetters
		local curGetters = cur.__staticGetters
		local curProto = cur.__prototype

		while cur do
			local foundSetter = curSetters[k]
			local foundGetter = curGetters[k]

			if foundSetter ~= nil or foundGetter ~= nil then
				setter = foundSetter
				getter = foundGetter
				break
			end

			cur = cur.__parentStaticMt

			if not cur then break end
			curProto = cur.__prototype
			curSetters = cur.__staticSetters
		end
	end

	-- If getter but not setter exists raise exception
	if getter and not setter then
		error(helpers.interpolate(MESSAGES.GETTER_ONLY_STATIC_ASSIGNMENT, { property = k }) , 3)
	elseif setter ~= nil then
		-- If in Debug mode, forbid tail call optimizations as that will obfuscate the function name in error stacks
		if _DEBUG then
			local res = helpers.pack(({ ["<static class setter>"] = setter })["<static class setter>"](t, v))
	
			if setter then return unpack(res, 1, res.n) end
		else
			return setter(t, v)
		end
	else
		if __newindex then
			-- If in Debug mode, forbid tail call optimizations as that will obfuscate the function name in error stacks
			if _DEBUG then
				local res = helpers.pack(__newindex(t))	
				
				if self then return unpack(res, 1, res.n) end
			else
				return __newindex(t)
			end
		end

		return rawset(t, k, v)
	end
end

function staticMtFuncs.__index(t, k)
	if util[k] then return util[k] end

	local self = classRegistry[t]

	if self.__indexDefaults[k] then return self.__indexDefaults[k] end

	local getter = self.__staticGetters[k]
	local value = rawget(t, k)
	local __index = self.__staticMetamethods.__index

	-- Search for getter/prototype property on parents
	if self.__hasParent and getter == nil and value == nil then
		local cur = self.__parentStaticMt
		local curGetters = cur.__staticGetters
		local curProto = cur.__prototype

		while cur do
			local foundGetter = curGetters[k]
			local foundValue = rawget(cur.__class, k)
			
			if foundValue ~= nil then
				value = foundValue
				break
			elseif foundGetter ~= nil then
				getter = foundGetter
				break
			end

			cur = cur.__parentStaticMt

			if not cur then break end
			curProto = cur.__prototype
			curGetters = cur.__staticGetters
		end
	end

	if getter ~= nil then
		-- If in Debug mode, forbid tail call optimizations as that will obfuscate the function name in error stacks
		if _DEBUG then
			local res = helpers.pack(({ ["<static class getter>"] = getter })["<static class getter>"](t))
	
			if getter then return unpack(res, 1, res.n) end
		else
			return getter(t)
		end
	else
		if __index then
			-- If in Debug mode, forbid tail call optimizations as that will obfuscate the function name in error stacks
			if _DEBUG then
				local res = helpers.pack(__index(t))	
				
				if self then return unpack(res, 1, res.n) end
			else
				return __index(t)
			end
		end

		return value
	end
end

function staticMtFuncs.__pairs(t)
	local self = classRegistry[t]
	local __pairs = self.__staticMetamethods.__pairs

	if __pairs then
		-- If in Debug mode, forbid tail call optimizations as that will obfuscate the function name in error stacks
		if _DEBUG then
			local res = helpers.pack(__pairs(t))	
			
			if self then return unpack(res, 1, res.n) end
		else
			return __pairs(t)
		end
	end

	local getters = helpers.tableKeys(self.__staticGetters)
	local i = 0
	local onGetters = false
	local protoDone = false

	return function(t, k1)
		local k, v

		-- Insert prototype into results
		if k1 == 'prototype' and not protoDone then
			protoDone = true
			return 'prototype', self.__protoMt.__fakeTable
		end

		if not onGetters then
			k, v = next(t, k1 ~= 'prototype' and k1 or nil)
		end

		-- Insert getters into results
		if k == nil then
			onGetters = true
			i = i + 1

			k, v = getters[i], t[getters[i]]
		end

		if k == nil then
			return nil, nil
		else
			return k, v
		end
	end, t, 'prototype'
end


function staticMtFuncs.__ipairs(t)
	local self = classRegistry[t]
	local __ipairs = self.__staticMetamethods.__ipairs

	if __ipairs then
		-- If in Debug mode, forbid tail call optimizations as that will obfuscate the function name in error stacks
		if _DEBUG then
			local res = helpers.pack(__ipairs(t))	
			
			if self then return unpack(res, 1, res.n) end
		else
			return __ipairs(t)
		end
	end

	return helpers.ipairsFunc, t, 0
end

function staticMtFuncs.__tostring(t)
	local self = classRegistry[t]
	local __tostring = self.__staticMetamethods.__tostring

	if __tostring then
		-- If in Debug mode, forbid tail call optimizations as that will obfuscate the function name in error stacks
		if _DEBUG then
			local res = helpers.pack(__tostring(t))	
			
			if self then return unpack(res, 1, res.n) end
		else
			return __tostring(t)
		end
	end

	return "class"
end

---------------------------------------------------------------------------------
-- Prototype metamethods
---------------------------------------------------------------------------------
function protoMtFuncs.__pairs(t)
	local self = prototypeRegistry[t]

	return function(t, k)
		local nextKey, value = next(self.__prototype, k);

		return nextKey, value
	end, self.__fakeTable, nil
end

function protoMtFuncs.__ipairs(t)
	return helpers.ipairsFunc, prototypeRegistry[t], 0
end

function protoMtFuncs.__newindex(t, k, v)
	local self = prototypeRegistry[t]
	local tp = type(v)

	if reservedProtoProps[k] then error(helpers.interpolate(MESSAGES.PROTO_FIELD_RESERVED, { property = k })) end
	if k == 'constructor' and tp == 'function' then
		-- Overwrite constructor
		local oldConstructor = self.__staticMt.__origConstructor
		local newConstructor = v

		self.__staticMt.__origConstructor = newConstructor or oldConstructor

		return self.__fakeTable
	elseif k == 'constructor' and tp ~= 'function' then
		error(helpers.interpolate(MESSAGES.INVALID_CONSTRUCTOR_VALUE))
	elseif tp == 'table' and next(v) ~= nil and k ~= '__metatable' then
		local err = helpers.parseAccessorTable(k, v, self.__staticMt.__classSetters, self.__staticMt.__classGetters, nil, false)

		if err then error(err, 2) end
		return
	else
		if metaProperties[k] then
			self.__staticMt.__classMetamethods[k] = v
		end
	end
	self.__prototype[k] = v
	
	return self.__fakeTable
end

function protoMtFuncs.__index(t, k)
	local self = prototypeRegistry[t]
	if self.__indexDefaults[k] then return self.__indexDefaults[k] end

	local value = self.__prototype[k]
	
	if value == nil then
		local parent = self.__parentMt
	
		while parent do
			local foundValue = parent.__prototype[k]

			if foundValue ~= nil then
				value = foundValue
				break 
			end
						
			parent = parent.__parentMt
		end
	end
	
	return value
end

function protoMtFuncs.__tostring()
	return "class prototype"
end

---------------------------------------------------------------------------------
-- Utilies, exposed on the static class
---------------------------------------------------------------------------------
function util:checkSelf(value, name)
	if not classRegistry[self] then error(helpers.interpolate(MESSAGES.INVALID_STATIC_SELF_OBJECT, { name = helpers.getMethodName(-1), value = helpers.safetostring(self), type = type(self) }), 2) end 

	if not self:instanceof(value) then
		local methodName = name or helpers.getMethodName(1)

		error(helpers.interpolate(MESSAGES.INVALID_SELF_OBJECT, { name = methodName, value = helpers.safetostring(value), type = type(value) }), 3)
	end

	return self
end

function util:checkSelfStatic(value, name)
	if not classRegistry[self] then error(helpers.interpolate(MESSAGES.INVALID_STATIC_SELF_OBJECT, { name = helpers.getMethodName(-1), value = helpers.safetostring(self), type = type(self) }), 2) end

	if not self:isChildOrEqual(value) then
		local methodName = name or mw.text.split(debug.traceback(), "\n")[3]:match("in function [\'\"](.-)[\'\"]")

		error(helpers.interpolate(MESSAGES.INVALID_STATIC_SELF_OBJECT, { name = methodName, value = helpers.safetostring(value), type = type(value) }), 3)
	end

	return self
end

function util:isChildOrEqual(value)
	if not classRegistry[self] then error(helpers.interpolate(MESSAGES.INVALID_STATIC_SELF_OBJECT, { name = helpers.getMethodName(-1), value = helpers.safetostring(self), type = type(self) }), 2) end

	local cr = classRegistry[value]
	if not cr then return false end
	if value == self then return true end	
	
	local i = 1
	local parents = cr.__parents
	local class = parents[i]

	while class do
		if class == self then return true end

		i = i + 1
		class = parents[i]
	end
	
	return false
end

-- Check if value is an instance of class
function util:instanceof(value)
	if not classRegistry[self] then error(helpers.interpolate(MESSAGES.INVALID_STATIC_SELF_OBJECT, { name = helpers.getMethodName(-1), value = helpers.safetostring(self), type = type(self) }), 2) end
	if not instanceRegistry[value] then return false end

	local class = value.__class__
	local parents = classRegistry[class].__parents

	if class == self then return true end

	local i = 1
	local parent = parents[i]

	while parent do
		if parent == self then return true end

		i = i + 1
		parent = parents[i]
	end

	return false
end

-- Check types of method arguments
function util:checkTypes(types, ...)
	if not classRegistry[self] then error(helpers.interpolate(MESSAGES.INVALID_STATIC_SELF_OBJECT, { name = helpers.getMethodName(-1), value = helpers.safetostring(self), type = type(self) }), 2) end

	local max = #types
	local values = helpers.pack(...)
	local i = 1
	local value = values[1]
	-- Rename error function to get proper name in stack
	local checkTypes = error

	while i <= max do
		local valueType = type(value)
		local targetType = types[i]

		if i > values.n then 
			checkTypes(helpers.interpolate(MESSAGES.INVALID_METHOD_ARG_TYPE, { name = helpers.getMethodName(1), type = "no value", pos = i, expected = helpers.getName(targetType) }), 3)
		end

		if p.isClass(targetType) then
			if not targetType:instanceof(value) then
				checkTypes(helpers.interpolate(MESSAGES.INVALID_METHOD_ARG_TYPE, { 
					name = helpers.getMethodName(1), 
					pos = i, 
					value = helpers.safetostring(value), 
					type = valueType, 
					expected = helpers.getName(targetType) 
				}), 3)
			end
		else
			if valueType ~= targetType then
				checkTypes(helpers.interpolate(MESSAGES.INVALID_METHOD_ARG_TYPE, { 
					name = helpers.getMethodName(1),
					pos = i,
					value = helpers.safetostring(value),
					type = helpers.getName(value),
					expected = targetType 
				}), 3)
			end
		end

		i = i + 1
		value = values[i]
	end

	return ...
end

---------------------------------------------------------------------------------
-- Package exports
---------------------------------------------------------------------------------
function p.isClass(v)
	return classRegistry[v] ~= nil
end

function p.isInstance(v)
	return instanceRegistry[v] ~= nil
end

function p.isPrototype(v)
	return prototypeRegistry[v] ~= nil
end

function p.makeClass(...)
	local args = { ... }
	local name, data

	if type(args[1]) == 'string' then
		data = args[2]
		name = args[1]
	else
		data = args[1]
	end

	data = data or {}

	if type(data) ~= 'table' then error(string.format('Argument #1 must be a table or a string (class name) or nil, recived %q instead', type(data)), 2) end
	if type(data) ~= 'table' then error(string.format('Argument #2 must be a table or nil, recived %q instead', type(data)), 2) end

	local parentClass = data.parentClass or data.parent
	local constructor = data.constructor or (parentClass and helpers.defaultInheritedConstructor or helpers.defaultConstructor)
	local staticData = data.static or {}
	local metadata = data.__metadata or {}
	local classFields = data.class or {}

	if type(staticData) ~= 'table' then error(helpers.interpolate(MESSAGES.STATIC_PROPERTIES_TYPE, { type = type(staticData) }), 2) end
	if type(classFields) ~= 'table' then error(helpers.interpolate(MESSAGES.PROPERTIES_TYPE, { type = type(classFields) }), 2) end

	local staticMt = {}

	local Class = {}
	local prototype = data.prototype or {}
	local initProps = {}

	local setters, getters = {}, {}

	classCount = classCount + 1

	if not classRegistry[parentClass] and parentClass ~= nil then
		error(MESSAGES.INVALID_PARENT_CLASS, 2)
	end

	-- Setup metadata
	metadata.name = name or metadata.name or "unnamed class " .. classCount
	metadata.id = classCount

	---------------------------------------------------------------------------------
	-- Set up static metatable
	---------------------------------------------------------------------------------
	helpers.merge(staticMt, {
		__prototype = prototype,
		__class = Class,
		__initProps = initProps,
		__origConstructor = constructor,

		__classSetters = setters,
		__classGetters = getters,
		__staticSetters = {},
		__staticGetters = {},
		__staticMetamethods = {},

		__parentClass = parentClass,
		__parentStaticMt = parentClass and classRegistry[parentClass],

		__isInstance = false,
		__hasParent = not not parentClass,
		__classMetamethods = {},
		__parents = setmetatable({}, { __mode = "v" }),
		__childClasses = setmetatable({}, { __mode = "v" }),
	});

	helpers.merge(staticMt, staticMtFuncs)

	---------------------------------------------------------------------------------
	-- Set static/class methods
	---------------------------------------------------------------------------------
	for k, v in pairs(data) do
		if k ~= 'constructor'
		and k ~= 'parent'
		and k ~= 'class'
		and k ~= 'prototype'
		and k ~= '__metadata'
		and k ~= 'static' then
			local tp = type(v)
			if tp == 'function' then
				rawset(prototype, k, v)
				if metaProperties[k] then
					staticMt.__classMetamethods[k] = v
				end
			elseif tp == 'table' then
				local len = #helpers.tableKeys(v)

				if (len <= 2 and len > 0) and (v.set or v.get) then
					local err = helpers.parseAccessorTable(k, v, staticMt.__classSetters, staticMt.__classGetters, len, false)
					if err then error(err, 2) end
				else
					rawset(initProps, k, v)
				end
			else
				rawset(initProps, k, v)
			end
		end
	end

	if next(classFields) ~= nil then
		for k, v in pairs(classFields) do
			initProps[k] = v
		end
	end

	if next(staticData) ~= nil then
		for k, v in pairs(staticData) do
			if reservedStaticProps[k] then error(helpers.interpolate(MESSAGES.STATIC_CLASS_FIELD_RESERVED, { property = k }), 2) end
			local tp = type(v)

			if tp == 'table' then
				local len = #helpers.tableKeys(v)
				if (len > 0 and len <= 2) and (v.get or v.set) then
					local err = helpers.parseAccessorTable(k, v, staticMt.__staticSetters, staticMt.__staticGetters, len, true)
					if err then error(err, 2) end
				else
					rawset(Class, k, v)
				end
			else
				rawset(Class, k, v)
			end

			if metaProperties[k] and tp == 'function' then
				if contextSafeProperties[k] or relationalOperators[k] or k == '__eq' or k == '__metatable' then
					staticMt[k] = v
				end

				staticMt.__staticMetamethods[k] = v
			-- TODO: Add metatable property verification
			-- elseif metaProperties[k] then
			-- 	error("Metatable properties must be functions.")
			end
		end
	end

	---------------------------------------------------------------------------------
	-- Set up prototype metatable
	---------------------------------------------------------------------------------
	local protoMt = {}
	local fakeProto = {}

	helpers.merge(protoMt, {
		__staticMt = staticMt,
		__class = Class,
		__prototype = staticMt.__prototype,
		__parentMt = staticMt.__hasParent and staticMt.__parentStaticMt.__protoMt or nil,
		__fakeTable = fakeProto,
		__indexDefaults = setmetatable({
			['constructor'] = staticMtFuncs.__call,
			['__setters__'] = staticMt.__classSetters,
			['__getters__'] = staticMt.__classGetters,
			['__proto__'] = staticMt.__hasParent and staticMt.__parentStaticMt.__protoMt.__fakeTable or nil,
			['__holdingClass__'] = staticMt.__class,
			['__parent__'] = staticMt.__hasParent and staticMt.__parentStaticMt.__class,
		}, { __mode = "v" }),
	});

	staticMt.__protoMt = protoMt
	staticMt.__metatable = {
		__isClass = true,
		__isInstance = false,
		__hasParent = staticMt.__hasParent,
		__class = Class,
		__parent = staticMt.__parentClass,
	}
	helpers.overwriteProto(staticMt, prototype, false)

	---------------------------------------------------------------------------------
	-- Set up final metadata for static metatable
	---------------------------------------------------------------------------------
	staticMt.__customMetadata = metadata
	staticMt.__indexDefaults = setmetatable({
		['__parent__'] = staticMt.__parentClass,
		['__proto__'] = staticMt.__parentClass,
		['prototype'] = protoMt.__fakeTable,
		['__setters__'] = staticMt.__staticSetters,
		['__getters__'] = staticMt.__staticGetters,
		['__children__'] = staticMt.__childClasses,
		['__parents__'] = staticMt.__parents,
		['__metadata__'] = staticMt.__customMetadata,
		['constructor'] = staticMtFuncs.__call,
		
		-- Utility methods
		['childClass'] = helpers.createChildClass,
	}, { __mode = "v" })

	-- Set prototype table metamethods
	for k, v in pairs(protoMtFuncs) do
		protoMt[k] = v
	end
	prototypeRegistry[fakeProto] = protoMt

	-- Merge parent initProps into target class and add child class to parent class list
	if parentClass then
		local parentMt = staticMt.__parentStaticMt

		table.insert(classRegistry[parentClass].__childClasses, Class)

		while parentMt do
			tinsert(staticMt.__parents, parentMt.__class)
			helpers.merge(initProps, staticMt.__initProps)

			parentMt = parentMt.__parentStaticMt
		end
	end

	-- Finalize setup
	setmetatable(fakeProto, protoMt)

	classRegistry[Class] = staticMt

	setmetatable(Class, staticMt)
	
	return Class
end
---------------------------------------------------------------------------------
-- Debug functions (Only use for debugging!)
---------------------------------------------------------------------------------
---------------------------------------------------------------------------------
-- Class instance debug functions
---------------------------------------------------------------------------------
function debug.instanceExists(value)
	return not not instanceRegistry[helpers.assertIsInstance(value)]
end

function debug.getInstanceMetatable(instance)
	return instanceRegistry[helpers.assertIsInstance(instance)]
end

function debug.hasInstanceMetamethod(instance, method)
	return not not debug.getInstanceMetamethod(helpers.assertIsInstance(instance), method)
end

function debug.getInstanceMetamethod(instance, method)
	return debug.getInstanceMetatable(helpers.assertIsInstance(instance)).__staticMt.__classMetamethods[method]
end

function debug.getInstanceSetters(instance)
	return helpers.assertIsInstance(instance).__setters__
end

function debug.getInstanceGetters(instance)
	return helpers.assertIsInstance(instance).__getters__
end

---------------------------------------------------------------------------------
-- Class debug functions
---------------------------------------------------------------------------------
function debug.classExists(value)
	return not not classRegistry[helpers.assertIsClass(value)]
end

function debug.getClassMetatable(class)
	return classRegistry[helpers.assertIsClass(class)]
end

function debug.hasClassMetamethod(class, method)
	return not not debug.getClassMetamethod(helpers.assertIsClass(class), method)
end

function debug.getClassMetamethod(class, method)
	return debug.getClassMetatable(helpers.assertIsClass(class)).__staticMetamethods[method]
end

function debug.getClassSetters(class)
	return helpers.assertIsClass(class).__setters__
end

function debug.getClassGetters(class)
	return helpers.assertIsClass(class).__getters__
end

function debug.getClassParents(value)
	return helpers.assertIsClass(value).__parent__
end

function debug.getClassName(class)
	return classRegistry[helpers.assertIsClass(class)].__customMetadata.name
end

function debug.getClassId(class)
	return classRegistry[helpers.assertIsClass(class)].__customMetadata.id
end

function debug.getClassByName(name)
	if type(name) ~= 'string' then error("Argument #1 must be a string", 2) end

	for k, v in pairs(classRegistry) do
		if v.__customMetadata.name == name then return k end	
	end
	
	return nil
end

---------------------------------------------------------------------------------
-- Class prototype functions
---------------------------------------------------------------------------------
function debug.getClassOfPrototype(proto)
	return helpers.assertIsPrototype(proto).__holdingClass__
end

function debug.getPrototypeMetatable(proto)
	return prototypeRegistry[helpers.assertIsPrototype(proto)]
end

function debug.getPrototypeTable(proto)
	return prototypeRegistry[helpers.assertIsPrototype(proto)].__prototype
end

function debug.getPrototypeConstructor(proto)
	return prototypeRegistry[helpers.assertIsPrototype(proto)].__prototype.constructor
end

---------------------------------------------------------------------------------
-- Class/Class instance functions
---------------------------------------------------------------------------------
function debug.getParentOf(value)
	return helpers.assertIsInstanceOrClassOrProto(value).__parent__
end

function debug.getPrototypeOf(value)
	return helpers.assertIsInstanceOrClassOrProto(value).__proto__
end

function debug.getNameOf(value)
	helpers.assertIsInstanceOrClassOrProto(value)
	
	if p.isClass(value) then
		return classRegistry[value].__customMetadata.name
	elseif p.isPrototype(value) then
		return prototypeRegistry[value].__staticMt.__customMetadata.name
	elseif p.isInstance(value) then
		return instanceRegistry[value].__staticMt.__customMetadata.name
	end
	
	error("Invalid program state entered")
end

return setmetatable(p, {
	__call = function(_, ...) return p.makeClass(...) end,
})
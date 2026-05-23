---------------------------------------------------------------------------------
--							Module:Table
--
-- This module includes a number of functions for dealing with Lua tables.
-- It is a meta-module, meant to be called from other Lua modules, and should 
-- not be called directly from {{#invoke:}}.			
--
----------------[ CONTENTS ]-----------------
-- The following list is all the functions this module houses.
--
-- * function: merge(target: table, ...items: any)
-- * function: mergeRight(target: table, ...items: any)
-- * function: mergeNamed(target: table, ...items: any)
-- * function: unpackRaw(t: table)
-- * function: length(t: table)
-- * function: xlength(t: table, countNamed?: boolean, countPositional?: boolean)
-- * function: slice(t: table, startIndex: table, endIndex: table)
-- * function: setPrototype(t: table, proto: table, indexFunc: function)
-- * function: isSequence(t: table)
-- * function: push(t: table, ...items: any)
-- * function: makeReadonlyTable(t: table, realTable: t)
-- * function: unshift(t: table, ...items: any)
-- * function: map(t: table, callbackfn: function(v: any, i?: number, t?: table))
-- * function: mapNamed(t: table, callback: function(v: any, i?: number, t?: table) => any)
-- * function: mapWith(t: table, callback: function(v: any, i?: number, t?: table) => any)
-- * function: filter(t: table, callbackfn: function(v: any, i?: number, t?: table))
-- * function: removeLast(t: table)
-- * function: removeFirst(t: table)
-- * function: flat(t: table)
-- * function: flatMap(t: function, cb: function)
-- * function: Map(items: table)
-- * function: Set(t)
-- * function: find(t: table, compare: any)
-- * function: findIndex(t: table, compare: any)
-- * function: splice(t: table, start: number, deleteCount?: number, ...items: any)
-- * function: fill(t?: table, v: any, startIndex: number, endIndex?: number)
-- * function: indexOf(t: table, v: any)
-- * function: lastIndexOf(t: table, v: any)
-- * function: includes(t: table, v: any)
-- * function: every(t: table, callbackfn: function(k: any, v?: any, t?: table, i?: number))
-- * function: some(t: table, callbackfn: (k: any, v?: number, t?: table) => boolean|any)
-- * function: reduce(t: table, callbackfn: (accumlator: any, curVal: any, i?: number, t?: table) => any, initVal: any)
-- * function: reduceRight( t: table, callbackfn: (accumlator: any, curVal: any, i?: number, t?: table) => any, initVal: any)
-- * function: keys(t: table)
-- * function: namedKeys(t: table)
-- * function: values(t: table)
-- * function: entries(t: table)
-- * function: keySubset(t: table)
-- * function: reverseIpairs(t: table)
-- * function: reverse(t: table)
-- * function: empty(t: table)
-- * function: isEmpty(t: table)
-- * function: clean(t: table)
-- * function: affixNums(t: table, prefix?: string, suffix?: string)
-- * function: numData(t: table, compress?: boolean)
-- * function: compressSparseArray(t: table)
-- * function: sparseIpairs(t: table)
-- * function: keysToList(t: table, keySort?: function|boolean, checked?: boolean)
-- * function: invert(t: table)
-- * function: from(t: table)
-- * function: sequenceToSet(t: table)
-- * function: sortedPairs(t: table, keySort?: boolean)
-- * function: sortedPairsByValue(t: table, keySort?: function|boolean)
-- * function: toCustomArrayNamed(t: table, customFn?: table|generator)
-- * function: recursiveConcat(t: table, sep?: string, i?: number, j?: number)
-- * function: each(t: table, callbackfn: function(k: any, v?: any, t?: table, i?: number)
-- * function: eachNamed(t: table, callbackfn: function(v?: any, k: any, t?: table, i?: number)
-- * function: format(t: table)
-- * function: deepCopy(t: table)
-- * function: dumpObject(t: table)
-- * function: logObject(t: table)
-- * function: tableUtil(t?: table)
-- 
--------------[ ATTRIBUTION ]----------------
-- Some documentation text of this module was taken form the MDN JS guide
-- (https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference).
--
-- Some Functions were taked from `Module:TableTools` at `en.wikipedia.org`.
---------------------------------------------------------------------------------
local libU = require('Module:LibU')
local checkType, checkArgs, assertTrue, assertFalse =
	libU.checkTypeLight, libU.checkArgs, libU.assertTrue, libU.assertFalse

-- Begin Exports
local p = {}

-- Load table library if this module is loaded as "table"
p.concat = table.concat
p.maxn = table.maxn
p.remove = table.remove
p.insert = table.insert
p.sort = table.sort
p.unpack = function(t)
	local mt = getmetatable(t)
	local __m = (mt or {}).__unpack
	
	if __m then
		if type(__m) == 'function' then
			return __m(t)
		else
			return __m
		end
	else
		local _, __ = pcall(unpack, t)
		return _ == false and error(__:gsub('%?', 'unpack'), 2) or unpack(t)
	end
end

p.pack = function(...)
	return { ..., n = select('#', ...) } 
end

---------------------------------------------------------------------------------
-- Local Helper functions
---------------------------------------------------------------------------------
local function isPositiveInteger(v)
	return type(v) == 'number' and v >= 1 and math.floor(v) == v and v < math.huge
end

local function isNaN(v)
	return type(v) == 'number' and tostring(v) == '-nan'
end

local function flattenTable(arr, cb)
	local i = 0
	while arr[i] do
		local v = arr[i]
		
		if type(v) == 'table' then
			flattenTable(v, arr)
		else
			cb(v, i, arr)
		end
	end
end

local function defaultKeySort(a, b)
	return a < b
end

---------------------------------------------------------------------------------
-- function: merge(target: table, ...items: any)
--
-- This function takes each entry in `...items` and adds it to the table.
-- If the item is not a table, it adds it to the table like `push()`.
-- Else, it destructures the table and adds each of its items to the end of `t1`.
---------------------------------------------------------------------------------
function p.merge(target, ...)
	local seen = {}
	checkType('merge', 1, target, 'table')
	
	local function merge(target, merger)
		if type(merger) == 'table' then
			if p.isSequence(merger) then
				p.push(target, unpack(merger))
			else
				for key, value in pairs(merger) do
					local tp = type(value)
					
					if tp == 'table' and not seen[value] then
						seen[value] = 1
						target[key] = target[key] or {}
						merge(target[key], value)
					else
						target[key] = value
					end
				end
			end
		else
			p.push(target, merger)
		end
	end
	
	if select('#', ...) > 1 then
		for i, v in ipairs{ ... } do
			merge(target, v)
		end
	else
		merge(target, ...)
	end
	
	return target
end

---------------------------------------------------------------------------------
-- function: mergeRight(target: table, ...items: any)
--
-- Works like `.merge()` except in reverse.
---------------------------------------------------------------------------------
function p.mergeRight(target, ...)
	local seen = {}
	checkType('mergeRight', 1, target, 'table')
	
	local function merge(target, merger)
		if type(merger) == 'table' then
			if p.isSequence(merger) then
				p.unshift(target, unpack(merger))
			else
				for key, value in pairs(merger) do
					local tp = type(value)
					
					if tp == 'table' and not seen[value] then
						seen[value] = 1
						target[key] = target[key] or {}
						merge(target[key], value)
					else
						target[key] = value
					end
				end
			end
		else
			p.unshift(target, merger)
		end
	end
	
	if select('#', ...) > 1 then
		for i, v in p.reverseIpairs{ ... } do
			merge(target, v)
		end
	else
		merge(target, ...)
	end
	
	return target
end

---------------------------------------------------------------------------------
-- function: mergeNamed(target: table, ...items: any)
--
-- This function takes each entry in `...items` and adds only items with named keys to the table.
-- If the item is not a table, it is ignored.
-- Else, it adds each of its items to the end of `t1`.
---------------------------------------------------------------------------------
function p.mergeNamed(target, ...)
	local seen = {}
	checkType('merge', 1, target, 'table')
	
	local function merge(target, merger)
		if type(merger) == 'table' then
			for key, value in pairs(merger) do
				if type(key) ~= 'number' then
					local tp = type(value)
					
					if tp == 'table' and not seen[value] then
						seen[value] = 1
						target[key] = target[key] or {}
						merge(target[key], value)
					else
						target[key] = value
					end
				end
			end
		end
	end
	
	if select('#', ...) > 1 then
		for i, v in ipairs{ ... } do
			merge(target, v)
		end
	else
		merge(target, ...)
	end
	
	return target
end

---------------------------------------------------------------------------------
-- function: unpackRaw(t: table)
-- 
-- Unpacks a table like `unpack()`, but works with iteration rather than C function.
---------------------------------------------------------------------------------
function p.unpackRaw(t)
	checkType('unpackRaw', 1, t, { 'table' })
	local ret = {}
	local i = 1
	
	while t[i] do
		p.push(ret, t[i])
		i = i+1
	end
	
	return unpack(ret)
end

---------------------------------------------------------------------------------
-- function: length(t: table)
--
-- Gets the length of `t`, as the `#` (length operator) does not work on tables.
-- This function counts all items. To restrict count type, use table.xlength.
----------------------------------------------------------------------------------
function p.length(t)
	checkType('length', 1, t, 'table')
	
	local i = 0
	for k in pairs(t) do
		i = i + 1
	end
	
	return i
end

---------------------------------------------------------------------------------
-- function: xlength(t: table, countNamed?: boolean, countPositional?: boolean)
--
-- Gets the length of `t`, as the `#` (length operator) does not work on tables.
-- Use countNamed and countPositional to restrict which to count.
-- This function runs slower than table.length.
----------------------------------------------------------------------------------
function p.xlength(t, countNamed, countPositional)
	checkType('length', 1, t, 'table')
	checkType('length', 2, countNamed, 'boolean', true)
	checkType('length', 3, countPositional, 'boolean', true)
	
	countNamed = countNamed == nil and true or countNamed
	countPositional = countPositional == nil and true or countPositional
	
	local i = 0
	for k in pairs(t) do
		if type(k) == 'number' then
			if countPositional then
				i = i + 1
			end
		else
			if countNamed then
				i = i + 1
			end
		end
	end
	
	return i
end

---------------------------------------------------------------------------------
-- function: slice(t: table, startIndex: table, endIndex: table)
-- 
-- method returns a shallow copy of a portion of an table into a new table object 
-- selected from start to end (end not included) where start and end represent the index of
-- items in that table. The original table will not be modified.
--
-- ^source: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice
---------------------------------------------------------------------------------
function p.slice(t, startIndex, endIndex)
	checkType('slice', 1, t, { 'table' })
	checkType('slice', 2, startIndex, { 'number' }, true)
	checkType('slice', 3, endIndex, { 'number' }, true)
	
	if not endIndex and not startIndex then
		return p.from(t)
	end
	local ret, len = {}, #t
	startIndex = startIndex or 1
	endIndex = endIndex or len
	
	if startIndex < 0 then
		startIndex = len+startIndex-1
	end
	if endIndex < 0 then
		endIndex = len+endIndex-1
	end
		
	for i, v in ipairs(t) do
		if i >= startIndex and i <= endIndex then
			p.push(ret, v)
		end
	end
	
	return ret
end

---------------------------------------------------------------------------------
-- function: setPrototype(t: table, proto: table, indexFunc: function)
--
-- Sets up a metatable prototype with a table.
---------------------------------------------------------------------------------
function p.setPrototype(t, proto, indexFunc, parentProto)
	checkType('setPrototype', 1, t, 'table')
	checkType('setPrototype', 2, proto, 'table')
	checkType('setPrototype', 3, indexFunc, 'function', true)
	checkType('setPrototype', 4, parentProto, 'table', true)
	
	local mt = {}
	mt.__proto = proto or {}
	parentProto = parentProto or {}
	
	if p.length(parentProto) ~= 0 then
		mt.__proto.prototype = parentProto
	end
	
	indexFunc = indexFunc or function(t, k, proto, parentProto)
		if k == 'prototype' then
			return mt.__proto
		else
			return mt.__proto[k] or (p.length(parentProto or {}) ~= 0 and mt.__proto.prototype[k] or nil)
		end
	end
	
	mt.__index = function(t, k)
		return indexFunc(t, k, mt.__proto, mt.__proto.prototype)
	end
	
	return setmetatable(t, mt)
end

---------------------------------------------------------------------------------
-- function: isSequence(t: table)
--
-- Checks if the table is a sequence.
---------------------------------------------------------------------------------
function p.isSequence(t)
	checkType('isSequence', 1, t, 'table')
	
	return p.every(t, function(i) 
		return type(i) == 'number' and i > 0
	end)
end

---------------------------------------------------------------------------------
-- function: push(t: table, ...items: any)
--
-- Appends each of `...items` to the end of `t`.
---------------------------------------------------------------------------------
function p.push(t, ...)
	checkType('push', 1, t, 'table')
	
	for _, v in ipairs{ ... } do
		table.insert(t, v)
	end
	
	return t
end

---------------------------------------------------------------------------------
-- function: makeReadonlyTable(t: table, realTable: t)
--
-- Makes a read-only table where the real table is a dummy table.
---------------------------------------------------------------------------------
function p.makeReadonlyTable(t, metatable)
	checkType('makeReadonlyTable', 1, t, 'table', true)
	checkType('makeReadonlyTable', 2, metatable, 'table', true)
	
	local tmp, mt, readableMt = {}, {}
	
	metatable = metatable or {}
	t = t or {}
	metatable.__index, metatable.__newindex, metatable.__pairs, metatable.__ipairs, metatable.__metatable = nil, nil, nil, nil, nil
	
	for k, v in pairs(metatable) do
		mt[k] = v
	end
	
	mt.__realTable = t
	
	local function __index(t, k)
		return mt.__realTable[k]
	end
	
	local function __newindex()
		return error('table is read-only', 2)
	end
	
	local function __pairs()
		return pairs(mt.__realTable)
	end

	local function __ipairs()
		return ipairs(mt.__realTable)
	end
	
	local function len()
		return #mt.__realTable
	end
	
	mt.__index = __index
	mt.__newindex = __newindex
	mt.__pairs = __pairs
	mt.__ipairs = __ipairs
	mt.__len = len
	mt.__metatable = {}
	
	return setmetatable(tmp, mt)
end

---------------------------------------------------------------------------------
-- function: unshift(t: table, ...items: any)
-- 
-- Prepends each of `...items` to the front of `t`.
---------------------------------------------------------------------------------
function p.unshift(t, ...)
	checkType('unshift', 1, t, 'table')
	
	if select('#', ...) > 1 then
		for _, v in p.reverseIpairs{ ... } do
			table.insert(t, 1, v)
		end
	else
		table.insert(t, 1, ...)
	end
	
	return t
end

---------------------------------------------------------------------------------
-- function: map(t: table, callbackfn: function(v: any, i?: number, t?: table))
--
-- Creates a new table and populates with results from the callback function.
--
---------------[ CALLBACK PARAMETERS ]-------------
-- The callback to `map` has three values passed to it described above.
-- `v`, the value of the table index, `i`, the table index, and `t`, the actual table.
-- `map` will popluate the new table with the return values of this function.
---------------------------------------------------------------------------------
function p.map(t, callbackfn)
	checkType('map', 1, t, 'table')
	checkType('map', 2, callbackfn, 'function')
	
	local ret = {}
	
	for i, v in ipairs(t) do
		ret[#ret+1] = callbackfn(v, i, t) 
	end
	
	return ret
end


---------------------------------------------------------------------------------
-- function: mapNamed(t: table, callback: function(v: any, i?: number, t?: table) => any)
-- 
-- Similar to map, but iterates through a table
-- Creates a new table and populates with results from the callback function.
---------------------------------------------------------------------------------
function p.mapNamed(t, callback)
	checkType('mapWith', 1, t, 'table')
	checkType('mapWith', 2, callback, 'function')
	
	local ret = {}
	
	for k, v in pairs(t) do
		ret[k] = callback(k, v, t)
	end
	
	return ret
end


---------------------------------------------------------------------------------
-- function: mapWith(t: table, callback: function(v: any, i?: number, t?: table) => any)
-- 
-- Maps over a table and sets the corresponding key with the callback's return value.
---------------------------------------------------------------------------------
function p.mapWith(t, callback)
	checkType('mapWith', 1, t, 'table')
	checkType('mapWith', 2, callback, 'function')
	
	for k, v in pairs(t) do
		t[k] = callback(k, v, t)
	end
	
	return t
end

---------------------------------------------------------------------------------
-- function: filter(t: table, callbackfn: function(v: any, i?: number, t?: table))
--
-- Creates a new table with all elements that pass the test implemented by the provided function.
---------------------------------------------------------------------------------
function p.filter(t, callbackfn)
	checkType('filter', 1, t, 'table')
	checkType('filter', 2, callbackfn, 'function')
	
	local ret = {}
	
	for i, v in ipairs(t) do
		if callbackfn(v, i, t) then
			p.push(ret, v)
		end
	end
	
	return ret
end

---------------------------------------------------------------------------------
-- function: filterWith(t: table, callbackfn: function(v: any, i?: number, t?: table))
--
-- Returns the same table with any values that did not pass the filter function removed.
---------------------------------------------------------------------------------
function p.filterWith(t, callbackfn)
	checkType('filterWith', 1, t, 'table')
	checkType('filterWith', 2, callbackfn, 'function')
	
	local temp = p.from(t)
	p.empty(t)
	
	for i, v in ipairs(temp) do
		if callbackfn(v, i, t) then
			p.push(t, v)
		end
	end
	
	return t
end


---------------------------------------------------------------------------------
-- function: filterNamed(t: table, callbackfn: function(v: any, i?: number, t?: table))
--
-- Creates a new table with all key/value pairs that pass the test implemented by the provided function.
---------------------------------------------------------------------------------
function p.filterNamed(t, callbackfn)
	checkType('filterNamed', 1, t, 'table')
	checkType('filterNamed', 2, callbackfn, 'function')
	
	local ret = {}
	
	for k, v in pairs(t) do
		if callbackfn(k, v, t) then
			ret[k] = v
		end
	end
	
	return ret
end

---------------------------------------------------------------------------------
-- function: filterWithNamed(t: table, callbackfn: function(v: any, i?: number, t?: table))
--
-- Return the same table with any key/value pairs that did not pass the filter function removed.
---------------------------------------------------------------------------------
function p.filterWithNamed(t, callbackfn)
	checkType('filterWithNamed', 1, t, 'table')
	checkType('filterWithNamed', 2, callbackfn, 'function')
	
	local temp = p.from(t)
	p.empty(t)
	
	for k, v in pairs(temp) do
		if callbackfn(k, v, t) then
			t[k] = v
		end
	end
	
	return t
end

---------------------------------------------------------------------------------
-- function: filterEntriesByKey(t: table, keys: Sequence<any>)
-- 
-- Removes the keys in `keys` from `t`.
---------------------------------------------------------------------------------
function p.filterEntriesByKey(t, keys)
	checkType('filterEntriesByKey', 1, t, 'table')
	checkType('filterEntriesByKey', 2, keys, 'table', true)
	
	return p.filterNamed(t, function(k)
		return not p.includes(keys or {}, k)
	end)
end

---------------------------------------------------------------------------------
-- function: removeLast(t: table)
--
-- Removes the last element of the table and returns it.
---------------------------------------------------------------------------------
function p.removeLast(t)
	checkType('removeLast', 1, t, 'table')
	
	return table.remove(t, p.length(t, false))
end
p.pop = p.removeLast

---------------------------------------------------------------------------------
-- function: removeFirst(t: table)
--
-- Removes the First element of the table and returns it.
---------------------------------------------------------------------------------
function p.removeFirst(t)
	checkType('removeFirst', 1, t, 'table')
	
	return table.remove(t, 1)
end
p.shift = p.removeFirst

---------------------------------------------------------------------------------
-- function: flat(t: table)
-- 
-- Takes a sequence table and flattens all elements down into a single-depth table recursively.
---------------------------------------------------------------------------------
function p.flat(t)
	checkType('flat', 1, t, { 'table' })
	assertTrue(p.isSequence(t), 'bad argument #1 to flat (table is not a sequence)', 2)
	
	local ret = {}
	local seen = {}
	local function _recurse(t)
		for i, v in ipairs(t) do
			if type(v) == 'table' and not seen[v] then
				_recurse(v)
				seen[v] = 1
			else
				p.push(ret, v)
			end
		end
	end
	
	_recurse(t)
	
	return ret
end

---------------------------------------------------------------------------------
-- function: flatMap(t: function, cb: function)
-- 
-- calls flat() on the `t` then calls map() on the flattened table with `cb`.
---------------------------------------------------------------------------------
function p.flatMap(t, cb)
	checkType('flatMap', 1, t, 'table')
	checkType('flatMap', 2, cb, { 'function' })
	
	return p.map(p.flat(t), cb)
end

---------------------------------------------------------------------------------
-- function: Map(items: table)
-- 
-- Creates a Map.
---------------------------------------------------------------------------------
function p.Map(items)
	local ret = {}
	local keys = {}
	local seenkeys = {}
	local Map = {}
	Map.getters = {}
	
	function Map.getters:size()
		return p.length(self, true)
	end
	
	function Map:set(k, v)
		assertFalse(k == nil, 'Map index is nil', 2)
		assertFalse(isNaN(k), 'Map index is NaN', 2)
		
		self[k] = v
		return self
	end
	
	function Map:get(k)
		assertFalse(k == nil, 'Map index is nil', 2)
		assertFalse(isNaN(k), 'Map index is NaN', 2)
		
		self[k] = v
		return self
	end
	
	function Map:remove(k)
		for i = 1, #keys do
			if keys[i] == k then
				table.remove(keys, i)
				break
			end
		end
		self[k] = nil
		
		return self
	end
	
	function Map:clear()
		p.empty(self)
		p.empty(keys)
		
		return self
	end
	
	function Map:forEach(cb)
		checkType('forEach', 1, cb, 'function', true)
		
		for k, v in pairs(self) do
			(cb or mw.log)(k, v, self)
		end
		
		return self
	end
	
	function Map:keys()
		return keys
	end
	
	function Map:values()
		local ret = {}
		
		for _, val in ipairs(keys) do
			p.push(ret, val)
		end
		
		return ret
	end
	
	
	function Map:entries()
		local ret = {}
		for i = 1, #keys do
			ret[i] = { keys[i], self[keys[i]] }
		end
		
		return ret
	end
	
	local function __pairs(t)
		local i, len = 0, #keys
		
		return function()
			i = i+1
			if keys[i] and i <= len then
				return keys[i], ret[keys[i]]
			else
				return nil, nil
			end
		end
	end
	
	local function __ipairs(t)
		local i, len = 0, #keys
		
		return function()
			i = i+1
			if keys[i] and i <= len then
				return i, ret[keys[i]], keys[i]
			else
				return nil, nil, nil
			end
		end
	end
	
	Map.constructor = p.Map
	
	setmetatable(ret, {
		__index = function(t, k)
			if Map.getters[k] then
				return Map.getters[k](t)
			elseif k ~= 'getters' then
				return Map[k]
			end
			
			return nil
		end,
		__newindex = function(t, k, v)
			if seenkeys[k] and not t[k] then
				for i = 1, #keys do
					if keys[i] == k then
						table.remove(keys, i)
						break
					end
				end
			end
			
			rawset(seenkeys, k, 1)
			table.insert(keys, k)
			rawset(t, k, v)
		end,
		__pairs = __pairs,
		__ipairs = __ipairs,
		__tostring = function() return 'map' end
	})
	
	return ret
end

---------------------------------------------------------------------------------
-- function: Set(t)
-- 
-- Turns a table into a set.
---------------------------------------------------------------------------------
function p.Set(t)
	checkType('Set', 1, t, 'table', true)
	t = t or {}
	local ret = {}
	local keys = {}
	local size = 0
	local reservedKeys = {
		['size'] = 1,
	}
	
	for k, v in pairs(t) do
		if type(k) == 'number' then
			if not keys[v] then size = size + 1 end
			keys[v] = 1
		else
			if not keys[k] then size = size + 1 end
			keys[k] = 1
		end
	end
	
	local Set = {}
	
	Set.constructor = p.Set
	
	function Set:has(...)
		if select('#', ...) == 1 then
			local value = ...
			assertFalse(value == nil, 'Set value is nil', 2)
			assertFalse(isNaN(value), 'Set value is NaN', 2)
			
			for v in pairs(keys) do
				if v == value then
					return true
				end
			end
			
			return false
		else
			local has = {}
			for val in forEachArgs({ 'any', required = 1 }, ...) do
				has[val] = self:has(val)
			end
			
			return has
		end
	end
	
	function Set:remove(...)
		local removed
		local len = select('#', ...)
		
		if len == 1 then
			assertFalse(... == nil, 'Set value is nil', 2)
			assertFalse(isNaN(...), 'Set value is NaN', 2)
			
			local has = self:has(...)
			if has then size = size - 1 end
			keys[...] = nil
			
			return has
		else
			removed = {}
			
			for val in forEachArgs({'any', required = 1}, ...) do
				removed[val] = self:remove(val)
			end
		end
	end
	
	function Set:clone()
		return p.Set(keys)
	end
	
	function Set:add(...)
		for val in forEachArgs({'any', required = 1}, ...) do
			if not keys[val] then size = size + 1 end
			keys[val] = 1
		end
		
		return self
	end
		
	function Set:find(callbackfn)
		checkType('find', 1, callbackfn, { 'function' })
		
		for val in self:pairs() do
			if callbackfn(val, self) then
				return val
			end
		end
		
		return nil
	end
	
	function Set:each(callbackfn)
		checkType('each', 1, callbackfn, { 'function' })
		
		for val in pairs(self) do
			callbackfn(val, self)
		end
		
		return self
	end
	
	function Set:map(callbackfn)
		checkType('map', 1, callbackfn, { 'function' })
		
		return self:clone():mapWith(callbackfn)
	end
	
	function Set:mapWith(callbackfn)
		checkType('mapWith', 1, callbackfn, { 'function' })
		
		for val in pairs(self) do
			self:remove(val)
			self:add(callbackfn(val, self))
		end
		
		return self
	end
	
	function Set:pairs()
		return pairs(self)
	end
	
	function Set:ipairs()
		return ipairs(self)
	end
	
	function Set:filter(callbackfn)
		checkType('filter', 1, callbackfn, { 'function' })
		
		return self:clone():filterWith(callbackfn)
	end
	
	function Set:filterWith(callbackfn)
		checkType('filterWith', 1, callbackfn, { 'function' })
		
		for val in pairs(self) do
			if not callbackfn(val, self) then self:remove(val) end
		end
		
		return self
	end
	
	function Set:intersection(otherSet)
		assertTrue(otherSet and otherSet.constructor == p.Set, 'bad argument #1 to \'intersection\' (compare value must be another set)', 2)
		
		local values = {}
		
		for val in pairs(self) do
			if otherSet:has(val) then
				p.push(values, val)
			end
		end
		
		return p.Set(values)
	end
	
	function Set:difference(otherSet)
		assertTrue(otherSet and otherSet.constructor == p.Set, 'bad argument #1 to \'difference\' (compare value must be another set)', 2)
		
		local values = {}
		
		for val in pairs(self) do
			if not otherSet:has(val) then
				p.push(values, val)
			end
		end
		
		return p.Set(values)
	end
	
	function Set:symDifference(otherSet)
		assertTrue(otherSet and otherSet.constructor == p.Set, 'bad argument #1 to \'symDifference\' (compare value must be another set)', 2)
		
		return self:difference(otherSet):union(otherSet:difference(self))
	end
	
	function Set:union(otherSet)
		assertTrue(otherSet and otherSet.constructor == p.Set, 'bad argument #1 to \'union\' (other value must be another set)', 2)
		
		local values = {}
		
		for val in pairs(self) do
			p.push(values, val)
		end
		
		return p.Set(values)
	end
	
	function Set:merge(...) 
		for val, i in forEachArgs({'any', required = 1}, ...) do
			checkType(i, val, 'table')
			
			if p.constructor == Set.constructor then
				for v in pairs(val) do
					self:add(v)
				end
			elseif not p.isSequence(val) then
				for v in pairs(val) do
					self:add(v)
				end
			else
				for _, v in ipairs(val) do
					self:add(v)
				end
			end
		end
	end
	
	function Set:clear()
		keys = {}
		size = 0
		
		return self
	end
	
	function Set:values()
		return p.keys(keys)
	end
	
	return setmetatable(ret, {
		__newindex = function(t, k, v)
			assertFalse(reservedKeys[k], 'Set property %q is read-only', 2, k)
			
			if not t[k] then size = size + 1 end
			return rawset(keys, k, 1)
		end,
		
		__index = function(t, k)
			if k == 'size' then
				return size
			elseif Set[k] then
				return Set[k]
			else
				return t:has(k)
			end
		end,
		
		__pairs = function(t)
			local keys = p.keys(keys)
			local i = 0
			
			return function()
				i = i+1
				if keys[i] and i <= size then
					return keys[i]
				else
					return nil
				end
			end
		end,
		
		__ipairs = function(t)
			local keys = p.keys(keys)
			local i = 0
			
			return function()
				i = i+1
				if keys[i] and i <= size then
					return i, keys[i]
				else
					return nil, nil
				end
			end
		end,
		
		__tostring = function()
			return string.format('Set: { %s }', table.concat(p.map(p.keys(keys), function(k)
				if (type(k) == 'table') then
					return 'table'
				elseif (type(k) == 'function') then
					return 'function'
				elseif (type(k) == 'string') then
					return string.format('"%s"', string.gsub(k, '"', '\\"'))
				else
					return k
				end
			end), ', '))
		end
	})
end

---------------------------------------------------------------------------------
-- function: find(t: table, compare: any)
-- 
-- Checks each result found by `compare` and compares it against `t`. If an index is found,
-- If `compare` is not a function, it compares each value to `compare`.
-- the result is returned along with it's index. If no value is found, it returns nil.
---------------------------------------------------------------------------------
function p.find(...)
	local t, compare = checkArgs({ 'table', { 'any', emptyOk = true } }, ...)
	
	local isFunction = type(compare) == 'function'
	for k, v in pairs(t) do
		if type(compare) == 'function' and compare(v, k, t) or compare == v then
			return v, k
		end
	end
	
	return
end

---------------------------------------------------------------------------------
-- function: findIndex(t: table, compare: any)
-- 
-- Very similar to find(), but returns only the index.
---------------------------------------------------------------------------------
function p.findIndex(...)
	local _, ret = p.find(checkArgs({ 'table', { 'any', emptyOk = true } }, ...))
	
	return ret
end

---------------------------------------------------------------------------------
-- function: splice(t: table, start: number, deleteCount?: number, ...items: any)
-- 
-- Removes/replaces/adds table elements in place. It may do the following functions:
-- *Insert elements at a certain index
-- *Remove a number of a element starting at a sertain index
-- *Replace a number of elements at a certain inxex
-- See https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice for more info.
---------------------------------------------------------------------------------
function p.splice(t, start, deleteCount, ...)
	checkType('splice', 1, t, { 'table' })
	checkType('splice', 2, start, { 'number' })
	checkType('splice', 3, deleteCount, { 'number' }, true)
	
	start = (start and start ~= 0) and start or 1
	local ret, len = {}, #t
	count = 0
	
	if - -start < 0 then
		start = len+start+1
	end
	maxCount = - -deleteCount or math.huge
	
	for i = start, len, 1 do
		count = count+1
		if count > maxCount then break end
		
		p.push(ret, table.remove(t, start))
	end
	
	if select('#', ...) > 0 then
		for _, v in forEachArgs({ 'any' }, ...) do
			table.insert(t, start, v)
		end
	end
	
	return ret
end

---------------------------------------------------------------------------------
-- function: fill(t?: table, v: any, startIndex: number, endIndex?: number)
--
-- Sets the table index starting at `startIndex` with the value of `v` ending at `endIndex`.
-- If end is not specified, it defualts to the length of the table.
---------------------------------------------------------------------------------
function p.fill(t, v, startIndex, endIndex)
	checkType('fill', 1, t, 'table', true)
	checkType('fill', 3, startIndex, 'number')
	checkType('fill', 4, endIndex, 'number', true)
	
	local t = t or {}
	
	for i = - -startIndex, endIndex and - -endIndex or #t, 1 do
		t[i] = v
	end
	
	return t
end

---------------------------------------------------------------------------------
-- function: indexOf(t: table, v: any)
--
-- Searches for `v` the first index in `t`. If nothing is found, it returns `-1`.
---------------------------------------------------------------------------------
function p.indexOf(t, value)
	checkType('indexOf', 1, t, 'table')
	
	local index
	p.some(t, function(k, v) 
		if v == value then
			index = k
			return true 
		else
			return false
		end
	end)
	
	return index or -1
end

---------------------------------------------------------------------------------
-- function: lastIndexOf(t: table, v: any)
--
-- Searches for `v` the first index in `t`. If nothing is found, it returns `-1`.
---------------------------------------------------------------------------------
function p.lastIndexOf(t, v)
	checkType('lastIndexOf', 1, t, 'table')
	
	for i, value in p.reverseIpairs(t) do
		if v == value then return i end 
	end
	return -1
end

---------------------------------------------------------------------------------
-- function: includes(t: table, v: any)
--
-- Checks if `v` is included in any indexes in `t`.
---------------------------------------------------------------------------------
function p.includes(t, v)
	checkType('includes', 1, t, 'table')
	
	return p.some(t, v)
end

---------------------------------------------------------------------------------
-- function: every(t: table, callbackfn: function(k: any, v?: any, t?: table, i?: number))
-- 
-- Tests every element from the return value from `callbackfn`. If any elements fail
-- the test, it returns false.
-- 
---------------[ CALLBACK PARAMETERS ]-------------
-- callbackfn(k: any, v?: any, t?: table, i?: number)
--
-- If the callback returns false, `every()` will consider the test failed and
-- return false.
--	 *`k` is the table key `every()` is currently over.
--	 *`v` is the value of the table key `every()` is currently over.
--	 *`t` is the table `every()` was called on.
--	 *`i` is the number of iterations `every()` has iterated over.
---------------------------------------------------------------------------------
function p.every(t, callbackfn)
	checkType('every', 1, t, 'table')
	assertTrue(callbackfn ~= nil, 'Compare value must not be nil', 2)
	
	local tp = type(callbackfn)
	local i = 0
	for k, v in pairs(t) do
		i = i+1
		if tp == 'function' then
			if not callbackfn(k, v, t, i) then
				return false
			end
		else
			return v == callbackfn
		end
	end
	
	return true
end

---------------------------------------------------------------------------------
-- function: some(t: table, callbackfn: (v: any, i: number, t: table) => boolean|any)
--
-- Tests whether at least one element in the table passes the test implemented 
-- by the provided function. It returns a Boolean value.
----------------------------------------------------------------------------------
function p.some(t, callbackfn)
	checkType('some', 1, t, 'table')
	assertTrue(callbackfn ~= nil, 'Compare value must not be nil', 2)
	
	local tp = type(callbackfn)
	for k, v in pairs(t) do
		if tp == 'function' then
			if callbackfn(k, v, t) then
				return true
			end
		else
			if v == callbackfn then
				return true
			end
		end
	end
	return false
end

---------------------------------------------------------------------------------
-- function: reduce(
--	 t: table, 
--	 callbackfn: (accumlator: any, curVal: any, i?: number, t?: table) => any, 
--	 initVal: any
-- )
-- 
-- Executes a reducer callback function on each element of the table, resulting in single output value.
--
---------------[ CALLBACK PARAMETERS ]-------------
-- callbackfn(accumlator: any, curVal: any, i?: number, t?: table)
--
-- The callback to `every` has four values passed to it described above.
-- `accumlator` is the accumulated value previously returned in the last invocation 
-- of the callback value of to accumalate.
-- `curVal` is the current element being processed in the table.
-- `i` is the current index of the processes element.
-- `t` is the table `reduce()` was called on.
---------------------------------------------------------------------------------
function p.reduce(t, callbackfn, initVal)
	checkType('reduce', 1, t, 'table')
	checkType('reduce', 2, callbackfn, 'function')
	assertTrue(callbackfn('', '', '', '') ~= nil, 'bad argument #1 to reduce (no return value for callback)', 2)
	
	local accumulator
	for i, v in ipairs(t) do
		if i == 1 then
			accumulator = initVal and callbackfn(initVal, v, i, t) or v
		elseif i ~= 1 then
			accumulator = callbackfn(accumulator, v, i, t)
		end
	end
	
	return accumulator
end


---------------------------------------------------------------------------------
-- function: reduceRight(
--	 t: table, 
--	 callbackfn: (accumlator: any, curVal: any, i?: number, t?: table) => any, 
--	 initVal: any
-- )
-- 
-- Executes a reducer callback function on each element of the table from left to right,
-- resulting in single output value. Very similar to `reduce()`.
--
---------------[ CALLBACK PARAMETERS ]-------------
-- callbackfn(accumlator: any, curVal: any, i?: number, t?: table)
--
-- The callback to `every` has four values passed to it described above.
-- `accumlator` is the accumulated value previously returned in the last invocation 
-- of the callback value of to accumalate.
-- `curVal` is the current element being processed in the table.
-- `i` is the current index of the processes element.
-- `t` is the table `reduceRight()` was called on.
---------------------------------------------------------------------------------
function p.reduceRight(t, callbackfn, initVal)
	checkType('reduceRight', 1, t, 'table')
	checkType('reduceRight', 2, callbackfn, 'function')
	assertTrue(callbackfn('', '', '', '') ~= nil, 'bad argument #1 to reduceRight (no return value for callback)', 2)
	
	local accumulator
	for i, v, start in p.reverseIpairs(t) do
		if i == start then
			accumulator = initVal and callbackfn(initVal, v, i, t) or v
		elseif i ~= start then
			accumulator = callbackfn(accumulator, v, i, t)
		end
	end
	return accumulator
end

---------------------------------------------------------------------------------
-- function: keys(t: table)
--
-- Returns a table containing all keys of this table.
---------------------------------------------------------------------------------
function p.keys(t)
	checkType('keys', 1, t, 'table')
	local ret = {}
	
	for k, v in pairs(t) do
		p.push(ret, k)
	end
	return ret
end

---------------------------------------------------------------------------------
-- function: namedKeys(t: table)
--
-- Returns a table containing all named keys of this table.
---------------------------------------------------------------------------------
function p.namedKeys(t)
	checkType('keys', 1, t, 'table')
	local ret = {}
	
	for k, v in pairs(t) do
		if type(k) ~= 'number' then
			p.push(ret, k)
		end
	end
	return ret
end

---------------------------------------------------------------------------------
-- function: values(t: table)
--
-- Returns a table containing all values of this table.
---------------------------------------------------------------------------------
function p.values(t)
	checkType('values', 1, t, 'table')
	local ret = {}
	
	for k, v in p.sortedPairs(t) do
		p.push(ret, v)
	end
	return ret
end

---------------------------------------------------------------------------------
-- function: entries(t: table)
--
-- Returns a table with each subtable containing the tables key in the first value,
-- and the original table's value corresponding to that key.
---------------------------------------------------------------------------------
function p.entries(t)
	checkType('entries', 1, t, 'table')
	local ret = {}
	
	for k, v in p.sortedPairs(t) do
		p.push(ret, { k, v })
	end
	return ret
end

---------------------------------------------------------------------------------
-- function: keySubset(t: table)
--
-- This takes a table and returns an array containing the numbers of any numerical
-- keys that have non-nil values, sorted in numerical order.
--
--------------[ ATTRIBUTION ]------------
-- This function was taken from `en.wikipedia.org` in `Module:TableTools`.
---------------------------------------------------------------------------------
function p.keySubset(t)
	checkType('keySubset', 1, t, 'table')
	
	local nums = {}
	for k, v in pairs(t) do
		if isPositiveInteger(k) then
			nums[#nums + 1] = k
		end
	end
	table.sort(nums)
	
	return nums
end

---------------------------------------------------------------------------------
-- function: reverseIpairs(t: table)
-- 
-- Returns a iterator function to iterate backwards over a sequence table.
-- This works like `ipairs()` except it works backwards, and it provides an additional
-- value in the iteration, `start`. The `start` value is the index the function
-- started iterating at.
--
-----------------[ EXAMPLE ]----------------
-- for i, v, start in table.reverseIpairs(t) do
--	 -- code block
-- end
---------------------------------------------------------------------------------
function p.reverseIpairs(t)
	checkType('reverseIpairs', 1, t, 'table')
	
	local len = p.length(t)
	return function(a, i)
		i = i - 1
		local v = a[i]
		if v ~= nil then
			return i, v, len
		end
	end, t, len+1
end

---------------------------------------------------------------------------------
-- function: reverse(t: table)
-- 
-- Reverses the table in place. The first array element becomes the last, and 
-- the last array element becomes the first.
---------------------------------------------------------------------------------
function p.reverse(t)
	checkType('reverse', 1, t, 'table')
	
	local n = #t
	local i = 1
	
	while i < n do
		t[i], t[n] = t[n], t[i]
		i = i + 1
		n = n - 1
	end
	
	return t
end

---------------------------------------------------------------------------------
-- function: empty(t: table)
-- 
-- Empties the table of all keys.
---------------------------------------------------------------------------------
function p.empty(t)
	checkType('empty', 1, t, 'table')
	
	for k, v in pairs(t) do
		t[k] = nil
	end
		
	return t
end

---------------------------------------------------------------------------------
-- function: isEmpty(t: table)
-- 
-- Checks if a table is completly empty
---------------------------------------------------------------------------------
function p.isEmpty(t)
	checkType('isEmpty', 1, t, 'table')
	
	return next(t) == nil
end

---------------------------------------------------------------------------------
-- function: clean(t: table)
-- 
-- Removes any indexes from the table which are nil, or are not a postive number.
---------------------------------------------------------------------------------
function p.clean(t)
	checkType('clean', 1, t, 'table')
	
	local ret = {}
	local nums = p.keySubset(t)
	
	for _, num in ipairs(nums) do
		ret[#ret+1] = t[num]
	end
	return ret
end

------------------------------------------------------------------------------------
-- function: affixNums(t: table, prefix?: string, suffix?: string)
--
-- This takes a table and returns an array containing the numbers of keys with the
-- specified prefix and suffix. For example, for the table
-- {a1 = 'foo', a3 = 'bar', a6 = 'baz'} and the prefix "a", affixNums will
-- return {1, 3, 6}.
--
--------------[ ATTRIBUTION ]------------
-- This function was taken from `en.wikipedia.org` in `Module:TableTools`.
------------------------------------------------------------------------------------
function p.affixNums(t, prefix, suffix)
	checkType('affixNums', 1, t, 'table')
	checkType('affixNums', 2, prefix, 'string', true)
	checkType('affixNums', 3, suffix, 'string', true)
	
	local function cleanPattern(s)
		-- Cleans a pattern so that the magic characters ()%.[]*+-?^$ are interpreted literally.
		return s:gsub('([%(%)%%%.%[%]%*%+%-%?%^%$])', '%%%1')
	end
	
	prefix = prefix or ''
	suffix = suffix or ''
	prefix = cleanPattern(prefix)
	suffix = cleanPattern(suffix)
	local pattern = table.concat{ '^', prefix, '([1-9]%d*)', suffix, '$' }
	
	local nums = {}
	for k, v in pairs(t) do
		if type(k) == 'string' then
			local num = string.match(k, pattern)
			if num then
				nums[#nums + 1] = tonumber(num)
			end
		end
	end
	table.sort(nums)
	return nums
end


------------------------------------------------------------------------------------
-- function: numData(t: table, compress?: boolean)
--
-- Given a table with keys like ("foo1", "bar1", "foo2", "baz2"), returns a table
-- of subtables in the format 
-- { [1] = {foo = 'text', bar = 'text'}, [2] = {foo = 'text', baz = 'text'} }
-- Keys that don't end with an integer are stored in a subtable named "other".
-- The compress option compresses the table so that it can be iterated over with
-- `ipairs()`.
--
--------------[ ATTRIBUTION ]------------
-- This function was taken from `en.wikipedia.org` in `Module:TableTools`.
------------------------------------------------------------------------------------
function p.numData(t, compress)
	checkType('numData', 1, t, 'table')
	checkType('numData', 2, compress, 'boolean', true)
	
	local ret = {}
	for k, v in pairs(t) do
		local prefix, num = string.match(tostring(k), '^([^0-9]*)([1-9][0-9]*)$')
		if num then
			num = tonumber(num)
			local subtable = ret[num] or {}
			if prefix == '' then
				-- Positional parameters match the blank string; put them at the start of the subtable instead.
				prefix = 1
			end
			subtable[prefix] = v
			ret[num] = subtable
		else
			local subtable = ret.other or {}
			subtable[k] = v
			ret.other = subtable
		end
	end
	if compress then
		local other = ret.other
		ret = p.compressSparseArray(ret)
		ret.other = other
	end
	return ret
end


---------------------------------------------------------------------------------
-- function: compressSparseArray(t: table)
--
-- This takes an array with one or more nil values, and removes the nil values
-- while preserving the order, so that the array can be safely traversed with
-- ipairs.
--
--------------[ ATTRIBUTION ]------------
-- This function was taken from `en.wikipedia.org` in `Module:TableTools`.
---------------------------------------------------------------------------------
function p.compressSparseArray(t)
	checkType('compressSparseArray', 1, t, 'table')
	local ret = {}
	local nums = p.keySubset(t)
	for _, num in ipairs(nums) do
		ret[#ret + 1] = t[num]
	end
	return ret
end


---------------------------------------------------------------------------------
-- function: sparseIpairs(t: table)
--
-- This is an iterator for sparse arrays. It can be used like `ipairs()`, but can
-- handle nil values.
--
--------------[ ATTRIBUTION ]------------
-- This function was taken from `en.wikipedia.org` in `Module:TableTools`.
---------------------------------------------------------------------------------
function p.sparseIpairs(t)
	checkType('sparseIpairs', 1, t, 'table')
	local nums = p.keySubset(t)
	local i = 0
	local lim = #nums
	return function()
		i = i + 1
		if i <= lim then
			local key = nums[i]
			return key, t[key]
		else
			return nil, nil
		end
	end
end


------------------------------------------------------------------------------------
-- function: keysToList(t: table, keySort?: function|boolean, checked?: boolean)
-- 
-- Returns a list of the keys in a table, sorted using either a default
-- comparison function or a custom keySort function.
-- 
--------------[ ATTRIBUTION ]------------
-- This function was taken from `en.wikipedia.org` in `Module:TableTools`.
------------------------------------------------------------------------------------
function p.keysToList(t, keySort, checked)
	if not checked then
		checkType('keysToList', 1, t, 'table')
		checkType('keysToList', 2, keySort, { 'function', 'boolean', 'nil' })
	end
	
	local list = {}
	local index = 1
	for key, value in pairs(t) do
		list[index] = key
		index = index + 1
	end
	
	if keySort ~= false then
		keySort = type(keySort) == 'function' and keySort or defaultKeySort
		
		table.sort(list, keySort)
	end
	
	return list
end

-------------------------------------------------------------------------------
-- function: invert(t: table)
-- 
-- Replaces keys with thier values and vice versa for thier values.
---------------------------------------------------------------------------------
function p.invert(t)
	checkType('invert', 1, t, 'table')
	-- assertTrue(p.isSequence(t), 'bad argument #1 to invert (table is not a sequence)', 2)
	
	local ret = {}
	for k, v in pairs(t) do
		ret[v] = k
	end
	
	return ret
end

---------------------------------------------------------------------------------
-- function: from(t: table)
-- 
-- Creates a shallow copy of `t`. This means any subtables and functions will be shared.
-- Use `deepCopy()` for a deep copy function.
---------------------------------------------------------------------------------
function p.from(t)
	checkType('from', 1, t, 'table')
	
	local ret = {}
	for k, v in p.sortedPairs(t) do
		ret[k] = v
	end
	
	return ret
end

---------------------------------------------------------------------------------
-- function: sequenceToSet(t: table)
-- 
-- Creates a shallow copy of `t`. This means any subtables and functions will be shared.
-- Use `deepCopy()` for a deep copy function.
---------------------------------------------------------------------------------
function p.sequenceToSet(t)
	checkType('sequenceToSet', 1, t, 'table')
	assertTrue(p.isSequence(t), 'bad argument #1 to sequenceToSet (table is not a sequence)', 2)
	
	local ret = {}
	p.each(t, function(v)
		ret[v] = true
	end)
	return ret
end
---------------------------------------------------------------------------------
-- function: sortedPairs(t: table, keySort?: boolean)
-- 
-- Iterates through a table, with the keys sorted using the keysToList function.
-- If there are only numerical keys, sparseIpairs is probably more efficient.
-- 
--------------[ ATTRIBUTION ]------------
-- This function was taken from `en.wikipedia.org` in `Module:TableTools`.
---------------------------------------------------------------------------------
function p.sortedPairs(t, keySort)
	checkType('sortedPairs', 1, t, 'table')
	checkType('sortedPairs', 2, keySort, 'function', true)
	
	local list = p.keysToList(t, keySort, true)
	
	local i = 0
	return function()
		i = i + 1
		local key = list[i]
		if key ~= nil then
			return key, t[key]
		else
			return nil, nil
		end
	end
end

---------------------------------------------------------------------------------
-- function: sortedPairsByValue(t: table, keySort?: function|boolean)
-- 
-- Iterates through a table, sorted using either a default comparison
-- function or a custom keySort function on the value
-- Returns a generator
---------------------------------------------------------------------------------
function p.sortedPairsByValue(t, keySort)
	checkType('sortedPairsByValue', 1, t, 'table')
	checkType('sortedPairsByValue', 2, keySort, { 'function', 'boolean', 'nil' })
	
	local function toArray(t)
		local ret = {}
		for k, v in pairs(t) do
			p.push(ret, { key = k, value = v })
		end
		return ret
	end
	
	local list = toArray(p.deepCopy(t, true))
	
	if keySort ~= false then
		keySort = type(keySort) == 'function' and keySort or defaultKeySort
		
		table.sort(list, function(a, b)
			a, b = a.value, b.value
			return keySort(a, b)
		end)
	end
	
	local i = 0
	return function()
		i = i + 1
		local data = list[i]
		if data ~= nil then
			return data.key, data.value
		else
			return nil, nil
		end
	end
end

---------------------------------------------------------------------------------
-- function: toCustomArrayNamed(t: table, customFn?: table|generator)
-- 
-- Iterates through a named table or using a generator, map each values
-- returned by a custom function into a table
-- There is no counterpart for indexed table because that would be the same as p.map
---------------------------------------------------------------------------------
function p.toCustomArrayNamed(t, customFn)
	checkType('toCustomArrayNamed', 1, t, { 'function', 'table' })
	checkType('toCustomArrayNamed', 2, customFn, { 'function', 'nil' })
	
	local ret = {}
	customFn = type(customFn) == 'function' and customFn or function(v, k) return k end
	if type(t) == 'function' then -- t as generator
		for k, v in t do
			p.push(ret, customFn(v, k, t))
		end
	else -- t as table
		for k, v in pairs(t) do
			p.push(ret, customFn(v, k, t))
		end
	end
	
	return ret
end

---------------------------------------------------------------------------------
-- function: recursiveConcat(t: table, sep?: string, i?: number, j?: number)
-- 
-- Takes all values of this table and any subtables then recursively goes through then
-- and adds them to new table, then joins concatnates that table.
---------------------------------------------------------------------------------
function p.recursiveConcat(t, sep, k, l)
	checkType('recursiveConcat', 1, t, 'table')
	checkType('recursiveConcat', 2, sep, 'string', true)
	checkType('recursiveConcat', 3, k, 'number', true)
	checkType('recursiveConcat', 4, l, 'number', true)
	
	return table.concat(p.flat(t), sep or '', k, l)
end

---------------------------------------------------------------------------------
-- function: each(t: table, callbackfn: function(v: any, k?: number, t?: table)
-- 
-- Executes a provided function once for each table element.
---------------------------------------------------------------------------------
function p.each(t, callbackfn)
	checkType('each', 1, t, 'table')
	checkType('each', 2, callbackfn, 'function')
	
	for k, v in ipairs(t) do
		callbackfn(v, k, t)
	end
	return t
end
---------------------------------------------------------------------------------
-- function: eachNamed(t: table, callbackfn: function(v?: any, k: any, t?: table, i?: number)
-- 
-- Executes a provided function once for key-value pair in a table
---------------------------------------------------------------------------------
function p.eachNamed(t, callbackfn)
	checkType('eachNamed', 1, t, 'table')
	checkType('eachNamed', 2, callbackfn, 'function')
	
	local i = 0
	for k, v in pairs(t) do
		i = i+1
		callbackfn(v, k, t, i)
	end
	return t
end


---------------------------------------------------------------------------------
-- function: format(t: table)
-- 
-- Takes the table and takes each value as an argument and puts it through `string.format()`.
---------------------------------------------------------------------------------
function p.format(t)
	checkType('format', 1, t, { 'table', 'number', 'string' }, true)
	
	t = t or ''
	local tp = type(t)
	local mt = getmetatable(t)
	
	if tp == 'string' or tp == 'number' or not (t[1] or ''):match('%%%a') then
		if tp == 'number' or mt and mt.__tostring then
			return tostring(t)
		elseif tp == 'table' then
			return table.concat(t, t.sep or t.s or t.seperator or '')
		elseif t == '' then
			return nil
		else
			return t
		end
	end
	
	p.each(t, function(v, k, t)
		local tp = type(v)
		t[k] = 
			p.includes({'string', 'number', 'boolean'}, tp) 
				and tostring(v) 
			or tp == 'table' 
				and table.concat(v, v.sep) 
			or v
	end)
	
	local success, result = pcall(string.format, unpack(t))
	
	if not success then
		local match = { result:match('bad argument #(%d+) .-%(.- expected, got (.-)%)') }
		
		if not match[1] then
			match = { result:match('bad argument #(%d+) .-%((.-)%)') }
		end
		
		if match[1] then
			error(string.format('invalid value (%s) at index %s in table for \'format\'', match[2] ~= 'no value' and match[2] or 'nil', match[1]), 2)
		else
			error(result, 2)
		end
	end
	
	return result
end

---------------------------------------------------------------------------------
-- function: deepCopy(t: table)
-- 
-- Recursively goes through the table and copies it preserving all identities of 
-- the subtables.
--
----------------[ ATTRIBUTION ]--------------
-- This function was taken from `en.wikipedia.org` from `Module:TableTools`.
---------------------------------------------------------------------------------
local function _deepCopy(orig, includeMetatable, already_seen)
	-- Stores copies of tables indexed by the original table.
	already_seen = already_seen or {}
	
	local copy = already_seen[orig]
	if copy ~= nil then
		return copy
	end
	
	if type(orig) == 'table' then
		copy = {}
		for orig_key, orig_value in pairs(orig) do
			copy[_deepCopy(orig_key, includeMetatable, already_seen)] = _deepCopy(orig_value, includeMetatable, already_seen)
		end
		already_seen[orig] = copy
		
		if includeMetatable then
			local mt = getmetatable(orig)
			if mt ~= nil then
				local mt_copy = _deepCopy(mt, includeMetatable, already_seen)
				setmetatable(copy, mt_copy)
				already_seen[mt] = mt_copy
			end
		end
	else -- number, string, boolean, etc
		copy = orig
	end
	return copy
end

function p.deepCopy(orig, noMetatable, already_seen)
	checkType('deepCopy', 3, already_seen, 'table', true)
	
	return _deepCopy(orig, not noMetatable, already_seen)
end

---------------------------------------------------------------------------------
-- function: dumpObject(t: table)
-- 
-- Takes the table and recursively goes through each and every key, creating
-- a string repersenting the whole table
--
-------------------[ ATTRIBUTION ]--------------
-- This function was taken from the media wiki source file (../includes/engines/LuaCommon/lualib/mw.lua)
---------------------------------------------------------------------------------
function p.dumpObject(object)
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
			return string.format('%q', object)
		elseif tp == 'table' then
			if not doneObj[object] then
				if type(object) == 'table' then
					ct[tp] = (ct[tp] or 0) + 1
					doneObj[object] = 'table#' .. ct[tp]
				else
					doneObj[object] = tostring(object)
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
				ret[#ret + 1] = string.rep(' ', indent + 2)
				ret[#ret + 1] = 'metatable = '
				ret[#ret + 1] = _dumpObject(mt, indent + 2, false)
				ret[#ret + 1] = '\n'
			end
			
			local doneKeys = {}
			for key, value in ipairs(object) do
				doneKeys[key] = true
				ret[#ret + 1] = string.rep(' ', indent + 2)
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
				ret[#ret + 1] = string.rep(' ', indent + 2)
				ret[#ret + 1] = '['
				ret[#ret + 1] = _dumpObject(key, indent + 3, false)
				ret[#ret + 1] = '] = '
				ret[#ret + 1] = _dumpObject(object[key], indent + 2, true)
				ret[#ret + 1] = ',\n'
			end
			ret[#ret + 1] = string.rep(' ', indent)
			ret[#ret + 1] = '}'
			return table.concat(ret)
		else
			if not doneObj[object] then
				ct[tp] = (ct[tp] or 0) + 1
				doneObj[object] = table.concat{ tostring(object), '#', ct[tp] }
			end
			return doneObj[object]
		end
	end
	return _dumpObject(object, 0, true)
end
p.dump = p.dumpObject
---------------------------------------------------------------------------------
-- function: logObject(t: table)
--
-- Calls `dumpObject()` on the table then logs it using `mw.log()`.
---------------------------------------------------------------------------------
function p.logObject(...)
	local args
	for i, v, _ in forEachArgs({'any'}, ...) do
		if i == 1 then args = _ end
		_[i] = p.dumpObject(v)
	end
	return mw.oldLog(getCodeLocation(), p.unpack(args or {}))
end
p.log = p.logObject

---------------------------------------------------------------------------------
-- function: tableUtil(t?: table)
-- 
-- Takes the table and makes all the methods above availble. It also includes
-- an option to set a metatable to this table.
---------------------------------------------------------------------------------
function p.tableUtil(...)
	local t, metatable = ...
	local len = select('#', ...)
	local doTable
	
	error('TableUtil is deprecated')
	
	if not (((type(t) == 'table' or type(metatable) == 'table') or t == nil and metatable == nil) and len <= 2) then
		t = { ... }
	end
	
	local methods = {}
	local t = t or {}
	
	local mt = {
		__index = function(_, k)
			return methods[k]
		end,
	}
	
	if metatable or getmetatable(t) then
		local metatable = getmetatable(t) or metatable
		if metatable.__index then
			setmetatable(methods, { __index = metatable.__index }) 
			metatable.__index = nil
		end
		
		for k, v in pairs(metatable) do
			mt[k] = v
		end
	end
	
	local keys = {
		rawset = rawset,
		rawget = rawget,
		pairs = pairs,
		ipairs = ipairs,
		getmetatable = getmetatable,
		setmetatable = setmetatable,
		next = next,
		pcall = pcall,
		xpcall = xpcall,
		tostring = tostring,
		tonumber = tonumber,
		type = type,
		unpack = unpack,
		len = function(self, countNamed)
			checkType('len', 1, countNamed, 'boolean', true)
			if countNamed then
				return p.length(self)
			else
				return #self
			end
		end,
		
		select = function(self, ops)
			return select(ops, unpack(self))
		end,
	}
	
	for k, v in pairs(keys) do
		methods[k] = v
	end
	
	for k, v in pairs(p) do
		methods[k] = v
	end
	
	return setmetatable(t, mt)
end


-- Finish Module/Exports
return p
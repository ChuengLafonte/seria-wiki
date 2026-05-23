---------------------------------------------------------------------------------
-- LibU: The version of LibraryUtil that does not inject functions into the global table
-- From MediaWiki source file
-- 
-- On import, this script does not expose all functions to the global table.
-- List of functions:
-- function: getCodeLocation(level)
-- function: makeArgNumber(val)
-- function: getParentName(level) [alias: getStackName]
-- function: typeMatches(valType, val, types, nilOk, numberOk)
-- function: generateMsg(name, index, msg, types)
-- function: validateTypes(types)
-- function: checkType(name?: string, pos: number, value: any, types: string|table, nilOk?: boolean)
-- function: checkType(name: 'no value', pos: number, types?: string|table, level?: number)
-- function: checkTypeLight(name, argIdx, arg, expectTypes, nilOk)
-- function: checkArgs(types: table<table<string> | string>, ...arguments?: any) [alias: checkTypeArgs]
-- function: checkTypeMulti(t, types)
-- function: alertDeprecation(name: string, useInstead?: string, level?: number)
-- function: forEachArgs(types: string, ...arguments?: string)
-- function: makeCheckSelfFunction(libraryName: string, varName: string, selfObj?: table, selfObjDesc?: string)
-- function: formattedError(formatStr?: string, level?: number, ...substitions?: string | number)
-- function: formattedAssert(v?: any, formatStr?: string, level?: number, ...substitions?: string | number) [alias: assertTrue]
-- function: assertFalse(v, formatStr, level, ...)
-- function: existsWithoutWanted(title: string)
-- function: inexpensivePageExists(title: string) [alias: pageExists]
-- function: pipeline(...)
-- function: bind(targetFn: function, ...items?: any)
-- 
-- The following methods are modified to a custom one:
-- function: mw.log(...)
-- function: mw.logObject(...)
-- function: mw.oldLog(...)
-- function: mw.oldLogObject(...)
---------------------------------------------------------------------------------
local p = {}
---------------------------------------------------------------------------------
-- Find line/module name via `debug.stacktrace()` for debugging
---------------------------------------------------------------------------------
function p.getCodeLocation(level)
	local trace = debug.traceback('', (level or 1) + 2)
	return ((trace:gsub('\nstack traceback:\n', ''):match('^\t([^\n<>]+):')..':'):gsub('\t?%(tail call%): ?%?', ''))
end
---------------------------------------------------------------------------------
-- Feature: Rewritten Log Methods
---------------------------------------------------------------------------------
-- Store Old Log Methods as `mw.oldLog` and `mw.oldLogObject`
mw.oldLog = mw.log
local oldLog = mw.oldLog
mw.oldLogObject = mw.logObject
local oldLogObject = mw.oldLogObject
-- Modify mw.log to display code location
local logLevel = 2
mw.log = function(...)
	local function newLog(...)
		return oldLog(p.getCodeLocation(logLevel), mw.allToString(...))
	end
	mw.log = newLog
	newLog(...)
	logLevel = 1
end
-- Modify mw.logObject to display code location
-- Note: This takes away the "prefix" feature from `mw.logObject( object, prefix )`
local logObjectLevel = 2
mw.logObject = function(...)
	local function newLog(...)
		return oldLog(p.getCodeLocation(logObjectLevel), mw.dumpObject(...))
	end
	mw.logObject = newLog
	newLog(...)
	logObjectLevel = 1
end

---------------------------------------------------------------------------------
-- Utility Functions
---------------------------------------------------------------------------------
---------------------------------------------------------------------------------
-- Create an argument number/name
---------------------------------------------------------------------------------
function p.makeArgNumber(val)
	return table.concat{ type(val) == 'number' and '#' or '\'', val, type(val) ~= "number" and '\'' or '' }
end
---------------------------------------------------------------------------------
-- Get the nama of a function based off of a stack level using `debug.stracktrace()`
---------------------------------------------------------------------------------
function p.getParentName(level)
	level = (level or 0) + 3
	local stack = debug.traceback('', level) or ''
	
	stack = (stack:gsub('\nstack traceback:\n', '')
		:match('in function ([^\n]+)') or '')
		:gsub('^\'(.-)\'$', '%1')
	
	stack = (stack:match('[<>:]') or stack == '') and '?' or stack
	
	return stack
end
p.getStackName = p.getParentName
---------------------------------------------------------------------------------
-- Utility function to find the index of a value in a table
---------------------------------------------------------------------------------
local function indexOf(t, value)
	if type(t) ~= 'table' then return -1 end
	
	local i = 1
	while t[i] do
		if t[i] == value then return i end
		i = i+1
	end
	
	return -1
end

---------------------------------------------------------------------------------
-- Feature: `checkArgs()` and `checkType()`
---------------------------------------------------------------------------------
---------------------------------------------------------------------------------
-- Helper function for `checkType()` to check of a set of given types matches a value
---------------------------------------------------------------------------------
function p.typeMatches(valType, val, types, nilOk, numberOk)
	local tpTypes = type(types)
	local tn = valType == 'number' and val or tonumber(val)
	local isStringNumber = not not (tn and (types == 'string' or indexOf(types, 'string') ~= -1))
	
	if tpTypes == 'table' and #types == 1 then types = types[1]; tpTypes = 'string' end
	
	if valType == 'nil' and nilOk then
		return true
	elseif val == nil and types == nil then
		return false
	end
	
	if tpTypes == 'string' then
		return (valType == types or (types == 'number' and not not tn)) or (isStringNumber and numberOk)
	end
	
	for i = 1, #types, 1 do
		local v = types[i]
		
		if v == valType or (v == 'number' and tn) or isStringNumber then
			return true
		end
	end
	
	return false
end
---------------------------------------------------------------------------------
-- Format a list of types in an error message for `checkType()` and it's related functions
---------------------------------------------------------------------------------
local function generateTypes(types)
	if type(types) == "string" then 
		return types
	end
	
	local n = #types
	if n == 1 then
		return types[1]
	end
	
	return table.concat(types, '/')
end
---------------------------------------------------------------------------------
-- Format an error message for `checkType()` and related functions
---------------------------------------------------------------------------------
function p.generateMsg(name, index, msg, types)
	local msg = string.format("bad argument %s to '%s' (%s)",
		p.makeArgNumber(index),
		name,
		types and (generateTypes(types)..' expected, got '..msg) or msg
	);
	return msg
end
---------------------------------------------------------------------------------
-- Data for `checkType()` 
---------------------------------------------------------------------------------
local validTypes = {
	['string'] = true,
	['number'] = true,
	['nil'] = true,
	['table'] = true,
	['boolean'] = true,
	['function'] = true,
	['any'] = true,
}
---------------------------------------------------------------------------------
-- Check if a set of given types is valid
---------------------------------------------------------------------------------
function p.validateTypes(types)
	local tp = type(types)
	local len = tp == 'table' and #types
	
	if not types 
	or (tp ~= "table" and tp ~= "string")
	or types == "" 
	or (tp == 'table' and len > 7) then 
		return false
	end
	
	if (tp == 'string' or tp == 'table') and len == 0 then return true end
	if len == 1 and tp == 'table' then types = types[1]; tp = 'string' end
	
	if tp == "string" then
		return not not validTypes[types]
	end
	
	for i = 1, len, 1 do
		if not validTypes[types[i]] then
			return false
		end
	end
	
	return true
end
---------------------------------------------------------------------------------
-- function: checkType
--
-- modes:
--	type checker: checkType(name?: string, pos: number, value: any, types: string|table, nilOk?: boolean)
--	no value error: checkType(name: 'no value', pos: number, types?: string|table, level?: number)
--------------------------------------------------------------------------------
-- Options to types:
--	*name: Changes the function to the value provided
--	*base: Makes the value provided have the correct number base
---------------------------------------------------------------------------------
function p.checkType(name, argIdx, arg, expectTypes, nilOk)
	local isConstructor, tpName

	if name == true then
		name = nil
		isConstructor = true
	end
	
	tpName = type(name)
	local tpTypes = type(expectTypes)
	local tpArg = type(arg);
	
	-- Argument overloads
	if (tpName == "number" and (tpArg == 'table' or tpArg == 'string') and tpTypes ~= 'string' and tpTypes ~= 'table') or (name == nil and argIdx == nil) then
		nilOk = expectTypes
		expectTypes = arg or 'string'
		arg = argIdx or nil
		argIdx = name or 1
		name = nil
	end
	
	name = name or expectTypes.name
	local t = {}
	local tpArg = type(arg)
	t.checkType = error
	
	-- Check if types match and if there is an error
	local level = isConstructor and 1 or (tpName == "number" and name or 0)
	local numOk = expectTypes.numberOk or expectTypes.numOk
	local matches = name ~= 'no value' and p.typeMatches(tpArg, arg, expectTypes, nilOk, (expectTypes and numOk))
	local isError = (tpName == "string" and name ~= 'no value') or not matches
	
	local fName
	local tn
	local numArg = expectTypes.numArg
	
	if expectTypes and expectTypes.numArg and not expectTypes.base then
		expectTypes.base = 10
	end
	
	-- Optimize as much as possible
	if isError then
		fName = (name ~= 'no value' and tpName ~= 'number') and name or p.getParentName(name == 'no value' and expectTypes or level)
	end
			
	if name == 'no value' then
		t.checkType(p.generateMsg(fName, argIdx, arg and 'no value' or 'value expected', arg), (expectTypes or level)+3)
	end
	
	-- Check if `base` is valid
	if expectTypes.base and (expectTypes.base < 2 or expectTypes.base > 36) then
		error('the option "base" must be between 2 and 36', level+2)
	end
	
	-- Return if `numArg` is valid
	if expectTypes and #expectTypes == 0 then
		return arg
	end
	
	if numArg or numOk then
		tn = (tpArg ~= 'string' and tpArg ~= 'number') and nil or tonumber(arg, expectTypes.base)
	end
	
	if (tpArg == 'string' or tpArg == 'number') and numArg and tn then
		return tn
	end
	
	if tpArg == 'number' and numOk then
		return arg
	end
	
	-- Error if types did not match
	if not matches then
		local msg = p.generateMsg(fName, argIdx, tpArg, expectTypes)
		t.checkType(msg, level+3)
	end
	
	-- Check if argument is convertable to a number
	if expectTypes and expectTypes.base and not tn then
		fName = p.getParentName(name == 'no value' and expectTypes or level);
		local msg = p.generateMsg(fName, argIdx, 'value is not convertable to a base '..expectTypes.base..' number')
		t.checkType(msg, level+3)
	elseif expectTypes and expectTypes.base and tn then
		return tn
	end
	
	return arg
end

---------------------------------------------------------------------------------
-- "Lite" version of `checkType()` due to performance issues
---------------------------------------------------------------------------------
function p.checkTypeLight(name, argIdx, arg, expectTypes, nilOk)
	local isMulti = expectTypes.lower ~= string.lower -- Check using properties instead of type()
	local argType = type(arg)
	
	if arg == nil and nilOk then
		return arg
	end
	
	if isMulti then
		for _, v in pairs(expectTypes) do
			if argType == v then
				return arg
			end
		end		
		
		return ({ checkType=error }).checkType(string.format("bad argument #%d to '%s' (%s expected, got %s)", argIdx, name, table.concat(expectTypes, '/'), argType), 3)
	end
	
	if argType ~= expectTypes then
		({ checkType=error }).checkType(string.format("bad argument #%d to '%s' (%s expected, got %s)", argIdx, name, expectTypes, argType), 3)
	end
	
	return arg
end

---------------------------------------------------------------------------------
-- function: checkArgs(types: table<table<string> | string>, ...arguments?: any)
--
-- Checks a given set of arguments against a list of types in a compact and streamlined manner
---------------------------------------------------------------------------------
function p.checkArgs(types, ...)
	p.checkTypeLight('checkArgs', 1, types, { 'string', 'table' })
	
	if type(types) == 'string' then
		types = { types }
	end
	
	local t = {}
	local ret = { ... }
	-- Number of arguments
	local n = select('#', ...)
	t.checkTypeArgs = error
	local level = type(types.level) == "number" and (types.level >= -1 and types.level or -types.level) or 0
	local len = #types
	
	local toIter
	if types.strict then
		toIter = (len >= n and len or n)
	else
		toIter = len
	end
	local fName
	
	for i = 1, (len >= n and len or n) do
		local any
		
		-- Variables
		local curTypes = type(types[i]) ~= "table" and { types[i] } or types[i]
		local emptyOk = curTypes.emptyOk or curTypes.emptyok
		local nilOk = curTypes.nilOk or curTypes.nilok
		local numberOk = curTypes.numberOk or curTypes.numOk or curTypes.numok or curTypes.numberok
		local val = ({ ... })[i]
		local argIndex = select('#', ...) + 1
		
		if i > #types and types.strict then
			fName = p.getParentName(level);
			
			t.checkTypeArgs(('bad argument #%d to \'%s\' (%d arguments expected, got %d)'):format(i, fName, #types, i), level+3)
		end
		
		-- Case for nilOk
		if nilOk and emptyOk == nil then
			emptyOk = true
		end
		
		-- Special Case if nilOk is false and emptyOk is false
		if nilOk and emptyOk == false then
			table.insert(curTypes, 'nil')
		end
		
		-- Special case for the 'any' type
		if indexOf(curTypes, 'any') ~= -1 or (emptyOk == false and #curTypes == 0) then
			any = true
			curTypes = {
				numberOk = numberOk,
				nilOk = nilOk,
				emptyOk = emptyOk,
			}
		end
		
		local tpVal = type(val)
		
		-- If argument is nil, but not empty, and the expected type is 'any' and nilOk is false, error
		if nilOk == false and any and not (n < len and i > n) and tpVal == 'nil' then
			fName = p.getParentName(level);
			-- Error message #1
			local valueExpected = ('bad argument #%d to \'%s\' (value expected)'):format(i, fName)
			
			t.checkTypeArgs(valueExpected, level+3)
		end
		
		-- If argument is empty
		if n < len and i > n and (not emptyOk or tpVal == 'nil') then
			if any then
				fName = p.getParentName(level);
				local valueExpected = ('bad argument #%d to \'%s\' (value expected)'):format(i, fName)
				
				-- Value expected error if argument is empty
				t.checkTypeArgs(valueExpected, level+3)
			elseif not nilOk or (nilOk and emptyOk == false) then
				fName = p.getParentName(level);
				
				-- No value error
				t.checkTypeArgs(p.generateMsg(fName, argIndex, 'no value', generateTypes(curTypes)), level+3)
			end
		else
			-- Else check its type as normal
			ret[i] = p.checkType((level ~= 0 and level+1 or 1), i, val, curTypes, nilOk)
		end
	end
	
	return unpack(ret)
end
p.checkTypeArgs = p.checkArgs
---------------------------------------------------------------------------------
-- Alias for `checkType`
---------------------------------------------------------------------------------
function p.checkTypeMulti(t, types)
	p.checkType(1, t, 'table')
	p.checkType(2, types, 'table')
	
	t.checkTypeMulti = error
	
	for i = 1, #types do
		p.checkType(true, i, t[i], types[i])
	end
end

---------------------------------------------------------------------------------
-- function: alertDeprecation(name: string, useInstead?: string, level?: number)
-- 
-- Throws a derecation error message with an optional substitute for the deprecated function
---------------------------------------------------------------------------------
function p.alertDeprecation(...)
	local name, useInstead, level = p.checkArgs({ 
		'string', { 'string', nilOk=true }, { 'number', nilOk=true } 
	}, ...)
	local t = {}
	t.alertDeprecation = error
	
	if type(name) == "table" then
		name, useInstead = unpack{
			name.name or name[1],
			name.useInstead or name.use or name[2],
		}
	end
	
	t.alertDeprecation(string.format(
		'function %q is deprecated%s', 
		name or p.getParentName(),
		useInstead and string.format(', use the function %q instead', useInstead) or ''
	), (level or 0)+3)
end

---------------------------------------------------------------------------------
-- function: forEachArgs(types: string, ...arguments?: string)
-- 
-- Returns an iterator which iterates over the list of given arguments, and asserts the type of each argument.
-- Useful in variable argument functions.
---------------------------------------------------------------------------------
function p.forEachArgs(types, ...)
	p.checkType(1, types, { 'string', 'table' })
	
	local startIndex = types.startIndex and types.startIndex-1 or 0
	local required = types.required or 0
	local i = 0+(startIndex or 0)
	
	local args = { ... }
	local lim = select('#', ...)
	local ind = indexOf(types, 'any')
	local t = {}
	t.checkType = error
	
	return function()
		i = i + 1
		
		if lim < required and i > lim then
			if ind ~= -1 then
				t.checkType(p.generateMsg(p.getParentName(), i, 'value expected'), 3)
			elseif ind == -1 then
				p.checkType('no value', i, types, 1)
			end
		end
		
		if i <= lim then
			if ind == -1 then
				p.checkType(1, i, args[i], types, types.nilOk)
			end
			
			return i, args[i], args
		else
			return nil, nil
		end
	end, ...
end

---------------------------------------------------------------------------------
-- function: makeCheckSelfFunction(libraryName: string, varName: string, selfObj?: table, selfObjDesc?: string) 
-- 
-- Creates a function which asserts that the given object is an instance of another.
---------------------------------------------------------------------------------
function p.makeCheckSelfFunction(libraryName, varName, selfObj, selfObjDesc)
	if type(varName) == 'table' then
		varName = libraryName
		selfObjDesc = selfObj
	end
	if type(libraryName) == 'table' then
		selfObj = libraryName
		libraryName = varName
	end
	
	return function(self, method)
		if self ~= selfObj then
			method = method or p.getParentName();
			({ checkSelf=error })['checkSelf'](string.format(
				"%s: invalid %s. Did you call .%s() with a dot instead of a colon, i.e. " ..
				"%s.%s(...) instead of %s:%s(...)?",
				libraryName, selfObjDesc or 'self object', method, varName, method, varName, method
			), 3)
		end
	end
end

---------------------------------------------------------------------------------
-- function: formattedError(formatStr?: string, level?: number, ...substitions?: string | number)
-- 
-- Throws an error but with an option to use `string.format()`.
---------------------------------------------------------------------------------
function p.formattedError(formatStr, level, ...)
	p.checkTypeLight('formattedError', 2, level, { 'number' }, true)

	local t = { ... }

	if #t > 0 then
		for i, v in ipairs(t) do
			t[i] = tostring(v)	
		end
	end
	
	local formatStr = type(formatStr) == 'string' and formatStr or 'unknown error'
	
	return error(string.format(formatStr, unpack(t)), tonumber(level) == 0 and level or (level or 1) + 1)
end

---------------------------------------------------------------------------------
-- function: formattedAssert(v?: any, formatStr?: string, level?: number, ...substitions?: string | number)
-- 
-- Works like the native `assert()` but allows an option for using `formattedError()`.
---------------------------------------------------------------------------------
function p.formattedAssert(v, formatStr, level, ...)
	local formatStr = type(formatStr) == 'string' and formatStr or 'assertion failed!'
	
	if not v then 
		p.formattedError(formatStr, level == 0 and level or (level or 1) + 1, ...)
	else
		return v
	end
end
p.assertTrue = p.formattedAssert
---------------------------------------------------------------------------------
-- Inverse alias for `formattedAssert()`
---------------------------------------------------------------------------------
function p.assertFalse(v, formatStr, level, ...)
	local formatStr = type(formatStr) == 'string' and formatStr or 'assertion failed!'
	
	if v then 
		p.formattedError(formatStr, level == 0 and level or (level or 1) + 1, ...)
	else
		return v
	end
end

---------------------------------------------------------------------------------
-- function: mw.title.existsWithoutWanted(title: string)
-- 
-- Checks if a page exists without marking it as a Special:WantedPages. title is name including namespace (if there is one)
-- [WARNING] Since this doesn't us backlinking (what causes it to be "wanted") the value returned for this function will not be reevaluated for a potentially infinite time after the page is created/deleted. Edits/null edits/purging will update it properly.
-- [EXPENSIVE] Note that just like a normal page `exists` check, this is an expensive function (although it runs faster)
---------------------------------------------------------------------------------
function p.existsWithoutWanted(title)
	local frame = mw.getCurrentFrame()
	
	-- PROTECTIONEXPIRY is a magic word that lets us check a page in a roundabout way without marking it as wanted.
	-- Trick taken from: https://www.mediawiki.org/wiki/Extension_talk:Scribunto/Lua_reference_manual#Avoid_creating_a_wanted_page_link_when_checking_if_page_exist
	return frame:callParserFunction('PROTECTIONEXPIRY:edit', title) ~= ''
end

---------------------------------------------------------------------------------
-- function: inexpensivePageExists(title: string)
-- 
-- Might not actually be faster, but doesn't count as an expensive parser function call
-- [WANTEDPAGES] If file doesn't exist, using this method will mark it as a Special:WantedPages
---------------------------------------------------------------------------------
function p.inexpensivePageExists(title)
    local t = mw.title.new(title)
    if not t then
        return nil
    end
    return t:getContent()
end
p.pageExists = p.inexpensivePageExists
---------------------------------------------------------------------------------
-- function: pipeline(...)
-- 
-- Creates a function pipeline, where each argument is stored then passed to a function
-- when it is found in the arguments list, then it is invoked.
---------------------------------------------------------------------------------
function p.pipeline(...)
	local value = p.checkArgs('any', ...)
	local prependArgs = { value }
	local t, functionFound
	
	for k, v in p.forEachArgs({ 'any', startIndex=2 }, ...) do
		if type(v) ~= 'function' then
			if #prependArgs == 0 then
				prependArgs[#prependArgs+1] = value
			end
			prependArgs[#prependArgs+1] = v
		else
			t = { pcall(v, unpack(prependArgs)) }
			
			functionFound = true
			if not t[1] then
				t[2] = tostring(t[2])
				
				-- Error message if invocation failed
				p.formattedAssert(
					t[1], 
					'Exception in calling function%s%s at que posistion #%d: %s', 
					2, 
					t[2]:match('^(.-):(.-):') and ' in module "'..t[2]:match('^(.-):(.-):')..'"' or '',
					t[2]:match('^(.-):(.-):') and ' at line '..({ t[2]:match('^(.-):(.-):') })[2]..' called' or '',
					k,
					t[2]:gsub('^(.-):(.-):', '')
				)
			end
			table.remove(t or {}, 1)
			prependArgs = t
		end
	end
	
	
	if functionFound then
		return unpack(t)
	else
		return ...
	end
end

---------------------------------------------------------------------------------
-- function: bind(targetFn: function, ...items?: any)
-- 
-- Wraps `targetFn` in a new function which serves as a proxy prepending any arguments
-- given when the new function is called
---------------------------------------------------------------------------------
function p.bind(targetFn, ...)
	local mt = getmetatable(targetFn)
	if not (mt and (mt.__call or mt.__isClass)) then
		p.checkType(1, targetFn, 'function')
	end
	
	local args = { ... }
	args.n = select('#', ...)
	
	return function(...)
		local len = select('#', ...)
		local callArgs = {}
		local passedArgs = { ... }
		
		for i = 1, args.n, 1 do
			callArgs[i] = args[i]
		end
		
		if len > 0 then
			for i = args.n + 1, args.n + len, 1 do
				callArgs[i] = passedArgs[i - args.n]
			end
		end
		
		return targetFn(unpack(callArgs, 1, args.n + len))
	end
end

return p

require('Module:LibraryUtil')
local autoloadsConfig = require('Module:LoadLib/Autoloads')
local titleObj = mw.title.getCurrentTitle()
local pagename = titleObj.fullText

local implicitLoads = {}
local autoloads = autoloadsConfig.callList
local moduleList = autoloadsConfig.moduleList

local function toCamelCase(s)
	return s
		:gsub(' (.)(.*)', function(a, b)
			return a:upper() .. b
		end)
		:gsub('[^%a]+', '')
		:gsub('^(.)(.*)', function(a, b)
			return a:lower() .. b
		end)
end

for _, v in ipairs(moduleList) do
	implicitLoads[v] = 1
	implicitLoads['Module:' .. v] = 1
end
moduleList = nil

local function isNaN(v)
	return type(v) == 'number' and tostring(v) == '-nan'
end

local function fallback(...)
	local val
	local values = { ... }
	local lim = select('#', ...)
	local i = 0
	local def = ({...})[lim]
	
	local f = {
		[0] = false,
		['f'] = false,
		['false'] = false,
		['0'] = false,
		['-0'] = false,
		['+0'] = false,
		['off'] = false,
		['of'] = false,
		['n'] = false,
		['no'] = false,
		[false] = false,
	}
	
	while lim > i do
		i = i+1
		val = values[i]
		if val ~= nil then
			local v = f[val]
			
			if v == nil and not isNaN(val) then
				return true
			else
				return false
			end
		end
	end
	
	return def
end

return function(...)
	local globalTable, lib, options = checkArgs({ 'table', { 'table', nilOk = true }, { 'table', nilOk = true } }, ...)
	local lib = lib or {}
	
	local options = options or {}
	local setVars, doAutoLoads, substVars = 
		fallback(options.setVars, options.set, options[1], false),
		fallback(options.doAutoLoads, options.doLoads, options.auto, options[2], true),
		fallback(options.substVars, options.subst, options[3], false)
		
	local skip = {}
	options.skip = options.skip or {}
	
	if #options.skip > 0 then
		for _, v in ipairs(options.skip) do
			options.skip[v] = 1
		end
	end
	
	if doAutoLoads then
		for key, value in pairs(lib) do
			local mName = type(value) == "string" and value or value[1] or value.m or value.module
			
			if implicitLoads[mName] or options.skip[mName] then
				skip[mName] = true
			end
		end
		
		for key, value in pairs(autoloads) do
			local mName = type(value) == "string" and value or value[1] or value.m or value.module or ''
			
			if not skip[mName] then
				if type(key) == 'number' then
					table.insert(lib, value)
				else
					lib[key] = value
				end
			end
		end
	end
	
	-- Iterate over supplied module names/variables/fields to get
	for key, value in pairs(lib) do
		local tpKey = type(key)
		local varToSet, fieldToGet, setVarsTmp, tmp
		-- If key is a table, set some values
		if type(value) == "table" then
			varToSet, fieldToGet, setVarsTmp, tmp = unpack{
				value.varToSet or value.value or value.values or value[3],
				value.fieldToGet or value.field or value[2],
				value.loadVars or value.setVars or value[4],
				value.module or value.m or value[1],
			}
		end	
		
		-- Set module name
		local value = tmp and tmp or value
		local oldVal = value
		
		-- require() enhancements
		if value:match('^%/') then
			value = titleObj.fullText .. value
		elseif value:match('^%.%/') then
			value = titleObj.baseText .. value:gsub('%.', '')
		end
		
		if value:match('%$%{.-%}') then
			local tpSubstVars = type(substVars)
			if value:match('%${parent}') or value:match('^%${base}$') then
				value = value:gsub('%${parent}', titleObj.baseText):gsub('%${base}', titleObj.baseText)
			end
			if value:match('%${root}') then
				value = value:gsub('%${root}', titleObj.rootText)
			end
			if value:match('%${fullpage}') then
				value = value:gsub('%${fullpage}', titleObj.fullText)
			end
			if value:match('%${page}') then
				value = value:gsub('%${page}', titleObj.text)
			end
			if value:match('%${subpage}') then
				value = value:gsub('%${subpage}', titleObj.subpageText)
			end
			if tpSubstVars == "table" then
				for k, v in pairs(substVars) do
					substVars[k:lower()] = v
				end
				for var in value:gmatch('%${var:(.-)}') do
					v = substVars[tostring(var):lower()]
					if not v then error('Unknown variable "' .. var .. '" in require path "' .. value .. '"', 2) end
					
					value = value:gsub('%${var:' .. var .. '}', v)
				end
			end
			if tpSubstVars ~= "table" and value:match('%${var:(.-)}') then
				error('Require path variables must have subsituion table to draw from (missing option `substVars`)', 2)
			end
		end
		
		local mName = 'Module:' .. value:gsub('Module:', '')
		
		-- Load actual module
		local res = globalTable.require(mName)
		local lib = res
		
		-- Key the module was saved in
		local savedKey = tpKey == "number" and toCamelCase(mName:gsub('Module:', '')) or key
		
		local function err(msg, ...)
			error(string.format('Invalid loader settings for module %q for index %q: ' .. msg, mName, key, ...), 3)
		end
		
		local tpFieldToGet = type(fieldToGet)
		local tpVarToSet = type(varToSet)
		
		-- Check types on variable to be set
		if tpFieldToGet ~= "string" and tpFieldToGet ~= "nil" then
			err('function name to load must be a string or nil')
		end
		
		-- If the function supplied a singular field to get, set the global table index as the field
		if (varToSet or fieldToGet) and tpVarToSet ~= "table" and tpKey == "number" then
			globalTable[varToSet or fieldToGet] = lib[fieldToGet] or lib[varToSet]
		-- Extra case if the user did not specify a field to get
		elseif tpKey ~= "number" and fieldToGet then
			globalTable[key] = lib[fieldToGet]
		end
		
		-- Extra case if user set the values to get as a table
		if tpVarToSet == "table" and not fieldToGet then
			for k, v in pairs(varToSet) do
				local tpK = type(k)
				-- Check types on variables to be set
				if tpK ~= "number" and tpK ~= "string" then
					error(string.format(
						'Invalid table index type in loader settings for module %q for index %q: index must be a string', mName, key
					), 2)
				-- Also check types on the value to search for
				elseif type(v) ~= "string" then
					error(string.format(
						'Invalid table index value type in loader settings for module %q for index %q: index must be a string', mName, key
					), 2)
				-- If the function is not found, error
				elseif not lib[v] then
					error(string.format(
						'Invalid loader configuration settings for module %q at index %q: specified function %q not found on %q', mName, key, v, mName
					), 2)
				end
				if tpK == "number" then
					globalTable[v] = lib[v]
				else
					globalTable[k] = lib[v]
				end
			end
		end
		
		-- Else, set the loaded variable name as the module
		if tpKey ~= "number" and not fieldToGet then
			globalTable[savedKey] = lib
		end
		
		-- If the option `setVars` is true, set global variables as required module methods
		if not fieldToGet and (setVarsTmp or setVars) and type(lib) == "table" then
			for k, v in pairs(lib) do
				globalTable[k] = v 
			end
		end
	end
	
	return globalTable
end
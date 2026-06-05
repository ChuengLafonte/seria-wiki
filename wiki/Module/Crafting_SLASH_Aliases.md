local loader = require('Module:Loader')

local string, table, minion, data, templates, utils =
	loader.require('String', 'Table', 'Minion', 'Crafting/Data', 'Crafting/Templates', 'Crafting/Utils')
local minionData = loader.loadData('Minion/Data')

local controlKeys = { 'id' }

local function templateReplacements(values, default)
	local tb, allFields = {}, {}
	
	if type(values) ~= 'table' then values = { values } end
	table.merge(allFields, table.filter(table.namedKeys(default), function(v)
		return not table.findIndex(controlKeys, v)
	end))
	
	local g = { id = values.id }
	for _, v in ipairs(allFields) do g[v] = default[v] end
	
	for _, item in ipairs(values) do -- ipairs: won't read global settings
		local repLs = {}
		local function repl(str)
			local function _repl(args)
				for _, sym in ipairs(args) do
					str = str:gsub(('{%s}'):format(sym), repLs[sym] or '')
				end
				return str
			end
			-- Apply all replacements
			local special, numeric = string.split('os', ''), {}
			local ret = _repl(special) -- special(1st)
			for i in ret:gmatch('{(%d+)}') do
				table.push(numeric, i)
			end
			local ret = _repl(numeric) -- numeric after special(1st)
			local ret = _repl(special) -- special(2nd) after numeric
			return ret
		end
		
		local loc = { default[1] }
		local raw, id, vars
		if type(item) == 'table' then
			raw = item[1]
			id = item.id or g.id or item[1]
			vars = table.slice(item, 2)
			for _, v in ipairs(table.merge({}, table.namedKeys(item), allFields)) do loc[v] = item[v] or g[v] end
		else
			raw, id = item, g.id or item
			for _, v in ipairs(allFields) do loc[v] = g[v] end
		end
		
		for i,v in ipairs(type(vars) == 'table' and vars or { vars }) do
			repLs[tostring(i-1)] = tostring(v):gsub('%%','%%%%') -- so that it does not incorrectly remove '%'s
		end
		
		repLs['o'], repLs['s'] = raw, raw
		id = repl(id)
		repLs['s'] = id
		
		for k, v in pairs(loc) do
			-- note: __NIL__ is to override a certain value with key existing in template with the nil value
			loc[k] = v ~= '__NIL__' and repl(v) or nil
		end
		
		tb[id] = loc
	end
	
	return tb
end

local function main()
	local craftingData, templatesTable = {}, {}
	-- Process Data from Crafting/Templates --
	local MAX_RUNS = 20
	local allow_continue, made_change, currentProcess, templateStorage, installed, runs = true, false, 1, {}, {}, 0
	while allow_continue and ((currentProcess == 1) or (table.length(templateStorage) > 0)) do
		if (currentProcess > 1) and (not made_change) then allow_continue = false end
		runs, made_change = runs + 1, false
		if runs > MAX_RUNS then error('Too many iterations in processing templates') end
		for key, values in pairs(currentProcess == 1 and templates or templateStorage) do
			local default = data[key]
			if not default then
				if allow_continue then
					templateStorage[key] = values
				else
					error('Key "'..key..'" no default')
				end
			else
				made_change = true
				table.push(installed, key)
				table.merge(templatesTable, templateReplacements(values, default))
			end
		end
		for _, key in ipairs(installed) do
			templateStorage[key] = nil
		end
		currentProcess, installed = currentProcess + 1, {}
	end
	
	local minionRecipes = {}
	
	table.each(table.keys(minionData), function(name)
		local _, highestCraftable = minion.peakStat(name)
		for i = 1, highestCraftable do
			local recipe = minion._getRecipe(name, i)
			if recipe then
				minionRecipes[recipe['Output']] = recipe
			end
		end
	end)
	
	craftingData = table.mapWith(table.merge({}, templatesTable, data), function(k, v)
		v = type(v) == 'table' and v or { v }
		return table.merge(v, utils.versionChange(utils._parseRecipe(v[1], k)), { Output = v['Output'] })
	end)
	
	return table.merge(craftingData, minionRecipes)
end

-- For Debugging
-- local p = { main = main }
-- return p

-- Actual Usage
return main()
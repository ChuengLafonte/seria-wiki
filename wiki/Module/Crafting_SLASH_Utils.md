local loader = require('Module:Loader')
local string, table =
	loader.require('String', 'Table')

local p = {}
local cArgVals = { 'A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3' }
local cArgValsT = { 'A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3' }

-- "Version change": performing a matrix transpose to the recipe table
function p.versionChange(t)
	local temp = {}
	for i = 1, 9 do
		temp[cArgVals[i]] = t[cArgValsT[i]]
	end
	for _, v in ipairs(cArgVals) do
		t[v] = temp[v]
	end
	return t
end

function p._parseRecipe(str, query)
	function err(reason)
		error(('Syntax error while trying to parse slot indicator "%s"%s'):format(str, reason and (' (%s)'):format(reason) or ''))
	end
	function parseSlot(str)
		-- returns unordered list of all slots indicated
		local args = string.split(str, '')
		local tb = {}
		local row = ''
		local flag = false
		for _, c in ipairs(args) do
			if c == '*' then
				if row == '' or not flag then -- treat '*' as row selector
					row = 'ABC'
					flag = true
				else
					for _, r in ipairs(string.split(row, '')) do
						table.push(tb, r .. '1')
						table.push(tb, r .. '2')
						table.push(tb, r .. '3')
					end
					flag = false
				end
			elseif string.match(c, '[ABC]') then
				if flag then
					err('Unused column specifier')
				else
					row = c
					flag = true
				end
			elseif string.match(c, '[123]') then
				if row == '' then
					err('Row number used before column specifier')
				else
					for _, r in ipairs(string.split(row, '')) do
						table.push(tb, r .. c)
					end
					flag = false
				end
			else
				err('Illegal character')
			end
		end
		if flag then err('Unused column specifier') end
		return table.Set(tb):values()
	end
	function each(substr)
		local args = string.matchAll(substr, '[ABC123*]+%s+".-"')
		local temp = {}
		for _, v in ipairs(args) do -- for each ingredient of that recipe
			v = v[1]
			local arg1, arg2 = string.match(v, '([ABC123*]+)%s+"(.-)"')
			for _, w in ipairs(parseSlot(arg1)) do -- for each slot placement of that ingredient
				temp[w] = arg2
			end
		end
		return temp
	end
	
	local ret = {}
	local splited = string.split(str or '', '%s*//%s*')
	
	if table.length(splited) > 1 then
		for i, substr in ipairs(splited) do -- for each recipe (animated slot)
			local temp = each(substr)
			for _, v in ipairs(cArgVals) do
				ret[v] = table.push(ret[v] or {}, temp[v] or '')
			end
			ret['Output'] = table.push(ret['Output'] or {}, query)
		end
		for k, v in pairs(ret) do
			ret[k] = table.concat(v, ';')
		end
	else
		ret = each(str)
		ret['Output'] = query
	end
	
	return ret
end

p.cArgVals = cArgVals
p.cArgValsT = cArgValsT

return p
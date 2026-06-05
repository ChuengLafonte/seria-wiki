local loader = require('Module:Loader')

local string, table, yesno, rarityTier, invslot, statModule, petItemMdl =
	loader.lazy.require('String', 'Table', 'Yesno', 'RarityTier', 'Inventory slot', 'Statname', 'Pet Item')
local petData, petAliases, rarityAliases =
	loader.lazy.loadData('Pet/Data', 'Pet/Aliases', 'RarityTier/Aliases')

local p = {}
local arrowsymbol = '➡'

local scale_functions = {
	linear = function(lv, base, per)
		return (base or 0) + lv * per
	end,
	Parrot = function(lv, base, per)
		local maxed = 15
		return math.ceil(.01 * lv * (maxed - 1) + 1)
	end
}

-- Helper functions
local function range(n)
	local t = {}
	for i = 1, tonumber(n) do t[#t + 1] = i end
	return t
end
local function rarityOrder(rarity)
	return rarityTier._getTier(rarity).order
end

function p.getPet(pet, getAdditionalInfo)
	local pet_ = pet:lower():gsub(' pet$', '')
	pet_ = petAliases[pet_] or string.ucfirst(pet_)
	local d = petData[pet_]
	-- returns the data, the pet name[, the base level, the max level]
	if getAdditionalInfo and d then
		local baselv, maxlv = p.getBaseMax(pet)
		return d, pet_, baselv, maxlv
	end
	return d, pet_
end

function p.getBaseMax(pet)
	local data, pet = p.getPet(pet)
	local baselv, maxlv
	if pet and data.level then
		baselv, maxlv = data.level, data.level
	elseif pet and data.levels then
		baselv, maxlv = data.levels:match('(%d+)[^%d](%d+)')
	end
	return tonumber(baselv) or 0, tonumber(maxlv) or 100
end

function p.discloseRarities(pet, returnAsTable)
	local data, pet = p.getPet(pet)
	local ret = data.rarities
	if (type(ret) == 'string') then
		local petRarities = ret:upper():gsub('[^%a]', '')
		ret = string.split(petRarities, '')
	end
	if yesno(returnAsTable, false) then
		return table.map(ret, function(v)
			return rarityAliases[v:lower()] or v
		end)
	end
	return table.concat(table.map(ret, function(v)
		return ('{{R|%s}}'):format(v)
	end), ' / ')
end

--------------------------------------------------------------------
--	A general utility to calculate the value of a specific set of stats for a specific level/rarity
--------------------------------------------------------------------
function p._getStatByTable(statTable, petlevel, rarity, baselv, options)
	options = options or {}
	local petitem = options.petitem
	local finalStatListActual = {}
	local finalStatListRounded = {}
	for statCode, statValue in pairs(statTable) do
		local reqRarity = statValue.req and rarityAliases[statValue.req:lower()] or nil
		if not (statValue.req and rarityOrder(rarity) < rarityOrder(reqRarity)) then
			local lvl = statValue.level or statValue.lvl or statValue.bonus or statValue[1]
			local base = statValue.base or statValue[2] or 0
			local num
			if tonumber(petlevel) then
				num = base + (tonumber(petlevel) - baselv) * lvl
			elseif petlevel == 'bonus' then
				num = lvl
			end
			finalStatListActual[statCode] = num
		end
	end
	if type(petitem) == 'string' and petitem ~= '' then
		petItemMdl._transformStatTable(finalStatListActual, petitem, { level = petlevel })
	end
	for k, v in pairs(finalStatListActual) do
		finalStatListRounded[k] = math.floor(v * 100) / 100 -- round down to 2 decimal places
	end
	return finalStatListActual, finalStatListRounded
end

--------------------------------------------------------------------
--	A general utility to get text of an ability variable
--------------------------------------------------------------------
function p._getVariable(pet, raritykey, index, petlevel, includeExactValue)
	local data, pet, baselv, maxlv = p.getPet(pet, true)
	local variable = data.variables[raritykey][index]
	
	local this = (' (Pet: %s; Rarity: %s; Index: %s)'):format(pet, raritykey, index)
	if not variable then error('Variable table missing.' .. this) end
	if not variable.color then error('Variable arg missing: "color"' .. this) end
	if not (variable.per_lvl or variable.eval) then
		return error('Variable arg missing: "per_lvl"/"eval"' .. this, 2)
	end
	
	local eval = scale_functions[variable.eval or 'linear']
	
	local num
	if tonumber(petlevel) then
		local levels_increased = tonumber(petlevel) - baselv
		num = eval(levels_increased, variable.base, variable.per_lvl)
	elseif petlevel == 'bonus' then
		num = variable.per_lvl
	end
	
	local rounded = variable.round_down and math.floor(num) or math.floor(num * 100 + 0.5) / 100 -- round OFF to 2 d.p.
	includeExactValue = (not variable.round_down and includeExactValue) and (math.abs(num - rounded) > 1e-9) or false
	
	rounded = variable.is_roman and string._toRoman(rounded) or rounded
	num = variable.is_roman and string._toRoman(num) or num
	
	if petlevel == 'bonus' then return num end -- return exact value for leveling bonuses
	
	return includeExactValue and
		string.makeTitle(tostring(rounded), ('Rounded off to 2 decimal places;&#10;The exact value is %s.'):format(num))
		or rounded
end

-------------------------------------------------------
-- A general utility to generate a pet template through pet, level, rarity, id
-------------------------------------------------------
function p.petTemplateCreator(pet, level, rarity, id, options) -- level can be a table of two values; id can be custom.
	local function numericOutput(min, max)
		if (not min or not max or min == max) then
			return min or max
		else
			return min .. arrowsymbol .. max
		end
	end
	
	options = options or {}
	local data, pet, baselv, maxlv = p.getPet(pet, true)
	
	local min_, max_ = level, level
	if type(level) == 'table' then
		min_, max_ = level[1], level[2]
	end
	min_, max_ = tonumber(min_), tonumber(max_)
	local twovals = not not min_ and not not max_ and (min_ ~= max_)
	
	local leveldisplay = twovals and ('%s%s%s'):format(min_, arrowsymbol, max_) or min_
	
	local raritykey = rarityAliases[rarity:lower()]
	local stats, heldItem, variables = data.variables[raritykey].stats or data.stats, data.heldItem, data.variables
	local raritynum = rarityOrder(raritykey) + 1
	local petname = variables[raritykey] and variables[raritykey].petname or pet
	local petimage = variables[raritykey] and variables[raritykey].petimage
	
	local statStr = {}
	local _, statMinValuesRounded = p._getStatByTable(stats, min_, raritykey, baselv, { petitem = options.petitem })
	local _, statMaxValuesRounded = p._getStatByTable(stats, max_, raritykey, baselv, { petitem = options.petitem })
	for key, _ in pairs(statMinValuesRounded) do
		local sdt = statModule._getstatdata(key)
		table.push(statStr, ('&7%s: &a%s%s%s'):format(
			sdt.name,
			(statMinValuesRounded[key] < 0 and '' or '+'),
			numericOutput(statMinValuesRounded[key], statMaxValuesRounded[key]) or '',
			sdt.percent and '%' or ''
		))
	end
	statStr = table.concat(statStr, '/') .. '//'
	if statStr == '//' then
		statStr = ''
	end
	
	local ab_names, ab_tooltips = data.abilities.name, data.abilities.tooltip or data.abilities.tooltips
	
	local abilityStr = {}
	if ab_tooltips and (#ab_names == #ab_tooltips) then
		local abilityList = variables[raritykey].ability_indices or range(variables[raritykey].ability_count)
		
		for _, i in ipairs(abilityList) do
			local name = ab_names[i]
			if not ab_tooltips[i] then error(pet .. ' Pet: desc and tooltip length mismatch') end
			local desc = ab_tooltips[i]
			
			local vars = variables[raritykey]
			if vars then
				for k in desc:gmatch('{(%d+)}') do
					local j = tonumber(k)
					if not vars[j] then error(('Variable for {%s} missing value (Pet: %s; Rarity: %s)'):format(i, pet,
							raritykey))
					end
					local min = p._getVariable(pet, raritykey, j, min_, false)
					local max = twovals and p._getVariable(pet, raritykey, j, max_, false)
					local subst = numericOutput(min, max)
					desc = subst and desc:gsub(('{%d}'):format(j), subst) or desc
				end
			end
			
			table.push(abilityStr, ('&6%s/&r%s'):format(name, desc:gsub('^/+(.*)', '%1'):gsub('(.-)/+$', '%1')))
		end
	end
	abilityStr = table.concat(abilityStr, '//') .. '//'
	
	local extraStr = ''
	if heldItem then
		local heldItemTooltip = heldItem.tooltip or heldItem.tooltips
		extraStr = (heldItem and heldItemTooltip and (raritykey == rarityAliases[heldItem.req:lower()]))
			and ('&6Held Item: %s/&r%s//'):format(heldItem.name, heldItemTooltip:gsub('^/+(.*)', '%1'):gsub('(.-)/+$', '%1'))
			or ''
	elseif options.petitem then
		if type(options.petitem) == 'string' and options.petitem ~= '' then
			extraStr = petItemMdl.heldItemTooltip(options.petitem)
		end
	end
	
	extraStr = extraStr .. (data.isPassive
		and '&8This pet\'s perks are active/&8even when the pet is not/&8summoned!//'
		or '')
	
	return { pet, petname, data.petType, leveldisplay, statStr, abilityStr, extraStr, r = raritykey, id = id,
		image = petimage }
end

function p.petNameWithRarity(name, rarity)
	-- rarity can be aliased (Module:RarityTier/Aliases)
	return ('%s %s Pet'):format(string.ucfirst(rarityTier._getTier(rarity).name or name), name)
end

function p.petItemInfo(petItemName)
	return {
		name = petItemMdl.getName(petItemName),
		description = petItemMdl.getDescription(petItemName),
	}	
end

return p
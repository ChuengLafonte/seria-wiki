local loader = require('Module:Loader')
local getArgs = require('Module:Arguments').getArgs
local string, table, yesno, uitext = loader.require('String', 'Table', 'Yesno', 'UIText')
local potionData, potionAliases = loader.loadData('Potion/Data', 'Potion/Aliases')

local p = {}
local unknownDisplay = '&r&f&l???&r'
local offsetIngredients = {
	'Glowstone Dust',
	'Enchanted Glowstone Dust',
	'Enchanted Glowstone'
}
-------------------------------------------------------
-- Generates table for Module:Inventory slot/Templates
-------------------------------------------------------
function p.getPotionsTemplate()
	local function toTable(v)
		local t = type(v) == 'table' and table.deepCopy(v, true) or {v}
		return t
	end
	local function colorCode(col)
		local temp = uitext.getFormatting(col):match('^[0-9a-z]$')
			and uitext.getFormatting(col)
			or uitext.getColorCode(col)
		return (temp or ''):match('^[0-9a-z]$') and temp or 'f'
	end
	local function effectText(effect, level, duration, onbase)
		if not level or level < 0 then return end
		local dt = potionData[effect]
		if dt then
			local g_desc = (onbase and dt.basedesc) or dt.desc or unknownDisplay
			
			variables = toTable(dt.vars)
			
			local desc
			local color = dt.ttColor or colorCode(dt.color or '&f')
			
			desc = g_desc
			if level > 0 then
				for i, var in ipairs(variables) do
					desc = desc:gsub(('{%d}'):format(i-1), var[level] or unknownDisplay)
				end
			end
			
			desc = desc:gsub('{%d+}', unknownDisplay)
			
			return ('&%s%s %s &r&f%s/&r%s//&r'):format(
				color, effect, onbase and '' or (level > 0 and string._toRoman(level) or '?'),
				onbase and '' or (duration and ('(%s&f)'):format(duration) or ''), desc
			)
		else
			return unknownDisplay
		end
	end
	local function generateTooltip(potionname, level, onbase)
		local value = potionData[potionname]
		
		local localret = {}
		local duration, composite = value.duration, value.composite
		if type(duration) == 'table' then duration = duration[level] end
		
		local tooltip
		
		if composite then
			for i, eff in ipairs(toTable(composite)) do
				if eff == 'self' then
					tooltip = effectText(potionname, level, duration, onbase)
				else
					local eff = toTable(eff)
					local e, l = eff[1], eff[2] or 1
					if type(l) == 'table' then l = l[level] end
					local compDuration = composite.duration
					if type(compDuration) == 'table' then compDuration = compDuration[level] end
					tooltip = effectText(e, l or 0, compDuration or duration, onbase)
				end
				table.push(localret, tooltip)
			end
		else
			tooltip = effectText(potionname, level, duration, onbase)
			table.push(localret, tooltip)
		end
		
		return table.concat(localret)
	end
	
	local ret = {}
	for potionname, value in pairs(potionData) do
		local name = ('%s Potion'):format(potionname)
		
		local rarityTbl = toTable(value.rarity)
		
		for level = 1, value.maxLevel or 0, 1 do
			local nameBase = ('%s Potions'):format(potionname)
			local nameRoman = ('%s %s Potion'):format(potionname, string._toRoman(level))
			local nameArabic = ('%s %s Potion'):format(potionname, level)
			
			local tooltip = generateTooltip(potionname, level, false)
			local rarity = rarityTbl[level] or 'C'
			local raritytext = rarityTbl[level] and '{l}' or '{r}&l???'
			table.push(ret, { nameRoman, name, tooltip, raritytext, r = rarity })
			-- table.push(ret, { nameArabic, name, tooltip, raritytext, r = rarity, title = '{r}' .. nameRoman })
			if level == 1 then
				tooltip = generateTooltip(potionname, level, true)
				table.push(ret, { name, name, tooltip, raritytext, r = rarity, title = '{r}' .. nameBase })
			end
		end
	end
	
	return ret
end
-------------------------------------------------------
-- Generates table for Module:Item/Variants
-------------------------------------------------------
function p.expandPotionAll()
	local ret = {}
	for potionname, value in pairs(potionData) do
		ret[#ret + 1] = ('%s Potion'):format(potionname)
	end
	return ret
end
function p.expandPotionType()
	local ret = {}
	for potionname, value in pairs(potionData) do
		local t = {}
		for level = 1, value.maxLevel or 0, 1 do
			t[#t + 1] = ('%s %s Potion'):format(potionname, string._toRoman(level))
		end
		ret[('%s Potion'):format(potionname)] = t
	end
	return ret
end

-- Function for getting a potion recipe, mainly used for potion UI.
function p._potionRecipe(potion)
	local function makePot(name, tier)
		return ('%s %s Potion'):format(name, string._toRoman(tier))
	end
	local function findIngre(ingredients, lv)
		-- returns the ingredient needed and the offset
		if ingredients[lv .. 'text'] then
			return nil
		end
		for i = lv, 1, -1 do
			if ingredients[i] then
				return ingredients[i], lv - i
			end
		end
	end
	local potion = (potion or ''):gsub('%s*[Pp]otion', '')
	local name, tier = potion:match('%s*(%S.*)%s+([%dIVX]+)')
	name = potionAliases[(name or potion):lower()]
	tier = string._toArabic(tier or 1) or 1
	local pd = potionData[name]
	
	if not pd then
		return string._error('Cannot find potion \"' .. potion .. '\"')
	end
	if tier > pd.maxLevel or tier < 0 then
		return string._error('Invalid level in potion \"' .. potion .. '\" (Maximum is ' .. pd.maxLevel .. ')')
	end
	
	local basePotion = pd.ingredients and pd.ingredients.basePotion or 'Awkward Potion'
	local basePotionRaw = basePotion:gsub('%s*[Pp]otion', '')
	local basePotionUsedForLevel = pd.ingredients and pd.ingredients.basePotionUsedForLevel
	
	local ingredient, ingredientLink, base
	local ingre, offset = findIngre(pd.ingredients, tier)
	if not ingre then
		return {
			string._error('Potion \"' .. potion .. '\" is not obtainable by brewing.')
		}
	end
	if basePotionUsedForLevel then
		ingredient = makePot(ingre, tier)
		base = makePot(basePotionRaw, tier)
	else
		if offset == 0 then
			ingredient = ingre
			base = basePotion
		else
			ingredient = offsetIngredients[offset]
			ingredientLink = 'Potions#Modifiers'
			base = makePot(name, tier - offset)
		end
	end
	
	return {
		ingredient = ingredient,
		ingredientLink = ingredientLink,
		base = base,
		output = makePot(name, tier),
	}
end

-- Function that returns the number of brewable potion
function p._brewableCount(potion)
	local potion = (potion or ''):gsub('%s*[Pp]otion', '')
	local name, tier = potion:match('%s*(%S.*)%s+([%dIVX]+)')
	name = potionAliases[(name or potion):lower()]
	tier = string._toArabic(tier or 1) or 1
	local pd = potionData[name]
	
	if pd and pd.ingredients then
		local count = 0
		for i = 1, pd.maxLevel do
			if not pd.ingredients[i .. 'text'] then
				count = count + 1
			end
		end
		return count
	end
	return -1
end

return p
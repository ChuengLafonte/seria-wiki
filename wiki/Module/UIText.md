--Get Required Modules
local getArgs = require('Module:Arguments').getArgs
local loader = require('Module:Loader')

local string, table, lu, yesno, stats, statAliases, rarityTier, zones =
	loader.lazy.require('String', 'Table', 'LibraryUtil', 'Yesno', 'Statname', 'Statname/Aliases', 'RarityTier', 'Zone')

local potionData, potionAliases, enchantData, enchantAliases, rarityData, rarityAliases, colorAliases, uitextdata, gemstonedata, zoneData =
	loader.lazy.loadData('Potion/Data', 'Potion/Aliases', 'Enchantment/Data', 'Enchantment/Aliases', 'RarityTier/Data', 'RarityTier/Aliases', 'Color/Aliases', 'UIText/Data', 'Gemstone/Data', 'Zone/Data')

local checkType = lu.checkTypeLight

-- Begin Exports
local p = {}

uitextdata = table.deepCopy(uitextdata, true)
local tooltipFormatting, customFormatting = uitextdata.conversions or {}, uitextdata.custom or {}

for k, v in pairs(gemstonedata.slots) do
	customFormatting[k] = v.ttColor:gsub('&', '')
end

for k, v in ipairs(potionData) do
	potionData[k].color = v.color:gsub('([A-Z])', function(l)
		return '_'..l:lower()
	end)
end

function p.applyReplacements(val)

	local function replaceStats(statname)
		local prefix = statname:match('^([%-%+]?[%.%dkm,]+%%?)%s*')
		statname = string.trim((statname:gsub('^([%-%+]?[%.%dkm,]+%%?)%s*', '')))
		stat = statAliases[statname:lower():gsub('%s', ' ')]
		
		if not stat then
			return "\\stat{" ..statname.. "}"
		end
		
		return ('&%s%s%s %s&r'):format(tooltipFormatting[stats._getstatdata(stat).color], prefix and prefix..' ' or '', stats._getstatdata(stat).character, string.ucfirst(stat))
	end
	
	local function replaceRarities(rarityName)
		local rarity = rarityAliases[string.trim((rarityName:lower():gsub('%s', ' ')))]
		
		if not rarity then
			return "\\rarity{" ..rarityName.. "}"
		end
		
		return ('&%s&l%s&r'):format(p.getRarityColor(rarity), rarityData[rarity].name)
	end
	
	local function replaceZones(zoneName)
		local zone = zones._getZoneData(string.trim(zoneName), true)
		
		if not zone then
			return "\\zone{" ..zoneName.. "}"
		end
		
		return ('&%s%s&r'):format(p.getZoneColor(zoneName), zone.name)
	end
	
	local function replacePotions(potionName)
		local oldPot = potion
		local suffix = potion:match('%s+([ivxIVX%d]+)')
		local potPrefix = potion:match('%s*[Pp]oti?o?n?')
		local potion = potionAliases[string.trim(potionName:gsub('%s+([ivxIVX%d]+)', ''):gsub('%s+[Pp]oti?o?n?', ''):lower())]
		local n = string._toNumber(suffix or '')
		
		if not potion or (n and n > potionData[potion].maxLevel) then 
			return '\\potion{'..potionName..'}'
		end
		
		return ('&%s%s%s%s&r'):format(tooltipFormatting[potionData[potion].color:lower()], potion, suffix and ' '..string._toRoman(suffix) or '', potPrefix and ' Potion' or '')
	end
	
	local function replaceEnchants(enchantName)
		local oldEnch = enchantName
		local suffix = enchantName:match('%s+([ivxIVX%d]+)')
		local enchant = enchantAliases[string.trim(enchantName:gsub('%s+[Ee]ncha?n?t?m?e?n?t?s?', ''):gsub('%s+([ivxIVX%d]+)', ''):lower())]
		local n = string._toNumber(suffix or '')
		
		if not enchant then
			return '\\enchant{'..enchantName..'}'
		end
		
		assertFalse(n and n > enchantData[enchant].max, 'Enchantment escape "\\enchant{%s}" is out of range (max is %s, got %s)', 4, oldEnch, enchantData[enchant].max, n)
		
		return ('&9%s%s&r'):format(enchant, suffix and ' '..string._toRoman(suffix) or '')
	end
	
	local ret = (string.unicodeConvert(val)
		:gsub('&amp;', '&')
		:gsub('\\sta?t?%{(.-)%}', replaceStats)
		:gsub('\\poti?o?n?%{(.-)%}', replacePotions)
		:gsub('\\ra?r?i?t?y?%{(.-)%}', replaceRarities)
		:gsub('\\zo?n?e?%{(.-)%}', replaceZones)
		:gsub('\\ench?a?n?t?m?e?n?t?%{(.-)%}', replaceEnchants)
	)
	return ret
end
---------------------------------------------------------------------------------
-- Temlate: UIText
-- 
-- Makes making UI's alot easier
---------------------------------------------------------------------------------
function p.main(frame)
	local args = getArgs(frame)
	local val = args[1] or args["t"] or args["text"]
	
	return string.pcall(p._main, val)
end

---------------------------------------------------------------------------------
-- Template: UIText Module access point
---------------------------------------------------------------------------------
function p._main(val)
	checkType('_main', 1, val, 'string')
	return (p.applyReplacements(val)
		:gsub('\\', '&#92;')
		:gsub('/', '&#47;')
		:gsub('\n', '/')
		:gsub('\\r', '\r')
		:gsub('\\t', '\t')
		:gsub('\\v', '\v')
		:gsub('\\b', '\b')
		:gsub('\\n', '/')
		:gsub('&#92;', '\\\\')
		:gsub('&#47;', '\\/')
	)
end

---------------------------------------------------------------------------------
-- function: getStatColor(statname: string, raw: boolean)
-- 
-- Gets the In-game color code of a stat (if raw, returns the color instead)
---------------------------------------------------------------------------------
function p.getStatColor(statname, raw)
	checkType('getStatColor', 1, statname, { 'string' })
	raw = raw or false
	
	if not stats.isStatAlias(statname) then return false end
	
	local statColor = stats._getstatdata(statname).color
	return raw and statColor or tooltipFormatting[statColor]
end

---------------------------------------------------------------------------------
-- function: getRarityColor(rarity: string, raw: boolean)
-- 
-- Gets the In-game color code of a rarity (if raw, returns the color instead)
---------------------------------------------------------------------------------
function p.getRarityColor(rarity, raw)
	checkType('getRarityColor', 1, rarity, { 'string' })
	raw = raw or false
	local rarityColor = rarityTier._getTier(string.trim(rarity:lower()):gsub('%s', ' ')).color
	return raw and rarityColor or tooltipFormatting[rarityColor]
end
---------------------------------------------------------------------------------
-- function: getZoneColor(zoneName: string, raw: boolean)
-- 
-- Gets the In-game color code of a zone (if raw, returns the color instead)
---------------------------------------------------------------------------------
function p.getZoneColor(zoneName, raw)
	checkType('getZoneColor', 1, zoneName, { 'string' })
	raw = raw or false
	local zone = zones._getZoneData(string.trim(zoneName), true)
	local color = zone and zone.color or nil
	return color and p.getColorCode(color, raw) or nil
end

---------------------------------------------------------------------------------
-- function: getColorCode(color: string)
-- 
-- Gets the In-game color code of a color (if raw, returns the color instead)
---------------------------------------------------------------------------------
function p.getColorCode(color, raw)
	checkType('getColorCode', 1, color, { 'string' })
	raw = raw or false
	local color = colorAliases[string.trim(color:lower()):gsub('%s', '_')]
	return raw and color or tooltipFormatting[color]
end

---------------------------------------------------------------------------------
-- function: getFormatting(color: string, text: string, ampersand: boolean)
-- 
-- Gets the In-game tooltip formatting
-- (If there is text, will wrap with &..color..text, this can be overridden)
-- Also works for stats, rarities and colors
---------------------------------------------------------------------------------
function p.getFormatting(color, text, ampersand)
	checkType('getFormatting', 1, color, { 'string', 'table' })
	checkType('getFormatting', 2, text, { 'string', 'table', 'number' }, true)
	amp = ampersand or (text and true or false)
	
	local code
	color = string.trim(string.lower(color))
	if color:match('^&[0-9a-z]$') then
		code = color:match('^&([0-9a-z])$')
	else
		code = tooltipFormatting[string.gsub(color, '%s', '_')] or customFormatting[color] or p.getStatColor(color) or p.getRarityColor(color) or p.getZoneColor(color)
	end
	
	return (amp and code and '&' or '')..(code or color)..(text or '')
end

---------------------------------------------------------------------------------
-- function: tooltipBreak(line: string, maxchar: number)
-- 
-- returns a list of strings that is broken down with maxchar set as the max.
-- line length, with formatting strings *included*
-- (since this is how collection UIs are handled)
---------------------------------------------------------------------------------
function p.tooltipBreak(line, maxchar)
	local t = { line }
	while true do
		local lastline = t[#t]
		if (#(t[#t]) <= maxchar) then
			break
		end
		-- choose break point
		local pos = lastline:sub(1, maxchar + 1):find(' %S*$')
		if not pos then
			pos = lastline:find(' ');
		end
		if not pos then
			break
		end
		-- find preceding color codes
		local colcode = ''
		local temp = lastline:sub(1, pos):gsub('\\\\', ''):gsub('\\&', '')
		local matches = {}
		for v in string.gmatch(temp, '&[0-9a-fk-o]') do
			table.push(matches, v)
		end
		colcode = table.concat(matches):gsub('.-(&[0-9a-f][^0-9a-f]*)$', '%1')
		-- split line at pos
		t[#t] = lastline:sub(1, pos - 1)
		t[#t + 1] = colcode .. lastline:sub(pos + 1, #lastline)
	end
	return t
end

-- Finish Module/Exports
return p

-- forced sync
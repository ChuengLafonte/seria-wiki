---------------------------------------------------------------------------------
-- Module:Link
-- This Module is used to house all linking templates on the wiki.
--
-- TABLE OF CONTENTS
--  *Template: CollectionLink
--  *Template: EnchantmentsLink
--  *Template: ReforgingLink
--  *Template: AchievementLink
--  *Template: PotionName
--  *Template: PotionsLink
--  *Template: AttributeLink
--  *Template: PowerStoneLink
--  *Template: FileLink
--  *Template: ParserLink
---------------------------------------------------------------------------------
local p = {}
local loader = require('Module:Loader')
local string, table, yesno, color, libraryutil, arguments =
	loader.require('String', 'Table', 'Yesno', 'Color', 'LibraryUtil', 'Arguments')
local enchant_data_raw, enchant_aliases_raw, potion_data, potion_aliases =
	loader.loadData('Enchantment/Data','Enchantment/Aliases', 'Potion/Data', 'Potion/Aliases')
	
local enchant_data = {}
for k, v in pairs(enchant_data_raw) do
	enchant_data[k:lower()] = v
end

local enchant_aliases = {}
for k, v in pairs(enchant_aliases_raw) do
	enchant_aliases[k:lower()] = v
end

local enchant_name_table = {}
for k, v in pairs(enchant_data_raw) do
	enchant_name_table[k:lower()] = k
end

local getArgs = arguments.getArgs
local mergeArgsSyntax = arguments.mergeArgsSyntax
local checkType = libraryutil.checkTypeLight

local bossCollections = {
	['Bonzo'] = 'Bonzo Head',
	['Scarf'] = 'Scarf Head',
	['The Professor'] = 'The Professor Head',
	['Professor'] = 'The Professor Head',
	['Thorn'] = 'Thorn Head',
	['Livid'] = 'Livid Head',
	['Sadan'] = 'Sadan Head',
	['Maxor'] = 'Wither Skeleton Skull',
	['Goldor'] = 'Wither Skeleton Skull',
	['Storm'] = 'Wither Skeleton Skull',
	['Necron'] = 'Wither Skeleton Skull',
}
local slayer_icons = {
	['Zombie Slayer'] = 'Rotten Flesh',
	['Spider Slayer'] = 'Web',
	['Wolf Slayer'] = 'Raw Mutton',
	['Enderman Slayer'] = 'Ender Pearl',
	['Vampire Slayer'] = 'Redstone',
	['Blaze Slayer'] = 'Blaze Rod',
}
local align_aliases = {
	['l'] = 'left',
	['c'] = 'center',
	['r'] = 'right',
	['t'] = 'thumb',
	['n'] = 'none',
}

---------------------------------------------------------------------------------
-- Template:CollectionLink
--
-- Makes a link that links to a specific collection tier
---------------------------------------------------------------------------------
function p.collectionLink(frame)
	local args = getArgs(frame)
	
	local collection = args[1]
	local tier = args[2]
	local showIcon = args.showIcon or args.icon or args.image or args.img
	
	return p._collectionLink( collection, tier, showIcon )
end

function p._collectionLink( collection, tier, showIcon )
	showIcon = yesno(showIcon, false)
	
	-- We want to show LVL in some cases, but never read it
	local inter = collection:match('%s([Ll][Vv][Ll])') or collection:match('%s([Tt]ier)') or collection:match('%s([Ll]evel)')
	if inter then
		collection = collection:gsub('%s'..inter, '')
		inter = ' ' .. inter
	else
		inter = ''
	end
	-- if the collection is set to 'none'
	if collection:lower() == 'none' then return '[[File:Barrier.png|21px|link=]]&nbsp;' .. color._colorTemplates('red', 'None') end
	
	if (not tier) then
		local str = string._splitNameAndTier(collection)
		collection = str[1]
		tier = str[2]
	end
	collection = string._delDoubleSpace(collection)
	
	if tier and not tier:find('%d') then tier = string._toArabic(tier) end
	
	local img = ''
	
	if collection == 'Professor' then collection = 'The Professor' end
	
	if slayer_icons[collection] and showIcon then
		img = '[[File:' .. slayer_icons[collection] .. '.png|21px|link=' .. collection .. ']] '
	elseif bossCollections[collection] and showIcon then
		img = '[[File:' .. bossCollections[collection] .. '.png|x21px|link=' .. collection .. (tier and '#' .. string._toRoman(tier) or '') .. ']] '
	elseif showIcon then
		img = tier and ('[[File:' .. collection .. '.png|21px|link=' .. collection .. '#' .. string._toRoman(tier) .. ']] ')
			or ('[[File:' .. collection .. '.png|21px|link=' .. collection .. ']] ')
	end
	
	return tier and (img .. '[[' .. collection .. '#' .. string._toRoman(tier) .. '|' .. collection .. inter .. '&nbsp;<code>' .. string._toRoman(tier) .. '</code>]]')
		or (img .. '[[' .. collection .. ']]')
end

-----------------------------------------------------------------------------
-- Template:EnchantmentsLink
--
-- Makes a link that links to a specific enchantment
-----------------------------------------------------------------------------
function p.enchantmentsLink(frame)
	local args = getArgs(frame)
	
	local enchant = args[1]
	
	return p._enchantmentsLink(enchant, {
		alt = args.alt or args[2],
		link = args.link,
		book = args.book or args.b,
		format = args.format or args.f,
		nolink = args.nolink or args.nl,
		showComma = args.showComma or args.c,
	})
end

-----------------------------------------------------------------------------
-- Template:EnchantmentsLink Module Access Point
-----------------------------------------------------------------------------
function p._enchantmentsLink(enchant, options)
	checkType('_enchantmentsLink', 1, enchant, 'string', true)
	checkType('_enchantmentsLink', 4, options, 'table', true)
	
	local options = options or {}
	local alt, link, format, nolink, book, showComma = 
		options.alt,
		options.link,
		yesno(options.format, true),
		yesno(options.nolink, false),
		yesno(options.book, false),
		yesno(options.showComma, false)
	local overrideAlt = alt
	
	-- Exit if enchant is empty/nil
	if enchant == nil or enchant == '' then return '' end
	
	if not enchant then return '' end
	
	enchant = string._delDoubleSpace(enchant)
	
	if (not book and enchant:lower():find('%s*book$')) then
		enchant = enchant:gsub('%s*[bB][oO][oO][kK]$', '')
		book = true
	end
	
	local tier = nil
	if enchant:match('^(.+) ([%dIVXivx%-]+)$')
		then enchant, tier = enchant:match('^(.+) ([%dIVXivx%-]+)$')
	end
	
	enchant = enchant_data[enchant:lower()] and enchant or enchant_aliases[enchant:lower()]
	if not enchant then
		return string.error('Invalid enchantment name \"' .. enchant .. '\"')
	end
	
	local isUltimate = enchant_data[enchant:lower()].isUltimate or false
	
	-- Turbo-crop Enchant Handling
	if enchant:match('^Turbo-') then
		alt = alt and alt or enchant
		enchant = 'Turbo-Crop'
	end
	
	local maxLevel = enchant_data[enchant:lower()] and enchant_data[enchant:lower()].max or 5
	
	if tier and not string.match(tier, '%-') then
		tier = string._toRoman(tier)
	elseif tier and tier:match('%-') then
		local min, max = tier:lower():match('([%divx]+)%s*%-%s*([%divx]+)')
		min, max = string._toArabic(min), string._toArabic(max)
		
		if min >= max or min <= 0 or max <= 0 then
			return string.error('Invalid enchantment range %s-%s', string._toRoman(min), string._toRoman(max))
		end
		
		tier = string._toRoman(min) .. '-' .. string._toRoman(max)
	end
	
	local mainText = table.concat{
		(alt and (overrideAlt and overrideAlt or alt) or enchant_name_table[enchant:lower()]),
		(overrideAlt and '' or (tier and (' ' .. tier) or '')),
		showComma and not overrideAlt and ', ' or '',
	}
	if format and not overrideAlt then
		mainText = color._colorTemplates(isUltimate and 'light purple' or 'blue', mainText)
	end
	if not nolink then
		mainText = ('[[%s|%s]]'):format(enchant_data[enchant:lower()].link or link or enchant_name_table[enchant:lower()], mainText)
	end
	if book then
		mainText = ('%s (%s)'):format(nolink and 'Enchanted Book' or '[[Enchanted Book]]', mainText)
	end
	if format then
		mainText = string.bold(mainText)
	end
	
	return mainText
end

-----------------------------------------------------------------------------
-- Template:ReforgingLink
--
-- Makes a link that links to a specific reforge
-----------------------------------------------------------------------------
function p.reforgingLink(frame)
	local args = getArgs(frame)
	
	local reforge = args[1]
	local text = args['text'] or args[2]
	
	return p._reforgingLink(reforge, text)
end

function p._reforgingLink(reforge, text)
	reforge = string._delDoubleSpace(reforge)
	
	return text and ('[[Reforging#' .. reforge .. '|' .. text .. ']]') or ('[[Reforging#' .. reforge .. '|' .. reforge .. ']]')
end

-----------------------------------------------------------------------------
-- Template:AchievementLink
--
-- Makes a link that links to a specific achievement
-----------------------------------------------------------------------------
function p.achievementLink(frame)
	local args = getArgs(frame)
	
	local achievement = args[1]
	local text = args['text'] or args[2]
	local ach = yesno(args['ach'], false)
	
	return p._achievementLink(achievement, text, ach)
end

function p._achievementLink(achievement, text, ach)
	achievement = string._delDoubleSpace(achievement)
	
	if (text) then
		return '[[Achievements#' .. achievement .. '|' .. text .. ']]'
	elseif (ach) == true then 
		return '[[Achievements#' .. achievement .. '|\"' .. achievement .. '\" Achievement]]'
	else
		return '[[Achievements#' .. achievement .. '|' .. achievement .. ']]'
	end
end

-----------------------------------------------------------------------------
-- Template:PotionsLink
--
-- Makes a link that links to a specific potion
-----------------------------------------------------------------------------
function p.potionName(frame)
	local args = getArgs(frame)
	
	local effect = args[1]
	
	return p._potion(effect, {
		text = args.text or args[2],
		img = args.image or args.img or args.show_image or args.si,
		potion = args.potion or args.pot or args.p or args.sp,
		format = args.format or args.f,
		hover = args.title or args.t,
		bold = args.bold or args.b or args.show_bold or args.sb,
		hashlink = args.hashlink,
	})
end

p.potionsLink = p.potionName

function p._potion(effect, options)
	local options = options or {}
	
	local text, hover, potion, img, format, bold, hashlink =
		options.text,
		options.hover,
		yesno(options.potion),
		yesno(options.img),
		yesno(options.format, true),
		yesno(options.bold, true),
		yesno(options.hashlink, false)
	
	-- Remove any multiple spaces
	effect = string._delDoubleSpace(effect)
	
	--find any invalid characters
	if (effect:match('([%-,%%%.%(%)%{%}%[%]%?/:;]+)')) 
		then return string.error('Invalid characters', effect:match('([%-,%%%.%(%)%{%}%[%]%?/:;]+)'))
	end
	--get whether or not 'Potion' suffix is requested
	local effect = effect:lower()
	if (potion == nil and (string.find(effect, '%s[Pp][Oo][Tt][Ii][Oo][Nn][Ss]?$') or string.find(effect, '%s[Pp][Oo][Tt][Ss]?$'))) then
		potion = true
		plural = (effect:match('(s)$') and true or false)
		effect = effect:lower():gsub('%s[Pp][Oo][Tt][Ii][Oo][Nn][Ss]?$', ''):gsub('%s[Pp][Oo][Tt][Ss]?$', '')
	end
	
	--get tier number
	local tier = string.match(effect:upper(), '^.* ([%dIVX]+)$')
	
	if tier then
		--convert to arabic number
		if (tier:find('[IVX]+')) then tier = string._toArabic(tier)
		elseif (tier:find('%d+')) then tier = tonumber(tier)
		--return error if tier is not matching any valid input
		else return string.error('Invalid potion tier\"' .. tier .. '\"')
		end
	end
	
	--get potion name
	effect = tier and effect:match('^(.*) [%dIVXivx]+$') or effect
	local src_effect = effect --save source input to later use to display error message
	--get name from aliases
	effect = potion_aliases[effect:lower()]
	--return error if effect name is invalid
	if (not effect) then return string.error('Invalid potion name: %s', src_effect) end
	if (not potion_data[effect]) then return string.error('Effect %s is not defined in Potion/Data', effect) end
	
	--check if potion tier is withing the range of 1 to max level
	if (tier ~= nil) then
		if (tier > potion_data[effect].maxLevel or tier <= 0) then return string.error('Potion tier is out of range: "' .. tier .. '"') end
		--convert tier back to roman
		tier = string._toRoman(tier)
	end
	
	local mainText
	if text then
		mainText = text
	else
		mainText = effect
		if tier then
			mainText = mainText .. '&nbsp;' .. tier
		end
		if potion then
			mainText = mainText .. ' Potion' .. (plural and 's' or '')
		end
	end
	if format then
		mainText = color._colorTemplates(potion_data[effect].color, mainText)
	end
	if format and bold then
		mainText = string.bold(mainText)
	end
	if (type(hover) == 'string' and hover ~= '') then
		mainText = string.makeTitle(mainText, hover)
	end
	mainText = ('[[%s|%s]]'):format(hashlink and ('#' .. effect) or (effect .. ' Potion'), mainText)
	
	if img then
		mainText = ('[[File:%s Potion.png|21px]] %s'):format(effect, mainText)
	end
	
	return mainText
end

-----------------------------------------------------------------------------
-- Template:AttributeLink
--
-- Makes a link that links to a specific attribute
-----------------------------------------------------------------------------
function p.attributeLink(frame)
	local args = getArgs(frame)
	
	local attribute = args.attribute or args[1]
	local tier = args.tier or args[2]
	
	return p._attributeLink(attribute, tier)
end

function p._attributeLink(name, tier)
	local attributeTier = tier or (name and name:match(" ([%dIVX]+)$"))
	local attribute = name and name:gsub(" ([%dIVX]+)$", "")
	
	return attribute and ("[[Attributes#%s|<span class=\"color-aqua bold\">%s</span>]]"):format(attribute, attribute .. (attributeTier and (' ' .. attributeTier) or ""))
end

-----------------------------------------------------------------------------
-- Template:PowerStoneLInk
--
-- Makes a link that links to a specific power stone
-----------------------------------------------------------------------------
function p.powerStoneLink(frame)
	local args = getArgs(frame)
	
	local powerStone = args[1]
	local text = args['text'] or args[2]
	
	return p._powerStoneLink(powerStone, text)
end

function p._powerStoneLink(powerStone, text)
	powerStone = string._delDoubleSpace(powerStone)
	
	return text and ('[[Power_Stones#' .. powerStone .. '|' .. text .. ']]') or ('[[Power_Stones#' .. powerStone .. '|' .. powerStone .. ']]')
end

-----------------------------------------------------------------------------
-- Template:FileLink
--
-- Makes file linking a tiny bit easier
-----------------------------------------------------------------------------
function p.fileLink(frame)
	local args = getArgs(frame)
	
	local file = args[1]
	local size = args['size'] or args['s'] or args[2]
	local align = args['alignment'] or args['align'] or args['a']
	local link = args['alt_link'] or args['al']
	local yesno_link = yesno(args['link'] or args['l'])
	
	return p._fileLink(file, size, align, link, yesno_link)
end

function p._fileLink(file, size, align, link, yesno_link)
	
	if (not file:find('%.')) then file = file .. '.png' end
	local text = {}
	text[#text+1] = '[[File:' .. file
	
	if (align) then
		align = align_aliases[align] or align
		text[#text+1] = '|' .. align
	end
	
	if size then text[#text+1] = '|' .. size end
	
	if not link then link = file:match('(.*)%.') end
	
	if yesno_link then text[#text+1] = '|link=' .. link end
	
	text[#text+1] = ']]'
	
	return table.concat(text, '')
end

---------------------------------------------------------------------------------
-- Template:ParserLink
--
-- Creates a link to a parser function on MediaWiki and provide parameter 
-- formatting
-- 
-- See also: Dev:Module:T
---------------------------------------------------------------------------------
function p.parserLink(frame) 
	local args = getArgs(frame, {removeBlanks = false})
	
	if args[1] == '' or not args[1] then return string.error('No title specified.') end
	local multiline = yesno(args['m'] or args['multi'] or args['multiline'], false)
	
	local list = mergeArgsSyntax(args)
	
	return p._parserLink(list, multiline)
end

---------------------------------------------------------------------------------
-- Template:ParserLink Module Access point
---------------------------------------------------------------------------------
function p._parserLink(list, multiline)
	if type(list) ~= 'table' then
		error('bad argument #1 to \"_parserLink\": table expected, got ' .. type(list) .. '', 2)
	end
	
	if #list == 0 then error('No title specified', 2) end
	
	multiline = yesno(list.m or list.mult or list.multiline or multiline, false)
	
	for i = 1, #list, 1 do
		if (type(list[i]) ~= 'string' and type(list[i]) ~= 'number') then
			error('Invalid list entry #' .. i .. ': invalid data type (string/number expected, got ' .. type(list[i]) .. ')', 2)
		end
		list[i] = tostring(list[i])
		
		newLineSep = multiline and '<br>' or ''
		
		if list[i]:gsub(mw.text.nowiki('='), '=', 1):match('=') then
			name, list[i] = list[i]:gsub(mw.text.nowiki('='), '=', 1):match('^(.+)%s*=%s*(.+)$')
			name = string.wrapHtml(name, 'b') .. '&nbsp;=&nbsp;'
		else
			name = ''
		end
		
		if (i == 1) then
			list[1] = '[[mw:Help:Extension:ParserFunctions##' .. list[1] .. '|#' .. list[1] .. ']]'
		end
		
		if (i == 2 and not list[i]:match('[\"\'](.*)[\"\']')) then
			list[2] = mw.text.nowiki(':') .. name .. '<span style="opacity: 0.65;">&lt;' .. list[2] .. '&gt;</span>'
		elseif (i == 2 and list[i]:match('[\"\'](.*)[\"\']')) then
			list[2] = list[2]:gsub('[\"\'](.*)[\"\']', mw.text.nowiki(':') .. name .. '%1')
		end
		
		if (i ~= 1 and i ~= 2 and list[i] == '') then list[i] = newLineSep .. '. .. ' end
		
		if (i ~= 1 and i ~= 2 and not list[i]:match('[\"\'](.*)[\"\']')) then
			list[i] = newLineSep .. mw.text.nowiki('|') .. name .. '<span style="opacity: 0.65;">&lt;' .. list[i] .. '&gt;</span>'
		elseif (i ~= 1 and i ~= 2 and list[i]:match('[\"\'](.*)[\"\']')) then
			list[i] = list[i]:sub(2, -2)
			list[i] = newLineSep .. mw.text.nowiki('|') .. name .. list[i]
		end
	end
	
	return '<span style="font-family: monospace;">&#x7b;&#x7b;' .. table.concat(list, '') .. newLineSep .. '&#x7d;&#x7d;</span>'
end


-- Finish Module
return p

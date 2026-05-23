local loader = require('Module:Loader')
local getArgs = require('Module:Arguments').getArgs

local string, table, yesno, raritytier, currency, linkmodule, color, cache =
	loader.require('String', 'Table', 'Yesno', 'RarityTier', 'Currency', 'Link', 'Color', 'Cache')
local itemData, itemAliases, armorSets = loader.loadData('Item/Data', 'Item/Aliases', 'Armor/Sets')

local apiDataCache = cache.itemApiDataCache
local apiAliasesCache = cache.itemApiAliasesCache
local formatNum = string._formatNum

local p = {}

local lang = mw.getContentLanguage()
local itemImage = itemAliases.itemImage
local itemReplacements = itemAliases.itemReplacements

-- Due to their sizes, don't load these modules until / unless they are needed
local __apidata, __apialiases
function p.getApiData()
	if __apidata then return __apidata end
	__apidata = mw.loadData('Module:Item/ApiData')
	return __apidata
end
function p.getApiAliases()
	if __apialiases then return __apialiases end
	__apialiases = mw.loadData('Module:Item/ApiAliases')
	return __apialiases
end

-----------------------------------------------------------------------------------
-- Template: Resource Display
-- 
-- Displays item and its amount, alongside its image, drop chance, rarity, enchant, etc
-----------------------------------------------------------------------------------
function p.resourceDisplay(frame)
	local args = getArgs(frame)
	local str = args[1]
	local img = yesno(args['image'] or args['img'] or args['i'], true)
	local nolink = yesno(args['nolink'] or args['nl'], false)
	local noErr = yesno(args['noerror'] or args['ne'], false)
	local ignoreOdds = yesno(args['ignoreodds'], false)
	local noImagePadding = yesno(args['noimgpad'], false)
	
	return string.pcall(p._item, str, img, nolink, noErr, false, ignoreOdds, noImagePadding)
end
-----------------------------------------------------------------------------------
-- Template: Item Display
-- 
-- Displays only item, alongside its image, drop chance, rarity, enchant, etc
-----------------------------------------------------------------------------------
function p.itemDisplay(frame)
	local args = getArgs(frame)
	local str = args[1]
	local img = yesno(args['image'] or args['img'] or args['i'], true)
	local nolink = yesno(args['nolink'] or args['nl'], false)
	local noErr = yesno(args['noerror'] or args['ne'], false)
	local ignoreOdds = yesno(args['ignoreodds'], false)
	local noImagePadding = yesno(args['noimgpad'], false)
	
	return string.pcall(p._item, str, img, nolink, noErr, true, ignoreOdds, noImagePadding)
end
-----------------------------------------------------------------------------------
-- Functions for use in other modules
-----------------------------------------------------------------------------------
function p._resourceDisplay(str, img, nolink, noErr, ignoreOdds, noImagePadding)
	return p._item(str, yesno(img, true), nolink, noErr, false, ignoreOdds, noImagePadding)
end
function p._itemDisplay(str, img, nolink, noErrm, ignoreOdds, noImagePadding)
	return p._item(str, yesno(img, true), nolink, noErr, true, ignoreOdds, noImagePadding)
end

-- Module Access Point
function p._item(str, img, nolink, noErr, ignoreAmount, ignoreOdds, noImagePadding)
	local function _getImage(img_, nolink_, item_, nip)
	    if img_ then
	        local extension = nil
	        if pageExists('File:' .. img_ .. '.gif') then
	            extension = 'gif'
	        elseif pageExists('File:' .. img_ .. '.png') then
	            extension = 'png'
	        end
	
	        if extension then
	            return string.makeImage(img_, { extension = extension, size=21, link=nolink_ and '' or item_, alt=img_ }) 
	            .. '&nbsp;' -- making alt `img_` so it can be properly picked up by resource pack
	        end
	    end
	
	    return (nip and '' or string.makeImage('Blank Icon.png', { size = 21, link = '' }) .. '&nbsp;')
	end
	
	local function _getHoverText(num)
		local title
		if num then
			local stacks = math.floor(tonumber(num) / 64)
			local items = tonumber(num) % 64
			num = formatNum(num)
			if stacks + items * 0.01 > 1 then
				local str_stacks = lang:plural( stacks, 'stack', 'stacks' )
				title = items > 0 and ('%s %s plus %s (%s in total)'):format(formatNum(stacks), str_stacks, items, num)
					or ('%s %s (%s items total)'):format(formatNum(stacks), str_stacks, num)
			end
		end
		return num, title
	end
	local function escape(str)
		str = str:gsub(',', ''):gsub('&percnt;', '%%'):gsub('&amp;', '&')
		str = str:gsub('\\\\', '__BACKSLASH__'):gsub('\\!', '__EXCLAMATIONPOINT__'):gsub('\\%', '__PERCENTMARK__'):gsub('\\&', '__AMPERSAND__'):gsub('\\$', '__DOLLARSIGN__')
		return str
	end
	local function unescape(str)
		str = str:gsub('__BACKSLASH__', '\\'):gsub('__EXCLAMATIONPOINT__', '!'):gsub('__PERCENTMARK__', '%'):gsub('__AMPERSAND__', '&'):gsub('__DOLLARSIGN__', '$')
		return str
	end
	
	-- Remove commas and handle escaped characters
	str = escape(str)
	-- Determine whether or not the hover text should be displayed
	local no_hover = str:match('%d+%-+%d+') and true or false
	-- Split main string and comment texts
	local after
	if str:match('%s*[^\\];%s*(.-)$') then
		str, after = str:match('^(.-)%s*;%s*(.+)$')
	end
	str = tostring(str) or ''
	-- Separate item and quantity, and handle invalid syntax
	local item, num, num2
	if not ignoreAmount then
		if str:match('^([%d,%-%?]+%.?[%d,%-]*x? ?or ?[%d,%-%?]+%.?[%d,%-]*x?) (.*)') then
			num, item = str:match('^([%d,%-%?]+%.?[%d,%-]*x? ?or ?[%d,%-%?]+%.?[%d,%-]*x?) (.*)')
		elseif str:match('^([%d,%-%?]+%.?[%d,%-]*x?) (.*)') then
			num, item = str:match('^([%d,%-%?]+%.?[%d,%-]*x?) (.*)')
		elseif noErr then
			return unescape(str)
		else
			item = str
			no_hover = true
			-- return string.error('Invalid Resource list syntax "%s"', str)
		end
		if num and num:match('or') then
			local tempStr = num
			num, num2 = tempStr:match('(.+) ?or ?(.+)')
		end
		-- Handle colors (green = standard, red = only when number is '?')
		text_color = 'Green'
		if (num and num:match('%?')) or (num2 and num2:match('%?')) then 
			no_hover = true
			text_color = 'Red'
		end
		-- Remove unnecessary characters from number
		num = num and num:gsub('[x,]', '')
		num2 = num2 and num2:gsub('[x,]', '')
	else
		-- Extract item string from "A or B" or "Nx" syntaxes
		if str:match('^[%d,%-%?]+%.?[%d,%-]*x? ?or ?[%d,%-%?]+%.?[%d,%-]*x? (.*)') then
			item = str:match('^[%d,%-%?]+%.?[%d,%-]*x? ?or ?[%d,%-%?]+%.?[%d,%-]*x? (.*)')
		elseif str:match('^[%d,%-%?]+%.?[%d,%-]*x? (.*)') then
			item = str:match('^[%d,%-%?]+%.?[%d,%-]*x? (.*)')
		else
			item = str
		end
	end
	-- Handle the calculations performed on the number, then format it
	local formatted_num, formatted_num2, title, title2
	if not (ignoreAmount or no_hover) then
		formatted_num, title = _getHoverText(num)
		formatted_num2, title2 = _getHoverText(num2)
	elseif not ignoreAmount or no_hover then
		formatted_num = num
		formatted_num2 = num2
	end
	
	-- Item Handling
	-- Remove unnecessary characters from item
	item = item:gsub('[%[%]]', '')
	-- Unpack and process aliases
	item = ' ' .. item .. ' '
	for pattern, replace in pairs(itemReplacements) do
		if item:match(pattern) then item = item:gsub(pattern, replace) end
	end
	item = mw.text.trim(item)
	-- Get alternate (displayed) text
	local alt = item
	if item:match('[Bb]locks') then
		alt = item
		item = item:gsub('[Bb]locks', 'Block')
	end
	if item:match('%|') then
		item, alt = item:match('(.*)%|(.*)')
	elseif item:match('[^%%]%!') then
		item, alt = item:match('(.*)%!(.*)')
	end
	-- Item Parameters Parsing
	-- Extract Odds (%...%)
	local odds
	if item:match('%s%%.+%%') then 
		odds = item:match('.*%s%%(.+)%%')
		item = item:gsub('(.*)%s%%.+%%(.*)', '%1%2')
	end
	if alt:match('%s%%.+%%') then 
		odds = alt:match('.*%s%%(.+)%%')
		alt = alt:gsub('(.*)%s%%.+%%(.*)', '%1%2')
	end
	-- Extract Enchant (&...&)
	local enchant
	if item:match('%s&.+&') then 
		enchant = item:match('.*%s&(.+)&')
		item = item:gsub('(.*)%s&.+&(.*)', '%1%2')
	end
	if alt:match('%s&.+&') then 
		enchant = alt:match('.*%s&(.+)&')
		alt = alt:gsub('(.*)%s&.+&(.*)', '%1%2')
	end
	-- Replace Rarity in place ($...$)
	alt = alt:gsub( '%$(.+)%$', function(b) 
		return raritytier._link(unescape(b), nil, nil, true)
	end)
	item = item:gsub('(.*)%s?%$.+%$%s?(.*)', '%1%2')
	item = mw.text.trim(item)
	-- Handle item image
	local item_img = itemImage[item] or item
	-- Convert armor piece string to functional string, pick the proper image (helmet)
	local trimmedArmorName = item:gsub('(.*) [Pp][Ii][Ee][Cc][Ee]$', '%1')
	local armor = armorSets[trimmedArmorName]
	if item:match('(.*) [Pp][Ii][Ee][Cc][Ee]$') then
		item = trimmedArmorName
		item_img = armor and armor[1]
	elseif armor then
		item_img = armor and armor[1]
	end
	-- Convert minion string to functional string, pick the proper image (tier I minion head)
	if item:match('Minion [IVXivx]+$') then
		item = item:gsub('(Minion )[IVXivx]+', '%1')
	elseif item:match('Minion$') then
		item_img = item .. ' I'
	end
	
	-- Return stuff
	if not ignoreAmount then
		local currencyName
		if item:lower():find('^%s*coins?%s*$') then
			currencyName = 'coins'
		elseif item:lower():find('^%s*bits?%s*$') then
			currencyName = 'bits'
		elseif item:lower():find('^%s*gems?%s*$') then
			currencyName = 'gems'
		elseif item:lower():find('^%s*pelts?%s*$') then
			currencyName = 'pelts'
		elseif item:lower():find('^%s*north stars?%s*$') then
			currencyName = 'northStars'
		elseif item:lower():find('^%s*copper%s*$') then
			currencyName = 'copper'
		elseif item:lower():find('^%s*motes?%s*$') then
			currencyName = 'motes'
		elseif item:lower():find('^%s*pests?%s*$') then
			currencyName = 'pests'
		elseif item:lower():find('^%s*bronze medals?%s*$') then
			currencyName = 'bronzeMedals'
		elseif item:lower():find('^%s*silver medals?%s*$') then
			currencyName = 'silverMedals'
		elseif item:lower():find('^%s*gold medals?%s*$') then
			currencyName = 'goldMedals'
		end
		if currencyName then
			return tostring(
				currency._currency(unescape(num), nil, false, false, img, nolink, true, nil, currencyName)
			)
		end
	end
	local amountStr = ''
	if not ignoreAmount then
		amountStr = string.makeTitle(formatted_num and color.ct(text_color, formatted_num .. 'x') or '', title, { ignoreTitleNil = true }) .. '&nbsp;'
		if num2 then
			amountStr = amountStr .. color.ct(text_color, 'or') .. '&nbsp;' ..
				string.makeTitle(formatted_num2 and color.ct(text_color, formatted_num2 .. 'x') or '', title2, { ignoreTitleNil = true }) .. '&nbsp;'
		end
	end
	local ret = {
		(img and _getImage(unescape(item_img), nolink, item, noImagePadding) or ''),
		amountStr,
		nolink and (alt or item) or string.makeLink(item, alt),
		(enchant and ('&nbsp;(%s)'):format(linkmodule._enchantmentsLink(unescape(enchant))) or ''),
		((odds and not ignoreOdds) and ('<sup>(%s)</sup>'):format(odds) or ''),
		after and ' ' .. after or '',
	}
	return (unescape(table.concat(ret)))
end

function p._api( id )
	id = id:upper():gsub(' ', '_')
	
	local key = apiAliasesCache:get(id) or id
	local a, b = apiDataCache:get(key), itemData.items[key]
	
	if a or b then
		return table.merge({}, table.deepCopy(a or {}, true), table.deepCopy(b or {}, true))
	end
end

function p._sellPrice( id )
	local it = p._api( id )
	return it and it.npc_sell_price
end

--Finish Module
return p

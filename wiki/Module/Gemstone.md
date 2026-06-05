local p = {}

local loader = require('Module:Loader')
local getArgs = require('Module:Arguments').getArgs
local mergeArgsSyntax = require('Module:Arguments').mergeArgsSyntax
local string, table = loader.require('String', 'Table')
local gemstoneData, gemstoneAliases = loader.loadData('Gemstone/Data', 'Gemstone/Aliases')

local slots = gemstoneData.slots
local gemstone_names = gemstoneData.names
local gemstone_tiers = gemstoneData.tiers
local largeCircleSymbol = '◯'

-- Template:Gemstone Slot
function p.gemstoneSlotText(frame)
	local args = getArgs(frame)
	return p._gemstoneSlotText(args[1], args.bracket or args.tier, args.applied)
end

function p._gemstoneSlotText(name, bracket, applied)
	local slot = slots[gemstoneAliases[name:lower()]]
	local icon, iconColor, slotName, bracketColor, str =
		slot and slot.icon, slot and slot.colorClass, slot and slot.slotName, 'dark_gray', '', ''
	if name and name:lower() == 'unknown' then
		icon, iconColor, slotName = largeCircleSymbol, 'white', 'Unknown'
	end
	if bracket or applied then
		if applied then
			local foo = slots[gemstoneAliases[applied:lower()]]
			if foo then
				iconColor = foo.colorClass
			elseif applied:lower() == 'unlocked' or applied:lower() == 'none' then
				iconColor, bracketColor = 'gray', 'dark_gray'
			elseif applied:lower() == 'locked' then
				iconColor, bracketColor = 'dark_gray', 'dark_gray'
			end
		end
		str = ('<span class="hsw-gamefont color-%s">%s</span>'):format(iconColor, icon)
		
		if bracket then
			local foo = gemstone_tiers[bracket:lower()]
			if foo then
				bracketColor = foo.color
			end
		end
		str = ('<span class="color-%s">&#91;</span>%s<span class="color-%s">&#93;</span>'):format(bracketColor, str, bracketColor)
	else
		str = ('<span class="hsw-gamefont color-%s">%s</span> <span class="color-%s">%s</span> Slot'):format(iconColor, icon, iconColor, slotName)
	end
	return str
end

-- Template:Gemstone slots
function p.gemstoneSlot(frame)
	local args = getArgs(frame)
	
	local text = args[1]
	
	return p._gemstoneSlots(text)
end

function p._gemstoneSlot(str)
	local noError = false
	local slotName = str, cost
	
	if slotName:match('^(.*) &(.*)&') then
		slotName, cost = slotName:match('^(.*) &(.*)&')
	end
	
	local slot = slots[gemstoneAliases[slotName:lower()]]
	
	local applicableText = ''
	if slot.applicable then
		applicableText = 'Applicable Gemstones:/' .. slot.applicable
	end
	
	local costText = ''
	local lockedIcon = ''
	if cost then
		local splitCost = mw.text.split(cost, ',', true)
		for i, val in ipairs(splitCost) do
			splitCost[i] = mw.text.trim(splitCost[i])
			-- if it's a number the cost is coins
			if tonumber(splitCost[i], 10) then
				splitCost[i] = '&6' .. string._formatNum(splitCost[i]) .. ' coins&r'
			else
				-- otherwise it's a gemstone and should be colored to match
				for j, gemstone in ipairs(gemstone_names) do
					if splitCost[i]:lower():find(gemstone, 0, true) then
						-- if cost contains gemstone name, use that color
						splitCost[i] = slots[gemstone].ttColor .. splitCost[i] .. '&r'
					end
				end
			end
		end
		costText = (applicableText ~= '' and '//' or '') .. 'Cost to unlock:/' .. table.concat(splitCost, '/')
		lockedIcon = '<span class="gemstone-slot-lock"></span>'
	end
	
	return string.wrapHtml{
		'[[Gemstone Slot|<span class="hsw-gamefont">' .. slot.icon .. '</span>' .. lockedIcon .. ']]',
		'<span>', {
			class = 'minetip gemstone-slot color-' .. slot.colorClass,
			['data-minetip-title'] = table.concat{ slot.ttColor, slot.icon, ' ', slot.slotName, ' Gemstone Slot' },
			['data-minetip-text'] = applicableText .. costText,
		}
	}
end

return p
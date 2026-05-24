local getArgs = require('Module:Arguments').getArgs
local loader = require('Module:Loader')

local string, table, yesno, color, mainonly = loader.require('String', 'Table', 'Yesno', 'Color', 'Mainonly')

local p = {}

local aliases, tiers, colordata = loader.loadData('RarityTier/Aliases', 'RarityTier/Data', 'Color/Data')
local hexColors = colordata.hexColors

function p._getRarity(tierid)
	if not tierid then return '' end
	
	tierid = tierid:lower():gsub(' ', '_')
	tier = tiers[aliases[tierid] or tierid]
	return tier and tier.name or tierid
end

-- Get function for a tier in the data
-- Accepts: tierid (& all aliases), order number (note: 'common' is indexed 0, not 1)
function p._getTier(tierid)
	if not tierid then return '' end
	if type(tonumber(tierid)) == 'number' then
		for k,v in pairs(tiers) do
			if v.order == tonumber(tierid) then
				return v, k
			end
		end
		return '<strong class=\"error\">Rarity tier out of index</strong>'
	else
		tierid = tierid:lower():gsub(' ', '_')
		local key = aliases[tierid] or tierid
		local tier = tiers[key]
		if not tier then
			return '<strong class=\"error\">Unknown rarity tier \'' .. tierid .. '\'</strong>'
		end
		return tier, key
	end
end

-- Returns an iterable version of p._getTier
-- This is for use when the order is important, as using
-- pairs() on RarityTier/Data will not retain the order
function p._getTierIterable()
	return table.sortedPairsByValue(tiers, function(a, b)
		return a.order < b.order
	end)
end

function p._orderedTiers()
	return table.toCustomArrayNamed(p._getTierIterable(), function(v, k)
		return k
	end)
end

function p.getHexColor(r) -- gets hex color of a rarity
	return hexColors[p._getTier(r).color]
end

function hideAlways(data)
	return ('<span class="desktop-hide hidden">%s</span>'):format(data)
end

-- Template:Rarity
function p.link(frame)
	local args = getArgs(frame)
	return p._link(args[1], args[2], args['addcategory'], args['nolink'], args['ordered'])
end

-- Template:RarityN
-- Similar to {{Rarity}}, but adds an invisible order number in front for table sorting
function p.orderedLink(frame)
	local args = getArgs(frame)
	return p._link(args[1], args[2], args['addcategory'], args['nolink'], true)
end

function p._link(tierid, linkText, addcategory, nolink, ordered)
	addcategory = yesno(addcategory, false)
	local tier = p._getTier(tierid)
	local name = tier.name
	
	if not tierid then return '' end
	
	if tier.name then
		local coloredText = string.wrapHtml{
			color.colorText(tier.color, linkText or name),
			'<span>', {
				class = 'hsw-gamefont raritytier',
			}
		}
		
		return
			(yesno(ordered) and hideAlways(tier.order or 0) or '')
			.. (nolink and coloredText or string.makeLink({ 'Rarity#', tier.link }, coloredText)) 
			-- Add category
			.. ((addcategory and mainonly.on_main()) and '[[Category:' .. tier.category .. ' items]]' or '')
	else
		return tierid
	end
end

-- Colors `text` based on the color of the rarity tierid specific
function p._colorText(tierid, text, withFormat, link, nolink)
	withFormat = withFormat ~= false -- default to true if nil
	
	local coloredText = string.wrapHtml{
		color.colorText(tierid.color, withFormat and "'''" .. text .. "'''" or text),
		'<span>', {
			class = 'hsw-gamefont raritytier',
		}
	}
	
	if link and not nolink then
		return string.makeLink(link, coloredText)
	else
		return coloredText
	end
end

-- returns the value from a lua table based on the rarity passed in
-- aliases are accounted for (ex: tierid='c' will trigger the 'common' key in the table)
-- ex: _switch('rare', { common='a', uncommon='b', rare='c' }) would return 'c'
function p._switch(tierid, cases)
	tierid = string.lower(tierid)
	tierid = aliases[tierid] or tierid
	return cases[tierid] or cases['default'] or nil
end

return p

local getArgs = require('Module:Arguments').getArgs
local loader = require('Module:Loader')

local string, table, yesno, uitext, cache =
	loader.require('String', 'Table', 'Yesno', 'UIText', 'Cache')

local invslotCache = cache.invslotCache
-- local slotAliasesCache = cache.slotAliasesCache
local itemVariantsCache = cache.itemVariantsCache

local p = {}

function p.theoretical(frame)
	local args = getArgs(frame)
return p.tooltip(args[1] or args['title'], args[2] or args['text'], args[3] or args['display'])
end

function p.tooltip(title, text, display)
    if string.find(text, '&') ~= nil then 
	tp = '<span class="minetip" data-minetip-title="' .. title .. '" data-minetip-text="' .. text .. '">' .. mw.getCurrentFrame():preprocess('{{rmt|' .. display .. '}}') .. '</span>'
	else
		tp = '<span class="minetip" data-minetip-title="' .. title .. '" data-minetip-text="' .. text .. '">' .. display .. '</span>'
	end
	return tp
end

return p
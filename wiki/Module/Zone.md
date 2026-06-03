local getArgs = require('Module:Arguments').getArgs
local loader = require('Module:Loader')

local string, table, color = loader.require('String', 'Table', 'Color')
local zonedata, aliases = loader.loadData('Zone/Data', 'Zone/Aliases')
local colorText = color._colorTemplates

local p = {}

function p._getZoneData(zoneName, noerror)
	if not noerror then assertTrue(type(zoneName) == 'string', '`zoneName` must be a string') end
	
	local zone = string.trim(zoneName:lower()):gsub('_', ' ')
	local dt = zonedata[aliases[zone] or zone]
	
	if not noerror then assertTrue(dt, 'bad argument #1 to \'_getZoneData\' (Unknown zone %q)', 2, zone) end
	return dt
end

---------------------------------------------------------------------------------
-- Template: Zone
-- 
-- Creates a colored zone link.
---------------------------------------------------------------------------------
function p.zone(frame)
	local args = getArgs(frame)
	
	local iconType = args[2] or args["icon"] or args["icon_type"]
	
	return p._zone(args[1], iconType)
end

---------------------------------------------------------------------------------
-- function: _zone(zone: string)
-- 
-- Creates a Colored string based off of the Skyblock Zone.
---------------------------------------------------------------------------------
function p._zone(zone, iconType)
	local zDt = zonedata[aliases[zone:lower()] or zone:lower()]
	-- if not zDt then return formattedError('Invalid zone: %q', 2, zone) end
	-- if not zDt.color then return formattedError('Missing color for zone: %q', 2, zDt.name) end
	
	local icon
	if (iconType == "rift" or (zDt and zDt.iconType == "rift")) then
		icon = colorText('purple', 'ф ')
	else
		icon = colorText('gray', '⏣ ')
	end
	
	return string.makeLink(zDt and (zDt.link or zDt.name) or zone, icon .. colorText(zDt and zDt.color or 'white', zDt and zDt.name or zone ))
		.. ((not zDt) and '[[Category:Unknown Zone Referenced]]' or '')
		.. ((zDt and not zDt.color) and '[[Category:Unknown Zone Color Referenced]]' or '')
end

return p
--[[
	A module for general wikitext elements.
--]]

local getArgs = require('Module:Arguments').getArgs
local string = require('Module:String')
local table = require('Module:Table')
local yesno = require('Module:Yesno')

local p = {}
local replpttn = '[%s\'",;:\.]'
local MAX_TOGGLES = 9

-- used by modules
function p._collapsible( args )
	local collapsible = args.collapsible and args.collapsible:lower() or 'collapsed'
	local additionalClass = args.class or ''
	local class = ('mw-collapsible mw-%s textsection %s'):format(
		(collapsible == 'un' or collapsible == 'uncollapsed' or collapsible == 'notcollapsed') 
		and 'uncollapsed' or 'collapsed',
		additionalClass
	)
	local id = args.id and 'mw-customcollapsible-' .. args.id:lower():gsub(replpttn,'-') or nil
	
	return string.wrapHtml(args[1] or '', 'div', { class = class, id = id })
end

-- used by modules
function p._collapsibleButton( args )
	local name = args[1] or args.name or args.text or 'Show/Hide'
	local additionalClass = args.class or ''
	local classes = { 'button' }
	for i = 1, MAX_TOGGLES do
		local field = 'id' .. (i == 1 and '' or i)
		if not args[field] then break end
		table.push(classes, 'mw-customtoggle-' .. args[field]:lower():gsub(replpttn,'-'))
	end
	if yesno(args.small, false) then
		table.push(classes, 'small')
	end
	if args.class then
		table.push(classes, args.class)
	end
	local class = table.concat(classes, ' ')
	local style = args.style or nil
	
	return string.wrapHtml(name, 'div', { class = class, style = style })
end

return p
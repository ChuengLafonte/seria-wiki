-- Module:Crafting — minimal implementation for Module:UI (furnace, brewingStand, anvil)
local loader = require('Module:Loader')
local slot = loader.require('Inventory slot')

local p = {}

function p.addSlot(args, item, prefix, class, default)
	local none, nostacksize
	prefix = prefix or ''
	if #prefix == 0 then
		none = 'none'
		nostacksize = ((item == '' or type(item) == 'nil') and '') or (args[item] and args[item]:gsub('[,%d]', '') or '')
	end
	if (args[item] or ''):match('<.->.-</.->')  then
		return args[item]
	end
	return slot.slot{
		nostacksize or args[item],
		link = none or args[prefix .. 'link'],
		title = none or args[prefix .. 'title'],
		class = class,
		default = default,
		parsed = args.parsed,
		forcenum = args.forcenum
	}
end

return p
local getArgs = require('Module:Arguments').getArgs
local loader = require('Module:Loader')

local string, table, yesno, potion, Interface =
	loader.require('String', 'Table', 'Yesno', 'Potion', 'UI/Core')

local aliasesCache = require('Module:Cache').slotAliasesCache

local p = {}

-- Potion UI
function p.potionUI( frame )
	local args = getArgs(frame)
	return p._potionUI(args)
end
function p._potionUI(args)
	local ingredient, base = args[2], args[3]
	local ingredientLink = args.ingredientLink
	
	if not ingredient or not base then
		local potIng = potion._potionRecipe(args[1])
		if type(potIng) == 'table' then
			ingredient = ingredient or potIng.ingredient
			ingredientLink = ingredientLink or potIng.ingredientLink
			base = base or potIng.base
		else
			return potIng
		end
	end
	base = base or 'Awkward Potion'
	
	ingredient = ingredient or curTitle.text
	local tooltip = aliasesCache:get(base)
	local itemTitle = tooltip and tooltip.title
	local itemText = tooltip and tooltip.text
	
	local ui = Interface({
		args.title or 'Brewing Stand',
		id = args.id,
		return_text = args.return_text or args.goback,
		return_link = args.return_link,
		return_id = args.return_id or args.return_to,
		hide = args.hide,
	})
	ui:setSlot(2, 5, {
		ingredient,
		link = ingredientLink,
	})
	for _, pos in ipairs{ {3, 3}, {3, 4}, {3, 5}, {3, 6}, {3, 7}, {4, 3}, {4, 5}, {4, 7}, } do
		ui:setSlot(pos[1], pos[2], {
			'Blank (Light Blue)',
			link = 'none',
			title = 'none',
		})
	end
	for _, pos in ipairs{ {5, 3}, {5, 5}, {5, 7}, } do
		ui:setSlot(pos[1], pos[2], {
			base,
			title = itemTitle or '',
			text = (itemText or '') .. (args.appendRecipe and '//&eClick to view recipe!' or ''),
		})
	end
	
	return tostring(ui)
end

return p
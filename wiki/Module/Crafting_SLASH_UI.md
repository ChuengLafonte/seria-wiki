--<pre>
-- Taken from: https://minecraft.gamepedia.com/Module:UI
local getArgs = require('Module:Arguments').getArgs
local loader = require('Module:Loader')

local string, table, yesno, crafting, Interface, element =
	loader.require('String', 'Table', 'Yesno', 'Crafting', 'UI/Core', 'Element')

local curTitle = mw.title.getCurrentTitle()

local p = {}

local addSlot = crafting.addSlot

function p.craftingGrid( frame )
	local args = getArgs(frame)
	local replpttn = '[%s\'",;:\.]'
	
	local collapse = yesno(args.collapse, false)
	local out = args.Output or args['output'] or args[1]
	
	local recipe, cat = crafting.parseRecipe(args)
	local grid = p._craftingGrid( recipe )
	
	grid = (not collapse and out and string.wrapHtml(out, 'center') or '') ..
		string.wrapHtml(grid, 'div', { class = "mcui mcui-Crafting_Table pixel-image" })
	
	grid = string.wrapHtml(grid, 'div', { style = { display = 'inline-block' } })
	
	local bzar
	if yesno(args.bazaar, false) then
		local t = {}
		table.each(cArgVals, function(v)
			if args[v] then table.push(t, args[v]) end
		end)
		
		bzar = ("'''Bazaar Material Cost: '''%s"):format(bazaar.calcMaterialBuyPrices(t))
		bzar = string.wrapHtml(bzar, 'div')
	end
	
	grid = grid .. (bzar or '')
	if collapse then
		local id = out and ('%s-table'):format(out:gsub(replpttn, '-'))
		grid = ('%s\n%s'):format(element._collapsibleButton( {'▦ Recipe', id = id} ),
			element._collapsible( {grid, id = id} )
		)
		grid = string.wrapHtml(grid, 'div')
	end
	
	-- if curTitle.namespace == 0 and (args.A1 or args.A2 or args.A3 or args.B1 or args.B2 or args.B3 or args.C1 or args.C2 or args.C3) then
	-- 	return grid .. '[[Category:Pages with Crafting Grids Not Using Database]]'
	-- end
	return grid .. cat
end

function p._craftingGrid(recipe)
	local grid = mw.html.create('div'):addClass('mcui-input')
	for num = 1, 3 do
		local row = grid:tag('div'):addClass('mcui-row')
		for _, letter in ipairs{ 'A', 'B', 'C' } do
			row:wikitext(addSlot(recipe, letter .. num, 'I'))
		end
	end
	return tostring(grid)
end

-- Crafting table
function p.craftingTable( frame )
	local args = getArgs(frame)
	local isEnchanted = yesno(args.enchanted)
	
	local body = mw.html.create('span'):addClass('mcui mcui-Crafting_Table pixel-image' .. (isEnchanted and ' enchanted' or ''))
	
	local recipe, cat = crafting.parseRecipe(args)
	local grid = p._craftingGrid(recipe)
	body:node(grid)
	
	local arrow = body:tag('span'):addClass('mcui-arrow'):done()
	
	body:tag('span')
		:addClass('mcui-output')
		:wikitext(addSlot(recipe, 'Output', 'O', 'invslot-large'))
	
	local shapeless = yesno(args.shapeless)
	local fixed = yesno(args.fixed)
	local notFixed = yesno(args.notfixed)
	if shapeless or fixed then
		local icon = body:tag('span'):addClass('mcui-icons')
		icon:tag('span')
		if shapeless then
			icon:addClass('mcui-shapeless')
				:attr('title', 'This recipe is shapeless, the inputs may be placed in any arrangement in the crafting grid.' )
		elseif fixed then
			local exceptFixed = notFixed and ('; except for ' .. notFixed .. ', which can go anywhere') or ''
			icon:addClass('mcui-fixed')
				:attr('title', 'This recipe is fixed, the input arrangement may not be moved or mirrored in the crafting grid' .. exceptFixed .. '.' )
		end
	end
	
	-- if curTitle.namespace == 0 and (args.A1 or args.A2 or args.A3 or args.B1 or args.B2 or args.B3 or args.C1 or args.C2 or args.C3) then
	-- 	return tostring(mw.html.create('div'):node(body)) .. '[[Category:Pages with Crafting Grids Not Using Database]]'
	-- end
	return tostring(mw.html.create('div'):node(body)) .. cat
end

-- Crafting UI
function p.craftingUI( frame )
	local args = getArgs(frame)
	
	local ui = Interface({
		args.title or 'Craft Item',
		id = args.id,
		return_text = args.return_text or args.goback,
		return_link = args.return_link,
		return_id = args.return_id or args.return_to,
		hide = args.hide,
	})
	ui:setSlot(3, 6, {
		'Crafting Table',
		link = 'none',
		title = '&aCrafting Table',
		text = '&7Craft this recipe by using/&7a crafting table.',
	})
	
	for num = 1, 3 do
		for i, lt in ipairs{ 'A', 'B', 'C' } do
			if yesno(args.custom) then
				ui:setSlot(num + 1, i + 1, args[lt .. num], true)
			else
				ui:setSlot(num + 1, i + 1, {
					args[lt .. num],
					link = args[lt .. '_link' .. num] or args[lt .. num .. '_link'],
					text = args[lt .. '_text' .. num] or args[lt .. num .. '_text'],
					class = args[lt .. '_class' .. num] or args[lt .. num .. '_class'],
					title = args[lt .. '_title' .. num] or args[lt .. num .. '_title'],
				})
			end
		end
	end
	if yesno(args.custom) then
		ui:setSlot(3, 8, args.Output, true)
	else
		ui:setSlot(3, 8, {
			args.Output,
			link = args.Output_link,
			text = args.Output_text,
			class = args.Output_class,
			title = args.Output_title,
		})
	end
	
	return tostring(ui)
end

-- Template:Collection Recipe
-- Outdated. The goback message should be something like
-- "Go back to Coal IV Rewards"
function p.collectionRecipe( frame )
	local args = getArgs(frame)
	local topText = args.title or (args.Output or curTitle.text):gsub('^(.-)[;,](.+)$', '$1')
	topText = topText .. (args.title and '' or ' Recipe')
	local back = '&7 to ' .. (args.return_text or args.goback or args[1] or curTitle.text) .. ' Collection'
	return p.craftingUI(table.merge(args, {
		title = topText,
		goback = back,
		hide = yesno(args.hide, true),
	}))
end

return p
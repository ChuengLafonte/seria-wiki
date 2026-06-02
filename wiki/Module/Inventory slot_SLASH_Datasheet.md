local loader = require('Module:Loader')

local string, table, utils, tooltipsTable, invTemplates =
	loader.require('String', 'Table', 'Inventory slot/Utils', 'Inventory slot/Tooltips', 'Inventory slot/Templates')

local colorData = loader.loadData('Color/Data')

local finalTable = {}

------------------------------------------------------------
-- Item Tool tips
--
-- See https://hypixel.net/threads/guide-minecraft-color-codes.1741307/ 
-- for information on the color syntax.
-- 
-- Other syntax:
-- *\ - New line
------------------------------------------------------------
local function main()
	----------------------
	-- Hypixel Skyblock stuff
	----------------------
	table.merge(finalTable, {
		-- Fake items
		['Air (minion)'] = { title = 'Air', name = 'Minions', image = 'Air (minion)', text = '&7Air should be 1 layer/&7underneath where the minion/&7is standing.', link = 'none' },
		['Blank'] = { image = 'Black Stained Glass Pane', name = 'none', title = 'none', link = 'none', text = 'none', image_id = 'Blank:15' },
		['Cancel'] = { name = 'Barrier', title = '&cCancel', link = 'none', text = 'none' },
		['Coming Soon'] = {name = 'Bedrock', title = '&cCOMING SOON', link = 'none', text = 'none', },
		['Close'] = { name = 'Barrier', title = '&cClose', link = 'none', text = 'none' },
		['Go Back'] = { name = 'Arrow', title = '&aGo Back', link = 'none' },
		['Next Page'] = { name = 'Arrow', title = '&aNext Page', link = 'none' },
		['Previous Page'] = { name = 'Arrow', title = '&aPrevious Page', link = 'none' },
		['Sell Item'] = { name = 'Hopper', title = '&aSell Item', link = 'none', text = '&7Click items in your inventory to/&7sell them to the shop!' },
		['SkyBlock Menu'] = { name = 'SkyBlock Menu', title = '&aSkyBlock Menu &7(Right Click)', text = '&7View all of your SkyBlock/&7progress, including your Skills,/&7Collections, Recipes, and more!//&eClick to open!', },
	})
	
	-- Other colored items --
	local colors = colorData.MCColors
	-- UI Blank (Any Specific Color) --
	for i, color in ipairs(colors) do
		finalTable['Blank (' .. color .. ')'] = { image = color .. ' Stained Glass Pane', name = 'none', title = 'none', link = 'none', text = 'none', image_id = 'Blank:' .. (i - 1) }
	end
	
	for key, instruction in pairs(invTemplates) do
		local template = instruction.template
		local apply = instruction.apply
		if not template then
			error('Instruction with key ' .. key .. ' has no template')
		else
			table.merge(finalTable, utils._templateReplacements(apply, template))
		end
	end
	
	return table.merge( finalTable, tooltipsTable )
end

function listing()
	local tt = main()
	local new = {}
	for k, v in pairs(tt) do
		k = k:gsub('\'', '\\\'')
		new[#new+1] = '\t\t\'' .. k .. '\','
	end
	return table.concat(new, '\n')
end

-- For Debugging
-- local p = { main = main, listing = listing }
-- return p

-- Actual Usage
return main()
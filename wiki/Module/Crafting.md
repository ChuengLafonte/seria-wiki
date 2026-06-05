-- <pre>
-- Taken from: https://minecraft.gamepedia.com/Module:Crafting
-- And modified for use in this wiki
local loader = require('Module:Loader')

local string, table, yesno, slot, arguments, utils =
	loader.require('String', 'Table', 'Yesno', 'Inventory slot', 'Arguments', 'Crafting/Utils')

local getArgs, mergeArgsSyntax, cArgVals, cArgValsT =
	arguments.getArgs, arguments.mergeArgsSyntax, utils.cArgVals, utils.cArgValsT
local curTitle = mw.title.getCurrentTitle()
-- local recipeTable = require('Module:Recipe table').table
-- local recipeTable = recipeTable.table

local aliasesCache = require('Module:Cache').craftingAliasesCache

local p = {}

-- local i18n = {
-- 	colored = 'Colored',
-- 	coloredDyes = {
-- 		'Orange Dye', 'Magenta Dye', 'Light Blue Dye', 'Yellow Dye', 'Lime Dye',
-- 		'Pink Dye', 'Gray Dye', 'Light Gray Dye', 'Cyan Dye', 'Purple Dye',
-- 		'Lapis Lazuli', 'Cocoa Beans', 'Cactus Green', 'Red Dye', 'Ink Sack'
-- 	},
-- 	categoryIngredientUsage = 'Category:Recipe using $1',
-- 	categoryRecipeType = 'Category:$1 recipe',
-- 	categoryUpcoming = 'Category:Upcoming',
-- 	itemBlockOfQuartz = 'Block of Quartz',
-- 	itemBoneMeal = 'Bone Meal',
-- 	itemBrownMushroom = 'Brown Mushroom',
-- 	itemCharcoal = 'Charcoal',
-- 	itemCoal = 'Coal',
-- 	itemColoredDye = 'Colored Dye',
-- 	itemDye = 'Dye',
-- 	itemMushroom = 'Mushroom',
-- 	itemQuartzBlock = 'Quartz Block',
-- 	itemRedMushroom = 'Red Mushroom',
-- 	itemStone = 'Stone',
-- 	stoneVariants = { 'Stone', 'Andesite', 'Granite', 'Diorite' },
-- 	type = 'Crafting',
-- 	variantPages = {
-- 		'Andesite', 'Banner', 'Bed', 'Diorite', 'Firework Star', 'Granite', 
-- 		'Pressure Plate', 'Sand', 'Sandstone', 'Shield', 'Slab', 'Stained Glass Pane', 
-- 		'Stained Glass', 'Stairs', 'Stone Bricks', 'Wood Planks', 'Wood', 'Wool',
-- 	},
-- }
-- p.i18n = i18n

-- function p.table( frame )
-- 	local args = getArgs(frame)
	
-- 	-- Automatic shapeless positioning
-- 	if args[1] then
-- 		args.shapeless = 1
-- 		if args[7] then
-- 			args.A1 = args[1]
-- 			args.B1 = args[2]
-- 			args.C1 = args[3]
-- 			args.A2 = args[4]
-- 			args.B2 = args[5]
-- 			args.C2 = args[6]
-- 			if args[8] then
-- 				-- ◼◼◼      ◼◼◼
-- 				-- ◼◼◼  OR  ◼◼◼
-- 				-- ◼◼◼      ◼◼◻
-- 				args.A3 = args[7]
-- 				args.B3 = args[8]
-- 				args.C3 = args[9]
-- 				if args[9] then
-- 					local identical = true
-- 					for i = 1, 8 do
-- 						if args[i] ~= args[i + 1] then
-- 							identical = false
-- 							break
-- 						end
-- 					end
-- 					if identical then
-- 						args.shapeless = nil
-- 					end
-- 				end
-- 			else
-- 				-- ◼◼◼
-- 				-- ◼◼◼
-- 				-- ◻◼◻
-- 				args.B3 = args[7]
-- 			end
-- 		elseif args[2] then
-- 			args.A2 = args[1]
-- 			args.B2 = args[2]
-- 			if args[5] then
-- 				-- ◻◻◻      ◻◻◻
-- 				-- ◼◼◼  OR  ◼◼◼
-- 				-- ◼◼◼      ◼◼◻
-- 				args.C2 = args[3]
-- 				args.A3 = args[4]
-- 				args.B3 = args[5]
-- 				args.C3 = args[6]
-- 			elseif args[4] then
-- 				-- ◻◻◻
-- 				-- ◼◼◻
-- 				-- ◼◼◻
-- 				args.A3 = args[3]
-- 				args.B3 = args[4]
-- 			else
-- 				-- ◻◻◻      ◻◻◻
-- 				-- ◼◼◻  OR  ◼◼◻
-- 				-- ◻◼◻      ◻◻◻
-- 				args.B3 = args[3]
-- 			end
-- 		else
-- 			-- ◻◻◻
-- 			-- ◻◼◻
-- 			-- ◻◻◻
-- 			args.B2 = args[1]
-- 			args.shapeless = nil
-- 		end
		
-- 		for i = 1, 9 do
-- 			args[i] = nil
-- 		end
-- 	end
	
-- 	-- Create recipe table, and list of ingredients
-- 	local out, ingredientSets = recipeTable( args, {
-- 		uiFunc = 'craftingTable',
-- 		type = i18n.type,
-- 		ingredientArgs = cArgVals,
-- 		outputArgs = { 'Output' },
-- 	} )
	
-- 	local title = mw.title.getCurrentTitle()
-- 	if args.nocat == '1' or title.namespace ~= 0 or title.isSubpage then
-- 		return out
-- 	end
	
-- 	local categories = {}
-- 	local cI = 1
-- 	if args.upcoming then
-- 		categories[cI] = '[[' .. i18n.categoryUpcoming .. ']]'
-- 		cI = cI + 1
-- 	end
	
-- 	if args.type then
-- 		categories[cI] = '[[' .. i18n.categoryRecipeType:gsub( '%$1', args.type ) .. ']]'
-- 		cI = cI + 1
-- 	end
	
-- 	if args.ignoreusage ~= '1' then
-- 		-- Create ingredient categories for DPL
-- 		local usedNames = {}
-- 		for _, ingredientSet in pairs( ingredientSets ) do
-- 			for _, ingredient in pairs( ingredientSet ) do
-- 				local name = ingredient.name
-- 				if not ingredient.mod and not usedNames[name] and name ~= title.text then
-- 					-- List each dye individually as they have their own pages
-- 					if
-- 						name == slot.i18n.prefixes.any .. ' ' .. i18n.itemDye or
-- 						name == slot.i18n.prefixes.matching .. ' ' .. i18n.itemDye or
-- 						name == slot.i18n.prefixes.any .. ' ' .. i18n.itemColoredDye or
-- 						name == slot.i18n.prefixes.matching .. ' ' .. i18n.itemColoredDye
-- 					then
-- 						if not name:find( i18n.colored ) then
-- 							categories[cI] = '[[' .. i18n.categoryIngredientUsage:gsub( '%$1', i18n.itemBoneMeal ) .. ']]'
-- 							cI = cI + 1
-- 							usedNames[i18n.itemBoneMeal] = true
-- 						end
						
-- 						for _, dye in pairs( i18n.coloredDyes ) do
-- 							categories[cI] = '[[' .. i18n.categoryIngredientUsage:gsub( '%$1', dye ) .. ']]'
-- 							cI = cI + 1
-- 							usedNames[dye] = true
-- 						end
-- 					-- List stone variants individually as they have their own pages
-- 					elseif
-- 						name == slot.i18n.prefixes.any .. ' ' .. i18n.itemStone or
-- 						name == slot.i18n.prefixes.matching .. ' ' .. i18n.itemStone
-- 					then
-- 						for _, stone in pairs( i18n.stoneVariants ) do
-- 							categories[cI] = '[[' .. i18n.categoryIngredientUsage:gsub( '%$1', stone ) .. ']]'
-- 							cI = cI + 1
-- 							usedNames[stone] = true
-- 						end
-- 					else
-- 						-- Merge item variants which use a single page
-- 						if
-- 							name == slot.i18n.prefixes.any .. ' ' .. i18n.itemMushroom or
-- 							name == slot.i18n.prefixes.matching .. ' ' .. i18n.itemMushroom or
-- 							name == i18n.itemRedMushroom or
-- 							name == i18n.itemBrownMushroom
-- 						then name = i18n.itemMushroom
-- 						elseif name == i18n.itemCharcoal then name = i18n.itemCoal
-- 						elseif name:find( ' ' .. i18n.itemQuartzBlock .. '$' ) then name = i18n.itemBlockOfQuartz
-- 						else
-- 							for _, variant in pairs( i18n.variantPages ) do
-- 								if name:find( ' ' .. variant .. '$' ) then
-- 									name = variant
-- 									break
-- 								end
-- 							end
							
-- 							-- Remove prefixes
-- 							for _, prefix in pairs( slot.i18n.prefixes ) do
-- 								if name:find( '^' .. prefix .. ' ' ) then
-- 									name = name:gsub( '^' .. prefix .. ' ', '' )
-- 									break
-- 								end
-- 							end
-- 						end
						
-- 						if not usedNames[name] then
-- 							categories[cI] = '[[' .. i18n.categoryIngredientUsage:gsub( '%$1', name ) .. ']]'
-- 							cI = cI + 1
-- 							usedNames[name] = true
-- 						end
-- 					end
-- 				end
-- 			end
-- 		end
-- 	end
	
-- 	return out, table.concat( categories, '' )
-- end

function p.addSlot(args, item, prefix, class, default)
	local none, nostacksize
	prefix = prefix or ''
	if #prefix == 0 then
		none = 'none'
		nostacksize = ((item == '' or type(item) == 'nil') and '') or (args[item] and args[item]:gsub('[,%d]', '') or '')
	end
	if (args[item] or ''):match('<.->.-</.->') then
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

function p.parseRecipe(args)
	-- method 3 (lowest priority): from database; always at ver=2 syntax
	-- method 2: input using the Quick Recipe Syntax
	-- method 1 (highest priority): use normal args as override
	local ret, recipe = {}, {}
	local qrs = args.qrs and utils._parseRecipe(args.qrs) or {}
	local missing = false -- any recipe tried to obtain from database that is missing
	local manualRecipes = false -- any recipe that uses methods 1 or 2
	
	local toprocess = mergeArgsSyntax(args)
	
	if #toprocess > 1 then
		local alldata = table.map(toprocess, function(v)
			local val = aliasesCache:get(v)
			missing = missing or (not val)
			return val
		end) -- only performs on positional arguments
		local todo = table.Set(table.merge({}, cArgVals, unpack(table.map(alldata, function(data) -- cArgVals must go before unpack
			return table.namedKeys(data)
		end)))):values()
		for _, data in ipairs(alldata) do
			for _, v in ipairs(todo) do
				recipe[v] = table.push(recipe[v] or {}, data[v] or '')
			end
		end
		for k, v in pairs(recipe) do
			recipe[k] = table.concat(v, ';')
		end
	elseif toprocess[1] and toprocess[1] ~= 'nil' then
		recipe = aliasesCache:get(toprocess[1])
		missing = missing or (not recipe)
	end
	
	if tostring(args.ver) == '2' then
		-- for ver=1 (original):
			-- ROWS are indicated by '1' '2' '3'
			-- COLUMNS are indicated by 'A' 'B' 'C'
			-- which can be less intuitive in some cases
		-- therefore, ver=2 is invented:
			-- ROWS are indicated by 'A' 'B' 'C'
			-- COLUMNS are indicated by '1' '2' '3'
		-- if using ver=2 syntax, it must be explicitly specified, since here we revert it to ver1 for the table
		qrs, args = utils.versionChange(qrs), utils.versionChange(args)
	end
	
	local argsKeys = table.namedKeys(args or {})
	local qrsKeys = table.namedKeys(qrs or {})
	local recipeKeys = table.namedKeys(recipe or {})
	local todo = table.Set(table.merge({}, argsKeys, qrsKeys, recipeKeys, cArgVals)):values() -- adding cArgVals makes runtime faster for unknown reason
	for _, v in ipairs(todo) do
		ret[v] = args[v] or qrs[v]
		if ret[v] then
			manualRecipes = true
		else
			ret[v] = (recipe or {})[v]
		end
	end
	
	-- Minion crafts, while technically directly using the recipe in the function call, are automated at Module:Minion and are purposefully excluded from the manual recipes category
	if args.minionRecipe then
		manualRecipes = false
	end
	-- ret = table.mergeNamed({}, recipe, qrs, args)
	
	return ret, (missing and '[[Category:Pages with Missing Recipes]]' or '') .. (manualRecipes and '[[Category:Pages with Recipes Directly in the Template]]' or '')
end

return p
local getArgs = require('Module:Arguments').getArgs
local mergeArgsSyntax = require('Module:Arguments').mergeArgsSyntax
local loader = require('Module:Loader')

local string, table, yesno, libU, safeResponse, stringT, inventoryslot, bazaar, colorModule, currency, itemMdl, craftingui, skillMdl =
	loader.lazy.require('String', 'Table', 'Yesno', 'LibU', 'SafeResponse', 'String/Templates', 'Inventory slot', 'Bazaar', 'Color', 'Currency', 'Item', 'Crafting/UI', 'Skillname')
local minionData, collectionData, minionAliases =
	loader.lazy.loadData('Minion/Data', 'Collection/Data', 'Minion/Aliases')

local _error = string._error
local lang = mw.getContentLanguage()
local title = mw.title.getCurrentTitle().text
local slot = function(...)
	return inventoryslot.slot(...)
end

local p = {}

-- not all minions have all 12 tiers; use #TIERS to cover all tiers, instead of using '12'
local TIERS = { 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII' }
local infosymbol = 'ⓘ'

-- merchant sell pricess for non-bazaar items, for profit calculation
local nonBazaarMerchantSellPrices = {
	['Poisonous Potato'] = 10,
	['White Wool'] = 2,
	['Clownfish'] = 20,
	['Cactus Green'] = 1,
	['White Wool'] = 2,
	['Egg'] = 3,
	['Poisonous Potato'] = 10,
	['Iron Ore'] = 3,
	['Gold Ore'] = 3,
	['Allium'] = 1,
	['Azure Bluet'] = 1,
	['Blue Orchid'] = 1,
	['Oxeye Daisy'] = 1,
	['Red Tulip'] = 1,
	['Orange Tulip'] = 1,
	['White Tulip'] = 1,
	['Pink Tulip'] = 1,
	['Lilac'] = 1,
	['Peony'] = 1,
	['Rose Bush'] = 1,
	['Sunflower'] = 1,
}

-- Produces that aren't recorded as items in Minion/Data
-- Used in p._minionPerDayTableCombined (DUMC) and _getStatTableBaseCost
local differentList = {
	['dandelion'] = {'Flower'},
	['poppy'] = {'Flower'},
}

-- <SafeResponse:enabled>
local function npcSellPrice(item)
	if string.trim(item) == '' then return 0 end
	local response = itemMdl._api(item)
	if response then
		return response.npc_sell_price
	else
		error({ type='Item/ApiDataNotFound', format={tostring(item)} })
	end
end

local function _actionsPerMinute(minion, tier)
	-- TBA * 2 = SECONDS_PER_FULL_ACTIONS : Each action either picks up or places, so 2 actions are needed for every collection.
	-- 60 / SECONDS_PER_FULL_ACTIONS = ACTIONS_PER_MINION : This gives us a number that can be used as a multiplier to find all other action/time related questions.
	return 60 / (minionData[minion].stats[tier].tba * 2)
end

-- utility: p.getMinion
function p.getMinion(name, noerr)
	if minionData[name] or noerr then
		return minionData[name]
	end
	return libU.formattedError("Minion %q does not exist in the database, consider adding it", 3, name)
end

-- utility: p.peakStat
-- not all minions have all 12 tiers; this function returns the values of
-- the highest tier and the highest craftable tier of a minion
function p.peakStat(name)
	highestTier = table.length(p.getMinion(name).stats)
	for x = #TIERS, 1, -1 do
		if minionData[name].stats[x] and minionData[name].stats[x].crafting then
			highestCraftable = x
		end
		if highestCraftable then
			break
		end
	end
	return highestTier, highestCraftable
end

-- utility: p._createPriceCell
function p._createPriceCell(npc, bz, amount, products, additional_text, shop_first)
	local function makeCoin(num)
		if tonumber(num) == nil then
			return
		end
		return tostring(currency._coins(math.ceil(num)))
	end
	amount = amount or 1
	additional_text = additional_text or ''
	local productInfo = table.concat(table.map(products or {}, function(prod)
		return ('%.0fx %s; '):format(tonumber(prod.num) or 0, prod.name)
	end), '&#10;')
	productInfo = productInfo == '' and '' or string.makeTitle('[\'\'Produces\'\']', 'List of Produces: &#10;' .. productInfo)
	
	local cell = mw.html.create('td')
	npc.price = tonumber(npc.val)
	bz.price = tonumber(bz.val)
	npc.price = npc.price and npc.price * amount
	bz.price = bz.price and bz.price * amount
	npc.coin = makeCoin(npc.price)
	bz.coin = makeCoin(bz.price)
	if npc.coin and bz.coin then
		local shopfirst = npc.price > bz.price -- shop prize first or bazaar price first
		if shop_first then -- If shop_first arguement, change shopfirst based on it.
			if shop_first == "Best" then
				shopfirst = shopfirst
			elseif shop_first == "Worst" then
				shopfirst = npc.price < bz.price
			elseif shop_first == "Bazaar" then
				shopfirst = false
			elseif shop_first == "NPC" then 
				shopfirst = true
			end
		end
		if shopfirst then
			cell:attr('data-sort-value', shopfirst and npc.price or bz.price):wikitext(('<small><span class="%s">%s:</span> %s<br><span class="%s">%s:</span> %s<br>%s %s</small>'):format(
				'color-alburn', npc.text, npc.coin,
				'color-blue_violet', bz.text, bz.coin,
				productInfo, additional_text
				)):done()
		else
			cell:attr('data-sort-value', shopfirst and npc.price or bz.price):wikitext(('<small><span class="%s">%s:</span> %s<br><span class="%s">%s:</span> %s<br>%s %s</small>'):format(
				'color-blue_violet', bz.text, bz.coin,
				'color-alburn', npc.text, npc.coin,
				productInfo, additional_text
				)):done()
		end
	elseif npc.coin and not bz.coin then
		cell:attr('data-sort-value', npc.price):wikitext(('<small><span class="%s">%s:</span> %s<br>%s %s</small>'):format(
			'color-alburn', npc.text, npc.coin,
			productInfo, additional_text
			)):done()
	elseif bz.coin and not npc.coin then
		cell:attr('data-sort-value', bz.price):wikitext(('<small><span class="%s">%s:</span> %s<br>%s %s</small>'):format(
			'color-alburn', bz.text, bz.coin,
			productInfo, additional_text
			)):done()
	else
		cell:wikitext(stringT.blankCell()):done()
	end
	
	return cell
end

-- utility: p._getRecipe
local recipeCache = {}
function p._getRecipe( minionName, tier, mode )
	local minion = p.getMinion(minionName)
	if not TIERS[tier] or not minion.stats[tier] then return end
	
	local recipeOutput = minionName .. ' Minion ' .. TIERS[tier]
	recipeCache[recipeOutput] = recipeCache[recipeOutput] or {}
	local function getval(k)
		return recipeCache[recipeOutput][k]
	end
	local crafting = minion.stats[tier].crafting
	if not crafting or crafting.info then return end
	
	local recipeBase = (
		crafting.item
		and crafting.item .. (crafting.num and ',' .. crafting.num or '')
		-- Some minion crafting recipes don't have a main item
		or ''
	)
	local recipeMinion = crafting.base or ('%s Minion %s'):format(minionName, TIERS[tier - 1] or '?')
	
	local ret = getval('grid') or {
		A1 = crafting.A1 or recipeBase, B1 = crafting.B1 or recipeBase, C1 = crafting.C1 or recipeBase,
		A2 = crafting.A2 or recipeBase, B2 = crafting.B2 or recipeMinion, C2 = crafting.C2 or recipeBase,
		A3 = crafting.A3 or recipeBase, B3 = crafting.B3 or recipeBase, C3 = crafting.C3 or recipeBase,
		Output = recipeOutput
	}
	recipeCache[recipeOutput].grid = table.deepCopy(ret, true)
	local mat = {}
	if mode == 'table' then
		-- return in a table format instead of crafting table format
		if getval('table') then return getval('table') end
		local ret2 = {}
		for k, v in pairs(ret) do
			local item, n = v:match('^%s*(.-)%s*,%s*(%d+)%s*$')
			if tonumber(n) then
				ret2[k] = { item = item, num = tonumber(n) }
			elseif k ~= '' then
				ret2[k] = { item = v, num = 1 }
			end
		end
		recipeCache[recipeOutput].table = table.deepCopy(ret2, true)
		return ret2
	elseif mode == 'materials' then
		if getval('materials') then return getval('materials') end
		local ret3, mat = {}, {}
		for k, v in pairs(ret) do
			local item, n = v:match('^%s*(.-)%s*,%s*(%d+)%s*$')
			if tonumber(n) then
				mat[item] = (mat[item] or 0) + tonumber(n)
			elseif v ~= '' then
				mat[v] = (mat[v] or 0) + 1
			end
		end
		mat[recipeOutput] = nil
		for k, v in pairs(mat) do
			table.push(ret3, { item = k, num = v })
		end
		recipeCache[recipeOutput].materials = table.deepCopy(ret3, true)
		return ret3
	else
		return ret
	end
end

--------------------------------------------------------------------------------
-- Template:GetMinionData
-- 
-- Returns a specified peice of data from the /Data module based on inputs
--------------------------------------------------------------------------------
function p.getMinionData(frame)
	local args = getArgs(frame)
	
	local minion = args[1] or args['minion'] or args['m']
	local tier = args['tier'] or args['t']
	local data = args[2] or args['data'] or args['d']
	local item = args[3] or args['i'] or args['item']
	
	if not minion then return _error('Inputs expected, got none') end
	if not data then return _error('Invalid Argument to #2: paramater "data" is required.') end
	
	if not tier and minion:match('(.+) ([%dIVXivx]+)') then
		minion, tier = minion:match('(.+) ([%dIVXivx]+)')
	else
		tier = tier
		minion = minion
	end
	 
	return p._getMinionData(minion, data, tier, item)
end
function p._getMinionData(minionName, data, tier, item)
	local minionData = p.getMinion(minionName)
	local highestTier, _ = p.peakStat(minionName)
	
	local aliases = minionAliases.minionDataAliases
	local data = aliases[data:lower()] or data:lower()
	
	if (tostring(tier) or ''):match('[Mm]ax') then
		tier = highestTier
	else
		tier = tonumber(string._toArabic(tier or 0))
	end
	local item = tonumber(item)
	
	if data == 'tiers' then
		ret = highestTier
	elseif data == 'storage' then
		ret = minionData.stats[tier].storage
	elseif data == 'time between actions' then
		ret = minionData.stats[tier].tba
	elseif data == 'crafting item' then
		ret = minionData.stats[tier].crafting.item
	elseif data == 'crafting number' then
		ret = minionData.stats[tier].crafting.num
	elseif data == 'description' then
		ret = minionData.description
	elseif data == 'average item' then
		ret = minionData.items[item].item
	elseif data == 'average number' then
		ret = minionData.items[item].avg
	else
		ret = _error('Invalid Argument to \"data\": unknown data type ([[Template:GetMinionData#Allowed Entries|help]])')
	end
	
	return ret
end

-----------------------------------------------------------------------------
-- Template:Days using minions
--
-- Makes a table with how long it would take a single minion to output a certain amount of items based on it's tier
-----------------------------------------------------------------------------
function p.minionPerDayTable( frame )
	--local parameters = frame.args
	local args = getArgs(frame)
	
	local minion = args['minion'] or args[1] or title
	local amount = args['amount'] or args[2]
	local item = args['item'] or (amount == args[2] and args[3] or args[2])
	local split = yesno(args['split'], false)
	local fullwidth = yesno(args['fullwidth'] or args['noscroll'], false)
	
	return p._minionPerDayTable( minion, amount, item, split, fullwidth )
end
function p._minionPerDayTable( minion, amount, item, split, fullwidth )
	if not minionData[minion] then error('Invalid minion ' .. minion) end
	local HALF_ROW = 6
	local actionsPerDay, days
	local itemIndex = 1
	if item then
		for key, value in ipairs(minionData[minion].items) do
			if value['item'] == item then
				itemIndex = key
			end
		end
	end
	
	local _table = mw.html.create('table'):addClass('wikitable centertxt table-fixed')
	if fullwidth and not split then _table:addClass('full-width-1') end
	_table:tag('caption'):wikitext(string.format(
		'%s to acquire %s using %s [[%s Minion]]<br><small>(By tier, No fuel, No Minion Upgrades)</small><br><small>If the player has multiple minions, divide the number of days by how many minions will be used.</small>',
		string.makeTitle('Days' .. infosymbol, 'The &#34;Day&#34; used in here has a duration of 1 real-life day, or 72 SkyBlock days.'),
		itemMdl._resourceDisplay(amount .. ' ' .. minionData[minion].items[itemIndex].item, true),
		(minion:lower():match('^([aeiouy])') and 'an' or 'a'),
		minion
		)
	)
	
	local row, row_data, row2, row_data2 = _table:tag('tr'), _table:tag('tr'), _table:tag('tr'), _table:tag('tr')
	
	for i, tier in ipairs(TIERS) do
		if minionData[minion].stats[i] then
			if split and i > HALF_ROW then
				row2:tag('th'):wikitext(tier):done()
			else
				if fullwidth and not split then row:tag('th'):wikitext(tier):done()
				else row:tag('th'):wikitext(tier):addClass('article-minion-smallTabs'):done() end
			end
		else
			if split then row2:tag('td'):wikitext(stringT.blankCell()):attr({ rowspan = 2 }) end
		end
	end
	
	for i, tier in ipairs(TIERS) do
		if minionData[minion].stats[i] then
			actionsPerDay = _actionsPerMinute(minion, i) * 60 * 24
			days = (amount / actionsPerDay) / minionData[minion].items[itemIndex].avg
			
			-- Show appropriate number of decimals (smaller the number = more)
			days = days < 1 and math.floor(days * 100) / 100 or
				days < 10 and math.floor(days * 10) / 10 or
				math.floor(days)
			
			if split and i > HALF_ROW then
				row_data2:tag('td'):wikitext( days ):done()
			else
				row_data:tag('td'):wikitext( days ):done()
			end
		end
	end
	
	row:done()
	row2:done()
	row_data:done()
	row_data2:done()
	_table:done()
	
	scrollable = string.wrapHtml(tostring(_table), 'div', {
		class = 'article-scrollable',
	})
	return fullwidth and tostring(_table) or scrollable
end

-----------------------------------------------------------------------------
-- Template:Days Using Minions Combined
-- Template:DUMC
--
-- Displays Days Using Minions with tabbers
-----------------------------------------------------------------------------
function p.minionPerDayTableCombined( frame )
	local args = getArgs(frame)
	local lang = mw.language.getContentLanguage()
	local split = yesno(args['split'], false)
	local fullwidth = yesno(args['fullwidth'] or args['noscroll'], false)
	
	-- first combine both methods of entering data into one list
	local resources = mergeArgsSyntax(args)
	
	local items = {}
	for _, item in ipairs(resources) do
		local numOrNil = tonumber(lang:parseFormattedNumber(item))
		if numOrNil then
			items[#items + 1] = numOrNil
		else
			local num, name = mw.ustring.match(item, '([%d,%.]+)x? %[?%[?([%a%s%d,\'-_]*)%|?.*%]?%]?')
			if not num then
				-- also test for {{Slot}} format
				name, num = mw.ustring.match(item, '([%a%s,\'-_]*),([%d]+)')
				if not num then
					return _error('Invalid item format: ' .. item)
				end
			end
			items[#items + 1] = { name, tonumber(lang:parseFormattedNumber(num)) }
		end
	end
	
	return p._minionPerDayTableCombined(items, split, fullwidth)
end
function p._minionPerDayTableCombined(entries, split, fullwidth)
	local result = {}
	
	local function addtolist(key, val)
		local stor = differentList[key:lower()]
		if stor then
			table.merge(stor, val)
		else
			differentList[key:lower()] = { val }
		end
	end
	
	for mn, dt in pairs(minionData) do
		-- Adds each item that is in Minion/Data into differentList
		table.each(dt.items, function(i)
			i = i.item
			if i == '' then return end
			addtolist(i, mn)
			if i:match('^Raw ') then
				local foo = i:gsub('^Raw ', '')
				addtolist(foo, mn)
			end
		end)
	end
	
	for i, entry in pairs(entries) do
		minionList = differentList[entry[1]:lower()]
		if minionList then
			table.push(result, ('|-|%s='):format(entry[1]))
			table.each(minionList, function(_minion)
				table.push(result, p._minionPerDayTable(_minion, entry[2], entry[1], split, fullwidth))
			end)
		else
			table.push(result, ('|-|%s='):format(entry[1]))
			table.push(result, p._minionPerDayTable(entry[1], entry[2], entry[1], split, fullwidth))
		end
	end
	result = '<tabber>' .. table.concat(result) .. '</tabber>'
	
	return mw.getCurrentFrame():preprocess(result)
end

-----------------------------------------------------------------------------
-- Template:Minion stats table
--
-- Takes all the data from /Data and displays it nicely in a table on the minion page.
-----------------------------------------------------------------------------
function p.minionStatsTable( frame )
	--local parameters = frame.args
	local args = getArgs(frame)
	
	local minion = args['minion'] or args[1] or title
	
	local success, result = safeResponse.call(p._minionStatsTable, minion)
	return mw.getCurrentFrame():preprocess(result)
end
-- <SafeResponse:enabled>
function p._minionStatsTable( minionName )
	local function _getStatTableBaseCost(minionName, item, num)
		-- Find the total number of the base minion items
		-- returns { {item, num} }
		local minion = p.getMinion(minionName)
		local recipes = minion.recipes
		if not recipes[item] then
			return (bazaar._getProduct(item) or not not differentList[item:lower()]) and { {item, num} } or {}
		end
		local items = {}
		for key, value in ipairs(recipes[item]) do
			local subitems = _getStatTableBaseCost(minionName, value[1], value[2] * num)
			for key2, value2 in ipairs(subitems) do
				table.push(items, value2)
			end
		end
		return items
	end
	local function _getStatTableSingleTier(minionName, tier)
		local minion = p.getMinion(minionName)
		local stats = minion.stats[tier]
		local materials = p._getRecipe( minionName, tier, 'materials' )
		local items = materials or stats.trade or {}
		local cost = {}
		for _, itemData in ipairs(items) do
			cost = table.merge(cost, _getStatTableBaseCost(minionName, itemData.item, itemData.num))
		end
		return cost
	end
	local function _getStatTableCumulativeTotal(minionName, tier)
		-- Find total of base minion items for all tiers up to the one passed in
		local totals = {}
		for i = 1, tier, 1 do
			local cost = _getStatTableSingleTier(minionName, i)
			for _, value in ipairs(cost) do
				local item = value[1]
				totals[item] = (totals[item] or 0) + value[2]
			end
		end
		return totals
	end
	
	local minion = p.getMinion(minionName, true)
	if not minion then
		error({ type='Minion/BadName', format={tostring(minionName)} })
	end
	if not minion.recipes or not minion.stats or not minion.items then
		error({ type='Minion/NotEnoughData', format={ name=tostring(minionName), type='Recipes/Stats/Items' } })
	end
	local recipes = minion.recipes
	
	local showBazaarCost = minionName:lower() ~= 'flower'
	
	local wikitable = mw.html.create('table'):addClass('wikitable article-margin-off article-msTable')
	local cumulativeDisplay = string.wrapHtml(string.makeTitle('CUMU', 'This result is cumulative.'), 'sup')
	
	-- Header row
	local row = wikitable:tag('tr')
		:tag('th'):attr({ rowspan = 2 }):wikitext('Tier'):done()
		:tag('th'):attr({ rowspan = 2 }):wikitext('Info'):done()
		:tag('th'):wikitext('Total Upgrade Cost'):done()
	if showBazaarCost then row:tag('th'):wikitext('Bazaar Upgrade Cost{{BazaarInfoIcon}}'):done() end
	row:tag('th'):attr({ rowspan = 2 }):wikitext('Recipe'):done()
	
	-- Header row (second row)
	row = wikitable:tag('tr')
	row:tag('th'):wikitext('Total Cumulative Cost')
	if showBazaarCost then row:tag('th'):wikitext('Bazaar Cumulat. Cost{{BazaarInfoIcon}}') end
	
	-- Display non-header rows
	
	local baseCraftingItem = minion.stats[2].crafting.item
	local items = minion.items
	
	local function getInfo(i)
		local stats = minion.stats[i]
		local crafting = stats.crafting
		local mainItem
		if crafting then
			-- Some minion crafting recipes don't have a main item
			mainItem = crafting.item or nil
		else
			mainItem = stats.trade[1].item
		end
		return stats, crafting, mainItem
	end
	
	for i = 1, #TIERS, 1 do
		if not minion.stats[i] then break end
		local stats, crafting, mainItem = getInfo(i)
		local recipe, materials = p._getRecipe(minionName, i), p._getRecipe( minionName, i, 'materials' )
		local actionsPerDay = _actionsPerMinute(minionName, i) * 60 * 24
		-- if need unique base material count, uncomment the following
		-- local unique = {}
		-- for j = i, 1, -1 do
		-- 	-- mainItem might be nil!
		-- 	local stats, crafting, mainItem = getInfo(j)
		-- 	unique[mainItem] = true
		-- end
		local uniqueAdded = true
		if i > 1 then
			local stats2, crafting2, mainItem2 = getInfo(i - 1)
			uniqueAdded = mainItem2 ~= mainItem
		end
		
		----------------------------------
		-- Calculate info for below
		----------------------------------
		-- Calculate Item Costs
		local tierCosts = {}
		if materials then
			tierCosts = table.map(materials, function (v, i)
				return (
					(not v.item:lower():match('^' .. minionName:lower() .. ' minion [%divx]+$'))
					and ('%sx [[%s]]'):format(v.num, v.item)
					or nil
				)
			end)
		elseif stats.trade then
			for _, itemData in ipairs(stats.trade) do
				if itemData.item:lower() == 'coin' then
					table.push(tierCosts, itemData.num .. ' coins')
				elseif itemData.item:lower() == 'pelt' then
					table.push(tierCosts, itemData.num .. ' pelts')
				elseif itemData.item:lower() == 'north star' then
					table.push(tierCosts, itemData.num .. ' north stars')
				else
					table.push(tierCosts, itemData.num .. 'x [[' .. itemData.item .. ']]')
				end
			end
		end
		
		-- Find totals for items needed for all tiers up to this one
		local totals = {}
		local totalsObj = _getStatTableCumulativeTotal(minionName, i)
		for key, value in pairs(totalsObj) do
			table.push(totals, string._formatNum(math.ceil(value)) .. ' ' .. key)
		end
		
		-- Calculate Bazaar Costs
		local bzTable = {}
		if showBazaarCost then
			-- Since crafting and trade data have different formats, list format is needed
			local basecosts = _getStatTableSingleTier(minionName, i)
			local items = basecosts or stats.trade or {}
			for _, itemData in ipairs(items) do
				local craftNum, craftItem = itemData.num or itemData[2], itemData.item or itemData[1]
				
				-- Hardcoded workaround for Silver Fang not being purchasable on Bazaar
				if craftItem == 'Silver Fang' then
					craftNum = craftNum * 25
					craftItem = 'Enchanted Ghast Tear'
				elseif craftItem == 'Melon (block)' then
					craftNum = craftNum * 9
					craftItem = 'Melon'
				end
				
				-- Handle special items
				if craftItem:lower() == 'coin' then
					-- just increment cost by coin amount
					table.push(bzTable, craftNum)
				elseif craftItem:lower() == 'pelt' then
					-- skip
				elseif craftItem:lower() == 'north star' then
					-- skip
				else
					table.push(bzTable, tonumber(craftNum) .. ' ' .. craftItem)
				end
			end
		end
		
		----------------------------------
		-- First row for this tier
		----------------------------------
		local row = wikitable:tag('tr'):addClass('article-row-main'):attr('id', TIERS[i])
		-- Tier + Icon
		
		row:tag('th'):attr({ rowspan = 2 }):wikitext(TIERS[i] .. '<br>' .. slot{ minionName .. ' Minion ' .. TIERS[i] })
		-- Info
		row:tag('td')
			:attr({ rowspan = 2 })
			:wikitext('Cooldown:&nbsp;' .. colorModule._colorTemplates('Green', stats.tba .. 's'))
			:wikitext('<br>Storage:&nbsp;' .. colorModule._colorTemplates('Yellow', stats.storage))
			:wikitext(stats.req and '<br>Requires:&nbsp;' .. stats.req or '')
		
		-- Cost
		row:tag('td'):wikitext(table.length(tierCosts) > 0 and
			'{{Resource List|' .. table.concat(tierCosts, '|') .. '}}' or '{{Bc}}'):done()
		
		-- Bazaar Cost
		if showBazaarCost then
			row:tag('td')
				:wikitext(table.length(bzTable) > 0 and '{{BPC|' .. table.concat(bzTable, '|') .. '|noerror=y}}' or '{{C|0}}')
		end
		
		-- Recipe
		if stats.trade then -- If bought via trade, list data
			local slots, list = { slot{ minionName .. ' Minion ' .. TIERS[i - 1] } }, {}
			for _, trd in ipairs(stats.trade) do
				if trd.item:lower() == 'coin' then
					slots[#slots + 1] = slot{trd.num .. ' coins'}
				elseif trd.item:lower() == 'pelt' then
					slots[#slots + 1] = slot{trd.num .. ' pelts'}
				elseif trd.item:lower() == 'north star' then
					slots[#slots + 1] = slot{trd.num .. ' north stars'}
				else
					slots[#slots + 1] = slot{ trd.item .. ',' .. trd.num }
				end
			end
			row:tag('td'):attr({ rowspan = 2 }):addClass('centertxt')
				:wikitext('<u>Merchant</u><br>' .. (table.concat(table.map(type(stats.tradeNpc) == 'table' and stats.tradeNpc or { stats.tradeNpc }, function (v)
					return '{{NPCSprite|' .. v .. '|noerr=y}}'
				end), '<br>')))
				:tag('div'):wikitext('<u>Required</u><br>' .. table.concat(slots, '')):done()
				:tag('ul'):addClass('lowmargin'):wikitext('<li>' .. table.concat(list, '</li><li>') .. '</li>'):done()
		elseif crafting.info then -- If there is no crafting recipe, show the details on why
			row:tag('td'):attr({ rowspan = 2 }):addClass('centertxt'):wikitext(crafting.info):done()
		else -- Recipe exists
			local grid = recipe
			grid.Output = nil
			grid.minionRecipe = true -- Exclusion of automated minion crafts on minion pages from the manual recipes category
			row:tag('td'):attr({ rowspan = 2 }):addClass('centertxt table-margin-off')
				:wikitext(craftingui.craftingGrid(grid)):done()
		end
		
		----------------------------------
		-- Second row for this tier
		----------------------------------
		row = wikitable:tag('tr'):addClass('oddrow2 article-row-bound')
		-- Total cost
		row:tag('td'):tag('div'):addClass('article-msTable-cumulative'):wikitext(table.length(totals) > 0
			and ('{{Resource List|' .. table.concat(totals, '|') .. '}} ' .. cumulativeDisplay) or '{{Bc}}')
		-- Bazaar Total Cost
		if showBazaarCost then
			row:tag('td'):tag('div'):addClass('article-msTable-cumulative'):wikitext(
				(table.length(totals) > 0 and '{{BPC|' .. table.concat(totals, '|') .. '|noerror=y}}' or '{{C|0}}')
				.. cumulativeDisplay
			)
		end
	end
	
	return tostring(wikitable)
end

-----------------------------------------------------------------------------
-- Template:Minion Drops Table
--
-- Returns a table with minion drops
-----------------------------------------------------------------------------
function p.minionDropsTable(frame)
	local args = getArgs(frame)
	
	local minion = args.minion or args.m or args[1] or title
	
	local success, result = safeResponse.call(p._minionDropsTable, minion, true, true)
	return mw.getCurrentFrame():preprocess(result)
end
-- <SafeResponse:enabled>
function p._minionDropsTable(minionName, withSellPrices, withNotice)
	minion = minionName:lower()
	minion = minion:match('(.+) minion') or minion
	local divideTwo = minion:lower() == 'fishing' and true or false
	local minionDt = p.getMinion(string._ucfirst(minion), true)
	
	if not minionDt then
		error({ type='Minion/BadName', format={ tostring(minionName) } })
	end
	if not minionDt.drops then
		error({ type='Minion/NotEnoughData', format={ name=tostring(minionName), type='Drops' } })
	end
	
	local wikitable = mw.html.create('table'):addClass('wikitable')
	
	-- headers
	local dropsData = minionDt.drops
	local row = wikitable:tag('tr')
	row:tag('th'):wikitext('Condition')
	row:tag('th'):attr('colspan', 2):wikitext('Input')
	row:tag('th'):attr('colspan', 2):wikitext('Output')
	row:tag('th'):wikitext('XP')
	if withSellPrices then
		row:tag('th'):wikitext('Sell Price')
	end
	
	-- data
	for _, cond in ipairs(minionAliases.minionPageRowParams) do
		if dropsData[cond.param] then
			local dd = dropsData[cond.param]
			for i, drop in ipairs(dd) do
				row = wikitable:tag('tr')
				if i == 1 then
					row:addClass('table-section-separator thick')
					row:tag('td'):attr('rowspan', table.length(dd)):wikitext(cond.condition) -- Condition
				end
				if not drop.from and drop.avg then
					-- Input: Harvest Table
					local innerTable = mw.html.create('table'):addClass('wikitable table-margin-off full-width smalltxt')
					local innerRow = innerTable:tag('tr')
					innerRow:tag('th'):attr('colspan', 2):wikitext('From Harvest')
					innerRow = innerTable:tag('tr')
					innerRow:tag('td'):wikitext('Avg. Amount')
					innerRow:tag('td'):wikitext(tostring(drop.avg))
					innerRow = innerTable:tag('tr')
					innerRow:tag('td'):wikitext('Chance of Obtaining')
					innerRow:tag('td'):wikitext(drop.onein and ('1 in %s'):format(drop.onein) or ('%s%%'):format(drop.avg < 1 and (drop.avg / (divideTwo and 2 or 1) * 100) or 100))
					row:tag('td'):attr('colspan', 2):addClass('table-margin-off'):node(innerTable)
				elseif drop.from then
					row:tag('td'):wikitext(slot{('%s, %d'):format(drop.from.item, drop.from.num)})
					row:tag('td'):wikitext(('<span class="color-green">%sx</span> [[%s]]'):format(drop.from.num, drop.from.item)) -- Input
				else
					row:tag('td'):wikitext('None')
				end
				row:tag('td'):wikitext(slot{drop.item})
				row:tag('td'):wikitext(string.makeLink(drop.item)) -- Output
				row:tag('td'):wikitext(drop.exp and skillMdl._skillXP(drop.exp, { iconOnly = true }) or stringT.blankCell()) -- XP
				if withSellPrices then
					-- Sell Price: Price Table
					local innerTable = mw.html.create('table'):addClass('table-margin-off full-width smalltxt')
					local innerRow = innerTable:tag('tr')
					innerRow:tag('th'):wikitext('Per Item')
					innerRow:tag('th'):wikitext('Stack')
					innerRow = innerTable:tag('tr')
					local npc = {
						val = npcSellPrice(drop.item),
						text = string.makeTitle('NPC', 'Price when sold to a shop.'),
					}
					local bz = {
						val = bazaar._getProduct(drop.item) and bazaar._calcMaterialBuyPrices({{ drop.item, 1 }}, 'sell') or nil,
						text = string.makeTitle('BZ', 'Price when sold to bazaar. Non-bazaar items sold to shop instead.'),
					}
					innerRow:node(p._createPriceCell(npc, bz, 1))
					innerRow:node(p._createPriceCell(npc, bz, 64))
					row:tag('td'):addClass('table-margin-off'):node(innerTable)
				end
			end
		end
	end
	return (withNotice and 'Note: {{ID|Auto Smelter}} and {{ID|Super Compactor 3000}} mentioned below are interchangeable with {{ID|Dwarven Super Compactor}}, which can perform the combination of functionalities of the prior two items.\n\n' or '') .. tostring(wikitable)
end

--------------------------------------------------------------------------------
-- Template:Days using minions collection
--
-- Shows a table with days to acquire each tier of a collection with a minion
--------------------------------------------------------------------------------
function p.minionCollectionDaysTable( frame )
	--local parameters = frame.args
	local args = getArgs(frame)
	
	local coll = args['collection'] or args['coll'] or args[1]
	local minion = args['minion']
	
	return p._minionCollectionDaysTable( coll, minion )
end
function p._minionCollectionDaysTable( coll, minion )
	local function handleMinion()
		local mins = {}
		for c, dt in pairs(collectionData) do
			if dt.minion and dt.minion == (minion or coll) then
				table.push(mins, c)
			end
		end
		if #mins == 0 then return
		else return mins
		end
	end
	
	if minion then
		local t = handleMinion()
		if t then return table.concat(table.map(t, function(m) return p._minionCollectionDaysTable(m) end), '\n') end
	end
	
	coll = coll or minion
	if not collectionData[string.ucfirst(coll)] then error('Invalid collection or minion: ' .. coll) end
	local minion = collectionData[string.ucfirst(coll)].minion
	if not minion then error('Collection ' .. coll .. ' cannot be obtained by minions.') end
	
	local wikitable = mw.html.create('table'):addClass('article-table')
	wikitable:tag('caption'):wikitext(string.format(
		'Time needed to acquire each tier of the %s Collection using a [[%s Minion]] (by tier, no fuel)<br><small>If you have multiple minions, just divide the number of days by how many minions you have.</small>',
		string.ucfirst(coll), minion))
	
	local highestTier, _ = p.peakStat(minion)
	local row = wikitable:tag('th'):wikitext('Minion Tier'):done()
	for i = 1, highestTier, 1 do
		row:tag('th'):addClass('article-minion-coolLabel'):wikitext(string._toRoman(i)):done()
	end
	
	for i, ctier in ipairs(collectionData[coll]) do
		local row = wikitable:tag('tr')
		row:tag('th'):wikitext(
			string.wrapHtml(('%s %s'):format(string.ucfirst(coll), string._toRoman(i)), 'span', { class = 'article-minion-coolLabel' })
			 .. '<br>'
			 .. string.wrapHtml(('(%s)'):format(ctier.required), 'span', { class = 'color-green' } )
		):done()
		for mtier = 1, highestTier, 1 do
			local actPerHour = _actionsPerMinute(minion, mtier) * 60
			local durationHr = ctier.required / actPerHour
			if durationHr < 24 then
				row:tag('td'):wikitext(('%.2f'):format(durationHr) .. 'h')
			else
				row:tag('td'):wikitext(('%.2f'):format(durationHr / 24) .. 'd')
			end
			
		end
	end
	
	return tostring(wikitable)
end




-----------------------------------------------------------------------------
-- Feature Set: Profit Calculation
-- These functions should support all calculations of minion profits with upgrades.
-- Utilities
-- ├──  p._producePerMinute
-- └──	p._getMultiplier
-- Main Things
-- ├──  p.minionProfitTable
-- │	└── p._minionProfitTable
-- ├──  p.minionProfit
-- │	└── p._minionProfit
-- └──	p.minionFullProfitTable
--      └── p._minionFullProfitTable
-----------------------------------------------------------------------------
function p._producePerMinute(amount, tba)
	-- ACTIONS_PER_MINUTE = 60 / TBA * 2
	-- PRODUCE_PER_MINUTE = ACTIONS_PER_MINUTE * AVG_AMOUNT
	return 60 / (tba * 2) * amount
end
function p._getMultiplier(minion, opts)
	local function getMultiplier(multiplier, boost)
		-- Note: 'boost' should be passed as a multiple, in other words, (1 + percentage increase)
		return boost == 0 and multiplier or ( 1 + (multiplier - 1) + (boost - 1) )
	end
	-- Calculate multiplier
	local multiplier = 1
	-- minion fuels
	local fuel, fuels = opts.fuel, minionAliases.fuelData
	if fuel and fuel:lower():match('none') then fuel = nil end
	if fuel and fuel:lower() == 'everburning flame' and table.find(minionAliases.everburningFlameCombatValid, minion:lower()) then
		fuel = fuel..' (combat)'
	end
	if fuel then fuel = minionAliases.fuelAliases[fuel:lower()] or error('Invalid fuel "' .. fuel .. '"') end
	-- this gets the fuel multiplier
	fuel = fuels[fuel] or 0
	multiplier = getMultiplier(multiplier, fuel)
	-- minion upgrades
	local expander = tonumber(opts.expander) or 0
	for i = 1, expander > 2 and 2 or expander < 0 and 0 or expander, 1 do
		multiplier = getMultiplier(multiplier, 1.05)
	end
	local flycatcher = tonumber(opts.flycatcher) or 0
	for i = 1, flycatcher > 2 and 2 or flycatcher < 0 and 0 or flycatcher, 1 do
		multiplier = getMultiplier(multiplier, 1.2)
	end
	-- others
	if yesno(opts.infusion) then multiplier = getMultiplier(multiplier, 1.1) end
	if yesno(opts.crystal) then
		local validMinions = minionAliases.crystalValid
		if table.find(validMinions, minion:lower()) then
			multiplier = getMultiplier(multiplier, 1.1)
		end
	end
	if opts.beacon and yesno(opts.beacon, true) ~= false and not opts.beacon:lower():match('none') then
		local beaconLv = tonumber(string._toArabic(opts.beacon)) or 0
		if beaconLv > 0 and beaconLv < 6 then
			multiplier = getMultiplier(multiplier, 1 + .02 * beaconLv)
		end
		if yesno(opts.scorched) then multiplier = getMultiplier(multiplier, 1.01) end
	end
	local bonus = tonumber(opts.bonus) or 0
	if bonus then multiplier = getMultiplier(multiplier, bonus) end
	return multiplier
end
-----------------------------------------------------------------------------
-- Template:MinionProfitTable
--
-- Shows a table with resources collected by the minion alongside their bazaar sell prices
-----------------------------------------------------------------------------
function p.minionProfitTable(frame)
	local args = getArgs(frame)
	
	local minion = args[1] or args['minion'] or title
	if not minion then minion = mw.title.getCurrentTitle().text end
	
	minion = minion:gsub('%s*[Mm]inion', '')
	
	local success, result = safeResponse.call(p._minionProfitTable, minion)
	return mw.getCurrentFrame():preprocess(result)
end
-- <SafeResponse:enabled>
function p._minionProfitTable(minionName, isOffline)
	local minion = p.getMinion(minionName, true)
	
	if not minion then
		error({ type='Minion/BadName', format={tostring(minionName)} })
	end	
	if not minion.items or not minion.stats then
		error({ type='Minion/NotEnoughData', format={ name=tostring(minionName), type='Stats/Items' } })
	end
	
	local produce = minion.items
	local items = {}
	
	-- get drops produced by the minion
	for i = 1, 25, 1 do -- 25 because some minions like flower minion have very large amount of different drops
		if produce[i] and produce[i].condition == nil then
			items[i] = produce[i]
		elseif produce[i] and produce[i].condition == 'Auto Smelter' and produce[i].item ~= 'Cactus Green' then
			items[i] = produce[i]
			table.remove(items, i - 1)
		elseif produce[i] and produce[i].condition == 'Flint Shovel' then
			items[i] = produce[i]
			table.remove(items, i - 1)
		end
	end
	
	-- compose the header of the table
	local wikitable = mw.html.create('table'):addClass('wikitable')
	wikitable:tag('caption'):addClass('txt-nowrap')
		:wikitext('Listed below are the profits of this minion when its items are sold to [[Bazaar]].<br>No [[Minion Fuel]], [[Super Compactor 3000|Compactors]], nor [[Diamond Spreading]] are used in the calculation.', '<br>', 'Values are shown when the player is online.')
	wikitable:tag('tr')
		:tag('th'):wikitext('Tier'):attr({ rowspan = 2 }):done()
		:tag('th'):wikitext('<abbr title="Harvests per minute = 60 / (time between actions × 2)">Harvests<br>per minute</abbr>'):attr({ rowspan = 2 }):done()
		:tag('th'):wikitext('Per day'):attr ({ colspan = 3 }):done()
	:done()
	wikitable:tag('tr')
		:tag('th'):wikitext('Items'):done()
		:tag('th'):wikitext('Bazaar Profit{{BazaarInfoIcon}}'):done()
		:tag('th'):wikitext('NPC Profit'):done()
	:done()
	
	function getProduceAmountDisplay(item, tba, hours)
		local produceAmount = p._producePerMinute(item.avg, tba) * 60 * hours
		if produceAmount >= 10 then
			-- standard rounding - i.e. no decimals
			return math.floor(string.roundNumber(produceAmount))
		elseif produceAmount >= 1 then
			-- round to 1 decimal and remove any .0 from the result
			local rounded = string.roundNumber(produceAmount, 1)
			local roundedInt = math.floor(rounded)
			return rounded == roundedInt and roundedInt or rounded
		elseif produceAmount > 0 then
			-- round to the first non-zero decimal
			local numDecimalsToRound = -math.floor(math.log10(produceAmount))
			return string.roundNumber(produceAmount, numDecimalsToRound)
		else
			-- convert to an integer - i.e. round down
			return math.floor(produceAmount)
		end
	end
	
	-- add minion produce and profits to the table
	for i = 1, #TIERS, 1 do 
		if not minion.stats[i] then
			return tostring(wikitable)
		end
		local tba = minion.stats[i].tba
		
		-- create the string displayed in the 'produce' column (compatible with {{Resource List}})
		local resourceStr = {}
		-- get first item
		resourceStr[1] = '*' .. getProduceAmountDisplay(items[1], tba, 1) .. ' ' .. items[1].item
		-- get rest of items, if applicable
		for j = 2, #items, 1 do
			resourceStr[#resourceStr + 1] = '\n*' .. getProduceAmountDisplay(items[j], tba, 1) .. ' ' .. items[j].item
		end
		resourceStr = table.concat(resourceStr)
		
		-- create string for profit calculation (compatible with {{BazaarPurchaseCalc}})
		local bazaarStr = {}
		-- get first item
		bazaarStr[1] = '*' .. (p._producePerMinute(items[1].avg, tba) * 60) .. ' ' .. items[1].item
		-- get rest of items, if applicable
		for j = 2, #items, 1 do
			if npcSellPrice(items[j].item) then
				bazaarStr[#bazaarStr + 1] = '\n*' .. (p._producePerMinute(items[j].avg, tba) * 60) * npcSellPrice(items[j].item)
			else
				bazaarStr[#bazaarStr + 1] = '\n*' .. (p._producePerMinute(items[j].avg, tba) * 60) .. ' ' .. items[j].item 
			end
		end
		bazaarStr = table.concat(bazaarStr)
		
		-- same thing as above but for the 24 hour section
		local resourceStr_24 = {}
		resourceStr_24[1] = '*' .. getProduceAmountDisplay(items[1], tba, 24) .. ' ' .. items[1].item
		for j = 2, #items, 1 do
			resourceStr_24[#resourceStr_24 + 1] = '\n*' .. getProduceAmountDisplay(items[j], tba, 24) .. ' ' ..items[j].item
		end
		resourceStr_24 = table.concat(resourceStr_24)
		
		local bazaarStr_24 = {}
		bazaarStr_24[1] = '*' .. (p._producePerMinute(items[1].avg, tba) * 60 * 24) .. ' ' .. items[1].item
		for j = 2, #items, 1 do
			if nonBazaarMerchantSellPrices[items[j].item] then
				bazaarStr_24[#bazaarStr_24 + 1] = '\n*' .. (p._producePerMinute(items[j].avg, tba) * 60 * 24 * nonBazaarMerchantSellPrices[items[j].item])
			else
				bazaarStr_24[#bazaarStr_24 + 1] = '\n*' .. (p._producePerMinute(items[j].avg, tba) * 60 * 24) .. ' ' .. items[j].item
			end
		end
		bazaarStr_24 = table.concat(bazaarStr_24)
		
		-- get harvests per minute
		local hpm
		if minionName == 'Pumpkin' or minionName == 'Melon' or minionName == 'Fishing' then
			hpm = string.roundNumber(60 / (tba), 2)
		else
			hpm = string.roundNumber(60 / (tba * 2), 2)
		end
		
		-- NPC sell price
		local npcPrice, npcPriceSum = {}, 0
		npcPrice[1] = (p._producePerMinute(items[1].avg, tba) * 60 * 24) * (npcSellPrice(items[1].item))
		for j = 2, #items, 1 do
			if items[j].item then
				npcPrice[j] = (p._producePerMinute(items[j].avg, tba) * 60 * 24) * (npcSellPrice(items[j].item))
			end
		end
		for j = 1, #npcPrice do
			npcPriceSum = npcPriceSum + npcPrice[j]
		end
		
		-- add the table cells and fill them with the data from above
		wikitable:tag('tr')
			:tag('th'):wikitext(string._toRoman(i), '<br>{{Slot|', minionName, ' Minion ', string._toRoman(i), '}}'):done()
			:tag('td'):wikitext('<center>{{Green|', hpm, '}}</center>'):done()
			:tag('td'):wikitext('{{Resource List|', resourceStr_24, '}}'):done()
			:tag('td'):wikitext('{{BazaarPurchaseCalc|type=sell|', bazaarStr_24, '}}'):done()
			:tag('td'):wikitext(npcPriceSum ~= 0 and ('{{Coins|%.2f}}'):format(npcPriceSum) or '{{Red|None}}'):done()
		:done()
	end
	
	return tostring(wikitable)
end
-----------------------------------------------------------------------------
-- Template:Minion Profit
--
-- Shows the average bazaar sell price for a specific minion setup
-----------------------------------------------------------------------------
function p.minionProfit(frame)
	local args = getArgs(frame)
	local minion = args[1] or args.minion or title
	local tier = args.tier or args.t
	args.coin = true
	args.productinfo = false
	args.selltobazaar = yesno(args.selltobazaar or args.bazsell, true)
	-- legacy alises support (please use stanard arg names as much as possible!)
	args.diam_spread = args.diamond_spreading or args.diam_spread or args.ds
	args.fuel = args.fuel or args.f
	args.crystal = args.crystal or args.c
	args.bonus = args.bonus or args.other
	args.flycatcher = args.flycatcher or args.fly or args.web
	args.input_time = args.input_time or args.time
	local success, result = safeResponse.call(p._minionProfit, minion, tier, args)
	return result
end
-- <SafeResponse:enabled>
function p._minionProfit(minion, tier, opts)
	local data = minionData[string.ucfirst(minion)]
	if not data then return _error('Invalid minion: '.. minion) end
	-- Remove 'Minion' from minion name
	if minion then
		minion = minion:gsub('(%w)(%w+)', function(t1, t2) return t1:upper() .. t2:lower() end)
		minion = minion:gsub('%s+?[Mm]inion', '')
	end
	local produce = data.items
	
	-- Set time to 1h if not specified
	if not opts.input_time then opts.input_time = 1 end
	-- Set tier to max tier if not specified. convert tier to arabic
	local maxTier = table.length(data.stats)
	if tier then 
		if tonumber(tier) then 
			tier = tonumber(tier)
			if tier > maxTier then return nil end
		else
			tier = string._toArabic(tier)
		end
	else 
		tier = maxTier
	end
	
	if opts.input_time then opts.input_time = tonumber(opts.input_time) or error('Invalid time "' .. opts.input_time .. '"') end
	
	-- Get items produced by minion
	local items = {}
	for i = 1, 25, 1 do -- 25 because some minions like flower minion have very large amount of different drops
		if produce[i] and produce[i].condition == nil then
			items[i] = produce[i]
		elseif produce[i] and produce[i].condition == 'Auto Smelter' and produce[i].item ~= 'Cactus Green' then
			items[i] = produce[i]
			table.remove(items, i - 1)
		elseif produce[i] and produce[i].condition == 'Flint Shovel' then
			items[i] = produce[i]
			table.remove(items, i - 1)
		elseif produce[i] and produce[i].condition == 'Enchanted Egg' then
			items[i] = produce[i]
		end
	end
	
	local tba = data.stats[tier].tba
	local _multiplier = opts.multiplier or p._getMultiplier(minion, opts)
	
	-- Calculate final produce collected
	local totalProduce = {}
	local itemCount = 0
	for i, item in pairs(items) do
		itemCount = itemCount + item.avg
		totalProduce[#totalProduce + 1] = {
			name = item.item,
			num = p._producePerMinute(item.avg, tba / _multiplier) * 60 * opts.input_time
		}
	end
	-- Add corrupt soil items if necessary
	if yesno(opts.corruptsoil) then
		local validMinions = minionAliases.corruptsoilValid
		if table.find(validMinions, minion:lower()) then
			totalProduce[#totalProduce + 1] = {
				name = 'Sulphur',
				num = p._producePerMinute(1, tba / _multiplier) * 60 * opts.input_time
			}
			totalProduce[#totalProduce + 1] = {
				name = 'Corrupted Fragment',
				num = p._producePerMinute(1, tba / _multiplier) * 60 * opts.input_time
			}
		end
	end
	-- Add diamond spreading diamonds if necessary
	if yesno(opts.diam_spread) then
		totalProduce[#totalProduce + 1] = {
			name = 'Diamond',
			num = p._producePerMinute(itemCount, tba / _multiplier) * 60 * opts.input_time / 10
		}
	end
	-- If a sc3000 is being used, use enchanted forms for more accurate price
	if yesno(opts.sc3000) then
		local recipes = table.merge({
			['Enchanted Diamond'] = { {'Diamond', 160} },
			['Enchanted Diamond Block'] = { {'Enchanted Diamond', 160} },
			['Enchanted Sulphur'] = { {'Sulphur', 160} },
			['Enchanted Sulphur Cube'] = { {'Enchanted Sulphur', 160} },
		}, table.deepCopy(data.recipes, true))
		
		local i = 1
		while totalProduce[i] do
			local item = totalProduce[i]
			-- Go down recipe list and see if this item can be upgraded
			for recipeName, recipeList in pairs(recipes) do
				-- If recipe has more than one ingredient sc3000 doesn't work on it
					-- Some items (such as Silver Fang) are ignored due to not having Bazaar support
				if table.length(recipeList) == 1 and (recipeName ~= 'Silver Fang' and recipeName ~= 'Melon (block)') then
					local ingr = recipeList[1]
					if ingr[1] == item.name and item.num >= ingr[2] then
						-- Integer division, since we only want a whole number of craftable amount
						local numToBeCompacted = math.floor(item.num / ingr[2])
						local numRemains = item.num % ingr[2]
						-- If item can be compacted then add new item to list and subtract count away from original recipe ingredient
						if numToBeCompacted > 0 then
							table.insert(totalProduce, i + 1, { name = recipeName, num = numToBeCompacted })
						end
						totalProduce[i].num = numRemains
					end
				end
			end
			i = i + 1
		end
	end
	-- Process all produces and combine duplicate items
	local temp, index = {}, 1
	while totalProduce[index] do
		local v = totalProduce[index]
		local j = table.findIndex(temp, v.name)
		if minion == 'Flower' then
			v.name = 'Any Flower Variant'
		end
		if v.num == 0 then
			table.remove(totalProduce, index)
		elseif j then
			totalProduce[j].num = totalProduce[j].num + v.num
			table.remove(totalProduce, index)
		else
			table.push(temp, v.name)
			index = index + 1
		end
	end
	-- Make a string that can be used in {{BazaarPurchaseCalc}}
	local bazaarValues = {}
	for i, item in pairs(totalProduce) do
		if yesno(opts.selltobazaar, false) and bazaar._getProduct(item.name) then
			bazaarValues[#bazaarValues + 1] = { item.name, item.num }
		else
			local price = (minion == 'Flower' and 1 or npcSellPrice(item.name))
			if price ~= nil then
				bazaarValues[#bazaarValues + 1] = item.num * price
			end
		end
	end
	-- Choose between the buy and sell Bazaar prices
	local priceTypeOpt = (opts.bazaar_price_type or ''):lower()
	local priceType = bazaar.getPriceTypeFromAlias(priceTypeOpt) or 'sell'
	-- Finish
	local finalprice = bazaar._calcMaterialBuyPrices(bazaarValues, priceType, opts.coin)
	if yesno(opts.productinfo) then
		return finalprice, totalProduce
	else
		return finalprice
	end
end
-----------------------------------------------------------------------------
-- Template:Minions page profit table
--
-- More or less p.minionProfit, just in table for each minion
-----------------------------------------------------------------------------
function p.minionFullProfitTable(frame)
	local args = getArgs(frame)
	
	local success, result = safeResponse.call(p._minionFullProfitTable, args)
	return result
end
-- <SafeResponse:enabled>
function p._minionFullProfitTable(args)
	-- These have defaults different from normal profit code due to minion page: sc3000, input_time
	args.sc3000 = yesno(args.sc3000, true)
	args.input_time = args.input_time or 24
	
	-- Store as a list first so we can sort it
	local rowData = {}
	
	for minion, minionDt in pairs(minionData) do
		local _multiplier = p._getMultiplier(minion, args)
		local minionText = table.concat{
			mw.getCurrentFrame():expandTemplate{ title = 'MinionName', args = {minion, short = 'y'} },
			minion == 'Chicken' and '<sup><abbr title="Assumes an Enchanted Egg is being used">ⓘ</abbr></sup>'
				or minion == 'Gravel' and '<sup><abbr title="Assumes a Flint Shovel is being used">ⓘ</abbr></sup>'
				or '',
			_multiplier > 1 and ('<br>+%s%% Boost'):format((_multiplier - 1) * 100) or ''
		}
		
		local function getPrice(minion, tier)
			local ret = {}
			ret[1], ret[2] = {}, {}
			ret[1], ret.products = p._minionProfit(minion, tier, table.merge({ selltobazaar = false, coin = false, productinfo = true, multiplier = _multiplier }, args))
			ret[2] = p._minionProfit(minion, tier, table.merge({ selltobazaar = true, coin = false, productinfo = true, multiplier = _multiplier }, args))
			ret.tba = minionDt.stats[tier] and ('%.2f'):format(minionDt.stats[tier].tba / _multiplier)
			return ret
		end
		
		rowData[#rowData + 1] = { getPrice(minion, 1), getPrice(minion, 3), getPrice(minion, 5), getPrice(minion, 7), getPrice(minion, 9), getPrice(minion, 11), getPrice(minion, #TIERS), text = minionText }
	end
	
	-- Now sort minion from best to worst in terms of profit
	table.sort(rowData, function(a, b)
		local aNpc, bNpc = tonumber(a[6][1]), tonumber(b[6][1])
		local aBz, bBz = tonumber(a[6][2]), tonumber(b[6][2])
		local _a = (aNpc and aBz) and (aNpc > aBz and aNpc or aBz) or (aNpc or aBz)
		local _b = (bNpc and bBz) and (bNpc > bBz and bNpc or bBz) or (bNpc or bBz)
		if _a == nil or _b == nil then
			return false
		else
			return _a > _b
		end
	end)
	
	-- Now construct table
	local wikitable = mw.html.create('table'):addClass('wikitable sortable searchable')
	wikitable:tag('caption'):wikitext(('Profit per %s hours'):format(args.input_time))
	wikitable:tag('tr')
		:tag('th'):wikitext('Minion'):done()
		:tag('th'):attr( 'data-sort-type', 'number' ):wikitext('Tier 1'):done()
		:tag('th'):attr( 'data-sort-type', 'number' ):wikitext('Tier 3'):done()
		:tag('th'):attr( 'data-sort-type', 'number' ):wikitext('Tier 5'):done()
		:tag('th'):attr( 'data-sort-type', 'number' ):wikitext('Tier 7'):done()
		:tag('th'):attr( 'data-sort-type', 'number' ):wikitext('Tier 9'):done()
		:tag('th'):attr( 'data-sort-type', 'number' ):wikitext('Tier 11'):done()
		:tag('th'):attr( 'data-sort-type', 'number' ):wikitext('Tier ' .. #TIERS):done()
	
	-- Now add rows to the table
	for _, data in ipairs(rowData) do
		local row = wikitable:tag('tr')
			:tag('td'):wikitext(data.text):done()
		for count = 1, 7 do
			local npc = {
				val = data[count][1],
				text = string.makeTitle('NPC', 'Price when sold to a shop.'),
			}
			local bz = {
				val = data[count][2],
				text = string.makeTitle('BZ', 'Price when sold to bazaar. Non-bazaar items sold to shop instead.'),
			}
			local products = data[count].products
			local tba = data[count].tba
			row:node(p._createPriceCell(npc, bz, nil, products, tba and tba .. 's' or '', args.shop_first or nil))
		end
	end
	
	return tostring(wikitable)
end

-- Finish Module --
return p
local loader = require('Module:Loader')

local string, table, yesno, libU, cacheM, uiText, Interface, potion, potionUI, random, arguments, pet =
	loader.lazy.require('String', 'Table', 'Yesno', 'LibU', 'Cache', 'UIText', 'UI/Core', 'Potion', 'Potion/UI', 'Random', 'Arguments', 'Pet')
local collectionData, collectionData2, armorSets, potionData =
	loader.lazy.loadData('Collection/Data', 'Collection/UI/Data', 'Armor/Sets', 'Potion/Data')
local explosions, rewardStrings, tradeCosts, tradeAmounts = collectionData2.explosions, collectionData2.rewardStrings, collectionData2.tradeCosts, collectionData2.tradeAmounts

local getArgs = arguments.getArgs
local mergeArgsSyntax = arguments.mergeArgsSyntax
local pagetitle = mw.title.getCurrentTitle()
local p = {}

-- first row positions for Collection UI and Collection (Outer) Rewards UI
local firstRowPositions = {
	--[[1]] { {3, 5} },
	--[[2]] { {3, 4}, {3, 6} },
	--[[3]] { {3, 3}, {3, 5}, {3, 7} },
	--[[4]] { {3, 2}, {3, 4}, {3, 6}, {3, 8} },
	--[[5]] { {3, 3}, {3, 4}, {3, 5}, {3, 6}, {3, 7} },
	--[[6]] { {3, 2}, {3, 3}, {3, 4}, {3, 6}, {3, 7}, {3, 8} },
	--[[7]] { {3, 2}, {3, 3}, {3, 4}, {3, 5}, {3, 6}, {3, 7}, {3, 8} },
	--[[8]] { {3, 1}, {3, 2}, {3, 3}, {3, 4}, {3, 6}, {3, 7}, {3, 8}, {3, 9} },
}
-- X/Y positions for Collection (Inner) Rewards UI
local rewardUIPositions = {
	--[[ 1]] { {3, 5} },
	--[[ 2]] { {3, 4}, {3, 6} },
	--[[ 3]] { {3, 4}, {3, 5}, {3, 6} },
	--[[ 4]] { {3, 2}, {3, 4}, {3, 6}, {3, 8} },
	--[[ 5]] { {2, 2}, {2, 4}, {2, 6}, {2, 8}, {4, 5}, },
	--[[ 6]] { {2, 2}, {2, 4}, {2, 6}, {2, 8}, {5, 4}, {5, 6}, },
	--[[ 7]] { {2, 2}, {2, 4}, {2, 6}, {2, 8}, {3, 3}, {3, 5}, {3, 7}, },
	--[[ 8]] { {3, 3}, {3, 4}, {3, 5}, {3, 6}, {3, 7}, {4, 4}, {4, 5}, {4, 6}, },
	--[[ 9]] { {2, 4}, {2, 5}, {2, 6}, {3, 4}, {3, 5}, {3, 6}, {4, 4}, {4, 5}, {4, 6}, },
	--[[10]] { {2, 4}, {2, 5}, {2, 6}, {2, 7}, {3, 4}, {3, 5}, {3, 6}, {4, 4}, {4, 5}, {4, 6}, },
	--[[11]] { {2, 3}, {2, 4}, {2, 5}, {2, 6}, {2, 7}, {3, 4}, {3, 5}, {3, 6}, {4, 4}, {4, 5}, {4, 6}, },
}
-- maximum of three rows of rewards (or 27 rewards) will be processed
local function calcXY(total, i, isInner)
	if isInner then
		local pos = rewardUIPositions[total][i]
		return pos[1], pos[2]
	else
		local frp = firstRowPositions[total]
		local x, y
		if frp then
			local pos = frp[i]
			x, y = pos[1], pos[2]
		else
			x = 3 + (math.floor(i / 9) - (i % 9 == 0 and 1 or 0))
			y = i % 9
			y = y == 0 and 9 or y
		end
		return x, y
	end
end
local numToEng = {
	'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
	'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
	'nineteen', 'twenty', 'twenty-one', 'twenty-two', 'twenty-three', 'twenty-four', 'twenty-five', 'twenty-six', 'twenty-seven'
}

local function getrandomid()
	return 'ui-' .. random.number{100000000, 999999999}
end
local function wrapdiv(s, wr)
	return yesno(wr, false) and ('<div class="sbw-ui-tabber">%s</div>'):format(s) or s
end
local function frm(...)
	return table.concat(table.map({...}, function(s)
		return string.lower(string.gsub(s, ' ', '-'))
	end), '-')
end
local function typeformatter(item, _type, ttcol, amount)
	local str, tp
	if _type:match('[Ff]arming [Ee]xperience') then
		str = ('&7&8+&3%s'):format(string._formatNum(item) or item)
		tp = '&7' .. 'Farming Experience'
	elseif _type:match('[Ff]ishing [Ee]xperience') then
		str = ('&7&8+&3%s'):format(string._formatNum(item) or item)
		tp = '&7' .. 'Fishing Experience'
	elseif _type:match('[Ff]oraging [Ee]xperience') then
		str = ('&7&8+&3%s'):format(string._formatNum(item) or item)
		tp = '&7' .. 'Foraging Experience'
	elseif _type:match('[Mm]ining [Ee]xperience') then
		str = ('&7&8+&3%s'):format(string._formatNum(item) or item)
		tp = '&7' .. 'Mining Experience'
	elseif _type:match('[Hh]unting [Ee]xperience') then
		str = ('&7&8+&3%s'):format(string._formatNum(item) or item)
		tp = '&7' .. 'Hunting Experience'
	elseif _type:match('[Cc]ombat [Ee]xperience') then
		str = ('&7&8+&3%s'):format(string._formatNum(item) or item)
		tp = '&7' .. 'Combat Experience'
	elseif _type:match('[Ee]nchanting [Ee]xperience') then
		str = ('&7&8+&3%s'):format(string._formatNum(item) or item)
		tp = '&7' .. 'Enchanting Experience'
	elseif _type:match('[Aa]lchemy [Ee]xperience') then
		str = ('&7&8+&3%s'):format(string._formatNum(item) or item)
		tp = '&7' .. 'Alchemy Experience'
	elseif _type:match('[Uu]pgrade') then
		str = ('&a%s'):format(item)
		if amount ~= 0 then
			tp = ('Upgrade &7(+%s slots)'):format(amount)
		end
	elseif _type:match('[Cc]oming [Ss]oon') then
		str = ('&7%s'):format(item)
		if item == 'Coming Soon' then
			str = ('&7&c%s'):format(item)
		end
		tp = '&8(&4COMING SOON&8)'
	elseif _type:match('[Dd]warven [Ff]orge [Rr]ecipe') then
		str = ('&7&%s%s'):format(ttcol, item)
		tp = '&7Dwarven Forge Recipe'
	elseif _type:match('[Ee]ssence') then
		str = ('&d%s Essence &8x%s'):format(item, amount)
	elseif _type:match('[Nn]one') then
		str = ('&7&%s%s'):format(ttcol, item)
	elseif _type:match('[Rr]eward') then
		str = ('&%s%s'):format(ttcol, item)
		if amount ~= 0 then
			str = str .. '&8 x' .. amount
		end
	elseif _type:match('[Rr]ecipe') and item:match('Minion$') then
		str = ('&7&%s%s'):format(ttcol, item)
		tp = '&7Recipes'
	elseif _type:match('[Rr]ecipe') and item:match('Pet$') then
		str = ('&7[Lvl 1] &%s%s'):format(ttcol, string.sub(item,1,-5))
		tp = '&7' .. 'Recipe'
	elseif _type:match('[Rr]ecipe') then
		str = ('&7&%s%s'):format(ttcol, item)
		tp = '&7' .. 'Recipe'
	elseif _type:match('[Tt]rade') then
		str = ('&7&%s%s'):format(ttcol, item)
		tp = '&7' .. 'Trade'
	else
		str = ('&7&%s%s'):format(ttcol, item)
		tp = '&7' .. _type
	end
	return table.concat(table.map(uiText.tooltipBreak(('%s %s'):format(str, tp or ''), 34), function (v) return '&#160;&#160;' .. v end), '/')
end
local function getRarityCol(item)
	-- For getting special case rarity colors
	local function specialCaseColors(item)
		if item:match('[Pp]otion$') then
			local pot = potionData[item:gsub('%s*[Pp]otion', '')]
			if pot then
				return uiText.getColorCode(pot.color)
			end
		end
		if item:match('[Mm]inion$') then return '9' end
		if item:match('[Pp]et$') then return 'f' end
		-- if item:match('Enchanted Book') then return '9' end
		if item:match('[Cc]oming [Ss]oon') then return 'c' end
		if tonumber(item) then return '3' end
	end
	local tooltip = cacheM.getInvslotCache(item, 1)
	local tooltipRarity = tooltip and tooltip.title and tooltip.title:match('^&([a-z0-9])') or nil
	return specialCaseColors(item) or tooltipRarity or 'f'
end
local function processRawRewardStr(rewardstr)
	if not rewardstr then
		return rewardstr
	end

	return table.concat(table.map(uiText.tooltipBreak(rewardstr, 34), function (v) return '&#160;&#160;' .. v end), '/')
end
local function getRewardStr(rewards, req)
	local rewardStr = ('&7Reward%s:/%s'):format(
		#rewards > 1 and 's' or '',
		table.concat(table.map(rewards, function(v)
			local rname = tostring(v[1])
			v = type(v) == 'table' and v or {v}
			local rstr = rewardStrings[rname] or processRawRewardStr(v.rewardstr) or typeformatter(rname, v.type or 'recipe', v.ttcolor or getRarityCol(rname), v.amount or v.slots or 0)
			rstr = rstr:gsub(' ', '&#160;')
			return rstr
		end), '/')
	)
	return ('&f%s &e0&6\\/&e%s&7//%s'):format(
		('-'):rep(20),
		string._formatShortNum(string._toNumber(req) or 0),
		rewardStr
	)
end
local function toShowRecipe(s)
	return s:match('[Rr]ecipe') or s:match('[Cc]oming [Ss]oon') or s:match('[Tt]rade') or s:match('[Rr]eward') or s:match('[Ee]ssence')
end

---------------------------------------------------------------------------------
-- Template: Collection UI
--
-- Main collection UI module, can dive deep into sub-interfaces!
-- Generates <collection>
---------------------------------------------------------------------------------
function p.collectionUI(frame)
	local args = getArgs(frame)
	local res = p._collectionUI(args)
	return res
end
local function subexplode(rewardTb)
	local function process(t)
		if yesno(t.comingsoon, false) or tostring(t[1]):match('[Cc]oming [Ss]oon') then
			t.type = 'Coming Soon'
		end
		return t
	end
	local tb = {}
	for _, reward in ipairs(rewardTb.reward) do
		-- checks all conditions when reward name needs explosion
		local exploded = explosions[reward[1]] or armorSets[reward[1]]
		if exploded then
			for _, v in ipairs(exploded) do
				local t = table.deepCopy(reward)
				if type(v) == 'table' then
					for _, w in ipairs(table.merge(table.namedKeys(v), {1})) do
						t[w] = (v[w] ~= '__NIL__' and v[w] or nil)
					end
				else
					t[1] = v
				end
				table.push(tb, process(t))
			end
		else
			local t = table.deepCopy(reward)
			table.push(tb, process(t))
		end
	end
	rewardTb.reward = tb
	return rewardTb
end
local function explode(collData)
	for i, rewardTb in ipairs(collData) do
		subexplode(rewardTb)
	end
	return collData
end
local function parseTextList(s)
	local rewards = {}
	local count = 0
	local function g(s)
		return s and s:gsub('\255', ',') or nil
	end
	for i, v in ipairs(string.split((s:gsub('\\,', '\255')), '\n')) do
		local _type
		v = string.trim(v)
		if v ~= '' then
			if string.charAt(v, 1) == '*' then
				_type = string.charAt(v, 2) == '*' and 'item' or 'amount'
			end
			if _type == 'amount' then -- * amount[, goto]
				local amount, _goto = unpack(string.split(string.sub(v, 2), "%s*,%s*"))
				count = count + 1
				rewards[count] = {
					required = g(amount),
					_goto = g(_goto and _goto:gsub('^goto%-', '') or nil),
					reward = {},
				}
			elseif _type == 'item' then -- ** reward[, type][, rarity]
				local item, type, rarity = unpack(string.split(string.sub(v, 3), '%s*,%s*'))
				item = g(item or string.sub(v, 3))
				table.push(rewards[count].reward, {
					item,
					ttcolor = g((rarity and rarity ~= '') and uiText.getFormatting(rarity) or nil),
					type = g((type and type ~= "") and string.ucfirst(type)),
				})
			end
		end
	end
	return rewards
end
function p._collectionUI(args)
	libU.checkType(1, args, { 'table' })
	
	libU.assertTrue(args[1], 'No collection specified', 2)
	local collection = args[1] and args[1]:gsub('[Ee][Nn][Cc][Hh][Aa]?[Nn]?[Tt]?[Ee]?[Dd]? ?', ''):gsub('[Bb][Ll][Oo][Cc][Kk] ?[Oo]?[Ff]? ?', '')
	
	local dt = table.deepCopy(collectionData[collection], true)
	if not args[2] and not dt then error('Collection ' .. collection .. ' not found in data') end
	dt = dt or {}
	
	-- Prepare the list from input
	local inputs = args[2] and parseTextList(args[2]) or {}
	
	for i = 1, #inputs do
		-- process/override args
		if inputs[i] then
			dt[i] = {}
			dt[i].reward = {}
			dt[i].required = inputs[i].required
			dt[i]._goto = inputs[i]._goto
			local dtreward, listreward = dt[i].reward, inputs[i].reward or {}
			for j = 1, #listreward do
				dtreward[j] = {
					listreward[j][1],
					ttcolor = listreward[j].ttcolor,
					type = listreward[j].type or 'Recipe',
					comingsoon = listreward[j].comingsoon,
				}
			end
		end
	end
	explode(dt)
	
	local id = args.id or frm(collection, 'default')
	local collection_image = args.collection_image or dt.collectionImage or collection
	local isBossColl = not not (dt.collectionType or ''):match('[Bb]oss')
	
	-- Now prepare parent UI.
	local ui = Interface({
		args.title or (collection and collection .. ' Collection' or pagetitle.rootText),
		id = id, -- this is <collection>
		return_text = args.return_text or args.goback,
		return_link = args.return_link,
		return_id = args.return_id,
		hide = args.hide,
	})
	pretext = ('&7View all your %s Collection progress and rewards!'):format(collection)
	pretext = table.concat(uiText.tooltipBreak(pretext, 34), '/')
	ui:setSlot(1, 5, {
		collection_image,
		link = 'none',
		title = '&e' .. (args.title or collection) .. ' Collection',
		text = pretext .. '//&7Total Collected: &e0',
	})
	local rows, total = 1, #dt
	for i, rewardTb in ipairs(dt) do
		if i > 27 then break end -- Processes upwards of 3 rows of rewards
		-- calculate X, Y
		local x, y = calcXY(total, i)
		-- advance row
		if i % 9 == 0 and i > 0 then
			rows = rows + 1
		end
		local rewardStr = getRewardStr(rewardTb.reward, rewardTb.required)
		local hasRecipe = table.some(rewardTb.reward, function(k, v)
			return toShowRecipe(v.type)
		end)
		local title = ('&%s%s %s'):format(i == 1 and 'e' or 'c', collection, string._toRoman(i))
		local text = ('/&7Progress: &e0&6%%/%s%s'):format(rewardStr, hasRecipe and '//&eClick to view rewards!' or '')
		ui:setSlot(x, y, {
			(i == 1 and 'Yellow' or 'Red') .. ' Stained Glass Pane,' .. i,
			link = 'none',
			class = Interface.makeGotoClass(rewardTb._goto or frm(collection, numToEng[i])),
			title = title,
			text = text,
		})
	end
	
	-- Now prepare all children UIs.
	local hasChildren = false
	local uis = {}
	if yesno(args.fulldepth, false) then
		for i, rewardTb in ipairs(dt) do
			-- create UIs
			local settings = {
				collection, i,
				id = ('%s'):format(frm(collection, numToEng[i])),
				collection_image = collection_image,
				return_text = ('To %s Collection'):format(collection),
				return_id = id,
				hide = true,
				predefined_table = rewardTb,
				predefined_rStr = rewardStr,
				isBossColl = isBossColl,
				fulldepth = true,
			}
			if table.some(rewardTb.reward, function(k, v)
				return toShowRecipe(v.type)
			end) then
				table.push(uis, p._collectionRewardsUI(settings))
				hasChildren = true
			end
		end
	end
	
	return wrapdiv(tostring(ui) .. table.concat(uis), hasChildren and args.clickable)
end

---------------------------------------------------------------------------------
-- Template: Collection Rewards UI
-- 
-- Creates a Collection Rewards UI.
-- Generates <collection>-n
---------------------------------------------------------------------------------
function p.collectionRewardsUI(frame)
	local args = getArgs(frame)
	return p._collectionRewardsUI(args)
end
function p._collectionRewardsUI(args)
	libU.checkType(1, args, { 'table' })
	args.id = args.id or getrandomid()
	
	-- Handling custom inputs from the templates
	local coll, tier, required, items = args[1], tonumber(args[2]), args[3], args[4]
	coll = coll and coll:gsub('[Ee][Nn][Cc][Hh][Aa]?[Nn]?[Tt]?[Ee]?[Dd]? ?', ''):gsub('[Bb][Ll][Oo][Cc][Kk] ?[Oo]?[Ff]? ?', '')
	if not items then
		items, required = required, nil
	end
	items = type(items) == 'string' and mergeArgsSyntax({ items }) or items or {}
	items = table.filter(items, function(v)
		local s = string.trim(v)
		return s ~= '' and s ~= 'nil'
	end)
	
	-- Getting data from database and parsing, letting custom input to override stuff.
	-- Is skipped when predefined_table (the "exploded" rewards table) is passed in.
	local dt
	local tierRoman = string._toRoman(tier or 1)
	local collFullname = ('%s %s'):format(coll, tierRoman)
	if args.predefined_table then
		dt = args.predefined_table
	else
		dt = table.deepCopy(collectionData[coll] and collectionData[coll][tier] or {}, true)
		dt.required = required or dt.required
		if items[1] then
			dt.reward = {}
		end
		for i = 1, #items do
			-- process/override args
			if items[i] then
				local item, id, title, text = libU.pipeline(items[i], string.trim, '%s*,%s*', string.unpackedSplit) -- these are custom inputs
				-- the dt table is info from the database, now we let custom inputs override them
				dt.reward = dt.reward or {}
				dt.reward[i] = {
					item,
					id = id,
					title = title,
					text = text,
					type = 'Recipe',
				}
			end
		end
		subexplode(dt)
	end
	
	-- Now prepare the parent UI.
	local topText = collFullname .. ' Rewards'
	local ui = Interface({
		topText,
		id = args.id, -- this is <collection>-n
		return_text = args.return_text or args.goback,
		return_link = args.return_link,
		return_id = args.return_id, -- this is <collection>
		hide = args.hide,
	})
	pretext = ('&7View your %s Collection rewards!'):format(collFullname)
	pretext = table.concat(uiText.tooltipBreak(pretext, 34), '/')
	ui:setSlot(1, 5, {
		args.collection_image or coll,
		link = 'none',
		title = ('&%s%s'):format(tier > 1 and 'c' or 'e', collFullname),
		text = ('%s%s/&7Progress: &e0&6%%/%s')
			:format(pretext, pretext and '/' or '', args.predefined_rStr or getRewardStr(dt.reward, dt.required or 'unknown'))
	})
	
	local uis = {}
	local todo = table.filter(dt.reward, function(v)
		return toShowRecipe(v.type)
	end)
	for i, reward in ipairs(todo) do
		local rname = reward[1]
		local isMinion, isPotion, isPet, isTrade, isDwarven, isReward, isEssence, comingSoon =
			rname:match('Minion$'),
			rname:match('Potion$'),
			rname:match('Pet$') and reward.type:match('[Rr]ecipe'),
			reward.type:match('[Tt]rade'),
			reward.type:match('[Dd]warven [Ff]orge [Rr]ecipe'),
			reward.type:match('[Rr]eward'),
			reward.type:match('[Ee]ssence'),
			reward.type:match('[Cc]oming [Ss]oon')
		local needChildren = isMinion or isPotion
		local tooltip = cacheM.getInvslotCache(rname, 1)
		local itemName = comingSoon and 'Bedrock' or isEssence and rname .. ' Essence' or rname .. (isMinion and ' I' or '')
		local itemTitle = comingSoon and '&cCOMING SOON' or isEssence and '&d' .. rname .. ' Essence' or (reward.title or (tooltip and tooltip.title) or '')
		local itemText = comingSoon and 'none' or (reward.desc or (tooltip and tooltip.text) or '')
		if isMinion then
			-- replace minion tooltip to what's shown in collection
			itemTitle = itemTitle:gsub(' %S+$', ' Recipes')
			itemText = itemText:gsub('[%s/&7]*Minions[%s/&7]*also[%s/&7]*work[%s/&7]*when[%s/&7]*you[%s/&7]*are[%s/&7]*offline!.*$', '')
		elseif isPet then
			-- replace minion tooltip to what's shown in collection
			petData = pet._petRawText(string.sub(rname,1,-5), {level = 1, rarity = 'Common'})
			itemTitle = petData['title']
			itemText = petData['text']
		end
		local x, y = calcXY(#todo, i)
		local extendTitle = reward.amount and '&8 x' .. reward.amount or ''
		local extendText = (comingSoon or isDwarven) and '' or
			isTrade and '//&7Cost/' .. (tradeCosts[rname] or '') ..'//&eClick to view trades!' or
			isReward and '//&cYou don\'t qualify for this reward!' or
			isEssence and '&7Essence can be used to convert/&7some items into Dungeon items/&7and to repair Dungeon items!///&cYou dont qualify for this reward!' or
			'//&eClick to view recipe' .. ((isMinion or isPotion) and 's' or '') .. '!'
		ui:setSlot(x, y, {
			('%s,%s'):format(itemName, tradeAmounts[rname] or 1),
			link = isTrade and 'Trades' or (needChildren or comingSoon) and 'none' or nil,
			class = needChildren and Interface.makeGotoClass(frm(args.id, 'inner')) or nil,
			title = (itemTitle and itemTitle .. extendTitle or 'none'),
			text = (itemText and itemText .. extendText or 'none'),
		})
	end
	
	-- Now prepare children UIs.
	local hasChildren = false
	if yesno(args.fulldepth, false) then
		for i, reward in ipairs(todo) do
			local rname = reward[1]
			local isMinion, isPotion, comingSoon = rname:match('Minion$'), rname:match('Potion$'), reward.type:match('[Cc]oming [Ss]oon')
			if not comingSoon then
				local settings = {
					rname, coll, tier,
					id = ('%s'):format(frm(args.id, 'inner')), -- this is <collection>-n-inner
					return_id = args.id, -- this is <collection>-n
					hide = true,
					return_text = 'To ' .. topText,
					fulldepth = true,
				}
				if isMinion then
					table.push(uis, p._minionRecipesUI(settings))
					hasChildren = true
				elseif isPotion then
					table.push(uis, p._potionRecipesUI(settings))
					hasChildren = true
				end
			end
		end
	end
	
	return wrapdiv(tostring(ui) .. table.concat(uis), hasChildren and args.clickable)
end

---------------------------------------------------------------------------------
-- Template: (none)
-- 
-- Creates a Recipe Selector.
-- Generates <collection>-n-inner only
---------------------------------------------------------------------------------
function p.recipeSelector(frame)
	local args = getArgs(frame)
	
	return p._recipeSelector(args)
end
function p._recipeSelector(args)
	libU.checkType(1, args, { 'table' })
	args.id = args.id or getrandomid()
	
	-- Handling custom inputs from the templates
	local items = args[1]
	topText = args.title and args.title:gsub('[Ee][Nn][Cc][Hh][Aa]?[Nn]?[Tt]?[Ee]?[Dd]? ?', ''):gsub('[Bb][Ll][Oo][Cc][Kk] ?[Oo]?[Ff]? ?', '')
	items = type(items) == 'string' and mergeArgsSyntax({ items }) or items or {}
	items = table.filter(items, function(v)
		local s = string.trim(v)
		return s ~= '' and s ~= 'nil'
	end)
	local nolink = yesno(args.nolink, true)
	
	-- Getting data from database and parsing, letting custom input to override stuff.
	-- Is skipped when predefined_table (the "exploded" rewards table) is passed in.
	local dt = {}
	for i = 1, #items do
		-- process/override args
		if items[i] then
			local item, id, title, text = libU.pipeline(items[i], string.trim, '%s*,%s*', string.unpackedSplit)
			table.push(dt, {
				item,
				id = id,
				title = title,
				text = text,
			})
		end
	end
	
	-- Prepares the parent (only) UI
	local ui = Interface({
		topText,
		id = args.id,
		return_text = args.return_text or args.goback,
		return_link = args.return_link,
		return_id = args.return_id,
		hide = args.hide,
	})
	for i, reward in ipairs(dt) do
		local rname = reward[1]
		local tooltip = cacheM.getInvslotCache(rname, 1)
		local itemTitle = reward.title or (tooltip and tooltip.title)
		local itemText = reward.desc or (tooltip and tooltip.text)
		if (itemTitle or ''):match('Potion$') then
			-- remove the duration from potion tooltips
			itemText = itemText:gsub('&f%(%d+:%d+&?f?%)', '')
		end
		local x, y = calcXY(#dt, i, true)
		ui:setSlot(x, y, {
			rname,
			link = nolink and 'none' or nil,
			class = Interface.makeGotoClass(frm(args.baseId, numToEng[i])),
			title = (itemTitle or 'none'),
			text = (itemText and itemText .. (itemTitle:match('[Cc]oming [Ss]oon') and '' or '//&eClick to view recipe!') or 'none'),
		})
	end
	
	-- Current implementation: This UI will not make children UIs,
	-- since Minion Recipes and Potion Recipes UI have varying handlers.
	return tostring(ui)
end

---------------------------------------------------------------------------------
-- Template: Minion Recipes UI
--
-- Creates a minion recipes UI
-- Calls on <collection>-n-inner only
---------------------------------------------------------------------------------
function p.minionRecipesUI(frame)
	local args = getArgs(frame)
	return p._minionRecipesUI(args)
end
function p._minionRecipesUI(args)
	libU.checkType(1, args, 'table')
	args.id = args.id or getrandomid()
	
	local minion, col, tier = args.item or args[1], args.collection or args[2], args.reward_tier or args[3]
	if not tier then
		tier, col = col, minion
	end
	tier = string._toRoman(tier or 1) or 'I'
	
	minion = (minion or pagetitle.rootText):gsub('%s[Mm]inion', '')
	col = (col or minion):gsub('%s[Mm]inion', '')
	local back = ('To %s %s Rewards'):format(col, tier)
	
	-- Now prepare the parent UI.
	local fulllist = mergeArgsSyntax({ libU.pipeline('*%s Minion $n\n', minion, string.format, 11, string._repeat):gsub('(%d+)', function(m) return string._toRoman(m) end) })
	local parent = p._recipeSelector{
		fulllist,
		title = minion .. ' Minion Recipes',
		hide = args.hide,
		id = args.id, -- this is <collection>-n-inner
		return_id = args.return_id, -- this is <collection>-n
		baseId = frm(args.id, 'recipe'), -- we want <collection>-n-recipe-inner-n
		return_text = args.return_text or args.goback or back,
		nolink = false,
	}
	
	-- Now prepare children UIs.
	
	return parent
end

---------------------------------------------------------------------------------
-- Template: (none)
--
-- Creates a potion recipes UI
-- Calls on <collection>-n-inner and <collection>-n-recipe-inner-n
---------------------------------------------------------------------------------
function p.potionRecipesUI(frame)
	local args = getArgs(frame)
	return p._potionRecipesUI(args)
end
function p._potionRecipesUI(args)
	libU.checkType(1, args, 'table')
	args.id = args.id or getrandomid()
	
	local pot, col, tier = args.item or args[1], args.collection or args[2], args.reward_tier or args[3]
	if not tier then
		tier, col = col, pot
	end
	tier = string._toRoman(tier or 1) or 'I'
	
	pot = (pot or pagetitle.rootText):gsub('%s[Pp]otion', '')
	col = (col or pot):gsub('%s[Pp]otion', '')
	local back = ('To %s %s Rewards'):format(col, tier)
	
	-- Now prepare the parent UI.
	local topText = pot .. ' Potion Recipes'
	local levels = potion._brewableCount(pot)
	local fulllist = mergeArgsSyntax({ libU.pipeline('*%s $n Potion\n', pot, string.format, levels, string._repeat):gsub('(%d+)', function(m) return string._toRoman(m) end) })
	local parent = p._recipeSelector{
		fulllist,
		title = topText,
		hide = args.hide,
		id = args.id, -- this is <collection>-n-inner
		return_id = args.return_id, -- this is <collection>-n
		baseId = frm(args.id, 'recipe'), -- we want <collection>-n-recipe-inner-n
		return_text = args.return_text or args.goback or back,
		nolink = true,
	}
	
	-- Now prepare children UIs.
	local uis = {}
	local hasChildren = false
	if yesno(args.fulldepth, false) then
		for i = 1, levels do
			table.push(uis, potionUI._potionUI{
				('%s %s'):format(pot, i),
				title = ('%s %s Potion Recipe'):format(pot, string._toRoman(i)),
				id = frm(args.id, 'recipe', numToEng[i]), -- we want <collection>-n-recipe-inner-n
				return_id = args.id, -- this is <collection>-n-inner
				return_text = 'To ' .. topText,
				hide = true,
				appendRecipe = true,
				fulldepth = true,
			})
			hasChildren = true
		end
	end
	
	return wrapdiv(parent .. table.concat(uis), hasChildren and args.clickable)
end

return p
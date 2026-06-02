--<pre>
-- Taken from: https://minecraft.gamepedia.com/Module:UI
local getArgs = require('Module:Arguments').getArgs
local mergeArgsSyntax = require('Module:Arguments').mergeArgsSyntax
local loader = require('Module:Loader')

local string, table, yesno, uiText, inventorySlot, crafting, Interface, random, mctxt =
	loader.lazy.require('String', 'Table', 'Yesno', 'UIText', 'Inventory slot', 'Crafting', 'UI/Core', 'Random', 'Mctxt')

local slot = function(...)
	return inventorySlot.slot(...)
end

local p = {}

local function getrandomid()
	return 'ui-' .. random.number{100000000, 999999999}
end
local function wrapdiv(content, toWrapAsTabber)
	return yesno(toWrapAsTabber, false) and ('<div class="sbw-ui-tabber">%s</div>'):format(content) or content
end
local function slotNotation(m, n)
	if tonumber(m) and tonumber(n) then
		return ('%s, %s'):format(m, n)
	elseif m and not n then
		local m, n = tostring(m):match('^(%d+)%s*,%s*(%d+)$')
		if m and n then
			return ('%s, %s'):format(m, n)
		end
	else
		return false
	end
end
local function rc(r, c, nospace)
	return ('%s,%s%s'):format(r, nospace and '' or ' ', c)
end
local function pagerid(base, i)
	if i > 1 then
		base = ('%s-%s'):format(base, i)
	end
	return base
end

-- Furnace
function p.furnace( frame )
	local args = getArgs(frame)
	
	local body = mw.html.create('span'):addClass('mcui mcui-Furnace')
	
	local input = body:tag('span'):addClass('mcui-input')
	input:wikitext(crafting.addSlot(args, 'Input', 'I'))
	local fuel = input:tag('span'):addClass('mcui-fuel'):done()
	local burning = (( args.Input or '' ) ~= '') or (( args.Fuel or '' ) ~= '')
	if not burning then
		fuel:addClass('mcui-inactive')
	end
	input:wikitext(crafting.addSlot(args, 'Fuel', 'F'))
	
	local arrow = body:tag('span'):addClass('mcui-arrow'):done()
	if not burning or (args.Output or '') == '' then
		arrow:addClass('mcui-inactive')
	end
	
	body:tag('span'):addClass('mcui-output')
		:wikitext(crafting.addSlot(args, 'Output', 'O', 'invslot-large'))
	
	return tostring(mw.html.create('div'):node(body))
end

-- Brewing Stand
function p.brewingStand( frame )
	local args = getArgs(frame)
	
	local body = mw.html.create('span'):addClass('mcui mcui-Brewing_Stand')
	
	local input = body:tag('span'):addClass('mcui-input')
	input:tag('span'):addClass('mcui-bubbling')
	input:wikitext(crafting.addSlot(args, 'Input', 'I'))
	input:tag('span'):addClass('mcui-arrow')
	if (args.Input or '') == '' or
		((args.Output1 or '') == '' and (args.Output2 or '') == '' and (args.Output3 or '') == '')
	then
		input:addClass('mcui-inactive')
	end
	
	body:tag('span'):addClass('mcui-paths')
	
	local output = body:tag('span'):addClass('mcui-output')
	for i = 1, 3 do
		output:wikitext(crafting.addSlot(args, 'Output' .. i, 'O' .. i, 'mcui-output' .. i))
	end
	
	return tostring(mw.html.create('div'):node(body))
end

-- Anvil
function p.anvil( frame )
	local args = getArgs(frame)
	local in1 = crafting.addSlot(args, 'Input1', 'I1')
	local in2 = crafting.addSlot(args, 'Input2', 'I2')
	local out1 = crafting.addSlot(args, 'Output', 'O')
	local header = args.header or 'Repair &amp; Name'
	local title = args.title or ''
	
	local isCrossed = yesno(args.crossed, false)
	local isExpensive = yesno(args.expensive, false) or args.cost == 'expensive'
	local displayCost = args.costtext or
		(args.cost == 'expensive' and 'Too expensive!') or
		(args.cost and 'Enchantment Cost: ' .. args.cost) or nil
	
	local body = mw.html.create('div'):addClass('mcui mcui-Anvil')
	
	local top = body:tag('div'):addClass('mcui-top')
	top:tag('div'):addClass('mcui-hammer')
	local topleft = top:tag('div'):addClass('mcui-topleft')
	topleft:tag('div'):addClass('mcui-header'):wikitext(header)
	local guibar = topleft:tag('div'):addClass('mcui-guibar')
	guibar:tag('div'):addClass('mcui-header mcui-guitext format-f'):wikitext(title)
	
	local bottom = body:tag('div'):addClass('mcui-bottom')
	bottom:node(in1)
	bottom:tag('div'):addClass('mcui-plus')
	bottom:node(in2)
	bottom:tag('div'):addClass('mcui-arrow' .. (isCrossed and ' mcui-disabled' or ''))
	bottom:node(out1)
	
	if displayCost then
		body:tag('div'):addClass('mcui-header mcui-cost' .. (isExpensive and ' mcui-expensive' or '')):wikitext(displayCost)
	end
	
	return tostring(mw.html.create('div'):node(body))
end

-- AnvilSB
function p.anvilSB( frame )
	function handleSkyBlockItemSpecialCases(itemName)
		if not itemName then return nil end
	    itemName = itemName:gsub("Enchanted Book %((.+)%)", "%1")
	    return itemName
	end
	-- Removes strings inside square brackets, inside round brackets, before a colon, after a comma, or after a semicolon
	function determineTitle(itemName)
		if not itemName then return nil end
	    itemName = itemName:gsub("%b[]", ""):gsub("%b()", ""):gsub("[^:]+:", ""):gsub(",[^,]*", ""):gsub(";[^;]*", "")
	    return string.trim(itemName)
	end
	
	local args = getArgs(frame)
	args.header = args.header or 'Combine Items'
	args.costtext = 'Exp Levels Cost: ' .. (string._formatNum(args.cost) or 0)
	
	args.title = args.title or
		handleSkyBlockItemSpecialCases(determineTitle(args.Output)) or
		handleSkyBlockItemSpecialCases(determineTitle(args.Input1)) or ''
	
	return p.anvil(args)
end

-- Melody (this is unrelated to Template:Note Sequence)
function p.noteSequence(f)
	local args = getArgs(f)
	local sequence = args[1]
	return p._noteSequence(sequence)
end
function p._noteSequence(sequence)
	local function simpleSlot(frames)
		frames = inventorySlot.parseFrameText(frames, nil, false, {aliases = '', default = nil})
		local function simpleMakeItem(name)
			return mw.html.create('span'):addClass('invslot-item invslot-item-image'):wikitext('[[File:',name,'.png|32px|link=]]'):done()
		end
		local body = mw.html.create('span'):addClass('invslot animated')
		local activeFrame = 1
		for i, frame in ipairs(frames) do
			local item
			if frame[1] then
				item = body:tag('span'):addClass('animated-subframe')
				local subActiveFrame = 1 --FC-frame.randomise and random(#frame) or 1
				for sI, sFrame in ipairs(frame) do
					local sItem = simpleMakeItem(sFrame.name)
					item:node(sItem)
					
					if sI == subActiveFrame then
						sItem:addClass('animated-active')
					else
						sItem:addClass('hidden')
					end
				end
			else
				item = simpleMakeItem(frame.name)
				body:node(item)
			end
			if i == activeFrame and animated then
				item:addClass('animated-active')
			elseif animated then
				item:addClass('hidden')
			end
		end
		return mw.getCurrentFrame():preprocess(tostring(body))
	end
	
	local colors = {
		'Red',
		'Yellow',
		'Lime',
		'Green',
		'Purple',
		'Blue',
		'Light_Blue'
	}
	
	local slots = {}
	for x = 1, 7, 1 do
		slots[x] = {}
		for y = 1, 6, 1 do
			if y == 5
				then slots[x][y] = sequence:gsub('[' .. x .. ']', 'Block_of_Quartz;')
				else slots[x][y] = sequence:gsub('[' .. x .. ']', colors[x] .. '_Wool;')
			end
			if y == 5
				then slots[x][y] = slots[x][y]:gsub('[%d%s]', colors[x] .. '_Stained_Clay;')
				else slots[x][y] = slots[x][y]:gsub('[%d%s]', colors[x] .. '_Stained_Glass_Pane;')
			end
			if y == 5
				then
					for z = 1, y, 1 do
						slots[x][y] = colors[x] .. '_Stained_Clay;' .. slots[x][y]
					end
					for z = 1, 12-y, 1 do
						slots[x][y] = slots[x][y] .. colors[x] .. '_Stained_Clay;'
					end
				else
					for z = 1, y, 1 do
						slots[x][y] = colors[x] .. '_Stained_Glass_Pane;' .. slots[x][y]
					end
					for z = 1, 12-y, 1 do
						slots[x][y] = slots[x][y] .. colors[x] .. '_Stained_Glass_Pane;'
					end
			end
			slots[x][y] = slots[x][y]:gsub('[_]', ' ')
		end
	end
	
	local table = mw.html.create('table'):addClass('mcui mcui-Crafting_Table'):css({margin = '0 auto', display = 'table', cursor = 'not-allowed'})
	
	for y = 1, 6, 1 do
		local row = table:tag('tr'):addClass('mcui-row')
		row:tag('td'):wikitext(simpleSlot('Gray Stained Glass Pane')):done()
		for x = 1, 7, 1 do
			row:tag('td'):wikitext(simpleSlot(slots[x][y])):done()
		end
		row:tag('td'):wikitext(simpleSlot('Gray Stained Glass Pane')):done()
		row:done()
	end
	table:done()
	return tostring(table)
end

---------------------------------------------------------------------------------
-- Template: UIPage
-- 
-- Imports (transclude) another UI page with custom options on its first UI.
---------------------------------------------------------------------------------
function p.uipage(frame)
	local args = getArgs(frame)
	local page = args.page or args[1]
	
	return frame:preprocess(p._uipage(page, args))
end
function p._uipage(page, args)
	local function injectParamsBoolean(callStr, args)
		for param, value in pairs(args) do
			if value then
				value = tostring(yesno(value))
				callStr, n = callStr:gsub('|%s*' .. param .. '%s*=.-%f[|}]','|' .. param .. '=' .. value .. '\n')
				if n == 0 then callStr = callStr:sub(0,callStr:len()-2) .. '|' .. param .. '=' .. value .. '}}' end
			end
		end
		return callStr
	end
	local function injectParamsString(callStr, args)
		for param, value in pairs(args) do
			if value then
				callStr, n = callStr:gsub('|%s*' .. param .. '%s*=.-%f[|}]','|' .. param .. '=' .. value .. '\n')
				if n == 0 then callStr = callStr:sub(0,callStr:len()-2) .. '|' .. param .. '=' .. value .. '}}' end
			end
		end
		return callStr
	end
	
	local return_id = args.return_id
	local extPageTitle = mw.title.new(page, 0)
	
	if not extPageTitle.exists then error('Specified page does not exist, page: ' .. page) end
	local extPageContent = extPageTitle:getContent()
	
	local ls = string.matchAll(extPageContent,'%b{}')
	local finalStr = ''
	local firstUI = true
	
	if ls.n < 1 then return '' end
	
	for i = 1, ls.n, 1 do
		local callStr = ls[i][1]
		local x, y = callStr:find('{{UI|', 1, true)
		if not x then x, y = callStr:find('{{UI Pager|', 1, true) end
		local x1, y1, subpage, subparams = callStr:find('{{UIPage|(.-)%f[|}](.-)}}')
		if x == 1 then
			if firstUI then -- first UI on page, apply all the custom settings to this UI
				callStr = injectParamsBoolean(callStr, {
					hide = yesno(args.hide,true),
					fill = args.fill, 
					rows = args.rows,
					cols = args.cols,
					noarrow = args.noarrow,
					noclose = args.noclose,
				})
				callStr = injectParamsString(callStr, {
					id = args.id,
					goback = (args.return_text or args.goback),
					goback_link = args.goback_link,
					return_id = args.return_id,
					arrow = (args.arrow or args.arrow_),
					close_ = (args.close or args.close_),
				})
				firstUI = false
			end
			finalStr = finalStr .. callStr
		elseif x1 == 1 then
			subparams = subparams and subparams:gsub('^[|%s]*(.-)[|%s]*$','%1') or ''
			local subargs = {}
			for _, param in ipairs(string.split(subparams,'|')) do
				if param:match('=') then
					param = string.split(param, '=')
					subargs[param[1]] = param[2]
				else
					-- no positional arguments for UIPage at the moment
				end
			end
			
			finalStr = finalStr .. p._uipage(subpage, subargs)
		end
	end
	return finalStr
end

---------------------------------------------------------------------------------
-- Template: UI
-- 
-- Creates a UI.
---------------------------------------------------------------------------------
function p.ui(frame)
	local args = getArgs(frame, { removeBlanks = false })
	
	local ui = Interface(args)
	
	local x, y, rowCount = 1, 1, 1
	local maxRows, maxCols = tonumber(args.rows) or 6, tonumber(args.cols) or 9
	local fill = yesno(args.fill, true)
	local defaultnolink = yesno((args['defaultnolink'] or args['dnl']), false)
	
	local function decodeCommas(...)
		local t = { ... }
		for i, v in ipairs(t) do
			t[i] = t[i]:gsub('\255', ',')
		end
		return unpack(t)
	end
	
	local function setSlot(v, x, y)
		local isCustom = v:match('<%a-(.-)>(.-)</%a->')
		
		v = v:gsub('\\,', '\255')
		local val, id, title, text = decodeCommas(string.unpackedSplit(v, '%s*,%s*'))
		
		local _val = val
		local val, num = val:match('^%s*(.+)%s*[;]%s*(%d+)%s*$')
		val = val or _val
		
		local link_specify
		if not id or id == '' then id = nil
		else
			local _id = id
			id, link_specify = id:match('^%s*(.+)%s*[;]%s*(.+)%s*$')
			id = id or _id
		end
		
		-- [IMPORTANT] Transform newlines into `/`
		if text and text:match('\n') then
			text = text:gsub('\n', '/')
		end
		
		ui:setSlot(x, y, isCustom and v or {
			val .. (num and ', ' .. num or ''),
			class = (id and id ~= 'none') and 'goto-' .. id:gsub('^goto%-', ''),
			link = (id and id ~= 'none') and 'none' or (link_specify or (defaultnolink and 'none' or'')),
			title = title,
			text = text,
		}, isCustom)
	end
	
	for i, v in ipairs(args) do
		if i > 1 then
			if x > 6 then break; end
			
			if v:match('^%-$') then
				for y2 = y, maxCols do
					if fill then
						ui:setBlankSlot(x, y2)
					else
						ui:setSlot(x, y2, '')
					end
				end
				x = x+1
				y = 1
			elseif y > maxCols then
				y = 1
				x = x+1
			else
				setSlot(v, x, y)
				y = y+1
			end
		end
	end
	
	for k, v in pairs(args) do
		local k = tostring(k)
		
		if k:match('^%d+%s*,%s*%d+$') then
			local x, y = k:match('^(%d+)%s*,%s*(%d+)$')
			
			setSlot(v, tonumber(x), tonumber(y))
		elseif k:match('^row%s*([1-6])%s*$') then
			local x = k:match('^row%s*([1-6])$')
			local endParams = v:match('%s*;%s*([%d%s,]-)%s*$')
			v = v:gsub('%s*;%s*([%d%s,]-)%s*$', '')
			
			endParams = endParams and string.split(endParams, '%s*,%s*') or {1, maxCols}
			
			if #endParams > 2 then
				for dummy, y in pairs(endParams) do
					setSlot(v:gsub('%$n', y):gsub('\\%$n', '$n'), tonumber(x), tonumber(y))	
				end
			else
				for y = tonumber(endParams[1] or 1), tonumber(endParams[2] or maxCols), 1 do
					setSlot(v:gsub('%$n', y):gsub('\\%$n', '$n'), tonumber(x), tonumber(y))	
				end
			end
			
		elseif k:match('^colu?m?n?%s*([1-9])%s*$') then
			local y = k:match('^colu?m?n?%s*([1-9])%s*$')
			local endParams = v:match('%s*;%s*([%d%s,]-)%s*$')
			v = v:gsub('%s*;%s*([%d%s,]-)%s*$', '')
			
			endParams = endParams and string.split(endParams, '%s*,%s*') or {1, maxRows}
			
			if #endParams > 2 then
				for dummy, x in pairs(endParams) do
					setSlot(v:gsub('%$n', x):gsub('\\%$n', '$n'), tonumber(x), tonumber(y))
				end
			else
				for x = tonumber(endParams[1] or 1), tonumber(endParams[2] or maxRows), 1 do
					setSlot(v:gsub('%$n', x):gsub('\\%$n', '$n'), tonumber(x), tonumber(y))
				end
			end
		end
	end
	
	return tostring(ui)
end

---------------------------------------------------------------------------------
-- Template: UI Pager
-- 
-- An automatic pager for UIs.
---------------------------------------------------------------------------------
function p.uiPager(frame)
	local args = getArgs(frame, { removeBlanks = false })
	local id = args.id or getrandomid()
	
	if yesno(args.title_index, false) and not yesno(args.index_last, false) then
		args[1] = '({0}/{1}) ' .. args[1]
	else
	if yesno(args.title_index, false) and yesno(args.index_last, false) then
		args[1] = args[1] .. ' ({0}/{1})'
	end
	end
	
	local ui = table.merge({
		[1] = args[1],
		fill = 'border',
	}, table.mapNamed(args, function (k, v)
		if type(k) ~= 'number' then return v else return nil end
	end))
	
	-- allocate items onto UI pages
	local pages = {}
	local rows, cols = args.rows or 6, args.cols or 9
	local i = 2
	while args[i] do
		local ui2 = table.deepCopy(ui)
		for r = 2, rows - 1 do
			for c = 2, cols - 1 do
				if args[i] then
					ui2[rc(r, c)] = args[i]
					i = i + 1
				else
					break
				end
			end
		end
		table.push(pages, ui2)
	end
	
	return wrapdiv(table.concat(table.map(pages, function (v, i, t)
		if t[i - 1] and not (v[rc(rows, 1)] or v[rc(rows, 1, true)]) then
			v[rc(rows, 1)] = ('Arrow, %s, &aPrevious Page, &ePage %s'):format(pagerid(id, i - 1), i - 1)
		end
		if t[i + 1] and not (v[rc(rows, cols)] or v[rc(rows, cols, true)]) then
			v[rc(rows, cols)] = ('Arrow, %s, &aNext Page, &ePage %s'):format(pagerid(id, i + 1), i + 1)
		end
		v.id = pagerid(id, i)
		if i > 1 then
			v.hide = true
		else
			v.hide = args.hide
		end
		v[1] = v[1]:gsub('{0}', i):gsub('{1}', #t)
		return tostring(p.ui(v))
	end)), #pages > 1 and args.clickable)
end

---------------------------------------------------------------------------------
-- Template: ShopUI
-- 
-- Creates a Shop UI using UIpager.
---------------------------------------------------------------------------------
function p.shopUI(frame)
	local args = getArgs(frame, { removeBlanks = false })
	local confslot = slotNotation(args.confirmation)
	local opts = {}
	if yesno(args.confirmation) or confslot then
		opts[confslot or '6, 4'] = 'Lime Dye, none; none, &aShop Confirmations, &7Confirm when purchasing items/&7worth at least a million coins.//&eClick to disable!'
	end
	if not (yesno(args.close) or slotNotation(args.close)) then
		opts['6, 5'] = 'Hopper, none; none, &aSell Item, &7Click items in your inventory to/&7sell them to this Shop!'
	end
	return p.uiPager(table.merge(opts, table.deepCopy(args, true)))
end

---------------------------------------------------------------------------------
-- Template: Rewards UI
-- 
-- Creates a Rewards UI.
---------------------------------------------------------------------------------
function p.rewardsUI(frame)
	local function getTot(first, second, step)
		return first * (math.floor(step / 2) + (step % 2)) + second * math.floor(step / 2)
	end
	local function getMinMax(i_min, first, second, all_n, step, cols)
		local tot_n = getTot(first, second, cols)
		local incr = getTot(first, second, step)
		return i_min, i_min + tot_n - 1, i_min + incr, (step % 2 == 0 and first or second)
	end
	
	local args = getArgs(frame, { removeBlanks = false })
	local id = args.id or getrandomid()
	if yesno(args.title_index, false) then
		args[1] = '({0}/{1}) ' .. args[1]
	end
	local ui = table.merge({
		[1] = args[1],
	}, table.mapNamed(args, function (k, v)
		if type(k) ~= 'number' then return v else return nil end
	end))
	 -- force row, col
	local rows, cols = 6, 9
	ui.rows, ui.cols = 6, 9
	-- fixed maps for snake height of 4, snake gap of 1
	local rowmap = { 4, 3, 2, 1, 1, 1, 2, 3, 4 }; rowmap[0] = 4
	local advancemap = { 0, 0, 0, 1, 1, 0, 0, 0, 1 }; advancemap[0] = 1
	-- slot allocation
	local step = args.step or 8
	local pages = {}
	local all_n, next_colsize, next_min, cont = table.xlength(args, false, true) - 1, 4, 2, true
	local min, max
	while cont do
		min, max, next_min, next_colsize = getMinMax(next_min, next_colsize, 4 + 1 - next_colsize, all_n + 1, step, cols)
		local ui2, index, c = table.deepCopy(ui), 0, 1
		for i = min, max do
			if args[i] then
				index = index + 1
				ui2[rc(rowmap[index % 10], c)] = args[i]
				c = c + advancemap[index % 10]
			else
				cont = false
				break
			end
		end
		table.push(pages, ui2)
	end
	local page_n = #pages
	return wrapdiv(table.concat(table.map(pages, function (v, i, t)
		if page_n > 1 and t[i - 1] and not (v[rc(rows, 1)] or v[rc(rows, 1, true)]) then
			v[rc(rows, 1)] = ('Arrow, %s, &aScroll Left, &eLeft-click to scroll!/&eRight-click to scroll fast!'):format(pagerid(id, i - 1))
		end
		if page_n > 1 and t[i + 1] and not (v[rc(rows, cols)] or v[rc(rows, cols, true)]) then
			v[rc(rows, cols)] = ('Arrow, %s, &aScroll Right, &eLeft-click to scroll!/&eRight-click to scroll fast!'):format(pagerid(id, i + 1))
		end
		v.id = pagerid(id, i)
		if i > 1 then
			v.hide = true
		else
			v.hide = args.hide
		end
		v[1] = v[1]:gsub('{0}', i):gsub('{1}', #t)
		return tostring(p.ui(v))
	end)), #pages > 1 and args.clickable)
end

---------------------------------------------------------------------------------
-- Template: Skill UI
-- 
-- Creates a Skill UI.
---------------------------------------------------------------------------------
local skillUISlotMap = {
	'2, 1', '3, 1', '4, 1', '4, 2', '4, 3',
	'3, 3', '2, 3', '1, 3', '1, 4', '1, 5',
	'2, 5', '3, 5', '4, 5', '4, 6', '4, 7',
	'3, 7', '2, 7', '1, 7', '1, 8', '1, 9',
	'2, 9', '3, 9', '4, 9', '5, 9', '6, 9'
}
function p.skillUI(frame)
	local args = getArgs(frame, { removeBlanks = false })
	local id = args.id or getrandomid()
	if yesno(args.title_index, false) then
		args[1] = '({0}/{1}) ' .. args[1]
	end
	local pageSize = #skillUISlotMap
	local ui = table.merge({
		[1] = args[1],
	}, table.mapNamed(args, function (k, v)
		if type(k) ~= 'number' then return v else return nil end
	end))
	-- slot allocation
	local pages = {}
	local item_n, index, ui2 = table.xlength(args, false, true) - 1, 0, table.deepCopy(ui)
	while args[index + 2] do
		ui2[skillUISlotMap[index % pageSize + 1]] = args[index + 2]
		if index % pageSize == (pageSize - 1) then
			table.push(pages, ui2)
			ui2 = table.deepCopy(ui)
		end
		index = index + 1
	end
	if #pages < 1 or index % pageSize > 0 --[[ ensure there are new things in the ui2 ]] then
		table.push(pages, ui2)
	end
	local page_n = #pages
	return wrapdiv(table.concat(table.map(pages, function (v, i, t)
		if page_n > 1 then
			local targetPage = i + 1 > page_n and 1 or i + 1 -- cyclic
			v['6, 6'] = ('Arrow, %s, &aLevels %s - %s, &eClick to view!'):format(pagerid(id, targetPage), (targetPage - 1) * pageSize + 1, math.min(targetPage * pageSize, item_n))
		end
		v.id = pagerid(id, i)
		if i > 1 then
			v.hide = true
		else
			v.hide = args.hide
		end
		v[1] = v[1]:gsub('{0}', i):gsub('{1}', #t)
		return tostring(p.ui(v))
	end)), #pages > 1 and args.clickable)
end

---------------------------------------------------------------------------------
-- Template: Book
-- 
-- Creates a book UI.
---------------------------------------------------------------------------------
function p.bookUI(frame)
	local args = getArgs(frame)
	
	-- We need to know how many pages there are before we can start main loop for next/prev buttons
	local pages, i = {}, 1
    while args[i] do
        pages[#pages+1] = args[i]
        i = i + 1
    end
	
	local t = {}
	for i, pageContent in ipairs(pages) do
		local pageTag = mw.html.create('div'):attr('id', 'ui-page'..i)
			:addClass('mcui-Book_Page sbw-ui-tab-content')
			:addClass(i==1 and '' or 'hidden')
		
		pageTag:tag('div'):addClass("mcui-page-count")
			:wikitext(mctxt.raw{ table.concat{ "Page ",  i," of ", #pages } }):done()
		
		pageTag:wikitext(mctxt.raw{ pageContent })
		-- Next/Prev buttons
		if #pages > 1 then
			local nav = pageTag:tag('div'):addClass('mcui-page-nav')
			--prev
			if i > 1 then
				nav:tag('div'):addClass('invslot goto-page'..(i-1)):wikitext("[[File:Book Arrowleft.png|link=#]]"):done()
			else
				nav:tag('div'):done() -- empty need for formatting
			end
			-- next
			if i < #pages then
				nav:tag('div'):addClass('invslot goto-page'..(i+1)):tag('div'):css{ transform= "scaleX(-1)" }:wikitext("[[File:Book Arrowleft.png|link=#]]")
			else
				nav:tag('div'):done() -- empty need for formatting
			end
		end
		
		t[#t+1] = tostring(pageTag)
	end
	
	return wrapdiv(table.concat(t), #pages > 1)
end

p.createBlankUI = Interface
return p
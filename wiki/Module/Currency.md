-- <pre>
local p = {}

local loader = require('Module:Loader')
local getArgs = require('Module:Arguments').getArgs

local string, table, yesno, colorMdl = loader.require('String', 'Table', 'Yesno', 'Color')
local currencyData, bazaarData = loader.loadData('Currency/Data', 'Bazaar/Data')

local formatNum, shorten, toNumber = string._formatNum, string._formatShortNum, string._toNumber

local lang = mw.language.getContentLanguage()

----------------------------------------------------------------------------------------------------
-- Template:Currency access point
--
--
----------------------------------------------------------------------------------------------------
function p.currency(frame)
	local args = getArgs(frame)
	
	local s = tostring(args[1])
	if s and s:match('</font>') then return s end
	s = s and s:gsub('%s*([Ss]ky[Bb]lock)?', '')
	local m = args[2]
	local useShort = yesno(args['short'] or args['s'] , false)
	local useApproximate = yesno(args['approximate'] or args['approx'] or args['a'], false)
	local useImage = yesno(args['image'] or args['i'] or args['si'] or args['show_image'], false)
	local noLink = yesno(args['nolink'] or args['nl'], false)
	local imageInFront = yesno(args['image_in_front'] or args['iif'], false)
	local alt = args['alt']
	
	return p._currencyTemplate(s, m, useShort, useApproximate, useImage, noLink, imageInFront, alt)
end
function p._currencyTemplate(s, m, useShort, useApproximate, useImage, noLink, imageInFront, alt)
	local curr
	if s:find('[Gg]ems?') then
		s = s:gsub('[Gg]ems?', '')
		curr = 'gems'
	elseif s:find('[Bb]its?') then
		s = s:gsub('[Bb]its?', '')
		curr = 'bits'
	elseif s:find('[Pp]elts?') then
		s = s:gsub('[Pp]elts?', '')
		curr = 'pelts'
	elseif s:find('[Tt]okens?') then
		s = s:gsub('[Tt]okens?', '')
		curr = 'tokens'
	elseif s:find('[Bb]ingo [Pp]oints?') then
		s = s:gsub('[Bb]ingo [Pp]oints?', '')
		curr = 'bingoPoints'
	elseif s:find('[Nn]orth [Ss]tars?') then
		s = s:gsub('[Nn]orth [Ss]tars?', '')
		curr = 'northStars'
	elseif s:find('[Cc]opper') then
		s = s:gsub('[Cc]opper', '')
		curr = 'copper'
	elseif s:find('[Mm]otes?') then
		s = s:gsub('[Mm]otes?', '')
		curr = 'motes'
	elseif s:find('[Cc]hocolate?') then
		s = s:gsub('[Cc]hocolate?', '')
		curr = 'chocolate'
	elseif s:find('[Ff]ossil [Dd]ust?') then
		s = s:gsub('[Ff]ossil [Dd]ust?', '')
		curr = 'fossilDust'
	elseif s:find('[Cc]arnival [Tt]okens?') then
		s = s:gsub('[Cc]arnival [Tt]okens?', '')
		curr = 'carnivalTokens'
	elseif s:find('[Pp]ests?') then
		s = s:gsub('Pp]ests?', '')
		curr = 'pests'
	else
		s = s:gsub('[Cc]oins?', '')
		curr = 'coins'
	end
	return p._currency(s, m, {
		useShort = useShort, 
		useApproximate = useApproximate, 
		useImage = useImage, 
		noLink = noLink, 
		imageInFront = imageInFront, 
		alt = alt, 
		currency = curr,
	})
end

local function getImg(val, t)
	if type(t) ~= 'table' then return {t} end
	if type(t[1]) ~= 'table' then return {t[1]} end
	for i, v in ipairs(t) do
		if (not v.lim or v.lim == 'inf') -- no upper limit, or upper limit is inf
			or (i == table.length(t)) -- reached last element in table
			or (val < v.lim)
		then
			return v
		end
	end
end

-- Module access point
function p._currency(...)
	local s, m, options, useShort, useApproximate, useImage, noLink, imageInFront, alt, currency
	-- Support numbered arguments
	if type(({...})[3]) ~= 'table' then
		s, m, useShort, useApproximate, useImage, noLink, imageInFront, alt, currency = ...
	else
		s, m, options = ...
		useShort, useApproximate, useImage, noLink, imageInFront, alt, currency =
			options.useShort,
			options.useApproximate,
			options.useImage,
			options.noLink,
			options.imageInFront,
			options.alt,
			options.currency
	end
	
	local a, b = tostring(s):match('^%s*(%-?%d+)%s*%-%s*(%-?%d+)%s*$')
	if not not a and not not b then
		s = a
		m = b
	end
	
	-- Default values
	if not currency then currency = 'coins' end
	useShort = useShort or false
	useApproximate = useApproximate or false
	currency = currencyData[currency]
	
	-- If first value is scientific notation
	if s and string.find(tostring(s), '10%^%d*') then
		--if not useShort, return scientific notation. if useShort, convert scientific notation to number
		if not useShort then
			s = s:gsub('%s+?%*%s+?', ' × ')
			s = s:gsub('10%^(%d*)', '10<sup>%1</sup>')
			return table.concat({
				colorMdl._colorTemplates(currency.numcolor or currency.color, s),
				'[[', currency.destPage, '|', colorMdl._colorTemplates(currency.color, currency.name), ']]'
			})
		else
			if s:find('%*') then
				local number = s:match('(%d*)%s?*%s+?10%^%d*')
				local exponent = s:match('%d*%s?*%s+?10%^(%d*)')
				s = tonumber(number) * math.pow(10, tonumber(exponent))
			else
				local toShort = s:match('10%^(%d*)')
				s = math.pow(10, tonumber(toShort))
			end
		end
	-- If first value isn't a valid number, just return the invalid number as a fallthrough
	elseif s and toNumber(s) == nil then
		return s
	-- If first value is null, just return colored currency text
	elseif s == nil then
		return table.concat({
			'[[', currency.destPage, '|', colorMdl._colorTemplates(currency.color, alt and alt or currency.pluralName or (currency.name .. 's')), ']]'
		})
	end
	
	-- Convert params to numbers - nil if not a number
	s = toNumber(s)
	m = toNumber(m)
	local sAsNumber = s
	local mAsNumber = m
	
	image = ''
	if (useImage or imageInFront) and currency.images then
		local img_ = getImg(s, currency.images)
		
		image = table.concat{
			'[[File:', img_[1], '.png|', 
			img_.size or 24, 'px', 
			'|link=', (noLink and '' or currency.destPage), ']]'
		}
		image = image .. '&thinsp;'
	end
	
	local tooltip = nil
	if useShort then
		if m then
			tooltip = formatNum(s) .. '–' .. formatNum(m)
		elseif s then
			tooltip = formatNum(s)
		end
		s = shorten(s)
		if m then
			m = shorten(m)
		end
	else
		s = formatNum(s)
		if m then
			m = formatNum(m)
		end
	end
	
	local g = mw.html.create('span')
		:attr('title', tooltip)
		:css('font-variant-numeric', 'tabular-nums')
	if useApproximate then
		g:wikitext('&#8776;')
	end
	if m then
		t = s .. '–' .. m .. '&nbsp;'
		g:wikitext(t)
	elseif s then
		t = s .. '&nbsp;'
		g:wikitext(t)
	end
	
	return mw.html.create('span')
		:css('color', currency.color)
		:wikitext(
			(imageInFront and image or ''),
			colorMdl._colorTemplates(currency.numcolor or currency.color, tostring(g)),
			(imageInFront and '' or image),
			'[[', currency.destPage, '|', colorMdl._colorTemplates(currency.color, alt and alt or lang:plural(mAsNumber and mAsNumber or sAsNumber, currency.name, currency.pluralName or (currency.name .. 's'))), ']]'
		)
end

-- Used in Module:Inventory_slot
function p._newCurrencySlot(s, m, noLink)
	local currency
	-- only parse if starts with number
	if type(s) ~= 'string' or not s:find('^%s*%d') then return end
	if s:find('[Gg]ems?%s*$') then
		s = s:gsub('[Gg]ems?%s*$', '')
		currency = 'gems'
	elseif s:find('[Bb]its?%s*$') then
		s = s:gsub('[Bb]its?%s*$', '')
		currency = 'bits'
	elseif s:find('[Pp]elts?%s*$') then
		s = s:gsub('[Pp]elts?%s*$', '')
		currency = 'pelts'
	elseif s:find('[Tt]okens?%s*$') then
		s = s:gsub('[Tt]okens?%s*$', '')
		currency = 'tokens'
	elseif s:find('[Bb]ingo [Pp]oints?%s*$') then
		s = s:gsub('[Bb]ingo [Pp]ointselts?%s*$', '')
		currency = 'bingoPoints'
	elseif s:find('[Nn]orth [Ss]tars?%s*$') then
		s = s:gsub('[Nn]orth [Ss]tars?%s*$', '')
		currency = 'northStars'
	elseif s:find('[Cc]opper%s*$') then
		s = s:gsub('[Cc]opper%s*$', '')
		currency = 'copper'
	elseif s:find('[Mm]otes?%s*$') then
		s = s:gsub('[Mm]otes?%s*$', '')
		currency = 'motes'
	elseif s:find('[Cc]hocolate?%s*$') then
		s = s:gsub('[Cc]hocolate?%s*$', '')
		currency = 'chocolate'
	elseif s:find('[Ff]ossil [Dd]ust?') then
		s = s:gsub('[Ff]ossil [Dd]ust?', '')
		currency = 'fossilDust'
	elseif s:find('[Cc]arnival [Tt]okens?%s*$') then
		s = s:gsub('[Cc]arnival [Tt]okens?%s*$', '')
		currency = 'carnivalTokens'
	elseif s:find('[Pp]ests?') then
		s = s:gsub('Pp]ests?', '')
		currency = 'pests'
	elseif s:find('[Cc]oins?%s*$') then
		s = s:gsub('[Cc]oins?%s*$', '')
		currency = 'coins'
	else return end
	
	if s then
		assertTrue(type(tostring(s)) == 'string')
		
		temp = string.split(tostring(s), '-')
		if (#temp == 2) then
			s = temp[1]
			m = temp[2]
		end
	end
	
	if not currency then currency = 'coins' end
	currency = currencyData[currency]
	
	-- If first value is scientific notation
	if s and string.find(tostring(s), '10%^%d*') then
		--if not useShort, return scientific notation. if useShort, convert scientific notation to number
		if s:find('%*') then
			local number = s:match('(%d*)%s?*%s+?10%^%d*')
			local exponent = s:match('%d*%s?*%s+?10%^(%d*)')
			s = tonumber(number) * math.pow(10, tonumber(exponent))
		else
			local toShort = s:match('10%^(%d*)')
			s = math.pow(10, tonumber(toShort))
		end
	-- If first value isn't a valid number, return nil as conversion failed
	-- If first value is null, also return nil as conversion failed
	elseif toNumber(s) == nil then
		return
	end
	
	-- Convert params to numbers - nil if not a number
	s, m = toNumber(s), toNumber(m)
	local sAsNumber = s
	
	image = ''
	local source = currency.images or currency.placeholder
	local item = getImg(m or s, source)[1]
	
	local grouped_num, tooltip
	if m then
		grouped_num = ('%.f-%.f'):format(s, m)
		tooltip = formatNum(s) .. '-' .. formatNum(m)
	elseif s then
		grouped_num = ('%.f'):format(s)
		tooltip = formatNum(s)
	end
	
	return {
		name = item,
		link = noLink and '' or currency.destPage,
		title = ('%s%s %s'):format(
			currency.tooltipcolor, 
			tooltip,
			lang:plural(sAsNumber, currency.name, currency.pluralName or (currency.name .. 's'))
			),
		text = '',
		num = s,
		num2 = m,
	}
end

local function generateCurrencyFunc(currencyName, substituteRegex)
	local function _main(s, m, useShort, useApproximate, useImage, noLink, imageInFront, alt)
		return p._currency(s, m, {
			useShort = useShort, 
			useApproximate = useApproximate, 
			useImage = useImage, 
			noLink = noLink, 
			imageInFront = imageInFront, 
			alt = alt, 
			currency = currencyName,
		})
	end
	local function main(frame)
		local args = getArgs(frame)
		local callfn = _main
		
		if args[1] and args[1]:match('</font>') then return args[1] end
		if args[1] then
			s = args[1]:lower():gsub('[%[%]]+', ''):gsub(substituteRegex, '')
		end
		local m = args[2]
		local useShort = yesno(args['short'] or args['s'] , false)
		local useApproximate = yesno(args['approximate'] or args['approx'] or args['a'], false)
		local useImage = yesno(args['image'] or args['i'] or args['si'] or args['show_image'], false)
		local noLink = yesno(args['nolink'] or args['nl'], false)
		local imageInFront = yesno(args['image_in_front'] or args['iif'], false)
		local alt = args['alt']
		
		if args['approximate'] or args['approx'] or args['a'] == yesno then
			mw.getCurrentFrame():preprocess('<span style="border-bottom:2px dotted #fff;>' .. args['approximate'] or args['approx'] or args['a'] .. '</span>')
		end
		return callfn(s, m, useShort, useApproximate, useImage, noLink, imageInFront, alt)
	end
	return main, _main
end

-- Template:Coins access point
p.coins, p._coins = generateCurrencyFunc('coins', '%s*coins?')

-- Template:Gins access point
p.gins, p._gins = generateCurrencyFunc('gins', '%s*gins?')

-- Template:Bits access point
p.bits, p._bits = generateCurrencyFunc('bits', '%s*(skyblock)?bits?')

-- Template:Gems access point
p.gems, p._gems = generateCurrencyFunc('gems', '%s*(skyblock)?gems?')

-- Template:Pelts access point
p.pelts, p._pelts = generateCurrencyFunc('pelts', '%s*pelts?')

-- Template:Tokens access point
p.tokens, p._tokens = generateCurrencyFunc('tokens', '%s*tokens?')

-- Template:Bingo Points access point
p.bingoPoints, p._bingoPoints = generateCurrencyFunc('bingoPoints', '%s*bingo points?')

-- Template:North Stars access point
p.northStars, p._northStars = generateCurrencyFunc('northStars', '%s*north stars?')

-- Template:Copper access point
p.copper, p._copper = generateCurrencyFunc('copper', '%s*copper')

-- Template:Motes access point
p.motes, p._motes = generateCurrencyFunc('motes', '%s*motes?')

-- Template:Chocolate access point
p.chocolate, p._chocolate = generateCurrencyFunc('chocolate', '%s*chocolate?')

-- Template:Fossil Dust access point
p.fossilDust, p._fossilDust = generateCurrencyFunc('fossilDust', '%s*fossil dust?')

-- Template:Carnival Tokens access point
p.carnivalTokens, p._carnivalTokens = generateCurrencyFunc('carnivalTokens', '%s*carnival tokens?')

-- Template:Pests access point
p.pests, p._pests = generateCurrencyFunc('pests', '%s*pests?')

-- Template:Kernels access point
p.kernels, p._kernels = generateCurrencyFunc('kernels', '%s*kernels?')


----------------------------------------------------------------------------------------------------
-- Template:Coins to Dollars
--
-- Used to convert value in coins to US Dollars, based on Booster Cookie prices
----------------------------------------------------------------------------------------------------
function p.coins_to_dollars(frame)
	local args = getArgs(frame)
	local coins = args[1]
	local isFormatted = yesno(args['format'] or args['f'], true)
	
	return p._coins_to_dollars(coins, type)
end

function p._coins_to_dollars(coins, isFormatted)
	if isFormatted == nil then isFormatted = true end
	local cookiePriceCoins = bazaarData.products.BOOSTER_COOKIE.buy
	local cookiePriceGems = 325
	local cookiePriceDollars = 4.99 / 675 * cookiePriceGems
	local coinPriceDollars = cookiePriceCoins / cookiePriceDollars
	
	if not isFormatted then return coins / coinPriceDollars end
	local dollars = coins / coinPriceDollars
	dollars = dollars * 100
	dollars = math.floor(dollars)
	dollars = dollars / 100
	return '$' .. formatNum(dollars)
end

----------------------------------------------------------------------------------------------------
-- Template:Bits to Coins
--
-- Used to convert value in cbits to coins, based on prices across items with fairly stable prices and demand
----------------------------------------------------------------------------------------------------
function p.bits_to_coins(frame)
	local args = getArgs(frame)
	local bits = args[1]
	
	return p._bits_to_coins(bits)
end

function p._bits_to_coins(bits)
	local conversion = (bazaarData['products']['MAGMA_BUCKET']['buy']-bazaarData['products']['ENCHANTED_LAVA_BUCKET']['buy']*2)/3000
	local coins = bits * conversion
	return p._coins(coins, nil, true, true)
end
----------------------------------------------------------------------------------------------------
-- Template:Profit
--
-- Used to display a number as a profit or loss
----------------------------------------------------------------------------------------------------
function p.profit(frame)
	local args = getArgs(frame)
	local value = args[1]
	
	return p._profit(value)
end
function p._profit(value)
	value = toNumber(value)
	if value > 0 then
		value = formatNum(value);
		return colorMdl._colorTemplates('green', "+"..value)
	elseif value < 0 then
		value = formatNum(value);
		return colorMdl._colorTemplates('red', value)
	else
		return colorMdl._colorTemplates('grey', value)
	end
end

return p
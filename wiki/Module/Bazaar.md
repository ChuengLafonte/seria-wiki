-- <pre>
local getArgs = require('Module:Arguments').getArgs
local loader = require('Module:Loader')

local string, table, yesno, currency, color = loader.require('String', 'Table', 'Yesno', 'Currency', 'Color')
local bazaarData, aliases, i18n = loader.loadData('Bazaar/Data', 'Bazaar/Aliases', 'Bazaar/i18n')

local formatGins = currency._gins
local makeColor = color._colorTemplates
local _error = string.error

local p = {}

local priceTypeAliases = {
	buy = 'buy',
	b = 'buy',
	higher = 'buy',
	sell = 'sell',
	s = 'sell',
	lower = 'sell',
}

function p.getPriceTypeFromAlias(priceTypeAlias)
	return priceTypeAliases[priceTypeAlias]
end

-- Allows converting item name into productId

-- Allows normal minecraft names using aliases
function p._getProductId(productId)
	-- Allow 'Ench' shorthand - replaced with capital as it's needed encase alias isn't used
	if not productId:find('[Ee][Nn][Cc][Hh][Aa][Nn][Tt][Mm][Ee][Nn][Tt]') then
		productId = productId:gsub('[Ee][Nn][Cc][Hh][Aa]?[Nn]?[Tt]?[Ee]?[Dd]?', 'ENCHANTED')
	end
	return aliases[productId:lower()] or productId
end

function p._getProduct(productId)
	productId = p._getProductId(productId)
	return bazaarData['products'][productId];
end

function p._bazaarable(productId)
	return not not p._getProduct(productId)
end

local function shortenNum(num)
	if num == nil then return 0 end
	
	if num >= 10000 then
		return math.ceil(num) end
	if num >= 1000 then
		return math.ceil(num*10)/10 end
	if num >= 1 then
		return math.ceil(num*100)/100
	else
		return math.ceil(num*1000)/1000
	end
end

-- Invokes {{ToBazaarID}}
function p.getProductId(frame)
	local args = getArgs(frame)
	return p._getProductId(args[1])
end

-- Invokes {{BazaarLastUpdate}}
function p.getLastUpdatedDate()
	-- local args = getArgs(frame)
	local lang = mw.language.getContentLanguage()
	return lang:formatDate( 'd F Y, h:i a', '@' .. bazaarData['last_updated'], false ) .. ' UTC'
	-- return bazaarData['last_updated']
end

function p.lastUpdatedIcon()
	return string.makeTitle('ⓘ', 'Values updated every half hour from Hypixel\'s API. Last updated on: ' .. p.getLastUpdatedDate())
end

-- Invokes {{BazaarPurchaseCalc}}
function p.calcMaterialBuyPrices(frame)
	local args = getArgs(frame)
	local lang = mw.language.new('en')
	
	local price_type = args['type'] or args['t']
	local gins = yesno(args['gins'] or args['c'], true)
	local not_including = args['not_including']
	local noerror = args['noerror']
	
	-- first combine both methods of entering data into one list
	local stringstocalc = {}
	if string.find(args[1], '%*') == 1 then
		local splitwikilist = mw.text.split(string.sub(args[1], 2), '%s*%*%s*');
		for i, li in pairs(splitwikilist) do
			stringstocalc[#stringstocalc+1] = li
		end
	else
		for i = 1, table.xlength(args, false, true), 1 do
			stringstocalc[#stringstocalc+1] = args[i]
		end
	end
	
	-- parse the paramaters into usable values
	local items = {}
	for i, item in pairs(stringstocalc) do
		local numOrNil = tonumber(lang:parseFormattedNumber(item))
		if numOrNil then
			items[#items+1] = numOrNil
		else
			local num, name = mw.ustring.match(item, '([%d,%.]+)x? %[?%[?([^%[%]]+)%|?.*%]?%]?')
			if not num then
				-- also test for {{Slot}} format
				name, num = mw.ustring.match(item, '([^%[%]%,]+)%s*,%s*([%d]+)')
				if not num then
					return _error('Invalid item format: '..item)
				end
			end
			items[#items+1] = {name, tonumber(lang:parseFormattedNumber(num))}
		end
	end
	
	return p._calcMaterialBuyPrices(items, price_type, gins, not_including, noerror)
end

function p._calcMaterialBuyPrices(entries, price_type, gins, not_including, noerror) -- entries = [ [id,num] or num ]
	local total, abbr = 0, {}
	noerror = yesno(noerror, false)
	for i, entry in pairs(entries) do
		if tonumber(entry) then
			total = total + tonumber(entry)
		else
			local product = p._getProduct(entry[1]);
			if not product and not noerror then
				return _error('Invalid product ID %q', entry[1])
			elseif not product then
				break
			end
			
			local prodName = i18n[p._getProductId(entry[1])] or string._ucfirst(p._getProductId(entry[1])):gsub('_',' ')
			table.insert(abbr, ('%sx %s'):format(entry[2], prodName))
			-- default to buy, but allow 'sell' as an option
			price_type = p.getPriceTypeFromAlias(price_type) or 'buy'
			total = total + (product[price_type] * entry[2])
		end
	end
	not_including = not_including and (' (not including: %s)'):format(not_including) or ''
	if gins then
		local ret = tostring(formatGins(shortenNum(total)))
		local temp = ret:match('<.-font%-variant%-numeric.->(.-)</.->')
		if temp then temp = string.makeTitle(string.trim(temp), 'Materials used: &#10;'..table.concat(abbr, ', &#010;')) end
		ret = ret:gsub('<(.-)font%-variant%-numeric(.-)>.-</(.-)>',
			'<%1font-variant-numeric%2>'..(temp or ret)..'</%3>')
		return ret .. not_including
	end
	return total .. not_including
end

-- Invokes {{BazaarData}}
function p.getProductData(frame)
	local args = getArgs(frame)
	
	local productId = args[1]
	local datatype = string.lower(args[2] or 'buy')
	local long = yesno(args['long'], false)
	local gins = yesno(args['gins'], false)
	
	return p._getProductData(productId, datatype, long, gins)
end

function p._getProductData(productId, datatype, long, gins)
	
	local product = p._getProduct(productId);
	
	if not product then
		return _error('Invalid product ID %q', productId)
	end
	
	if datatype == 'buy' or datatype == 'sell' then
		local num = product[datatype]
		if not long then
			num = shortenNum(num)
		end
		if gins then
			num = formatGins(num)
		end
		return num
	end
	-- else datatype not valid
	return _error('Invalid data type')
end

-- Invokes {{BazaarPriceChange}} not
function p.getPriceChange(frame)
	local args = getArgs(frame)
	
	local productId = args[1]
	local datatype = string.lower(args[2] or 'buy')
	local format = yesno(args['format'] or args['f'], true)
	
	return p._getPriceChange(productId, datatype, format)
end

function p._getPriceChange(productId, datatype, format)
	
	local product = p._getProduct(productId);
	
	if not product then
		return _error('Invalid product ID', productId)
	end
	
	if datatype == 'buy' or datatype == 'sell' then
		local num = product[datatype] or 0
		local num_old = product.prev[1][datatype] or 0
		
		local ret_num = (num - num_old) / num_old
		-- Detect inf/nan
		if ret_num ~= ret_num or math.abs(ret_num) == math.huge then
			return table.concat{'<br>Not enough offers to calculate ', datatype == 'buy' and 'buy' or 'sell', ' price change'}
		end
		if format then
			local iconOnlyFormat = format == 'icononly'
			local function getText(icon, pNum)
				return iconOnlyFormat and string.makeTitle(icon, table.concat{ datatype == 'buy' and 'Buy Price Change: ' or 'Sell Price Change: ', pNum, '%' }) or table.concat{ icon, icon ~= '' and ' ' or '', pNum, '%' }
			end
			local shouldAddPlus = ret_num > 0
			ret_num = ret_num * 100
			ret_num = string.roundNumber(ret_num, 2)
			if ret_num >= 25 then
				return makeColor('dark green', getText('<b>⇑</b>', '+'..ret_num))
			elseif ret_num >= 5 then
				return makeColor('green', getText('<b>↑</b>', '+'..ret_num))
			elseif ret_num <= -25 then
				return makeColor('dark red', getText('<b>⇓</b>', ret_num))
			elseif ret_num <= -5 then
				return makeColor('red', getText('<b>↓</b>', ret_num))
			else
				return makeColor('gray', getText(iconOnlyFormat and '➖' or '', (shouldAddPlus and '+' or '')..ret_num))
			end
		end
	end
	-- else datatype not valid
	return _error('Invalid data type')
end

-- Invokes {{BazaarPriceSpread}} not
function p.getPriceSpread(frame)
	local args = getArgs(frame)
	
	local productId = args[1]
	local long = yesno(args.long or args.l, false)
	local gins = yesno(args.gins or args.gins or args.c, false)
	
	return p._getPriceSpread(productId, long, gins)
end

function p._getPriceSpread(productId, long, gins)
	
	local product = p._getProduct(productId);
	
	if not product then
		return _error('Invalid product ID %q', productId)
	end
	
	local buy = product.buy
	local sell = product.sell
	local spread = buy - sell
	spread = math.abs(spread)
	if not long then
		spread = shortenNum(spread)
	end
	if gins then
		spread = tostring(formatGins(spread))
	end
	return spread
end
 
return p
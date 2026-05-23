--<pre>--------------------------------------------------------------------------
-- This module houses helper functions for use on strings. In general this module
-- is loaded as the "string" variable in other modules for conistency.
-- Most string functions will accept a `table` or `number` besides a string
-- using `parseDualArg()`.
-- See the comments on the functions for futher details.
-- The `stringable` type repersents the types `string, `table`, and `number`.
--
----------------[ CONTENTS ]-----------------
-- * function: split(text: string, pattern: string, plain?: boolean)
-- * function: gsplit(text: string, pattern: string, plain?: boolean)
-- * function: matchNum(s: string, pattern: string, pos?: number|boolean, escape?: boolean)
-- * function: charAt(s: string, pos?: number)
-- * function: styleString(s, css, classes, attrs)
-- * function: escape(s: string)
-- * function: unescape(s: string)
-- * function: includes(s: string, pattern: string, pos?: number|boolean, escape?: boolean)
-- * function: codePointAt(s: string, pos?: number)
-- * function: concat(s: string, ...items: string)
-- * function: indexOf(s: string, searcher: string, pos?: string|boolean, escape?: boolean)
-- * function: lastIndexOf(s: string, searcher: string, pos?: string|boolean, escape?: boolean)
-- * function: endsWith(s: string, searcher: string, pos?: string)
-- * function: startsWith(s: string, searcher:string, pos?: string)
-- * function: matchAll(s: string, pattern: string, escape?: boolean)
-- * function: allMatched(s: string, t: table)
-- * function: anyMatched(s: string, t: table)
-- * function: gsubAll(s: string, ...)
-- * function: gsubMulti(s: string, replacements: table)
-- * function: orderedFormat(formatString: string, ...subsitutions)
-- * function: ucfirst(s: string)
-- * function: lcfirst(s: string)
-- * function: toCamelCase(s: string)
-- * function: bold(s: stringable)
-- * function: italic(s: stringable)
-- * function: underline(s: stringable)
-- * function: reverseSymbol(s: string, reverse?: boolean)
-- * function: pcall(f: function [function to call], ...params?: any [function parameters])
-- * function: makeImage(name: string | table, table, options: table)
-- * function: makeTitle(s: string, title: string [the title to make the element with], options: table)
-- * function: parseDualArg(arg: stringable [argument to parse])
-- * function: wrapLink(val: string, dest: string)
-- * function: parseUrlQuery(s: string | table [query to parse])
-- * function: isStringable(v: any [value to check])
-- * function: urlQueryToString(s: table [query table to parse], url?: string | table)
-- * function: getUrlParam(url: string | table, param: string, default: any)
-- * function: externalUrl(url: stringable, query: string | table, alt?: stringable)
-- * function: stringUtil(s: stringable)
-- * function: fullUrl(page: string, query: string | table, alt: string | table)
-- * function: _formatShortNumber(number: string|number)
-- * function: _toNumber(str: string)
-- * function: error(msg: string, ...<string.format() arguments>)
-- * function: preprocess(val: string)
-- * function: centerText(s: string)
-- * function: trimWhitespace(s: string)
-- * function: toRoman(s: string)
-- * function: toArabic(s: string)
-- * function: roundNumber(num: number, posistion: number)
-- * function: sublength(frame: table)
-- * function: matchTemplate(frame: table)
----------------[ TODO ]-----------------
-- *None yet.
---------------------------------------------------------------------------------
local p = {}

local getArgs = require('Module:Arguments').getArgs
local yesno = require('Module:Yesno')
local libU = require('Module:LibU')
local table = require('Module:Table')
local checkType, checkTypeLight, checkArgs, assertTrue, assertFalse, bind =
	libU.checkType, libU.checkTypeLight, libU.checkArgs, libU.assertTrue, libU.assertFalse, libU.bind

-- Load string library if the module is loaded as "string" in another module
p.rep = string.rep
p.gsub = string.gsub
p.len = string.len
p.sub = string.sub
p.char = string.char
p.gmatch = string.gmatch
p.lower = string.lower
p.upper = string.upper
p.find = string.find
p.match = string.match
p.reverse = string.reverse
p.byte = string.byte
p.format = string.format

---------------------------------------------------------------------------------
-- function: .split(text: string, pattern: string, plain?: boolean)
-- 
-- Breaks up the text according to the pattern specified. `plain` may be specified
-- to make the pattern be treated as raw text.
---------------------------------------------------------------------------------
function p.split(...)
	local text, pattern, plain = checkArgs({ 'string', 'string', { 'boolean', nilOk = true } }, ...)
	local ret = {}
	
	for m in p.gsplit(tostring(text), pattern, plain) do
		ret[#ret+1] = m
	end
	
	return ret
end

---------------------------------------------------------------------------------
-- function: .unpackedSplit(text: string, pattern: string, plain?: boolean)
-- 
-- Same as `.split()` execpt it returns an unpacked table instead of a regular one.
---------------------------------------------------------------------------------
function p.unpackedSplit(...)
	return unpack(p.split(checkArgs({ 'string', 'string', { 'boolean', nilOk = true } }, ...)))
end

---------------------------------------------------------------------------------
-- function: .gsplit(text: string, pattern: string, plain?: boolean)
-- 
-- Returns an iterator function which iterates over the indices of the split string.
---------------------------------------------------------------------------------
function p.gsplit(...)
	local text, pattern, plain = checkArgs({ 'string', 'string', { 'boolean', nilOk = true } }, ...)
	text = tostring(text)
	local s, l = 1, text:len()
	
	return function()
		if s then
			local e, n = text:find(pattern, s, plain)
			local ret
			if not e then
				ret = text:sub(s)
				s = nil
			elseif n < e then
				-- Empty separator!
				ret = text:sub(s, e)
				if e < l then
					s = e + 1
				else
					s = nil
				end
			else
				ret = e > s and text:sub(s, e-1) or ''
				s = n + 1
			end
			return ret
		end
	end
end
---------------------------------------------------------------------------------
-- function: .matchNum(s: string, pattern: string, pos?: number|boolean, escape?: boolean)
--
-- Gets the number of all matches in `s` from `pattern`.
-- If no matches are found, it returns -1.
---------------------------------------------------------------------------------
function p.matchNum(...)
	local s, pattern, pos, escape = checkArgs({
		'string', 'string', { 'number', 'boolean', nilOk = true }, { 'boolean', nilOk = true } 
	}, ...)
	
	local t = {}
	
	if type(pos) == 'boolean' then 
		escape = pos
		pos = nil
	end
	
	for match in s:gmatch(pattern) do
		table.insert(t, match)
	end
	
	return #t == 0 and -1 or #t
end
---------------------------------------------------------------------------------
-- function: .dedent(s: string, isSpaces?: boolean)
-- 
-- Removes uneeded indentation from `s`. Supports both spaces and Tabs.
---------------------------------------------------------------------------------
function p.dedent(s, isSpaces)
	checkTypeLight('dedent', 1, s, 'string')
	checkTypeLight('dedent', 2, isSpaces, 'boolean', true)
	
	s = s:gsub('^[ \n\r\v]*(.-)[ \n\r\v]*$', '%1'):gsub('\\([%a\"\'%d]+)', {
		['t'] = '\t',
		['n'] = '\n',
		['r'] = '\r',
		['v'] = '\v',
		['f'] = '\f',
		['a'] = '\a',
		['b'] = '\b',
		['"'] = '\"',
		['\''] = '\'',
	})
	local lines = mw.text.split(s, '\n')
	local overallLen = {}
	local isSpaces = true
	
	-- Check spaces
	for i, v in ipairs(lines) do
		local _, num = v:find('^\t+')
		if num then
			isSpaces = false
		end
	end
	
	for i, v in ipairs(lines) do
		local _, num
		
		if isSpaces then
			_, num = v:find('^ +')
		else
			_, num = v:find('^\t+')
		end
		num = isSpaces and num/4 or num
		table.insert(overallLen, #overallLen+1, num)
	end
	local overallLen = math.min(unpack(overallLen) or 0)
	
	for i, v in ipairs(lines) do
		lines[i] = v:gsub('^' .. (not isSpaces and ('\t'):rep(overallLen) or (' '):rep(overallLen*4)), '')
	end
	return table.concat(lines, '\n')
end

---------------------------------------------------------------------------------
-- function: remove(s: string, pattern: string|table, index?: number)
-- 
-- Removes the specified match from the string and returns it.
--------------------------------------------------------------------------------
function p.remove(...)
	local s, pattern, index = checkArgs({ 'string', { 'string', 'table' }, { 'number', nilOk = true } }, ...)
	local oldString = s
	local i, match = 1
	
	if type(pattern) == 'table' then
		while not match do
			if i > #pattern then
				match = {}
				break
			end
			match = oldString:match(pattern[i], index)
			
			if match then
				s = s:gsub(pattern[i], '', 1)
				match = { oldString:match(pattern[i], index) }
			end
			i = i+1
		end
	else
		match = { oldString:match(pattern, index) }
		s = s:gsub(pattern, '', 1)
	end
	
	return unpack{ s, unpack(match) }
end

---------------------------------------------------------------------------------
-- function: .charAt(s: string, pos?: number)
--
-- Returns the character `s` at the posistion of `pos`. `pos` will default to 1. 
-- `pos` maybe fed a negative number to count from the rear of `s`.
---------------------------------------------------------------------------------
function p.charAt(...)
	local s, pos = checkArgs({ 'string', { 'number', nilOk = true } }, ...)
	
	pos = pos and -(-pos) or 1
	if pos < 0 then
		pos = #s+pos
	elseif pos == 0 then 
		pos = 1
	end
	
	return (mw.ustring.isutf8(s) and mw.ustring or string).sub(s, pos, pos)
end

---------------------------------------------------------------------------------
-- function: .charAt(s: string, pos?: number)
--
-- Returns the character `s` at the posistion of `pos`. `pos` will default to 1. 
-- `pos` maybe fed a negative number to count from the rear of `s`.
---------------------------------------------------------------------------------
function p.charCodeAt(...)
	local s, pos, useHex = checkArgs({ 'string', { 'number', nilOk = true }, { 'boolean', nilOk = true } }, ...)
	s = p.charAt(s, pos)
	
	local ret = (mw.ustring.isutf8(s) and mw.ustring.codepoint or string.byte)(s) or -1
	
	return useHex and p.toHex(ret) or ret
end

---------------------------------------------------------------------------------
-- function: .toHex(num: number)
-- 
-- Converts a number to a hex number repersentation.
---------------------------------------------------------------------------------
function p.toHex(...)
	local num = checkArgs({ { 'number', 'string', base = 16 } }, ...)
	
	return string.format('%x', type(num) == 'string' and tonumber(num, 16) or num)
end

---------------------------------------------------------------------------------
-- function: .unicodeConvert(s: string)
-- 
-- Turns unicode encodings like `\u0F303`, `\u+0F303`, and `\u{FFFFF}` to actual characters.
---------------------------------------------------------------------------------
function p.unicodeConvert(...)
	local s = checkArgs('string', ...)
	
	function replUnicode(code)
		local success, res = pcall(mw.ustring.char, tonumber(code, 16))
		if not success then formattedError('The unicode codepoint "\\u{%x}" is out of range', 4, p.toHex(code)) end
		return res
	end
		
	return (s:gsub('\\u%+?(%x%x?%x?%x?)', replUnicode):gsub('\\u%{%+?(%x+)%}', replUnicode))
end

---------------------------------------------------------------------------------
-- function: .styleString(s, css, classes, attrs)
-- 
-- Styles text according to the css properties provided.
---------------------------------------------------------------------------------
function p.styleString(...)
	local s, css, classes, attrs = checkArgs({ { 'string', numberOk = true }, 'table', { 'table', nilOk = true }, { 'table', nilOk = true } }, ...)
	
	return p.wrapHtml(s, '<font>', table.merge({ style = css, class = classes }, attrs))
end

---------------------------------------------------------------------------------
-- function: .escape(s: string)
--
-- Escapes any special characters in `s` that are used in patterns.
---------------------------------------------------------------------------------
function p.escape(...)
	local s, skipPow = checkArgs({ 'string', { 'boolean', nilOk = true } }, ...)
	
	local pat = '([%*%+%-%(%)%[%]%%%$%^%?%.])'
	if skipPow then
		pat = pat:gsub('%%%^', '')
	end
	
	return (s:gsub(pat, function(m) return '%' .. m end))
end

---------------------------------------------------------------------------------
-- function: .unescape(s: string)
--
-- Unescapes any special characters in `s` that are used in patterns.
---------------------------------------------------------------------------------
function p.unescape(...)
	local s, skipPow = checkArgs({ 'string', { 'boolean', nilOk = true } }, ...)
	
	local pat = '(%%([%*%+%-%(%)%[%]%%%$%^%?%.]))'
	if skipPow then
		pat = pat:gsub('%%%^', '')
	end
	
	return (s:gsub(pat, '%2'))
end

---------------------------------------------------------------------------------
-- function: .includes(s: string, pattern: string, pos?: number|boolean, escape?: boolean)
--
-- Checks if `s` has `pattern` inside of it. `pos` can be set to where to start searching.
---------------------------------------------------------------------------------
function p.includes(...)
	local s, pattern, pos, escape = checkArgs({ 
		'string', 'string', { 'number', 'boolean', nilOk = true }, { 'boolean', nilOk = true } 
	}, ...)
	
	if type(pos) == 'boolean' then 
		escape = pos
		pos = nil
	end
	
	pos = pos or 1
	
	return not not s:match(escape and p.escape(pattern) or pattern, pos)
end

---------------------------------------------------------------------------------
-- function: .codePointAt(s: string, pos?: number)
--
-- Gets the codepoint for the character at `pos`.
---------------------------------------------------------------------------------
function p.codePointAt(...)
	local s, pos = checkArgs({ 'string', { 'number', nilOk = true } }, ...)
	
	local success, res = pcall(mw.ustring.isutf8(s) and mw.ustring.codepoint or string.byte, p.charAt(s, pos))
	
	if not success then
		error(res, 2)
	end
	
	return res
end

---------------------------------------------------------------------------------
-- function: .concat(s: string, ...items: string)
--
-- Appends each string to `s`.
---------------------------------------------------------------------------------
function p.concat(...)
	checkArgs({ 'string' }, ...)
	
	local ret = {}
	for i, v in forEachArgs({ 'any', startIndex = 1 }, ...) do
		v = tostring(v)
		table.push(ret, v)
	end
	
	return table.concat(ret)
end

---------------------------------------------------------------------------------
-- function: .indexOf(s: string, searcher: string, pos?: string|boolean, escape?: boolean)
--
-- Gets the index of the found string in `s` found by `searcher`.
---------------------------------------------------------------------------------
function p.indexOf(...)
	local s, searcher, pos, escape = checkArgs({ 
		{ 'string', numberOk = true }, 'string', { 'number', 'boolean', nilOk = true, }, { 'boolean', nilOk = true } 
	}, ...)
	
	if type(pos) == 'boolean' then 
		escape = pos
		pos = nil
	end
	
	pos = pos or 1
	local index, endsAt = s:find(searcher, pos, escape)
	
	return index or -1
end

---------------------------------------------------------------------------------
-- function: .lastIndexOf(s: string, searcher: string, pos?: string|boolean, escape?: boolean)
--
-- Gets the last index of the found string in `s` found by `searcher`.
---------------------------------------------------------------------------------
function p.lastIndexOf(...)
	local s, searcher, pos, escape = checkArgs({ 
		'string', 'string', { 'number', 'boolean', nilOk = true }, { 'boolean', nilOk = true } 
	}, ...)
	
	local index = p.indexOf(s:reverse(), searcher, pos and -pos-1, escape)
	
	if index ~= -1 then
		return -(index-#s)
	else
		return index
	end
end

---------------------------------------------------------------------------------
-- function: .endsWith(s: string, searcher: string, pos?: string)
--
-- Checks if `s` ends with `searcher`. Begins searching at `pos` in `s`.
---------------------------------------------------------------------------------
function p.endsWith(...)
	local s, searcher, pos = checkArgs({ 'string', 'string', { 'number', nilOk = true } }, ...)
	
	return not not s:match(p.escape(searcher) .. '$', pos)
end

---------------------------------------------------------------------------------
-- function: .startsWith(s: string, searcher: string, pos?: string)
--
-- Checks if `s` starts with `searcher`. Begins searching at `pos` in `s`.
---------------------------------------------------------------------------------
function p.startsWith(...)
	local s, searcher, pos = checkArgs({ 'string', 'string', { 'number', nilOk = true } }, ...)
	
	return not not s:match('^' .. p.escape(searcher), pos)
end

---------------------------------------------------------------------------------
-- function: .matchAll(s: string, pattern: string, escape?: boolean)
--
-- Gets all matches of `s` with `string.gmatch()` with `pattern` as the matcher.
---------------------------------------------------------------------------------
function p.matchAll(...)
	local s, pattern, escape = checkArgs({ 'string', 'string',{ 'boolean', nilOk = true } }, ...)
	
	pattern = escape and p.escape(pattern) or pattern
	
	local ret
	local n = p.matchNum(s, pattern, escape)
	local mt = {}
	
	local function log()
		return mw.logObject(ret) or ret	
	end
	
	ret = setmetatable({ n = n, origPattern = pattern, input = s }, {
		__index = {
			print = log,
			log = log,
			dump = function()
				return mw.dumpObject(ret)
			end,
		}
	})
	
	local function callMatcher(f, i)
		return (function(...)
			local t = { ... }
			t.index = i
			t.n = table.pack(...).n
			
			return t
		end)(f())
	end
	
	local matcher = s:gmatch(escape and p.escape(pattern) or pattern)
	
	for i = 1, n do
		local res = callMatcher(matcher, i)
		table.insert(ret, res)
	end
	
	return ret
end

---------------------------------------------------------------------------------
-- function: allMatched(s: string, t: table)
-- 
-- Attempt to match each pattern in the table/subsequent args,
-- then return true if all matches exists
---------------------------------------------------------------------------------
function p.allMatched(s, ...)
	checkType('allMatched', 1, s, 'string')
	
	local t = { ... }
	if type(t[1]) == 'table' then
		t = t[1]
	end
	
	for _, v in ipairs(t) do
		if not(s:match(v)) then
			return false
		end
	end
	
	return true
end

---------------------------------------------------------------------------------
-- function: anyMatched(s: string, t: table)
-- 
-- Attempt to match each pattern in the table/subsequent args,
-- returns true if any match exists
---------------------------------------------------------------------------------
function p.anyMatched(s, ...)
	checkType('anyMatched', 1, s, 'string')
	
	local t = { ... }
	if t[1] == 'table' then
		t = t[1]
	end
	
	for _, v in ipairs(t) do
		if s:match(v) then
			return true
		end
	end
	
	return false
end

---------------------------------------------------------------------------------
-- function: gsubAll(s: string, ...)
-- 
-- For each pair of values in subsequent args, get pattern and replacement string
-- Apply all replacements on a string
---------------------------------------------------------------------------------
function p.gsubAll(s, ...)
	checkType('gsubAll', 1, s, 'string')
	
	local t, i = { ... }, 1
	if t[1] == 'table' then
		t = t[1]
	end
	t = table.flat(t)
	if #t % 2 ~= 0 then
		error('[gsubAll] Pattern/Replacement pairs mismatch (Odd number arguments)')
	end
	while i * 2 <= #t do
		s = s:gsub(t[i*2-1], t[i*2])
		i = i + 1
	end
	
	return s
end

---------------------------------------------------------------------------------
-- function: gsubMulti(s: string, replacements: table)
-- 
-- Takes multiple patterns and replacements in a table and calls `:gsub()` on `s`.
---------------------------------------------------------------------------------
function p.gsubMulti(...)
	local s, replacements = checkArgs({ 'string', 'table', { 'number', nilOk = true } }, ...)
	
	for search, repl in pairs(replacements) do
		s = s:gsub(search, type(search) == 'number' and '' or repl)	
	end
	
	return s
end

---------------------------------------------------------------------------------
-- function: .orderedFormat(formatString: string, ...subsitutions)
-- 
-- Works like `string.format()`, execpt the formatters work with ordered arguments.
-- Directives are exactly the same as `string.format()`.
---------------------------------------------------------------------------------
function p.orderedFormat(...)
	local s = checkArgs({ 'string' }, ...)
	
	local subsitutions = table.tableUtil()
	local nArgs = select('#', ...)
	local match = p.matchAll('\127' .. s, '[^%%]?%%([%d%.%#+%-]*)(%w-)(%d)%{?([^}]+)%}?')
	local args = { ... }
	local values = args
	
	if ('\127' .. s .. '\127'):gsub('%%%%', '%%%%' .. '\127'):match('[^%%]%%[^%d%w%%]') then
		formattedError('options must be escaped or be followed by an option or argument number (at string posistion #%s)', 2, ('\127' .. s .. '\127'):find('[^%%]?%%[^%d%w]'))
	elseif (s .. '\127'):gsub('%%%%', '%%%%' .. '\127'):match('%%[%a[^%d]]+') then
		formattedError('options must have a argument to subsitute from (at string posistion #%s)', 2, (s .. '\127'):find('[^%%]?%%%a+[^%d]'))
	end
	
	local optionTypes = {
		['c'] = 'number',
		['d'] = 'number',
		['i'] = 'number',
		['o'] = 'number',
		['x'] = 'number',
		['X'] = 'number',
		['e'] = 'number',
		['E'] = 'number',
		['f'] = 'number',
		['g'] = 'number',
		['G'] = 'number',
		['u'] = 'number',
		['un'] = 'number',
		['q'] = 'string',
		['s'] = 'string',
		['l'] = 'string',
		['uc'] = 'string',
		['tm'] = 'string',
		['tg'] = 'string',
		['t'] = 'table',
	}
	
	local customOptions = {
		['t'] = p.parseDualArg,
		['l'] = string.lower,
		['uc'] = string.upper,
		['tm'] = p.trim,
		['tg'] = function(value, ...)
			return p.wrapTag(value, {...})
		end,
		['un'] = function(value)
			return p.unicodeConvert('\\u{' .. -(-value) .. '}')
		end,
	}
	
	local optionsTemp = {}
	
	-- Find the greatest index first and check for bad indexes
	local greatestIndex = 0
	for i, v in ipairs(match) do
		local new = - -v[3]
		
		if greatestIndex+1 < new then
			formattedError('options must be sequential (at option #%s)', i, new)
		end
		
		if greatestIndex < new then
			greatestIndex = new
		end
	end
	
	-- Check the types of arguments, error if one is missing or is an invalid type
	for i = 1, #match do
		local index = - -match[i][3]
		local option = match[i][2]
		
		if match[i] ~= nil then
			local arg = args[i+1]
			
			if not optionTypes[option] and option ~= '' then formattedError('invalid option formatting "%%%s"', 2, option) end
			if optionsTemp[index] and optionsTemp[index] ~= option then formattedError('options may not have conflicting types (at option #%s)', 2, index) end
			optionsTemp[index] = option
			
			if i > nArgs-1 then
				checkType('no value', i+1, { optionTypes[option] or 'string' })
			end	
		end
	end
	
	for i = 1, match.n do
		if match[i] ~= nil then
			local index = match[i][3]
			local value = args[index+1]
			
			checkType(- -index+1, value, { optionTypes[match[i][2]] or 'string', numberOk = true })
			
			subsitutions:push(value)
		end
	end	
	
	local count = 0
	local s, _ = (string.gsub('\127' .. s, '([^%%]?)%%([%d%.%#+%-]*)(%w-)(%d)%{?([^{}]+)%}?', function(before, modifier, option, number, options)
			count = count+1
			if customOptions[option] then
				local t = p.split(options:gsub('\\,', '\255'), '%s*,%s*')
				local success, res 
				
				for i = 1, #t do
					t[i] = t[i]:gsub('\255', ',')
				end
				
				if t[1] == '{' and #t == 1 then
					success, res = pcall(customOptions[option], values[count+1])
				else
					success, res = pcall(customOptions[option], values[count+1], unpack(t))
				end
				
				assertTrue(success, res, 4)
				return before .. res
			else
				return before .. '%' .. modifier .. (option ~= '' and option or 's') .. '\127'
			end
		end)):gsub('\127', '')

	return s:format(unpack(subsitutions))
end

---------------------------------------------------------------------------------
-- function: parseTextList(s, phrase): table
-- 
-- Parses a text list into a table.
---------------------------------------------------------------------------------
function p.parseTextList(s, phrase, removeTrailing)
	checkType('parseTextList', 1, s, 'string')
	checkType('parseTextList', 2, phrase, 'string')
	checkType('parseTextList', 3, includeTrailing, 'boolean', true)
	
	phrase = p.trim(phrase)
	removeTrailing = removeTrailing ~= false
	s = p.trim(s):gsub('^%s*' .. phrase .. '%s*', '')
	
	if removeTrailing then
		s = s:gsub('%s*' .. phrase .. '%s*$', '')
	end
	
	local t = p.split(s, '%s*' .. p.escape(phrase) .. '+%s*')
	
	return t
end

---------------------------------------------------------------------------------
-- function: parserTag(tagName: string, t?: table)
-- 
-- 
---------------------------------------------------------------------------------
function p.parserTag(tagName, t)
	checkType('parserTag', 1, tagName, 'string')
	checkType('parserTag', 2, t, 'table', true)
	
	local buffer = {'{{#', tagName, ':'}
	
	if t then
		table.push(buffer, '\n')
		for key, val in pairs(t) do
			local isNum = tonumber(key)
			if type(val) == 'table' then
				for _, value in ipairs(val) do
					table.push(buffer, '| ', key, ' = ', value, '\n')
				end
			else
				table.push(buffer, '| ', key, ' = ', val, '\n')
			end
		end
	end
	
	table.insert(buffer, '}}')
	
	return table.concat(buffer)
end

---------------------------------------------------------------------------------
-- function: .ucfirst(s: string)
---------------------------------------------------------------------------------
function p._ucfirst(s)
	checkTypeLight('ucfirst', 1, s, 'string')
	
	if s == nil then s = '' end
	return s:gsub('(%w)([%w\']*)', function(a, b) return string.upper(a) .. string.lower(b) end)
end
---------------------------------------------------------------------------------
-- function: .lcfirst(s: string)
---------------------------------------------------------------------------------
function p._lcfirst(s)
	checkTypeLight('lcfirst', 1, s, 'string')
	if s == nil then s = '' end
	return s:gsub('(%w)([%w\']*)', function(a, b) return string.lower(a) .. string.lower(b) end)
end
p.lcfirst = p._lcfirst
p.ucfirst = p._ucfirst

--------------------------------------------------------------------------------
-- function: .toCamelCase(s: string)
--
-- converts a string to camel case
--------------------------------------------------------------------------------
function p.toCamelCase(s)
	checkTypeLight('toCamelCase', 1, s, 'string')
	
	return s
		:gsub('(%w)(%w*)', 
			function(a, b) 
				return table.concat{ 
					a:upper(), 
					b,
				} 
			end
		)
		:gsub('[^%a]+', '')
		:gsub('^(%w)(%w*)', 
			function(a, b) 
				return table.concat{ 
					a:lower(), 
					b,
				} 
			end
		)
end
---------------------------------------------------------------------------------
-- function: .bold(s: stringable)
--
-- Makes bold text
---------------------------------------------------------------------------------
function p.bold(s)
	return table.concat{ '<b>', p.parseDualArg(s), '</b>' }
end

---------------------------------------------------------------------------------
-- function: .italic(s: stringable)
--
-- Makes italic text
---------------------------------------------------------------------------------
function p.italic(s)
	return table.concat{ '<i>', p.parseDualArg(s), '</i>' }
end

---------------------------------------------------------------------------------
-- function: .underline(s: stringable)
--
-- Makes underlined text
---------------------------------------------------------------------------------
function p.underline(s)
	return table.concat{ '<u>', p.parseDualArg(s), '</u>' }
end

---------------------------------------------------------------------------------
-- function: .reverseSymbol(s: string, reverse?: boolean)
--
-- Reverses the symbols in a given string
---------------------------------------------------------------------------------
function p.reverseSymbol(s, reverse)
	if type(s) ~= 'string' then error(string.format('bad argument #1 to \"reverseSymbol\": string expected, got %s', type(s)), 2) end
	local replacementSymbols = {
		['['] = ']',
		[']'] = '[',
		['('] = ')',
		[')'] = '(',
		['{'] = '}',
		['}'] = '{',
		['<'] = '>',
		['>'] = '<',
		['/'] = '\\',
		['\\'] = '/',
	}
	local s = string.gsub(s, '([%[%]{}%(%)<>\\/])', replacementSymbols)
	
	if yesno(reverse, false) then
		return s:reverse()
		else return s
	end
end

---------------------------------------------------------------------------
-- function: .makeImage(name: string | table, table, options: table)
-- 
-- Creates a wikitext image element. You can specify the file extention by adding 
-- `.<extension>` at the end of the file name.
--
------------[ OPTIONS ]----------
-- Specify one of these fields below in the `options` argument to configure the 
-- output of this function.
-- 
-- *size: ? - 
-- *extension: ? - 
-- *vertAlign: ? - 
-- *horizAlign: ? - 
-- *link: ? - 
-- *alt: ? - 
-- *page: ? - 
-- *class: ? - 
-- *noLink: ? - 
-- *format: ? - 
-- *caption: ? - 
-- *lang: ? - 
-- *upright: ? - 
---------------------------------------------------------------------------
function p.makeImage(name, options)
	checkTypeLight('makeImage', 1, name, {'string', 'table'})
	checkTypeLight('makeImage', 2, options, 'table', true)
	
	name = p.parseDualArg(name)
	options = options or {}
	
	local size, extension, vertAlign, horizAlign = unpack{
			options.size or options.s or 21,
			options.extension or options.ext or options.e or 'png',
			options.vertalign or options.vertical_align or options.vAlign or options.v_align or options.vl,
			options.horizalign or options.horizontal_align or options.hAlign or options.h_align or options.hl,
		}
		
	local link = options.link or options.l
	local alt = options.alt or options.a
	local page = options.page or options.p
	local class = options.class or options.cl
	local noLink = options.nolink or options.nl
	local format = options.format or options.form or options.f
	local caption = options.caption or options.cap or options.c
	local lang = options.langauge or options.lang or options.lan
	local upright = options.upright or options.ur
	
	vertAlign = vertAlign and vertAlign:lower()
	horizAlign = horizAlign and horizAlign:lower()
	format = format and format:lower()
	
	local hl_aliases = {
		['l'] = 'left',
		['le'] = 'left',
		['lef'] = 'left',
		['left'] = 'left',
		
		['r'] = 'right',
		['ri'] = 'right',
		['rig'] = 'right',
		['righ'] = 'right',
		['right'] = 'right',
		
		['c'] = 'center',
		['ce'] = 'center',
		['cen'] = 'center',
		['cent'] = 'center',
		['cente'] = 'center',
		['center'] = 'center',
		['cnt'] = 'center',
		['cntr'] = 'center',
		['centr'] = 'center',
		['cnter'] = 'center',
		['ct'] = 'center',
		
		['n'] = 'none',
		['no'] = 'none',
		['non'] = 'none',
		['none'] = 'none',
	}
	
	local vl_aliases = {
		['bl'] = 'baseline',
		['basel'] = 'baseline',
		['baselin'] = 'baseline',
		['bline'] = 'baseline',
		['baseline'] = 'baseline',
		['baslin'] = 'baseline',
		['baseli'] = 'baseline',
		
		['s'] = 'sub',
		['su'] = 'sub',
		['sub'] = 'sub',
		
		['sup'] = 'super',
		['supr'] = 'super',
		['sper'] = 'super',
		['spr'] = 'super',
		['super'] = 'super',
		
		['t'] = 'top',
		['to'] = 'top',
		['top'] = 'top',
		
		['tt'] = 'text-top',
		['t-t'] = 'text-top',
		['txt-tp'] = 'text-top',
		['text-top'] = 'text-top',
		['texttop'] = 'text-top',
		['txttp'] = 'text-top',
		['text-tp'] = 'text-top',
		
		['m'] = 'middle',
		['md'] = 'middle',
		['mid'] = 'middle',
		['midle'] = 'middle',
		['mdle'] = 'middle',
		['middle'] = 'middle',
		['midway'] = 'middle',
		
		['b'] = 'bottom',
		['bottom'] = 'bottom',
		['bt'] = 'bottom',
		['btm'] = 'bottom',
		['bot'] = 'bottom',
		['botom'] = 'bottom',
		
		['tb'] = 'text-bottom',
		['t-b'] = 'text-bottom',
		['txt-bt'] = 'text-bottom',
		['text-bot'] = 'text-bottom',
		['text-botom'] = 'text-bottom',
		['txt-bottom'] = 'text-bottom',
		['text-bottom'] = 'text-bottom',
	}
	
	local format_aliases = {
		['t'] = 'thumb',
		['tn'] = 'thumb',
		['thmb'] = 'thumb',
		['thumb'] = 'thumb',
		['thumbnail'] = 'thumb',
		['tmb'] = 'thumb',
		['tmbnl'] = 'thumb',
		
		['fl'] = 'frameless',
		['frmlss'] = 'frameless',
		['frameless'] = 'frameless',
		['fless'] = 'frameless',
		['framel'] = 'frameless',
		['frmless'] = 'frameless',
		['framelss'] = 'frameless',
		
		['f'] = 'frame',
		['fr'] = 'frame',
		['fra'] = 'frame',
		['fram'] = 'frame',
		['frame'] = 'frame',
		['frm'] = 'frame',
		['frme'] = 'frame',
		
		['b'] = 'border',
		['bo'] = 'border',
		['br'] = 'border',
		['bdr'] = 'border',
		['bord'] = 'border',
		['border'] = 'border',
		['bordr'] = 'border',
	}
	
	local vertAlign, horizAlign, format = vl_aliases[vertAlign], hl_aliases[horizAlign], format_aliases[format]
	
	if name:match('^(.*)%.(%a+)$') then
		name, extension = name:match('^(.*)%.(%a+)$')
	end
	
	local tpSize = type(size)
	local size = 
		(tpSize == 'number' or (tpSize == 'string' and size:match('^%d-(px)$')))
			and table.concat{ tonumber((tostring(size):gsub('px', ''))), 'px' }
		or (tpSize == 'table' and #size ~= 0)
			and table.concat{ tonumber(size[1]), 'x', tonumber(size[2]), 'px' }
		or size
	
	return table.concat{
		'[[File:',
		-- Filename
		name,
		'.',
		-- Extension
		extension,
		-- File format
		format and '|' or '',
		format or '',
		-- Vertical Alignment
		vertAlign and '|' or '',
		vertAlign or '',
		-- Horizontal Alignment
		horizAlign and '|' or '',
		horizAlign or '',
		-- Size
		'|',
		size,
		-- Link/No Link
		(noLink 
			and '|link=' 
			or table.concat{
				link and '|link=' or '',
				link or '',
			}
		),
		-- Class
		class and '|class=' or '',
		p.parseDualArg(class or ''),
		-- Alt
		alt and '|alt=' or '',
		p.parseDualArg(alt or ''),
		-- Page number
		tonumber(page) and '|page=' or '',
		tonumber(page) and page or '',
		-- Langauge
		lang and '|lang=' or '',
		lang or '',
		-- Upright
		(yesno(upright)
			and '|upright'
		or tonumber(upright)
			and table.concat{ '|upright=', tonumber(upright) }
		or upright == ''
			and '|upright='
		or ''
		),
		-- Caption
		caption and '|' or '',
		caption or '',
		-- Finish
		']]',
	}
end

---------------------------------------------------------------------------
-- function: .makeTitle(s: string, title: string [the title to make the element with], options: table)
--
-- Returns a html `<abbr>` element with `s` as its inner text and `title` as
-- its `title` attribute.
--
-----------[ OPTIONS ]----------
-- Specify one of the fields below in the `options` argument
-- to configure the output of this function.
---------------------------------------------------------------------------
function p.makeTitle(s, title, options)
	checkTypeLight('makeTitle', 1, s, {'string', 'table', 'number'})
	checkTypeLight('makeTitle', 2, title, {'string', 'table', 'number', 'nil'})
	checkTypeLight('makeTitle', 3, options, {'table', 'nil'})
	
	local options = options or {}
	
	local disableAbbr, ignoreTitleNil = unpack{
		options.disableAbbr or options.noAbbr,
		options.ignoreTitleNil or options.ignoreTitle or options.ignTitle
	}
	if ignoreTitleNil and not title then return s end
	parsedTip = p.parseDualArg(title)
	return p.wrapHtml(s, disableAbbr and '<span>' or '<abbr>', { title = parsedTip, tabIndex=0 })
end

---------------------------------------------------------------------------
-- function: .parseDualArg(arg: stringable [argument to parse])
-- 
-- Parses the argument to a string if it is a table using `table.concat()`
-- and the `sep` field if the table has one. Else, it returns the argument.
-- If `arg` is a number, it converts it a string.
---------------------------------------------------------------------------
function p.parseDualArg(arg)
	if arg == nil then return end
	checkType('parseDualArg', 1, arg, {'string', 'table', 'number'})
	
	if type(arg) == 'number' then arg = tostring(arg) end
	
	return type(arg) == 'table' and table.concat(arg, arg.sep or arg.s or '') or arg
end
p.makeHover = p.makeTitle

---------------------------------------------------------------------------
-- function: .wrapLink(val: string, dest: string)
--
-- Makes a wikitext link
---------------------------------------------------------------------------
function p.wrapLink(page, displayText)
	checkType('wrapLink', 1, page, {'string', 'table' }, true)
	checkType('wrapLink', 2, displayText, {'string', 'table' }, true)
	
	if not page or page == '' then return '' end
	
	local page = p.parseDualArg(page)
	local displayText = p.parseDualArg(displayText)
	
	return table.concat{
		'[[',
		page, 
		displayText and '|' or '', 
		displayText and displayText or '', 
		']]'
	}
end
p.makeLink = p.wrapLink
---------------------------------------------------------------------------
-- function: .parseUrlQuery(s: string | table [query to parse])
--
-- Parses a url query string into a table in the following format: a format where the parameter name is 
-- the field, and the value of that field the parameter.
---------------------------------------------------------------------------
function p.parseUrlQuery(s)
	local s = p.isStringable(s) and p.parseDualArg(s) or ''
	
	if type(query) == 'table' then return setmetatable(mt, s) end
	
	s = p.parseDualArg(s):gsub('^[%?&]+', ''):gsub(' ', '+')
	-- Remove preceding unesscessary params
	if s:match('^(https?:%/%/%S-)(%?.-=.+)$') then
		url, s = s:match('^(https?:%/%/%S-)(%?.*)$') 
		s = p.parseDualArg(s):gsub('^[%?&]+', ''):gsub(' ', '+')
		
	elseif not s:match('^(%w-)=(.*)$') and not s:match('^(https?:%/%/%S-)(%?.*)$') then
		error(string.format('Syntax error in parsing URL query: invalid URL query %q', s), 2)
	end
	local tmp = {}
	
	if s == '' then 
		error('Syntax error in parsing URL query: query is empty', 2)
	end
	
	-- Detect errors
	if s:match('%&$') then
		error('Syntax error in parsing URL query: trailing \"&\" found in input', 2)
	end
	
	local proto = {}
	
	-- Metatable methods
	function proto:extend(t, k)
		checkType('extend', 1, t, { 'table', 'string' })
		
		if type(t) == 'table' and k == nil then
			for key, v in pairs(t) do
				tmp[key] = v
			end
		else
			tmp[t] = k
		end
		
		return tmp, url
	end
	
	function proto:tostring(addUrl)
		ret = p.urlQueryToString(tmp, addUrl and url or nil)
		
		if not addUrl then
			return ret, url
		else
			return ret
		end
	end
	
	function proto:getParam(k)
		checkType('getParam', 1, k, {'string', 'number', 'function', 'boolean', 'table'})
		
		if type(k) == 'table' then
			local ret = {}
			for i, v in ipairs(k) do
				-- customFieldError(tmp[v] == nil, i, 1, 'getParam', 'attempted to get a non-existent query parameter %q', v)
				ret[v] = tmp[v]
			end
			return ret, url
		else
			assertTrue(tmp[k] ~= nil, 'bad argument #1 to getParam (attempted to get a non-existent query parameter %s)', 1, k)
			return tmp[k], url
		end
	end
	
	function proto:setUrl(s, isInternal)
		checkType('setUrl', 1, s, 'string')
		
		url = isInternal and tostring(mw.uri.fullUrl(s)) or s
		return tmp, url
	end
	
	function proto:setFragment(s)
		checkType('setFragment', 1, s, 'string')
		
		proto.fragment = s
		url = table.concat{ url, '#', mw.uri.anchorEncode(mw.uri.anchorDecode(s)) }
		
		return tmp, url
	end
	
	local mt = { 
		__index = function(t, k) 
			return proto[k]
		end, 
	}
	
	-- Check if the url query is only 1 param long
	if s:match('^(%w-)=([^&]*)$') then
		param, value = s:match('^%??(%w-)=(.*)$')
		tmp[param] = value
	
	-- Else use multiple method
	elseif #p.split(s, '&') > 1 then
		s = p.split(s, '&')
		
		for i = 1, #s, 1 do
			local param, value = s[i]:match('^(%w-)=(.*)$')
			
			-- Detect if param is empty
			if param == '' or not param then
				error('Syntax error in parsing URL query at index #' .. i .. ': url parameter name expected', 2)
			end
			
			value = type(value) ~= 'nil' and value or ''
			value = type(value) == 'string' and mw.uri.encode(mw.uri.decode(value)) or value
			
			tmp[param] = value
		end
	end
	
	setmetatable(tmp, mt)
	
	-- Return
	return tmp, url
end

---------------------------------------------------------------------------
-- function: .isStringable(v: any [value to check])
--
-- Checks if the value if the value is able to be turned into a string 
-- through any method with its data intact.
---------------------------------------------------------------------------
function p.isStringable(v)
	local vType = type(v)
	if vType == 'string' or (vType == 'table' and #v ~= 0 and v[1]) or vType == 'number' then
		return true
	else
		return false
	end
end

---------------------------------------------------------------------------
-- function: .urlQueryToString(s: table [query table to parse], url?: string | table)
--
-- Parses a query table in the following format into a string, where the following 
-- format can be: a format where the parameter name is the field, and the value 
-- of that field the parameter.
---------------------------------------------------------------------------
function p.urlQueryToString(t, url)
	-- Exit if the string is a query in string format
	if type(t) == 'string' and t:match('^[%?&]+(.-)=(.*)$') then
		return t
	end
	
	checkType('urlQueryToString', 1, t, { 'table' })
	
	-- Variables
	local ret, j = {}, 0
	
	for k, v in pairs(t) do
		j = j + 1
		v = mw.uri.encode(mw.uri.decode(p.isStringable(v) and p.parseDualArg(v) or ''))
		
		if j == 1 then
			ret[#ret+1] = table.concat{ '?', k, '=', v }
		else
			ret[#ret+1] = table.concat{ '&', k, '=', v }
		end
	end
	
	-- Return
	return table.concat{ p.parseDualArg(url or ''), table.concat(ret, '') }
end

--------------------------------------------------------------------------
-- function: .getUrlParam(url: string | table, param: string, default: any)
-- 
-- gets a url query parameter from a string
---------------------------------------------------------------------------
function p.getUrlParam(url, param, default)
	checkType('getUrlParam', 1, url, { 'string', 'table' })
	checkType('getUrlParam', 2, param, { 'string' })
	
	local query, url = p.parseUrlQuery(url)
	
	return query[param] ~= nil and query[param] or default
end

--------------------------------------------------------------------------
-- function: .externalUrl(url: stringable, query: string | table, alt?: stringable)
-- 
-- Makes a external link with an optional query and alternate text
---------------------------------------------------------------------------
function p.externalUrl(url, query, alt, fragment)
	checkType('externalUrl', 1, url, { 'string', 'table' })
	checkType('externalUrl', 2, query, { 'string', 'table', 'nil' })
	checkType('externalUrl', 3, alt, { 'string', 'table', 'nil' })
	checkType('externalUrl', 4, alt, { 'string', 'table', 'nil' })
	
	local url = p.parseDualArg(url)
	
	query = type(query) == 'string' and p.parseUrlQuery(query) or query
	query = p.urlQueryToString(query or {})
	fragment = p.parseDualArg(fragment)
	
	if not url:match('^https?:%/%/') then
		url = table.concat{ 'https://', url }
	end
	
	return p.wrapHtml{
		{
			alt and '[' or '',
			url:gsub(' ', '_'),
			query or '',
			alt and ' ' or '',
			alt and alt or '',
			alt and ']' or '',
		},
		'<span>',
		{ class = 'plainlinks' },
	}
end

function p._externalUrl(frame)
	local args = getArgs(frame)
	
	local url, alt, fragment = args[1], args[2], args[3]
	local query = {}
	
	for k, v in pairs(args) do
		if type(k) == 'table' then
			query[k] = v
		end
	end
	
	return p.pcall(p.externalUrl, url, query, alt, fragment)
end

---------------------------------------------------------------------------
-- function: .fullUrl(page: string, query: string | table, alt: string | table)
--
-- Makes a full url
---------------------------------------------------------------------------
function p.fullUrl(page, query, alt, fragment)
	if not page then page = '2034890239833333' end
	
	if page == true and type(query) == 'table' then
		page, query, alt, fragment = unpack{
			query.page or query.p or query[1],
			query.query or query.quer or query.q or query[2],
			query.alt or query.a or query[3],
			query.fragment or query.frag or query.f or query[4],
		}
	end
	
	checkType('fullUrl', 1, page, { 'string', 'table' })
	checkType('fullUrl', 2, query, { 'string', 'table', 'nil' })
	checkType('fullUrl', 3, alt, { 'string', 'table', 'nil' })
	
	local page = p.parseDualArg(page)
	query = type(query) == 'string' and p.parseUrlQuery(query) or query
	query = type(query) == 'table' and p.urlQueryToString(query) or query
	
	return table.concat{
		alt and '[' or '',
		tostring(mw.uri.fullUrl(page:gsub(' ', '_'), query)):gsub('2034890239833333', ''),
		(fragment and fragment ~= '') and '#' or '',
		(fragment and fragment ~= '') and p.parseDualArg(fragment) or '',
		alt and ' ' or '',
		alt and (p.parseDualArg(alt)) or '',
		alt and ']' or '',
	}
end

function p._fullUrl(frame)
	local query = {}
	local args = getArgs(frame)
	
	for arg, value in pairs(args) do
		if type(arg) == 'string' then
			query[arg] = value
		end
	end
	
	return p.pcall(p.fullUrl, args[1], query, args[2], args[3])
end
---------------------------------------------------------------------------
-- Template:Repeat
-- 
-- Repeats the given string a specified number of times
---------------------------------------------------------------------------
function p.repeatF(frame)
	local args = getArgs(frame, {removeBlanks = false, trim = false })
	local s = args[1] or ''
	local num = p.trim(args[2]) or 1
	local sep = p.trim(args[3])
	
	assertFalse(num:match('[^%d%-%+]+'), 'number expected, got %q', 2, num)
	assertFalse(0 >= tonumber(num), 'repeat delimiter must be greater than 0, got %q', 2, num)
	
	return p._repeat(s, num, sep, yesno(p.trim(args[4]), false))
end
---------------------------------------------------------------------------
-- Template:Repeat Module Access Point
---------------------------------------------------------------------------
function p._repeat(s, num, sep, isRoman)
	checkTypeLight('_repeat', 1, s, { 'string', 'number', 'table' })
	assertTrue(tonumber(num), 'argument #2 is not convertable to a number', 2)
	checkTypeLight('_repeat', 3, sep, { 'string', 'number', 'table' }, true)
	
	local num = tonumber(num) or 1
	local start = tonumber(sep) or 1
	
	assertTrue(num < 0 or num < 1e308, 'number out of range', 2)
	
	local t = {}
	s, sep = s and s:gsub('\\n', '\n'), sep and sep:gsub('\\n', '\n')
	for i = start, num, 1 do
		local parsedNum = isRoman and p._toRoman(i) or i
		
		t[i] = p.parseDualArg(s):gsub('([^\\])%$n', '%1' .. parsedNum):gsub('^%$n', parsedNum):gsub('\\%$', '$')
	end
	
	return table.concat(t, sep)
end

---------------------------------------------------------------------------------
-- Html Wrapping Function
-- 
-- Allows for easy creating of html elements in a lua format 
-- This function is meant to make single html elements. 
-- Use mw.html.create() for more complex elements.
---------------------------------------------------------------------------------
local function parseHtmlAttrs(attrs)
	local attrsTable = {}
	
	for k, v in pairs(attrs) do
		local kType, vType = type(k), type(v)
		if kType ~= 'string' and kType ~= 'number' then
			error(string.format('Invalid table index (attribute name/string expected, got %s)', kType), 2)
		elseif k == '' then
			error('Invalid table index (attribute name expected)', 2)
		elseif not tostring(k):match('^([%w%_%:%.%-]+)$') then
			error(string.format('Invalid HTML attribute name "%s"', k), 2)
		end
		
		k = tostring(k):lower()
		if k == 'style' and vType == 'table' then
			cssTables = {}
			for key, val in pairs(v) do
				cssTables[#cssTables+1] = (type(key) == 'string' and key:lower() .. ':' or '') .. tostring(val)
			end
			v = table.concat(cssTables, ';')
		elseif k == 'style' and not v:match('(;)$') then
			v = v .. ';'
		elseif k == 'id' then
			v = v:gsub(' ', '-')
		elseif k == 'class' and vType == 'table' then
			classTables = {}
			for i, val in pairs(v) do
				classTables[#classTables+1] = val:gsub(' ', '-')
			end
			v = table.concat(classTables, ' ')
		elseif k == 'href' then
			v = mw.uri.encode(mw.uri.encode(v))
		elseif k == 'title' and vType == 'table' then
			v = p.parseDualArg(v)
		end
		attrsTable[#attrsTable+1] = table.concat{k, '="', p.parseDualArg(v), '"'}
	end
	return table.concat(attrsTable, ' ')
end

local selfClosingTags = {
	['area'] = true,
	['base'] = true,
	['br'] = true,
	['col'] = true,
	['command'] = true,
	['embed'] = true,
	['hr'] = true,
	['img'] = true,
	['input'] = true,
	['keygen'] = true,
	['link'] = true,
	['meta'] = true,
	['param'] = true,
	['source'] = true,
	['track'] = true,
	['wbr'] = true,
	['path'] = true,
	['svg'] = true,
	['defs'] = true,
}

function p.wrapHtml(val, wrap, attrs)
	if type(val) == 'table' and not wrap then
		attrs = val[3] or val.attrs
		wrap = val[2] or val.tag
		sep = val.sep or val.s
		val = val[1] or val.text
	end
	
	checkTypeLight('wrapHtml', 1, val, { 'string', 'table', 'number' })
	checkTypeLight('wrapHtml', 2, wrap, 'string')
	checkTypeLight('wrapHtml', 3, attrs, 'table', true)
	
	if wrap == '' or not wrap
		then error('bad argument #2 to \'wrapHtml\' (tag name expected)', 2)
	end
	
	sep = type(val) == 'table'
		and (val.seperator or val.sep or val.s)
		or ''
	
	wrap = wrap:lower():gsub('%<[%\\%/]?([^%/%\\]+)[%\\%/]?>', '%1')
	local selfClosing = selfClosingTags[wrap]
		
	if attrs ~= nil
		then 
		attrs = ' ' .. parseHtmlAttrs(attrs)
		else attrs = ''
	end
	
	if wrap:match('([^%a0-9]+)')
		then error(string.format('Invalid HTML tag name \"<%s>\"', wrap), 2)
	end
	
	return table.concat{
		'<',
		wrap, 
		attrs,
		selfClosing and ' />' or '>',
		type(val) == 'table' and table.concat(val, sep) or val,
		selfClosing and '' or '</',
		selfClosing and '' or wrap,
		selfClosing and '' or '>',
	}
end

local function _makeTag(text, tag)
	tag = tag:lower():gsub('%<[%\\%/]?([^%/%\\]+)[%\\%/]?>', '%1')
	assertTrue(not tag:match('([^%a0-9]+)'), 'bad argument #2 to \'wrapTag\' (Invalid HTML tag name \"<%s>\")', 2, tag)
	
	text = p.parseDualArg(text) or ''
	local selfClosing = selfClosingTags[tag]
	return table.concat{
		'<',
		tag,
		selfClosing and ' />' or '>',
		text,
		selfClosing and '' or '</',
		selfClosing and '' or tag,
		selfClosing and '' or '>',
	}
end
function p.wrapTag(text, tag, attrs)
	checkTypeLight('wrapTag', 1, text, { 'string', 'table', 'number' }, true)
	checkTypeLight('wrapTag', 2, tag, { 'string', 'table' })
	assertTrue(#tag > 0, 'bad argument #2 to \'wrapTag\' (tag name expected)', 2)
	assertTrue(not attrs, 'Tag name contains attributes, please string.wrapHtml()', 2)
	
	text = p.parseDualArg(text) or ''
	tag = type(tag) ~= 'table' and { tag } or tag
	for i, tg in ipairs(tag) do
		text = _makeTag(text, tg)
	end
	
	return text
end

---------------------------------------------------------------------------------
-- function: ._formatShortNumber(number: string|number)
--
-- This function takes a number value and returns a short version of it
-- Example: 10000 = 10k
---------------------------------------------------------------------------------
function p._formatShortNum(number)
	local steps = {
		{1, ''},	-- units
		{1e3, 'k'},	-- thousand
		{1e6, 'M'},	-- million
		{1e9, 'B'},	-- billion
		{1e12, 'T'},	-- trillion
		{1e15, 'Qu'},	-- quadrillion
		{1e18, 'Qi'},	-- quintillion
		{1e21, 'Se'},	-- sextillion
		{1e24, 'Sp'},	-- septillion
		{1e27, 'O'},	-- octillion
		{1e30, 'N'},	-- nonillion
		{1e33, 'De'},	-- decillion
		{1e36, 'UDe'},	-- undecillion
		{1e39, 'DDe'},	-- duodecillion
		{1e42, 'TDe'},	-- tredecillion
		{1e45, 'QaDe'},	-- quattuordecillion
		{1e48, 'QiDe'},	-- quindecillion
		{1e51, 'SeDe'},	-- sexdecillion
		{1e54, 'SpDe'},	-- septemdecillion
		{1e57, 'ODe'},	-- octodecillion
		{1e60, 'NDe'},	-- novemdecillion
		{1e63, 'v'},	-- vigintillion
		{1e66, 'Uv'},	-- unvigintillion
		{1e69, 'Dv'},	-- duovigintillion
		{1e72, 'Tv'},	-- trevigintillion
		{1e75, 'Qav'},	-- quattuorvigintillion
		{1e78, 'Qiv'},	-- quinvigintillion
		{1e81, 'Sev'},	-- sexvigintillion
		{1e84, 'Spv'},	-- septemvigintillion
		{1e87, 'Ov'},	-- octovigintillion
		{1e90, 'Nv'},	-- novemvigintillion
	}
	for _, b in ipairs(steps) do
		if b[1] <= number+1 then
			steps.use = _
		end
	end
	local result = string.format('%.1f', number / steps[steps.use][1])
	if tonumber(result) >= 1e3 and steps.use < #steps then
		steps.use = steps.use + 1
		result = string.format('%.1f', tonumber(result) / 1e3)
	end
	result = string.sub(result, 0, string.sub(result, -1) == '0' and -3 or -1)
	return result .. steps[steps.use][2]
end

---------------------------------------------------------------------------------
-- function: trimTrailingZeros(n)
-- 
-- Removes trailing zeros from a number.
---------------------------------------------------------------------------------
function p.trimTrailingZeros(s)
	return tonumber((tostring(s):gsub('0*$', '')))
end

---------------------------------------------------------------------------------
-- function: ._toNumber(str: string)
---------------------------------------------------------------------------------
function p._toNumber(str)
	local lang = mw.language.new('en')
	
	-- check normal string -> number
	local num = tonumber(lang:parseFormattedNumber(tostring(str)))
	if num then return num end
	
	-- check if number short form
	local steps = {
		{1e3, 'k'},
		{1e6, 'm'},
		{1e9, 'b'},
		{1e12, 't'},
		{1e15, 'qa'},
		{1e18, 'qi'},
		{1e21, 'se'},
		{1e24, 'sp'},
		{1e27, 'o'},
		{1e30, 'n'},
		{1e33, 'de'}
	}
	for i, step in pairs(steps) do
		num = string.match(string.lower(tostring(str)), '([%d%.,]+)' .. step[2] )
		if num then
			local exp = step[1]
			num = num * exp
			break
		end
	end
	if num then return num end
	
	-- else invalid
	return nil
end

---------------------------------------------------------------------------------
-- Template:FormatNum
---------------------------------------------------------------------------------
function p.formatNum( frame )
	local args = getArgs(frame)
	return p._formatNum( args[1] )
end

---------------------------------------------------------------------------------
-- Template:FormatNum Module Access point
---------------------------------------------------------------------------------
function p._formatNum(num)
	local lang = mw.language.new('en')
	
	local num = tostring(num or 0):gsub('[%, ]', '')
	local neg
	
	if not tonumber(num) then
		return tonumber(lang:parseFormattedNumber(num))
	end
	
	if #num < 3 then return num end
	if num:match('^%-') then 
		neg = true
		num = num:gsub('^%-', '')
	end
	
	local decimal = num:match('%.([0-9]+)$')
	num = num:gsub('%.([0-9]+)$', '')
	num, ret = tostring(num), {}
	
	local _, len = num:gsub('%d%d%d', '')
	
	for i = len, 1, -1 do
		table.insert(ret, 1, num:match('%d%d%d$'))
		num = num:gsub('%d%d%d$', '')
	end
	
	if num ~= '' then
		table.insert(ret, 1, num)
	end
	
	return (neg and '-' or '') .. table.concat(ret, ',') .. (decimal and '.' .. decimal or '')
end

---------------------------------------------------------------------------------
-- Internal implementation of p.error() for more flexibility
---------------------------------------------------------------------------------
local function errorWithStack(msg, level)
	if msg and msg:match('^[Tt]emplate:(.-):%s*') then
		template = msg:match('^[Tt]emplate:(.-):%s*')
		msg = msg:gsub('^[Tt]emplate:(.-):%s*', '')
	end
	
	local tmp = msg
	local errorMsg = debug.traceback(tmp or 'Unknown error', level or 0)
	local msg = tmp or 'Unknown error'
	
	if msg:match('bad argument.*') then
		msg = msg:gsub('^.-%((.-)%).-$', '%1')
	end
	local errorMsg = (errorMsg:match('^(M?o?d?u?l?e?:?[%w%.%(%)%:]+):(%d+)') and '' or 'Lua Error: ') .. errorMsg
		:gsub('^(M?o?d?u?l?e?:?[%w%.%(%)%:%/%_ %(%)]+):(%d+)', function(name, line)
			return table.concat{ 
				'Lua Error in ', 
				name:match('Module:') and p.fullUrl(
					name,
					{ action = 'edit' },
					{ name, '&#x0200b;:', line },
					{ 'mw-ce-l', line }
				) or name, 
				' at line ',
				line 
			}
		end, 1)
		:gsub('\n\t([%w%.%(%)%:%/%_ %(%)%[%]]+):', '\n\t<b>%1</b>:')
		:gsub('\n', '<br>')
		:gsub(
			'Module:([%w%.%(%)%:%/%_ %(%)]+):(%d+)', 
			function(module, line)
				return p.fullUrl(
					{ 'Module:', module }, 
					{ action = 'edit' },
					{ 'Module:', module, ':', line },
					{ 'mw-ce-l', line }
				)
			end
		)
		
	local ret = table.concat{
		p.wrapHtml{
			{
				'➤ ',
				template and 'Template Error in [[Template:' .. template .. '|'.. p.wrapHtml('Template:' .. template, 'strong', {class = 'error'}) .. ']]:&nbsp;' or 'Template Error:&nbsp;',
				msg,
			},
			'<span>',
			{
				class = {
					'error',
					'mw-customtoggle-callstack',
				},
			},
		},
		p.wrapHtml{
			errorMsg,
			'<div>',
			{
				id = 'mw-customcollapsible-callstack',
				class = {
					'mw-collapsible',
					'mw-collapsed',
				},
				style = {
					['background-color'] = 'rgba(0,0,0,0.1)',
					['line-height'] = '14px',
					['overflow'] = 'auto',
					['padding'] = '8px',
					['word-wrap'] = 'normal',
					['display'] = 'block',
					['white-space'] = 'pre',
					['margin'] = '1em 0px',
					['font-family'] = 'monospace',
					['tab-size'] = 4,
				},
			},
		},
		'[[Category:Pages with template errors]]',
	}
	
	mw.addWarning(ret)
	return ret
end

---------------------------------------------------------------------------------
-- function: .error(msg: string, ...<string.format() arguments>)
--
-- Returns a error message with the lua call stack. "Template:<template>" 
-- may be added at the front of the message to link a template to the error message.
-- Arguments may be passed as they are in `string.format()`.
---------------------------------------------------------------------------------
function p.error(msg, ...)
	local vArgs = { ... }
	for i, v in pairs(vArgs) do
		if type(v) == 'number' then
			level = v
			table.remove(vArgs, i)
			break
		end
	end
	for i, v in pairs(vArgs) do
		vArgs[i] = p.parseDualArg(v)
	end
	return errorWithStack(string.format(msg, ...), 0)
end
p.templateError = p.error
p._error = p.error

---------------------------------------------------------------------------
-- function: .pcall(f: function [function to call], ...params?: any [function parameters])
--
-- Returns all values by the called function if no error was raised.
-- If there was an error in calling the function, it returns a formatted error message.
---------------------------------------------------------------------------
function p.pcall(f, ...)
	checkType('pcall', 1, f, 'function')
	
	local len = select('#', ...)
	local t = { ... }
	local success, response = xpcall(bind(function(...)
		return f(...)
	end, ...), function(e)
		local t = p.split(errorWithStack(e, 4), '<br>')
		
		return table.concat(t, '<br>')
	end)
	
	return response
end

---------------------------------------------------------------------------------
-- function: .preprocess(val: string)
--
-- parse wikitext into html
---------------------------------------------------------------------------------
function p._preprocess(val)
	local frame = mw.getCurrentFrame()
	
	return frame:preprocess(val)
end
p.preprocess = p._preprocess

---------------------------------------------------------------------------------
-- function: .centerText(s: string)
--
-- aligns text to the center of an element
---------------------------------------------------------------------------------
function p.centerText(s)
	return p.wrapHtml(s, 'div', {style = 'text-align: center;'}) 
end

---------------------------------------------------------------------------------
-- function: .trimWhitespace(s: string)
--
-- Trims the whitespace from the string
---------------------------------------------------------------------------------
function p.trimWhitespace(s, removeDoubles)
	checkTypeLight('trimWhitespace', 1, s, 'string', true)
	checkTypeLight('trimWhitespace', 2, removeDoubles, 'boolean', true)
	
	if not s then return s end
	
	s = s:gsub('^%s*(.-)%s*$', '%1')
	if removeDoubles then
		s = s:gsub('(%s)%s*', '%1')
	end
	return s
end
p.trim = p.trimWhitespace

------------------------------------------------
-- function: .toRoman(s: string)
-- original source: https://gist.github.com/efrederickson/4080372
--[[
Symbol	Value
I		1
V		5
X		10
L		50
C		100
D		500
M		1000
If a lesser number comes before a greater number (e.g. IX), then
the lesser number is subtracted from the greater number (IX -> 9, 900 -> CM)
So, 
Symbol	Value
IV		4
IX		9
XL		40
XC		90
CD		400
CM		900
LM		950
VX is actually valid as 5, along with other irregularities, such as IIIIIV for 8
Copyright (C) 2012 LoDC
]]
---------------------------------------------------------------------------------
local map = { 
	I = 1,
	V = 5,
	X = 10,
	L = 50,
	C = 100, 
	D = 500, 
	M = 1000,
}
local numbers = { 1, 5, 10, 50, 100, 500, 1000 }
local chars = { 'I', 'V', 'X', 'L', 'C', 'D', 'M' }

function p._toRoman(s)
	s = p._toArabic(s)
	
	if not s or s ~= s then return nil end
	if s == math.huge then error('Unable to convert infinity', 2) end
	
	s = math.floor(s)
	
	if s <= 0 then return s end
	
	local ret = ''
		for i = #numbers, 1, -1 do
		local num = numbers[i]
		while s - num >= 0 and s > 0 do
			ret = ret .. chars[i]
			s = s - num
		end
		-- for j = i - 1, 1, -1 do
		for j = 1, i - 1 do
			local n2 = numbers[j]
			if s - (num - n2) >= 0 and s < num and s > 0 and num - n2 ~= n2 then
				ret = ret .. chars[j] .. chars[i]
				s = s - (num - n2)
				break
			end
		end
	end
	return ret
end

---------------------------------------------------------------------------------
-- Template:ToRomanNum
--
-- Convert Numbers to roman numerals
---------------------------------------------------------------------------------
function p.roman(frame)
	local args = getArgs(frame)
	local num = args[1]
	local min = tonumber(args['min']) or 1
	local max = tonumber(args['max']) or 9999999
	
	-- if already a roman numeral, convert to number
	if string.match(num:upper(), '^[IVXLCDM]+$') then
		num = p._toArabic(num)
	end
	
	num = tonumber(num)
	if tonumber(num) then
		if num >= min and num <= max then
			return p.wrapHtml(p._toRoman(num), 'span', {style = 'font: bold 100% times new roman;'})
		else
			-- if we set a min/max and the number doesn't fall between it then it's invalid
			return '[out of range][[Category:Pages with roman numeral errors]]'
		end
	end
	return 'INVALID INPUT[[Category:Pages with roman numeral errors]]'
end

---------------------------------------------------------------------------------
-- function: .toArabic(s: string)
--
-- converts roman numerals to regular numbers
---------------------------------------------------------------------------------
function p._toArabic(s)
	s = tostring(s):upper()
	local ret = 0
	local i = 1
	
	if s:match('^%d+$') then
		return tonumber(s)
	elseif s == '' or s == 'NIL' then
		return 0
	elseif not s:match('^[IVXLCDM%d%-]+$') then
		return nil
	end
	
	while i <= s:len() do
	-- for i = 1, s:len() do
		local c = s:sub(i, i)
		if c ~= ' ' then -- allow spaces
			local m = map[c] or error('Unknown Roman Numeral \'' .. c .. '\'', 2)
			
			local next = s:sub(i + 1, i + 1)
			local nextm = map[next]
			
			if next and nextm then
				if nextm > m then 
				-- if string[i] < string[i + 1] then result += string[i + 1] - string[i]
				-- This is used instead of programming in IV = 4, IX = 9, etc, because it is
				-- more flexible and possibly more efficient
					ret = ret + (nextm - m)
					i = i + 1
				else
					ret = ret + m
				end
			else
				ret = ret + m
			end
		end
		i = i + 1
	end
	return tonumber(ret)
end

function p._splitNameAndTier(str)
	local out = {}
	if str:find('%s[%dIVXLCDMivxlcdm]+$') then
		out[1], out[2] = str:match('^(.+)%s([%dIVXLCDMivxlcdm]+)$')
	else
		out[1] = str
		out[2] = nil
	end
	return out
end

---------------------------------------------------------------------------------
-- Template: Skydate
--
-- Converts an ingame date to a date compatible with skydate.js
---------------------------------------------------------------------------------
-- function p.skydate(str)
-- 	local conversions = {
-- 		['early spring'] = 'ESP',
-- 		['^spring'] = 'SP',
-- 		['late spring'] = 'LSP',
-- 		['early summer'] = 'ESU',
-- 		['^summer'] = 'SU',
-- 		['late summer'] = 'LSU',
-- 		['early autumn'] = 'EAU',
-- 		['^autumn'] = 'AU',
-- 		['late autumn'] = 'LAU',
-- 		['early fall'] = 'EAU',
-- 		['^fall'] = 'AU',
-- 		['late fall'] = 'LAU',
-- 		['early winter'] = 'EWI',
-- 		['^winter'] = 'WI',
-- 		['late winter'] = 'LWI',
-- 		['(%d)st'] = '%1',
-- 		['(%d)nd'] = '%1',
-- 		['(%d)rd'] = '%1',
-- 		['(%d)th'] = '%1',
-- 	}
-- 	local str = getArgs(frame)[1] or ''
-- 	for k, v in pairs(conversions) do
-- 		str = str:gsub(k, v)
-- 	end
-- 	return str
-- end

---------------------------------------------------------------------------------
-- Template: Lorem
--
-- Classic lorem ispum
---------------------------------------------------------------------------------
function p.lorem(frame)
	local args = getArgs(frame)
	local num = args[1]
	if not num then num = '1p' end
	return p._lorem(num)
end
---------------------------------------------------------------------------------
-- Template: Lorem module access point
---------------------------------------------------------------------------------
function p._lorem(num)
	lorem = require('Module:String/Lorem')
	
	local suffix
	suffix = num:match('^%d*(%a)$') or nil
	num = num:match('^(%d*)%a?$') or error('No number provided')
	num = tonumber(num)
	
	if not (suffix == nil or suffix == 'w' or suffix == 'p') then p._error('invalid suffix', suffix) end
	
	local str = {}
	if suffix == nil then suffix = 'w' end
	if suffix == 'p' then 
		if num > 10 or num == 0 then return p._error('Invalid number. Maximum number accepted: 10') end
		str[#str+1] = lorem[i]
		for i = 2, num, 1 do
			str[#str+1] = '\n' .. lorem[i]
		end
	elseif suffix == 'w' then
		if num > 1008 or num == 0 then return p._error('Invalid number. Maximum number accepted: 10') end
		full = lorem['full']
		full = p.split(full, '[%s\n]')
		str[#str+1] = full[i]
		for i = 1, num, 1 do
			str[#str+1] = ' ' .. full[i]
		end
	end
	return table.concat(str)
end
---------------------------------------------------------------------------------
-- function: .roundNumber(num: number, posistion: number)
--
-- rounds numbers nicely
---------------------------------------------------------------------------------
function p.roundNumber(num, position)
	if not position then position = 0 end
	position = 10^position
	num = num * position
	num = math.floor(num + 0.5)
	num = num / position
	return num
end

---------------------------------------------------------------------------------
-- function _delDoubleSpace(text: string)
--
-- Remove duplicate spaces form strings
---------------------------------------------------------------------------------
function p._delDoubleSpace(text)
	text = text:gsub('(%s)%s*', '%1')
	return text
end

---------------------------------------------------------------------------------
-- Template:Lower
---------------------------------------------------------------------------------
function p._lower(frame)
	local args = getArgs(frame)
	local s = args[1]
	
	if not s then s = '' end
	return s:lower()
end
---------------------------------------------------------------------------------
-- Template:Upper
---------------------------------------------------------------------------------
function p._upper(frame)
	local args = getArgs(frame)
	local s = args[1] or ''
	
	return s:upper()
end

function p.warning(frame)
	return mw.addWarning(getArgs(frame)[1])
end

---------------------------------------------------------------------------------
-- function: sublength(frame: table)
-- 
-- returns a substring of a given string at a specific index and length
-- originally from [[WP:Module:String]]
---------------------------------------------------------------------------------
function p.sublength(frame)
	local args = getArgs(frame)
	
	local i = tonumber(args.i) or 0
	local len = tonumber(args.len)
	return mw.ustring.sub(args.s, i + 1, len and (i + len))
end

---------------------------------------------------------------------------------
-- function: matchTemplate(frame)
--
-- a version of string.match() that can be used with {{#invoke:String|matchTemplate}}
---------------------------------------------------------------------------------
function p.matchTemplate(frame)
	local args = getArgs(frame)
	
	local s = args['s'] or args[1] or ''
	local pattern = args['pattern'] or args[2] or ''
	local nomatch = args['nomatch']
	
	return mw.ustring.match(s, pattern) or nomatch
end

-- Finish module
return p
local loader = require('Module:Loader')
local string, table, yesno, color, mctxt, arguments = loader.lazy.require('String', 'Table', 'Yesno', 'Color', 'Mctxt', 'Arguments')

local p = {}

---------------------------------------------------------------------------
-- Template:Repeat
--
-- Repeats the given string a specified number of times
---------------------------------------------------------------------------
function p.repeatF(frame)
	local args = arguments.getArgs(frame, { removeBlanks = false })
	local s = args[1] or ''
	local num = args[2] or '1'
	local sep = args[3]

	if num:match('[^%d%-%+]+')
	then return string.error('number expected, got "%s"', tonumber(num))
	elseif 0 >= tonumber(num)
	then return string.error('repeat delimiter must be greater than 0, got %s', num)
	end

	return p._repeat(s, num, sep)
end

---------------------------------------------------------------------------------
-- Template:Code
--
-- Creates a piece of formatted code.
---------------------------------------------------------------------------------
function p.code(frame)
	local args = arguments.getArgs(frame, { removeBlanks = false, trim = false })

	local code = args['code'] or args['c'] or args[1]
	local tmp = yesno(args['inline'] or args['i'], not code:match('\n'))
	local contentOnly = yesno(args['conly'] or args['contentonly'] or args['only'], false)

	if not tmp and tmp ~= nil then
		tmp = false
	end

	local inline = tmp ~= false
		and 1
		or nil

	return (args['lang'] or args['l'])
		and mw.getCurrentFrame():extensionTag('syntaxhighlight', code, {
			inline = inline,
			lang = args['lang'] or args['l'],
			class = (args['class'] or args['cl'] or '') .. (contentOnly and ' contents-only' or '')
		})
		or string.wrapHtml(code, '<span>', {
			class = 'code'
		})
end

---------------------------------------------------------------------------------
-- Template: Style
--
-- Makes making CSS easier.
---------------------------------------------------------------------------------
function p.style(frame)
	local ret = {}

	for prop, value in pairs(arguments.getArgs(frame)) do
		table.push(ret, prop, ': ', value, '; ')
	end

	return table.concat(ret, '')
end

---------------------------------------------------------------------------------
-- Template: ClassList
--
-- Creates an HTML Class List.
---------------------------------------------------------------------------------
function p.classList(frame)
	local t = arguments.mergeArgsSyntax(arguments.getArgs(frame))
	local ret = {}

	for i, v in ipairs(t) do
		table.push(ret, v)
	end
	return table.concat(ret, ' ')
end

---------------------------------------------------------------------------------
-- function: yes(text, size)
--
-- Creates a "Yes" pictogram.
---------------------------------------------------------------------------------
function p.yes(text, size)
	return mctxt._raw('&a✔') .. (text and ' ' .. color.colorText('Green', '<b>Yes</b>') or '')
end

---------------------------------------------------------------------------------
-- function: no(text, size)
--
-- Creates a "No" pictogram.
---------------------------------------------------------------------------------
function p.no(text, size)
	return mctxt._raw('&c✕') .. (text and ' ' .. color.colorText('Red', '<b>No</b>') or '')
end

---------------------------------------------------------------------------------
-- function: yescircle(text, centered)
--
-- Creates a "Yes" circle.
---------------------------------------------------------------------------------
function p.yescircle(text, centered)
	return string.wrapHtml(text and ' ' .. color.colorText('#7ec525', text) or '', 'span', { class = 'circled-y' .. (centered and ' centered' or '') })
end

---------------------------------------------------------------------------------
-- function: nocircle(text, centered)
--
-- Creates a "No" circle.
---------------------------------------------------------------------------------
function p.nocircle(text, centered)
	return string.wrapHtml(text and ' ' .. color.colorText('#aaa', text) or '', 'span', { class = 'circled-n' .. (centered and ' centered' or '') })
end

---------------------------------------------------------------------------------
-- function: unknown(?text: boolean, ?size: number, ?altText: string, ?reason: string)
--
-- Creates a "unknown" pictogram.
---------------------------------------------------------------------------------
function p.unknown(text, size, altText, reason)
	return mctxt._raw('&7?') .. (text and ' ' or '') ..
		string.makeTitle((altText or (text and color.colorText('gray', '<b>Unknown</b>')) or ''),
			'This information is unknown' ..
			(reason and ' ' .. reason or '') .. '. If you know this information, please edit the page and replace this.')

end

---------------------------------------------------------------------------------
-- function: .blankCell()
--
-- Makes a blank table cell, made for use in `<td>` tags
-- See {{Template:BlankCell}} for CSS and further details
---------------------------------------------------------------------------------
function p.blankCell()
	return string.wrapHtml('', 'div', {
		class = {'cellTemplate', 'blankCell'}, 
		title = 'This cell is intentionally left blank', 
		['data-sort-value'] = 0
	})
end

---------------------------------------------------------------------------------
-- function: .infoNeeded()
--
-- Makes info needed text
---------------------------------------------------------------------------------
function p.infoNeeded()
	return tostring(
		mw.html.create('div')
			:tag('font')
				:attr({ color = '#910000' })
				:wikitext('More Info Needed')
			:done()
			:wikitext('[[Category:More info needed]]')
		:done()
	)
end

return p
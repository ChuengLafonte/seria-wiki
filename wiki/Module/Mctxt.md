local getArgs = require('Module:Arguments').getArgs

local p = {}

function p.raw( frame )
	local args = getArgs(frame)
	return p._raw(args[1], args.size or args[2], args.class, args.style)
end

function p._raw( str, size, class, style )
	if not str then return '' end
	str = str:gsub('\n', '/'):gsub('<br>', '/')
	size = tonumber(size) and (size .. 'px') or size or '12px'
	local s = str:gsub('\\\\', '%%BACKSLASH%%'):gsub('\\/', '%%FORSLASH%%'):gsub('\\&', '%%AMPERSAND%%')
	local t = mw.text.split(s, '/')
	for i, l in ipairs(t) do
		l = l .. '&r'
		while (l:match('&[0-9a-fk-o]')) do
			l = l:gsub('&([0-9a-fk-o])(.-)((&[0-9a-fr]))', '<span class="format-%1">%2&r</span>%3', 1)
		end
		t[i] = l
	end
	s = table.concat(t, '<br>')
	s = s:gsub('&r', ''):gsub('%%BACKSLASH%%', '\\\\'):gsub('%%FORSLASH%%', '\\/'):gsub('%%AMPERSAND%%', '\\&'):gsub('\\(.)', '%1')
	return ('<span class="mcui-text %s" style="display: inline; font-size: %s; %s">%s</span>'):format(class or '', size, style or '', s)
end

function p.dialogue( frame )
	local args = getArgs(frame)
	return p._dialogue(args[1], args.size or args[2], args.class, args.style)
end

function p._dialogue( str, size, class, style )
	if not str then return '' end
	str = str:gsub('\n', '/'):gsub('<br>', '/')
	size = size and (tonumber(size) and (size .. 'px') or size) or nil
	local s = str:gsub('\\\\', '%%BACKSLASH%%'):gsub('\\/', '%%FORSLASH%%')
	local t = mw.text.split(s, '/')
	for i, l in ipairs(t) do
		local lineclass = ''
		l = '<div class="mcdialogue-line ' .. lineclass .. '">' .. l .. '&r</div>'
		while (l:match('&[0-9a-fk-o]')) do
			l = l:gsub('&([0-9a-fk-o])(.-)((&[0-9a-fr]))', '<span class="format-%1">%2&r</span>%3', 1)
		end
		t[i] = l
	end
	s = table.concat(t)
	s = s:gsub('&r', ''):gsub('%%BACKSLASH%%', '\\\\'):gsub('%%FORSLASH%%', '\\/'):gsub('\\(.)', '%1')
	return ('<div class="mcdialogue %s" style="%s">%s</div>'):format(
		class or '', (size and ('font-size:' .. size) or '') .. (style or ''), s
	)
end

return p

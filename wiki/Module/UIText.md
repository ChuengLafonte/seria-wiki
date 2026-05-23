local getArgs = require('Module:Arguments').getArgs

local p = {}

-- Applies Minecraft-style color/formatting codes (&0-9, &a-f, &k-r) to a string.
function p.applyReplacements(val)
	if not val then return '' end
	-- Pass-through: no stat/rarity/zone replacement needed for basic UI rendering
	return val
end

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

function p.getFormatting(color, text, ampersand)
	local amp = ampersand or (text and true or false)
	-- Simple passthrough — return color code with optional text
	return (amp and '&' or '') .. (color or '') .. (text or '')
end

return p

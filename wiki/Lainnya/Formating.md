<syntaxhighlight line="1">
local p = {}
local lib = require('Module:Feature')
local search = lib.inArray

function p.main(frame)
	local args = require('Module:Arguments').getArgs(frame, {
		parentFirst = true,
		removeBlanks = false
	})
	local main = args['text'] or args[1]
	local label = args['label'] or args[2] or ''
	local r_s,r_e,b,i,u_s,u_e,v_s,v_e = '','','','','','','',''
	if main == nil then error('A value must be given') end
	local nw = mw.text.nowiki
	local out = mw.html.create('span'):addClass(' custom-formatting-code')
	if args.NC then
		out:addClass(' custom-formatting-plain')
	end
	if args.block then
		out:addClass(' code-block' .. lib.ternary(main:find('Infobox'),'-table',''))
	end

	--check what to add, leave variable blank if option wasn't enabled
	if (args['ref'] or args['r']) then
		r_s = '<ref>'
		r_e = '</ref>'
	end
	if (args['bold'] or args['b']) then
		b = "'''"
	end
	if (args['italic'] or args['i']) then
		i = "''"
	end
	if (args['underline'] or args['u']) then
		u_s = '<u>'
		u_e = '</u>'
	end
	if (args['variable'] or args['v']) then
		main = tostring(mw.html.create():tag("span"):addClass('variable'):wikitext(nw(main)))
	end
	if lib.isNotEmpty(label) and (args['variable-label'] or args['vl']) then
		label = tostring(mw.html.create():tag("span"):addClass('variable'):wikitext(nw(label)))
	end

	local prefix = ((args.prefix or ''):gsub('{space}', ' '):gsub('{newline}', '\n')) .. b .. i .. u_s
	local suffix = u_e .. i .. b .. ((args.suffix or ''):gsub('{space}', ' '):gsub('{newline}', '\n'))
	
	local joint = ' yields: '
	if args['no_joint'] then joint = ' ' end
	
	if args['_Ybr_'] then
		joint = joint .. '<br />'
	elseif args['_Yn_'] then
		joint = joint .. '\n'
	end

	--create result as internal link
	if (args['link'] or args['l']) then
		if lib.isNotEmpty(label) then
			out
				:wikitext(nw(r_s .. prefix),nw('[['),p.variableFormat(main),nw('|'),p.variableFormat(label),nw(']]'),nw(suffix .. r_e))
		else
			out
				:wikitext(nw(r_s .. prefix),nw('[['),p.variableFormat(main),nw(']]'),nw(suffix .. r_e))
		end
		if (args['_Ybr_'] or args['_Y_'] or args['_Yn_']) then
			local content = prefix  .. '[[' .. main .. '|' .. (lib.isNotEmpty(label) and label or main) .. ']]' .. suffix
			if (args['ref'] or args['r']) then
				return tostring(out) .. joint .. frame:extensionTag{ name = 'ref', content = content}
			else
				return tostring(out) .. joint .. content
			end
		elseif args.NC then
			local content = prefix  .. '[[' .. main .. '|' .. (lib.isNotEmpty(label) and label or main) .. ']]' .. suffix
			return '<span class="custom-formatting-nested">'..tostring(out)..'</span><span class="custom-formatting-resulting">' .. tostring(content) .. '</span>'
		end

	--create result as external link
	elseif (args['external-link'] or args['el']) then
		if lib.isNotEmpty(label) then
			out
				:wikitext(nw(r_s .. prefix),nw('['),p.variableFormat(nw(mw.text.unstrip(main))),' ',p.variableFormat(label),nw(']'),nw(suffix .. r_e))
		else
			out
				:wikitext(nw(r_s .. prefix),nw('['),p.variableFormat(nw(mw.text.unstrip(main))),nw(']'),nw(suffix .. r_e))
		end
		if (args['_Ybr_'] or args['_Y_'] or args['_Yn_']) then
			local content = prefix  .. '[' .. main .. ' ' .. label .. ']' .. suffix
			if (args['ref'] or args['r']) then
				return tostring(out) .. joint .. frame:extensionTag{ name = 'ref', content = content}
			else
				return tostring(out) .. joint .. content
			end
		elseif args.NC then
			local content = prefix  .. '[' .. main .. ' ' .. label .. ']' .. suffix
			return '<span class="custom-formatting-nested">'..tostring(out)..'</span><span class="custom-formatting-resulting">' .. tostring(content) .. '</span>'
		end

	elseif (args['template'] or args['t']) then
		local SPECIAL = {'_Y_','_Ybr_','_Yn_','let_parse','block','t','template','NC','ref','r','b','boid','i','italic','u','underline','v','variable','suffix','prefix'}
		local yieldargs = {}
		local pre = main
		local t_prefix = lib.split(main, ':')[1]
		if not lib.inArray({'User','U','Profile', 'Genshin Impact Wiki'}, t_prefix) then
			pre = 'Template:' .. main
		end
		main = '[[' .. pre .. '|' .. main:gsub(' ','&nbsp;') .. ']]'

		--template call with params
		if p.checkParams(args,SPECIAL) then
			
			--open fake template call
			out
				:wikitext(nw(r_s .. prefix),nw('{{'),main)
			local param = 1
			while (args['v'..param] or args['P' .. param] or args['p' .. param] or args[param+1]) do
				--variable input format
				if args['v'..param] then
					local parse = p.parseParam(args['v'..param])

					if args.block then
						out:wikitext('<br />')
					end

					--named param format
					if parse.value then
						out
							:wikitext(nw('|'),'<b>',p.variableFormat(nw(parse.name)),'</b>',string.rep('&nbsp;',parse.spacing),'= ',tostring(mw.html.create():tag("span"):addClass('variable'):wikitext(p.NewLineAllow(parse.value, args.let_parse))))

					--unnamed param format
					else
						out
							:wikitext(nw('|'),tostring(mw.html.create():tag("span"):addClass('variable'):wikitext(p.NewLineAllow(parse.name, args.let_parse))))
					end
					args['v' .. param] = nil

				--fixed input format
				elseif (args['p' .. param] or args[param+1]) then
					local value = args['p' .. param] or args[param+1]
					local parse = p.parseParam(value)

					if args.block then
						out:wikitext('<br />')
					end

					--named param format
					if parse.value then
						yieldargs[parse.name] = mw.text.unstrip(parse.value)
						out
							:wikitext(nw('|'),'<b>',p.variableFormat(nw(parse.name)),'</b>',string.rep('&nbsp;',parse.spacing),'= ',p.NewLineAllow(p.variableFormat(parse.value), args.let_parse))

					--unnamed param format
					else
						yieldargs[param] = mw.text.unstrip(parse.name)
						out
							:wikitext(nw('|'),p.NewLineAllow(p.variableFormat(parse.name), args.let_parse))
					end
					
					--set values to nil for yield to ignore them
					if args['p' .. param] then args['p' .. param] = nil end
					if args[param+1] then args[param+1] = nil end
				--fixed input format, default let parse
				elseif args['P' .. param] then
					local value = args['P' .. param]
					local parse = p.parseParam(value)

					if args.block then
						out:wikitext('<br />')
					end

					--named param format
					if parse.value then
						yieldargs[parse.name] = mw.text.unstrip(parse.value)
						out
							:wikitext(nw('|'),'<b>',p.variableFormat(nw(parse.name)),'</b>',string.rep('&nbsp;',parse.spacing), '= ', p.NewLineAllow(p.variableFormat(parse.value), true))

					--unnamed param format
					else
						yieldargs[param] = mw.text.unstrip(parse.name)
						out
							:wikitext(nw('|'),p.NewLineAllow(p.variableFormat(parse.name), true))
					end
					
					--set values to nil for yield to ignore them
					args['P' .. param] = nil
				end

				--increase count for the next 'while' loop
				param = param + 1
			end
			
			for n,v in pairs(args) do
				if (n ~= 1 and not search(SPECIAL,n)) then
					yieldargs[n] = mw.text.unstrip(v)
					if args.block then
						out:wikitext('<br />')
					end
					out:wikitext(nw('|'),'<b>',p.variableFormat(nw(n)),'</b> = ',p.NewLineAllow(p.variableFormat(v),args.let_parse))
				end
			end

			if args.block then
				out:wikitext('<br />')
			end

			--close fake template call and all the selected items
			out
				:wikitext(nw('}}'),nw(suffix .. r_e))

		--template call without params
		else
			out
				:wikitext(nw(r_s .. prefix),nw('{{'),main,nw('}}'),nw(suffix .. r_e))
		end

		-- auto template result for examples
		if (args['_Ybr_'] or args['_Y_'] or args['_Yn_']) then
			frame = frame or mw.getCurrentFrame()
			local content = prefix .. frame:expandTemplate{title = (args['text'] or args[1]),args = yieldargs} .. suffix
			if args.block then
				joint = '<br />' .. joint
			end
			if (args['ref'] or args['r']) then
				return tostring(out) .. joint .. frame:extensionTag{ name = 'ref', content = content}
			else
				if main:find('Infobox') then
					return content .. tostring(out)
				else
					return tostring(out) .. joint .. content
				end
			end
		-- auto template result for nested usage in examples
		elseif args.NC then
			frame = frame or mw.getCurrentFrame()
			local content = prefix .. frame:expandTemplate{title = (args['text'] or args[1]),args = yieldargs} .. suffix
			return '<span class="custom-formatting-nested">'..tostring(out)..'</span><span class="custom-formatting-resulting">' .. tostring(content) .. '</span>'
		end

	--create plain text result
	else
		if (args['nowiki'] or args['nw']) then
			out
				:wikitext(nw(r_s .. prefix),p.variableFormat(nw(main)),nw(suffix .. r_e))
		else
			out
				:wikitext(nw(r_s .. prefix),p.variableFormat(main),nw(suffix .. r_e))
		end
		if (args['_Ybr_'] or args['_Y_'] or args['_Yn_']) then
			local content = prefix  .. main .. suffix
			if (args['ref'] or args['r']) then
				return tostring(out) .. joint .. frame:extensionTag{ name = 'ref', content = content}
			else
				return tostring(out) .. joint .. content
			end
		end
	end
	
	--return completed result
	return tostring(out)
end

function p.parseParam(param)
    local tmp = param
    local name, value, spacing = '','',' '

    -- the parameter's name is anything to the left of the first equals sign;
    -- the equals sign can be escaped, for wikis that don't have [[Template:=]]
    if tmp:find('=') then
        name, spacing, value = string.match(tmp,'^(.-)(%s*)=%s*(.-)$')
        if string.len(spacing) == 0 then spacing = 1 else spacing = string.len(spacing) end
    else
    	name = tmp
    	value = false
    end
    return {
    	name = name,
    	value = value,
    	spacing = spacing
    }
end

function p.variableFormat(textin)
	while (textin:find('%(%(') and textin:find('%)%)')) do
		local textrp = string.match(textin,'%(%((.-)%)%)')
		textin = textin:gsub('%(%(.-%)%)',tostring(mw.html.create():tag("span"):addClass('variable'):wikitext(mw.text.nowiki(textrp))),1)
	end
	return textin
end

function p.checkParams(args,SPECIAL)
	for n,v in pairs(args) do
		if (n ~= 1 and not search(SPECIAL,n)) then
			return true
		end
	end
	return false
end

--helper function to allow new line format in template calls in block format, as directly allowing makes the <code> container break
function p.NewLineAllow(str,parse)
	local container = mw.html.create()
	local nw = mw.text.nowiki
	
	if str:find('[\n\r]') then
		str = str:gsub('[\n\r]', '¤¤¤'):gsub('¤¤¤$', '')
		local splitstr = mw.text.split(str, '¤¤¤', true )
		for i,v in ipairs(splitstr) do
			if not parse then v = nw(v) end
			container:wikitext(v)
			if i ~= #splitstr then
				container:wikitext('<br />')
			end
		end
		return tostring(container)
	else
		if not parse then str = nw(str) end
		return str
	end
end

return p

</syntaxhighlight>
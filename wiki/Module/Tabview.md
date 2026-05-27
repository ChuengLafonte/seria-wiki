-- <pre>
local getArgs = require('Module:Arguments').getArgs
local loader = require('Module:Loader')

local string, table, yesno, jSON = loader.require('String', 'Table', 'Yesno', 'JSON')

local wikilink = 'https://Project Seria Caveblock-Project Seria Caveblock.fandom.com/wiki/'
local p = {}

function p.tabview( frame )
	local args = getArgs(frame)
	
	return p._tabview(table.deepCopy(args, true))
end

function p._tabview(args)
	local function argI(i)
		local s = string.trim(args[i])
		return s ~= '' and s or nil
	end
	local function get(s)
		local s = string.trim(s)
		return s ~= '' and s or nil
	end
	
	local positions, all, tabsList, linkList, index = {}, {}, {}, {}, 0
	
	for i = 1, #args do
		if argI(i) == '-' then
			table.push(positions, i)
		end
	end
	
	for i, thispos in ipairs(positions) do
		local temp, nextpos = {}, positions[i + 1]
		if ((nextpos or #args) - thispos > 0) and (argI(thispos + 1)) then
			for j = thispos + 1, nextpos and (nextpos - 1) or #args, 1 do
				table.push(temp, argI(j) or '')
			end
			table.push(all, temp)
		end
	end
	
	for i, tab in ipairs(all) do
		local pagename = get(tab[1])
		local tabname = get(tab[2]) or 'Tab ' .. i
		
		table.push(tabsList, {
			cache = yesno(tab[3], true),
			pagename = pagename,
			caption = tabname,
		})
		
		table.push(linkList, ('*[[%s|%s]]'):format(pagename, tabname))
	end
	
	local json_str = string.gsubAll(jSON.encode({
		activeTabIndex = args.active or 1,
		customButtonName = args.button,
		forceTabber = yesno(args.forceTabber, nil),
		noTabs = yesno(args.noTabs, nil),
		tabs = tabsList,
	}), '/', '\\/')
	
	local ret = mw.html.create('div')
		:addClass('partialLoad-settings')
		:attr('data-tabs', json_str)
		:wikitext('\n', table.concat(linkList, '\n'), '\n')
	
	return tostring(ret)
end

return p
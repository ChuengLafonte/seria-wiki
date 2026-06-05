--<pre>
---------------------------------------------------------------------------------
-- Module:List
-- This Module is used to store list templates of all kinds.
-- 
-- TABLE OF CONTENTS
--   * Unordered List (Unused as of now)
--   * Template: Plainlist
--   * Template: Horizontal List
--   * Template: Resource list
--   * Template: Image List
--   * Template: Mob List
--   * Template: NPC List
--   * Template: Location List
--   * Template: Zone List
--   * Template: Stats List
--   * Template: Gemstone slots
---------------------------------------------------------------------------------
local p = {}

local getArgs = require('Module:Arguments').getArgs
local mergeArgsSyntax = require('Module:Arguments').mergeArgsSyntax

local loader = require('Module:Loader')
local string, table, yesno, statname, sprite, item, gemstone, zone = loader.require('String', 'Table', 'Yesno', 'Statname', 'Sprite', 'Item', 'Gemstone', 'Zone')

local processResource, processItem = item._resourceDisplay, item._itemDisplay

--List Type Table
local listTypes = {
	['circle']='circle',
	['c']='circle',
	
	['square']='square',
	['sq']='square',
	['s']='square',
	
	['disc']='disc',
	['d']='disc',
	
	['none']='none',
	['n']='none',
}

local function generateList(list_, type_)
	return string.wrapHtml{
		list_,
		'<ul>', {
			style={
				['list-style-type'] = listTypes[type_] or 'none';
				['margin-left'] = '0';
				['line-height'] = 'inherit';
			}
		}
	}
end

local function generateListItem(res, liststyle)
	local styles = table.concat{
		'margin-left: 0;',
		'margin-bottom: 0;',
		'padding-bottom: 0;',
		liststyle or '',
		}
	
	return string.wrapHtml{
		res, '<li>', {
			style = styles
		}
	}
end

---------------------------------------------------------------------------------
-- Unordered List (not a template)
--
--
---------------------------------------------------------------------------------
function p.list(frame)
	local args = getArgs(frame)
	local text = args[1]
	local color = args['color']
	local listType = args['list_type'] or args['listtype'] or args['type'] or args['ls'] or args['t']

	return p._list(text, color, listType)
end

function p._list(text, color, listType)
	local split = mw.text.split(string.gsub(text, '\*', '<li/>'), '%s*\*%s*');
	
	if not color then color = '' end
	if not listType then listType = 'square' end
	
	return string.wrapHtml{ 
		split,
		'<ul>', {
			style={
				['list-style-type']=listType;
				color=color;
			}
		}
	}
end

---------------------------------------------------------------------------------
--Template:Plainlist
--
--makes a list without any spacing in the lines, indistinguishable from a '<br> list'
---------------------------------------------------------------------------------
function p.plainlist(frame)
	args = getArgs(frame)
	
	text = args[1]
	class = args['class']
	style = args['style']
	indent = args['indent']
	
	return p._plainlist(text, class, style, indent)
end

function p._plainlist(text, class, style, indent)
	local styleObj = {}
	
	local div = mw.html.create('div'):addClass('plainlist')
	if class then div:addClass(class) end
	if style then div:cssText(style) end
	if indent then
		indent = tonumber(indent) * 1.6
		div:css('margin-left', indent..'em')
	end
	-- Don't mess with the [[]]s! they're needed to force a new line before the wiki list syntax
	div:wikitext([[
	
	]]..text)
	
	return div
end

--------------------------------------------------------------------------------
-- Template:Horizontal List
--
-- For making a horizontal list (seperated by •)
--------------------------------------------------------------------------------
function p.horizontal(frame)
	local args = getArgs(frame)
	local list = mergeArgsSyntax(args)
	local bracket = yesno(args['bracket'] or args['brackets'], false)
	local inlineList = yesno(args['inlineList'], false)
	local inlineBlock = yesno(args['inline-block'], true)
	local style = args['style']
	
	local hlist = mw.html.create('ul'):cssText(style or '')
		:addClass('hlist')
	if inlineList then
		hlist:css('display', 'inline'):css('margin-left', '0')
	else
		hlist:css('margin-left', '2em')
	end
	
	for _, v in ipairs(list) do
		hlist:tag('li'):wikitext( v )
		:addClass((inlineBlock and ' inline-block' or ''))
	end
	
	return tostring(hlist)
end

--------------------------------------------------------------------------------
-- Template:Resource List
--
-- For making a formatted list of items, mostly used in infoboxes ('Raw Materials' section)
--------------------------------------------------------------------------------
function p.resourceList(frame)
	local args = getArgs(frame)
	
	local text = mergeArgsSyntax(args)
	local listType = args['list_type'] or args['listtype'] or args['type'] or args['ls'] or args['t']
	local img = yesno(args['image'] or args['img'] or args['i'], true)
	local nolink = yesno(args['nl'] or args['nolink'], false)
	local noerror = yesno(args['ne'] or args['noerror'] or args['error'] or args['e'] or args['no_error'])
	local ignoreOdds = yesno(args['ignoreodds'], false)
	local liststyle = args['list_style'] or args['liststyle'] or args['style']
	local noImgPad = yesno(args['noimgpad'], false)
	
	return string.pcall(p._resourceList, text, listType, img, nolink, noerror, args, ignoreOdds, noImgPad, liststyle)
end

function p._resourceList(text, listType, img, nolink, noerror, args, ignoreOdds, noImgPad, liststyle)
	
	if text[1] == 'none' then return 'none' end
	
	for i = 1,#text,1 do
		--function stored in Module:Item._resourceDisplay
		text[i] = generateListItem(processResource(text[i], img, nolink, noerror, ignoreOdds, noImgPad), liststyle)
	end
	
	return generateList(text, listType)
end

---------------------------------------------------------------------------------
-- Template:Image List
--
-- Produces a list of items alongside their images
---------------------------------------------------------------------------------
function p.imageList(frame)
	local args = getArgs(frame)
	
	local text = mergeArgsSyntax(args)
	local listType = args['list_type'] or args['listtype'] or args['type'] or args['ls'] or args['t']
	local img = yesno(args['image'] or args['img'] or args['i'], true)
	local nolink = yesno(args['nl'] or args['nolink'], false)
	local noerror = yesno(args['ne'] or args['noerror'] or args['error'] or args['e'] or args['no_error'])
	local ignoreOdds = yesno(args['ignoreodds'], false)
	local liststyle = args['list_style'] or args['liststyle'] or args['style']
	local noImgPad = yesno(args['noimgpad'], false)
	
	return string.pcall(p._imageList, text, listType, img, nolink, noerror, args, ignoreOdds, noImgPad , liststyle)
end
function p._imageList(text, listType, img, nolink, noerror, args, ignoreOdds, noImgPad, liststyle)
	
	if text[1] == 'none' then return 'none' end
	
	for i = 1,#text,1 do
		--function stored in Module:Item._itemDisplay
		text[i] = generateListItem(processItem(text[i], img, nolink, noerror, ignoreOdds, noImgPad), liststyle)
	end
	
	return generateList(text, listType)
end

---------------------------------------------------------------------------------
-- Template:Mob List
--
-- Produces a list of mobs alongsite their sprites.
---------------------------------------------------------------------------------
function p.mobList(frame)
	local args = getArgs(frame)
	
	local text = mergeArgsSyntax(args, 1)
	local listType = args['list_type'] or args['listtype'] or args['type'] or args['ls'] or args['t']
	local noError = args['noerror'] or args['ne'] or args['noerr']
	local liststyle = args['list_style'] or args['liststyle'] or args['style']
	local noImgPad = args['noimgpad']
	
	return p._mobList(text, listType, noError, noImgPad, liststyle)
end

function p._mobList(text, listType, noError, noImgPad, liststyle)
	local addPlainlist = p._plainlist
	for i = 1,#text,1 do
		-- get alterante text to display
		local alt
		text[i] = text[i]:gsub('&amp;', '&')
		if text[i]:match(';') then
			mob, alt = text[i]:match('(.+);(.+)')
		else 
			mob = text[i]
		end
		-- add images
		text[i] = generateListItem(sprite.spriteGenerator('mob', mob, alt, true, noError, noImgPad), liststyle)
	end
	
	return generateList(text, listType)
end

---------------------------------------------------------------------------------
-- Template:NPC List
--
-- Produces a list of NPCs alongsite their sprites.
---------------------------------------------------------------------------------
function p.npcList(frame)
	local args = getArgs(frame)
	
	local text = mergeArgsSyntax(args, 1)
	local listType = args['list_type'] or args['listtype'] or args['type'] or args['ls'] or args['t']
	local noError = args['noerror'] or args['ne'] or args['noerr']
	local liststyle = args['list_style'] or args['liststyle'] or args['style']
	local noImgPad = args['noimgpad']
	
	return p._npcList(text, listType, noError, noImgPad, liststyle)
end

function p._npcList(text, listType, noError, noImgPad, liststyle)
	local addPlainlist = p._plainlist
	listType = listType or 'none'
	
	for i=1,#text,1 do
		-- get alterante text to display
		local alt
		text[i] = text[i]:gsub('&amp;', '&')
		if text[i]:match(';') then
			npc, alt = text[i]:match('(.+);(.+)')
		else 
			npc = text[i]
		end
		-- add images
		text[i] = generateListItem(sprite.spriteGenerator('npc', npc, alt, true, noError, noImgPad), liststyle)
	end
	
	return generateList(text, listType)
end

---------------------------------------------------------------------------------
-- Template:Location List
--
-- Produces a list of locations alongsite their sprites.
---------------------------------------------------------------------------------
function p.locationList(frame)
	local args = getArgs(frame)
	
	local text = mergeArgsSyntax(args, 1)
	local listType = args['list_type'] or args['listtype'] or args['type'] or args['ls'] or args['t']
	local noError = args['noerror'] or args['ne'] or args['noerr']
	local liststyle = args['list_style'] or args['liststyle'] or args['style']
	local noImgPad = args['noimgpad']
	
	return p._locationList(text, listType, noError, noImgPad, liststyle)
end

function p._locationList(text, listType, noError, noImgPad, liststyle)
	local addPlainlist = p._plainlist
	listType = listType or 'none'
	
	local ret = {}
	
	for i, v in ipairs(text) do
		-- get alterante text to display
		local alt
		v = v:gsub('&amp;', '&')
		if v:match('[^%%];') then
			location, alt = v:match('(.+)%s*;%s*(.*)')
		else 
			location = v
		end
		v = v:gsub('%%;', ';')
		if not location:match('catacombs') then
			local result = sprite.spriteGenerator('location', location, alt, true, noError, noImgPad)
			
			-- add images
			if result ~= '' then
				table.push(ret, generateListItem(result or v), liststyle)
			end
		else
			table.push(ret, string.makeLink(alt or location, location))
		end
	end
	
	return generateList(ret, listType)
end

---------------------------------------------------------------------------------
-- Template:Zone List
--
-- Produces a list of locations with their colors as seen in game.
---------------------------------------------------------------------------------
function p.zoneList(frame)
	local args = getArgs(frame)
	
	local text = mergeArgsSyntax(args, 1)
	local listType = args['list_type'] or args['listtype'] or args['type'] or args['ls'] or args['t']
	local liststyle = args['list_style'] or args['liststyle'] or args['style']
	
	return p._zoneList(text, listType, liststyle)
end

function p._zoneList(text, listType, liststyle)
	local addPlainlist = p._plainlist
	listType = listType or 'none'
	
	local ret = {}
	
	for i, v in ipairs(text) do
		-- get alterante text to display
		v = v:gsub('&amp;', '&')
		v = v:gsub('%[%[', ''):gsub('%]%]', '')
		location = v
		v = v:gsub('%%;', ';')
		
		local locationlower = location:lower()
		if not (locationlower:match('catacombs') 
			or locationlower:match('anywhere') 
			or locationlower:match('goblin egg') 
			or locationlower:match('bat firework')
			or locationlower:match('hub island')) then
			
			local result = zone._zone(location)
			
			-- add images
			if result ~= '' then
				table.push(ret, generateListItem(result or v), liststyle)
			end
		else
			table.push(ret, string.makeLink(location, location))
		end
	end
	
	return generateList(ret, listType)
end

---------------------------------------------------------------------------------
-- Template:Stats List
--
-- Produces a list of stats alongsite the amounts.
---------------------------------------------------------------------------------
function p.statsList(frame)
	local args = getArgs(frame)
	
	local text = mergeArgsSyntax(args, 1)
	local short = yesno(args['short'], false)
	local superShort = args['short'] == 'ss'
	local liststyle = args['list_style'] or args['liststyle'] or args['style']
	
	return p._statsList(text, short, superShort, liststyle)
end

function p._statsList(text, short, superShort)
	local addPlainlist = p._plainlist
	local listType = 'none'
	local noError = false
	
	local ret = {}
	
	for i, v in ipairs(text) do
		local success, result = pcall(statname._getStatName, v, nil, short, superShort)
		
		if not success then result = noError and '' or string.error(result) end
		
		-- add stats
		if result ~= '' then
			table.push(ret, generateListItem(result or v), liststyle)
		end
	end
	
	return generateList(ret, listType)
end

---------------------------------------------------------------------------------
-- Template:Gemstone slots
--
-- Produces a list of gemstone slots
---------------------------------------------------------------------------------
function p.gemstoneSlots(frame)
	local args = getArgs(frame)
	
	local list = mergeArgsSyntax(args, 1)
	
	return p._gemstoneSlots(list)
end

function p._gemstoneSlots(list)
	local noError = false, num
	
	-- nil string check needed for DPL
	if not list or not list[1] or list[1] == 'nil' then
		return ''
	end
	
	local ret = {}
	for i, str in ipairs(list) do
		-- seperate out the number
		if str:match('^([%d,%-%?]+%.?[%d,%-]*x?) (.*)') then
			num, str = str:match('^([%d,%-%?]+%.?[%d,%-]*x?) (.*)')
		else
			num = 1
		end
		
		-- If we have multiple of same slot specified by a number in front, duplicate it that many times
		for i = 1,num do
			ret[#ret+1] = gemstone._gemstoneSlot(str)
		end
	end
	
	return string.wrapHtml{ table.concat(ret, ''), 'div', { class='gemstone-slot-list' } }
end

return p
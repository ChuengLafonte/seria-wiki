------------------------------------------------------------
-- Module:Inventory slot
-- Initially taken from: https://minecraft.gamepedia.com/Module:Inventory_slot
------------------------------------------------------------

local p = {}

local getArgs = require('Module:Arguments').getArgs
local loader = require('Module:Loader')

local string, table, yesno, random =
	loader.require('String', 'Table', 'Yesno', 'Random')
local slotAliases = loader.loadData('Inventory slot/Aliases')

local pageName = mw.title.getCurrentTitle().text
local availableFrameParameters = { 'title', 'text', 'num', 'num2', 'link', 'image', 'image_id' }

local function mergeList( parentTable, content )
	if content[1] then
		for _, v in ipairs( content ) do
			parentTable[#parentTable + 1] = v
		end
	else
		parentTable[#parentTable + 1] = content
	end
end

function p.slot( f )
	local args = getArgs(f)
	
	if not args.parsed then
		args[1] = string.trim( args[1] and (args[1]:gsub("(%s)%s+", "%1")) or '' )
	end
	
	local frames
	if args.parsed then
		frames = args[1]
	elseif args[1] ~= '' then
		local randomise = args.class == 'invslot-large' and 'never' or nil
		frames = p.parseFrameText( args[1], randomise, false )
	end
	
	if not frames then
		local body = p.makeBody( args, false )
		return tostring(body:tag('span'):addClass('invslot-item'):done())
	end
	
	local activeFrame = frames.randomise == true and random.number{ #frames } or 1
	local animated = frames and #frames > 1 and (args.display or 'animated') == 'animated'
	local body = p.makeBody( args, animated )
	for index, frame in ipairs( frames ) do
		local item = p.makeItem( frame, index, args )
		body:node( item )
		if index == activeFrame and animated then
			item:addClass( 'animated-active' )
		elseif animated then
			item:addClass( 'nomobile' )
		end
	end
	return tostring( body )
end

function p.makeBody( args, animated )
	local body = mw.html.create( 'span' ):addClass( 'invslot' ):css{ ['vertical-align'] = args.align }
	if animated then
		body:addClass( 'animated' )
	end
	if args.class then
		body:addClass( args.class )
	end
	if args.style then
		body:cssText( args.style )
	end
	return body
end

function p.makeItem( frame, i, args )
	local item = mw.html.create( 'span' ):addClass( 'invslot-item' )
	if args.imgclass then
		item:addClass( args.imgclass )
	end
	if frame.image_id then
		item:attr('data-iid', frame.image_id)
	end
	if frame.name == '' then
		return item
	end
	
	local name = frame.name or ''
	local title = (args.title or frame.title or name)
	local description = (args.text or frame.text or '')
	local n_1 = tonumber(frame.num) or 1
	local n_2 = tonumber(frame.num2)
	local n_str, n_fs, n_r
	local image = args.image or frame.image or nil
	local img
	
	if frame.image_id then
		img = nil
	elseif image and string.anyMatched(image, '%.gif$', '%.webp$', '%.png$', '%.apng$', '%.jpg$', '%.jpeg$') then
		img = image
	else
		img = (image or name) .. '.png'
	end

	local link = args.link or frame.link or ''
	if link == '' then
		link = name
	end
	if link:lower() == 'none' then
		link = nil
	end

	if not (n_1 and n_2 and n_1 ~= n_2) then
		n_2 = nil
	end
	if (n_1 or 0) >= 10000 then
		n_1 = string._formatShortNum(n_1):lower()
	end
	if (n_2 or 0) >= 10000 then
		n_2 = string._formatShortNum(n_2):lower()
	end
	if yesno(args.forcenum) or ((not n_2) and n_1 and n_1 ~= 1) or (n_1 and n_2) then
		local function len(n)
			return n and tostring(n):len() or 0
		end
		if n_1 and n_2 then
			n_1 = tostring(n_1) .. '-'
		end
		local splitLine = n_2 and (len(n_1) + len(n_2) > 4)
		if (len(n_1) > 7) or (len(n_2) > 7) then
			n_fs = 5.4; n_r = 1.2
		elseif (len(n_1) > 6) or (len(n_2) > 6) then
			n_fs = 6.1; n_r = 1.3
		elseif (len(n_1) > 5) or (len(n_2) > 5) then
			n_fs = 7.2; n_r = 1.6
		elseif (len(n_1) > 3) or (len(n_2) > 3) or splitLine then
			n_fs = 9; n_r = 1
		elseif n_2 or splitLine then
			n_fs = 12; n_r = 0
		else
			n_fs = 15; n_r = 0
		end
		n_str = n_2 and (n_1 .. (splitLine and '<br>' or '') .. n_2) or n_1
	end

	local formattedTitle, plainTitle
	if title == '' then
		plainTitle = name
		formattedTitle = name
	elseif title:lower() ~= 'none' then
		formattedTitle = title
		plainTitle = title:gsub('&[0-9a-fk-or]', '')
		if plainTitle == '' then plainTitle = name end
	elseif link then
		if img then formattedTitle = '' else plainTitle = '' end
	end

	if description:lower() == 'none' then description = '' end
	if description and description:match('\n') then
		description = description:gsub('\n', '/')
	end

	item:attr{
		['data-minetip-title'] = formattedTitle and formattedTitle:gsub('"', '&quot;') or nil,
		['data-minetip-text'] = description and description:gsub('"', '&quot;') or nil,
	}
	if img then
		local escapedTitle = ( plainTitle or '' ):gsub( '&', '&#38;' )
		item:addClass( 'invslot-item-image' )
			:wikitext( '[[File:', img, '|32x32px|link=', link or '', '|', escapedTitle, ']]' )
	end
	if n_str then
		local stacksizeElm = item:tag( 'span' )
			:addClass( 'invslot-stacksize' )
			:attr{ title = plainTitle }
		stacksizeElm:css('font-size', n_fs .. 'px'):css('right', (n_r - 2) .. 'px')
		if args.numStyle then
			stacksizeElm:cssText( args.numStyle )
		end
		stacksizeElm:wikitext( n_str )
	end
	
	return item
end

function p.parseFrameText( framesText, randomise )
	local frames = { randomise = randomise }
	framesText = framesText:gsub( '\\;', '%SEMICOLON%' )
	local splitFrames = string.split( string.trim( framesText ), '%s*;%s*' )
	for _, frameText in ipairs( splitFrames ) do
		frameText = frameText:gsub('%SEMICOLON%', ';')
		local frame = p.makeFrame( frameText )
		local newFrame = frame
		local id = frame.name
		local alias = slotAliases[id]
		if alias then
			newFrame = p.combineFrames( alias, frame )
		end
		if frames.randomise == nil and frame.name:match( '^%?' ) then
			frames.randomise = true
		elseif frames.randomise ~= 'never' then
			frames.randomise = false
		end
		mergeList( frames, newFrame )
	end
	return frames
end

function p.combineFrames( aliasFrames, parsedFrame )
	if type( aliasFrames ) == 'string' then
		local expandedFrame = mw.clone( parsedFrame )
		expandedFrame.name = aliasFrames
		return { expandedFrame }
	end
	if aliasFrames.name then
		aliasFrames = { aliasFrames }
	end
	local expandedFrames = {}
	for i, aliasFrame in ipairs( aliasFrames ) do
		local expandedFrame
		if type( aliasFrame ) == 'string' then
			expandedFrame = { name = aliasFrame }
		else
			expandedFrame = table.deepCopy( aliasFrame, true )
		end
		for _, param in ipairs(availableFrameParameters) do
			expandedFrame[param] = parsedFrame[param] or expandedFrame[param]
		end
		expandedFrames[i] = expandedFrame
	end
	return expandedFrames
end

function p.makeFrame( frameText )
	if type(frameText) ~= 'string' then error(type(frameText)) end
	if not frameText:match( '[%[:,]' ) then
		return { name = string.trim(frameText) }
	end
	frameText = frameText:gsub( '%s*([%[%]:,;])%s*', '%1' )
	local frame = {}
	frame.title = frameText:match( '^%[([^%]]+)%]' )
	frame.image = frameText:match( '([^:%]]+):' )
	local nameStart = ( frameText:find( ':' ) or frameText:find( '%]' ) or 0 ) + 1
	if nameStart - 1 == #frameText then nameStart = 1 end
	frame.name = frameText:sub( nameStart, ( frameText:find( '[,%[]', nameStart ) or 0 ) - 1 )
	frame.num = math.floor( frameText:match( ',%s*(%d+)' ) or 1 )
	frame.num2 = math.floor( frameText:match( ',%s*%d+%s*[%-%–]%s*(%d+)%s*' ) or frame.num )
	frame.text = frameText:match( '%[([^%]]+)%]$' )
	if frame.text and frame.text:match('\n') then
		frame.text = frame.text:gsub('\n', '/')
	end
	return frame
end

p.getAlias = p.combineFrames
function p.expandAlias( parsedFrame, alias )
	return p.combineFrames( alias, parsedFrame )
end

function p.stringifyFrame( frame )
	local s = frame.name or frame[1]
	if not s then return '' end
	if frame.num then s = ('%s,%s'):format(s, frame.num) end
	if frame.title then s = ('[%s]%s'):format(frame.title, s) end
	if frame.text then s = ('%s[%s]'):format(s, frame.text) end
	return s
end

function p.stringifyFrames( frames )
	for i, frame in ipairs( frames ) do
		frames[i] = p.stringifyFrame( frame )
	end
	return table.concat( frames, ';' )
end

return p

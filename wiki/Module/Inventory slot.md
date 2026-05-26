------------------------------------------------------------
-- Initially taken from: https://minecraft.gamepedia.com/Module:Inventory_slot
------------------------------------------------------------

local p = {}

local getArgs = require('Module:Arguments').getArgs
local loader = require('Module:Loader')

local string, table, yesno, currency, random, uitext, cache =
	loader.require('String', 'Table', 'Yesno', 'Currency', 'Random', 'UIText', 'Cache')
local slotAliases = loader.loadData('Inventory slot/Aliases')

local getInvslotCache = cache.getInvslotCache
-- local slotAliasesCache = cache.slotAliasesCache
local itemVariantsCache = cache.itemVariantsCache

local pageName = mw.title.getCurrentTitle().text
local availableFrameParameters = { 'title', 'text', 'num', 'num2', 'link', 'image', 'image_id' }

--------------------------------------------------------------------
--	Structure for main slot creation:
--	p.slot()
--	├── p.parseFrameText()
--	│	└── p.combineFrames()
--	│	└── p.makeFrame()
--	└── p.makeItem()
--------------------------------------------------------------------

--[[Merges a list, or inserts a string
	or table into a table
--]]
local function mergeList( parentTable, content )
	if content[1] then
		-- Merge list into table
		for _, v in ipairs( content ) do
			parentTable[#parentTable + 1] = v
		end
	else
		-- Add strings or tables to table
		parentTable[#parentTable + 1] = content
	end
end

-- Main entry point
function p.slot( f )
	local args = getArgs(f)
	
	if not args.parsed then
		args[1] = string.trim( args[1] and (args[1]:gsub("(%s)%s+", "%1")) or '' )
	end
	
	-- Prepare List of "Frames"
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
	
	-- Create Slot Item for Each "Frame"
	if args.display == 'grid' or args.display == 'inline-grid' then -- display: grid
		local inline = args.display == 'inline-grid'
		local grid = mw.html.create('div'):addClass(inline and '' or ' mcui-centered')
		local row
		local gridcol = tonumber(args.grid_columns) or 6
		if gridcol < 1 then
			row = mw.html.create('div'):addClass('mcui-row')
			grid:node( row )
			for index, frame in ipairs( frames ) do
				local body = p.makeBody( args, animated )
				local item = p.makeItem( frame, index, args )
				body:node( item )
				row:node( body )
			end
		else
			for index, frame in ipairs( frames ) do
				if gridcol == 1 or index % gridcol == 1 then
					-- new row
					row = mw.html.create('div'):addClass('mcui-row')
					grid:node( row )
				end
				local body = p.makeBody( args, animated )
				local item = p.makeItem( frame, index, args )
				body:node( item )
				row:node( body )
			end
		end
		return tostring( grid )
	else -- display: animated
		local activeFrame = frames.randomise == true and random.number{ #frames } or 1
		local animated = frames and #frames > 1 and (args.display or 'animated') == 'animated'
		local body = p.makeBody( args, animated )
		for index, frame in ipairs( frames ) do
			local item = p.makeItem( frame, index, args )
			body:node( item )
			if index == activeFrame and animated then
				item:addClass( 'animated-active' )
			elseif animated then
				-- CUSTOM: "nomobile" class is needed to hide it on mobile (since Fandom doesn't allow JS on mobile)
				item:addClass( 'nomobile' )
			end
		end
		return tostring( body )
	end
end

--[[Creates the HTML for a single Top-level Slot Element
--]]
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

--[[Creates the HTML for a single Slot Item
--]]
function p.makeItem( frame, i, args )
	-- Initialize Element
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
	
	local category
	local name = frame.name or ''
	-- Top-level inheritance handling (args inherits item)
	local rp_title = (frame.title or ''):gsub('%%', '%%%%')
	local rp_description = (frame.text or ''):gsub('%%', '%%%%')
	local title = (args.title or '%inherit%'):gsub('%%inherit%%', rp_title)
	local description = (args.text or '%inherit%'):gsub('%%inherit%%', rp_description)
	local n_1 = tonumber(frame.num) or 1
	local n_2 = tonumber(frame.num2)
	local n_str, n_fs, n_r
	local image = args.image or frame.image or nil
	local img
	
	-- Handle Image
	if frame.image_id then -- has CSS handled image ID: don't display image
		img = nil
	elseif image and string.anyMatched(image, '%.gif$', '%.webp$', '%.png$', '%.apng$', '%.jpg$', '%.jpeg$') then
		img = image
	else
		if pageExists('File:' .. (image or name) .. '.gif') then
			img = (image or name) .. '.gif'
		else 
			img = (image or name) .. '.png'
		end
	end
	-- Handle Link
	local link = args.link or frame.link or ''
	if link == '' then
		link = name
	end
	if link:lower() == 'none' then
		link = nil
	else
		-- (Handle Link Redirects)
		local rtName = mw.title.makeTitle(0, link or '') or false
		rtName = rtName and rtName.redirectTarget and rtName.redirectTarget.text or false
		local unfragmentedLink = (link or ''):gsub('^(.-)#.-$', '%1')
		if unfragmentedLink == pageName or rtName == pageName then
			link = nil
		end
	end
	-- Handle Numbers
	if not (n_1 and n_2 and n_1 ~= n_2) then
		-- No second number
		n_2 = nil
	end
	if (n_1 or 0) >= 10000 then
		n_1 = string._formatShortNum(n_1):lower()
	end
	if (n_2 or 0) >= 10000 then
		n_2 = string._formatShortNum(n_2):lower()
	end
	if yesno(args.forcenum) or ((not n_2) and n_1 and n_1 ~= 1) or (n_1 and n_2) then
		-- Entering condition for displaying numbers (else, n_str undefined)
		local function len(n)
			return n and tostring(n):len() or 0
		end
		if n_1 and n_2 then
			n_1 = tostring(n_1) .. '-'
		end
		local splitLine = n_2 and (len(n_1) + len(n_2) > 4)
		-- Deciding font-size (n_fs) and right (n_r) values
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
		-- Stringify Numbers
		n_str = n_2 and (n_1 .. (splitLine and '<br>' or '') .. n_2) or n_1
	end
	-- Handle Title
	local formattedTitle, plainTitle
	title = uitext.applyReplacements(title)
	if title == '' then
		plainTitle = name
		formattedTitle = name
	elseif title:lower() ~= 'none' then
		formattedTitle = title
		plainTitle = title
		local formatPattern = '&[0-9a-fk-or]'
		if plainTitle:match( formatPattern ) then
			plainTitle = plainTitle:gsub( formatPattern, '' )
		end
		if plainTitle == '' then
			plainTitle = name
		end
	elseif link then
		if img then
			formattedTitle = ''
		else
			plainTitle = ''
		end
	end
	-- Handle Description
	description = uitext.applyReplacements(description)
	if description:lower() == 'none' then description = '' end
	-- (Transform newlines into `/`)
	if description and description:match("\n") then
		description = description:gsub("\n", "/")
	end
	
	-- Now, Prepare Element
	-- Insert Title/Text
	item:attr{
		['data-minetip-title'] = formattedTitle and formattedTitle:gsub('"', '&quot;') or nil,
		['data-minetip-text'] = description and description:gsub('"', '&quot;') or nil,
	}
	-- Insert Image
	if img then
		-- & is re-escaped because mw.html treats attributes
		-- as plain text, but MediaWiki doesn't
		local escapedTitle = ( plainTitle or '' ):gsub( '&', '&#38;' )
		item:addClass( 'invslot-item-image' )
			:wikitext( '[[File:', img, '|32x32px|link=', link or '', '|', escapedTitle, ']]' )
	end
	-- Insert Numbers
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

--[[Parses the frame text into a table of frames,
	expanding aliases, and
	deciding if the slot can be randomised
--]]
function p.parseFrameText( framesText, randomise )
	local frames = { randomise = randomise }
	local expandedAliases
	framesText = framesText:gsub( '\\;', '%%SEMICOLON%%' );-- gsub here allows us to escape ; character
	local splitFrames = string.split( string.trim( framesText ), '%s*;%s*' )
	for _, frameText in ipairs( splitFrames ) do
		frameText = frameText:gsub('%%SEMICOLON%%', ';') -- undo-escape now that semicolon regex check is done
		-- Now, Parse Frame Text
		local frame = p.makeFrame( frameText )
		local newFrame = frame
		local id = frame.name
		local id_trim = frame.name:gsub('^%?', ''):gsub('^%*', '')
		-- Find Frame Alias and Combine With Frame
		local alias, variants
		if frame.name ~= id_trim then
			variants = itemVariantsCache:get(id_trim)
		end
		if variants then
			alias = {}
			for i, v in ipairs(variants) do
				-- local alt = slotAliasesCache:get(v, 1)
				local alt = slotAliases[v]
				alias[i] = alt and getInvslotCache(alt, 1) or getInvslotCache(v, 1) or v
				-- note: this falls back to the string (v) instead of leaving alias[i] a nil
			end
		else
			-- local alt = slotAliasesCache:get(id, 1)
			local alt = slotAliases[id]
			alias = alt and getInvslotCache(alt, 1) or getInvslotCache(id, 1)
		end
		if alias then
			newFrame = p.combineFrames( alias, frame )
		end
		
		-- Randomise starting frame for "Any *" aliases, as long as the alias is the only frame
		if frames.randomise == nil and frame.name:match( '^%?' ) then
			frames.randomise = true
		elseif frames.randomise ~= 'never' then
			frames.randomise = false
		end
		
		mergeList( frames, newFrame )
	end
	
	return frames
end

--[[Returns a new table with the parsed frame values
	added to alias frames (parsed frame overrides alias frames)
--]]
function p.combineFrames( aliasFrames, parsedFrame )
	-- If alias is just a name, return the parsed frame with the new name
	if type( aliasFrames ) == 'string' then
		local expandedFrame = mw.clone( parsedFrame )
		expandedFrame.name = aliasFrames
		return { expandedFrame }
	end
	-- Single frame alias, put in list
	if aliasFrames.name then
		aliasFrames = { aliasFrames }
	end
	-- Prepare new table, combine frames
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
		-- Lower-level inheritance handling (parsed item inherits alias)
		if aliasFrame.title then
			local rp = aliasFrame.title:gsub('%%', '%%%%')
			expandedFrame.title = (expandedFrame.title or '%inherit%'):gsub('%%inherit%%', rp)
		end
		if aliasFrame.text then
			local rp = aliasFrame.text:gsub('%%', '%%%%')
			expandedFrame.text = (expandedFrame.text or '%inherit%'):gsub('%%inherit%%', rp)
		end
		expandedFrames[i] = expandedFrame
	end
	return expandedFrames
end

--[[Parses frame text into a table
	[<Title>]<image>:<item>,<count>[<description>]
-]]
function p.makeFrame( frameText )
	local function forwardSubstitute(text)
		return text:gsub( '\\\\', '%%BACKSLASH%%' ):gsub( '\\%[', '%%SQBRACL%%' ):gsub( '\\%]', '%%SQBRACR%%' ):gsub( '\\:', '%%COLON%%' ):gsub( '\\,', '%%COMMA%%' )
	end
	local function backSubstitute(text)
		return text:gsub('%%BACKSLASH%%','\\'):gsub('%%SQBRACL%%','['):gsub('%%SQBRACR%%',']'):gsub('%%COLON%%',':'):gsub('%%COMMA%%',',')
	end
	local c = currency._newCurrencySlot( frameText )
	if c then return c end
	-- Simple frame with no parts
	if type(frameText) ~= 'string' then error(type(frameText)) end
	-- [ESC] allow escaping special characters - we'll convert normal character after we parse
	frameText = forwardSubstitute(frameText)
	
	if not frameText:match( '[%[:,]' ) then
		frameText = backSubstitute(frameText)
		return {
			name = string.trim(frameText),
		}
	end
	frameText = frameText:gsub( '%s*([%[%]:,;])%s*', '%1' )
	
	local frame = {}
	frame.title = frameText:match( '^%[([^%]]+)%]' )
	frame.image = frameText:match( '([^:%]]+):' )
	
	local nameStart = ( frameText:find( ':' ) or frameText:find( '%]' ) or 0 ) + 1
	if nameStart - 1 == #frameText then
		nameStart = 1
	end
	frame.name = frameText:sub( nameStart, ( frameText:find( '[,%[]', nameStart ) or 0 ) - 1 )
	
	-- Handle m-n syntax
	frame.num = math.floor( frameText:match( ',%s*(%d+)' ) or 1 )
	frame.num2 = math.floor( frameText:match( ',%s*%d+%s*[%-%–]%s*(%d+)%s*' ) or frame.num )
	frame.text = frameText:match( '%[([^%]]+)%]$' )
	
	-- [/ESC] un-replace the characters we used for escaped characters earlier
	if frame.title then frame.title = backSubstitute(frame.title) end
	if frame.name then frame.name = backSubstitute(frame.name) end
	if frame.text then frame.text = backSubstitute(frame.text) end
	
	-- Transform newlines into `/`
	if frame.text and frame.text:match("\n") then
		frame.text = frame.text:gsub("\n", "/")	
	end
	
	return frame
end

-------------------------------------
-- Other Features
-------------------------------------

p.getAlias = p.combineFrames
function p.expandAlias( parsedFrame, alias )
	return p.combineFrames( alias, parsedFrame )
end

-- create [%s]%s,%s[%s] and escape symbols
function p.stringifyFrame( frame )
	local function escape(s)
		return s:gsub( '\\', '\\\\' ):gsub( '([%[%]:,;])', '\\%1' )
	end
	local s = frame.name or frame[1]
	if not s then
		return ''
	end
	s = escape(s)
	if frame.num then
		s = ('%s,%s'):format(s, escape(frame.num))
	end
	if frame.title then
		s = ('[%s]%s'):format(escape(frame.title), s)
	end
	if frame.text then
		s = ('%s[%s]'):format(s, escape(frame.text))
	end
	return s
end

function p.stringifyFrames( frames )
	for i, frame in ipairs( frames ) do
		frames[i] = p.stringifyFrame( frame )
	end
	return table.concat( frames, ';' )
end

return p

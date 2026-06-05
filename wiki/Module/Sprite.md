--<pre>
local p = {}

local loader = require('Module:Loader')
local getArgs = require('Module:Arguments').getArgs
local string, yesno, lu = loader.require('String', 'Yesno', 'LibU')
local _1, _2, _3, _4, _5, _6 =
	loader.loadData('Mob/Sprites', 'NPC/Sprites', 'Location/Sprites', 'Mob/Aliases', 'NPC/Aliases', 'Location/Aliases')

local pageName = mw.title.getCurrentTitle().text
local spritesList = {
	mob = _1,
	npc = _2,
	location = _3,
}
local aliasesList = {
	mob = _4,
	npc = _5,
	location = _6,
}

function p.spriteGenerator(mode, key, alt, showName, noErr, noImagePadding, noLink)
	local sprites, aliases = spritesList[mode], aliasesList[mode]
	local spr, img, exist
	local untouchedKey = key
	showName = yesno(showName, true)
	showImage = yesno(showImage, true)
	noErr = yesno(noErr, true)
	noImagePadding = yesno(noImagePadding, false)
	noLink = yesno(noLink, false)
	local getSprite = {
		mob = function()
			return sprites.mobs[key:lower()] or sprites.sea_creatures[key:lower()] or sprites.slayer_mobs[key:lower()] or sprites.passive_mobs[key:lower()] or sprites.dungeon_mobs[key:lower()] or sprites.dungeon_bosses[key:lower()] or sprites.dungeon_boss_mobs[key:lower()] or sprites.dungeon_watcher_mobs[key:lower()] or sprites.spooky_festival_mobs[key:lower()]
		end,
		npc = function()
			return sprites[key:lower()]
		end,
		location = function()
			return sprites[key:lower()]
		end,
	}
	local function _getLink(link)
		local rtName = mw.title.makeTitle(0, link or '') or false
		rtName = rtName and rtName.redirectTarget and rtName.redirectTarget.text or false
		local unfragmentedLink = (link or ''):gsub('^(.-)#.-$', '%1')
		if not (unfragmentedLink == pageName or rtName == pageName or link == 'none') then
			return link
		end -- else return nil
	end
	local function _getImage(img_, ext_, key_, nip, noLink_, link_)
		local imgexist = lu.pageExists(('File:%s Sprite.%s'):format(img_, ext_ or 'png'))
		return imgexist and string.makeImage({ img_, ' Sprite' }, { ext=ext_, size=16, link=((noLink_ or not link_) and '' or link_) })
			or ( nip and ''
				or string.makeImage('Blank Icon', { ext='png', size=16, link='' })
			)
	end
	local specialHandlers = {
		-- 1: returns a value to be returned; else return nothing
		{
			location = function()
				if key:lower():match('[Cc]atacombs?') then
					return table.concat{'[[', alt or key, '|', key, ']]'}
				else return
				end
			end
		},
	}
	local function specialHandler(n)
		local handle_ = specialHandlers[n][mode]
		return handle_ and handle_() or nil
	end
	-- check for errors
	lu.assertTrue(key, 'No sprite '..string.ucfirst(mode)..' provided', 2)
	-- leave only text
	-- local pttn = '[^%a%s;%-% \'"%.,]' -- (whitelist pattern)
	local pttn = '[%[%]|]' --(blacklist pattern)
	if key:find(pttn) then key = key:gsub(pttn, '') end
	-- alternate text
	img, exist = key, false
	if key:find(';') then 
		local str_storage = mw.text.split(key, ';') 
		key, alt = str_storage[1], str_storage[2]
		img = key
	end
	orig_key = key
	-- go through sprites and apply correct image
	key = aliases[key:lower()] or key
	local handle = specialHandler(1, mode)
	if handle and handle.action == 'return' then return handle.value end
	if orig_key:lower():find("^mayor ") ~= nil then
		alt = alt or key:gsub("^Candidate ", "Mayor ")
	else
		alt = alt or key
	end
	alt = alt or key
	spr = getSprite[mode]()
	if spr then
		exist = true
		if type(spr) == 'table' then
			img, ext = spr[1], sprites.format or 'png'
		else
			img, ext = spr, 'png'
		end
	else
		if not noErr then
			formattedError('Invalid %s name: %q', 2, string.ucfirst(mode), key)
		end
	end
	local link = _getLink(key)
	local function categoryName(mode)
		local capitalizations = {npc='NPC', mob='Mob', location='Location'}
		return capitalizations[mode]
	end
	return table.concat{
		'<span style="white-space: nowrap">',
		_getImage(img, ext, key, noImagePadding, noLink, link),
		showName and (' ' .. ((noLink or not link) and (alt or key) or string.makeLink(key, alt))) or '',
		exist and '' or '[[Category:Unknown ' .. categoryName(mode) .. ' Referenced]]',
		'</span>',
	}
end

------------------------------------------------------------------------------
-- Template:MobSprite
--
-- Creates a link to a mob with an option for sprites and images
------------------------------------------------------------------------------
function p.mobSprite(frame)
	local args = getArgs(frame)
	
	local mob = args[1]
	local showName = args[2] or args.showName or args.show_name or args.sn
	local alt = args.alt
	local noErr = args.noerr or args.noe
	local noImgPad = args.noimgpad
	local noLink = args.nolink or args.nl
	
	return p._mobSprite(mob, alt, showName, noErr, noImgPad, noLink)
end

p._mobSprite = lu.bind(p.spriteGenerator, 'mob')

------------------------------------------------------------------------------
-- Template:NPCSprite
--
-- Creates a link to an NPC with an option for sprites and images
------------------------------------------------------------------------------
function p.npcSprite(frame)
	local args = getArgs(frame)
	
	local npc = args[1]
	local showName = args[2] or args.showName or args.show_name or args.sn
	local noErr = args.noerr or args.noe
	local alt = args.alt
	local noImgPad = args.noimgpad
	local noLink = args.nolink or args.nl
	
	return p._npcSprite(npc, alt, showName, noErr, noImgPad, noLink)
end

p._npcSprite = lu.bind(p.spriteGenerator, 'npc')

------------------------------------------------------------------------------
-- Template:LocationSprite
--
-- Creates a link to a location with an option for sprites and images
------------------------------------------------------------------------------
function p.locationSprite(frame)
	local args = getArgs(frame)
	
	local location = args[1]
	local showName = args[2] or args.showName or args.show_name or args.sn
	local noErr = args.noerr or args.noe
	local alt = args.alt
	local noImgPad = args.noimgpad
	local noLink = args.nolink or args.nl
	
	return p._locationSprite(location, alt, showName, noErr, noImgPad, noLink)
end

p._locationSprite = lu.bind(p.spriteGenerator, 'location')

--Finish Module
return p
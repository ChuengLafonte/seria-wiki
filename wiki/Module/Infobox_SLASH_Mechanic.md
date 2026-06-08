-- Get Required Modules
local loader = require('Module:Loader')

local string, table, yesno, arguments, statname, Infobox, inventorySlot, templates, minimap, animate, sprite, mayor =
	loader.lazy.require('String', 'Table', 'Yesno', 'Arguments', 'Statname', 'Infobox', 'Inventory slot', 'String/Templates', 'Minimap', 'Animate', 'Sprite', 'Mayor')
local iData = loader.lazy.loadData('Infobox/Data')

local getArgs = arguments.getArgs
local curTitle = mw.title.getCurrentTitle()

-- Begin Exports
local p = {}
local yesIcon, noIcon, unknownIcon = templates.yes(1), templates.no(1), templates.unknown(1)
local aprilFools = false

local function yesnodefault(val, yes, no, def)
	if tostring(val):sub(1, 1):lower() == 'u' then
		return unknownIcon
	end
	
	local bool = yesno(val);
	if bool == nil then return def or val
	elseif bool then return yes
	else return no
	end
end

local function yesnoIcon(val, def)
	return yesnodefault(val, yesIcon, noIcon, def)
end

local function additergroup(pref, sdata, parent)
	for count = 1,iData.MAX_INDEX,1 do
		local desc, name = (pref..'%d_desc'):format(count), (pref..'%d_name'):format(count)
		parent:addData{ sdata[desc], label = sdata[name] }
	end
end

local function argNormalize(tb)
	-- Simple replacement functions for the whole table
	local ret = {}
	for oldkey, v in pairs(tb) do
		local key = oldkey:gsub('[{}]', '')
		ret[key] = v
	end
	
	return ret
end


function p.infoboxCreate(frame)
	local args = getArgs(frame)
	
	return (frame.getParent and frame:getParent() or mw.getCurrentFrame()):preprocess(p._infoboxCreate(args))
end

function p._infoboxCreate(args)
	local deftype = args.default_type
	
	-- All checkings
	local isNPC, isMayor, isQuest, isPuzzle, isStat, isMinion, isLocation, isMob
	do
		local function checkval(v)
			return (deftype or ''):lower():match(v) and true or false
		end
		isNPC = checkval('npc') or checkval('character') or checkval('mayor')
		isMayor = checkval('mayor')
		isQuest = checkval('quest')
		isPuzzle = checkval('puzzle')
		isStat = checkval('stat')
		isMinion = checkval('minion')
		isLocation = checkval('location')
		isMob = checkval('mob') or checkval('creature')
		isSeaCreature = checkval('creature')
	end
	local minimalist = (isQuest or isPuzzle) and true
	
	local pagename = curTitle.text or 'Diamond'
	local title = args.title
	local isValidMayor = isMayor and mayor.isValidMayor(title or pagename)
	if isValidMayor then
		title = mayor.getMayorLink(title or pagename)
	elseif not title then
		title = ((not minimalist) and pagename or nil)
		isValidMayor = isMayor and mayor.isValidMayor(title)
		if isNPC then
			local status, sprite = pcall(function() return sprite._npcSprite(title, nil, false, nil, nil, nil, true) end)
			if status and sprite then
				title = sprite .. ' ' .. title
			end
		end
	end
	local category_to_add = args.category_to_add
	local onmain = curTitle.namespace == 0
	
	local sections = {}
	local location_sections = {}
	for j = 1,iData.MAX_TAB,1 do
		local function argJ(name, default)
			return args[name..j] or default
		end
		
		-- section one does have numbers after params; on 2+ do that
		local i = j == 1 and '' or j
		local _i = j == 1 and '' or '_'..j -- needed for when a param ends in a number naturally
		
		local function argI(name, default)
			return args[name..((type(name) == 'string' and name:match('%d$')) and _i or i)] or default
		end
		
		-- Look up an argument in any of formats supported by argI and argJ
		-- If not found, return default
		-- Generally, every tab-specific argument should use this, to ensure consistent synonymity of
		-- arguments such as 'arg1' and 'arg'. (arguments global to whole infobox (not tab-specific) should stay as 'arg')
		--
		-- TODO: Remove argJ and argI altogether and move their logic inside for simplification - they don't seem to be needed as separate functions
		local function argK(name, default)
			return argI(name) or argJ(name) or default
		end
		
		local sectionExists = j == 1 or argJ('tab')
		if sectionExists then
			-- table of all params for this section
			local s = {}
			
			local function additerdata(pref)
				for count = 1,iData.MAX_INDEX,1 do
					local desc, name = (pref..'%d_desc'):format(count), (pref..'%d_name'):format(count)
					s[desc] = argK(desc)
					s[name] = argK(name) or ('%s %d'):format(string.ucfirst(pref), count)
				end
			end
			
			-- Top level infobox values
			--[[0]]
			s.tab = argK('tab')
			--[[0.5]]
			s.tab_title = argK('tab_title')
			
			local tabPage = argK('tab_page') or pagename -- page to get images/slots from
			
			--[[1|2]]
			s.caption = argK('caption') or argK('imagecaption')
			s.image_gallery = (argK('image') and argK('image'):match('UNIQ%-%-gallery')) and argK('image') or nil
			if not s.image_gallery and (argK('image') or not (minimalist or isStat or isMinion)) then
				if aprilFools and isNPC then
					s.image = (argK('image') or tabPage..'.png') .. ';Jerry Fan.png'
				end
				s.image = string.wrapTag(animate.animate({ s.image or argK('image') or tabPage..'.png', class = 'pi-image-thumbnail', caption = s.caption }), 'center')
			end
			if not s.image_gallery and not s.image and isMinion then
				s.image_gallery = string.dedent([[<gallery>
				%s.png|Pose
				%s I.png|Head
				</gallery>]]):format(tabPage, tabPage)
			end
			if s.image_gallery and s.caption then
				s.caption = string.wrapHtml(s.caption, 'div', { class = 'pi-item-spacing pi-caption' })
			end
			
			--[[3]]
			s.slot_item = argK('slot_item') or argK('slot')
			if not s.slot_item and isValidMayor then
				-- For mayors, 2 slots are created: one showing them in election UI, one in mayor UI, like once they are elected.
				
				-- Since mayor.createTooltip returns a raw table of slot parameters, (rather than a simple string)
				-- 'parsed=true' is needed in inventorySlot.slot to make it use such input
				s.slot_item = string.wrapHtml(
						inventorySlot.slot{{mayor.createTooltip(args.title or tabPage, nil, true)}, parsed=true}..
						inventorySlot.slot{{mayor.createTooltip(args.title or tabPage, nil, false)}, parsed=true},
					'center')
			else
				if isMinion then
					s.slot_item = s.slot_item or ('*' .. tabPage)
				end
				s.slot_item = yesno(s.slot_item, false) and (s.slot_item or tabPage) or s.slot_item
				s.slot_item = s.slot_item and string.wrapHtml(not s.slot_item:match('<%a-(.-)>(.-)</%a->') and inventorySlot.slot{
					s.slot_item,
					text = argK('slot_text') or nil,
					title = argK('slot_title') or nil,
					link = argK('slot_link') or (not onmain and 'none' or nil),
					display = 'inline-grid'
				} or s.slot_item, 'center')
			end
			
			--[[4]]
			s.aka = argK('aka')
			--[[5]]
			s.type = argK('type') or ((not minimalist) and deftype or nil)
			--[[6]]
			s.color = argK('color')
			
			--[[7]]
			s.appearance = argK('appearance')
			--[[8]]
			s.collection = argK('collection') and ('{{CollectionLink|showIcon=y|%s}}'):format(argK('collection'))
			--[[9]]
			s.usage = argK('usage')
			
			--[[10]]
			s.uses = argK('uses')
			--[[11]]
			s.ways_to_increase = argK('ways_to_increase')
			--[[12]]
			s.ways_to_decrease = argK('ways_to_decrease')
			
			--[[13]]
			s.category = argK('category')
			--[[14]]
			s.collects = argK('collects') and ('{{Resource List|image=1|%s}}'):format(argK('collects'))
			--[[15]]
			s.upgrade_with = argK('upgrade_with') and ('{{Image List|%s}}'):format(argK('upgrade_with'))
			
			--[[16]]
			s.travel_scroll = argK('travel_scroll')
			--[[17]]
			s.level = argK('level')
			--[[18]]
			s.sublocations = argK('sublocations') and ('{{Zone List|%s|noerror=true|noimgpad=true}}'):format(argK('sublocations'))
			--[[19]]
			s.fairy_souls = argK('fairy_souls')
			--[[20]]
			s.enigma_souls = argK('enigma_souls')
			
			--[[21]]
			s.election_wins = argK('election_wins') or isValidMayor and mayor.getWins{ args.title or tabPage } .. ' <sup>[Based on existing [[Mayor_Election/Events|data]]]</sup>' or nil
			
			--[[22]]
			s.amount = argK('amount')
			
			-- Dungeon Information group
			--[[A0]]
			s.dungeon = argK('dungeon')
			--[[A1]]
			s.floor = argK('floor')
			--[[A2]]
			s.boss = argK('boss')
			--[[A3]]
			s.status = argK('status')
			--[[A4]]
			s.dungeon_size = argK('dungeon_size')
			--[[A5]]
			s.party_size = argK('party_size')
			--[[A6]]
			s.required_combat_level = argK('required_combat_level')
			--[[A7]]
			s.required_catacombs_level = argK('required_catacombs_level')
			--[[A8]]
			s.reqs = argK('reqs')
			--[[A9]]
			s.base_xp = argK('base_xp')
			--[[A10]]
			s.failable = yesnoIcon(argK('failable'))
			
			-- Mob Information group
			--[[B0]]
			s.mob_level = argK('mob_level')
			--[[B1]]
			s.damage_deals = argK('damage_deals')
			--[[B2]]
			s.damage_rift = argK('rift_damage') and ('{{stat|rt|%s}}'):format(argK('rift_damage')) 
			--[[B3]]
			s.damage_resistance = argK('damage_resistance')
			--[[B4]]
			s.spawn_location = argK('spawn_location') and ('{{Zone List|%s|noerror=true|noimgpad=true}}'):format(argK('spawn_location'))
			--[[B5]]
			s.spawn_condition = argK('spawn_condition')
			--[[B6]]
			s.special = argK('special')
			--[[B7]]
			s.special_behavior = argK('special_behavior')
			--[[B8]]
			s.mob_type = argK('mob_type')
			if isMob and not argK('mob_type') then
				s.mob_type = '[[Category:Mobs with no mob type specified]]'
			end
			
			--[[B9]]
			s.entity_type = argK('entity_type')
			--[[B10]]
			local ee = argK('effective_enchant')
			s.effective_enchant = ee and (
				(ee == 'none' or ee == 'no' or ee == 'n') and 'None'
				or ('{{Ench|%s}}'):format(ee)
			)
			
			-- Quest group
			--[[C0]]
			s.requirements = argK('requirements') or argK('requirement')
			--[[C1]]
			s.rewards = argK('rewards') or argK('reward')
			
			-- Stats group
			--[[D0]]
			s.stats = argK('stats')
			--[[D1+]]
			table.each(table.values(iData.allstats), function(v)
				local ln = v[1]
				s[ln] = argK(ln)
			end)
			
			-- Perks group
			--[[E0+]]
			additerdata('perk')
			if isValidMayor then
				for i, v in ipairs(mayor._mayorPerksTable(args.title or tabPage, true)) do
					local desc, name = ('perk%d_desc'):format(i), ('perk%d_name'):format(i)
					if v[2] and not s[desc] then
						s[desc] = v[2]
						s[name] = v[1] and string.gsub(v[1], '^%[%[(.*)%]%]*%]$', '[[%1|\'\'\'%1\'\'\']]') or s[name]
					end
				end
			end
			
			-- Capacity group
			--[[F0]]
			s.default_desc = argK('default_desc')
			s.default_name = argK('default_name') or 'Default'
			--[[F1+]]
			additerdata('upgrade')
			
			-- Inhabitants group
			--[[H0]]
			s.npcs = argK('npcs') and ('{{NPC List|noerr=1|%s}}'):format(argK('npcs'))
			--[[H1]]
			s.mobs = argK('mobs') and ('{{MobList|noerr=1|%s}}'):format(argK('mobs'))
			
			-- Resources group
			--[[I0]]
			s.drops = argK('drops') and string.wrapHtml(
				('{{Image List|image=1|noerror=1|%s}}'):format(argK('drops')),
				'div', { style = 'text-align:left;' }
			)
			--[[I1]]
			s.resources = argK('resources') and string.wrapHtml(
				('{{Image List|noerror=1|%s}}'):format(argK('resources')),
				'div', { style = 'text-align:left;' }
			)
			
			-- Drops group
			--[[R0]]
			s.mob_drops = argK('mob_drops') and ('{{Resource List|image=1|noerror=1|%s}}'):format(argK('mob_drops'))
			--[[R1]]
			s.xp = argK('xp') and ('{{Skill XP|%s}}'):format(argK('xp'))
			--[[R2]]
			s.gins = argK('gins') and ('{{C|%s}}'):format(argK('gins'))
			--[[R3]]
			s.experience = argK('exp') or argK('experience') or argK('experience_orbs')
			--[[R4]]
			s.essence = argK('essence') and ('{{Resource Display|image=1|noerror=1|%s}}'):format(argK('essence'))
			--[[R5]]
			s.attribute_shard = argK('attribute_shard') and ('{{Item Display|image=1|noerror=1|%s}}'):format(argK('attribute_shard'))
			
			-- Values group
			--[[J0]]
			s.base_value = argK('base_value')
			--[[J1]]
			s.max_value = argK('max_value')
			--[[J2]]
			s.min_value = argK('min_value')
			
			-- Properties group
			--[[K0]]
			s.unlock_requirement = argK('unlock_requirement')
			--[[K1]]
			s.max_level = argK('max_level')
			
			-- Special Effects group
			--[[L0]]
			s.skill_special_effect = argK('skill_special_effect')
			
			-- Upgrades group
			local disable_upgrades = yesno(argK('disable_upgrades'), false)
			--[[M0]]
			s.super_compactor = (isMinion and not disable_upgrades) and yesnoIcon(argK('super_compactor') or true) or nil
			--[[M1]]
			s.compactor = (isMinion and not disable_upgrades) and yesnoIcon(argK('compactor')) or nil
			--[[M2]]
			s.auto_smelter = (isMinion and not disable_upgrades) and yesnoIcon(argK('auto_smelter')) or nil
			
			-- Player Interactions group
			--[[N0]]
			s.quests = argK('quests')
			--[[N1]]
			s.shop = yesnoIcon(argK('shop') or isMayor and 'n' or nil)
			
			-- Next Event
			local skydate_start, skydate_end = argK('skydate_start') or argK('skydate_begin'), argK('skydate_end')
			if skydate_start then
				--[[S0]]
				s.datetime = string.wrapHtml('', 'span', {
					class = 'skydate-timestamp',
					['data-skydate'] = skydate_start,
				})
				--[[S1]]
				skydate_end = skydate_end or skydate_start
				skydate_end = skydate_end .. (skydate_end:match(',') and '' or ', 23:59')
				s.countdown = string.wrapHtml('', 'span', {
					class = 'skydate-countdown',
					['data-skydate-start'] = skydate_start,
					['data-skydate-end'] = skydate_end,
				})
			end
			
			-- Item Metadata
			-- [[Q0]]
			s.id = argK('item_id') or argK('id')
			if s.id then
				-- Always show ID in all caps
				s.id = string.wrapTag(s.id:upper(), 'code')
				-- If array syntax, make a list
				s.id = s.id:gsub(' ', '') -- lazy trim for array; ids never naturally have spaces
				s.id = table.concat(mw.text.split(s.id, ','), '<br />')
			end
			
			-- Symbol
			-- [[T0]]
			s.symbol = argK('symbol')
			-- [[T1]]
			s.unicode = argK('unicode')
			-- [[T2]]
			s.icon = argK('icon')
			
			
			-- Sea Creature Properties
			-- [[U0]]
			s.sc_weight = argK('sc_weight')
			-- [[U1]]
			s.sc_location = argK('sc_location') or argK('sc_spawn_location')
			-- [[U2]]
			if isSeaCreature then
				local sc_type = argK('sc_type')
				local sc_type_text = ''
				if not sc_type then
					sc_type_text = '[[File:Water Bucket.png|16px]] [[Sea_Creatures#Water|Water]]'
				else
					if (sc_type:lower():find("water")) then
						sc_type_text = sc_type_text .. '[[File:Water Bucket.png|16px]] [[Sea_Creatures#Water|Water]]\n'
					end
					if (sc_type:lower():find("lava")) then
						sc_type_text = sc_type_text .. '[[File:Lava Bucket.png|16px]] [[Sea_Creatures#Lava|Lava]]'
					end
				end
				s.sc_type = sc_type_text
			end
			-- [[U3]]
			s.sc_fishing_req = argK('sc_fishing_req') and ('{{Skill|fishing|%s}}'):format(argK('sc_fishing_req'))
			-- [[U4]]
			s.sc_hotspot = argK('sc_hotspot') and yesnoIcon(argK('sc_hotspot'))
			-- [[U5]]
			s.sc_bait = argK('sc_bait') and ('{{Resource List|image=1|%s}}'):format(argK('sc_bait'))
			-- [[U6]]
			s.sc_hunter = argK('sc_trophy_hunter')
			-- [[U7]]
			s.sc_time_req = argK('sc_time_req')
			-- [[U8]]
			s.sc_event_req = argK('sc_event_req')
			-- [[U9]]
			s.sc_other_req = argK('sc_other_req') and yesnoIcon(argK('sc_other_req'))
			
			-- Push section data into array
			sections[#sections+1] = s
		end
		
		-- Location/Minimap data
		local l = {}
		if not argK('location') and isMayor then
			if j == 1 then
				l.minimap = minimap.getMinimapForInfobox{ 'Community Center', x = 7, z = -110 }
				location_sections[#location_sections+1] = l
			end
		elseif argK('x') or argK('coordinates') or argK('minimap') or argK('start_location') or argK('start_npc') or argK('prev_location') or argK('next_location') then
			-- Location group
			--[[G0]]
			l.xyz = argK('x') and ('<tr><td>%s</td><td>%s</td><td>%s</td></tr>'):format(argK('x'), argK('y') or '', argK('z') or '')
			l.xyz = l.xyz and string.wrapHtml(l.xyz, 'table', { style = 'width:100%; table-layout:fixed; text-align:center;' })
			--[[G1]]
			l.coordinates = argK('coordinates')
			--[[G2]]
			do
				local loc, guide = argK('location'), argK('location_guide')
				if loc then 
					if isNPC then
						loc = ('{{Zone List|%s|noerror=true|noimgpad=true}}'):format(loc)
					elseif not loc:match('%[%[') then 
						loc = '[[' .. loc .. ']]'
					end
				end
				
				l.location = (loc and guide) and (loc .. '<br>' .. guide) or (loc or guide)
			end
			--[[G3]]
			l.start_location = argK('start_location') and ('{{Zone List|%s|noerror=true|noimgpad=true}}'):format(argK('start_location'))
			--[[G4]]
			l.start_npc = argK('start_npc') and ('{{NPC List|{{{start_npc}}}}}'):format(argK('start_npc'))
			--[[G5]]
			l.prev_location = argK('prev_location')
				or (argK('next_location') and 'None')
			--[[G6]]
			l.next_location = argK('next_location')
				or (argK('prev_location') and 'None')
			
			if isNPC then
				l.minimap = minimap.getMinimapForInfobox{ location = argK('location'), minimap_location = argK('minimap_location'), x = argK('x'), z = argK('z') }
			end
			
			location_sections[#location_sections+1] = l	
		end
	end
	
	-- Make infobox
	local ibox = Infobox()
	ibox:addTitle{ title }
	
	local function add_location_section(section, ldata, minimalist, collapsed)
		section:addGroup{ header = (not minimalist) and 'Location' or '', collapse = collapsed and 'open' or '' }
				--[[G0 ]]:addData{ ldata.xyz, label = string.wrapHtml('Coordinates', 'span', { style = 'white-space:nowrap; vertical-align: middle;' })}
				
				--[[G1 ]]:addData{ ldata.coordinates, label = 'Coordinates' }
				--[[G2 ]]:addData{ ldata.location, label = 'Location' }
				
				--[[G3 ]]:addData{ ldata.start_location, label = 'Start Location' }
				--[[G4 ]]:addData{ ldata.start_npc, label = 'Start NPC' }
				:addGroup{ layout = 'horizontal' }
					--[[G5 ]]:addData{ ldata.prev_location, label = '← Previous Location' }
					--[[G6 ]]:addData{ ldata.next_location, label = 'Next Location →' }
				:done()
				:addGroup()
					:addData { ldata.minimap }
				:done()
			:done()
	end
	
	local panel = ibox:addPanel()
	for i, sectionData in ipairs(sections) do
		local sdata = argNormalize(sectionData)
		local ldata = location_sections[i] and argNormalize(location_sections[i]) or {}
		local section = --[[0]]panel:addSection{ label = sdata.tab }
		
		--[[1|2]]
		if sdata.image_gallery then
			-- seems like galleries does not accept caption
			section:addImage{ sdata.image_gallery, --[[caption = { sdata.caption },]] source = 'image'..(i == 1 and '' or i) }
			section:addData{ sdata.caption }
		else
			section:addData{ sdata.image }
		end
		
		section
		--[[3  ]]:addData{ sdata.slot_item }
		--[[4  ]]:addData{ sdata.aka, label = 'Also known as' }
		--[[5  ]]:addData{ sdata.type, label = 'Type' }
		--[[6  ]]:addData{ sdata.color, label = 'Color' }
		
		--[[7  ]]:addData{ sdata.appearance, label = 'Appearance' }
		--[[8  ]]:addData{ sdata.collection, label = 'Collection' }
		--[[9  ]]:addData{ sdata.usage, label = 'Usage' }
		
		--[[10 ]]:addData{ sdata.uses, label = 'Uses' }
		--[[11 ]]:addData{ sdata.ways_to_increase, label = 'Increasing' }
		--[[12 ]]:addData{ sdata.ways_to_decrease, label = 'Decreasing' }
		
		--[[12 ]]:addData{ sdata.category, label = 'Category' }
		--[[13 ]]:addData{ sdata.collects, label = string.makeTitle('Collects', 'Average items collected per action') }
		--[[14 ]]:addData{ sdata.upgrade_with, label = 'Upgrade with' }
		
		--[[15 ]]:addData{ sdata.travel_scroll, label = '[[Travel Scroll|\'\'\'Travel Scroll\'\'\']]' }
		--[[16 ]]:addData{ sdata.level, label = 'Level' }
		--[[17 ]]:addData{ sdata.sublocations, label = 'Sub-locations' }
		--[[18 ]]:addData{ sdata.fairy_souls, label = ('[[File:Fairy Soul.png|15px]] [[Fairy Souls#%s|\'\'\'Fairy Souls\'\'\']]'):format(pagename) }
		--[[19 ]]:addData{ sdata.enigma_souls, label = ('[[File:Enigma Soul.png|15px]] [[Enigma Souls#%s|\'\'\'Enigma Souls\'\'\']]'):format(pagename) }
		
		--[[20 ]]:addData{ sdata.election_wins, label = '[[Mayor Election|\'\'\'Election Wins\'\'\']]' }
		
		--[[21 ]]:addData{ sdata.amount, label = 'Amount' }
		
		:addGroup()
			--[[A0 ]]:addData{ sdata.dungeon, label = 'Dungeon' }
			--[[A1 ]]:addData{ sdata.floor, label = 'Dungeon Floor' }
			--[[A2 ]]:addData{ sdata.boss, label = 'Boss' }
			--[[A3 ]]:addData{ sdata.status, label = 'Status' }
			--[[A4 ]]:addData{ sdata.dungeon_size, label = 'Dungeon Size' }
			--[[A5 ]]:addData{ sdata.party_size, label = 'Party Size' }
			--[[A6 ]]:addData{ sdata.required_combat_level, label = 'Required {{Skill|Combat}} Level' }
			--[[A7 ]]:addData{ sdata.required_catacombs_level, label = 'Required {{Skill|catacombs}} Level' }
			--[[A8 ]]:addData{ sdata.reqs, label = 'Requirements to enter' }
			--[[A9 ]]:addData{ sdata.base_xp, label = 'Base XP' }
			--[[A10]]:addData{ sdata.failable, label = 'Failable' }
		:done()
		
		:addGroup()
			--[[B0 ]]:addData{ sdata.mob_level, label = 'Mob Level' }
			--[[B1 ]]:addData{ sdata.damage_deals, label = 'Damage Deals' }
			--[[B2 ]]:addData{ sdata.damage_rift, label = 'Rift Damage' }
			--[[B3 ]]:addData{ sdata.damage_resistance, label = 'Damage Resistance' }
			--[[B4 ]]:addData{ sdata.spawn_location, label = 'Spawn Location' }
			--[[B5 ]]:addData{ sdata.spawn_condition, label = 'Spawn Condition' }
			--[[B6 ]]:addData{ sdata.special, label = 'Special' }
			--[[B7 ]]:addData{ sdata.special_behavior, label = 'Special Behavior' }
			--[[B8 ]]:addData{ sdata.mob_type, label = 'Mob Type' }
			--[[B9 ]]:addData{ sdata.entity_type, label = 'Entity Type' }
			--[[B10 ]]:addData{ sdata.effective_enchant, label = string.makeTitle('Effective Enchant', 'The weapon enchant that is most effective for killing this mob') }
		:done()
		
		:addGroup()
			--[[C0 ]]:addData{ sdata.requirements, label = 'Start Req.' }
			--[[C1 ]]:addData{ sdata.rewards, label = 'Reward' }
		:done()
		
		:addGroup{ header = 'Fishing Info', collapse = 'open' }
			--[[U0 ]]:addData{ sdata.sc_weight, label = '[[Weight]]' }
			--[[U1 ]]:addData{ sdata.sc_location, label = 'Fishing Location' }
			--[[U2 ]]:addData{ sdata.sc_type, label = 'Rod Type' }
			--[[U3 ]]:addData{ sdata.sc_fishing_req, label = 'Fishing Level Requirement' }
			--[[U4 ]]:addData{ sdata.sc_hotspot, label = 'Hotspot Only' }
			--[[U5 ]]:addData{ sdata.sc_bait, label = 'Effective Bait' }
			--[[U6 ]]:addData{ sdata.sc_hunter, label = '[[Odger#Rewards|Trophy Hunter Requirement]]' }
			--[[U7 ]]:addData{ sdata.sc_time_req, label = 'Catch Times' }
			--[[U8 ]]:addData{ sdata.sc_event_req, label = 'Event Required' }
			--[[U9 ]]:addData{ sdata.sc_other_req, label = 'Other Requirements' }
		:done()
		
		do
			local group_
			group_ = section:addGroup{ header = 'Stats', name = 'infobox-stats-list' }
			--[[D0 ]]group_:addData{ sdata.stats }
			table.each(table.values(iData.allstats), function(v)
				local ln = v[1]
				--[[D1+]]group_:addData{ sdata[ln], label = statname._getStatName(ln, nil, true) }
			end)
		end
		
		do
			local group = section:addGroup{ header = 'Perks' }
			--[[E0+]]
			additergroup('perk', sdata, group)
		end
		
		do
			local group = section:addGroup{ header = 'Perks' }
			--[[F0]]
			if sdata.default_desc then
				group:addData{ sdata.default_desc, label = sdata.default_name }
			end
			--[[F1+]]
			additergroup('upgrade', sdata, group)
		end
		
		-- for zone pages, location info is in the middle of the infobox
		local show_tabbed_locations_on_bottom = isNPC and (not sections[2]) and location_sections[2]
		local has_minimap = ldata.minimap
		if isLocation or ((not show_tabbed_locations_on_bottom) and (not has_minimap)) then
			add_location_section(section, ldata, minimalist, false)
		end
		
		section:addGroup{ header = 'Inhabitants', collapse = 'open' }
			:addGroup{ layout = 'horizontal', ['row-items'] = 2 }
				--[[H0 ]]:addData{ sdata.npcs, label = '[[Characters|NPCs]]' }
				--[[H1 ]]:addData{ sdata.mobs, label = '[[Mobs]]' }
			:done()
		:done()
		
		:addGroup{ header = 'Resources', collapse = 'open' }
			:addGroup{ layout = 'horizontal', ['row-items'] = 2 }
				--[[I0 ]]:addData{ sdata.drops, label = 'Mob Drops' }
				--[[I1 ]]:addData{ sdata.resources, label = 'Resources' }
			:done()
		:done()
		
		section:addGroup{ header = 'Drops' }
			--[[R0 ]]:addData{ sdata.mob_drops, label = 'Drops' }
			--[[R1 ]]:addData{ sdata.xp, label = 'XP' }
			--[[R2 ]]:addData{ sdata.gins, label = '{{C|alt=Gins}}' }
			--[[R3 ]]:addData{ sdata.experience, label = '[[File:Experience Orb.png|18px]] [[Experience]] Orbs' }
			--[[R4 ]]:addData{ sdata.essence, label = 'Essence' }
			--[[R5 ]]:addData{ sdata.attribute_shard, label = 'Attribute Shard' }
		:done()
		
		:addGroup{ header = 'Values' }
			--[[J0 ]]:addData{ sdata.base_value, label = 'Base Value' }
			--[[J1 ]]:addData{ sdata.max_value, label = 'Max Value' }
			--[[J2 ]]:addData{ sdata.min_value, label = 'Min Value' }
		:done()
		
		:addGroup{ header = 'Properties' }
			--[[K0 ]]:addData{ sdata.unlock_requirement, label = 'Unlock Requirements' }
			--[[K1 ]]:addData{ sdata.max_level, label = 'Skill Max Level' }
		:done()
		
		:addGroup{ header = 'Special Effects' }
			--[[L0 ]]:addData{ sdata.skill_special_effect, label = 'Special Effect' }
		:done()
		
		:addGroup{ header = 'Upgrades', layout = 'horizontal', ['row-items'] = 1 }
			--[[M0 ]]:addData{ sdata.super_compactor, label = '[[Super Compactor 3000]]' }
			:addGroup{ layout = 'horizontal', ['row-items'] = 2 }
				--[[M1 ]]:addData{ sdata.compactor, label = '[[Compactor]]' }
				--[[M2 ]]:addData{ sdata.auto_smelter, label = '[[Auto Smelter]]' }
			:done()
		:done()
		
		:addGroup{ header = 'Player interactions' }
			--[[N0 ]]:addData { sdata.quests, label = 'Quests' }
			--[[N1 ]]:addData { sdata.shop, label = 'Shop' }
		:done()
		
		:addGroup{ header = 'Next Event', collapse = 'open' }
			--[[S0 ]]:addData{ sdata.datetime, label = 'Date & Time' }
			--[[S1 ]]:addData{ sdata.countdown, label = 'Happening In' }
		:done()
		
		:addGroup{ header = 'Symbol'}
			--[[T0 ]]:addData{ sdata.symbol, label = 'Symbol' }
			--[[T1 ]]:addData{ sdata.unicode, label = 'Unicode Code Point' }
			--[[T2 ]]:addData{ sdata.icon, label = string.makeTitle('Icon', 'The icon displayed in the Equipment Menu interface.') }
		:done()
		
		:addGroup{ header = 'Metadata', ['row-items'] = 1, collapse = 'closed' }
			--[[Q0 ]]:addData{ sdata.id, label = 'ID' }
		:done()
		
		if (not isLocation) and (show_tabbed_locations_on_bottom or has_minimap) then
			if not show_tabbed_locations_on_bottom then
				add_location_section(section, ldata, false, true)
			elseif i == 1 then
				local location_panel = section:addPanel{header = 'Locations', collapse = 'open' }
				for l, location_section_data in ipairs(location_sections) do
					local location_tab_data = argNormalize(location_section_data)
					local location_tab_section = --[[0]]location_panel:addSection{ label = l }
					
					add_location_section(location_tab_section, location_tab_data, true, false)	
				end
			end
		end
	end
	
	return table.concat{
		ibox:tostring(),
		curTitle.namespace == 0 and category_to_add or '',
	}
end

function p.test()
	return p._infoboxCreate{
		
	}
end

--Finish Module/Exports
return p
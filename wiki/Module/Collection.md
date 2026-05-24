local getArgs = require('Module:Arguments').getArgs
local loader = require('Module:Loader')

local string, table, yesno, item, color, skills = loader.require('String', 'Table', 'Yesno', 'Item', 'Color', 'Skillname')
local collectionData = loader.loadData('Collection/Data')

local p = {}

-----------------------------------------------------------------------------
-- Template:CollectionTable
--
-- Makes a simple table that lists each reward from a collection for use on it's collection page
-----------------------------------------------------------------------------
function p.collectionTable( frame )
	
	local function split(s)
		return string.split(s, '%s*;%s*')
	end
	local function getlist(arg, i)
		local temp = arg and split(arg)
		return temp and (temp[i] or temp[1]) or nil
	end
	
	local args = getArgs(frame)
	
	local collection = args['collection'] or args[1] or mw.title.getCurrentTitle().fullText
	local collectionPageTable = yesno(args['collectionPageTable'])
	-- get collection data from database
	local rows = table.deepCopy(collectionData[collection] or {}, true)
	
	-- parse input into the collection data structure
	for i = 1, 16 do
		local rewards = args['reward'..i]
		if rewards then
			rows[i] = {
				required = args['required' .. i],
				reward = table.map(split(rewards), function(reward, j)
					return {
						reward,
						type = getlist(args['type' .. i], j),
						comingsoon = getlist(args['comingsoon' .. i], j),
						link = getlist(args['link' .. i], j),
						nolink = getlist(args['nolink' .. i], j),
					}
				end),
			}
		end
	end
	
	return p._collectionTable( collection, rows, collectionPageTable )
end

function p._collectionTable( collection, colRowData, subTable )
	local wikitable = mw.html.create('table'):addClass('wikitable margin-centered')
	if subTable then
		wikitable:css({ margin = 0, width = "100%", border = 0 })
	end
	local row = wikitable:tag('tr')
	row:tag('th'):wikitext('LVL'):done()
	row:tag('th'):wikitext('Required'):addClass('size-small'):done()
	row:tag('th'):wikitext('Reward'):css(subTable and { width="100%" } or {}):done()
	row:tag('th'):wikitext('[[Project Seria Caveblock Levels|' .. color._colorTemplates('Aqua', 'XP') .. ']]'):done()
	row:done()
	
	for i, data in ipairs(colRowData) do
		local tier = string._toRoman(i)
		local row = wikitable:tag('tr'):attr('id', tier)
		
		-- Tier
		row:tag('td'):addClass('centertxt'):css({ ['font-weight']='bold', ['font-family']='"Times New Roman", monospace' }):wikitext(tier):done()
		
		-- Requirement
		row:tag('td'):wikitext(string._formatNum(data.required)):done()
		
		-- Reward
		local td = row:tag('td')
		local cellData = {}
		for i, reward in pairs(data.reward) do
			local _name, _type, _comingsoon, _link, _nolink, _image =
				reward[1],
				reward.type or data.type or 'Recipe',
				reward.comingsoon or data.comingsoon,
				reward.link or data.link,
				reward.nolink or data.nolink,
				reward.image or data.image
			table.push(cellData, getRewardLine(_name, _type, _comingsoon, _link, _nolink, _image))
		end
		td:wikitext(table.concat(cellData, '<br />')):done()
		
		-- Find Project Seria Caveblock Xp
		td = row:tag('td')
		local xp = '{{Bc}}'
		for i, reward in pairs(data.reward) do
			if (reward.type or data.type or 'Recipe'):match('Project Seria Caveblock Experience') then
				xp = color._colorTemplates('Aqua', '+' .. reward[1])
				break
			end
		end
		td:wikitext(xp)
		
		row:done()
	end
	
	wikitable:done()
	
	return tostring(wikitable)
end

function getRewardLine(reward, pType, pComingSoon, pLink, pNoLink, pImage)
	local function makeLink(reward, link, nolink, noImg)
		local name = reward
		nolink = yesno(nolink, false)
		-- For supplied link, no processing
		if reward:match('^%[%[.-%]%]$') then
			return reward
		end
		-- Check if it's an enchanted book
		local enchant, tier = string.match(reward, '^Enchanted Book %((.+) ([%dIVXivx]+)%)$')
		if enchant then
			name = ('Enchanted Book &%s %s&'):format(enchant, tier)
		end
		-- Check if it's a pet
		if reward:match('^Mystery%s[A-Z]+[a-z]+%sPet$') then
			link = string.sub(reward,9)
		end
		-- Check if it's essence
		if pType == 'Essence' then
			link = name .. ' Essence'
		end
		
		-- Output
		if noImg then
			if pType == 'Custom' then
				return mw.getCurrentFrame():preprocess(nolink and name or ('[[%s|%s]]'):format(link or name, name))
			end
			return nolink and name or ('[[%s|%s]]'):format(link or name, name)
		end
		return item._item(pImage or link or name, true, nolink, false, false, false, false)
	end
	
	local isExp = pType:match('[Ee]xperience') and not pType:match('Project Seria Caveblock')
	local sbExp = pType:match('Project Seria Caveblock Experience')
	local isCustom = pType:match('Custom')
	local unknownType = not not pType:match('[Cc]oming [Ss]oon')
	pComingSoon = unknownType or yesno(pComingSoon, false)
	
	if sbExp then
		return nil
	elseif isExp then
		local temp = pType
		if string.find(pType, ' [Ee]xperience$') then
			temp = skills._getSkillName(string.gsub(pType, '%s*[eE]xperience$', ''), '', {}) .. ' Experience'
		end
		return ('+%s %s'):format(string._formatNum(reward), temp), pComingSoon
	else
		local comingSoonText = pComingSoon
			and string.wrapHtml('[Coming Soon] ', 'span', { class = 'color-red' })
			or ''
		local noRewardYet = reward:lower():match('^coming soon$')
		return ('%s%s %s'):format(
			comingSoonText,
			noRewardYet and string.wrapHtml('Coming Soon', 'span', { class = 'color-red' }) or makeLink(reward, pLink, pNoLink, not pImage and isCustom),
			string.wrapHtml((noRewardYet or isCustom or unknownType) and '' or pType, 'i')
		)
	end
end

-- Finish Module --
return p


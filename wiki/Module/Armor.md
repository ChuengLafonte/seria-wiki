local loader = require('Module:Loader')

local string, yesno, arguments, invslot, raritytier, colorMdl, ability, makeHtmlStatsList, elementMdl =
	loader.lazy.require('String', 'Yesno', 'Arguments', 'Inventory slot', 'RarityTier', 'Color', 'Ability', 'Armor/StatsList', 'Element')

local fairyArmorData = loader.lazy.loadData('Armor/Data/FairyArmorColors')

local p = {}

--Global parameters
local title = mw.title.getCurrentTitle()
local getArgs = arguments.getArgs

local function tableError(errMsg, sec)
	if sec
		then sec = '<br>' .. sec
	end
	return '<table class="messagebox" style="display:inline-block; text-align:left; border-color:#e83f33; background:#691610;"><td><strong class="error">Error in Parsing Template: ' .. errMsg .. (sec and sec or '') .. '</strong></td></table>[[Category:Pages with template errors]]'
end

---------------------------------------------------------------------------------
-- function: json(frame: table|frame)
-- 
-- Returns the data of this module to JSON.
---------------------------------------------------------------------------------
function p.json(frame)
	return mw.text.jsonEncode(armorData):gsub('\\', '\\\\')
end

-----------------------------------------------------------------------------
-- Template:GetArmorStat
-- 
-- Retrivies a piece specified data from /Data
-----------------------------------------------------------------------------
function p.getArmorStat(frame)
	local args = getArgs(frame)
	local armor = args[1]
	if not armor and title.namespace == 0
			then armor = title.text
		elseif not armor and title.namespace ~= 0 then error('Unknown Argument to #1: Invalid input (input expected, got none)', 2)
	end
	
	return frame:preprocess(p._getArmorStat( assert(armor, 'Bad argument to #1 (input expected, got nil)') ))
end

-----------------------------------------------------------------------------
-- Template:GetArmorStat Module Access Point
-----------------------------------------------------------------------------
function p._getArmorStat(armorName)
	local armor = armorData[armorName:lower()]
	local stats = armor.stats
	local head = stats.head
	
	--Load Nil Stats
	if not head.def then head.def = '' end
	--Return the Stat
	if head.def == '' then outputStat = '' else outputStat = head.def end
	
	return outputStat
end


-----------------------------------------------------------------------------
-- Template:ArmorInfo
--
-- Gathers All the data from /Data and formats it in a comprehensive table
-----------------------------------------------------------------------------
function p.armorInfo(frame)
	local args = getArgs(frame)
	local armor = args['armor'] or args['a'] or args[1]
	local useHeader = yesno(args['h'] or args['header'])
	local showOtherInfo = yesno(args['info'] or args['other info'], true)
	
	--Error Mechanism
	if not armor and title.namespace == 0
			then armor = title.text
		elseif not armorData[armor:lower()] and title.namespace ~= 0
			then return tableError('Bad Argument to \"armor\": Invalid Inputs', 'Inputed Armor set: ' .. armor)
	end
	
	return frame:preprocess(p._armorInfo(armor, useHeader, showOtherInfo))
end

-----------------------------------------------------------------------------
-- Template:ArmorInfo Module Access Point
-----------------------------------------------------------------------------
function p._armorInfo(armorName, useHeader, showOtherInfo)
	if not armorName
		then return error('Bad argument to #1 "armorInfo": inputs expected', 2)
	end
	local armor = armorData[armorName:lower()]
	if not armor
		then error('Bad Argument to #1 "armorInfo": invalid inputs \"' .. armorName .. '\"')
	end
	
	local endStr = {}
	
	--Load all Data sets in variables
	local stats = armor.stats
	local head = stats.head
	local chest = stats.chest
	local legs = stats.legs
	local boots = stats.boots
	local total = stats.total
	
	local fsb_name = total.fsb_name
	local fsb_desc = total.fsb_desc
	local fsb2_name = total.fsb2_name
	local fsb2_desc = total.fsb2_desc
	local secretFsb = total.secretFsb
	
	local materials = armor.materials
	local source = armor.source
	local rarity = armor.rarity
	local collection = armor.collection
	local dropChance = armor.dropChance
	local mobSource = armor.mobSource
	local customRarity = armor.customRarity
	local catacombsLevel = armor.catacombsLevel
	
	--If Stat group is nil, set to Empty table
	if not head then head = {} end
	if not chest then chest = {} end
	if not legs then legs = {} end
	if not boots then legs = {} end
	
	--Load Nil Stats
		local function loadNilStats(item)
			if not item.str then item.str = '' end
			if not item.cc then item.cc = '' end
			if not item.cd then item.cd = '' end
			if not item.as then item.as = '' end
			if not item.int then item.int = '' end
			if not item.spd then item.spd = '' end
			if not item.hp then item.hp = '' end
			if not item.def then item.def = '' end
			if not item.td then item.td = '' end
			if not item.scc then item.scc = '' end
			
			--Other
			if not item.specialEffect then item.specialEffect = '' end
			if not item.pcb_name then item.pcb_name = '' end
			if not item.pcb_desc then item.pcb_desc = '' end
			if not item.pcb2_name then item.pcb2_name = '' end
			if not item.pcb2_desc then item.pcb2_desc = '' end
		end
		--Head
		loadNilStats(head)
		--Chest
		loadNilStats(chest)
		--Legs
		loadNilStats(legs)
		--Boots
		loadNilStats(boots)
			
		--Total
			if not total.str then total.str = '' end
			if not total.cc then total.cc = '' end
			if not total.cd then total.cd = '' end
			if not total.as then total.as = '' end
			if not total.int then total.int = '' end
			if not total.spd then total.spd = '' end
			if not total.hp then total.hp = '' end
			if not total.def then total.def = '' end
			if not total.td then total.td = '' end
			if not total.scc then total.scc = '' end
			
		
		--Load other Nil params
			if not fsb_name then fsb_name = '' end
			if not fsb_desc then fsb_desc = '' end
			if not fsb2_name then fsb2_name = '' end
			if not fsb2_desc then fsb2_desc = '' end
			if not materials then materials = {} end
			if not collection then collection = '' end
			if not dropChance then dropChance = '' end
			if not mobSource then mobSource = '' end
			if not secretFsb then secretFsb = '' end
			if not customRarity then customRarity = '' end
		
	--Text Parameters
		local baseArmorName = string.gsub(armorName, 'Armor$', '')
		
		local function itemCellData(item, defaultPieceName, filePieceName)
			local t = {}
			
			if item.label
				then t.name = item.label
				else t.name = defaultPieceName 
			end
			t.stats = makeHtmlStatsList(item, '{{Bc}}')
			
			--Label
			if rarity and not item.labelText
				then t.label = raritytier._colorText(rarity, (item.name and item.name or baseArmorName .. ' ' .. t.name), nil, armorName .. '#' .. defaultPieceName)
				else 
					if item == head or item == chestplate 
							then k = 'Chestplate' 
						elseif item == legs or item == boots 
							then k = 'Boots' 
						else k = '' 
					end
					t.label = '[[' .. armorName .. '#' .. k .. '|' .. item.labelText .. ']]'
					
			end
				
			--Other
			if item.specialEffect == '' 
				then t.se = '' 
				else t.se = '<li>' .. item.specialEffect .. '</li>' 
			end
			if item.pcb_name == '' 
				then t.pcbName = '' 
				else t.pcbName = '<li>{{PieceBonus|' .. item.pcb_name .. '}}<br>' .. item.pcb_desc
			end
			if item.pcb2_name == ''
				then t.pcb2Name = ''
				else t.pcb2Name = '<li>{{PieceBonus|' .. item.pcb2_name .. '}}<br>' .. item.pcb2_desc .. '</li>'
			end
				
			if item.ia then
				if item.ia.name 
					then item.ia.name = '{{ItemAbility|' .. item.ia.name .. '}}'
					else item.ia.name = ''
				end
				if item.ia.desc 
					then item.ia.desc = '<br>' .. item.ia.desc
					else item.ia.desc = ''
				end
				if item.ia.cost
					then item.ia.cost = '<br>{{Mc|' .. item.ia.cost .. '}}'
					else item.ia.cost = ''
				end
				if item.ia.cd
					then item.ia.cd = '<br>{{Cd|' .. item.ia.cd .. '}}'
					else item.ia.cd = ''
				end
				t.iaName = '<li>' .. item.ia.name .. item.ia.desc .. item.ia.cost .. item.ia.cd .. '</li>'
				else t.iaName = ''
			end
				
			if item.slot then
				t.slot = item.slot
			elseif item.name and not item.label then
				t.slot = item.name
			elseif item.label then
				t.slot = armorName:gsub('%s*([Aa]rmor)$', '') .. ' ' .. item.label
			else
				t.slot = armorName:gsub('%s*([Aa]rmor)$', '') .. ' ' .. t.name
			end
				
			return t
		end
	
	--Parse Stats in to Usable Lists
		--Head
		local headData = itemCellData(head, 'Helmet', 'Helmet')
		--Chest
		local chestData = itemCellData(chest, 'Chestplate', 'Chestplate')
		--Legs
		local legsData = itemCellData(legs, 'Leggings', 'Leggings')
		--Boots
		local bootsData = itemCellData(boots, 'Boots', 'Boots')
		--Total
		local totalStatsData = makeHtmlStatsList(total, '{{Bc}}')
	
	--Rarity Label
	if rarity and not customRarity then rText = raritytier._getTier(rarity).name else rText = {} end
	if rarity then coloredArmorName = '[[' .. armorName .. '|' .. raritytier._colorText(rarity, armorName) .. ']]'else coloredArmorName = customRarity end
		

	r = '<li><b>Armor Rarity:</b> ' .. (customRarity and customRarity or '{{R|' .. rarity .. '}}') .. '</li></ul>'
	
	if rarity
		then tText = coloredArmorName
		else tText = '[[' .. armorName .. '|' .. armor.totalLabel .. ']]'
	end
	
	--Full Set Bonus
	if fsb_desc == '' or fsb_name == '' 
		then fsb = '' 
		else fsb = '<li>{{FullSetBonus|' .. fsb_name .. '}}<br>' .. fsb_desc
	end
	if fsb2_desc == '' or fsb_name2 == '' 
		then fsb2 = ''
		else fsb2 = '<li>{{FullSetBonus|' .. fsb2_name .. '}}<br>' .. fsb2_desc
	end
	local checkInvColls = head.collection or chest.collection or legs.collection or boots.collection
	if stats.total.secretFsbDesc then 
		sFSBName = '<li>{{FullSetBonus|' .. total.secretFsbName .. '|secret=1}}</code>'
		sFSBdesc = '<br>' .. stats.total.secretFsbDesc .. '</li>'
		sFSB = sFSBName .. sFSBdesc
		else sFSB = ''
	end
	
	local fsbText = fsb .. fsb2 .. sFSB
	
	--Crafting Functions
	local craftingHeader = '<h2>Other Info</h2>'
	local mText = function(t, startText, endText) return startText .. '{{RL|image=1|' .. materials[t].amount .. ' ' .. materials[t].name .. '}}' .. endText end
	
	local bazaarLine = function(k) 
		local mat = materials[k].amount .. ' ' .. materials[k].name
		local z = function(...)
			local t = ...
			return '{{#iferror:{{BPC|' .. mat .. '}}|' .. t..'|' .. mat .. '}}'
		end
		
		if not materials[k].cost then materials[k].cost = 0 end
		return('\n*' .. z(materials[k].cost*materials[k].amount))
	end
	
	local cText = function(i, startText, endText) return startText .. '{{BazaarPurchaseCalc|' .. bazaarLine(i) .. '}}' .. endText end
	
	--Materials/Cost Table
	local materialsList = function()
		local t = {}
		for i = 1, 9, 1 do
			if materials[i] then t[#t+1] = mText(i, '<li>', '</li>') end
		end
		return '<ul style="list-style-type: square;">' .. table.concat(t, '') .. '</ul>'
	end
	
	local costList = function()
		local i = {}
		local bullet = '{{RightBullet|padding=8px}}'
		for j = 1, 9, 1 do
			if materials[j] then i[#i+1] = cText(j, '<li>', '') .. bullet .. '</li>' end
		end

		return '<ul style="list-style-type:none; padding: 0px;">' .. table.concat(i, '') .. '</ul>'
	end
	
	local function totalMaterialsCost()
		local f = {}
		for i = 1, 9, 1 do 
			if materials[i] then f[#f+1] = bazaarLine(i) end
		end
					
		return 'Total Bazaar Materials Cost: {{BazaarPurchaseCalc|' .. table.concat(f, '') .. '}}'
	end
	
	--Create the Materials Table
	local materialsTable = mw.html.create('table'):attr({ style = 'margin: 1em 1em 0.2em 0em;' }):addClass('article-table')
		--Table Header
		local row = materialsTable:tag('tr')
			row:tag('th'):wikitext('{{Center|Material (Amount, Name)}}'):done()
			row:tag('th'):wikitext('<span style=\'text-align: center\'>Bazaar Purchase Cost<sup><abbr title=\"Values are updated every half hour from the Hypixel API. Last updated on: {{BazaarLastUpdate}}.\">ⓘ</abbr></sup></span>'):done()
		row:done()
		--Materials List/Cost
		local row = materialsTable:tag('tr')
			row:tag('td'):wikitext(materialsList()):done()
			row:tag('td'):attr({ style = 'text-align: right;' }):wikitext(costList()):done()
		row:done()
		
		--Total Cost
		local row = materialsTable:tag('tr')
			row:tag('td')
				:attr({ colspan = 2 })
				:wikitext('<center>' .. totalMaterialsCost() .. '</center>')
			:done()
		row:done()
		
	materialsTable:done()
	
	if armor.materials
		then m = tostring(materialsTable)
		else m = ''
	end
	--Collection
	if collection == '' then
		if head.collection 
			then headColl = '<li>{{B|Head:}}&nbsp;{{Coll|' .. head.collection .. '|showicon=yes}}</li>' 
			else headColl = ''
		end
		if chest.collection 
			then chestColl = '<li>{{B|Chestplate:}}&nbsp;{{Coll|' .. chest.collection .. '|showicon=yes}}</li>'
			else chestColl = ''
		end
		if legs.collection 
			then legsColl = '<li>{{B|Leggings:}}&nbsp;{{Coll|' .. legs.collection .. '|showicon=yes}}</li>'
			else legsColl = ''
		end
		if boots.collection 
			then bootsColl = '<li>{{B|Boots:}}&nbsp;{{Coll|' .. boots.collection .. '|showicon=yes}}</li>' 
			else bootsColl = ''
		end
		
		coll = '<b>Collections:</b><ul>' .. headColl .. chestColl .. legsColl .. bootsColl .. '</ul>'
		
		else coll = '<b>Collection: </b>{{Coll|' .. collection .. '|showicon=yes}}'
	end
	
	if catacombsLevel then
		endStr[#endStr+1] = table.concat{
			'<br>',
			string.bold{ string.makeLink('The Catacombs', 'Catacombs Level requirement') ': ' },
			color.makeColor('red', catacombsLevel)
		}
	end
	
	if checkInvColls and collection == '' then
		source = '<b>Source: </b>[[' .. source .. ']]'
		else source = '<br><b>Source: </b>[[' .. source .. ']]'
	end
	if source:match('Merchant')
		then source = source .. '<ul><li><b>Merchant:</b>&nbsp;[[' .. armor.merchant .. ']]</li>' .. (
				armor.merchantPrice
				and '<li><b>Price:</b> {{C|' .. armor.merchantPrice .. '}}'
				or ''
			) .. '</ul>' 
	end
	
	if collection == '' and (not checkInvColls) then coll = '' end
	
	--Drop Chance
	if collection == '' and dropChance ~= '' then
		if dropChance <= 0.01
				then k = '{{odds|rngl}}'
			elseif dropChance <= 0.1
				then k = '{{odds|ll|na=1}}'
			elseif dropChance <= 1
				then k = '{{odds|rl|na=1}}'
			elseif dropChance <= 30
				then k = '{{odds|ucl|na=1}}'
			elseif dropChance > 30
				then k = '{{odds|cl|na=1}}'
			else k = ''
		end
		drops = '<br><b>Armor Piece Drop Chance: </b>{{G|' .. dropChance .. '%}} (' .. k..')'
		if coll == '' then
			drops = '<b>Armor Piece Drop Chance: </b>{{G|' .. dropChance .. '%}} (' .. k..')'
		end
		else drops = ''
	end
	
	
	
	if mobSource ~= ''
		then mob = '<br><b>Dropped From: </b>[[' .. mobSource .. ']]'
		else mob = ''
	end
	--Header
	local header = '<h2>Armor Stats</h2>'
	--CSS parameters
	local borderStyle = 'border-style', 'solid'
	local borderColor = 'border-color', '#aaa'
	
	
	--Piece Bonus Toggle Button
	if head.specialEffect == '' and
		chest.specialEffect == '' and
		legs.specialEffect == '' and
		boots.specialEffect == '' and
		
		head.pcb_name == '' and 
		head.pcb_desc == '' and 
		chest.pcb_name == '' and 
		chest.pcb_desc == '' and 
		legs.pcb_name == '' and 
		legs.pcb_desc == '' and 
		boots.pcb_name == '' and 
		boots.pcb_desc == ''and not
		head.ia and not
		chest.ia and not
		legs.ia and not
		boots.ia and not
		armor.stats.total.specialEffect
		
		then toggleButton = ''
		else toggleButton = elementMdl._collapsibleButton{
			id = 'pcb-toggle',
			text = 'Show/Hide Piece Bonuses'
		}
	end
	
	--Create the Table
	local wikitable = mw.html.create('table')
		:addClass('wikitable')
		:css('overflow', 'auto')
		:css('border-width', '2px 2px 2px 2px !important')
		:css('vertical-align', 'text-top')
		
	-----------------------------------------------------------------------------
	--Table Functions
	-----------------------------------------------------------------------------
	
	--Search For Empty Special Effect cells
	local nilVals = function()
		return head.specialEffect == '' and
		chest.specialEffect == '' and
		legs.specialEffect == '' and
		boots.specialEffect == '' and
		
		head.pcb_name == '' and 
		head.pcb_desc == '' and 
		chest.pcb_name == '' and 
		chest.pcb_desc == '' and 
		legs.pcb_name == '' and 
		legs.pcb_desc == '' and 
		boots.pcb_name == '' and 
		boots.pcb_desc == ''and not
		head.ia and not
		chest.ia and not
		legs.ia and not
		boots.ia and not
		armor.stats.total.specialEffect

	end
	
	--Empty Stat Cells
	local nilStatCells = function()
		return bootsData.stats == '{{Bc}}'
		and legsData.stats == '{{Bc}}'
		and chestData.stats == '{{Bc}}'
		and headData.stats == '{{Bc}}'
	end
	
	--Empty Cell
	local emptyCell = function(params, k) 
		return k:attr({ colspan = 2 })
			:wikitext('{{Bc}}')
			:css(borderStyle)
			:css('border-width', params)
			:css(borderColor)
		:done()
	end
	
	--Collapsible Peice Bonus Cell
	if nilVals()
		then collapsibleCell = {}
		else collapsibleCell = function(item, a, k)
			
			local data = ''
			if item.se == '' and item.pcbName == '' and item.pcb2Name == '' and item.ia == ''
				then return a:attr({ 
					class = 'mw-collapsible mw-collapsed',
					id = 'mw-customcollapsible-pcb-toggle',
					style = 'max-width: 300px;', 
				})
				:css('border-width', '1px 2px 2px 1px')
				:wikitext('{{Bc}}')
				:done()
				else return a:attr({ 
					class = 'mw-collapsible mw-collapsed',
					id = 'mw-customcollapsible-pcb-toggle',
					style = 'max-width: 300px; vertical-align: text-top;', 
				})
			:css('border-width', '1px 2px 2px 1px')
			:wikitext(k.label .. '<ul style="list-style-type: square;">' .. (armor.stats.total.specialEffect or item.se) .. item.pcbName .. item.pcb2Name .. item.iaName .. '</ul>')
			:done()
			
			end	
		end
	end
	--Collapsible Main Stats Cell
	if nilVals() then collapsible = {}
		else collapsible = {
			class = 'mw-collapsible',
			id = 'mw-customcollapsible-pcb-toggle',
		}
	end
	--Collapsible Peice Bonus Cell
	if nilVals() 
		then collapsed = {}
		else collapsed = {
				class = 'mw-collapsible mw-collapsed',
				id = 'mw-customcollapsible-pcb-toggle',
			}
	end
	
	--Empty Peice Bonus Cell
	if nilVals()
			then emptyPcbCell = function(k) return '' end
			else 
				emptyPcbCell = function(t) 
					return t:tag('td'):attr(collapsed)
						:css({ ['border-width'] = '1px 2px 2px 1px', ['min-width'] = '100px' })
						:wikitext('{{Bc}}')
					:done() 
				end
	end
	
	--Add the Table Rows
		local row = wikitable:tag('tr')
			if nilVals() 
				then dummy = ''
				else row:tag('th')
					:attr({ colspan = 4 })
					:wikitext(tostring(toggleButton))
					:css('border-width', '2px 2px 2px 3px')
				:done()
			end
		local row = wikitable:tag('tr')
		--Header row 1
			row:tag('th')
				:attr({ colspan = 2 })
				:wikitext(headData.name)
				:css(borderStyle)
				:css('border-width', '2px 2px 0px 3px')
				:css(borderColor)
				:css('min-width', '150px')
			:done()
			
			row:tag('th')
				:attr({ colspan = 2 })
				:wikitext(chestData.name .. '<span style="float: right; font-size: 11px;">[[Module:Armor/Data|v]] {{*}} [{{FULLURL:Module:Armor/Data|action=edit}} e] {{*}} [[Module_talk:Armor|d]]</span>')
				:css(borderStyle)
				:css('border-width', '2px 2px 1px 2px')
				:css(borderColor)
				:css('min-width', '150px')
			:done()
		row:done()
		
		local row = wikitable:tag('tr')
		--Stats row 1
			--Helmet
			if headData.stats == '{{Bc}}'
				then emptyCell('1px 2px 2px 3px', row:tag('td'))
				else row:tag('td')
					:wikitext(invslot.slot{headData.slot})
					:css(borderStyle)
					:css('border-width', '1px 1px 2px 3px')
					:css(borderColor)
					:done()
					
					row:tag('td')
					:attr(collapsible)
					:wikitext(headData.label .. headData.stats)
					:css(borderStyle)
					:css('border-width', '1px 2px 2px 1px')
					:css('vertical-align', 'text-top')
					:css(borderColor)
					:done()
					if 
						head.specialEffect == '' 
						and head.pcb_desc == '' 
						and head.pcb_name == '' 
						and not head.iaia 
						and not armor.stats.total.specialEffect
					then 
						emptyPcbCell(row) 
					else 
						collapsibleCell(headData, row:tag('td'), headData)
					end
			end
			--Chestplate
			if chestData.stats == '{{Bc}}'
				then emptyCell('1px 2px 2px 2px', row:tag('td'))
				else row:tag('td')
					:wikitext(invslot.slot{ chestData.slot })
					:css(borderStyle)
					:css('border-width', '1px 1px 2px 2px')
					:css(borderColor)
				:done()
					
				row:tag('td')
					:attr(collapsible)
					:wikitext(chestData.label .. chestData.stats)
					:css(borderStyle)
					:css('border-width', '1px 2px 2px 1px')
					:css('vertical-align', 'text-top')
					:css(borderColor)
				:done()
					
				if 
					chest.specialEffect == '' 
					and chest.pcb_desc == '' 
					and chest.pcb_name == '' 
					and not chest.ia 
					and not armor.stats.total.specialEffect
				then 
					emptyPcbCell(row)
				else
					collapsibleCell(chestData, row:tag('td'), chestData)
				end
			end
		row:done()
		
		local row = wikitable:tag('tr')
		--Header row 2
			row:tag('th')
				:attr({ colspan = 2 })
				:wikitext(legsData.name)
				:css(borderStyle)
				:css('border-width', '2px 2px 1px 3px')
				:css(borderColor)
			:done()
			
			row:tag('th')
				:attr({ colspan = 2 })
				:wikitext(bootsData.name)
				:css(borderStyle)
				:css('border-width', '2px 2px 1px 2px')
				:css(borderColor)
			:done()
		row:done()
		
		local row = wikitable:tag('tr')
		--Stats Row 2
			--Leggings
			if legsData.stats == '{{Bc}}'
				then emptyCell('1px 2px 2px 3px', row:tag('td'))
				else row:tag('td')
					:wikitext(invslot.slot{legsData.slot})
					:css(borderStyle)
					:css('border-width', '1px 1px 2px 3px')
					:css(borderColor)
				:done()
				
				row:tag('td')
					:attr(collapsible)
					:wikitext(legsData.label .. legsData.stats)
					:css(borderStyle)
					:css('border-width', '1px 1px 2x 3x')
					:css('vertical-align', 'text-top')
					:css(borderColor)
				:done()
				
				if 
					legs.specialEffect == ''
					and legs.pcb_desc == ''
					and legs.pcb_name == ''
					and not legs.ia
					and not armor.stats.total.specialEffect
				then 
					emptyPcbCell(row)
				else 
					collapsibleCell(legsData, row:tag('td'), legsData)
				end
			end
			--Boots
			if bootsData.stats == '{{Bc}}'
				then emptyCell('1px 2px 2px 2px', row:tag('td'))
				else row:tag('td')
					:wikitext(invslot.slot{bootsData.slot})
					:css(borderStyle)
					:css('border-width', '1px 1px 2px 2px')
					:css(borderColor)
				:done()
				
				row:tag('td')
					:attr(collapsible)
					:wikitext(bootsData.label .. bootsData.stats)
					:css(borderStyle)
					:css('border-width', '1px 2px 2px 1px')
					:css('vertical-align', 'text-top')
					:css(borderColor)
				:done()
				
				if 
					boots.specialEffect == ''
					and boots.pcb_desc == ''
					and boots.pcb_name == '' 
					and not boots.ia
					and not armor.stats.total.specialEffect
				then 
					emptyPcbCell(row)
				else 
					collapsibleCell(bootsData, row:tag('td'), bootsData)
				end
			end
		row:done()
		
		--Total Stats row
		local row = wikitable:tag('tr')
			if nilStatCells()
				then dummy = ''
				else row:tag('th')
					:attr({ colspan = 4 })
					:attr(collapsible)
					:wikitext('Total')
					:css(borderStyle)
					:css('border-width', '2px 2px 1px 3px')
					:css(borderColor)
				:done()
			end
		local row = wikitable:tag('tr')
			if nilStatCells()
				then dummy = ''
				else row:tag('td')
					:attr({ colspan = 4 })
					:attr(collapsible)
					:wikitext('{{Text anchor|Total|&#x0200B;}}' .. tText .. totalStatsData)
					:css(borderStyle)
					:css('border-width', '1px 2px 2px 3px')
					:css(borderColor)
				:done()
			end
		row:done()
		
	wikitable:done()
	
	if not showOtherInfo then return (not useHeader and '' or header) .. tostring(wikitable) .. '<ul style="list-style-type:square;">' .. fsbText .. r end
	
	return (not useHeader and '' or header) .. tostring(wikitable) .. '<ul style="list-style-type:square;">' .. fsbText .. r..craftingHeader .. m..coll .. drops .. mob .. source .. table.concat(endStr)
end

-----------------------------------------------------------------------------
-- Template:ArmorStats
--
-- Formats armor data passed into it in a comprehensive table
-- not to be confused with getArmorStat()
-----------------------------------------------------------------------------
function p.templateArmorStats(frame)
	local args = getArgs(frame)
	local useHeader = yesno(args['header'], false)
	
	local partsData = {}
	for _, part in ipairs({ 'helmet', 'chest', 'legs', 'boots', 'total' }) do
		partsData[part] = {
			-- these 3 aren't used for total, but no harm having them checked
			special_name = args[part .. '_special_name'],
			img = args[part .. '_img'],
			color = args[part .. '_color'],
			
			-- stats
			manual = args[part .. '_manual'],
			def = args[part .. '_def'],
			hp = args[part .. '_hp'],
			str = args[part .. '_str'],
			int = args[part .. '_int'],
			spd = args[part .. '_spd'],
			critchance = args[part .. '_critchance'],
			critdmg = args[part .. '_critdmg'],
			trudef = args[part .. '_trudef'],
			hpbs = yesno(args[part .. '_hpbs'], false),
			
			-- also not used for total
			pcb = args[part .. '_pcb'],
			pcb_desc = args[part .. '_pcb_desc'],
		}
	end
	
	local allHpbs = yesno(args['all_hpbs'], false)
	local defaultImages = yesno(args['default_images'], false)
	local useBlazePet = yesno(args['blaze_pet'], false)
	
	local additionalEffects = args['additional_effects']
	local fsbName = args['full_set_bonus_name']
	local fsbDesc = args['full_set_bonus_desc']
	local fsb2Name = args['full_set_bonus2_name']
	local fsb2Desc = args['full_set_bonus2_desc']
	local pcbName = args['piece_bonus_name']
	local pcbDesc = args['piece_bonus_desc']
	local note = args['note']
	
	local showPcb = yesno(args['show_pcb'], false)
	local showPcbR1 = yesno(args['show_pcb_r1'], false)
	local showPcbR2 = yesno(args['show_pcb_r2'], false)
	local pcbToggleButtonName = args['pcb_toggle_button_name']
	
	return frame:preprocess(p._templateArmorStats(useHeader,
		partsData['helmet'], partsData['chest'], partsData['legs'], partsData['boots'], partsData['total'],
		allHpbs, defaultImages, useBlazePet, additionalEffects, fsbName, fsbDesc, fsb2Name, fsb2Desc,
		pcbName, pcbDesc, note, showPcb, showPcbR1, showPcbR2, pcbToggleButtonName
	))
end

function p._templateArmorStats(useHeader, helmetData, chestData, legsData, bootsData, totalData,
	allHpbs, defaultImages, useBlazePet, additionalEffects, fsbName, fsbDesc, fsb2Name, fsb2Desc,
	pcbName, pcbDesc, note, showPcb, showPcbR1, showPcbR2, pcbToggleButtonName)
	
	local usePcb = (showPcb or showPcbR1 or showPcbR2) and (
		helmetData['pcb'] or helmetData['pcb_desc'] or
		chestData['pcb'] or chestData['pcb_desc'] or
		legsData['pcb'] or legsData['pcb_desc'] or
		bootsData['pcb'] or bootsData['pcb_desc']
	)
	
	-- Format a stat as hpbs value
	local function hpbsStat(pStat, pVal)
		return table.concat{ pStat, ' ', colorMdl._colorTemplates("Yellow", table.concat{'(+', pVal, ')'}) }
	end
	
	for i, tData in ipairs({ helmetData, chestData, legsData, bootsData, totalData }) do
		local useHpbs = tData['hpbs'] or allHpbs
		local def = tData['def']
		local hp = tData['hp']
		if useHpbs then
			local hpbsVal = 20 * ((i == 5 and tData['hpbs']) and tonumber(tData['hpbs']) or 1)
			if useBlazePet then hpbsVal = hpbsVal * 2 end
			
			def = tData['def'] and hpbsStat(tData['def'], hpbsVal) or tData['def']
			hp = tData['hp'] and hpbsStat(tData['hp'], hpbsVal*2) or tData['hp']
		end
		
		tData['statslist'] = tData['manual'] or makeHtmlStatsList({
			def = def,
			hp = hp,
			str = tData['str'],
			int = tData['int'],
			spd = (tData['spd'] or ''):gsub('%%', ''),
			cc = (tData['critchance'] or ''):gsub('%%', ''),
			cd = (tData['critdmg'] or ''):gsub('%%', ''),
			td = tData['trudef'],
		})
	
		tData['exists'] = tData['img'] or tData['color'] or tData['manual'] or tData['def'] or tData['hp'] or tData['str'] or tData['int'] or tData['spd'] or tData['critchance'] or tData['critdmg'] or tData['trudef']
	end
	
	local function getDefaultImage(pType, pIsLink)
		local link = table.concat{'File:', title:gsub('Armor', pType), '.png'}
		if pIsLink then link = table.concat{'[[', link, '|40px|center]]'} end
		return link
	end
	
	local function makeImageCell(pRow, pData, pType)
		local td = pRow:tag('td'):attr('id', pType)
		
		if pData['exists'] or defaultImages then
			if pData['img'] then
				td:addClass('as2x2-icon'):wikitext(table.concat{'[[File:', pData['img'], '|40px|center]]'})
				
			elseif pData['color'] then
				td:addClass('as2x2-icon'):wikitext(table.concat{'{{', pType, '|', pData['color'], '|size=48}}'})
				
			elseif defaultImages then
				td:wikitext(getDefaultImage(pType, true))
				
			else
				td:wikitext('<center>{{ImageNeeded}}</center>')
			end
		else
			td:attr('colspan', 2):css{ ['border-right-width'] = '2px' }:wikitext('{{Blank cell}}')
		end
		return td
	end
	
	local function makeCellCollapsible(pCell, pCollapsed)
		pCell
		:addClass('mw-collapsible')
		:attr('id', 'mw-customcollapsible-pcb-toggle-button')
		
		if pCollapsed then
			pCell:addClass('mw-collapsed')
		end
	end
	
	local function makeDataCell(pRow, pData)
		if pData['exists'] then
			local td = row:tag('td'):wikitext(pData['statslist'])
			:css({ ['border-right-width'] = '2px' })
			
			if showPcb or showPcbR1 then
				-- make cell collapsible
				makeCellCollapsible(td)
				
				-- add a second collapsed cell to allow user to toggle between both cells
				local td2 = row:tag('td'):css({ ['border-right-width'] = '2px' })
				makeCellCollapsible(td2, true)
				
				if pData['pcb'] or pData['pcb_desc'] then
					if pData['pcb'] then
						td2:tag('div'):wikitext(ability.pieceBonus{ pData['pcb'] }) 
					end
					td2:wikitext(pData['pcb_desc'])
				else
					td2:wikitext('{{Blank cell}}')
				end
			end
		end
	end
	
	------------
	-- Start making string
	------------
	
	local t = {}
	
	if useHeader then
		t[#t+1] = '<h2>Armor Stats</h2>\n'
	end
	
	if usePcb then
		t[#t+1] = '<span style=\'font-size:20px\'>\'\'\'Note:\'\'\' You Can Click on the \'\'\'Orange\'\'\' Button below to Show/Hide the Piece Bonuses</span>\n'
	end
	
	local wikitable = mw.html.create('table'):addClass('wikitable armorstats2x2'):css{ ['border-width'] = '2px', ['border-color'] = '#aaa' };
	
	if usePcb then
		wikitable:tag('tr'):tag('th'):attr('colspan', 4):wikitext(elementMdl._collapsibleButton{
			id = 'pcb-toggle-button',
			text = 'Show/Hide Piece Bonuses'
		})
	end
	
	-- Helmet / Chestplate label name
	wikitable:tag('tr')
		:tag('th'):attr('colspan', 2):css{ ['border-right-width'] = '2px' }
			:wikitext(helmetData['special_name'] or 'Helmet'):done()
		:tag('th'):attr('colspan', 2)
			:wikitext(chestData['special_name'] or 'Chestplate'):done()
	
	-- Helmet / Chestplate image and data row
	row = wikitable:tag('tr')
	
	makeImageCell(row, helmetData, 'Helmet')
	makeDataCell(row, helmetData)
	
	makeImageCell(row, chestData, 'Chestplate')
	makeDataCell(row, chestData)
	
	-- Legs / Boots label name
	wikitable:tag('tr')
		:tag('th'):attr('colspan', 2):css{ ['border-right-width'] = '2px', ['border-top-width'] = '2px' }
			:wikitext(legsData['special_name'] or 'Leggings'):done()
		:tag('th'):attr('colspan', 2):css{ ['border-top-width'] = '2px' }
			:wikitext(bootsData['special_name'] or 'Boots'):done()
	
	-- Legs / Boots image and data row
	row = wikitable:tag('tr')
	
	makeImageCell(row, legsData, 'Leggings')
	makeDataCell(row, legsData)
	
	makeImageCell(row, bootsData, 'Boots')
	makeDataCell(row, bootsData)
	
	-- Total
	if totalData['exists'] then
		local pcbTotal = showPcb or showPcbR1 or showPcbR2
	
		row = wikitable:tag('tr')
		td = row:tag('th'):attr('colspan', 4):wikitext('Total'):css{ ['border-right-width'] = '2px', ['border-top-width'] = '2px' }
		if pcbTotal then makeCellCollapsible(td) end
	
		row = wikitable:tag('tr')
		td = row:tag('td'):attr('colspan', 4):wikitext(totalData['statslist']):css{ ['border-right-width'] = '2px' }
		if pcbTotal then makeCellCollapsible(td) end
	end
	
	-- Finished table
	t[#t+1] = tostring(wikitable)
	
	-- Add stuff after table
	
	-- Additional Effects
	if additionalEffects then
		t[#t+1] = additionalEffects .. '<br /><br />'
	end
	
	-- Full Set Bonus
	if fsbName then
		t[#t+1] = table.concat{ ability.fullSetBonus{ fsbName }, '<br>' }
	end
	if fsbDesc then t[#t+1] = fsbDesc end
	
	if fsb2Name then
		t[#t+1] = table.concat{ '<br><br>', ability.fullSetBonus{ fsb2Name }, '&#32;-&#32;' }
	end
	if fsb2Desc then t[#t+1] = fsb2Desc end
	
	-- Piece Bonus
	if pcbName then
		t[#t+1] = table.concat{ '<br/>Each piece also has the following ', ability.pieceBonus{ pcbName }, ' - ', pcbDesc }
	end
	
	-- Note
	if note then
		t[#t+1] = '<br>\'\'\'Note:\'\'\' ' .. note
	end
	
	return table.concat(t);
end

-----------------------------------------------------------------------------
--Template:Fairy Armor Stage
--
--Retrieves the color of specified armor piece on specific stage (1-46). Outputs either {{Color Display}}, image, or color hex code
-----------------------------------------------------------------------------
function p.FairyArmorStage(frame)
	local args = getArgs(frame)
	
	local stage = args[1]
	local piece = args['piece'] or args['p'] or args[2]
	local output_type = args['type'] or args['t']
	local imgSize = args['size'] or args['s']
	
	return p._FairyArmorStage(stage, piece, output_type, imgSize)
end
function p._FairyArmorStage(stage, piece, output_type, imgSize)
	--make all variables usable and consistent
	stage = tonumber(stage)
	if not output_type then output_type = 'raw' end
	if not imgSize then imgSize = '64px' else if not imgSize:find('px') then imgSize = imgSize .. 'px' end end
	if not piece then piece = 'helmet' end
	
	if stage < 1 or stage > 46 then return error('Stage exceeds the maximum range (1-46). Specified: "' .. stage .. '"') end
	
	--check what ouotput is needed
	if output_type:lower() == 'image' or output_type:lower() == 'img' then
		--return proper value for the stage and armor piece
		if piece:lower() == 'helmet' or piece:lower() == 'h' or piece:lower() == 1 then
			return '[[File:Fairy\'s Fedora (' .. fairyArmorData[stage].helmet .. ').png|' .. imgSize .. ']]'
		elseif piece:lower() == 'chestplate' or piece:lower() == 'c' or piece:lower() == 2 then
			return '[[File:Fairy\'s Polo (' .. fairyArmorData[stage].chest .. ').png|' .. imgSize .. ']]'
		elseif piece:lower() == 'leggings' or piece:lower() == 'l' or piece:lower() == 3 then
			return '[[File:Fairy\'s Trousers (' .. fairyArmorData[stage].legs .. ').png|' .. imgSize .. ']]'
		elseif piece:lower() == 'boots' or piece:lower() == 'b' or piece:lower() == 4 then
			return '[[File:Fairy\'s Galoshes (' .. fairyArmorData[stage].boots .. ').png|' .. imgSize .. ']]'
		--return error if the piece name is invalid
		else error('Invalid armor piece "' .. piece .. '".')
		end
	elseif output_type:lower() == 'color' or output_type:lower() == 'col' then
		--return proper value for the stage and armor piece
		if piece:lower() == 'helmet' or piece:lower() == 'h' or piece:lower() == 1 then
			return colorMdl._colorDisplay('#' .. fairyArmorData[stage].helmet)
		elseif piece:lower() == 'chestplate' or piece:lower() == 'c' or piece:lower() == 2 then
			return colorMdl._colorDisplay('#' .. fairyArmorData[stage].chest)
		elseif piece:lower() == 'leggings' or piece:lower() == 'l' or piece:lower() == 3 then
			return colorMdl._colorDisplay('#' .. fairyArmorData[stage].legs)
		elseif piece:lower() == 'boots' or piece:lower() == 'b' or piece:lower() == 4 then
			return colorMdl._colorDisplay('#' .. fairyArmorData[stage].boots)
		--return error if the piece name is invalid
		else error('Invalid armor piece "' .. piece .. '".')
		end
	elseif output_type:lower() == 'raw' or output_type:lower() == 'r' then
		--return proper value for the stage and armor piece
		if piece:lower() == 'helmet' or piece:lower() == 'h' or piece:lower() == 1 then
			return '#' .. fairyArmorData[stage].helmet
		elseif piece:lower() == 'chestplate' or piece:lower() == 'c' or piece:lower() == 2 then
			return '#' .. fairyArmorData[stage].chest
		elseif piece:lower() == 'leggings' or piece:lower() == 'l' or piece:lower() == 3 then
			return '#' .. fairyArmorData[stage].legs
		elseif piece:lower() == 'boots' or piece:lower() == 'b' or piece:lower() == 4 then
			return '#' .. fairyArmorData[stage].boots
		--return error if the piece name is invalid
		else error('Invalid armor piece "' .. piece .. '".')
		end
	else error('Invalid type "' .. output_type .. '".')
	end
end

-----------------------------------------------------------------------------
--Template:Fairy Armor Stages Table
--
--Produces the table from Fairy Armor page
-----------------------------------------------------------------------------
function p.FairyArmorStagesTable()
	--create table
	local wikitable = mw.html.create('table'):addClass('wikitable centertext')
	--construct the header
	wikitable:tag('tr')
		:tag('th'):wikitext('Stage'):done()
		:tag('th'):wikitext('Colors<sup><abbr title=\'From top to bottom: Fedora, Polo, Trousers, Galoshes.\'>ⓘ</abbr></sup>'):done()
		:tag('th'):wikitext('Fedora'):css('width', '100px'):done()
		:tag('th'):wikitext('Polo'):css('width', '100px'):done()
		:tag('th'):wikitext('Trousers'):css('width', '100px'):done()
		:tag('th'):wikitext('Galoshes'):css('width', '100px'):done()
	:done()
	--construct each row
	for i = 1, 46, 1 do
		(i % 2 == 0 and wikitable:tag('tr'):addClass('oddrow') or wikitable:tag('tr')) --set oddrows
			:tag('th'):wikitext(i):done()
			:tag('td'):wikitext(table.concat({
					p._FairyArmorStage(i, 'helmet', 'color') .. '<br/>',
					p._FairyArmorStage(i, 'chestplate', 'color') .. '<br/>',
					p._FairyArmorStage(i, 'leggings', 'color') .. '<br/>',
					p._FairyArmorStage(i, 'boots', 'color')
				})):done()
			:tag('td'):wikitext(p._FairyArmorStage(i, 'helmet', 'img')):done()
			:tag('td'):wikitext(p._FairyArmorStage(i, 'chestplate', 'img')):done()
			:tag('td'):wikitext(p._FairyArmorStage(i, 'leggings', 'img')):done()
			:tag('td'):wikitext(p._FairyArmorStage(i, 'boots', 'img')):done()
		:done()
	end
	return tostring(wikitable)
end

--Finish Module
return p

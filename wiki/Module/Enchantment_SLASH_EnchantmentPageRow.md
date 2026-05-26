local loader = require('Module:Loader')
local getArgs = require('Module:Arguments').getArgs
local string, table, rarity, link, skillname = loader.require('String', 'Table', 'RarityTier', 'Link', 'Skillname')
local enchData = loader.require('Enchantment/Data')

local p = {}

local function makeMinetip(s, tooltip)
	return tostring(
		mw.html.create('span'):addClass('minetip linetip')
			:attr('data-minetip-title', tooltip)
			:wikitext(s)
	)
end

local function isEnchantmentLevelValid(ench, i)
	return ((ench.vars or {})[1] or {})[i] ~= nil or (ench.cost or {})[i] ~= nil	
end

local function getMinLevel(ench)
	for i = 1, ench.max do
		if isEnchantmentLevelValid(ench, i) then
			return i	
		end
	end
	return 1
end

local function getAffectsSection(affects)
	affects = string.parseTextList( affects, '*' )
	
	local cont = mw.html.create('div'):addClass('enchaffectsdiv')
	cont:tag('b'):wikitext('Affects:')
	cont:tag('div'):wikitext(table.concat{
		'<span>',
		table.concat(affects, '</span><span>'),
		'</span>'
	})
	
	return tostring(cont)
end

local function parseSources(source, ench)
	if not source then return nil end
	
	-- escapes asterixs in slot template tooltips (which always have &l in front of them)
	source = source:gsub('&amp;l%*', '&amp;l&ast;')
	source = string.parseTextList( source, '*' )
	
	local sourceMap = {}
	for i = 1, #source do
		local nums, str = unpack(string.split(source[i], '%s*~%s*'))
		if str == nil then
			str = nums
			local minLevel = getMinLevel(ench)
			-- If source is just a string with no tier/span data, then just make it take up whole thing
			sourceMap[minLevel] = { colspan=ench.max - (minLevel-1), text=str }
		else
			local tier, span = unpack(string.split(nums, 'span'))
			sourceMap[tonumber(tier)] = { colspan=tonumber(span) or 1, text=str }
		end
	end
	return sourceMap
end

-------------------------------------------------------
-- Generates multiple rows needed for a single potion on Potions page
-- Invoked by Template:PotionPageRow
-------------------------------------------------------
function p.enchantmentPageRow(frame)
	local args = getArgs(frame)
	local name = args[1]
	local affects = args['affects']
	local desc = args['desc']
	local source = args['source']
	local alt_ids = args['alt_ids'] -- used by Turbo-Crop to allow linking multiple enchantments to one row
	
	return p._enchantmentPageRow(name, affects, desc, source, alt_ids)
end
function p._enchantmentPageRow(enchantName, affects, desc, source, alt_ids)
	local ench = enchData[enchantName]
	if not ench then
		return string._error('Invalid enchantment name \"' .. enchantName .. '\"')
	end
	local sourceMap = parseSources(source, ench)
	
	-- Basic Row Data
	local introTable = mw.html.create('table'):addClass('wikitable article-enchantments-table')
	if alt_ids then
		alt_ids = string.parseTextList( alt_ids, '*' )
		for i = 1, #alt_ids do
			introTable:tag('tr'):addClass('article-row-before'):attr('id', alt_ids[i])
				:tag('td'):css{ display='none' }:done()
		end
	end
	local row1 = introTable:tag('tr'):css{ height="37px" }
	local temp = row1:attr{ id=enchantName }:addClass('article-row-main')
		-- max width added purely for stylistic reasons on wider table
		:tag('th'):addClass('lefttxt'):attr{ colspan=2 }
			:tag('div'):addClass('enchnamediv')
				:tag('div')
					:wikitext( link.enchantmentsLink{ enchantName } )
				:done()
				if ench.req and ench.req > 0 then
					-- note: parent div hasn't been `done()` yet, so `temp` here is adding it to the parent div, not the row or cell - basically this just acts as a continuation
					temp:tag('span'):addClass('enchreqdiv')
						:tag('b'):wikitext(table.concat{ skillname.getSkillName{ 'enchanting', short=true }, ' Lvl: ' }):done()
						:tag('span'):wikitext( ench.req ):done()
					:done()
				end
			temp:done()
		:done()
	
	
	
	
	local row2 = introTable:tag('tr'):addClass('enchdisctr'):addClass('article-row-bound') -- 100% height needed for cell contents to use 100% height
		:tag('td'):addClass('seperator-cell'):wikitext(table.concat{
			affects and getAffectsSection(affects) or '',
			desc or 'Unknown description'
		}):done()
		:done()
	
	-- Level data half of table / data sub table
	local dataTable = mw.html.create('table'):addClass('wikitable centertext article-enchantments-table')
	local dataRow1 = dataTable:tag('tr'):css{ height="37px" }
	local dataRow2 = dataTable:tag('tr'):css{ ['line-height']='1.3' }
	local dataRow3 = dataTable:tag('tr'):css{ ['line-height']='1.3' }
	
	-- Add level data to rows
	local numDataColumns = ench.max;
	local lastLevelWithItem = 0
	for i = 1, ench.max do
		-- This if checks if both vars and cost for this tier are nil, and skips it if they are (needed for enchants that don't start at 1)
		if isEnchantmentLevelValid(ench, i) then
			dataRow1:tag('th'):wikitext( rarity._link(ench.rarity[i], ench.cost[i] and makeMinetip(string._toRoman(i), table.concat{ '&7Apply Cost: &3', ench.cost[i], ' Exp Levels' }) or string._toRoman(i), false, true) ):css{ width=(100/numDataColumns)..'%' }
			
			if ench.vars then
				local levelVars = {}
				for j, varList in pairs(ench.vars) do
					levelVars[#levelVars+1] = varList[i]
				end
				dataRow2:tag('td'):wikitext( table.concat(levelVars, '<br />') )
			end
			
			if sourceMap then
				if sourceMap[i] then
					dataRow3:tag('td'):attr('colspan', sourceMap[i]['colspan']):addClass('seperator-cell'):wikitext( sourceMap[i]['text'] )
				end
			elseif i == 1 then
				dataRow3:tag('td'):attr('colspan', ench.max):addClass('seperator-cell'):wikitext( string.blankCell() )
			end
			
			if not sourceMap and not ench.vars then
				dataRow2:tag('td'):addClass('seperator-cell')
					:wikitext( '&nbsp;'..string.blankCell() )
					:attr{ rowspan=2 }
			end
			
		end
	end
	
	return table.concat{ tostring(introTable), tostring(dataTable) }
end

return p

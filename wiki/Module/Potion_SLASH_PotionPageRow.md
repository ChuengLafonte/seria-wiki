local getArgs = require('Module:Arguments').getArgs
local loader = require('Module:Loader')
local string, table, yesno, uitext, inventoryslot, link, rarity = loader.require('String', 'Table', 'Yesno', 'UIText', 'Inventory slot', 'Link', 'RarityTier')
local potionData, potionAliases = loader.loadData('Potion/Data', 'Potion/Aliases')

local p = {}
local slot = inventoryslot.slot
local potionPageRowLevelBoosters = {
	string.wrapHtml('+[[File:Glowstone Dust.png|22x22px|link=]]', 'span', { class='cursor-help', style={ opacity=0.5 }, title='Glowstone Dust' }),
	string.wrapHtml('+[[File:Enchanted Glowstone Dust.png|22x22px|link=]]', 'span', { class='cursor-help', style={ opacity=0.5 }, title='Enchanted Glowstone Dust' }),
	string.wrapHtml('+[[File:Enchanted Glowstone.png|22x22px|link=]]', 'span', { class='cursor-help', style={ opacity=0.5 }, title='Enchanted Glowstone' }),
}

-------------------------------------------------------
-- Generates multiple rows needed for a single potion on Potions page
-- Invoked by Template:PotionPageRow
-------------------------------------------------------
function p.potionPageRow(frame)
	local args = getArgs(frame)
	local name = args['name']
	local nameNote = args['nameNote']
	local effect = args['effect']
	local varnames = args['varnames']
	local unlock = args['unlock']
	local brews = args['brews']
	
	return p._potionPageRow(name, nameNote, effect, varnames, unlock, brews)
end
function p._potionPageRow(name, nameNote, effect, varnames, unlock, brews)
	name = potionAliases[name:lower()]
	local pd = potionData[name]
	if not pd then
		return string._error('Invalid potion name \"' .. name .. '\"')
	end
	
	-- Basic Row Data
	local introTable = mw.html.create('table'):addClass('wikitable')
		:css{ height="100%" } -- This and other 100% on lable elements below are required for 100% height to work inside the description cell
	local row1 = introTable:tag('tr'):css{ height="36px" }
	local temp = row1:attr{ id=name }:addClass('article-row-main')
		-- max width added purely for stylistic reasons on wider table
		:tag('th'):attr{ colspan=2 }:css{ ['text-align']='left !important' }
			:tag('div'):css{ display='flex', gap='16px' }
				:tag('div')
					:wikitext( link.potionName{ name.." I Potion", format=true, bold=true } )
					:wikitext( nameNote )
				:done()
				if unlock then
					-- note: parent div hasn't been `done()` yet, so `temp` here is adding it to the parent div, not the row or cell - basically this just acts as a continuation
					temp:tag('span'):css{ flex=1, ['text-align']='right' }
						:tag('b'):wikitext('Unlock: '):done()
						:tag('span'):wikitext( unlock ):css{ ['font-weight']='normal' }:done()
					:done()
				end
			temp:done()
		:done()
	
	local row2 = introTable:tag('tr'):addClass('article-row-bound'):css{ height='100%' }--100% height needed for cell contents to use 100% height
		:tag('th'):wikitext( slot{ name.." I Potion" } ):addClass('seperator-cell'):css{ ['max-width']='36px', width='36px', ['box-sizing']='content-box' }:done()
		:tag('td'):css{ ['text-align']='left' }:addClass('seperator-cell'):css{ height='100%' }--100% height needed for cell contents to use 100% height
			:tag('div'):css{ display='flex', ['flex-direction']='column' }:css{ height='100%' }--100% height needed for cell contents to use 100% height
				:tag('div'):css{ flex=1 } -- this flex pushes the varnames text down (if there is any)
					:wikitext(effect or 'Unknown effect')
					:wikitext(
						brews and string.wrapHtml('<b style="vertical-align:top;">Compatible Brews:</b> \n'..brews, 'div', { style={ margin='5px 0 0 5px', ['border-top']='1px solid #FFFFFF33', ['padding-top']='3px' } }) or ''
					)
				:done()
				:wikitext( varnames and string.wrapHtml(table.concat{ '(in ', varnames, ')' }, 'div', { style={ ['text-align']='right', ['font-style']='italic' } }) or '' )
			:done()
		:done()
	
	-- Level data half of table / data sub table
	local dataTable = mw.html.create('table'):addClass('wikitable centertext')
	local dataRow1 = dataTable:tag('tr'):css{ height="36px" }
	local dataRow2 = dataTable:tag('tr')
	local dataRow3 = dataTable:tag('tr'):css{ ['line-height']='1.3' }
	
	local numDataColumns = basePotion and pd.maxLevel+1 or pd.maxLevel;
	local basePotion = pd.ingredients and pd.ingredients.basePotion
	local basePotionUsedForLevel = pd.ingredients and pd.ingredients.basePotionUsedForLevel
	
	if basePotion then
		dataRow1:tag('th')
			:tag('abbr'):wikitext('Base<br />Potion'):attr{ title='Some potions require a non-typical base to be used instead of an Awkward Potion' }:done()
		dataRow2:tag('td'):wikitext( slot{ basePotion } ):addClass('seperator-cell'):attr{ rowspan=2 }
		
		if basePotionUsedForLevel then
			dataRow2:tag('td'):wikitext( slot{ pd.ingredients[1] } ):css{ ['border-right']='0 !important' }
			dataRow2:tag('td'):wikitext( '(level based on level of base potion)' ):attr{ colspan=(pd.maxLevel-1) }:css{ ['border-left']='0 !important' }
		end
	end
	
	-- Add level data to rows
	local lastLevelWithItem = 0
	for i = 1, pd.maxLevel do
		dataRow1:tag('th'):wikitext( rarity._link(pd.rarity[i] or 'c', string._toRoman(i), false, true) ):css{ width=(100/numDataColumns)..'%' }
		
		-- potions can have ingredients, level-specific stats, or both!
		local singleDataRow = not (pd.ingredients and pd.vars)
		-- Don't draw ingredient column if base potion used for level, as we already added a colspan for here previously
		if pd.ingredients and not basePotionUsedForLevel then
			local ingredient = nil
			if pd.ingredients[i] then 
				ingredient = slot{ pd.ingredients[i] }
				lastLevelWithItem = i
			elseif pd.ingredients[i..'text'] then 
				ingredient = pd.ingredients[i..'text']
				lastLevelWithItem = i
			else
				ingredient = potionPageRowLevelBoosters[i-lastLevelWithItem]
			end
			
			local cell = dataRow2:tag('td'):wikitext( ingredient or '?' )
			if singleDataRow then
				cell:attr{ rowspan=2 }:addClass('seperator-cell')
			end
		end
		
		-- If ingredients exist, show them; if not, then only list the stats
		if pd.vars then
			local levelVars = {}
			for j, varList in pairs(pd.vars) do
				levelVars[#levelVars+1] = varList[i]
			end
			(singleDataRow and dataRow2 or dataRow3):tag('td'):addClass('seperator-cell')
				:wikitext( table.concat(levelVars, '<br />') )
		end
		
		if not pd.ingredients and not pd.vars then
			dataRow2:tag('td'):addClass('seperator-cell')
				:wikitext( '&nbsp;'..string.blankCell() )
				:attr{ rowspan=2 }
		end
		
	end
	
	return table.concat{ tostring(introTable), tostring(dataTable) }
end

return p

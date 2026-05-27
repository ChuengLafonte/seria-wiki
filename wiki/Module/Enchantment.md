local loader = require('Module:Loader')
local string, stringtemplates, table, yesno, mctxt, rarity = loader.require('String', 'String/Templates', 'Table', 'Yesno', 'Mctxt', 'RarityTier')
local getArgs = require('Module:Arguments').getArgs
local enchData = loader.require('Enchantment/Data')

local p = {}
local unknownDisplay = '&r&f&l???&r'

-------------------------------------------------------
-- Generates table for Module:Inventory slot/Templates
-------------------------------------------------------
function p.getEnchantedBooksTemplate()
	local function toDoubleTable(v)
		local t = type(v) == 'table' and table.deepCopy(v, true) or {v}
		t = type(t[1]) == 'table' and t or {t}
		return t
	end
	local function toTable(v)
		local t = type(v) == 'table' and table.deepCopy(v, true) or {v}
		return t
	end
	
	local ret = { id = 'Enchanted Book ({o})' }
	for enchname, value in pairs(enchData) do
		local g_desc, ultimate, nocombine = value.desc or unknownDisplay, value.isUltimate, value.noCombine
		local variables, costTbl, upgradesTbl, rarityTbl, awardTbl = toDoubleTable(value.vars), toTable(value.cost), toTable(value.upgrades), toTable(value.rarity), toTable(value.awardReq)
		
		for tier = 1, value.max, 1 do
			local name, arabicname, link, displayname, upgradeType, tierup, awardReq, ultWarning, cost, combineWarning, requirement, rarity
			local desc = g_desc
			
			name = ('%s %s'):format(enchname, string._toRoman(tier))
			arabicname = ('%s %s'):format(enchname, tier)
			link = value.link or enchname
			
			displayname = (ultimate and '&d&l' or '&9') .. (name)
			
			for i, var in ipairs(variables) do
				desc = desc:gsub(('{%d}'):format(i-1), var[tier] or unknownDisplay)
			end
			desc = desc:gsub('{%d}', unknownDisplay)
			
			tierup = (string._toNumber(upgradesTbl[tier]) or -1) > 0
				and ('&r&8%s %s to tier up!/'):format(upgradesTbl[tier], value.upgradeType or 'blocks') or ''
			
			awardReq = awardTbl[tier] ~= nil
				and ('&r&7Requires %s &r&7in &a%s &r&7contest!/'):format(awardTbl[tier] or unknownDisplay, value.contest) or ''
			
			ultWarning = ultimate and '/&cYou can only have 1 Ultimate/&cEnchantment on an item!/' or ''
			
			cost = tonumber(costTbl[tier]) ~= 0
				and ('/&r&7Apply Cost: &3%s Exp Levels/'):format(costTbl[tier] or unknownDisplay) or ''
			
			combineWarning = nocombine and ('&e▲ %s%s cannot be combined!/'):format(ultimate and '&d&l' or '&7', enchname) or ''
			
			requirement = (tonumber(value.req) or -1) > 0 and ('&cRequires Enchanting %d to/&capply.//'):format(tonumber(value.req)) or ''
			
			rarity = rarityTbl[tier] or 'common'
			
			local everything = table.concat({
				displayname, '/',
				desc, '/',
				tierup,
				awardReq,
				ultWarning,
				cost, '/',
				combineWarning,
				requirement
			}, '&r')
			table.push(ret, {name, link, everything, r = rarity})
			-- table.push(ret, {arabicname, link, everything, r = rarity})
			if tier == 1 then
				table.push(ret, {enchname, link, everything, r = rarity})
			end
		end
	end
	return ret
end
-------------------------------------------------------
-- Generates table for Module:Item/Variants
-------------------------------------------------------
function p.expandEnchantedBookAll()
	local ret = {}
	for enchname, value in pairs(enchData) do
		ret[#ret + 1] = ('Enchanted Book (%s)'):format(enchname)
	end
	return ret
end
function p.expandEnchantedBookType()
	local ret = {}
	for enchname, value in pairs(enchData) do
		local t = {}
		for tier = 1, value.max, 1 do
			t[#t + 1] = ('Enchanted Book (%s %s)'):format(enchname, string._toRoman(tier))
		end
		ret[('Enchanted Book (%s)'):format(enchname)] = t
	end
	return ret
end

function p.listSearchSuggestions(frame)
	local suggestions = {}
	for enchant,v in pairs(enchData) do
		suggestions[#suggestions+1] = enchant
	end
	return table.concat(suggestions, ",")
end

function p.displayEnchantmentData(frame)
	local args = getArgs(frame)
	
	local enchantName = args[1]
	
	return p._displayEnchantmentData(enchantName)
end

function p._displayEnchantmentData(enchantName)
	local enchant = enchData[enchantName]
	
	if not enchant then
		return string.wrapHtml("Enchantment not found", 'div', {style='color:red'})
	end
	
	local t = {}
	
	t[#t+1] = string.wrapHtml(mw.getCurrentFrame():preprocess("{{Ench|"..enchantName.."}}"), 'h3')
	t[#t+1] = mw.getCurrentFrame():preprocess(string.wrapHtml(mctxt._raw(enchant.desc), 'p'))
	
	t[#t+1] = tostring(mw.html.create('ul')
		:tag('li'):wikitext("'''Enchanting Level Required:''' "..enchant.req):done()
	)
	
	if enchant.vars or enchant.cost then
		local wikitable = mw.html.create('table'):addClass('wikitable centertext')
		
		-- Header rows
		
		local rowH = wikitable:tag('tr')
		rowH:tag('th'):attr('colspan', 2):wikitext("")
		
		local effectRows = {}
		
		if enchant.vars then
			local VAR_VARS = { '<code>{0}</code>', '<code>{1}</code>', '<code>{2}</code>' }
			for vi,_ in ipairs(enchant.vars) do
				effectRows[#effectRows+1] = wikitable:tag('tr')
				if vi == 1 then
					effectRows[1]:tag('th'):attr('rowspan', #enchant.vars):wikitext("Effect(s)")
				end
				effectRows[vi]:tag('th'):wikitext(VAR_VARS[vi])
			end
		end
		
		local rowCost = wikitable:tag('tr')
		if enchant.cost then
			rowCost:tag('th'):attr('colspan', 2):wikitext("Exp Cost")
		end
		
		-- Data rows
		
		local TIERS = { 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X' }
		for i = 1, enchant.max, 1 do
			if enchant.rarity[i] ~= nil or (enchant.vars[1] and enchant.vars[1][i] ~= nil) then
				rowH:tag('th'):wikitext( enchant.rarity[i] and rarity._link(enchant.rarity[i], TIERS[i]) or TIERS[i])
				
				
				if enchant.vars then
					for vi,_ in ipairs(enchant.vars) do
						effectRows[vi]:tag('td'):wikitext( enchant.vars[vi][i] or stringtemplates.blankCell() )
					end
				end
				
				if enchant.cost then
					rowCost:tag('td'):wikitext( enchant.cost[i] or stringtemplates.blankCell() )
				end
			end
		end
		
		t[#t+1] = tostring(wikitable)
	end
	
	-- TODO: Rest of enchant data

	return table.concat(t)
end

return p
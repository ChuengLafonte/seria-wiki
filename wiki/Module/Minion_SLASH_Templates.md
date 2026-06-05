local string, table, minion = require('Module:String'), require('Module:Table'), require('Module:Minion')
local minionData = mw.loadData('Module:Minion/Data')

local function to(a, b)
	local arrow = '➜'
	return ('%s%s%s'):format(a, arrow, b)
end

local function minions()
	-- used on Module:Inventory slot/Templates
	local ret = {}
	
	table.each(table.keys(minionData), function(name)
		local stats = minionData[name].stats
		local description = {{ req = 1, minionData[name].description or 'Tidak ada deskripsi' }}
		table.merge(description, table.deepCopy(minionData[name].abilities or {}, true))
		local max = table.length(stats)
		local max_ = string._toRoman(max)
		
		for i, v in ipairs(stats) do
			local desc = table.concat(table.map(description, function (d)
				if (i >= d.req) then return d[1] end
			end), '//')
			if (v.tba and v.storage) then
				table.push(ret, { name, string._toRoman(i), desc, v.tba, v.storage, id = '{o} Minion {0}' })
			end
		end
		local f, l = stats[1], stats[max]
		if (f.tba and f.storage and l.tba and l.storage) then
			local desc = table.concat(table.map(description, function (d)
				return d[1]
			end), '//')
			table.push(ret, { name, to('I', max_), desc, to(f.tba, l.tba), to(f.storage, l.storage), id = '{o} Minion', name = '{o} Minion', image = '{o} Minion ' .. max_ })
		end
	end)
	
	return ret
end

local function skins()
	-- used on Module:Inventory slot/Templates
	return {
		{'Sloth Minion Skin', '&7a &eSloth', r='c'},
		{'Happy Emoji Minion Skin', '&7a &eHappy/&eEmoji', r='c'},
		{'Fish Minion Skin', '&ea/&eFish', r='c'},
		{'Pufferfish Minion Skin', '&ea/&ePufferfish', r='c'},
		{'Tropical Bird 2 Minion Skin', '&ea/&eTropical Bird 2', r='c'},
		{'Tropical Bird 1 Minion Skin', '&ea/&eTropical Bird 1', r='c'},
		{'White Tiger Minion Skin', '&ea White/&eTiger', r='c'},
		{'Festive Jerry Minion Skin', '&ea/&eFestive Jerry', r='c'},
		{'Festive Zombie Minion Skin', '&ea/&eFestive Zombie', r='c'},
		{'Festive Skeleton Minion Skin', '&ea/&eFestive Skeleton', r='c'},
		{'Cyclops Minion Skin', '&ea/&eCyclops', r='c'},
		{'Scarecrow Minion Skin', '&ea/&eScarecrow', r='c'},
		{'Shark Minion Skin', '&ea/&eShark', r='c'},
		{'Basketball Minion Skin', '&ea/&eBasketball', r='c'},
		{'Ghost Minion Skin', '&ea/&eGhost', r='c'},
		{'Pumpkin Minion Skin', '&ea/&ePumpkin', r='c'},
		{'Mummy Minion Skin', '&ea/&eMummy', r='c'},
		{'Penguin Minion Skin', '&ea/&ePenguin', r='c'},
		{'Pink Bunny Personality', '&ea &ePink/&eBunny', r='c'},
		{'Easter Egg Minion Skin', '&ean/&eEaster Egg', r='c'},
		{'Present Minion Skin', '&ea/&ePresent', r='c'},
		{'Reindeer Minion Skin', '&ea/&eReindeer', r='c'},
		{'Hermit Crab Minion Skin', '&ea/&eHermit Crab', r='c'},
		{'Pink Donut Minion Skin', '&ea &ePink/&eFrosted Donut', r='c'},
		{'Beach Ball Minion Skin', '&ea Beach/Ball', r='c'},
		{'Bee Minion Skin', '&ea/&eBee', r='c'},
		{'Bunny Minion Skin', '&ea/&eBunny', r='c'},
		{'Clownfish Minion Skin', '&ea &eClownfish', r='c'},
		{'Gingerbread Man Minion Skin', '&ea/&eGingerbread Man', r='c'},
		{'Grinch Minion Skin', '&ea/&eGrinch', r='c'},
		{'Ice Cream Minion Skin', '&ean Ice/&eCream', r='c'},
		{'Ice Lolly Minion Skin', '&ean Ice/&eLolly', r='c'},
		{'Killer Minion Skin', '&ea/&eKiller', r='c'},
		{'Lady Bug Minion Skin', '&ea &eLady/&eBug', r='c'},
		{'Melon Minion Skin', '&ea/&eMelon', r='c'},
		{'Sandcastle Minion Skin', '&ea/&eSandcastle', r='c'},
		{'Santa Minion Skin', '&ea/&eSanta', r='c'},
		{'Skull Minion Skin', '&ea/&eSkull', r='c'},
		{'Sun Minion Skin', '&ea/&eSun', r='c'},
		{'Undead Minion Skin', '&ean/&eUndead', r='c'},
		{'Snowman Minion Skin', '&7a &eSnowman', r='c'},
		{'Choco Rabbit Minion Skin', '&7a &eChoco/&eRabbit', r='e'},
		{'Seal Minion Skin', '&7a &eSeal', r='c'},
	}
end

local function expandMinionAll()
	-- return a table with all minions
	-- used on Module:Item/Variants
	local names = {}
	for name, _ in pairs(minionData) do
		names[#names + 1] = name .. ' Minion'
	end
	return names
end

local function expandMinionType()
	-- return a table with keys "... Minion" and values of all tiers of that minion
	-- used on Module:Item/Variants
	local perType = {}
	for name, _ in pairs(minionData) do
		local stats = minionData[name].stats
		perType[name .. ' Minion'] = table.map(stats, function(v,i)
	    	return name .. ' Minion ' .. string._toRoman(i)
		end)
	end
	return perType
end

return {
	minions = minions,
	skins = skins,
	expandMinionAll = expandMinionAll,
	expandMinionType = expandMinionType
}
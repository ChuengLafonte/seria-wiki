local loader = require('Module:Loader')

local string, table, yesno, rarityTier, statModule, petUtils =
	loader.lazy.require('String', 'Table', 'Yesno', 'RarityTier', 'Statname', 'Pet/Utils')
local petData, skinData, rarityAliases =
	loader.lazy.loadData('Pet/Data', 'Pet/Skins', 'RarityTier/Aliases')

local p = {}
local arrowsymbol = '➡'

-------------------------------------------------------
-- Generates table for Module:Inventory slot/Templates
-------------------------------------------------------
function p.getPetsTemplate()
	local allPackages = table.map(table.keys(petData), function(pet)
		local returnPackage = {}
		local data, pet, baselv, maxlv = petUtils.getPet(pet, true)
		
		if not data then return end
		if not data.rarities then return end
		if not data.variables then return end
		
		local leveldisplay = tonumber(baselv) + 1 .. arrowsymbol .. maxlv
		local allrarities = petUtils.discloseRarities(pet, true)
		
		for i, raritykey in ipairs(allrarities) do
			local raritykey = rarityAliases[raritykey]
			local petname = data.variables[raritykey] and data.variables[raritykey].petname
			
			local id = petUtils.petNameWithRarity(pet, raritykey)
			
			lvlarg = { baselv + 1, maxlv }
			if (baselv == maxlv) then
				lvlarg = baselv
			end
			local res = petUtils.petTemplateCreator(pet, lvlarg, raritykey, id)
			
			if petname then
				local res2 = table.deepCopy(res, true)
				res2['id'] = petname .. ' Pet'
				table.push(returnPackage, res2)
			end
			if i == #allrarities then
				local res2 = table.deepCopy(res, true)
				res2['id'] = '{o} Pet'
				table.push(returnPackage, res2)
			end
			
			table.push(returnPackage, res)
		end
		return returnPackage
	end)
	
	local ret = {}
	table.each(allPackages, function(pack)
		table.each(pack, function(t)
			table.push(ret, t)
		end)
	end)
	
	return ret
end

-------------------------------------------------------
-- Generates table for Module:Inventory slot/Templates
-------------------------------------------------------
function p.getMysteryTemplate()
	local ls = table.map(table.keys(petData), function(petname)
		local data = petData[petname]
		local baselv, maxlv = petUtils.getBaseMax(petname)
		local stats = {}
		local rarities = petUtils.discloseRarities(petname, true)
		local highestrarity = rarities[#rarities]
		local statValuesActual, statValuesRounded = petUtils._getStatByTable(
			data.variables[highestrarity].stats or data.stats, 1, highestrarity, baselv)
		for statCode, statValue in pairs(statValuesRounded) do
			local sdt = statModule._getstatdata(statCode)
			table.push(stats, ('&r%s: &a+%s%s'):format(sdt.name, statValue, sdt.percent and '%' or ''))
		end
		return { petname, data.petType, table.concat(stats, '/') }
	end)
	
	return table.merge(ls, { id = 'Mystery {o} Pet' })
end

-------------------------------------------------------
-- Generates table for Module:Inventory slot/Templates
-------------------------------------------------------
function p.getSkinsTemplate()
	local petSkinsTable = {}
	for petname, skins in pairs(skinData) do
		for _, v in ipairs(skins) do
			local attrs = string.split(v[2], '%s+')
			local r = rarityTier._getTier(attrs[1]).name
			table.remove(attrs, 1)
			local animated, daynight, factionadapt, lovehypixel = false, false, false, false
			for _, attr in ipairs(attrs) do
				if attr:lower() == 'animated' then
					animated = true
				elseif attr:lower() == 'daynight' then
					daynight = true
				elseif attr:lower() == 'factionadapt' then
					factionadapt = true
				elseif attr:lower() == 'lovehypixel' then
					lovehypixel = true
				end
			end
			local suppStr = (animated and daynight) and '&aThis skin is animated, and adapts to/&athe day-night cycle!//' or (
				(animated and '&aThis skin is animated!//' or '') ..
				(daynight and '&5This skin adapts to the day-night/&5cycle!//' or '')
			)
			suppStr = suppStr .. (factionadapt and '&5This skin adapts to your Crimson Isle/&5Faction!//' or '')
			suppStr = suppStr .. (lovehypixel and '&cMade with ❤ for hypixel//' or '')
			table.push(petSkinsTable, { ('%s %s Skin'):format(v[1], petname), petname, suppStr, r = r })
		end
	end
	return petSkinsTable
end

-------------------------------------------------------
-- For Module:Item/Variants
-------------------------------------------------------
function p.expandSkinAll()
	-- returns a list of skins
	local petSkinsTable = {}
	for pet, skins in pairs(skinData) do
		for _, v in ipairs(skins) do table.push(petSkinsTable, v[1] .. ' ' .. pet .. ' Skin') end
	end
	return petSkinsTable
end
function p.expandPetAll()
	-- return a table with keys "... Pet" and values of all tiers of that pet
	local names = {}
	for name, _ in pairs(petData) do
		names[#names + 1] = name .. ' Pet'
	end
	return names
end
function p.expandPetType()
	-- return a table with keys "... Pet" and values of all tiers of that pet
	local perType = {}
	for name, _ in pairs(petData) do
		local t = {}
		for _, raritykey in ipairs(petUtils.discloseRarities(name, true)) do
			t[#t + 1] = petUtils.petNameWithRarity(name, raritykey)
		end
		perType[name .. ' Pet'] = t
	end
	return perType
end
function p.expandPetTypeImage()
	local function inquireimages(pet_)
		if type(pet_) ~= 'string' then return end
		local dt, pet = petUtils.getPet(pet_)
		local rarities, variables = dt and dt.rarities, dt and dt.variables
		if not (pet and dt and rarities and variables) then return end
		local images = {}
		for _, r in ipairs(petUtils.discloseRarities(pet, true)) do
			table.push(images, variables[r].petimage or ('%s Pet'):format(variables[r].petname or pet))
		end
		local i = 1
		-- remove duplicates
		while i <= #images do
			local rm = false
			for j = i - 1, 1, -1 do
				if images[i] == images[j] then
					table.remove(images, i)
					rm = true
				end
				if rm then break end
			end
			i = i + (rm and 0 or 1)
		end
		return images
	end
	-- return a table with keys "... Pet" and values of all tiers of that pet
	local perType = {}
	for name, _ in pairs(petData) do
		perType['[Image]' .. name .. ' Pet'] = inquireimages(name)
	end
	return perType
end

return p
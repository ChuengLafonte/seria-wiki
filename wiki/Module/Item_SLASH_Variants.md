local table = require('Module:Table')
local string = require('Module:String')
local MCColors = require('Module:Color/Data').MCColors
local petTemplates = require('Module:Pet/Templates')
local minionTemplates = require('Module:Minion/Templates')
local potionM = require('Module:Potion')
local enchantmentM = require('Module:Enchantment')
local armorSets = mw.loadData('Module:Armor/Sets')

--------------------------------------------------------------------------------------------------------------
-- TABLE OF CONTENTS
-- 01: More aliases support: Conversion tables
-- 02: Main function for the aliases processing
-- 03: Main table for lists of item variants
-- 04: Individual procedures to generate lists of item variants
--------------------------------------------------------------------------------------------------------------
-- Notes:
-- 1. More aliases
-- Add additional aliases to the additionalAliases table
--------------------------------------------------------------------------------------------------------------

---------- 01: More aliases support: Conversion tables ----------
--[[
	Other names to copy from the original name must be declared here
--]]
local additionalAliases = {
	-- ['<existing item>'] = '<other name>'
    ['Sloth Hat of Celebration'] = 'Sloth Hat',
	['Crab Hat of Celebration'] = 'Crab Hat', 
}

local function main()
	local variants = {}
	
	local function gsubFn(...)
		-- Function for one or more gsub + trim
		-- function: gsubFn(<...>) | parameters must be in pairs of <pattern>, <repl>, and in order
		local args = { ... }
		assertFalse(#args % 2 == 1, 'gsubFn: Patterns and replacements not in pairs')
		return function(n)
			for i = 1, #args, 2 do
				n = n:gsub(args[i], args[i+1])
			end
			return string.trim(n)
		end
	end
	
	---------- 02: Main function for the aliases processing ----------
	local function createMultiAliases(name, items)
		local normalize = gsubFn('%$.', '')
		local function search(name)
			for k, v in pairs(additionalAliases) do
				if normalize(k) == normalize(name) then
					return v
				end
			end
			return {}
		end
		local allAliases = table.merge({}, name, search(name))
		items = table.map(items, normalize)
		for _, n in ipairs(allAliases) do -- Don't use pairs: we don't want named indexes
			variants[n] = table.map(items, function (v) return v:gsub('%$.', '') end)
		end
	end
	
	---------- 03: Main table for lists of item variants ----------
	--[[
		Mainly for adding items with lesser iteration
	--]]
	local itemVariants = {
		-- ['Item group'] = { 'Item1', <'Item2'> }
		-- MISC --
		['Biome Stick'] = table.map({ 
			'Birch Forest', 'Deep Ocean', 'Desert', 'End', 'Forest', 'Jungle', 'Nether', 'Roofed Forest', 'Savanna', 'Taiga',
		}, function(v) return v .. ' Biome Stick' end),
		['Music Disc'] = { 'Music Disc - Cat', 'Music Disc - Blocks', 'Music Disc - Far', 'Music Disc - Strad', 'Music Disc - Mellohi', 'Music Disc - Ward', 'Music Disc - Chirp', 'Music Disc - 11', 'Music Disc - 13', 'Music Disc - Stal', 'Music Disc - Mall', 'Music Disc - Wait' },
		['Custom Music Disc'] = { 'Spooky Disc', 'Battle Disc', 'Winter Disc', 'Dungeon Disc', 'Clown Disc', 'Watcher Disc', 'Necron Disc', 'Old Disc' },
		['Flower'] = { 'Dandelion', 'Poppy', 'Blue Orchid', 'Azure Bluet', 'Oxeye Daisy', 'Allium', 'Lilac', 'Rose Bush', 'White Tulip', 'Pink Tulip', 'Red Tulip', 'Orange Tulip', 'Sunflower', }, 
		['Mixin'] = { 'Zombie Brain Mixin', 'Spider Egg Mixin', 'Wolf Fur Mixin', 'End Portal Fumes', }, 
		['Lucky Block'] = { 'Green Lucky Block', 'Red Lucky Block', 'Yellow Lucky Block', }, 
		['Null Head'] = { 'Steve Head', 'Alex Head' }, 
		['Coin'] = { 'Iron Coin', 'Gold Coin', 'Diamond Coin', 'Emerald Coin', 'Redstone Coin', 'Lapis Coin' }, 
		['Travel Scroll'] = table.map({
			'Blazing Fortress','Deep Caverns','Dwarven Mines','the Gold Mine',
			'Mushroom Island','Spider\'s Den','the Barn','the End', 'the Void Sepulture',
			'The Park','Hub Castle','Dark Auction','Hub Crypts',
			'Spider\'s Den Top of Nest','Magma Fields','Dragon\'s Nest',
			'Jungle Island','Howling Cave','the Dwarven Base Camp',
		}, function(v) return 'Travel Scroll to ' .. v end),
		['Fishing Bait'] = { 'Minnow Bait', 'Fish Bait', 'Light Bait', 'Dark Bait', 'Spiked Bait', 'Spooky Bait', 'Carrot Bait', 'Blessed Bait', 'Whale Bait', 'Ice Bait', 'Frozen Bait', 'Shark Bait', 'Hot Bait', 'Corrupted Bait', 'Glowy Chum Bait', 'Worm Bait', 'Golden Bait'},
		['Brew'] = { 'Cheap Coffee', 'Tepid Green Tea', 'Pulpous Orange Juice', 'Bitter Ice Tea', 'KnockOff Cola', 'Decent Coffee', 'Viking\'s Tear', 'Tutti-Frutti Flavored Poison', 'Dctr. Paper', 'Slayer Energy Drink' },
		['Power Orb'] = { 'Radiant Power Orb', 'Mana Flux Power Orb', 'Overflux Power Orb', 'Plasmaflux Power Orb' },
		['Gift'] = { 'White Gift', 'Green Gift', 'Red Gift', },
		['Candy'] = { 'Green Candy', 'Purple Candy' },
		['2020 Crab Hat of Celebration'] = table.map({
			'Red','Orange','Yellow','Lime','Green','Aqua','Purple','Pink','Black',
		}, function(v) return v .. ' Crab Hat of Celebration' end),
		['2022 Crab Hat of Celebration'] = table.map({
			'Red','Orange','Yellow','Lime','Green','Aqua','Purple','Pink','Black',
		}, function(v) return v .. ' Crab Hat of Celebration - 2022 Edition' end),
		['Sloth Hat of Celebration'] = table.map({
			'Cheeky','Cool','Cute','Derp','Flushed','Grumpy','Happy','Regular','Shock','Tears',
		}, function(v) return v .. ' Sloth Hat of Celebration' end),
		['5th Anniversary Balloon Hat'] = table.map({
			'Red','Orange','Yellow','Lime','Green','Aqua','Purple','Pink','Black',
		}, function(v) return v .. ' 5th Anniversary Balloon Hat' end),
		['6th Anniversary Balloon Hat'] = table.map({
			'Red','Orange','Yellow','Lime','Green','Aqua','Purple','Pink','Black',
		}, function(v) return v .. ' 6th Anniversary Balloon Hat' end),
		['Century Cake'] = { 'Crab-Colored Century Cake', 'Pet Rock Century Cake', 'aPunch Century Cake', 'Potato-Style Century Cake', 'Barry Century Cake', 'Sea Emperor Century Cake', 'Century Cake of the Next Dungeon Floor', 'Latest Update Century Cake', 'Streamer\'s Century Cake', 'Chocolate Century Cake', 'Cloudy Century Cake', 'Century Cake of Hype', 'Undead ༕ Century Cake', 'Not-a-lie Century Cake' },
		['Repelling Candle'] = table.map({
			'Red','Orange','Yellow','Green','Blue','Purple','Black','Pink','Lilac','Aqua','Cyan','Brown','Gray','White',
		}, function(v) return v .. ' Repelling Candle' end),
		['Minion Crystal'] = { 'Farm Crystal', 'Woodcutting Crystal', 'Mithril Crystal' },
		['Gemstone Crystal'] = { 'Ruby Crystal', 'Amber Crystal', 'Sapphire Crystal', 'Jade Crystal', 'Amethyst Crystal', 'Topaz Crystal', 'Jasper Crystal', 'Opal Crystal', 'Onyx Crystal', 'Citrine Crystal', 'Aquamarine Crystal', 'Peridot Crystal' },
		['Horse Armor'] = { 'Iron Horse Armor', 'Gold Horse Armor', 'Diamond Horse Armor' },
		['Mushroom'] = { 'Red Mushroom', 'Brown Mushroom' },
		['Enchanted Mushroom'] = { 'Enchanted Red Mushroom', 'Enchanted Brown Mushroom' },
		['Quartz Block'] = { 'Block of Quartz', 'Chiseled Quartz Block', 'Quartz Pillar' },
		['Red Sandstone'] = { 'Red Sandstone', 'Chiseled Red Sandstone', 'Smooth Red Sandstone' },
		['Sandstone'] = { 'Sandstone', 'Chiseled Sandstone', 'Smooth Sandstone' },
		['Stone Bricks'] = { 'Stone Bricks', 'Mossy Stone Bricks', 'Cracked Stone Bricks', 'Chiseled Stone Bricks' },
		['Stone Slab'] = { 'Sandstone Slab', 'Cobblestone Slab', 'Brick Slab', 'Stone Brick Slab', 'Nether Brick Slab', 'Quartz Slab' },
		['Stone'] = { 'Stone', 'Andesite', 'Granite', 'Diorite', 'Polished Andesite', 'Polished Granite', 'Polished Diorite' },
		['Tulip'] = { 'Red Tulip', 'Orange Tulip', 'White Tulip', 'Pink Tulip' },
		['Custom Dye'] = { 'Iceberg Dye', 'Aurora Dye', 'Aquamarine Dye', 'Bingo Blue Dye', 'Black Ice Dye', 'Bone Dye', 'Brick Red Dye', 'Byzantium Dye', 'Carmine Dye', 'Celadon Dye', 'Celeste Dye', 'Chocolate Dye', 'Cyclamen Dye', 'Dark Purple Dye', 'Emerald Dye', 'Flame Dye', 'Holly Dye', 'Livid Dye', 'Lava Dye', 'Lucky Dye', 'Mango Dye', 'Midnight Dye', 'Nadeshiko Dye', 'Necron Dye', 'Nyanza Dye', 'Pastel Sky Dye', 'Ocean Dye', 'Pastel Sky Dye', 'Portal Dye', 'Pure Black Dye', 'Pure Blue Dye', 'Pure White Dye', 'Pure Yellow Dye', 'Rose Dye', 'Snowflake Dye', 'Tentacle Dye', 'Warden Dye', 'Wild Strawberry Dye' }, -- put iceberg first for infobox to work
		['Abiphone'] = {'Abiphone X Plus', 'Abiphone X Plus Special Edition', 'Abiphone XI Ultra', 'Abiphone XI Ultra Style', 'Abiphone XII Mega', 'Abiphone XII Mega Color', 'Abiphone XIII Pro Giga'},
		['Abicase'] = {'Sumsung© G3 Abicase', 'Sumsung© GG Abicase', 'Rezar® Abicase', 'Blue™ but Red Abicase', 'Actually Blue™ Abicase', 'Blue™ but Green Abicase', 'Blue™ but Yellow Abicase', 'Lighter Blue™ Abicase'},
		['Trophy Fish'] = {'Blobfish', 'Flyfish', 'Golden Fish', 'Gusher', 'Karate Fish', 'Lavahorse', 'Mana Ray', 'Moldfin', 'Skeleton Fish', 'Slugfish', 'Soul Fish', 'Steaming-Hot Flounder', 'Sulphur Skitter', 'Vanille', 'Volcanic Stonefish', 'Obfuscated 1', 'Obfuscated 2', 'Obfuscated 3'},
		['Tiered Beacon'] = {'Beacon I', 'Beacon II', 'Beacon III', 'Beacon IV', 'Beacon V'},
		['Barn Skin'] = table.map({
			'Default', 'Medieval', 'Sunny', 'Red', 'Cabin', 'Mansion Heights', 'Trading Post', 'Autumn Hut', 'Bamboo', 'Hive', 'Castle', 'Cozy Cottage', 'Cube', 'Tavern', 'Windmill', 'Frog', 'Jerry', 'Pinwheel House', 'Mushroom', 'Melon', 'Lucky', 'Town Hall', 'Winter Homestead', 'The End', 'Enchanted Nook', 'Chocolate Factory', 'Beach Ball', 'Sand Castle', 'Beautifall Cabin', 'Pesthunter\'s Lair', 'Main Street', 'Butterfly', 'Flower Pot'}, function(v) return v .. ' Barn Skin' end),
		['Power Stone'] = {'Scorched Books', 'Vitamin Death', 'Hazmat Enderman', 'Mandraa', 'Eccentric Painting', 'Horns of Torment', 'Magma Urchin', 'Precious Pearl', 'End Stone Shulker', 'Beating Heart', 'Acacia Birdhouse', 'Furball', 'Obsidian Tablet', 'Dark Orb', 'Ender Monocle', 'Luxurious Spool', 'Rock Candy', 'Displaced Leech', 'Glacite Shard'},
		['Timecharm'] = {'Chicken N Egg Timecharm', 'Supreme Timecharm', 'mrahcemiT esrevrorriM', 'SkyBlock Citizen Timecharm', 'Living Timecharm', 'Globulate Timecharm', 'Vampiric Timecharm'},
		['Enchanted Book Bundle'] = {'Enchanted Book Bundle (Vicious)', 'Enchanted Book Bundle (Big Brain)', 'Enchanted Book Bundle (Reflection)', 'Enchanted Book Bundle (Quantum)', 'Enchanted Book Bundle (The One)', 'Enchanted Book Bundle (Rainbow)'},
		['Carnival Mask'] = {'Zombie Mask', 'Salmon Mask', 'Armadillo Mask', 'Parrot Mask', 'Snowman Mask', 'Bee Mask', 'Frog Mask'},
		['Greenhouse Skin'] = {'Default Greenhouse Skin', 'Estate Greenhouse Skin', 'Country Greenhouse Skin', 'Moon Greenhouse Skin', 'Orchard Greenhouse Skin', 'Botanical Garden Greenhouse Skin', 'Glacite Palace Greenhouse Skin'},
	}
	itemVariants['Crab Hat of Celebration'] = table.merge(itemVariants['2020 Crab Hat of Celebration'], itemVariants['2022 Crab Hat of Celebration'])
	
	for n, v in pairs(itemVariants) do
		createMultiAliases(n, v)
	end
	
	---------- Below this line: 04: Individual procedures to generate lists of item variants ----------
	-- Pets --
	local allPets = petTemplates.expandPetAll()
	createMultiAliases('Pet', allPets)
	createMultiAliases('Mystery Pet', table.map(allPets, function(v)
		return 'Mystery ' .. v
	end))
	createMultiAliases('Pet Skin', petTemplates.expandSkinAll())
	for k, v in pairs(petTemplates.expandPetType()) do
		createMultiAliases(k, v)
	end
	for k, v in pairs(petTemplates.expandPetTypeImage()) do
		createMultiAliases(k, v)
	end
	
	-- Colored dye (in Minecraft Namespace ID Order) --
	coloredDyes = {
		--[['Bone Meal',]] 'Orange Dye', 'Magenta Dye', 'Light Blue Dye', 
		'Dandelion Yellow', 'Lime Dye', 'Pink Dye', 'Gray Dye', 
		'Light Gray Dye', 'Cyan Dye', 'Purple Dye', 'Lapis Lazuli', 
		'Cocoa Beans', 'Cactus Green', 'Rose Red',  'Ink Sack', 
	};
	
	createMultiAliases('Colored Dye', coloredDyes)
	table.insert(coloredDyes, 1, 'Bone Meal')
	createMultiAliases('Dye', coloredDyes)
	
	-- Colored items: General items that use the sixteen colors --
	local zapkeep = gsubFn('%$k.-%s+', '', '%$k', '', '%$r', '')
	local zapremove = gsubFn('%$r.-%s+', '', '%$k', '', '%$r', '')
	-- ColorItmes Array --
	--[[
		Parameters
		    first param: General name for ALL (colored & non-colored) items
		    [second param]: General name for ALL COLORED items
		    ['nocolor']: Alternative name for no-color item, otherwise assume no-color item as the ''White'' Item
		Irregular Insersions
			For irregular color-indicating words (e.g. Dyed/Stained), insert symbol in front of a word. Symbols available:
		    $k for color indicating term to be *KEPT in the actual item names* BUT to be removed for the general name
		    $r for color indicating term to be *REMOVED in the actual item names* BUT to be kept for the general name
	--]]
	local coloredItems = {
		{'Carpet', '$rDyed Carpet'},
		{'Wool', '$rDyed Wool'},
		{'Jumbo Backpack ($1)', '$rDyed Jumbo Backpack ($1)', nocolor='Jumbo Backpack'}, 
		{'Greater Backpack ($1)', '$rDyed Greater Backpack ($1)', nocolor='Greater Backpack'}, 
		{'Large Backpack ($1)', '$rDyed Large Backpack ($1)', nocolor='Large Backpack'}, 
		{'Medium Backpack ($1)', '$rDyed Medium Backpack ($1)', nocolor='Medium Backpack'}, 
		{'Small Backpack ($1)', '$rDyed Small Backpack ($1)', nocolor='Small Backpack'}, 
		{'$kStained Glass', 'Stained Glass', nocolor='Glass'},
		{'$kStained Glass Pane', 'Stained Glass Pane', nocolor='Glass'},
		{'Hardened Clay', '$rStained Hardened Clay', nocolor='Hardened Clay'},
	}
	
	for _, item in ipairs(coloredItems) do
		local itemAny, listAny, itemColored, listColored, nocolor
		itemAny, listAny = item[1], {}
		itemColored, listColored = item[2], {}
		noColorItem = item['nocolor']
		
		table.push(listAny, noColorItem)
		
		table.eachNamed(MCColors, function(color)
			table.push(listAny, itemAny:match('%$1') 
					and gsubFn('%$1', color)(zapremove(itemAny)) 
					or color .. ' ' .. zapremove(itemAny)
			)
			if (not not noColorItem or color:lower() ~= 'white') and not not itemColored then
				table.push(listColored, itemColored:match('%$1') 
						and gsubFn('%$1', color)(zapremove(itemColored)) 
						or color .. ' ' .. zapremove(itemColored)
				)
			end
		end)
		
		createMultiAliases(gsubFn('%$1%s*', '', '%(%)', '')(zapkeep(itemAny)), listAny)
		
		if itemColored then
			createMultiAliases(gsubFn('%$1%s*', '', '%(%)', '')(zapkeep(itemColored)), listColored)
		end
	end
	
	-- Item groups --
	-- Dragon armor pieces and fragments --
	local dragonArmors = { 'Protector', 'Old', 'Unstable', 'Holy', 'Wise', 'Young', 'Strong', 'Superior' }
	for _, piece in ipairs{ 'Helmet', 'Chestplate', 'Leggings', 'Boots', 'Fragment' } do
		local dragonRelatedAliases = table.map(table.deepCopy(dragonArmors), function(v) 
			return v .. ' Dragon ' .. piece
		end)
		createMultiAliases('Dragon ' .. piece, dragonRelatedAliases)
	end
	
	-- Armor Pieces --
	for k, v in pairs(armorSets) do
		createMultiAliases(k, v)
	end
	
	-- Dungeon Boss Heads --
	local dungeonBosses = { 'Bonzo', 'Scarf', 'Professor', 'Thorn', 'Livid', 'Sadan', 'Necron' }
	for _, tier in ipairs{ 'Golden', 'Diamond' } do
		local dungBossHeads = table.map(table.deepCopy(dungeonBosses), function(v) 
			return ('%s %s Head'):format(tier, v)
		end)
		createMultiAliases(tier .. ' Dungeon Boss Head', dungBossHeads)
	end
	
	-- Wood --
	local woods = {
		'Oak', 
		'Spruce', 
		'Birch', 
		'Dark Oak', 
		'Acacia', 
		'Jungle'
	}
	local woodItems = {
		'Log', 
		'Wood Plank', -- Skyblock specific
		'Wood Slab', 
		'Wood Stairs', 
		'Fence', 
		'Fence Gate', 
		'Sapling', 
		'Leaves', 
	}
	for _, item in ipairs(woodItems) do
		local itemName;
		local woodAliases = {}
		
		for _, wood in ipairs(woods) do
			if item:find('wood') then
				itemName = item:gsub('wood', wood)
			elseif item:find('%$1') then
				itemName = item:gsub('%$1', wood)
			else
				itemName = wood .. ' ' .. item
			end
			table.insert(woodAliases, itemName)
		end
		item = item:gsub('%$1 ', '')
		createMultiAliases(item, woodAliases)
	end
	
	-- Minions
	createMultiAliases('Minion', minionTemplates.expandMinionAll())
	for k, v in pairs(minionTemplates.expandMinionType()) do
		createMultiAliases(k, v)
	end
	
	-- Potions
	createMultiAliases('Potion', potionM.expandPotionAll())
	for k, v in pairs(potionM.expandPotionType()) do
		createMultiAliases(k, v)
	end
	
	-- Enchanted Books
	createMultiAliases('Enchanted Book', enchantmentM.expandEnchantedBookAll())
	for k, v in pairs(enchantmentM.expandEnchantedBookType()) do
		createMultiAliases(k, v)
	end
	
	-- Gemstones
	local gemstoneTiers = {
		'Rough',
		'Flawed',
		'Fine',
		'Flawless',
		'Perfect',
	}
	
	local gemstoneTypes = {
		'Ruby',
		'Amber',
		'Sapphire',
		'Jade',
		'Amethyst',
		'Topaz',
		'Jasper',
		'Opal',
		'Onyx',
		'Aquamarine',
		'Citrine',
		'Peridot',
	}
	
	for _, a in ipairs(gemstoneTiers) do
		createMultiAliases(('%s Gemstone'):format(a), table.map(gemstoneTypes, function(b)
			return ('%s %s Gemstone'):format(a, b)
		end))
	end
	
	for _, b in ipairs(gemstoneTypes) do
		createMultiAliases(('%s Gemstone'):format(b), table.map(gemstoneTiers, function(a)
			return ('%s %s Gemstone'):format(a, b)
		end))
	end
	
	-- Power Scrolls
	createMultiAliases('Power Scroll', table.map(gemstoneTypes, function(b)
		return ('%s Power Scroll'):format(b)
	end))
	
	-- Sacks
	local sackTypes = {
		'Agronomy',
		'Combat',
		'Husbandry',
		'Foraging',
		'Fishing',
		'Mining',
		'Slayer',
		'Gemstone',
		'Nether',
		'Lava Fishing',
		'Dragon',
	}
	
	for _, b in ipairs(sackTypes) do
		createMultiAliases(('%s Sack'):format(b), table.map( {'Small', 'Medium', 'Large'}, function(a)
			return ('%s %s Sack'):format(a, b)
		end))
	end
	
	return variants
end

-- For Debugging
-- local p = { main = main }
-- return p

-- Actual Usage
return main()
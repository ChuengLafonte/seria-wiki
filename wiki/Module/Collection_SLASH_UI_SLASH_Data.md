local tradeCosts = {
	-- Acacia Wood Collection
	['Acacia Leaves'] = '&fAcacia Sapling',
	-- Birch Wood Collection
	['Birch Leaves'] = '&fBirch Sapling',
	-- Bone Collection
	['Enchanted Bone Meal'] = '&fBone &8x64',
	-- Clownfish Collection
	['Water Bucket'] = '&612 Coins',
	-- Dark Oak Wood Collection
	['Dark Oak Leaves'] = '&fDark Oak Sapling',
	-- Jungle Wood Collection
	['Jungle Leaves'] = '&fJungle Sapling',
	['Vines'] = '&fJungle Leaves &8x5',
	-- Leather Collection
	['Milk Bucket'] = '&650 Coins',
	-- Magma Cream Collection
	['Lava Bucket'] = '&620 Coins',
	-- Netherrack Collection
	['Nether Brick'] = '&fNetherrack',
	-- Oak Wood Collection
	['Oak Leaves'] = '&fOak Sapling',
	-- Sand Collection
	['Soul Sand'] = '&fSand &8x2/&fFermented Spider Eye',
	-- Seeds Collection
	['Dirt'] = '&fSeeds &8x8',
	['Clay'] = '&fSeeds &8x12',
	['Long Grass'] = '&fDirt &8x8',
	['Fern'] = '&fDirt &8x8',
	['Dead Bush'] = '&fDirt &8x8',
	['Double Tallgrass'] = '&fDirt &8x8',
	-- Sponge Collection
	['Sponge'] = '&fWet Sponge',
	-- Spruce Wood Collection
	['Spruce Leaves'] = '&fSpruce Sapling',
}

-- Trade amount defaults to 1
local tradeAmounts = {
	['Dirt'] = 2,
}

-- Note: Armor sets explosions should go to Module:Armor/Sets
local explosions = {
	-- Diamond Collection
	['Perfect Armor'] = {
		'Perfect Helmet - Tier I',
		'Perfect Chestplate - Tier I',
		'Perfect Leggings - Tier I',
		'Perfect Boots - Tier I',
	},
	-- Gemstone Collection
	['Power Scroll'] = {
		'Ruby Power Scroll',
		'Sapphire Power Scroll',
		'Jasper Power Scroll',
		'Amethyst Power Scroll',
		'Amber Power Scroll',
		'Opal Power Scroll',
	},
	['Flawed Gemstone'] = {
		'Flawed Ruby Gemstone',
		'Flawed Jade Gemstone',
		'Flawed Sapphire Gemstone',
		'Flawed Amethyst Gemstone',
		'Flawed Amber Gemstone',
		'Flawed Topaz Gemstone',
		'Flawed Jasper Gemstone',
		'Flawed Opal Gemstone',
		'Flawed Onyx Gemstone',
		'Flawed Citrine Gemstone',
		'Flawed Aquamarine Gemstone',
		'Flawed Peridot Gemstone',
	},
	['Fine Gemstone'] = {
		'Fine Ruby Gemstone',
		'Fine Jade Gemstone',
		'Fine Sapphire Gemstone',
		'Fine Amethyst Gemstone',
		'Fine Amber Gemstone',
		'Fine Topaz Gemstone',
		'Fine Jasper Gemstone',
		'Fine Opal Gemstone',
		'Fine Onyx Gemstone',
		'Fine Citrine Gemstone',
		'Fine Aquamarine Gemstone',
		'Fine Peridot Gemstone',
	},
	['Flawless Gemstone'] = {
		'Flawless Ruby Gemstone',
		'Flawless Jade Gemstone',
		'Flawless Sapphire Gemstone',
		'Flawless Amethyst Gemstone',
		'Flawless Amber Gemstone',
		'Flawless Topaz Gemstone',
		'Flawless Jasper Gemstone',
		'Flawless Opal Gemstone',
		'Flawless Onyx Gemstone',
		'Flawless Citrine Gemstone',
		'Flawless Aquamarine Gemstone',
		'Flawless Peridot Gemstone',
	},
	['Perfect Gemstone'] = {
		'Perfect Ruby Gemstone',
		'Perfect Jade Gemstone',
		'Perfect Sapphire Gemstone',
		'Perfect Amethyst Gemstone',
		'Perfect Amber Gemstone',
		'Perfect Topaz Gemstone',
		'Perfect Jasper Gemstone',
		'Perfect Opal Gemstone',
		'Perfect Onyx Gemstone',
		'Perfect Citrine Gemstone',
		'Perfect Aquamarine Gemstone',
		'Perfect Peridot Gemstone',
	},
}

-- Use this for some rare cases when the item displayed is different or when the line break placement is wrong
local rewardStrings = {
	-- Gemstone Collection
	['Flawed Ruby Gemstone'] = '&a  ❤ Flawed Ruby Gemstone/&7  Recipe',
	['Flawed Jade Gemstone'] = '&a  ☘ Flawed Jade Gemstone/&7  Recipe',
	['Flawed Sapphire Gemstone'] = '&a  ✎ Flawed Sapphire Gemstone/&7  Recipe',
	['Flawed Amethyst Gemstone'] = '&a  ❈ Flawed Amethyst Gemstone/&7  Recipe',
	['Flawed Amber Gemstone'] = '&a  ⸕ Flawed Amber Gemstone/&7  Recipe',
	['Flawed Topaz Gemstone'] = '&a  ✧ Flawed Topaz Gemstone/&7  Recipe',
	['Flawed Jasper Gemstone'] = '&a  ❁ Flawed Jasper Gemstone/&7  Recipe',
	['Flawed Opal Gemstone'] = '&a  ❂ Flawed Opal Gemstone/&7  Recipe',
	['Flawed Onyx Gemstone'] = '&a  ☠ Flawed Onyx Gemstone/&7  Recipe',
	['Flawed Citrine Gemstone'] = '&a  ☘ Flawed Citrine Gemstone/&7  Recipe',
	['Flawed Aquamarine Gemstone'] = '&a  ☂ Flawed Aquamarine Gemstone/&7  Recipe',
	['Flawed Peridot Gemstone'] = '&a  ☘ Flawed Peridot Gemstone/&7  Recipe',
				
	['Fine Ruby Gemstone'] = '&9  ❤ Fine Ruby Gemstone/&7  Recipe',
	['Fine Jade Gemstone'] = '&9  ☘ Fine Jade Gemstone/&7  Recipe',
	['Fine Sapphire Gemstone'] = '&9  ✎ Fine Sapphire Gemstone/&7  Recipe',
	['Fine Amethyst Gemstone'] = '&9  ❈ Fine Amethyst Gemstone/&7  Recipe',
	['Fine Amber Gemstone'] = '&9  ⸕ Fine Amber Gemstone/&7  Recipe',
	['Fine Topaz Gemstone'] = '&9  ✧ Fine Topaz Gemstone/&7  Recipe',
	['Fine Jasper Gemstone'] = '&9  ❁ Fine Jasper Gemstone/&7  Recipe',
	['Fine Opal Gemstone'] = '&9  ❂ Fine Opal Gemstone/&7  Recipe',
	['Fine Onyx Gemstone'] = '&9  ☠ Fine Onyx Gemstone/&7  Recipe',
	['Fine Citrine Gemstone'] = '&9  ☘ Fine Citrine Gemstone/&7  Recipe',
	['Fine Aquamarine Gemstone'] = '&9  ☂ Fine Aquamarine Gemstone/&7  Recipe',
	['Fine Peridot Gemstone'] = '&9  ☘ Fine Peridot Gemstone/&7  Recipe',
	
	['Flawless Ruby Gemstone'] = '&5  ❤ Flawless Ruby Gemstone/&7  Recipe',
	['Flawless Jade Gemstone'] = '&5  ☘ Flawless Jade Gemstone/&7  Recipe',
	['Flawless Sapphire Gemstone'] = '&5  ✎ Flawless Sapphire Gemstone/&7  Recipe',
	['Flawless Amethyst Gemstone'] = '&5  ❈ Flawless Amethyst Gemstone/&7  Recipe',
	['Flawless Amber Gemstone'] = '&5  ⸕ Flawless Amber Gemstone/&7  Recipe',
	['Flawless Topaz Gemstone'] = '&5  ✧ Flawless Topaz Gemstone/&7  Recipe',
	['Flawless Jasper Gemstone'] = '&5  ❁ Flawless Jasper Gemstone/&7  Recipe',
	['Flawless Opal Gemstone'] = '&5  ❂ Flawless Opal Gemstone/&7  Recipe',
	['Flawless Onyx Gemstone'] = '&5  ☠ Flawless Onyx Gemstone/&7  Recipe',
	['Flawless Citrine Gemstone'] = '&5  ☘ Flawless Citrine Gemstone/&7  Recipe',
	['Flawless Aquamarine Gemstone'] = '&5  ☂ Flawless Aquamarine Gemstone/&7  Recipe',
	['Flawless Peridot Gemstone'] = '&5  ☘ Flawless Peridot Gemstone/&7  Recipe',
	
	['Perfect Ruby Gemstone'] = '&6  ❤ Perfect Ruby Gemstone/&7  Recipe',
	['Perfect Jade Gemstone'] = '&6  ☘ Perfect Jade Gemstone/&7  Recipe',
	['Perfect Sapphire Gemstone'] = '&6  ✎ Perfect Sapphire Gemstone/&7  Recipe',
	['Perfect Amethyst Gemstone'] = '&6  ❈ Perfect Amethyst Gemstone/&7  Recipe',
	['Perfect Amber Gemstone'] = '&6  ⸕ Perfect Amber Gemstone/&7  Recipe',
	['Perfect Topaz Gemstone'] = '&6  ✧ Perfect Topaz Gemstone/&7  Recipe',
	['Perfect Jasper Gemstone'] = '&6  ❁ Perfect Jasper Gemstone/&7  Recipe',
	['Perfect Opal Gemstone'] = '&6  ❂ Perfect Opal Gemstone/&7  Recipe',
	['Perfect Onyx Gemstone'] = '&6  ☠ Perfect Onyx Gemstone/&7  Recipe',
	['Perfect Citrine Gemstone'] = '&6  ☘ Perfect Citrine Gemstone/&7  Recipe',
	['Perfect Aquamarine Gemstone'] = '&6  ☂ Perfect Aquamarine Gemstone/&7  Recipe',
	['Perfect Peridot Gemstone'] = '&6  ☘ Perfect Peridot Gemstone/&7  Recipe',
	
	--Kuudra Collection
	['Kuudra Pet (C)'] = '&f  Common Kuudra Pet',
	['Common Kuudra Pet'] = '&f  Common Kuudra Pet',
}

return {
	explosions = explosions,
	rewardStrings = rewardStrings,
	tradeCosts = tradeCosts,
	tradeAmounts = tradeAmounts,
}
local allstats = {
	-- in the order of display
	{'health', 'hp'},
	{'defense', 'def'},
	{'true_defense', 'trudef'},
	{'damage', 'dmg'},
	{'true_damage', 'tdmg'},
	{'strength', 'str'},
	{'speed', 'spd'},
	{'crit_chance', 'critchance'},
	{'crit_damage', 'critdmg'},
	{'intelligence', 'int'},
	{'ability_damage', 'abdmg'},
	{'attack_speed', 'atkspd'},
	{'ferocity', 'fer'},
	{'health_regen', 'hr'},
	{'vitality', 'vt'},
	{'mending', 'md'},
	{'sea_creature_chance', 'scc'},
	{'fishing_speed', 'fishspd'},
	{'farming_fortune', 'fmfortune'},
	{'foraging_fortune', 'frfortune'},
	{'mining_speed', 'mspeed'},
	{'mining_fortune', 'mfortune'},
	{'gemstone_fortune', 'gmfortune'},
	{'breaking_power', 'bpower'},
	{'magic_find', 'mf'},
	{'pet_luck', 'pl'},
	{'fear', 'fr'},
	{'combat_wisdom', 'cw'},
	{'mining_wisdom', 'mw'},
	{'farming_wisdom', 'fmw'},
	{'foraging_wisdom', 'frw'},
	{'fishing_wisdom', 'fsw'},
	{'enchanting_wisdom', 'ew'},
	{'alchemy_wisdom', 'aw'},
	{'rift_time', 'rt'},
	{'mana_regen', 'mr'},
	{'hearts', 'hrt'},
	{'swing_range', 'sr'},
	{'bonus_pest_chance', 'bpc'},
	{'sweep', 'swp'},
	{'pressure_resistance', 'pr'},
	{'cold_resistance', 'cr'},
	{'pull', 'pll'},
}

local armorInfo = {
	helmet = { name = 'Helmet', shortname = 'Head', aliases = { 'helmet', 'head' }, order = 0 },
	chest = { name = 'Chestplate', shortname = 'Chest', aliases = { 'chest', 'chestplate' }, order = 1 },
	legs = { name = 'Leggings', shortname = 'Legs', aliases = { 'legs', 'leggings' }, order = 2 },
	boots = { name = 'Boots', shortname = 'Boots', aliases = { 'boots' }, order = 3 },
	--necklace = { name = 'Necklace', shortname = 'Neck', aliases = { 'neck', 'necklace' }, order = 4 },
	--cloak = { name = 'Cloak', shortname = 'Cloak', aliases = { 'cloak' }, order = 5 },
	--belt = { name = 'Belt', shortname = 'Belt', aliases = { 'belt' }, order = 6 },
	--gauntlet = { name = 'Gauntlet', shortname = 'Gauntlet', aliases = {'gauntlet'}, order = 7 },
}

local rarityList = {
	-- in the order of display
	{ '_c', 'Com' },
	{ '_u', 'Uncom' },
	{ '_r', 'Rare' },
	{ '_e', 'Epic' },
	{ '_l', 'Legd' },
	{ '_m', 'Myth' },
	{ '_d', 'Divi' },
	{ '_sp', 'Spec' },
	{ '_vsp', 'VSpec' },
}

local sacksSuffix = {
	{ '_s', 'Small', '2,240' },
	{ '_m', 'Medium', '6,720' },
	{ '_l', 'Large', '20,160' },
}

local abilityPlaces = { '', 'Second', 'Third', 'Fourth' }

return {
	allstats = allstats,
	armorInfo = armorInfo,
	rarityList = rarityList,
	sacksSuffix = sacksSuffix,
	abilityPlaces = abilityPlaces,
	MAX_TAB = 16,
	MAX_INDEX = 10,
}
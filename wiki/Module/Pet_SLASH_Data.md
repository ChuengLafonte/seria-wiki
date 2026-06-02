return {
	-- sorted alphabetically
	['Ankylosaurus'] = {
		id = 'ANKYLOSAURUS',
		rarities = { 'L' },
		petType = 'Combat Pet',
		stats = {
			hp = {1.5},
			def = {0.5},
			td = {0.15},
			
		},
		abilities = {
			name = {
				[1] = 'Armored Tank',
				[2] = 'Unyielding',
				[3] = 'Clubbed Tail',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Gain {0} of your STAT_DEF as STAT_STR. {{Gray|(Max +500)}}',
				[2] = 'Increase the effectiveness of {{UltimateEnchantmentsLink|Last Stand}} and {{AttributeLink|Lifeline}} by {1}.',
				[3] = 'Every 5th hit deals {2} of your final damage to enemies within 5 blocks. Enemies hit deal 10% less damage for 10s.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip 
				[1] = '&7Gain &a{0}% &7of your &a❈ Defense &7as &c❁/&cStrength&7.',
				[2] = '&7Increase the effectiveness of &d&lLast/&d&lStand &7and &6Lifeline &7by &a{1}%&7.',
				[3] = '&7Every 5th hit deals &a{2}% &7of your/&7final damage to enemies within 5/&7blocks. Enemies hit deal 10% less/&7damage for 10s.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell
				[1] = '+{0} more STAT_DEF per level',
				[2] = '+{1} higher effectiveness per level',
				[3] = '+{2} more damage per level',
			},
		},
		variables = {
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl =  0.5,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.5,
					color = 'Green',
					suffix = '%%',
				},
				[2] = {
					per_lvl = 0.5,
					color = 'Green',
					suffix = '%%',
				},
			},
		},
	},
	['Ammonite'] = {
		id = 'AMMONITE',
		rarities = { 'L' },
		petType = 'Fishing Pet',
		stats = {
			scc = {0.05, 0},
		},
		abilities = {
			name = {
				[1] = 'Heart of the Sea',
				[2] = 'Expert Cave Fisher',
				[3] = 'Gift of the Ammonite',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Grants <DARK_AQUA>+</DARK_AQUA>{0}STAT_SCC to your pet for each <DARK_PURPLE>Heart of the Mountain</DARK_PURPLE> level.',
				[2] = 'Grants <BLUE>+</BLUE>{1}STAT_DHC for each <DARK_PURPLE>Heart of the Mountain</DARK_PURPLE> level while in the <DARK_PURPLE>Crystal Hollows</DARK_PURPLE>.',
				[3] = 'Each Mining and Fishing level grants <AQUA>+</AQUA>{2}STAT_FS, <WHITE>+</WHITE>{3}STAT_SPD and <GREEN>+</GREEN>{4}STAT_DEF.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Grants &3+{0}α Sea Creature/&3Chance &7to your pet for each/&5Heart of the Mountain &7level.',
				[2] = '&7Grants &9+{1}⚓ Double Hook Chance/&7for each &5Heart of the Mountain &7level/&7while in the &5Crystal Hollows&7.',
				[3] = '&7Each Mining and Fishing level grants/&b+{2}☂ Fishing Speed&7,/&7&f+{3}✦ Speed /&7and &a+{4}❈/&aDefense&7.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} STAT_SCC per level',
				[2] = '+{1} STAT_DHC per level',
				[3] = '+{3} STAT_FS, STAT_SPD, and STAT_DEF per level',
			},
		},
		variables = {
			legendary = {
				ability_count = 3,
				[0] = {
					base = 0,
					per_lvl = 0.01,
					color = 'Turquoise',
				},
				[1] = {
					base = 0,
					per_lvl = 0.005,
					color = 'Blue',
				},
				[2] = {
					base = 0,
					per_lvl = 0.005,
					color = 'Aqua',
				},
				[3] = {
					base = 0,
					per_lvl = 0.02,
					color = 'White',
				},
				[4] = {
					base = 0,
					per_lvl = 0.02,
					color = 'Green',
				},
			},
		},
	},
	['Armadillo'] = {
		id = 'ARMADILLO',
		rarities = { 'C', 'U', 'R', 'E', 'L' },
		petType = 'Mining Mount',
		stats = {
			def = {2},
		},
		abilities = {
			name = {
				[1] = 'Ridable',
				[2] = 'Tunneller',
				[3] = 'Earth Surfer',
				[4] = 'Rolling Miner',
				[5] = 'Long Claws',
				--[6] = 'Well-Worked',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Right-click your summoned pet to ride it!',
				[2] = 'The Armadillo breaks all stone or ore in its path while you are riding it in the Crystal Hollows.',
				[3] = 'The Armadillo moves faster based on your Speed.',
				[4] = 'Every {0} seconds, the next gemstone you mine gives 2x drops.',
				[5] = 'Grants {1} STAT_MSR while mining Hard Stone.',
				--[6] = 'Consumes {2} less energy when tunneling.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Right-click your summoned pet/&7to ride it!',
				[2] = '&7The Armadillo breaks all stone/&7or ore in it\'s path while you/&7are riding it in the &3Crystal/&3Hollows&7.',
				[3] = '&7The Armadillo moves faster/&7based on your &fSpeed&7.',
				[4] = '&7Every &a{0} &7seconds, the next/&7gemstone you mine gives 2x/&7drops.',
				[5] = '&7Grants &e{1}▚ Mining Spread &7while/&7mining Hard Stone.',
				--[6] = '&7Consumes &e{2}% &7less energy when tunneling.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = nil,
				[2] = nil,
				[3] = nil,
				[4] = '+{0} seconds per level',
				[5] = '+{1} STAT_MSR per level',
				--[6] = '+{2} less energy per level',
			},
		},
		variables = {
			common = {
				ability_count = 3,
			},
			uncommon = {
				ability_count = 3,
			},
			rare = {
				ability_count = 4,
				[0] = {
					base = 60,
					per_lvl = -0.2,
					color = 'Green',
				},
			},
			epic = {
				ability_count = 4,
				[0] = {
					base = 60,
					per_lvl = -0.3,
					color = 'Green',
				},
			},
			legendary = {
				ability_count = 5,
				[0] = {
					base = 60,
					per_lvl = -0.3,
					color = 'Green',
				},
				[1] = {
					base = 0,
					per_lvl = 3,
					color = 'Yellow',
				},
			},
			--[[ mythic = {
				ability_count = 6,
				[0] = {
					base = 60,
					per_lvl = -0.3,
					color = 'Green',
				},
				[1] = {
					base = 0,
					per_lvl = 3,
					color = 'yellow',
				},
				[2] = {
					base = 0,
					per_lvl = 1,
					color = 'yellow',
				},
			},
			]]
		},
	},
['Baby Yeti'] = {
		id = 'BABY_YETI',
		rarities = { 'C', 'U', 'R', 'E', 'L', 'M' },
		petType = 'Fishing Pet',
		stats = {
			str = {0.5},
			fs = {0.5},
			scc = {0.05},
			cr = {0.1},
		},
		abilities = {
			name = {
				[1] = 'Yeti Fury',
				[2] = 'Cold Breeze',
				[3] = 'Frosty Familiarity',
                [4] = 'Family Gathering',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Buffs the <GOLD>Yeti Sword</GOLD> by {0} STAT_DMG and STAT_INT and reduces its cooldown by {1}.',
				[2] = 'Increases <RED>Combat Stats</RED> and <AQUA>Fishing Stats</AQUA> by {2} while on <RED>Jerry\'s Workshop</RED>.',
				[3] = 'Grants <AQUA>+</AQUA>{3}STAT_MF against <WHITE>Winter Sea Creatures</WHITE>.',
                [4] = 'Grants {4}STAT_TRA while on <RED>Jerry\'s Workshop</RED>.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Buffs the &6Yeti Sword &7by &a{0} &c❁/&cDamage &7and &b✎ Intelligence &7and/&7reduces its cooldown by &a{1}&7.',
				[2] = '&7Increases &cCombat Stats &7and &bFishing/&bStats &7by &a{2} &7while on &cJerry\'s/Workshop&7.',
				[3] = '&7Grants &b+{3}✯ Magic Find &7against/&fWinter Sea Creatures&7.',
                [4] = '&7Grants &d{4}❃ Tracking &7while on/&cJerry\'s Workshop&7.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '<GREEN>+</GREEN>{0} more STAT_DMG and STAT_INT per level and <GREEN>+</GREEN>{1} more cooldown reduction',
				[2] = '<GREEN>+</GREEN>{2} more <RED>Combat</RED> and <AQUA>Fishing</AQUA> Stats',
                [3] = '<AQUA>+</AQUA>{3} more STAT_MF',
                [4] = '<LIGHT_PURPLE>+</LIGHT_PURPLE>{4} more STAT_TRA',
			},
		},
		variables = {
			common = {
				stats = {
					str = {0.5},
					fs = {0.5},
					scc = {0.05},
				},
				ability_count = 1,
				[0] = {
					per_lvl = 0.5,
					color = 'Green',
				},
				[1] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
			},
			uncommon = {
				stats = {
					str = {0.5},
					fs = {0.5},
					scc = {0.05},
				},
				ability_count = 1,
				[0] = {
					per_lvl = 0.8,
					color = 'Green',
				},
				[1] = {
					per_lvl = 0.4,
					color = 'Green',
					suffix = '%%',
				},
			},
			rare = {
				stats = {
					str = {0.5},
					fs = {0.5},
					scc = {0.05},
				},
				ability_count = 2,
				[0] = {
					per_lvl = 0.8,
					color = 'Green',
				},
				[1] = {
					per_lvl = 0.4,
					color = 'Green',
					suffix = '%%',
				},
                [2] = {
                    per_lvl = 0.1,
                    color = 'Green',
                    suffix = '%%',
				},
			},
			epic = {
				stats = {
					str = {0.5},
					fs = {0.5},
					scc = {0.05},
				},
				ability_count = 2,
				[0] = {
					per_lvl = 1,
					color = 'Green',
				},
				[1] = {
					per_lvl = 0.5,
					color = 'Green',
					suffix = '%%',
				},
                [2] = {
                    per_lvl = 0.2,
                    color = 'Green',
                    suffix = '%%',
				},
			},
			legendary = {
				stats = {
					str = {0.5},
					fs = {0.5},
					scc = {0.05},
				},
				ability_count = 3,
				[0] = {
					per_lvl = 1,
					color = 'Green',
				},
				[1] = {
					per_lvl = 0.5,
					color = 'Green',
					suffix = '%%',
				},
                [2] = { 
                    per_lvl = 0.2,
                    color = 'Green',
                    suffix = '%%',
				},
                [3] = {
                    per_lvl = 0.1,
                    color = 'Aqua',
				},
			},
			mythic = {
				stats = {
					str = {0.5},
					fs = {0.5},
					scc = {0.05},
					cr = {0.1},
				},
				ability_count = 4,
				[0] = {
					per_lvl = 1.5,
					color = 'Green',
				},
				[1] = {
					per_lvl = 0.75,
					color = 'Green',
					suffix = '%%',
				},
                [2] = { 
                    per_lvl = 0.2,
                    color = 'Green',
                    suffix = '%%',
				},
                [3] = {
                    per_lvl = 0.1,
                    color = 'Aqua',
                },
                [4] = {
                    per_lvl = 0.1,
                    color = 'LightPurple',
				},
			},
		},
	},
	['Bal'] = {
		id = 'BAL',
		rarities = { 'E', 'L' },
		petType = 'Mining Pet',
		stats = {
			mining_fortune = {1},
			heat_resistance = {1.5},
		},
		abilities = {
			name = {
				[1] = 'Furnace',
				[2] = 'Dispersion',
				[3] = 'Chimney',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Grants {0} STAT_PRISTINE while in the [[Magma Fields]].',
				[2] = 'While in the [[Crystal Hollows]], killing mobs reduces your STAT_HEAT by {1}.',
				[3] = 'Reduce Pickaxe Ability cooldowns by {2}.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Grants &5+{0}✧ Pristine &7while in the/&cMagma Fields&7.',
				[2] = '&7While in the &5Crystal Hollows&7, killing/&7mobs reduces your &c♨ Heat &7by &c4&7.',
				[3] = '&7Reduce Pickaxe Ability cooldowns by/&a10%&7.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} more STAT_PRISTINE per level',
				[2] = '+{1} STAT_HEAT reduction per level',
				[3] = '+{2}% cooldown reduction per level',
			},
		},
		variables = {
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.02,
					color = 'Purple',
				},
				[1] = {
					per_lvl = 0.04,
					color = 'Red',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.03,
					color = 'Purple',
				},
				[1] = {
					per_lvl = 0.04,
					color = 'Red',
				},
				[2] = {
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				}
			},
		},
	},
	['Bat'] = {
		id = 'BAT',
		rarities = { 'C', 'U', 'R', 'E', 'L', 'M' },
		petType = 'Mining Pet',
		stats = {
			int = {1},
			spd = {0.05},
			scc = {0.05, req='mythic'},
		},
		abilities = {
			name = {
				[1] = 'Candy Lover',
				[2] = 'Nightmare',
				[3] = 'Wings of Steel',
				[4] = 'Sonar',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Increases drop chance of candies from mobs by {0}',
				[2] = 'During night, gain {1} STAT_INT, {2} STAT_SPD, and Night Vision.',
				[3] = 'Deals +{3} damage to Spooky enemies during the Spooky Festival.',
				[4] = '+{4} chance to fish up spooky sea creatures',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Increases drop chance of/&7candies from mobs by &a{0}%',
				[2] = '&7&7During night, gain &a{1} &b✎/&bIntelligence&7, &a{2} &f✦/&fSpeed&7, and &aNight Vision&7.',
				[3] = '&7Deals &a+{3}% &7damage to/&7&6Spooky &7enemies during the/&7&6Spooky Festival.',
				[4] = '&7+&a{4}% &7chance to fish up/&7spooky sea creatures.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} higher chance to drop Candy',
				[2] = '+{1} more STAT_INT per level; +{2} more STAT_SPD per level',
				[3] = '+{3} more damage per level',
				[4] = '+{4} higher chance to fish up spooky sea creatures',
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.15,
					color = 'Green',
					suffix = '%%',
				},
			},
			rare = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.15,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.2,
					color = 'Green',
				},
				[2] = {
					per_lvl = 0.4,
					color = 'Green',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.3,
					color = 'Green',
				},
				[2] = {
					per_lvl = 0.5,
					color = 'Green',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.3,
					color = 'Green',
				},
				[2] = {
					per_lvl = 0.5,
					color = 'Green',
				},
				[3] = {
					per_lvl = 0.5,
					color = 'Green',
					suffix = '%%',
				},
			},
			mythic = {
				ability_count = 4,
				[0] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
						per_lvl = 0.3,
						color = 'Green',
				},
				[2] = {
					per_lvl = 0.5,
					color = 'Green',
				},
				[3] = {
					per_lvl = 0.5,
					color = 'Green',
					suffix = '%%',
				},
				[4] = {
					per_lvl = 0.25,
					color = 'Green',
					suffix = '%%',
				},
			},
		},
	},
	['Bee'] = {
		id = 'BEE',
		rarities = { 'C', 'U', 'R', 'E', 'L' },
		petType = 'Farming Pet',
		stats = {
			str = {0.25, 5},
			int = {0.5},
			spd = {0.1},
		},
		abilities = {
			name = {
				[1] = 'Hive',
				[2] = 'Busy Buzz Buzz',
				[3] = 'Weaponized Honey',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'For each player within <GREEN>25</GREEN> blocks:<br/><AQUA>+</AQUA>{0} STAT_INT<br/><RED>+</RED>{1} STAT_STR<br/><GREEN>+</GREEN>{2} STAT_DEF<br/><DARK_GRAY>Max 15 players</DARK_GRAY>',
				[2] = 'Grants <GREEN>+</GREEN>{3} of each to your pet:<br/>STAT_FMF<br/>STAT_FRF<br/>STAT_MNF',
				[3] = 'Gain {4} of received damage as STAT_ABS.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7For each player within &a25 &7blocks:/&b +{0}✎ Intelligence/&c +{1}❁ Strength/&a +{2}❈ Defense/&8Max 15 players',
				[2] = '&7Grants &a+{3} &7of each to your pet:/&6☘ Farming Fortune/&6☘ Foraging Fortune/&6☘ Mining Fortune',
				[3] = '&7Gain &a{4}% &7of received/&7damage as &6❤ Absorption.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '{0} more STAT_INT per level, {1} more STAT_STR per level, {2} more STAT_DEF per level',
				[2] = '{3} more STAT_FMF, STAT_FRF, STAT_MNF per level',
				[3] = '{4} more damage converted to STAT_ABS',
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.02,
					base = 1,
					color = 'Aqua',
				},
				[1] = {
					per_lvl = 0.02,
					base = 1,
					color = 'Red',
				},
				[2] = {
					per_lvl = 0.01,
					base = 1,
					color = 'Green',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.05,
					base = 1,
					color = 'Aqua',
				},
				[1] = {
					per_lvl = 0.04,
					base = 1,
					color = 'Red',
				},
				[2] = {
					per_lvl = 0.02,
					base = 1,
					color = 'Green',
				},
			},
			rare = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.05,
					base = 1,
					color = 'Aqua',
				},
				[1] = {
					per_lvl = 0.04,
					base = 1,
					color = 'Red',
				},
				[2] = {
					per_lvl = 0.02,
					base = 1,
					color = 'Green',
				},
				[3] = {
					per_lvl = 0.2,
					color = 'Green',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.09,
					base = 1,
					color = 'Aqua',
				},
				[1] = {
					per_lvl = 0.07,
					base = 1,
					color = 'Red',
				},
				[2] = {
					per_lvl = 0.04,
					base = 1,
					color = 'Green',
				},
				[3] = {
					per_lvl = 0.3,
					color = 'Green',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.09,
					base = 1,
					color = 'Aqua',
				},
				[1] = {
					per_lvl = 0.07,
					base = 1,
					color = 'Red',
				},
				[2] = {
					per_lvl = 0.04,
					base = 1,
					color = 'Green',
				},
				[3] = {
					per_lvl = 0.3,
					color = 'Green',
				},
				[4] = {
					per_lvl = 0.2,
					base = 5,
					color = 'Green',
					suffix = '%%',
				},
			},
		},
	},
	['Bingo'] = {
		id = 'BINGO',
		rarities = { 'C', 'U', 'R', 'E', 'L', 'M' },
		petType = 'All Skills',
		isPassive = true,
		discloseXP = { 'common' }, -- only displays these rarities on XP table
		stats = {
			hp = {1},
			str = {0.25},
			spd = {0.75},
		},
		abilities = {
			name = {
				[1] = 'Lucky Looting',
				[2] = 'Mountain Climber',
				[3] = 'Fast Learner',
				[4] = 'Chimera',
				[5] = 'Scavenger',
                [6] = 'Consumer',
				[7] = 'Power Of Completion',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Gain {0} more collection items from any source!',
				[2] = 'Gain {1} more HOTM experience.',
				[3] = 'Gain {2} more Skill Experience and Slayer Experience.',
				[4] = 'Increases the base stats of your active pet by {3}.',
				[5] = 'Gain {4} more coins per monster level on kill.',
				[6] = 'Potion effects you obtain will have {5} more time.',
				[7] = 'Gain {{stat|str|+2}}, {{stat|cc|+1}}, and {{stat|hp|+5}} per completed Personal Bingo Goal in the current Bingo Event.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip 
				[1] = '&7Gain &c{0}% &7more collection/&7items from any source!',
				[2] = '&7Gain &c{1}% &7more HOTM experience.',
				[3] = '&7Gain &c{2}% &7more Skill/&7Experience and/&7Slayer Experience.',
				[4] = '&7Increases the base stats of/&7your active pet by &c{3}%&7.',
				[5] = '&7Gain &c{4} &7more coins per/&7monster level on kill.',
				[6] = '&7Potion effects you obtain will have &c{5} &7more time.',
				[7] = '&7Gain &c+2❁ Strength&7, &9+1☣/&9Crit Chance&7, and &c+5❤/&cHealth&7 per completed Personal/&7Bingo Goal in the current Bingo/&7Event.'
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} more collection items per level',
				[2] = nil,
				[3] = '+{1} more skill and slayer experience per level',
				[4] = '+{2} increases the base stats of your active pet per level',
				[5] = '+{3} more coins per monster level on kill per level',
				[6] = '+{4} more duration of effects per level',
				[7] = nil,
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					base = 5,
					per_lvl = 0.2,
					color = "Red",
					suffix = '%%',
				},
			},
			uncommon = {
				ability_count = 2,
				[0] = {
					base = 5,
					per_lvl = 0.2,
					color = "Red",
					suffix = '%%',
				},
				[1] = {
					base = 100,
					per_lvl = 1.5,
					color = "Red",
					suffix = '%%',
				},
			},
			rare = {
				ability_count = 3,
				[0] = {
					base = 5,
					per_lvl = 0.2,
					color = "Red",
					suffix = '%%',
				},
				[1] = {
					base = 100,
					per_lvl = 1.5,
					color = "Red",
					suffix = '%%',
				},
				[2] = {
					base = 5,
					per_lvl = 0.1,
					color = "Red",
					suffix = '%%',
				},
			},
			epic = {
				ability_count = 4,
				[0] = {
					base = 5,
					per_lvl = 0.2,
					color = "Red",
					suffix = '%%',
				},
				[1] = {
					base = 100,
					per_lvl = 1.5,
					color = "Red",
					suffix = '%%',
				},
				[2] = {
					base = 5,
					per_lvl = 0.1,
					color = "Red",
					suffix = '%%',
				},
				[3] = {
					base = 10,
					per_lvl = 0.3,
					color = 'Red',
				},
			},
			legendary = {
				ability_count = 6,
				[0] = {
					base = 5,
					per_lvl = 0.2,
					color = "Red",
					suffix = '%%',
				},
				[1] = {
					base = 100,
					per_lvl = 1.5,
					color = "Red",
					suffix = '%%',
				},
				[2] = {
					base = 5,
					per_lvl = 0.1,
					color = "Red",
					suffix = '%%',
				},
				[3] = {
					base = 10,
					per_lvl = 0.3,
					color = 'Red',
				},
				[4] = {
					base = 0.1,
					per_lvl = 0.009,
					color = 'Red',
					suffix = '%%',
				},
				[5] = {
					base = 10,
					per_lvl = 0.4,
					color = 'Red',
					suffix = '%%',
				},
			},
		    mythic = {
		    	ability_count = 7,
		    	[0] = {
					base = 5,
					per_lvl = 0.2,
					color = "Red",
					suffix = '%%',
				},
				[1] = {
					base = 100,
					per_lvl = 1.5,
					color = "Red",
					suffix = '%%',
				},
				[2] = {
					base = 5,
					per_lvl = 0.1,
					color = "Red",
					suffix = '%%',
				},
				[3] = {
					base = 10,
					per_lvl = 0.3,
					color = 'Red',
				},
				[4] = {
					base = 0.1,
					per_lvl = 0.009,
					color = 'Red',
					suffix = '%%',
				},
				[5] = {
					base = 10,
					per_lvl = 0.4,
					color = 'Red',
					suffix = '%%',
				},
		    }
		},
	},
	['Black Cat'] = {
		id = 'BLACK_CAT',
		rarities = { 'L', 'M' },
		petType = 'Combat Pet',
		stats = {
			spd = {1.25},
			int = {1},
			mf = {0.15},
			pl = {0.15},
		},
		abilities = {
			name = {
				[1] = 'Hunter',
				[2] = 'Omen',
				[3] = 'Supernatural',
				[4] = 'Looting',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Increases your STAT_SPD and speed cap by {0}.',
				[2] = 'Grants {1} STAT_PL.',
				[3] = 'Grants {2} STAT_MF.',
				[4] = 'Gain {3} more collection items from monsters!',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Increases your speed and/&7speed cap by +&a{0}&7.',
				[2] = '&7Grants &a{1} &7&d♣ Pet Luck&7.',
				[3] = '&7Grants &a{2} &7&b✯ Magic Find&7.',
				[4] = '&7Gain &c{3}% &7more collection/&7items from monsters!',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} STAT_SPD per level.',
				[2] = '+{1} STAT_PL per level.',
				[3] = '+{2} STAT_MF per level.',
				[4] = '+{3} Looting per level.',
			},
		},
		variables = {
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 1,
					color = 'Green',
				},
				[1] = {
					per_lvl = 0.15,
					color = 'Green',
				},
				[2] = {
					per_lvl = 0.15,
					color = 'Green',
				},
			},
			mythic = {
				ability_count = 4,
				[0] = {
					per_lvl = 1,
					color = 'Green',
				},
				[1] = {
					per_lvl = 0.15,
					color = 'Green',
				},
				[2] = {
					per_lvl = 0.15,
					color = 'Green',
				},
				[3] = {
					per_lvl = 0.15,
					color = 'Red',
					suffix = '%%',
				},
			},
		},
	},
	['Blaze'] = {
		id = 'BLAZE',
		rarities = { 'C', 'U', 'R', 'E', 'L' },
		petType = 'Combat Pet',
		stats = {
			int = {1},
			def= {0.3},
		},
		abilities = {
			name = {
				[1] = 'Nether Embodiment',
				[2] = 'Bling Armor',
				[3] = 'Fusion-Style Potato',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Increases Combat and Miscellaneous stats by {0} while on the [[Crimson Isle]].',
				[2] = 'Upgrades [[Blaze Armor]] stats and ability by {1}.',
				[3] = 'Double effects of [[Hot Potato Book]]s.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Increases &cCombat &7and &dMiscellaneous/&7stats by &a{0}%/&a&7while on the Crimson Isle.',
				[2] = '&7Upgrades &cBlaze Armor &7stats/&7and ability by &a{1}%',
				[3] = '&7Double effects of hot potato/&7books.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} higher stats increase per level',
				[2] = '+{1} bigger [[Blaze Armor]] upgrade per level',
				[3] = nil,
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.05,
					color = 'Green',
					suffix = '%%',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.075,
					color = 'Green',
					suffix = '%%',
				},
			},
			rare = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.075,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.4,
					color = 'Green',
					suffix = '%%',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.4,
					color = 'Green',
					suffix = '%%',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.4,
					color = 'Green',
					suffix = '%%',
				},
			},
		},
	},
	['Blue Whale'] = {
		id = 'BLUE_WHALE',
		rarities = { 'C', 'U', 'R', 'E', 'L' },
		petType = 'Fishing Pet',
		stats = {
			hp = {2},
		},
		abilities = {
			name = {
				[1] = 'Ingest',
				[2] = 'Bulk',
				[3] = 'Archimedes',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'All potions heal +{0} STATs_HP.',
				[2] = 'Gain +{1} STAT_DEF per {2} <RED>Max</RED> STAT_HP.',
				[3] = 'Gain +{3} <RED>Max</RED> STAT_HP.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7All potions heal &c+{0}❤.',
				[2] = '&7Gain &a{1}&a❈ Defense &7per/&7&c{2} Max &c❤ Health.',
				[3] = '&7Gain &c+{3}% Max &c❤ Health.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} higher healing per level',
				[2] = '+{1} more STAT_DEF per {2} Max STAT_HP',
				[3] = '+{3} higher STAT_HP boost per level',
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.5,
					color = 'Red',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					per_lvl = 1,
					color = 'Red',
				},
			},
			rare = {
				ability_count = 2,
				[0] = {
					per_lvl = 1.5,
					color = 'Red',
				},
				[1] = {
					per_lvl = 0.01,
					color = 'Green',
				},
				[2] = { -- constant variable. Changes with rarities, but not with levels
					per_lvl = 0,
					base = 30,
					color = 'Red',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 2,
					color = 'Red',
				},
				[1] = {
					per_lvl = 0.01,
					color = 'Green',
				},
				[2] = { -- constant variable. Changes with rarities, but not with levels
					per_lvl = 0,
					base = 25,
					color = 'Red',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 2,
					color = 'Red',
				},
				[1] = {
					per_lvl = 0.01,
					color = 'Green',
				},
				[2] = { -- constant variable. Changes with rarities, but not with levels
					per_lvl = 0,
					base = 20,
					color = 'Red',
				},
				[3] = {
					per_lvl = 0.2,
					color = 'Red',
					suffix = '%%',
				},
			},
		},
	},
	['Chicken'] = {
		id = 'CHICKEN',
		rarities = { 'C', 'U', 'R', 'E', 'L' },
		petType = 'Farming Pet',
		stats = {
			spd = {0.5},
			fmf = {0.5},
		},
		abilities = {
			name = {
				[1] = 'Free Range',
				[2] = 'Eggstra Loot',
				[3] = 'Light Feet',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Grants +{0} STAT_FMF while on <AQUA>Public Islands</AQUA>.',
				[2] = 'Chickens always drop an Egg when killed. Grants a {1} chance for animals to drop an additional item.',
				[3] = 'Reduces fall damage by {2}.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Grants &6+{0}☘ Farming Fortune &7while/&7on &bPublic Islands&7.',
				[2] = '&7Chickens always drop an &fEgg &7when/&7killed. Grants a &a{1}% &7chance for/&7animals to drop an additional item.',
				[3] = '&7Reduces fall damage by &a{2}%&7.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} more STAT_FMF per level',
				[2] = '+{1} higher chance per level',
				[3] = '+{2} less damage per level',
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.5,
					color = 'Gold',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.75,
					color = 'Gold',
				},
			},
			rare = {
				ability_count = 2,
				[0] = {
					per_lvl = 1,
					color = 'Gold',
				},
				[1] = {
					per_lvl = 0.8,
					color = 'Green',
					suffix = '%%',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 1,
					color = 'Gold',
				},
				[1] = {
					per_lvl = 1,
					color = 'Green',
					suffix = '%%',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 1,
					color = 'Gold',
				},
				[1] = {
					per_lvl = 1,
					color = 'Green',
					suffix = '%%',
				},
				[2] = {
					per_lvl = 1,
					color = 'Green',
					suffix = '%%',
				},
			},
		},
	},
    ['Crow'] = {
        id = 'CROW',
        rarities = { 'C', 'U', 'R', 'E', 'L' },
        petType = 'Combat Pet',
        stats = {
            int = {1.5},
            ad = {0.2},
        },
        abilities = {
            name = {
                [1] = 'Quick Hands',
                [2] = 'Camouflage',
                [3] = 'Insightful',
            },
            desc = {
                -- the description of abilities used in the two top cells
                [1] = 'Lowers the cooldown of your abilities by +{0}.',
                [2] = 'After casting an ability, increase your STAT_DEF by +{1} for 20 seconds. Capped at 500 Defense.',
                [3] = 'Gives a {2} chance to not consume Mana when using an ability.',
            },
            tooltip = {
                -- the description of abilities used in the tooltip 
                [1] = '&7Lowers the cooldown of your/&7abilities by &a+{0}&7.',
                [2] = '&7After casting an ability, increase/&7your &a❈ Defense &7by &a+{1} &7for &b20/&bseconds&7./&8Capped at 500 Defense',
                [3] = '&7Gives a &a{2}% &7chance to not consume/&7Mana when using an ability.',
            },
            bonus_desc = {
                -- the description of abilities used in the bottom cell
                [1] = '{0} lower cooldown',
                [2] = '{1} more STAT_DEF',
                [3] = '{2} chance to not consume mana',
            },
        },
        variables = {
            common = {
                ability_count = 1,
                [0] = {
                	base = 3,
                    per_lvl = 0.07, -- TODO: FIND REAL VALUE / FUNCTION
                    color = 'Green',
                    suffix = '%%',
                },
            },
            uncommon = {
                ability_count = 1,
                [0] = {
                	base = 3,
                    per_lvl = 0.07, -- TODO: FIND REAL VALUE / FUNCTION
                    color = 'Green',
                    suffix = '%%',
                },
            },
            rare = {
                ability_count = 2,
                [0] = {
                	base = 3,
                    per_lvl = 0.07, -- TODO: FIND REAL VALUE / FUNCTION
                    color = 'Green',
                    suffix = '%%',
                },
                [1] = {
                	base = 5,
                    per_lvl = 0.1,
                    color = 'Green',
                    suffix = '%%',
                },
            },
            epic = {
                ability_count = 2,
                [0] = {
                	base = 3,
                    per_lvl = 0.12, -- TODO: FIND REAL VALUE / FUNCTION
                    color = 'Green',
                    suffix = '%%',
                },
                [1] = {
                	base = 5,
                    per_lvl = 0.15,
                    color = 'Green',
                    suffix = '%%',
                },
            },
            legendary = {
                ability_count = 3,
                [0] = {
                	base = 3,
                    per_lvl = 0.12, -- TODO: FIND REAL VALUE / FUNCTION
                    color = 'Green',
                    suffix = '%%',
                },
                [1] = {
                	base = 5,
                    per_lvl = 0.15,
                    color = 'Green',
                    suffix = '%%',
                },
                [2] = {
                    base = 3,
                    per_lvl = 0.12, -- TODO: FIND REAL VALUE / FUNCTION
                    color = 'Green',
                    suffix = '%%',
                },
            },
        },
    },
	['Dolphin'] = {
		id = 'DOLPHIN',
		rarities = { 'C', 'U', 'R', 'E', 'L' },
		petType = 'Fishing Pet',
		stats = {
			int = {1},
			scc = {0.05},
		},
		abilities = {
			name = {
				[1] = 'Pod Tactics',
				[2] = 'Echolocation',
				[3] = 'Splash Surprise',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Grants <AQUA>+</AQUA>{0}STAT_FS for each player within <GREEN>30</GREEN> blocks, up to <GREEN>5</GREEN> players.',
				[2] = 'Grants {1} STAT_SCC.',
				[3] = 'Stun sea creatures for <GREEN>5s</GREEN> after fishing them up',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Grants &b+{0}☂ Fishing Speed/&7for each player within &a30/&7blocks, up to &a5 &7players.',
				[2] = '&7Grants &3+{1}α Sea Creature/&3Chance.',
				[3] = '&7Stun sea creatures for &a5s/&a&7after fishing them up.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} more STAT_FS per level',
				[2] = '+{1} higher sea creatures catch chance per level',
				[3] = nil,
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.06,
					color = 'Aqua',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.08,
					color = 'Aqua',
				},
			},
			rare = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.08,
					color = 'Aqua',
				},
				[1] = {
					per_lvl = 0.07,
					color = 'Green',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.1,
					color = 'Aqua',
				},
				[1] = {
					per_lvl = 0.1,
					color = 'Green',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.1,
					color = 'Aqua',
				},
				[1] = {
					per_lvl = 0.1,
					color = 'Green',
				},
			},
		},
	},
	['Eerie'] = {
		id = 'EERIE',
		rarities = { 'C', 'R', 'L' },
		petType = 'Combat Pet',
		stats = {
			spd = {0.1},
			int = {0.5},
		},
		abilities = {
			name = {
				[1] = 'Fearnesy',
				[2] = 'Fearama',
				[3] = 'Fearcreasing',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = '<DARK_PURPLE>Fear</DARK_PURPLE> from <DARK_PURPLE>Great Spook Armor</DARK_PURPLE> in your <AQUA>wardrobe</AQUA> applies to you, even if you aren\'t wearing it.',
				[2] = 'Increases <RED>damage</RED> dealt to Primal Fears and Spooky Mobs by <GREEN>1%</GREEN> for every <DARK_PURPLE>Fear</DARK_PURPLE> you have.',
				[3] = 'Gives <GREEN>+{0}</GREEN> <DARK_PURPLE>Fear</DARK_PURPLE> for every <GREEN>10</GREEN> <RED>Primal Fears</RED> killed, up to <GREEN>150</GREEN> <RED>Primal Fears</RED>.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&5Fear &7from &5Great Spook Armor &7in/&7your &bwardrobe &7applies to you, even/&7if you aren\'t wearing it.',
				[2] = '&7Increases &cdamage &7dealt to Primal/&7Fears and Spooky Mobs by &a1% &7for/&7every &5Fear &7you have.',
				[3] = '&7Gives &a+{0} &5Fear &7for every &a10 &cPrimal/&cFears &7killed, up to &a150 &cPrimal Fears&7./&cPrimal Fear Kills&7: (&a0&7/&a150&7)',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = nil,
				[2] = nil,
				[3] = '+{0} STAT_FEAR per level.',
			},
		},
		variables = {
			common = {
				ability_count = 1,
			},
			rare = {
				ability_count = 2,
			},
			legendary = {
				ability_count = 3,
				[0] = {
					base = 0.1,
					per_lvl = 0.003,
					color= 'Green',
				}
			},
		},
	},
	['Elephant'] = {
		id = 'ELEPHANT',
		rarities = { 'C', 'U', 'R', 'E', 'L' },
		petType = 'Farming Pet',
		stats = {
			hp = {1},
			int = {0.75},
		},
		abilities = {
			name = {
				[1] = 'Stomp',
				[2] = 'Walking Fortress',
				[3] = 'Trunk Efficiency',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Gain {0} STAT_DEF for every 100 STAT_SPD',
				[2] = 'Gain {1} STAT_HP for every <GREEN>10</GREEN> STAT_DEF',
				[3] = 'Grants <GOLD>+{2}</GOLD> STAT_FMF, which increases your chance for multiple drops.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Gain &a{0}❈ Defense &7for every/&7100 &f✦ Speed&7.',
				[2] = '&7Gain &c{1}❤ Health &7for every/&710 &a❈ Defense&7.',
				[3] = '&7Grants &6+{2}☘ Farming/&6Fortune, &7which increases your/&7chance for multiple drops.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} more STAT_DEF per level',
				[2] = '+{1} more STAT_HP per level',
				[3] = '+{2} more STAT_FMF per level',
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.15,
					color = 'Green',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.15,
					color = 'Green',
				},
			},
			rare = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.15,
					color = 'Green',
				},
				[1] = {
					per_lvl = 0.01,
					color = 'Red',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.2,
					color = 'Green',
				},
				[1] = {
					per_lvl = 0.01,
					color = 'Red',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.2,
					color = 'Green',
				},
				[1] = {
					per_lvl = 0.01,
					color = 'Red',
				},
				[2] = {
					per_lvl = 1.5,
					color = 'Gold',
				},
			},
		},
	},
	['Ender Dragon'] = {
		id = 'ENDER_DRAGON',
		rarities = { 'E', 'L' },
		petType = 'Combat Pet',
		stats = {
			str = {0.5},
			cd = {0.5},
			cc = {0.1},
		},
		abilities = {
			name = {
				[1] = 'End Strike',
				[2] = 'One with the Dragons',
				[3] = 'Superior',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Deal +{0} more damage to end mobs.',
				[2] = 'Buffs the [[Aspect of the Dragons]] sword by {1} STAT_DMG and {2} STAT_STR.',
				[3] = 'Increases most stats by {3}.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Deal &a{0}% &7more damage to/&7end mobs.',
				[2] = '&7Buffs the Aspect of the/&7Dragons sword by &a{1} &c❁ Damage/&c&7and &a{2} &c❁ Strength.',
				[3] = '&7Increases most stats by &a{3}%',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} more damage per level.',
				[2] = '+{1} more STAT_DMG and +{2} STAT_STR per level.',
				[3] = '+{3} higher bonus per level.',
			},
		},
		variables = {
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 2,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.5,
					color = 'Green',
				},
				[2] = {
					per_lvl = 0.3,
					color = 'Green',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 2,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.5,
					color = 'Green',
				},
				[2] = {
					per_lvl = 0.3,
					color = 'Green',
				},
				[3] = {
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
			},
		},
	},
	['Enderman'] = {
		id = 'ENDERMAN',
		rarities = { 'C', 'U', 'R', 'E', 'L', 'M' },
		petType = 'Combat Pet',
		stats = {
			cd = {0.75},
		},
		abilities = {
			name = {
				[1] = 'Enderian',
				[2] = 'Teleport Savvy',
				[3] = 'Zealot Madness',
				[4] = 'Enderman Slayer',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Take {0} less damage from end monsters.',
				[2] = 'Buffs the Transmission ability granting {1} STAT_DMG for 5s on use.',
				[3] = 'Increases your odds to find a special [[Zealot]] by {2}.',
				[4] = 'Grants {3} Combat XP against <GREEN>Endermen</GREEN>.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Take &a{0}% &7less damage/&7from end monsters.',
				[2] = '&7Buffs the Transmission/&7abilities granting &a{1} &7weapon/&7damage for 5s on use.',
				[3] = '&7Increases your odds to find a/&7special Zealot by &a{2}%',
				[4] = '&7Grants &b{3} &7Combat XP/&7against &aEndermen',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} less damage per level',
				[2] = '+{1} more STAT_DMG per level',
				[3] = '+{2} higher chance per level',
				[4] = '+{3} more Combat XP per level',
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
			},
			rare = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.4,
					color = 'Green',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.3,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.5,
					color = 'Green',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.3,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.5,
					color = 'Green',
				},
				[2] = {
					per_lvl = 0.25,
					color = 'Green',
					suffix = '%%',
				},
			},
			mythic = {
				ability_count = 4,
				[0] = {
					per_lvl = 0.3,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.5,
					color = 'Green',
				},
				[2] = {
					per_lvl = 0.25,
					color = 'Green',
					suffix = '%%',
				},
				[3] = {
					base = 1.0,
					per_lvl = 0.005,
					color = 'Aqua',
					suffix = 'x',
				},
			},
		},
	},
	['Endermite'] = {
		id = 'ENDERMITE',
		rarities = { 'C', 'U', 'R', 'E', 'L', 'M' },
		petType = 'Mining Pet',
		stats = {
			int = {1.5},
			pl = {0.1},
		},
		abilities = {
			name = {
				[1] = 'More Stonks',
				[2] = 'Daily Commuter',
				[3] = 'Mite Bait',
				[4] = 'Sacrificer',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Gain more exp orbs for breaking end stone and gain a +{0} chance to get an extra block dropped.',
				[2] = '<BLUE>Transmission Abilities</BLUE> cost {1} less mana.',
				[3] = 'Gain a {2} chance to dig up a bonus <RED>Nest Endermite</RED> per <LIGHT_PURPLE>+1</LIGHT_PURPLE>STAT_PL <DARK_GRAY>(Stacks above 100%).</DARK_GRAY>',
				[4] = 'Increases the odds of rolling for bonus items in the <RED>Draconic Altar</RED> by {3}.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Gain more exp orbs for/&7breaking end stone and gain a/&7+&a{0}% &7chance to get an extra/&7block dropped.',
				[2] = '&9Transmission Abilities/&7cost &a{1}% &7less mana.',
				[3] = '&7Gain a &a{2}% &7chance to dig up/&7a bonus &cNest Endermite &7per/&d+1♣ Pet Luck &8(Stacks above/&8100%).',
				[4] = '&7Increases the odds of rolling/&7for bonus items in the/&cDraconic Altar &7by &a{3}%&7.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} higher chance to drop an extra block per level',
				[2] = '+{1} less {{stat|mana}} per level',
				[3] = '+{2} chance to dig up a bonus <RED>Nest Endermite</RED> per level',
				[4] = '+{3} increased odds of rolling for bonus items in the <RED>Draconic Altar</RED> per level',
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.5,
					color = 'Green',
					suffix = '%%',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.8,
					color = 'Green',
					suffix = '%%',
				},
			},
			rare = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.8,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.3,
					color = 'Green',
					suffix = '%%',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 1,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.4,
					color = 'Green',
					suffix = '%%',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 1,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.4,
					color = 'Green',
					suffix = '%%',
				},
				[2] = {
					per_lvl = 0.03,
					color = 'Green',
					suffix = '%%',
				},
			},
			mythic = {
				ability_count = 4,
				[0] = {
					per_lvl = 1,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.4,
					color = 'Green',
					suffix = '%%',
				},
				[2] = {
					per_lvl = 0.03,
					color = 'Green',
					suffix = '%%',
				},
				[3] = {
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
			},
		},
	},
	['Flying Fish'] = {
		id = 'FLYING_FISH',
		rarities = { 'R', 'E', 'L', 'M' },
		petType = 'Fishing Pet',
		stats = {
			str = {0.5},
			def = {0.5},
		},
		abilities = {
			name = {
				[1] = 'Quick Reel',
				[2] = 'Water Bender',
				[3] = 'Deep Sea Diver',
				[4] = 'Lava Bender',
				[5] = 'Magmatic Diver',
				[6] = 'Rapid Decay',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Grants <AQUA>+</AQUA>{0} STAT_FS.',
				[2] = 'Gives {1} STAT_STR and STAT_DEF when near water.',
				[3] = 'Increases the stats of [[Diver Armor]] and [[Abyssal Armor]] by {2}.',
				[4] = 'Gives {3} STAT_STR and STAT_DEF when near lava.',
				[5] = 'Increases the stats of [[Diver Armor]], [[Magma Lord Armor]], and [[Abyssal Armor]] by {4}.',
				[6] = 'Increases the chance to activate {{UltimateEnchantmentsLink|Flash}} Enchantment by {5}.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Grants &b+{0}☂ Fishing/&bSpeed&7.',
				[2] = '&7Gives &a{1} &c❁ Strength &7and/&7&a❈ Defense &7when near water.',
				[3] = '&7Increases the stats of Diver/&7Armor by &a{2}%',
				[4] = '&7Gives &a{3} &c❁ Strength &7and/&7&a❈ Defense &7when near  lava.',
				[5] = '&7Increases the stats of Magma/&7Lord armor by &a{4}%',
				[6] = '&7Increases the chance to/&7activate the &d&lFlash/&d&lEnchantment&a by {5}%&7.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} more STAT_FS per level',
				[2] = '+{1} more STAT_STR and STAT_DEF per level',
				[3] = '+{2} higher stat increase per level',
				[4] = '+{3} more STAT_STR and STAT_DEF per level',
				[5] = '+{4} higher stat increase per level',
				[6] = '+{5} higher chance for activation',
			},
		},
		variables = {
			rare = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.6,
					color = 'Aqua',
				},
				[1] = {
					per_lvl = 0.8,
					color = 'Green',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.75,
					color = 'Aqua',
				},
				[1] = {
					per_lvl = 1,
					color = 'Green',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.8,
					color = 'Aqua',
				},
				[1] = {
					per_lvl = 1,
					color = 'Green',
				},
				[2] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
			},
			mythic = {
				petimage = 'Flying Fish Pet (Mythic)',
				ability_indices = {1, 4, 5, 6},
				[0] = {
					per_lvl = 0.8,
					color = 'Aqua',
				},
				[3] = {
					per_lvl = 1,
					color = 'Green',
				},
				[4] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
				[5] = {
					per_lvl = 0.5,
					color = 'Green',
					suffix = '%%',
				},
			},
		},
	},
	['Frog'] = {
		id = 'FROG',
		rarities = { 'C', 'U', 'R', 'E', 'L' },
		petType = 'Foraging Pet',
		stats = {
			speed = {0.5},
			fs = {0.4},
			respiration = {0.1},
		},
		abilities = {
			name = {
				[1] = 'Hunting Enjoyer',
				[2] = 'Hop',
				[3] = 'Happy Tree Friends',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Increases your chance to catch <DARK_GREEN>Forest</DARK_GREEN>, <AQUA>Water</AQUA>, and <RED>Combat</RED> Shards by {0}.',
				[2] = 'Grants {1} STAT_FORF for <YELLOW>20</YELLOW> seconds every time you jump.',
				[3] = 'Grants {2} STAT_FORF for every other <DARK_GREEN>Frog Pet</DARK_GREEN> on the island, up to <AQUA>10</AQUA> frogs.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Increases your chance to catch/&2Forest&7, &bWater&7, and &cCombat &7Shards by /&a{0}%&7.',
				[2] = '&7Grants&6 {1}☘ Foraging Fortune &7for /&e20 &7seconds every time you jump.',
				[3] = '&7Grants&6 {2}☘ Foraging Fortune &7for /&7every other &2Frog Pet &7on the island,/&7up to &b10 &7frogs.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} higher chance to catch <DARK_GREEN>Forest</DARK_GREEN>, <AQUA>Water</AQUA>, and <RED>Combat</RED> Shards per level',
				[2] = '+{1} more STAT_FORF per level',
				[3] = '+{2} more STAT_FORF per level',
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					base = 1.0,
					per_lvl = 0.09,
					color = 'Green',
					suffix = '%%',
					round_down = true,
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					base = 1.0,
					per_lvl = 0.09,
					color = 'Green',
					suffix = '%%',
					round_down = true,
				},
			},
			rare = {
				ability_count = 1,
				[0] = {
					base = 1.0,
					per_lvl = 0.09,
					color = 'Green',
					suffix = '%%',
					round_down = true,
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					base = 1.0,
					per_lvl = 0.09,
					color = 'Green',
					suffix = '%%',
					round_down = true,
				},
				[1] = {
					base = 1.0,
					per_lvl = 0.79,
					color = 'Gold',
				},
			},
			legendary = {
				[0] = {
					base = 1.0,
					per_lvl = 0.09,
					color = 'Green',
					suffix = '%%',
					round_down = true,
				},
				ability_count = 3,
				[1] = {
					base = 1.0,
					per_lvl = 0.79,
					color = 'Gold',
				},
				[2] = {
					base = 1.0,
					per_lvl = 0.09,
					color = 'Gold',
				},
			},
		},
	},
	['Ghoul'] = {
		id = 'GHOUL',
		rarities = { 'E', 'L' },
		petType = 'Combat Pet',
		stats = {
			hp = {1},
			int = {0.75},
			fer = {0.05},
			vit = {0.25},
			md = {0.25},
		},
		abilities = {
			name = {
				[1] = 'Undead Slayer',
				[2] = 'Army of the Dead',
				[3] = 'Reaper Soul',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Gain {0} Combat XP against <GREEN>Zombies</GREEN>.',
				[2] = 'Increases the amount of souls you can store by <GREEN>2</GREEN> and the chance of getting a mob\'s soul by {1}.',
				[3] = 'Reduces the summoning cost of mobs by {2} and increases their damage output by {3}. Increases the health of all summoned mobs by {4}.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Gain &b{0} &7Combat XP against/&aZombies&7.',
				[2] = '&7Increases the amount of souls you/&7can store by &a2 &7and the chance of/&7getting a mob\'s soul by &a{1}%',
				[3] = '&7Reduces the summoning cost of mobs/&7by &a{2}% &7and increases their damage/&7output by &a{3}%&7. Increases the health/&7of all summoned mobs by &a{4}%&7.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} more Combat XP per level',
				[2] = '+{1} chance to get a mob\'s soul per level',
				[3] = '-{2} cost to summon a mob, increasing their damage output by {3} and the health by {4} per level',
			},
		},
		variables = {
			epic = {
				ability_count = 2,
				[0] = {
					base = 1.0,
					per_lvl = 0.005,
					color = 'Aqua',
					suffix = 'x',
				},
				[1] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					base = 1.0,
					per_lvl = 0.005,
					color = 'Aqua',
					suffix = 'x',
				},
				[1] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
				[2] = {
					per_lvl = 0.3,
					color = 'Green',
					suffix = '%%',
				},
				[3] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
				[4] = {
					per_lvl = 1,
					color = 'Green',
					suffix = '%%',
				},
			},
		},
	},
	['Giraffe'] = {
		id = 'GIRAFFE',
		rarities = { 'C', 'U', 'R', 'E', 'L' },
		petType = 'Foraging Pet',
		stats = {
			hp = {1},
			cc = {0.05},
			sr = {0.01},
		},
		abilities = {
			name = {
				[1] = 'Good Heart',
				[2] = 'Higher Ground',
				[3] = 'Long Neck',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Grants <RED>+</RED>{0} STAT_HR.',
				[2] = 'Increases your STAT_CD and STAT_STR by <RED>{1}%</RED> for every <YELLOW>0.1</YELLOW> STAT_SR over <YELLOW>3Ⓢ</YELLOW> (up to <YELLOW>6Ⓢ</YELLOW>).',
				[3] = 'Increases your melee damage by <RED>{2}</RED> if you are more than 3 blocks away from the target.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Grants &c+{0}❣ Health Regen&7.',
				[2] = '&7Increases your &9☠ Crit Damage &7and/&c❁ Strength &7by &c{1}% &7for every/&e0.1Ⓢ Swing Range &7over &e3Ⓢ &7(up to /&e6Ⓢ&7).',
				[3] = '&7Increases your melee damage by/&c{2} &7if you are more than 3 blocks/&7away from the target.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} higher STAT_HR per level',
				[2] = '+{1}% more STAT_STR and STAT_CD per level',
				[3] = '+{2} more damage increase per level',
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					base = 0.995,
					per_lvl = 0.995,
					color = 'Red',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					base = 1.495,
					per_lvl = 1.495,
					color = 'Red',
				},
			},
			rare = {
				ability_count = 2,
				[0] = {
					base = 1.495,
					per_lvl = 1.495,
					color = 'Red',
				},
				[1] = {
					per_lvl = 0.0015,
					color = 'Red',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					base = 1.99,
					per_lvl = 1.99,
					color = 'Red',
				},
				[1] = {
					per_lvl = 0.0015,
					color = 'Red',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 1.99,
					color = 'Red',
				},
				[1] = {
					per_lvl = 0.0015,
					color = 'Red',
				},
				[2] = {
					base = 50,
					per_lvl = 0.5,
					color = 'Red',
					suffix = '%%',
				},
			},
		},
	},
	['Glacite Golem'] = {
		id = 'GLACITE_GOLEM',
		rarities = { 'C', 'U', 'R', 'E' , 'L' },
		petType = 'Mining Pet',
		stats = {
			ms = {1.25},
			cr = {0.1},
		},
		abilities = {
			name = {
				[1] = 'Powder-powered',
				[2] = 'Iceborn',
				[3] = 'Frozen Perfection',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Gain <GREEN>+</GREEN>{0} more {{Glacite Powder}} from most sources.',
				[2] = 'Gain <GREEN>+</GREEN>{1} STAT_MNF while in the [[Glacite Mineshafts]].',
				[3] = 'Gain <GREEN>+</GREEN>{2} STAT_PRIS fore every [[Frozen Corpse]] you\'ve looted in the current [[Glacite Mineshaft]].',
			},
			tooltip = {
				-- the description of abilities used in the tooltip 
				[1] = '&7Gain &a+{0}%&7 more &bGlacite Powder &7from/&7most sources.',
				[2] = '&7Gain &a+{1} &6☘ Mining Fortune &7while in the/&bGlacite Mineshafts&7.',
				[3] = '&7Gain &a+{2} &5✧ Pristine &7for every/&bFrozen Corpse &7you\'ve looted in the/&7current &bGlacite Mineshaft&7.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell
				[1] = '+{0} more {{Glacite Powder}} per level',
				[2] = '+{1} more STAT_MNF per level',
				[3] = '+{2} more STAT_PRIS per level',
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.15,
					color = 'Green',
					suffix = '%%',
				},
			},
			rare = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.15,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.75,
					color = 'Green',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 1,
					color = 'Green',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 1,
					color = 'Green',
				},
				[2] = {
					per_lvl = 0.01,
					color = 'Green',
				},
			},
		},
	},
	['Goblin'] = {
		id = 'GOBLIN',
		rarities = { 'L' },
		petType = 'Mining Pet',
		stats = {
			spd = {0.2},
			ore_fortune = {1},
		},
		abilities = {
			name = {
				[1] = 'Grunt Work',
				[2] = 'Fetid Thief',
				[3] = 'Free-range Eggs',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Gain +{0} STAT_MS when mining <GOLD>Ores</GOLD>.',
				[2] = 'Gain +{1} STAT_MSR while in the <DARKGREEN>Mines of Divan</DARKGREEN>.',
				[3] = 'Increases the chance of finding rare goblin eggs by {2}.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip 
				[1] = '&7Gain &6+{0}⸕ Mining Speed &7when mining/&6Ores&7.',
				[2] = '&7Gain &e+{1}▚ Mining Spread &7while in the/&2Mines of Divan&7.',
				[3] = '&7Increases the chance of finding/&7rare goblin eggs by &a{2}%&7.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell
				[1] = '+{0} more STAT_MS per level',
				[2] = '+{1} more STAT_MSR per level',
				[3] = '+{2} higher chance per level',
			},
		},
		variables = {
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 2.5,
					color = 'Gold',
				},
				[1] = {
					per_lvl = 1,
					color = 'Yellow',
				},
				[2] = {
					per_lvl = 0.5,
					color = 'Green',
					suffix = '%%',
				},
			},
		},
	},
	['Golden Dragon'] = {
		id = 'GOLDEN_DRAGON',
		rarities = { 'L' },
		petType = 'Combat Pet',
		levels = '100-200',
		stats = {
			str = {0.25, 25},
			bas = {0.25, 25},
			mf = {0.05, 5},
		},
		abilities = {
			name = {
				[1] = 'Gold\'s Power',
				[2] = 'Shining Scales',
				[3] = 'Dragon\'s Greed',
				[4] = 'Legendary Treasure',
				[5] = 'Symbiosis',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Adds +{0} STAT_STR to all <GOLD>golden</GOLD> weapons.',
				[2] = 'Grants +<span title="Exactly 100/9"><RED>11.1</RED></span> STAT_STR and +<span title="Exactly 20/9"><AQUA>2.2</AQUA></span> STAT_MF to your pet for each digit in your <GOLD>Gold Collection</GOLD>. <DARK_GRAY>(Max 100M collection)</DARK_GRAY>',
				[3] = 'Grants +{1} STAT_STR per <AQUA>5</AQUA> STAT_MF. <DARK_GRAY>(Max +5%)</DARK_GRAY>',
				[4] = 'Gain {2}<RED>%</RED> STAT_DMG for every million coins in your bank. <DARK_GRAY>(Max 250%)</DARK_GRAY>',
				[5] = 'If you own a level <GREEN>200 Golden Dragon</GREEN>, gain <GOLD>+5 coins</GOLD> per monster kill for every other unique maxed Combat Pet that you own.'
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Adds &c+{0}❁ Strength &7to all &6golden/&7weapons.',
				[2] = '&7Grants &c+11.1❁ Strength &7and &b+2.2✯/&bMagic Find &7to your pet for each digit/&7in your &6Gold Collection&7./&8(Max 100M collection)',
				[3] = '&7Grants &c+{1} &c❁ Strength &7per &b5✯/&bMagic Find&7. &8(Max +5%)',
				[4] = '&7Gain &c{2}% &7damage for every million/&7coins in your bank. &8(Max 250%)',
				[5] = '&7If you own a level &a200 Golden/&aDragon&7, gain &6+5 coins &7per monster/&7kill for every other unique maxed/&7Combat Pet that you own.'
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} Strength per level',
				[2] = nil,
				[3] = '+{1} Strength per Magic Find per level',
				[4] = '+{2} more damage per level',
				[5] = nil,
			},
		},
		variables = {
			legendary = {
				ability_count = 4,
				[0] = {
					base = 50,
					per_lvl = 0.5,
					color = 'Red',
				},
				[1] = {
					base = 0.25,
					per_lvl = 0.0025,
					color = 'Red',
					suffix = '%%',
				},
				[2] = {
					base = 0.125,
					per_lvl = 0.00125,
					color = 'Red',
				},
			},
		},
	},
	['Golem'] = {
		id = 'GOLEM',
		rarities = { 'E', 'L' },
		petType = 'Combat Pet',
		stats = {
			hp = {1.5},
			str = {0.5},
			sr = {0.01},
		},
		abilities = {
			name = {
				[1] = 'Last Stand',
				[2] = 'Ricochet',
				[3] = 'Toss',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'While at less than <GREEN>20% HP</GREEN>, reduce incoming damage by <GREEN>20%</GREEN>. Additionally, gain a temporary shield equal to <GREEN>40%</GREEN> of your maximum health and deal <GREEN>40%</GREEN> more damage.<br/><DARKGRAY>(Lasts 12s, 60s cooldown)</DARKGRAY>',
				[2] = 'Your iron plating causes {0} of attacks to ricochet and hit the attacker.',
				[3] = 'Every 5 hits, throw the enemy up into the air and deal <GREEN>5x</GREEN> damage <DARKGRAY>(5s cooldown).</DARKGRAY>',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7While at less than &a20% HP&7, reduce/&7incoming damage by &a20%&7. Additionally,/&7gain a temporary shield equal to &a40%/&7of your maximum health and deal &a40%/&7more damage./&8(Lasts 12s, 60s cooldown)',
				[2] = '&7Your iron plating causes &a{0}% &7of/&7attacks to ricochet and hit the/&7attacker.',
				[3] = '&7Every 5 hits, throw the enemy up into/&7the air and deal &a5x &7damage &8(5s cooldown).',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} more attacks can ricochet',
			},
		},
		variables = {
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.25,
					color = 'Green',
					suffix = '%%',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.25,
					color = 'Green',
					suffix = '%%',
				},
			},
		},
	},
	['Grandma Wolf'] = {
		id = 'GRANDMA_WOLF',
		rarities = { 'C', 'U', 'R', 'E', 'L' },
		petType = 'Combat Pet',
		stats = {
			str = {0.25},
			hp = {1},
		},
		abilities = {
			name = {
				[1] = 'Kill Combo',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Gain buffs for combo kills. Effects stack as you increase your combo.<br/>{{Bull}}<GREEN>5 Combo</GREEN> <DARKGRAY>(lasts</DARKGRAY> <GREEN>{0}s</GREEN><DARKGRAY>)</DARKGRAY>{{Bull}}<DARKGRAY>+</DARKGRAY><AQUA>{6}</AQUA> STAT_MF<br/>{{Bull}}<GREEN>10 Combo</GREEN> <DARKGRAY>(lasts</DARKGRAY> <GREEN>{1}s</GREEN><DARKGRAY>)</DARKGRAY>{{Bull}}<DARKGRAY>+</DARKGRAY><GOLD>{7} coins per kill</GOLD><br/>{{Bull}}<GREEN>15 Combo</GREEN> <DARKGRAY>(lasts</DARKGRAY> <GREEN>{2}s</GREEN><DARKGRAY>)</DARKGRAY>{{Bull}}<DARKGRAY>+</DARKGRAY><AQUA>{8} STAT_MF</AQUA><br/>{{Bull}}<GREEN>20 Combo</GREEN> <DARKGRAY>(lasts</DARKGRAY> <GREEN>{3}s</GREEN><DARKGRAY>)</DARKGRAY>{{Bull}}<DARKAQUA>+</DARKAQUA>{9} STAT_CW<br/>{{Bull}}<GREEN>25 Combo</GREEN> <DARKGRAY>(lasts</DARKGRAY> <GREEN>{4}s</GREEN><DARKGRAY>)</DARKGRAY>{{Bull}}<DARKGRAY>+</DARKGRAY><AQUA>{6}</AQUA> STAT_MF<br/>{{Bull}}<GREEN>30 Combo</GREEN> <DARKGRAY>(lasts</DARKGRAY> <GREEN>{5}s</GREEN><DARKGRAY>)</DARKGRAY>{{Bull}}<DARKGRAY>+</DARKGRAY><GOLD>{7} coins per kill</GOLD>',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Gain buffs for combo kills./&7Effects stack as you increase/&7your combo.//&a5 Combo &8(lasts &a{0}s&8)/  &8+&b{6}% &b✯ Magic Find/&a10 Combo &8(lasts &a{1}s&8)/  &8+&6{7} &7coins per kill/&a15 Combo &8(lasts &a{2}s&8)/  &8+&b{8}% &b✯ Magic Find/&a20 Combo &8(lasts &a{3}s&8)/  &8+&3{9}☯ Combat Wisdom/&a25 Combo &8(lasts &a{4}s&8)/  &8+&b{6}% &b✯ Magic Find/&a30 Combo &8(lasts &a{5}s&8)/  &8+&6{7} &7coins per kill//&8This pet\'s perks are active/&8even when the pet is not/&8summoned!',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0}/{1}/{2}/{3}/{4}/{5}s increase in combo duration for 5/10/15/20/25/30 combos per level.',
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = { -- 5 kill combo
					per_lvl = 0.02,
					base = 8,
					color = 'Green',
				},
				[1] = { -- 10 kill combo
					per_lvl = 0.02,
					base = 6,
					color = 'Green',
				},
				[2] = { -- 15 kill combo
					per_lvl = 0.02,
					base = 4,
					color = 'Green',
				},
				[3] = { -- 20 kill combo
					per_lvl = 0.02,
					base = 3,
					color = 'Green',
				},
				[4] = { -- 25 kill combo
					per_lvl = 0.01,
					base = 3,
					color = 'Green',
				},
				[5] = { -- 30 kill combo
					per_lvl = 0.01,
					base = 2,
					color = 'Green',
				},
				[6] = { -- Magic Find 1
					per_lvl = 0,
					base = 1,
					color = 'Aqua',
					suffix = '%%',
				},
				[7] = { -- Coins 1
					per_lvl = 0,
					base = 2,
					color = 'Gold',
				},
				[8] = { -- Magic Find 2
					per_lvl = 0,
					base = 1,
					color = 'Aqua',
					suffix = '%%',
				},
				[9] = { -- Combat XP
					per_lvl = 0,
					base = 5,
					color = 'DarkAqua',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = { -- 5 kill combo
					per_lvl = 0.02,
					base = 8,
					color = 'Green',
				},
				[1] = { -- 10 kill combo
					per_lvl = 0.02,
					base = 6,
					color = 'Green',
				},
				[2] = { -- 15 kill combo
					per_lvl = 0.02,
					base = 4,
					color = 'Green',
				},
				[3] = { -- 20 kill combo
					per_lvl = 0.02,
					base = 3,
					color = 'Green',
				},
				[4] = { -- 25 kill combo
					per_lvl = 0.01,
					base = 3,
					color = 'Green',
				},
				[5] = { -- 30 kill combo
					per_lvl = 0.01,
					base = 2,
					color = 'Green',
				},
				[6] = { -- Magic Find 1
					per_lvl = 0,
					base = 1,
					color = 'Aqua',
					suffix = '%%',
				},
				[7] = { -- Coins 1
					per_lvl = 0,
					base = 4,
					color = 'Gold',
				},
				[8] = { -- Magic Find 2
					per_lvl = 0,
					base = 2,
					color = 'Aqua',
					suffix = '%%',
				},
				[9] = { -- Combat XP
					per_lvl = 0,
					base = 7,
					color = 'DarkAqua',
				},
			},
			rare = {
				ability_count = 1,
				[0] = { -- 5 kill combo
					per_lvl = 0.02,
					base = 8,
					color = 'Green',
				},
				[1] = { -- 10 kill combo
					per_lvl = 0.02,
					base = 6,
					color = 'Green',
				},
				[2] = { -- 15 kill combo
					per_lvl = 0.02,
					base = 4,
					color = 'Green',
				},
				[3] = { -- 20 kill combo
					per_lvl = 0.02,
					base = 3,
					color = 'Green',
				},
				[4] = { -- 25 kill combo
					per_lvl = 0.01,
					base = 3,
					color = 'Green',
				},
				[5] = { -- 30 kill combo
					per_lvl = 0.01,
					base = 2,
					color = 'Green',
				},
				[6] = { -- Magic Find 1
					per_lvl = 0,
					base = 2,
					color = 'Aqua',
					suffix = '%%',
				},
				[7] = { -- Coins 1
					per_lvl = 0,
					base = 6,
					color = 'Gold',
				},
				[8] = { -- Magic Find 2
					per_lvl = 0,
					base = 2,
					color = 'Aqua',
					suffix = '%%',
				},
				[9] = { -- Combat XP
					per_lvl = 0,
					base = 9,
					color = 'DarkAqua',
				},
			},
			epic = {
				ability_count = 1,
				[0] = { -- 5 kill combo
					per_lvl = 0.02,
					base = 8,
					color = 'Green',
				},
				[1] = { -- 10 kill combo
					per_lvl = 0.02,
					base = 6,
					color = 'Green',
				},
				[2] = { -- 15 kill combo
					per_lvl = 0.02,
					base = 4,
					color = 'Green',
				},
				[3] = { -- 20 kill combo
					per_lvl = 0.02,
					base = 3,
					color = 'Green',
				},
				[4] = { -- 25 kill combo
					per_lvl = 0.01,
					base = 3,
					color = 'Green',
				},
				[5] = { -- 30 kill combo
					per_lvl = 0.01,
					base = 2,
					color = 'Green',
				},
				[6] = { -- Magic Find 1
					per_lvl = 0,
					base = 2,
					color = 'Aqua',
					suffix = '%%',
				},
				[7] = { -- Coins 1
					per_lvl = 0,
					base = 8,
					color = 'Gold',
				},
				[8] = { -- Magic Find 2
					per_lvl = 0,
					base = 3,
					color = 'Aqua',
					suffix = '%%',
				},
				[9] = { -- Combat XP
					per_lvl = 0,
					base = 12,
					color = 'DarkAqua',
				},
			},
			legendary = {
				ability_count = 1,
				[0] = { -- 5 kill combo
					per_lvl = 0.02,
					base = 8,
					color = 'Green',
				},
				[1] = { -- 10 kill combo
					per_lvl = 0.02,
					base = 6,
					color = 'Green',
				},
				[2] = { -- 15 kill combo
					per_lvl = 0.02,
					base = 4,
					color = 'Green',
				},
				[3] = { -- 20 kill combo
					per_lvl = 0.02,
					base = 3,
					color = 'Green',
				},
				[4] = { -- 25 kill combo
					per_lvl = 0.01,
					base = 3,
					color = 'Green',
				},
				[5] = { -- 30 kill combo
					per_lvl = 0.01,
					base = 2,
					color = 'Green',
				},
				[6] = { -- Magic Find 1
					per_lvl = 0,
					base = 3,
					color = 'Aqua',
					suffix = '%%',
				},
				[7] = { -- Coins 1
					per_lvl = 0,
					base = 10,
					color = 'Gold',
				},
				[8] = { -- Magic Find 2
					per_lvl = 0,
					base = 3,
					color = 'Aqua',
					suffix = '%%',
				},
				[9] = { -- Combat XP
					per_lvl = 0,
					base = 15,
					color = 'DarkAqua',
				},
			},
		},
	},
	['Griffin'] = {
		id = 'GRIFFIN',
		rarities = { 'C', 'U', 'R', 'E', 'L', 'M' },
		petType = 'Combat Pet',
		stats = {
			str = {0.5},
			cc = {0.1},
			cd = {0.5},
			as = {0.25},
		},
		abilities = {
			name = {
				[1] = 'Odyssey',
				[2] = 'Sacred Strength',
				[3] = 'King of Kings',
				[4] = 'Ancient Earth',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = '{0} types of <DARKGREEN>Mythological</DARKGREEN> can spawn from <YELLOW>Griffin Burrows</YELLOW>. Their stats scale with your Griffin\'s rarity.',
				[2] = 'Gain <RED>+</RED>{1} STAT_STR when above <RED>85%</RED> health.',
				[3] = 'Grants <AQUA>+{2} Magic Find</AQUA> on <DARKGREEN>Mythological</DARKGREEN> mobs.',
				[4] = 'Grants <PINK>+{3}</PINK> STAT_TRA on <YELLOW>Griffin Burrows</YELLOW> for each burrow excavated in your current chain.'
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&c{0} &7types of &2✿ Mythological &7can/&7spawn from &eGriffin Burrows&7. Their/&7stats scale with your Griffin\'s/&7rarity.',
				[2] = '&7Gain &c+{1}% &c❁ Strength/&7when above &c85% &7health.',
				[3] = '&7Grants &b+{2} ✯ Magic Find &7on &2✿/&2Mythological &7mobs.',
				[4] = '&7Grants &d+{3} ❃ Tracking &7on &eGriffin/&eBurrows &7for each burrow excavated/&7in your current chain.'
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = nil,
				[2] = '+{1} more STAT_STR per level',
				[3] = '+{2} more STAT_MF per level',
				[4] = nil,
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					base = 2,
					per_lvl = 0,
					color = 'Red',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					base = 4,
					per_lvl = 0,
					color = 'Red',
				},
			},
			rare = {
				ability_count = 2,
				[0] = {
					base = 6,
					per_lvl = 0,
					color = 'Red',
				},
				[1] = {
					base = 0,
					per_lvl = 0.15,
					color = 'Red',
					suffix = '%%',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					base = 8,
					per_lvl = 0,
					color = 'Red',
				},
				[1] = {
					base = 0,
					per_lvl = 0.15,
					color = 'Red',
					suffix = '%%',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					base = 10,
					per_lvl = 0,
					color = 'Red',
				},
				[1] = {
					base = 0,
					per_lvl = 0.15,
					color = 'Red',
					suffix = '%%',
				},
				[2] = {
					base = 0,
					per_lvl = 0.2,
					color = 'Aqua',
				}
			},
			mythic = {
				ability_count = 4,
				[0] = {
					base = 12,
					per_lvl = 0,
					color = 'Red',
				},
				[1] = {
					base = 0,
					per_lvl = 0.15,
					color = 'Red',
					suffix = '%%',
				},
				[2] = {
					base = 0,
					per_lvl = 0.2,
					color = 'Aqua',
				},
				[3] = {
					base = 1,
					per_lvl = 0,
					color = 'Pink',
				}
			},
		},
	},
	['Guardian'] = {
		id = 'GUARDIAN',
		rarities = { 'C', 'U', 'R', 'E', 'L', 'M' },
		petType = 'Enchanting Pet',
		stats = {
			int = {1},
			def = {0.5},
		},
		abilities = {
			name = {
				[1] = 'Lazerbeam',
				[2] = 'Enchanting Wisdom Boost',
				[3] = 'Mana Pool',
				[4] = 'Lucky Seven',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Zaps your enemies for {0} your STAT_INT every <GREEN>3s</GREEN>.',
				[2] = 'Grants <DARK_AQUA>+</DARK_AQUA>{1}STAT_EW.',
				[3] = 'Regenerate {2} extra STAT_MANA, doubled when near or in water.',
				[4] = 'Gain <AQUA>+</AQUA>{3} chance to find <DARK_PURPLE>ultra rare</DARK_PURPLE> books in <LIGHT_PURPLE>Superpairs</LIGHT_PURPLE>.'
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Zaps your enemies for &b{0}x/&b&7your &b✎ Intelligence &7every/&7&a3s.',
				[2] = '&7Grants &3+{1}☯ Enchanting/&3Wisdom&7.',
				[3] = '&7Regenerate &b{2}% &7extra mana,/&7doubled when near or in water.',
				[4] = '&7Gain &b+{3}% &7chance to find/&5ultra rare &7books in/&dSuperpairs&7.'
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} higher zap damage per level',
				[2] = '+{1} higher STAT_EW per level',
				[3] = '+{2} higher STAT_MANA regeneration per level',
				[4] = '+{3} chance per level',
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.02,
					color = 'Aqua',
					suffix = 'x',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.06,
					color = 'Aqua',
					suffix = 'x',
				},
			},
			rare = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.1,
					color = 'Aqua',
					suffix = 'x',
				},
				[1] = {
					per_lvl = 0.25,
					color = 'Dark_Aqua',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.15,
					color = 'Aqua',
					suffix = 'x',
				},
				[1] = {
					per_lvl = 0.3,
					color = 'Dark_Aqua',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.2,
					color = 'Aqua',
					suffix = 'x',
				},
				[1] = {
					per_lvl = 0.3,
					color = 'Dark_Aqua',
				},
				[2] = {
					per_lvl = 0.3,
					color = 'Aqua',
					suffix = '%%',
				},
			},
			mythic = {
				ability_count = 4,
				[0] = {
					per_lvl = 1.2,
					color = 'Aqua',
					suffix = 'x',
				},
				[1] = {
					per_lvl = 0.3,
					color = 'Dark_Aqua',
				},
				[2] = {
					per_lvl = 0.3,
					color = 'Aqua',
					suffix = '%%',
				},
				[3] = {
					per_lvl = 0.07,
					color = 'Aqua',
					suffix = '%%',
				},
			},
		},
	},
	['Hedgehog'] = {
		id = 'HEDGEHOG',
		rarities = { 'L' },
		petType = 'Farming Pet',
		stats = {
			spd = {0.15, 0},
		},
		abilities = {
			name = {
				[1] = 'Spiky Quills',
				[2] = 'Fearsome Farmer',
				[3] = "Hunter's Insight",
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Deal {0} more damage to <DARK_GREEN>ൠ Pests</DARK_GREEN>.',
				[2] = 'Grants <GOLD>+</GOLD>{1} STAT_FMF against <DARK_GREEN>ൠ Pests</DARK_GREEN>.',
				[3] = 'Grants <GOLD>+</GOLD>{2} STAT_FMF per Pest Bestiary Tier (max of <GOLD>147☘</GOLD>).',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Deal &a{0}% &7more damage to &2ൠ Pests&7.',
				[2] = '&7Grants &6+{1}☘ Farming Fortune &7on &2ൠ/&2Pests&7.',
				[3] = '&7Grants &6+{2}☘ Farming Fortune&7 per/&7Pest Bestiary Tier.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '{0} more damage per level.',
				[2] = '+{1} STAT_FMF against pests per level.',
				[3] = '+{2} STAT_FMF per Pest Bestiary Tier per level.',
			},
		},
		variables = {
			legendary = {
				ability_count = 3,
				[0] = {
					base = 0,	
					per_lvl = 1,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					base = 0,
					per_lvl = 1,
					color = 'Gold',
					suffix = '',
				},
				[2] = {
					base = 0.7,
					per_lvl = 0,
					color = 'Gold',
					suffix = '',
				},
			},
		},
	},
	['Hermit Crab'] = {
		id = 'HERMIT_CRAB',
		rarities = { 'C', 'U', 'R', 'E', 'L', 'M'},
		petType = 'Fishing Pet',
		stats = {
			def = {0.2},
			fs = {0.2},
			scc = {0.02},
		},
		abilities = {
			name = {
				[1] = 'Comfort Zone',
				[2] = 'Seafloor Scalper',
				[3] = 'Crab Rave',
				[4] = 'Hotspot Hazard',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Grants +{0} STAT_FS for <GREEN>30s</GREEN> upon catching <GOLD>Treasure</GOLD>.',
				[2] = '<GOLD>Treasure</GOLD> catches are {1} more likely to be <GOLD>GREAT</GOLD> or <PINK>OUTSTANDING</PINK>.',
				[3] = 'Grants +{2} STAT_TC for each player with a <GREEN>Hermit Crab Pet</GREEN> within <GREEN>30</GREEN> blocks, up to <GREEN>5</GREEN> players.',
				[4] = 'Increases the chance of catching <PINK>Hotspot Sea Creatures</PINK> by {3}.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip 
				[1] = '&7Grants &b+{0}☂ Fishing Speed &7for &a30s/&7upon catching &6Treasure&7.',
				[2] = '&6Treasure &7catches are &a{1}% &7more/&7likely to be &6&lGREAT &7or &d&lOUTSTANDING&7.',
				[3] = '&7Grants &6+{2}⛃ Treasure Chance/&7for each player with a &aHermit Crab Pet/&7within &a30 &7blocks, up to &a5 &7players.',
				[4] = '&7Increases the chance of catching/&dHotspot Sea Creatures &7by &a{3}%&7.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell
				[1] = '+{0} more STAT_FS per level',
				[2] = '+{1} more likely per level',
				[3] = '+{2} higher STAT_TC per level',
				[4] = '+{3} higher chance per level',
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.2,
					color = 'Aqua',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.3,
					color = 'Aqua',
				},
			},
			rare = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.3,
					color = 'Aqua',
				},
				[1] = {
					per_lvl = 0.075,
					color = 'Green',
					suffix = '%%',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.4,
					color = 'Aqua',
				},
				[1] = {
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
			},
			legendary = {
				ability_count = '3',
				[0] = {
					per_lvl = 0.4,
					color = 'Aqua',
				},
				[1] = {
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
				[2] = {
					per_lvl = 0.002,
					color = 'Gold',
				},
			},
			mythic = {
				ability_count = '4',
				[0] = {
					per_lvl = 0.4,
					color = 'Aqua',
				},
				[1] = {
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
				[2] = {
					per_lvl = 0.002,
					color = 'Gold',
				},
				[3] = {
					per_lvl = 0.5,
					color = 'Green',
					suffix = '%%',
				},
			},
		},
	},
	['Horse'] = {
		id = 'HORSE',
		rarities = { 'C', 'U', 'R', 'E', 'L' },
		petType = 'Combat Mount',
		stats = {
			int = {0.5},
			spd = {0.25},
		},
		abilities = {
			name = {
				[1] = 'Rideable',
				[2] = 'Run',
				[3] = 'Ride Into Battle',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Right-click your summoned pet to ride it!',
				[2] = 'Increases the speed of your mount by {0}.',
				[3] = 'While riding your horse, gain +{1} bow damage.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Right-click your summoned pet/&7to ride it!',
				[2] = '&7Increases the speed of your/&7mount by &a{0}%',
				[3] = '&7While riding your horse, gain/&7+&a{1}% &7 bow damage.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = nil,
				[2] = '+{0} higher speed increase per level',
				[3] = '+{1} higher bow damage per level',
			},
		},
		variables = {
			common = {
				ability_count = 1,
			},
			uncommon = {
				ability_count = 1,
			},
			rare = {
				ability_count = 2,
				[0] = {
					per_lvl = 1.1,
					color = 'Green',
					suffix = '%%',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 1.2,
					color = 'Green',
					suffix = '%%',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 1.2,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.25,
					color = 'Green',
					suffix = '%%',
				},
			},
		},
	},
	['Hound'] = {
		id = 'HOUND',
		rarities = { 'E', 'L' },
		petType = 'Combat Pet',
		stats = {
			spd = {0.1},
			str = {0.4},
			as = {0.25},
			fer = {0.05},
		},
		abilities = {
			name = {
				[1] = 'Scavenger',
				[2] = 'Finder',
				[3] = 'Pack Slayer',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Gain +{0} coins per monster kill.',
				[2] = 'Increases the chance for monsters to drop their armor by {1}.',
				[3] = 'Gain <GREEN>+</GREEN>{2} Combat XP against <GREEN>Wolves</GREEN>.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Gain +&a{0} &7coins per monster kill.',
				[2] = '&7Increases the chance for monsters/&7to drop their armor by &a{1}%&7.',
				[3] = '&7Gain &b+{2} &7Combat XP against &aWolves&7.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} more COINS',
				[2] = '+{1} higher chance per level',
				[3] = '+{2} more Combat XP per level',
			},
		},
		variables = {
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 1,
					color = 'Gold',
				},
				[1] = {
					per_lvl = 0.3,
					color = 'Green',
					suffix = '%%',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 1,
					color = 'Gold',
				},
				[1] = {
					per_lvl = 0.3,
					color = 'Green',
					suffix = '%%',
				},
				[2] = {
					base = 1,
					per_lvl = 0.005,
					color = 'Green',
					suffix = 'x',
				},
			},
		},
	},
	['Jade Dragon'] = {
		id = 'JADE_DRAGON',
		rarities = { 'L' },
		petType = 'Foraging Pet',
		levels = '100-200',
		stats = {
			mf = {0.05, 5},
			frf = {0.25, 25},
			str = {0.25, 25},
		},
		abilities = {
			name = {
				[1] = 'Forest Power',
				[2] = 'Jade Scale',
				[3] = 'Dragon\'s Pride',
				[4] = 'Apex Predator',
				[5] = 'Symbiosis',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Adds +{0} STAT_STR and +{1} STAT_SPD to all your Axes.',
				[2] = 'Grants +<GOLD>15</GOLD> STAT_FRF and +<DARK_GREEN>4</DARK_GREEN> STAT_SWP for every digit in your <GREEN>Mangrove Collection</GREEN>. <DARK_GRAY>(Max 10M collection)</DARK_GRAY>',
				[3] = 'Grants +<GOLD>1</GOLD> STAT_FRF per <DARK_GREEN>5</DARK_GREEN> STAT_SWP.',
				[4] = 'Increases your total STAT_SWP by <DARK_GREEN>0.1%</DARK_GREEN> for every Maxed out Attribute you unlocked.',
				[5] = 'If you own a level <GREEN>200 Jade Dragon</GREEN>, Grants <GOLD>+4</GOLD> STAT_FRF for every other unique maxed Foraging Pet that you own..',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Adds &c{0}❁ Strength &7and &f{1}✦ Speed/&7to all your Axes.',
				[2] = '&7Grants &615☘ Foraging Fortune &7and/&24∮ Sweep &7for every digit in your/&aMangrove Collection&7./&8(Max 10M collection)' ,
				[3] = '&7Grants &61☘ Foraging Fortune &7per &25∮/&2Sweep&7.',
				[4] = '&7Increases your total &2∮ Sweep &7by/&20.1% &7for every Maxed out Attribute/&7you unlocked.',
				[5] = '&7If you own a level &a200 Jade Dragon&7,/&7Grants &6+4☘ Foraging Fortune for/&7every other unique maxed Foraging/&7Pet that you own..',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} strength per level and +{1} speed per level',
				[2] = nil,
				[3] = nil,
				[4] = nil,
				[5] = 'Only active on level 200',
			},
		},
		variables = {
			legendary = {
				ability_count = 5,
				[0] = {
					base = 75,
					per_lvl = 0.25,
					color = 'Red',
				},
				[1] = {
					base = 37.5,
					per_lvl = 0.125,
					color = 'White',
				},
			},
		},
	},
	['Jellyfish'] = {
		id = 'JELLYFISH',
		rarities = { 'E', 'L' },
		petType = 'Alchemy Pet',
		stats = {
			hp = {2},
			hr = {1},
		},
		abilities = {
			name = {
				[1] = 'Radiant Scyphozoa',
				[2] = 'Stored Energy',
				[3] = 'Powerful Potions',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'While in dungeons, reduces the mana cost of Power Orbs by {0}.',
				[2] = 'While in dungeons, for every <RED>2,000 HP</RED> you heal teammates the cooldown of <GREEN>Wish</GREEN> is reduced by {1}, up to <GREEN>30s</GREEN>.',
				[3] = 'While in dungeons, increase the effectiveness of Dungeon Potions by {2}',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7While in dungeons, reduces the/&7mana cost of/&7Power Orbs by &a{0}%&7.',
				[2] = '&7While in dungeons, for every/&c2,000 HP &7you heal teammates/&7the cooldown of &aWish &7is/&7reduced by &a{1}s&7, up to/&a30s&7.',
				[3] = '&7While in dungeons, increase/&7the effectiveness of Dungeon/&7Potions by &a{2}%',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '{0} decreased mana cost for Power Orbs per level',
				[2] = '<GREEN>Wish</GREEN> reduced by {1} per level',
				[3] = '+{2} more effectiveness per level',
			},
		},
		variables = {
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.5,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.01,
					color = 'Green',
					suffix = 's',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.5,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.01,
					color = 'Green',
					suffix = 's',
				},
				[2] = {
					per_lvl = 0.5,
					color = 'Green',
					suffix = '%%',
				},
			},
		},
	},
	['Jerry'] = {
		id = 'JERRY',
		rarities = { 'C', 'U', 'R', 'E', 'L', 'M' },
		petType = 'Combat Pet',
		stats = {
			int = {-1},
		},
		abilities = {
			name = {
				[1] = 'Jerry',
				[2] = 'Jerry',
				[3] = 'Jerry',
				[4] = 'Jerry',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Gain <GREEN>50%</GREEN> chance to deal your regular damage.',
				[2] = 'Gain <GREEN>100%</GREEN> chance to receive a normal amount of drops from mobs.',
				[3] = 'Actually adds {0} STAT_DMG to the [[Aspect of the Jerry]].',
				[4] = 'Tiny chance to find Jerry Candies when killing mobs.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Gain &a50% &7chance to deal/&7your regular damage.',
				[2] = '&7Gain &a100% &7chance to/&7receive a normal amount of drops/&7from mobs.',
				[3] = '&7Actually adds &c{0} damage &7to/&7the Aspect of the Jerry.',
				[4] = '&7Tiny chance to find Jerry/&7Candies when killing mobs.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = nil,
				[2] = nil,
				[3] = '+{0} more damage added per level',
				[4] = nil,
			},
		},
		variables = {
			common = {
				ability_count = 2,
			},
			uncommon = {
				ability_count = 2,
			},
			rare = {
				ability_count = 2,
			},
			epic = {
				ability_count = 2,
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.1,
					color = 'Red',
				},
			},
			mythic = {
				ability_count = 4,
				[0] = {
					per_lvl = 0.5,
					color = 'Red',
				},
			},
		},
	},
	['Kuudra'] = {
		id = 'KUUDRA',
		rarities = { 'C', 'U', 'R', 'E', 'L' },
		petType = 'Combat Pet',
		stats = {
			str = {0.4},
			hp = {4},
		},
		abilities = {
			name = {
				[1] = 'Wither Bait',
				[2] = 'Trophy Bait',
				[3] = 'Crimson',
				[4] = 'Kuudra Fortune',
				[5] = 'Kuudra Specialist',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Increases the odds of finding a {{MobSprite|Vanquisher}} by {0}.',
				[2] = 'Grants <GOLD>+</GOLD>{1} STAT_TFC.',
				[3] = 'Grants {2} extra [[Crimson Essence]].',
				[4] = 'Gain <GOLD>+</GOLD>{3} STAT_MNF while on the {{Zone|Crimson Isle}}.',
				[5] = 'Increases all damage to Kuudra and his minions by <RED>20%</RED>.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip 
				[1] = '&7Increases the odds of finding/&7a vanquisher by &a{0}%&7.',
				[2] = '&7Grants &6+{1}♔ Trophy Fish Chance&7.',
				[3] = '&7Grants &a{2}% &7extra Crimson/&7Essence.',
				[4] = '&7Gain &6+{3}☘ Mining Fortune/&7while on the Crimson Isle.',
				[5] = '&7Increases all damage to Kuudra and/&7his minions by &c20%&7.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell
				[1] = '+{0} odds of finding a [[Vanquisher]] per level',
				[2] = '+{1} more STAT_TFC per level',
				[3] = '+{2} extra [[Crimson Essence]] per level',
				[4] = '+{3} more STAT_MNF while on the [[Crimson Isle]] per level',
				[5] = nil,
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
			},
			uncommon = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.15,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.15,
					color = 'Gold',
				},
			},
			rare = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.15,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.15,
					color = 'Gold',
				},
				[2] = {
					per_lvl = 0.15,
					color = 'Green',
					suffix = '%%',
				},
			},
			epic = {
				ability_count = 4,
				[0] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.2,
					color = 'Gold',
				},
				[2] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
				[3] = {
					per_lvl = 1,
					color = 'Gold',
				},
			},
			legendary = {
				ability_count = '5',
				[0] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.2,
					color = 'Gold',
				},
				[2] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
				[3] = {
					per_lvl = 1,
					color = 'Gold',
				},
			},
		},
	},
	['Lion'] = {
		id = 'LION',
		rarities = { 'C', 'U', 'R', 'E', 'L' },
		petType = 'Foraging Pet',
		stats = {
			fer = {0.05},
			str = {0.5},
			spd = {0.25},
		},
		abilities = {
			name = {
				[1] = 'Primal Force',
				[2] = 'First Pounce',
				[3] = 'King of the Jungle',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Adds +{0} STAT_DMG and +{1} STAT_STR to your weapons.',
				[2] = 'First strike, Triple-strike, and {{Ench|combo}} are {2} more effective.',
				[3] = 'Deal +{3} STAT_DMG against mobs that have attacked you.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Adds &c+{0} &c❁ Damage &7and/&7&c+{1} &c❁ Strength &7to your/&7weapons.',
				[2] = '&7First Strike&7,/&7Triple-Strike&7, and &d&lCombo/&r&7are &a{2}% &7more effective.',
				[3] = '&7Deal &c+{3}% &c❁ Damage/&c&7against mobs that have/&7attacked you.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} more STAT_DMG per level; +{1} STAT_STR per level',
				[2] = '+{2} more damage per level',
				[3] = '+{3} more damage per level',
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.03,
					color = 'Red',
				},
				[1] = {
					per_lvl = 0.03,
					color = 'Red',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.05,
					color = 'Red',
				},
				[1] = {
					per_lvl = 0.05,
					color = 'Red',
				},
			},
			rare = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.1,
					color = 'Red',
				},
				[1] = {
					per_lvl = 0.1,
					color = 'Red',
				},
				[2] = {
					per_lvl = 0.75,
					color = 'Green',
					suffix = '%%',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.15,
					color = 'Red',
				},
				[1] = {
					per_lvl = 0.15,
					color = 'Red',
				},
				[2] = {
					per_lvl = 1,
					color = 'Green',
					suffix = '%%',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.2,
					color = 'Red',
				},
				[1] = {
					per_lvl = 0.2,
					color = 'Red',
				},
				[2] = {
					per_lvl = 1,
					color = 'Green',
					suffix = '%%',
				},
				[3] = {
					per_lvl = 1.5,
					color = 'Red',
					suffix = '%%',
				},
			},
		},
	},
	['Magma Cube'] = {
		id = 'MAGMA_CUBE',
		rarities = { 'C', 'U', 'R', 'E', 'L' },
		petType = 'Combat Pet',
		stats = {
			hp = {0.5},
			str = {0.2},
			def = {0.33},
		},
		abilities = {
			name = {
				[1] = 'Slimy Minions',
				[2] = 'Salt Blade',
				[3] = 'Hot Ember',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Slime minions work {0} faster while on your island.',
				[2] = 'Deal {1} more damage to slimes.',
				[3] = 'Buffs the stats of [[Ember Armor]] by {2}.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Slime minions work &a{0}%/&a&7faster while on your island.',
				[2] = '&7Deal &a{1}% &7more damage to/&7slimes.',
				[3] = '&7Buffs the stats of Ember Armor/&7by &a{2}%',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} higher minion speed bonus per level',
				[2] = '+{1} more damage per level',
				[3] = '+{2} higher buff per level',
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
			},
			rare = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.25,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.3,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.25,
					color = 'Green',
					suffix = '%%',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.3,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.25,
					color = 'Green',
					suffix = '%%',
				},
				[2] = {
					per_lvl = 0.5,
					color = 'Green',
					suffix = '%%',
				},
			},
		},
	},
	['Mammoth'] = {
		id = 'MAMMOTH',
		rarities = { 'L' },
		petType = 'Combat Pet',
		stats = {
			def = {0.5},
			cr = {0.1},
		},
		abilities = {
			name = {
				[1] = 'Wooly Coat',
				[2] = 'Tusk Luck',
				[3] = 'Corpse Crusher',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Gain a {0} chance for mobs to not inflict STAT_COLD when damaging you in the [[Glacite Mineshafts]].',
				[2] = 'Gain {1} Magic Find for every 100 STAT_MNF, doubled in the [[Glacite Tunnels]] and [[Glacite Mineshafts]].',
				[3] = 'Gain <ORANGE>+</ORANGE>{2}STAT_MNF for each [[Frozen Corpse]] looted in your current Glacite Mineshaft.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip 
				[1] = '&7Gain a &a{0}% &7chance for mobs to not/&7inflict &b❄ Cold &7when damaging you in/&7the &bGlacite Mineshafts&7.',
				[2] = '&7Gain &b+{1}✯ Magic Find &7for every/&7100 &6☘ Mining Fortune&7, doubled in the/&bGlacite Tunnels &7and &bGlacite/&bMineshafts&7.',
				[3] = '&7Gain &6+{2}☘ Mining Fortune &7for each/&bFrozen Corpse &7looted in your/&7current &bGlacite Mineshaft&7.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell
				[1] = '+{0} higher chance per level',
				[2] = '+{1} more STAT_MF per level',
				[3] = '+{2} more STAT_MNF per level',
			},
		},
		variables = {
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 1,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.005,
					color = 'Aqua',
				},
				[2] = {
					per_lvl = 0.3,
					color = 'Orange',
				},
			},
		},
	},
	['Megalodon'] = {
		id = 'MEGALODON',
		rarities = { 'E', 'L' },
		petType = 'Fishing Pet',
		stats = {
			str = {0.5},
			mf = {0.1},
			scc = {0.05, 5},
			fer = {0.05, 5},
			fs = {0.3, 10},
		},
		abilities = {
			name = {
				[1] = 'Blood Scent',
				[2] = 'Enhanced Scales',
				[3] = 'Feeding Frenzy',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Deal up to <RED>+</RED>{0} STAT_DMG based on the enemy\'s missing health.',
				[2] = 'Doubles the pet\'s base stats during the <AQUA>Fishing Festival</AQUA>.',
				[3] = 'Increases your chance to catch Sharks during the <AQUA>Fishing Festival</AQUA> by {1}.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Deal up to &c+{0}% &c❁ Damage &7based on/&7the enemy\'s missing health.',
				[2] = '&7Doubles the pet\'s base stats during/&7the &bFishing Festival&7.',
				[3] = '&7Increases your chance to catch/&7Sharks during the &bFishing Festival &7by/&a{1}&7.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} more damage dealt per level',
				[3] = '+{1} higher Shark chance per level',
			},
		},
		variables = {
			epic = {
				ability_count = 2,
				[0] = {
					base = 50,
					per_lvl = 1,
					color = 'Red',
					suffix = '%%',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					base = 50,
					per_lvl = 1,
					color = 'Red',
					suffix = '%%',
				},
				[1] = {
					base = 10,
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
			},
		},
	},
	['Mithril Golem'] = {
		id = 'MITHRIL_GOLEM',
		rarities = { 'C', 'U', 'R', 'E', 'L', 'M' },
		petType = 'Mining Pet',
		stats = {
			tdef = {0.5},
			mnf = {0.25},
		},
		abilities = {
			name = {
				[1] = 'Mithril Affinity',
				[2] = 'Subterranean Battler',
				[3] = 'The Smell Of Powder',
				[4] = 'Refined Senses',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Grants {0} STAT_MS when mining <DARKGREEN>Mithril</DARKGREEN>.',
				[2] = 'Grants {1} of most combat stats while on <AQUA>Mining Islands</AQUA>.',
				[3] = 'Grants +{2} <DARKGREEN>Mithril Powder</DARKGREEN> from all sources.',
				[4] = 'Grants +{3} <AQUA>Magic Find</AQUA> while on <AQUA>Mining Islands</AQUA>.'
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Grants &6+{0}&6⸕ Mining Speed &7when/&7mining &2Mithril&7.',
				[2] = '&7Grants &a+{1}% &7of most combat stats/&7while on &bMining Islands&7.',
				[3] = '&7Grants &2+{2}% ᠅ Mithril Powder &7from/&7all sources.',
				[4] = '&7Grants &b+{3}% ✯ Magic Find&7 while on/&bMining Islands&7.'
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} more Mining Speed while mining <YELLOW>Mithril</YELLOW>',
				[2] = '+{1} more combat stats on mining islands',
				[3] = '+{2} extra <DARKGREEN>Mithril Powder</DARKGREEN>',
				[4] = '+{3} more Magic Find when on a Mining Island'
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					per_lvl = 1,
					color = 'Orange',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					per_lvl = 1.5,
					color = 'Orange',
				},
			},
			rare = {
				ability_count = 2,
				[0] = {
					per_lvl = 1.5,
					color = 'Orange',
				},
				[1] = {
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 2,
					color = 'Orange',
				},
				[1] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 2,
					color = 'Orange',
				},
				[1] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
				[2] = {
					per_lvl = 0.2,
					color = 'DarkGreen',
					suffix = '%%',
				},
			},
			mythic = {
				ability_count = 4,
				[0] = {
					per_lvl = 2,
					color = 'Orange',
				},
				[1] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
				[2] = {
					per_lvl = 0.2,
					color = 'DarkGreen',
					suffix = '%%',
				},
				[3] = {
					per_lvl = 0.1,
					color = 'Aqua',
					suffix = '%%',
				},
			},
		},
	},
	['Mole'] = {
		id = 'MOLE',
		rarities = { 'L' },
		petType = 'Mining Pet',
		stats = {
			int = {1},
			mf = {0.05},
			ms = {0.75},
		},
		abilities = {
			name = {
				[1] = 'Archaeologist',
				[2] = 'Magnetic Nose',
				[3] = 'Nucleic Explorer',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Increase your chance of finding Scavenged Items in the Mines of Divan by {0}.',
				[2] = 'Automatons drop their parts {1} more frequently.',
				[3] = 'Gain a {2} chance to receive an extra drop when completing the Crystal Nucleus.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip 
				[1] = '&7Increase your chance of finding/&cScavenged Items &7in the &2Mines of/&2Divan &7by {0}&7.',
				[2] = '&9Automatons &7drop their parts &a50%/&7more frequently.',
				[3] = '&7Gain a {2} &7chance to receive an/&7extra drop when completing the/&dCrystal Nucleus&7.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell
				[1] = '+{0} higher chance per level',
				[2] = '+{1} higher drop rate per level',
				[3] = '+{2} higher chance per level',
			},
		},
		variables = {	
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.25,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.5,
					color = 'Green',
					suffix = '%%',
				},
				[2] = {
					per_lvl = 1,
					color = 'Green',
					suffix = '%%',
				},
			},
		},
	},
	['Monkey'] = {
		id = 'MONKEY',
		rarities = { 'C', 'U', 'R', 'E', 'L' },
		petType = 'Foraging Pet',
		stats = {
			spd = {0.2},
			int = {0.5},
		},
		abilities = {
			name = {
				[1] = 'Treeborn',
				[2] = 'Vine Swing',
				[3] = 'Evolved Axes',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Grants +{0} STAT_FRF, which increases your chances at double logs.',
				[2] = 'Gain +{1} STAT_SPD while in [[The Park]].',
				[3] = 'Grants +{2} STAT_SWP while in [[The Park]].',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Grants &a+{0} &6☘ Foraging/&6Fortune&7, which increases your/&7chance at double logs.',
				[2] = '&7Gain +&a{1} &f✦ Speed &7while/&7in The Park.',
				[3] = '&7Grants &2{2}∮ Sweep &7while in &aThe Park',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} higher chance per level',
				[2] = '+{1} more STAT_SPD per level',
				[3] = '+{2} more STAT_SWP per level',
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.4,
					color = 'Green',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.5,
					color = 'Green',
				},
			},
			rare = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.5,
					color = 'Green',
				},
				[1] = {
					per_lvl = 0.75,
					color = 'Green',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.6,
					color = 'Green',
				},
				[1] = {
					per_lvl = 1,
					color = 'Green',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.6,
					color = 'Green',
				},
				[1] = {
					per_lvl = 1,
					color = 'Green',
				},
				[2] = {
					per_lvl = 0.1,
					color = 'Green',
				},
			},
		},
	},
	['Montezuma'] = {
		id = 'MONTEZUMA', -- placeholder, couldn't find it shown in game
		rarities = { 'R', 'E' },
		level = 100,
		petType = 'Fractured Soul Pet',
		stats = {
			rt = {0, 25},
			mr = {0, 0, req = 'epic'},
		},
		abilities = {
			name = {
				[1] = 'Nine Lives',
				[2] = 'Trickery',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Gain <GREEN>+</GREEN>{0} STAT_RT per soul piece.',
				[2] = 'Gain <AQUA>+</AQUA>{1} STAT_MR per soul piece found.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Gain &a+{0}ф Rift Time &7per/&7soul piece.',
				[2] = '&7Gain &b+{1}⚡ Mana Regen &7per/&7soul piece found.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = nil,
				[2] = nil,
			},
		},
		variables = {
			rare = {
				ability_count = 1,
				[0] = {
					base = 15,
					per_lvl = 0,
					color = 'Green',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					base = 15,
					per_lvl = 0,
					color = 'Green',
				},
				[1] = {
					base = 2,
					per_lvl = 0,
					color = 'Aqua',
				},
			},
		},
	},
	['Mooshroom Cow'] = {
		id = 'MOOSHROOM_COW',
		rarities = { 'C', 'U', 'R', 'E', 'L' },
		petType = 'Farming Pet',
		stats = {
			hp = {1},
			fmf = {1,10},
		},
		abilities = {
			name = {
				[1] = 'Efficient Mushrooms',
				[2] = 'Mushroom Eater',
				[3] = 'Farming Strength',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Mushroom and Mycelium minions work {0} faster while on your island.',
				[2] = 'When Breaking crops, there is a {1} chance that a mushroom will drop.',
				[3] = 'Gain <GOLD>+0.7</GOLD> STAT_FMF per every {2} STAT_STR.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Mushroom and Mycelium/&7minions work &a{0}% &7faster while/&7on your island.',
				[2] = '&7When Breaking crops, there is/&7a &a{1}% &7chance that a/&7mushroom will drop.',
				[3] = '&7Gain &6+0.7☘ Farming Fortune/&7per every &c{2} ❁ Strength&7.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} higher speed boost per level',
				[2] = '+{1} higher drop chance per level',
				[3] = '{2} lower strength requirement per farming fortune per level',
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
			},
			rare = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.3,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 1, 	
					color = 'Green',
					suffix = '%%',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.3,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 1, 	
					color = 'Green',
					suffix = '%%',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.3,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 1, 	
					color = 'Green',
					suffix = '%%',
				},
				[2] = {
					base = 40,
					per_lvl = -0.2, 	
					color = 'Red',
				},
			},
		},
	},
	['Mosquito'] = {
        id = 'MOSQUITO',
        rarities = { 'C', 'U', 'R', 'E', 'L' },
        petType = 'Farming Pet',
        stats = {
            spd = {0.2},
            bpc = {0.5},
        },
        abilities = {
            name = {
                [1] = 'Smooth Jazz',
                [2] = 'Buzzin\' Barterer',
                [3] = 'Bloodsucker\'s Betrayal',
            },
            desc = {
                -- the description of abilities used in the two top cells
                [1] = 'Pest Vinyls are +{0} more effective.',
                [2] = 'Gain +{1} STAT_SCF for every unique visitor you\'ve served in <GREEN>The Garden</GREEN>.<br/><DARK_GRAY>Your Bonus: # Sugar Cane Fortune<br/>Capped at 175 Fortune</DARK_GRAY>',
                [3] = 'When collected, <DARK_GREEN>Pest Traps</DARK_GREEN> will catch the next pest {2} faster.',
            },
            tooltip = {
                [1] = '&7Pest Vinyls are &a+{0}% &7more effective.',
                [2] = '&7Gain &6+{1}☘ Sugar Cane Fortune &7for/&7every unique visitor you\'ve served/&7in &aThe Garden&7./&8Your Bonus: # Sugar Cane Fortune/&8Capped at 175 Fortune',
                [3] = '&7When collected, &2Pest Traps &7will catch/&7the next pest &a{2}% &7faster.',
            },
            bonus_desc = {
                -- the description of abilities used in the bottom cell.
                [1] = '+{0} more effective per level',
                [2] = '+{1} more STAT_SCF per unique visitor per level',
                [3] = '+{2} faster Pest Traps per level',
            },
        },
        variables = {
			common = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.25,
					color = 'Green',
					suffix = '%%',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.25,
					color = 'Green',
					suffix = '%%',
				},
			},
			rare = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.35,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.01, 	
					color = 'Gold',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.5,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.02, 	
					color = 'Gold',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.5,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.02, 	
					color = 'Gold',
				},
				[2] = {
					per_lvl = 0.2, 	
					color = 'Green',
					suffix = '%%',
				},
			},
		},
    },
	['Ocelot'] = {
		id = 'OCELOT',
		rarities = { 'C', 'U', 'R', 'E', 'L' },
		petType = 'Foraging Pet',
		stats = {
			spd = {0.5},
			fer = {0.1},
		},
		abilities = {
			name = {
				[1] = 'Foraging Wisdom Boost',
				[2] = 'Tree Hugger',
				[3] = 'Tree Essence',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Grants <DARK_AQUA>+</DARK_AQUA>{0}STAT_FRW.',
				[2] = 'Foraging minions work {1} faster while on your island.',
				[3] = 'Gain a {2} chance to get exp from breaking a log.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Grants &3+{0}☯ Foraging/&3Wisdom&7.',
				[2] = '&7Foraging minions work &a{1}%/&a&7faster while on your island.',
				[3] = '&7Gain a &a{2}% &7chance to get/&7exp from breaking a log.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} STAT_FRW per level',
				[2] = '+{1} higher speed boost per level',
				[3] = '+{2} higher chance per level',
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.2,
					color = 'Dark_Aqua',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.25,
					color = 'Dark_Aqua',
				},
			},
			rare = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.25,
					color = 'Dark_Aqua',
				},
				[1] = {
					per_lvl = 0.3,
					color = 'Green',
					suffix = '%%',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.3,
					color = 'Dark_Aqua',
				},
				[1] = {
					per_lvl = 0.3,
					color = 'Green',
					suffix = '%%',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.3,
					color = 'Dark_Aqua',
				},
				[1] = {
					per_lvl = 0.3,
					color = 'Green',
					suffix = '%%',
				},
				[2] = {
					per_lvl = 0.3,
					color = 'Green',
					suffix = '%%',
				},
			},
		},
	},
	['Owl'] = {
		id = 'OWL',
		rarities = { 'L' },
		petType = 'Taming Pet',
		stats = {},
		abilities = {
			name = {
				[1] = 'Training Refunds',
				[2] = 'Efficient Trainer',
				[3] = 'Fast Learner',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'The more coins to spend on Fann\'s Sessions, the less coins they will cost. <DARK_GRAY>(max 5% off).</DARK_GRAY>',
				[2] = 'Makes training sessions at Fann more efficient when added into a session.\n\nIncreased EXP: <AQUA>+{0} EXP</AQUA>',
				[3] = 'Passively grants <DARK_AQUA>+</DARK_AQUA>{1}STAT_TW.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7The more coins to spend on/&7Fann\'s Sessions, the less coins/&7they will cost. &8(max 5% off).',
				[2] = '&7Makes training sessions at/&7Fann more efficient when added/&7into a session.//&7Increased EXP: &b+{0}% EXP',
				[3] = '&7Passively grants &3+{1}☯ Taming/&3Wisdom',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = nil,
				[2] = '+{0} increased pet training EXP per level',
				[3] = '+{1} more STAT_TW per level',
			},
		},
		variables = {
			legendary = {
				ability_count = 3,
				[0] = {
					base = 0.1,
					per_lvl = 0.099,
					color = 'Aqua',
					suffix = '%%',
				},
				[1] = {
					base = 0.05,
					per_lvl = 0.045,
					color = 'Dark_Aqua',
				}
			},
		},
	},
	['Parrot'] = {
		id = 'PARROT',
		rarities = { 'E', 'L' },
		petType = 'Alchemy Pet',
		stats = {
			int = {1},
			cd = {0.1},
		},
		abilities = {
			name = {
				[1] = 'Flamboyant',
				[2] = 'Repeat',
				[3] = 'Bird Discourse',
				[4] = 'Parrot Feather Infusion',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Adds {0} level(s) to [[Accessories|intimidation accessories]].',
				[2] = 'Boosts potions duration by {1}.',
				[3] = 'Gives +{2} STAT_STR to players within 20 Blocks <DARK_GRAY>(doesn\'t stack)</DARK_GRAY>.',
				[4] = 'When summoned or in your pets menu, boost the duration of consumed [[God Potion|God Potions]] by +{3}.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Adds &a{0} &7levels to/&7intimidation accessories.',
				[2] = '&7Boosts potions duration by/&7&a{1}%',
				[3] = '&7Gives &c+{2}❁ Strength &7to/&7players within &a20 &7blocks/&8Doesn\'t stack.',
				[4] = '&7When summoned or in your pets/&7menu, boost the duration of/&7consumed &cGod Potions &7by/&7&a{3}%',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+<GREEN>1</GREEN> level per ≈{4} level(s)',
				[2] = '+{1} higher duration boost per level',
				[3] = '+{2} more STAT_STR per level',
				[4] = '+{3} higher duaration boost per level',
			},
		},
		variables = {
			epic = {
				ability_count = 2,
				[0] = {
					eval = 'Parrot',
					base = 1,
					color = 'Green',
				},
				[1] = {
					per_lvl = 0.35,
					base = 5,
					color = 'Green',
					suffix = '%%',
				},
				[4] = {
					per_lvl = 7, -- only used in bonus_desc
					color = 'Green',
				},
			},
			legendary = {
				ability_count = 4,
				[0] = {
					eval = 'Parrot',
					base = 1,
					color = 'Green',
				},
				[1] = {
					per_lvl = 0.35,
					base = 5,
					color = 'Green',
					suffix = '%%',
				},
				[2] = {
					per_lvl = 0.25,
					base = 5,
					color = 'Green',
				},
				[3] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
				[4] = {
					per_lvl = 5, -- only used in bonus_desc
					color = 'Green'
				},
			},
		},
	},
	['Penguin'] = {
		id = 'PENGUIN',
		rarities = { 'L' },
		petType = 'Fishing Pet',
		stats = {
			scc = {0.1},
		},
		abilities = {
			name = {
				[1] = 'Thick Blubber',
				[2] = 'Chilly Reception',
				[3] = 'Subzero Hero',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Each time you catch a <DARK_AQUA>Sea Creature</DARK_AQUA>, reduce your STAT_COLD by {0}.',
				[2] = 'Grants <AQUA>+{1}</AQUA>STAT_CR for each player within <GREEN>30</GREEN> blocks, up to <GREEN>10</GREEN> players.',
				[3] = 'Gain <AQUA>+</AQUA>{2}STAT_FS while in the <AQUA>Glacite Tunnels</AQUA>.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip 
				[1] = '&7Each time you catch a Sea Creature,/&7reduce your &b❄ Cold &7by &a{0}&7.',
				[2] = '&7Grants &b+{1}❄ Cold Resistance &7for/&7each player within &a30 &7blocks, up to/&a10 &7players.',
				[3] = '&7Gain &b+{2}☂ Fishing Speed&7 while in the/&bGlacite Tunnels&7.',	
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell
				[1] = '+{0} STAT_COLD reduced per level',
				[2] = '+{1} STAT_CR per level',
				[3] = '+{2} STAT_FS per level',
			},
		},
		variables = {
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.05,
					base = 1,
					color = 'Green',
					round_down = true,
				},
				[1] = {
					per_lvl = 0.01,
					base = 0,
					color = 'Aqua',
				},
				[2] = {
					per_lvl = 0.75,
					color = 'Aqua',
				},
			},
		},
	},
	['Phoenix'] = {
		id = 'PHOENIX',
		rarities = { 'E', 'L' },
		petType = 'Combat Pet',
		stats = {
			str = {0.5, 10},
			int = {1, 50},
		},
		abilities = {
			name = {
				[1] = 'Rekindle',
				[2] = 'Fourth Flare',
				[3] = 'Magic Bird',
				[4] = 'Eternal Coins',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Before death, become immune and gain {0} STAT_STR for {1} seconds (1 minute cooldown)',
				[2] = 'On 4th melee strike, ignite mobs, dealing {2} your STAT_CD each second for {3} seconds.',
				[3] = 'You may always fly on your [[Private Island]].',
				[4] = 'Don\'t lose COINS from death.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Before death, become &eimmune/&e&7and gain &c{0} &c❁ Strength/&c&7for &a{1} &7seconds./&81 minute cooldown',
				[2] = '&7On 4th melee strike, &6ignite/&6&7mobs, dealing &c{2}x &7your &9☠/&9Crit Damage &7each second for/&7&a{3} &7seconds.',
				[3] = '&7You may always fly on your/&7private island.',
				[4] = '&7Don\'t lose coins from death.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} STAT_STR per level; duration increases by {1} second',
				[2] = '+{2} more damage bonus per level; duration increases by {3} second',
				[3] = nil,
				[4] = nil,
			},
		},
		variables = {
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.1,
					base = 10,
					color = 'Red',
				},
				[1] = {
					per_lvl = 0.02,
					base = 2,
					color = 'Green',
					round_down = true,
				},
				[2] = {
					per_lvl = 0.12,
					base = 1,
					color = 'Red',
					suffix = '×',
				},
				[3] = {
					per_lvl = 0.02,
					base = 2,
					color = 'Green',
					round_down = true,
				},
			},
			legendary = {
				ability_count = 4,
				[0] = {
					per_lvl = 0.15,
					base = 15,
					color = 'Red',
				},
				[1] = {
					per_lvl = 0.02,
					base = 2,
					color = 'Green',
					round_down = true,
				},
				[2] = {
					per_lvl = 0.14,
					base = 1,
					color = 'Red',
					suffix = '×',
				},
				[3] = {
					per_lvl = 0.03,
					base = 2,
					color = 'Green',
					round_down = true,
				},
			},
		},
	},
	['Pig'] = {
		id = 'PIG',
		rarities = { 'C', 'U', 'R', 'E', 'L' },
		petType = 'Farming Mount',
		stats = {
			spd = {0.15},
			potato_fortune = {0.2},
		},
		abilities = {
			name = {
				[1] = 'Hamfisted',
				[2] = 'Shining Stampede',
				[3] = 'Pig Parade',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Increase {{c}} gain from {{gold|Shiny Pigs}} by {0}%.',
				[2] = 'Grants +{1} {{gold|Potato Fortune}} per {{gold|Shiny Pig}} {{DarkAqua|Bestiary}} tier.',
				[3] = 'Increases the base stats of this pet by {2} during the {{Pink|Year of the Pig}}.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Increases &6Coin &7gain from &6Shiny Pigs/&7by &a{0}%&7.',
				[2] = '&7Grants &6+{1}☘ Potato Fortune &7per/&6Shiny Pig &3Bestiary &7tier.',
				[3] = '&7Increases the base stats of this pet/&7by &a{2}% &7during the &dYear of the Pig&7.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0}% more Coins from Shiny Pigs per level.',
				[2] = '+{1} more Potato Farming Fortune per Shiny Pig Bestiary tier per pet level',
				[3] = '+{2}% more increase to pet\'s base stats during Year of the Pig per level',
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.35,
					color = 'Green',
					suffix = '%%',
				},
			},
			rare = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.35,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.04,
					color = 'Gold',
					suffix = '☘',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.5,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.05,
					color = 'Gold',
					suffix = '☘',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.5,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.05,
					color = 'Gold',
					suffix = '☘',
				},
				[2] = {
					per_lvl = 1,
					color = 'Green',
					suffix = '%%',
				},
			},
		},
	},
	['Pigman'] = {
		id = 'PIGMAN',
		rarities = { 'C', 'U', 'R', 'E', 'L' },
		petType = 'Combat Pet',
		stats = {
			str = {0.5},
			def = {0.5},
			fer = {0.05},
		},
		abilities = {
			name = {
				[1] = 'Bacon Farmer',
				[2] = 'Pork Master',
				[3] = 'Giant Slayer',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = '[[Pig Minion|Pig minions]] work {0} faster while on your island.',
				[2] = 'Buffs the [[Pigman Sword]] by {1} STAT_DMG and {2} STAT_STR.',
				[3] = 'Deal <RED>+50%</RED> damage to monsters Level <GREEN>50+</GREEN> and <RED>+75%</RED> damage to monsters Level <GREEN>100+</GREEN>.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Pig minions work &a{0}%/&a&7faster while on your island.',
				[2] = '&7Buffs the Pigman sword by &a{1}/&a&c❁ Damage &7and &a{2} &c❁/&cStrength.',
				[3] = '&7Deal &c+50% &7damage to monsters Level/&a50+ &7and &c+75% damage to monsters/&7Level &a100+&7.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} higher minion speed boost per level',
				[2] = '+{1} more STAT_DMG per level; +{2} STAT_STR per level',
				[3] = 'None',
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
			},
			rare = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.3,
					color = 'Green',
				},
				[2] = {
					per_lvl = 0.15,
					color = 'Green',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.3,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.4,
					color = 'Green',
				},
				[2] = {
					per_lvl = 0.25,
					color = 'Green',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.3,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.4,
					color = 'Green',
				},
				[2] = {
					per_lvl = 0.25,
					color = 'Green',
				},
			},
		},
	},
	['Precursor Drone'] = {
		id = 'PRECURSOR_DRONE',
		rarities = { 'C' },
		petType = 'Combat Pet',
		stats = {
			scc = {0.1, 0},
			mining_fortune = {0.3, 0},
			foraging_fortune = {0.3, 0},
		},
		abilities = {
		    name = {
		        [1] = 'Contraband',
		        [2] = 'Grungle',
		        [3] = 'Mining Off Camera',
		    },
		    desc = {
		        [1] = 'Catching a <DARK_AQUA>Sea Creature</DARK_AQUA> has a <GREEN>10%</GREEN> chance to also give you <GOLD>Treasure</GOLD>.',
		        [2] = 'You can now ONLY throw your Foraging Axe, but it has <RED>no throwing penalty</RED> anymore.',
		        [3] = 'While mining, each collection progress grants a <GREEN>0.005%</GREEN> chance to drop a random enchanted mining item.',
		    },
		    tooltip = {
		        [1] = '&7Catching a &3Sea Creature &7has a &a10%/&7chance to also give you &6Treasure&7.',
		        [2] = '&7You can now ONLY throw your/&7Foraging Axe, but it has &cno throwing/&cpenalty&7 anymore.',
		        [3] = '&7While mining, each collection/&7progress grants a &a0.005% &7chance to/&7drop a random enchanted mining item.',
		    },
			bonus_desc = {
				[1] = nil,
				[2] = nil,
				[3] = nil,
			},
		},
		variables = {
			common = {
				ability_count = 3,
			},
		},
	},
	['Rabbit'] = {
		id = 'RABBIT',
		rarities = { 'C', 'U', 'R', 'E', 'L', 'M' },
		petType = 'Farming Pet',
		stats = {
			hp = {1},
			spd = {0.2},
		},
		abilities = {
			name = {
				[1] = 'Happy Feet',
				[2] = 'Farming Wisdom Boost',
				[3] = 'Efficient Farming',
				[4] = 'Chocolate Injections',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Jump potions also give +{0} STAT_SPD',
				[2] = 'Grants <DARK_AQUA>+</DARK_AQUA>{1}STAT_FMW.',
				[3] = '[[Minions|Farming minions]] work {2} faster while on your island.',
				[4] = 'Increases <YELLOW>[[Chocolate Factory]]</YELLOW> production by {3}. Duplicate <GREEN>Chocolate Rabbits</GREEN> that you find grant <GOLD>+</GOLD>{4} <GOLD>[[Chocolate]]</GOLD>.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Jump potions also give &a+{0}/&a&7speed.',
				[2] = '&7Gives &3+{1}☯ Farming/&3Wisdom&7.',
				[3] = '&7Farming minions work &a{2}%/&a&7faster while on your island.',
				[4] = '&7Increases &6Chocolate Factory/&7production by &a+{3}x&7. Duplicate/&aChocolate Rabbits&7 that you find/&7grant &6+{4}% Chocolate.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} more STAT_SPD per level',
				[2] = '+{1} STAT_FMW per level',
				[3] = '+{2} higher speed boost',
				[4] = '+{3} production multiplier and +{4} more Chocolate per level',
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.3,
					color = 'Green',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.4,
					color = 'Green',
				},
			},
			rare = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.4,
					color = 'Green',
				},
				[1] = {
					per_lvl = 0.25,
					color = 'Dark_Aqua',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.5,
					color = 'Green',
				},
				[1] = {
					per_lvl = 0.3,
					color = 'Dark_Aqua',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.5,
					color = 'Green',
				},
				[1] = {
					per_lvl = 0.3,
					color = 'Dark_Aqua',
				},
				[2] = {
					per_lvl = 0.3,
					color = 'Green',
					suffix = '%%',
				},
			},
			mythic = {
				ability_count = 4,
				[0] = {
					per_lvl = 0.5,
					color = 'Green',
				},
				[1] = {
					per_lvl = 0.3,
					color = 'Dark_Aqua',
				},
				[2] = {
					per_lvl = 0.3,
					color = 'Green',
					suffix = '%%',
				},
				[3] = {
					per_lvl = 0.0004,
					base = 0.01,
					color = 'Green',
					suffix = 'x',
				},
				[4] = {
					per_lvl = 0.32,
					base = 1.3,
					color = 'Gold',
					suffix = '%%',
				},
			},
		},
	},
	['Rat'] = {
		id = 'RAT',
		rarities = { 'L', 'M' },
		petType = 'Combat Morph',
		stats = {
			cd = {0.1},
			str = {0.5},
			hp = {1},
		},
		abilities = {
			name = {
				[1] = 'Morph',
				[2] = 'CHEESE!',
				[3] = 'Rat\'s Blessing',
				[4] = 'Extreme Speed',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Right-click your summoned pet to morph into it!',
				[2] = 'As a Rat, you smell {{Yellow|CHEESE}} nearby! Yummy!',
				[3] = 'Has a chance to grant a random player +{0} STAT_MF for {1} seconds after finding a yummy piece of Cheese! If the player gets a drop during this buff, you have a {{Green|20%}} chance to get it too.',
				[4] = 'The Rat is TWO times faster.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Right-click your summoned pet/&7to morph into it!',
				[2] = '&7As a Rat, you smell/&7&e&lCHEESE&r&7 nearby! Yummy!',
				[3] = '&7Has a chance to grant a random/&7player &b+{0}✯ Magic Find&7 for/&7&a{1}&7 seconds after finding a/&7yummy piece of Cheese! If the/&7player gets a drop during this/&7buff, you have a &a20% &7chance/&7to get it too.',
				[4] = '&7The Rat is TWO times faster.'
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = nil,
				[2] = nil,
				[3] = '+{0} more STAT_MF and +{1} seconds per level',
				[4] = nil,
			},
		},
		variables = {
			legendary = {
				ability_count = 3,
				[0] = {  -- Magic Find
					per_lvl = 0.05,
					base = 2,
					color = 'Green',
				},
				[1] = {  -- Seconds
					per_lvl = 0.4,
					base = 20,
					color = 'Green',
				},
			},
			mythic = {
				ability_count = 4,
				[0] = {  -- Magic Find
					per_lvl = 0.05,
					base = 2,
					color = 'Green',
				},
				[1] = {  -- Seconds
					per_lvl = 0.4,
					base = 20,
					color = 'Green',
				},
			},
		},
	},
	['Reindeer'] = {
		id = 'REINDEER',
		rarities = { 'L' },
		petType = 'Fishing Pet',
		stats = {
			hp = {1},
			scc = {0.05},
			fs = {0.25},
		},
		abilities = {
			name = {
				[1] = 'Winter Spirit',
				[2] = 'Infused',
				[3] = 'Snow Power',
				[4] = 'Icy Wind',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Gain <PINK>double</PINK> pet <GREEN>EXP</GREEN>.',
				[2] = 'Gives <AQUA>+</AQUA>{0} STAT_FS and <DARK_AQUA>+10</DARK_AQUA>STAT_SCC while on <RED>Jerry\'s Workshop</RED>.',
				[3] = 'Grants <GREEN>+{1}</GREEN> bonus gift chance during the <RED>Gift Attack</RED> event.',
				[4] = 'Grants <GREEN>+{2}</GREEN> chance of getting double <AQUA>Ice Essence</AQUA>.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Gain &ddouble &7pet &aEXP&7.',
				[2] = '&7Gives &b+{0}&b☂ Fishing Speed/&7and &3+10&α Sea Creature/&3Chance &7while on &cJerry\'s/&cWorkshop&7.',
				[3] = '&7Grants &a+{1}% &7bonus gift/&7chance during the &cGift Attack/&c&7event.',
				[4] = '&7Grants &a+{2}% &7chance of/&7getting double &bIce Essence&7.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = nil,
				[2] = '+{0} more STAT_FS per level',
				[3] = '+{1} bonus gift chance per level',
				[4] = '+{2} chance of getting double <AQUA>Ice Essence</AQUA> per level',
			},
		},
		variables = {
			legendary = {
				ability_count = 4,
				[0] = {
					per_lvl = 0.75,
					color = 'Aqua',
				},
				[1] = {
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
				[2] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
			},
		},
	},
	['Rift Ferret'] = {
		id = 'RIFT_FERRET',
		rarities = { 'E', 'L' },
		petType = 'Combat Pet',
		stats = {
			spd = {0.5},
			int = {-0.02},
		},
		abilities = {
			name = {
				[1] = 'Orbs are Fun',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Gain <GREEN>+</GREEN>{0} experience from <AQUA>XP Orbs</AQUA>.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Gain &a+{0}% &7experience from/&bXP Orbs&7.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = nil,
			},
		},
		variables = {
			epic = {
				ability_count = 1,
				[0] = {
					base = 10,
					per_lvl = 0,
					color = 'Green',
					suffix = '%%',
				},
			},
			legendary = {
				ability_count = 1,
				[0] = {
					base = 10,
					per_lvl = 0,
					color = 'Green',
					suffix = '%%',
				},
			},
		},
	},
	['Rock'] = {
		id = 'ROCK',
		rarities = { 'C', 'U', 'R', 'E', 'L' },
		petType = 'Mining Mount',
		stats = {
			def = {2},
			tdef = {0.1},
		},
		abilities = {
			name = {
				[1] = 'Rideable',
				[2] = 'Sailing Stone',
				[3] = 'Fortify',
				[4] = 'Steady Ground',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Right-click on your summoned pet to ride it!',
				[2] = 'Sneak to move your rock to your location (15s cooldown)',
				[3] = 'While sitting on your rock, gain +{0} STAT_DEF',
				[4] = 'While sitting on your rock, gain +{1} STAT_DMG',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Right-click your summoned pet/&7to ride it!',
				[2] = '&7Sneak to move your rock to/&7your location (15s cooldown).',
				[3] = '&7While sitting on your rock,/&7gain +&a{0}% &7defense.',
				[4] = '&7While sitting on your rock,/&7gain &c+{1}x &7damage.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = nil,
				[2] = nil,
				[3] = '+{0} more STAT_DEF per level',
				[4] = '+{1} more STAT_DMG per level',
			},
		},
		variables = {
			common = {
				ability_count = 2,
			},
			uncommon = {
				ability_count = 2,
			},
			rare = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
			},
			epic = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.25,
					color = 'Green',
					suffix = '%%',
				},
			},
			legendary = {
				ability_count = 4,
				[0] = {
					per_lvl = 0.25,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.3,
					color = 'Red',
				},
			},
		},
	},
['Rose Dragon'] = {
		id = 'ROSE_DRAGON',
		rarities = { 'L' },
		petType = 'Farming Pet',
		levels = '100-200',
		stats = {
			spd = {0.5, 50},
			fmf = {0.2, 20},
		},
		abilities = {
			name = {
				[1] = 'Garden Power',
				[2] = 'Rosy Scales',
				[3] = 'Dragon\'s Gluttony',
				[4] = 'Spiritual Perfection',
				[5] = 'Symbiosis',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Grants +{0} STAT_FMF per <GREEN>Farming</GREEN> level.',
				[2] = 'Grants +{1} STAT_FMF and +{2} STAT_SPD per Crop Milestone.',
				[3] = 'Increases the chance to drop rare items when breaking crops by {3}.',
				[4] = 'Gain {4} more <RED>Copper</RED> from <GREEN>Garden Visitors</GREEN> and from analyzing <YELLOW>Mutations</YELLOW>.',
				[5] = 'If you own a level <GREEN>200 Rose Dragon</GREEN>, Grants <GOLD>+3</GOLD> STAT_FMF for every other unique maxed Farming Pet that you own.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Grants +&6{0}☘ Farming Fortune per/&aFarming &7level.',
				[2] = '&7Grants &60.15☘ Farming Fortune &7and/&f0.1✦ Speed&7 per Crop/Milestone.' ,
				[3] = '&7Increases the chance to drop rare/items when breaking crops by &a40%&7.',
				[4] = '&7Gain &a20% &7more &cCopper &7from &aGarden/&aVisitors&7 and from analyzing &eMutations&7.',
				[5] = '&7If you own a level &a200 Rose Dragon&7,/&7Grants &6+3☘ Farming Fortune for/&7every other unique maxed Farming/&7Pet that you own.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} STAT_FMF per level',
				[2] = '+{1} STAT_FMF and +{2} STAT_SPD per level',
				[3] = '+{3} drop chance per level',
				[4] = '+{4} more Copper per level',
				[5] = 'Only active on level 200',
			},
		},
		variables = {
			legendary = {
				ability_count = 5,
				[0] = {
					base = 1.5,
					per_lvl = 0.015,
					color = 'Orange',
				},
				[1] = {
					base = 0.075,
					per_lvl = 0.00075,
					color = 'Orange',
				},
				[2] = {
					base = 0.05,
					per_lvl = 0.0005,
					color = 'White',
				},
				[3] = {
					base = 20,
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
				[4] = {
					base = 10,
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
			},
		},
	},
	['Scatha'] = {
		id = 'SCATHA',
		rarities = { 'R', 'E', 'L' },
		petType = 'Mining Pet',
		stats = {
			ms = {1},
			mnf = {1.25},
		},
		abilities = {
			name = {
				[1] = 'Burrowing',
				[2] = 'Drill Infusion',
				[3] = 'Bejeweled Eyes',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Grants a <GREEN>+</GREEN>{0} chance to find <YELLOW>Treasure Chests</YELLOW> while mining.',
				[2] = 'Grants <GOLD>+</GOLD>{1}<GOLD>☘ Gemstone Fortune</GOLD> to Drills.',
				[3] = 'Earn <GREEN>+</GREEN>{2} {{Gemstone Powder}} from all sources.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Grants a &a+{0}% &7chance to find/&eTreasure Chests &7while mining.',
				[2] = '&7Grants &6+{1}☘ Gemstone Fortune &7to/&7Drills.',
				[3] = '&7Earn &a+{2}% &dGemstone Powder &7from all/&7sources.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} higher chance to find <YELLOW>Treasure Chests</YELLOW> while mining per level',
				[2] = '+{1} more <GOLD>☘ Gemstone Fortune</GOLD> to Drills per level',
				[3] = '+{2} more {{Gemstone Powder}} from all sources per level',
			},
		},
		variables = {
			rare = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.3,
					color = 'Green',
					suffix = '%%',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.4,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 1,
					color = 'Gold',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.5,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 1.25,
					color = 'Gold',
				},
				[2] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
			},
		},
	},
	['Seal'] = {
		id = 'SEAL',
		rarities = { 'C', 'U', 'R', 'E', 'L' },
		petType = 'Fishing Pet',
		stats = {
			fs = {0.35},
			scc = {0.05},
            tc = {0.01},
		},
		abilities = {
			name = {
				[1] = 'Showboater',
				[2] = 'Peak Performance',
				[3] = 'Amphibious',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Increases your chance of catching {{Purple|Bouncy Beach Balls}} and {{Gold|Giant Bouncy Beach Balls}} during the {{Blue|Year of the Seal}} by {0}.',
				[2] = 'Gain a {1} chance to materialize some {{Green|Golden Bait}} in your inventory upon catching Treasure.',
				[3] = 'Increases the base stats of this pet by {2} during the {{Blue|Year of the Seal}}.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Increases your chance of catching/&5Bouncy Beach Balls &7and &6Giant Bouncy/&6Beach Balls &7during the &9Year of the/&9Seal &7by &a{0}%&7.',
				[2] = '&7Gain a &a{1}% &7chance to materialize/&7some &aGolden Bait &7in your/&7inventory upon catching &6Treasure&7.',
				[3] = '&7Increases the base stats of this pet/&7by &a{2}% &7during the &9Year of the Seal&7.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} higher chance to catch Bouncy and Giant Bouncy Beach Balls',
				[2] = '+{1} higher chance to gain Treasure Bait on treasure catch',
				[3] = '+{2} more base stats during Year of the Seal',
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					per_lvl = 1,
					color = 'Green',
					suffix = '%%',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					per_lvl = 1,
					color = 'Green',
					suffix = '%%',
				},
			},
			rare = {
				ability_count = 2,
				[0] = {
					per_lvl = 1,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.05,
					color = 'Green',
					suffix = '%%',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 1,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.05,
					color = 'Green',
					suffix = '%%',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 1,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.05,
					color = 'Green',
					suffix = '%%',
				},
				[2] = {
					per_lvl = 1,
					color = 'Green',
					suffix = '%%',
				},
			},
		},
	},
	['Sheep'] = {
		id = 'SHEEP',
		rarities = { 'C', 'U', 'R', 'E', 'L' },
		petType = 'Alchemy Pet',
		stats = {
			int = {1},
			ad = {0.2},
		},
		abilities = {
			name = {
				[1] = 'Mana Saver',
				[2] = 'Overheal',
				[3] = 'Dungeon Wizard',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Reduces the STAT_MANA cost of abilities by {0}.',
				[2] = 'Gives a {1} shield after not taking damage for <GREEN>10s</GREEN>.',
				[3] = 'Increases your total STAT_MANA by {2} while in [[Dungeons]].',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Reduces the mana cost of/&7abilities by &a{0}%',
				[2] = '&7Gives a &a{1}% &7shield after/&7not taking damage for 10s.',
				[3] = '&7Increases your total mana by/&7&a{2}% &7while in dungeons.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} more STAT_MANA reduction per level',
				[2] = '+{1} tougher shield per level',
				[3] = '+{2} more STAT_MANA per level',
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
			},
			rare = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
				[2] = {
					per_lvl = 0.25,
					color = 'Green',
					suffix = '%%',
				},
			},
		},
	},
	['Silverfish'] = {
		id = 'SILVERFISH',
		rarities = { 'C', 'U', 'R', 'E', 'L' },
		petType = 'Mining Pet',
		stats = {
			def = {1},
			mnf = {0.2},
		},
		abilities = {
			name = {
				[1] = 'Magnetic',
				[2] = 'Experienced Burrower',
				[3] = 'Dexterity',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Earn +{0} more Exp when mining.',
				[2] = 'Grants <DARK_AQUA>+</DARK_AQUA>{1}STAT_MW.',
				[3] = 'Grants <ORANGE>+</ORANGE>{2} STAT_MS and permanent <YELLOW>Haste I/II/III</YELLOW>',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Earn &a+{0}% &7more Exp when mining.',
				[2] = '&7Grants &3+{1}☯ Mining Wisdom&7.',
				[3] = '&7Grants &6+{2}⸕ Mining Speed &7and/&7permanent &eHaste I\\/II\\/III&7.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} more Exp per level',
				[2] = '+{1} STAT_MW per level',
				[3] = '+{2} STAT_MS per level and +1 Haste level at Lvl 50 & 100'
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.3,
					color = 'Green',
					suffix = '%%',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.4,
					color = 'Green',
					suffix = '%%',
				},
			},
			rare = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.4,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.2,
					color = 'Dark_Aqua',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.5,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.25,
					color = 'Dark_Aqua',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.5,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.3,
					color = 'Dark_Aqua',
				},
				[2] = {
					per_lvl = 1.5,
					color = 'Orange'
				},
			},
		},
	},
	['Skeleton'] = {
		id = 'SKELETON',
		rarities = { 'C', 'U', 'R', 'E', 'L' },
		petType = 'Combat Pet',
		stats = {
			cc = {0.15},
			cd = {0.3},
		},
		abilities = {
			name = {
				[1] = 'Bone Arrows',
				[2] = 'Combo',
				[3] = 'Skeletal Defense',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Increase arrow damage by {0} which is tripled while in [[Dungeons]]',
				[2] = 'Gain a combo stack for every bow hit granting +3 Strength. Max {1} stacks, stacks disappear after <GREEN>8</GREEN> seconds.',
				[3] = 'Your skeleton shoots an arrow dealing <GREEN>30x</GREEN> your STAT_CD when a mob gets close to you (5s cooldown)',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Increase arrow damage by/&7&a{0}%&7 which is tripled while/&7in dungeons.',
				[2] = '&7Gain a combo stack for every/&7bow hit granting +&a3 &c❁/&cStrength&7. Max &a{1} &7stacks,/&7stacks disappear after 8/&7seconds.',
				[3] = '&7Your skeleton shoots an arrow/&7dealing &a30x &7your &9☠ Crit/&9Damage &7when a mob gets close/&7to you (5s cooldown).',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} higher arrow damage increase per level',
				[2] = '+{1} more stacks per level',
				[3] = nil,
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.15,
					color = 'Green',
					suffix = '%%',
				},
			},
			rare = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.15,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.15,
					color = 'Green',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.17,
					color = 'Green',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.2,
					color = 'Green',
				},
			},
		},
	},
	['Skeleton Horse'] = {
		id = 'SKELETON_HORSE',
		rarities = { 'L' },
		petType = 'Combat Mount',
		stats = {
			int = {1},
			spd = {0.5},
		},
		abilities = {
			name = {
				[1] = 'Rideable',
				[2] = 'Run',
				[3] = 'Ride Into Battle',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Right-click your summoned pet to ride it!',
				[2] = 'Increases the speed of your mount by {0}.',
				[3] = 'While riding your horse, gain +{1} bow damage.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Right-click your summoned pet/&7to ride it!',
				[2] = '&7Increases the speed of your/&7mount by &a{0}%',
				[3] = '&7While riding your horse, gain/&7+&a{1}% &7 bow damage.',
			},
			bonus_desc = {
					-- the description of abilities used in the bottom cell.
					[1] = nil,
					[2] = '+{0} higher speed increase per level',
					[3] = '+{1} higher bow damage per level',
			},
		},
		variables = {
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 1.5,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.4,
					color = 'Green',
					suffix = '%%',
				},
			},
		},
	},
	['Slug'] = {
		id = 'SLUG',
		rarities = { 'E', 'L' },
		petType = 'Farming Pet',
		stats = {
			def = {0.2},
			int = {0.25},
		},
		abilities = {
			name = {
				[1] = 'Slow and Steady',
				[2] = 'Pest Friends',
				[3] = 'Repugnant Aroma',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'When fishing in the <RED>Crimson Isle</RED>, <GREEN>Slugfish</GREEN> take <GREEN>{0}</GREEN> less time to catch.',
				[2] = 'Grants +{1} STAT_BPC.',
				[3] = 'When farming in a plot affected by a <GREEN>Sprayonator</GREEN>, gain +{2} STAT_FMF.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7When fishing in the &cCrimson/&cIsle&7, &aSlugfish &7take &a{0}%/&7less time to catch.',
				[2] = '&7Grants &2+{1}ൠ Bonus Pest/&2Chance&7.',
				[3] = '&7When farming in a plot/&7affected by a &aSprayonator&7,/&7gain &6+{2}☘ Farming Fortune&7.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = 'Slugfish take {0} less time to catch per level',
				[2] = '+{1} more STAT_BPC per level',
				[3] = '+{2} more STAT_FMF per level',
			},
		},
		variables = {
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.5,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.4,
					color = 'Dark Green',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.5,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.4,
					color = 'Dark Green',
				},
				[2] = {
					per_lvl = 1,
					color = 'Gold',
				},
			},
		},
	},
	['Snail'] = {
		id = 'SNAIL',
		rarities = { 'C', 'U', 'R', 'E', 'L' },
		petType = 'Mining Pet',
		stats = {
			def = {1},
			int = {1},
		},
		abilities = {
			name = {
				[1] = 'Red Sand Enjoyer',
				[2] = 'Slow and Steady',
				[3] = 'Slimy Reach',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = '<BLUE>Red Sand Minions</BLUE> work {0} faster while on your island.',
				[2] = 'Convert every {1}STAT_SPD you have above <WHITE>100</WHITE> into <GOLD>+1</GOLD>STAT_BKF.',
				[3] = 'Grants <YELLOW>+</YELLOW>{2}STAT_MSD while mining mining <BLUE>Blocks</BLUE>.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&9Red Sand Minions &7work &a{0}% &7faster/while on your &bPrivate Island&7.',
				[2] = '&7Convert every &f{1}✦ Speed &7you have/&7above &f100 &7into &6+1☘ Block Fortune&7.',
				[3] = '&7Grants &e+{2}▚ Mining Spread &7while/&7mining &9Blocks&7.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '<GREEN>+</GREEN>{0} more Red Sand Minion speed per level',
				[2] = '{1} less <WHITE>✦ Speed</WHITE> needed to gain <GOLD>+1 Block Fortune</GOLD>, per level',
				[3] = '<YELLOW>+</YELLOW>{2} more <YELLOW>▚ Mining Spread</YELLOW> per level',
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
			},
			rare = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					base = 6,
					per_lvl = -0.03,
					color = 'White',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.3,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					base = 6,
					per_lvl = -0.03,
					color = 'White',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.3,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					base = 5,
					per_lvl = -0.03,
					color = 'White',
				},
				[2] = {
					per_lvl = 4,
					color = 'Yellow',
				},
			},
		},
	},
	['Snowman'] = {
		id = 'SNOWMAN',
		rarities = { 'L', 'M' },
		petType = 'Combat Pet',
		stats = {
			str = {0.25},
			dmg = {0.25},
			cd = {0.25},
		},
		abilities = {
			name = {
				[1] = 'Blizzard',
				[2] = 'Frostbite',
				[3] = 'Snow Cannon',
				[4] = 'Ouch!',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Enemies within {0} blocks are slowed by <GREEN>25%</GREEN> and deal {1} less damage.',
				[2] = 'Your freezing aura slows enemy attacks causing you to take {2} reduced damage.',
				[3] = 'Shoots a snowball towards an enemy when you attack dealing {3} of your last dealt melee damage, capped at <WHITE>200,000</WHITE>. <DARK_GRAY>(1s cooldown).</DARK_GRAY>',
				[4] = 'Your snowballs have <GREEN>50%</GREEN> chance of dealing <RED>double</RED> damage!',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Enemies within &a{0} &7blocks are slowed/&7by &a25% &7and deal &a{1}% &7less damage.',
				[2] = '&7Your freezing aura slows enemy/&7attacks causing you to take &a{2}%/&7reduced damage.',
				[3] = '&7Shoots a snowball towards an enemy/&7when you attack dealing &a{3}% &7of/&7your last dealt melee damage,/&7capped at &f200,000&7. &8(1s cooldown).',
				[4] = '&7Your snowballs have &a50% &7chance of/&7dealing &cdouble &7damage!',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} more blocks per level, +{1} higher damage reduction per level',
				[2] = '+{2} higher damage reduction per level',
				[3] = '+{3} higher damage scaling per level',
				[4] = nil,
			},
		},
		variables = {
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.08,
					base = 8,
					color = 'Green',
				},
				[1] = {
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
				[2] = {
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
				[3] = {
					per_lvl = 0.1,
					base = 10,
					color = 'Green',
					suffix = '%%',
				},
			},
			mythic = {
				petimage = 'Snowman Pet (Mythic)',
				ability_count = 4,
				[0] = {
					per_lvl = 0.08,
					base = 8,
					color = 'Green',
				},
				[1] = {
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
				[2] = {
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
				[3] = {
					per_lvl = 0.1,
					base = 10,
					color = 'Green',
					suffix = '%%',
				},
			},
		},
	},
	['Spider'] = {
		id = 'SPIDER',
		rarities = { 'C', 'U', 'R', 'E', 'L', 'M' },
		petType = 'Combat Pet',
		stats = {
			str = {0.5},
			cc = {0.1},
		},
		abilities = {
			name = {
				[1] = 'One With the Spider',
				[2] = 'Web-Weaver',
				[3] = 'Spider Whisperer',
				[4] = 'Web Battlefield',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Applies {0} STAT_STR to all <DARK_RED>Arachnal Ж</DARK_RED> weapons, armor, and equipment you have equipped.',
				[2] = 'Upon hitting a monster it becomes slowed by {1}.',
				[3] = 'Spider and tarantula minions work {2} faster while on your island.',
				[4] = 'Killing mobs grants {3} STAT_STR and {4} STAT_MF for <GREEN>40s</GREEN> to all players staying within <GREEN>20</GREEN> blocks of where they died. <DARK_GRAY>Stacks up to 10 times.</DARK_GRAY>',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Applies &c{0} ❁ Strength &7to all/&7&4Arachnal Ж &7weapons, armor, and/&7equipment you have equipped.',
				[2] = '&7Upon hitting a monster it/&7becomes slowed by &a{1}%',
				[3] = '&7Spider and tarantula minions/&7work &a{2}% &7faster while on/&7your island.',
				[4] = '&7Killing mobs grants &c+{3}❁/&cStrength &7and &b+{4} Magic Find/&7for &a40s &7to all players/&7staying within &a20 &7blocks/&7of where they died. &8Stacks/&8up to 10 times.'
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} more STAT_STR per level',
				[2] = '+{1} higher slowness per level',
				[3] = '+{2} higher speed boost per level',
				[4] = '+{3} STAT_STR and +{4} STAT_MF per level',
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					base = 1,
					per_lvl = 0.02,
					color = 'Red',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					base = 2,
					per_lvl = 0.04,
					color = 'Red',
				},
			},
			rare = {
				ability_count = 2,
				[0] = {
					base = 3,
					per_lvl = 0.06,
					color = 'Red',
				},
				[1] = {
					per_lvl = 0.4,
					color = 'Green',
					suffix = '%%',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					base = 4,
					per_lvl = 0.08,
					color = 'Red',
				},
				[1] = {
					per_lvl = 0.4,
					color = 'Green',
					suffix = '%%',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					base = 5,
					per_lvl = 0.1,
					color = 'Red',
				},
				[1] = {
					per_lvl = 0.4,
					color = 'Green',
					suffix = '%%',
				},
				[2] = {
					per_lvl = 0.3,
					color = 'Green',
					suffix = '%%',
				},
			},
			mythic = {
				ability_count = 4,
				[0] = {
					base = 5,
					per_lvl = 0.1,
					color = 'Red',
				},
				[1] = {
					per_lvl = 0.4,
					color = 'Green',
					suffix = '%%',
				},
				[2] = {
					per_lvl = 0.3,
					color = 'Green',
					suffix = '%%',
				},
				[3] = {
					base = 0,
					per_lvl = 0.06,
					color = 'Red',
				},
				[4] = {
					base = 0,
					per_lvl = 0.01,
					color = 'Aqua',
				},
			},
		},
	},
	['Spinosaurus'] = {
		id = 'SPINOSAURUS',
		rarities = { 'L' },
		petType = 'Fishing Pet',
		stats = {
			scc = {0.08},
			fs = {0.25},
		},
		abilities = {
			name = {
				[1] = 'Sharp Attitude',
				[2] = 'Pursuit',
				[3] = 'Primordial Fisher',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = '[[Sea Creatures]] spawn with {0} of their maximum health missing.',
				[2] = 'Gain {1}STAT_MF against Sea Creatures.',
				[3] = 'During rain, increases this pet\'s base stats and stats granted by perks by {2}.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip 
				[1] = '&bSea Creatures &7spawn with &a{0}% &7of/&7their maximum health missing.',
				[2] = '&7Gain &b+{1}✯ Magic Find &7against &bSea/&bCreatures.',
				[3] = '&7During &9rain&7, increases this pet\'s/&7base stats and stats granted by/&7perks by &a{2}%&7.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell
				[1] = '+{0} health missing per level',
				[2] = '+{1} STAT_MF per level',
				[3] = '+{2} base stat increase per level',
			},
		},
		variables = {
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.15,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.08,
					color = 'Aqua',
				},
				[2] = {
					per_lvl = 0.75,
					color = 'Green',
					suffix = '%%',
				},
			},
		},
	},
	['Spirit'] = {
		id = 'SPIRIT',
		rarities = { 'E', 'L' },
		petType = 'Combat Pet',
		isPassive = true,
		stats = {
			spd = {0.3},
			int = {1},
		},
		abilities = {
			name = {
				[1] = 'Spirit Assistance',
				[2] = 'Spirit Cooldowns',
				[3] = 'Half Life',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Spawns and assists you when you are a ghost in dungeons.',
				[2] = 'Reduces the cooldown of your ghost abilities in dungeons by {0}.',
				[3] = 'If you are the first player to die in a dungeon, the score penalty for that death is reduced to <GREEN>1</GREEN>.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Spawns and assists you when/&7you are a ghost in Dungeons.',
				[2] = '&7Reduces the cooldown of your/&7ghost abilities in dungeons by/&7&a{0}%&7.',
				[3] = '&7If you are the first player to/&7die in a dungeon, the score/&7penalty for that death is/&7reduced to &a1&7.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = nil,
				[2] = '+{0} higher cooldown reduction per level',
				[3] = nil,
			},
		},
		variables = {
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.45,
					base = 5,
					color = 'Green',
					suffix = '%%',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.45,
					base = 5,
					color = 'Green',
					suffix = '%%',
				},
			},
		},
	},
	['Squid'] = {
		id = 'SQUID',
		rarities = { 'C', 'U', 'R', 'E', 'L' },
		petType = 'Fishing Pet',
		stats = {
			hp = {0.5},
			int = {0.5},
		},
		abilities = {
			name = {
				[1] = 'More Ink',
				[2] = 'Ink Specialty',
				[3] = 'Fishing Wisdom Boost',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Gain a {0} chance to get double drops from squids.',
				[2] = 'Buffs the [[Ink Wand]] by {1} STAT_DMG and {2} STAT_STR.',
				[3] = 'Grants <DARK_AQUA>+</DARK_AQUA>{3} STAT_FSW.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Gain a &a{0}% &7chance to get/&7double drops from squids.',
				[2] = '&7Buffs the &5Ink Wand &7by &a{1} &c❁/&cDamage &7and &a{2} &c❁ Strength.',
				[3] = '&7Gives &3+{3}☯ Fishing/&3Wisdom&7.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} higher chance per level',
				[2] = '+{1} more STAT_DMG per level; +{2} more STAT_STR per level',
				[3] = '+{3} more STAT_FSW per level',
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.5,
					color = 'Green',
					suffix = '%%',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.75,
					color = 'Green',
					suffix = '%%',
				},
			},
			rare = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.75,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.3,
					color = 'Green',
				},
				[2] = {
					per_lvl = 0.1,
					color = 'Green',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 1,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.4,
					color = 'Green',
				},
				[2] = {
					per_lvl = 0.2,
					color = 'Green',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 1,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.4,
					color = 'Green',
				},
				[2] = {
					per_lvl = 0.2,
					color = 'Green',
				},
				[3] = {
					per_lvl = 0.3,
					color = 'Dark_Aqua',
				},
			},
		},
	},
	['T-Rex'] = {
		id = 'TYRANNOSAURUS',
		rarities = { 'L' },   
		petType = 'Combat Pet',
		stats = {
			str = {0.75},
			cc = {0.05},
			fer = {0.25},
		},	
		abilities = {
			name = {
				[1] = 'Close Combat',
				[2] = 'Ferocious Roar',
				[3] = 'Tyrant',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Deal {0} more damage to enemies within 1.5 blocks.',
				[2] = 'Attacks have a {1} chance to stun the target (10s cooldown).',
				[3] = 'Combat stats granted by pet items on this pet are increased by {2}.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip 
				[1] = '&7Deal &a{0}% &7more &cdamage &7to enemies/&7within 1.5 blocks.',
				[2] = '&7Attacks have a &a{1}% &7chance to stun/&7the target &8(10s cooldown).',
				[3] = '&7Combat stats granted by pet items on/&7this pet are increased by &a{2}%&7.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell
				[1] = '+{0} damage per level',
				[2] = '+{1} chance to stun per level',
				[3] = '+{2} combat stats from pet items per level',
			},
		},
		variables = {
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 1,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
				[2] = {
					per_lvl = 1,
					color = 'Green',
					suffix = '%%',
				},
			},
		},
	},
	['Tarantula'] = {
		id = 'TARANTULA',
		rarities = { 'E', 'L', 'M' },
		petType = 'Combat Pet',
		stats = {
			str = {0.1},
			cc = {0.1},
			cd = {0.3},
		},
		abilities = {
			name = {
				[1] = 'Webbed Cells',
				[2] = 'Eight Legs',
				[3] = 'Arachnid Slayer',
				[4] = 'Web Battlefield',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Anti-healing is {0} less effective against you.',
				[2] = 'Decreases the STAT_MC of [[Spider Boots|Spider]], [[Tarantula Boots|Tarantula]] and [[Spirit Boots|Spirit]] boots by {1}.',
				[3] = 'Gain {2} Combat XP against <GREEN>Spiders</GREEN>.',
				[4] = 'Killing mobs grants {3} STAT_STR and {4} STAT_MF for <GREEN>40s</GREEN> to all players staying within <GREEN>20</GREEN> blocks of where they died. <DARK_GRAY>Stacks up to 10 times.</DARK_GRAY>',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Anti-healing is &a{0}% &7less/&7effective against you.',
				[2] = '&7Decreases the mana cost of/&7Spider, Tarantula and Spirit/&7boots by &a{1}%',
				[3] = '&7Gain &b{2}x &7Combat XP/&7against &aSpiders&7.',
				[4] = '&7Killing mobs grants &c+{3}❁/&cStrength &7and &b+{4} Magic Find/&7for &a40s &7to all players/&7staying within &a20 &7blocks/&7of where they died. &8Stacks/&8up to 10 times.'
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} less effective anti-healing per level',
				[2] = '{1} less STAT_MC per level',
				[3] = '+{2} more Combat XP per level',
				[4] = '+{3} STAT_STR and +{4} STAT_MF per level',
			},
		},
		variables = {
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.3,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.5,
					color = 'Green',
					suffix = '%%',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.3,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.5,
					color = 'Green',
					suffix = '%%',
				},
				[2] = {
					base = 1.0,
					per_lvl = 0.005,
					color = 'Aqua',
					suffix = 'x',
				},
			},
			mythic = {
				ability_count = 4,
				[0] = {
					per_lvl = 0.3,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.5,
					color = 'Green',
					suffix = '%%',
				},
				[2] = {
					base = 1.0,
					per_lvl = 0.005,
					color = 'Aqua',
					suffix = 'x',
				},
				[3] = {
					base = 0,
					per_lvl = 0.06,
					color = 'Red',
				},
				[4] = {
					base = 0,
					per_lvl = 0.01,
					color = 'Aqua',
				},
			},
		},
	},
	['Tiger'] = {
		id = 'TIGER',
		rarities = { 'C', 'U', 'R', 'E', 'L' },
		petType = 'Combat Pet',
		stats = {
			str = {0.1, 5},
			cc = {0.05},
			cd = {0.5},
			fer = {0.25},
		},
		abilities = {
			name = {
				[1] = 'Merciless Swipe',
				[2] = 'Hemorrhage',
				[3] = 'Apex Predator',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Gain <RED>+</RED>{0} STAT_FER.',
				[2] = 'Melee attacks reduce healing by {1} for <GREEN>10</GREEN> seconds.',
				[3] = 'Deal +{2} damage against targets with no other mobs within 15 blocks.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Gain &c+{0}% &c⫽ Ferocity.',
				[2] = '&7Melee attacks reduce healing/&7by &6{1}% &7for &a10s.',
				[3] = '&7Deal &c+{2}% &7damage against/&7targets with no other mobs/&7within &a15 &7blocks.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} more STAT_FER per level',
				[2] = '+{1} higher healing reduction per level',
				[3] = '+{2} more damage per level',
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.1,
					color = 'Red',
					suffix = '%%',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.2,
					color = 'Red',
					suffix = '%%',
				},
			},
			rare = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.2,
					color = 'Red',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.3,
					color = 'Gold',
					suffix = '%%',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.3,
					color = 'Red',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.55,
					color = 'Gold',
					suffix = '%%',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.3,
					color = 'Red',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.55,
					color = 'Gold',
					suffix = '%%',
				},
				[2] = {
					per_lvl = 1,
					color = 'Red',
					suffix = '%%',
				},
			},
		},
	},
	['Turtle'] = {
		id = 'TURTLE',
		rarities = { 'E', 'L' },
		petType = 'Combat Pet',
		stats = {
			hp = {0.5},
			def = {1},
			tdef = {0.15},
		},
		abilities = {
			name = {
				[1] = 'Turtle Tactics',
				[2] = 'Genius Amniote',
				[3] = 'Unflippable',
				[4] = 'Turtle Shell',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Gain +{0} STAT_DEF and an additional <GREEN>+10%</GREEN> STAT_DEF when standing still.',
				[2] = 'Grants +{1} STAT_DEF to 4 players within 50 blocks of you.',
				[3] = 'Gain <GREEN>immunity</GREEN> to knockback.',
				[4] = 'When under <RED>40%</RED> maximum HP, you take {2} less damage. Gain +{3} STAT_VIT for 15 seconds after taking 10 hits.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Gain &a+{0}% ❈ Defense &7and an/&7additional &a+10% &a❈ Defense &7when/&7standing still.',
				[2] = '&7Grants &a+{1}% ❈ Defense &7to 4/&7players within 50 blocks of you.',
				[3] = '&7Gain &aimmunity &7to knockback.',
				[4] = '&7When under &c40% &7maximum HP, you take/&a{2}% &7less damage. Gain &4+{3} ♨/&4Vitality &7for 15 seconds after taking/&710 hits.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} more STAT_DEF per level',
				[2] = '+{1} more STAT_DEF per level',
				[3] = nil,
				[4] = '+{2} less damage taken while below <RED>40%</RED> maximum HP taken per level and +{3} more STAT_VIT per level',
			},
		},
		variables = {
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.27,
					base = 3,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.015,
					base = 1,
					color = 'Green',
					suffix = '%%',
				},
			},
			legendary = {
				ability_count = 4,
				[0] = {
					per_lvl = 0.27,
					base = 3,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.015,
					base = 1,
					color = 'Green',
					suffix = '%%',
				},
				[2] = {
					per_lvl = 0.25,
					color = 'Green',
					suffix = '%%',
				},
				[3] = {
					base = 10,
					per_lvl = 0.1,
					color = 'Dark Red',
					suffix = '%%',
				},
			},
		},
	},
	['Wisp'] = {
			id = 'DROPLET_WISP,FROST_WISP,GLACIAL_WISP,SUBZERO_WISP', -- TODO: Change to table once we figure out why it doesn't work
			rarities = { 'U', 'R', 'E', 'L' },
			petType = 'Gabagool Pet, feed to gain XP',
			stats = {
				hp = {1},
				dmg = {0.1},
				tdef = {0.1},
				int = {0.5},
			},
			abilities = {
				name = {
					[1] = 'Drophammer',
					[2] = 'Bulwark',
					[3] = 'Blaze Slayer',
					[4] = 'Extinguish',
					[5] = 'Ephemeral Stability',
					[6] = 'Icehammer',
				},
				desc = {
					-- the description of abilities used in the two top cells
					[1] = 'Lets you break fire pillars.',
					[2] = 'Kill Blazes to gain defense against them and demons.\nBonus: <GREEN>+0❈</GREEN> & <WHITE>+0❂</WHITE> Next Upgrade: <GREEN>+30❈</GREEN> & <WHITE>+3❂</WHITE> <DARK_GRAY>(</DARK_GRAY><GREEN>0</GREEN>/<RED>100</RED><DARK_GRAY>)</DARK_GRAY>',
					[3] = 'Grants {0} STAT_CW against <GREEN>Blazes</GREEN>.',
					[4] = 'While in combat on the Crimson Isle, spawn a pool every <GREEN>8s</GREEN>. Bathing in it heals {1}<RED>❤</RED> now and {2}<RED>❤</RED>/s for <GREEN>8s</GREEN>.',
					[5] = 'Regenerate mana {3} faster.',
					[6] = 'Lets you break fire pillars.',
				},
				tooltip = {
					-- the description of abilities used in the tooltip
					[1] = '&7Lets you break fire pillars.',
					[2] = '&7Kill Blazes to gain defense/&7against them and demons./&7Bonus: &a+0❈ & &f+0❂/&7Next Upgrade: &a+30❈ & &f+3❂ &8(&a0&7\\/&c100&8)',
					[3] = '&7Grants &a{0}% &3☯ Combat/&3Wisdom &7against &aBlazes&7.',
					[4] = '&7While in combat on the Crimson/&7Isle, spawn a pool every &a8s&7./&7Bathing in it heals &c{1}%❤ &7now/&7and &c{2}%❤&7\\/s for &a8s&7.',
					[5] = '&7Regenerate mana &b{3}%/&7faster.',
					[6] = '&7Lets you break fire pillars.',
				},
				bonus_desc = {
					-- the description of abilities used in the bottom cell.
					[1] = nil,
					[2] = nil,
					[3] = '+{0} STAT_CW per level',
					[4] = 'Heals +{1} STAT_HP now and +{2} STAT_HP/s for 8s per level',
					[5] = '+{3} faster per level',
					[6] = nil,
				},
			},
		variables = {
			uncommon = {
				stats = {
					hp = {1},
					dmg = {0.1},
				},
				petname = 'Droplet Wisp',
				ability_count = 3,
				[0] = {
					per_lvl = 0.3,
					color = 'Dark_Aqua',
					suffix = '%%',
				},
			},
			rare = {
				stats = {
					hp = {2.5},
					dmg = {0.15},
					tdef = {0.15},
					int = {0.5},
				},
				petname = 'Frost Wisp',
				ability_indices = {6, 2, 3, 4},
				[0] = {
					per_lvl = 0.4,
					color = 'Dark_Aqua',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.15,
					color = 'Red',
					suffix = '%%',
				},
				[2] = {
					per_lvl = 0.04,
					color = 'Red',
					suffix = '%%',
				},
			},
			epic = {
				stats = {
					hp = {4},
					dmg = {0.2},
					tdef = {0.3},
					int = {1.25},
				},
				petname = 'Glacial Wisp',
				ability_indices = {6, 2, 3, 4},
				[0] = {
					per_lvl = 0.45,
					color = 'Dark_Aqua',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.2,
					color = 'Red',
					suffix = '%%',
				},
				[2] = {
					per_lvl = 0.07,
					color = 'Red',
					suffix = '%%',
				},
			},
			legendary = {
				stats = {
					hp = {6},
					dmg = {0.25},
					tdef = {0.35},
					int = {2.5},
				},
				petname = 'Subzero Wisp',
				ability_indices = {6, 2, 3, 4, 5},
				[0] = {
					per_lvl = 0.5,
					color = 'Dark_Aqua',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.25,
					color = 'Red',
					suffix = '%%',
				},
				[2] = {
					per_lvl = 0.1,
					color = 'Red',
					suffix = '%%',
				},
				[3] = {
					per_lvl = 0.4,
					color = 'Aqua',
					suffix = '%%',
				},
			},
		},
	},

	['Witch'] = {
		id = 'WITCH',
		rarities = { 'C', 'U', 'R', 'E', 'L' },
		petType = 'Alchemy Pet',
		stats = {
			int = {1},
			aw = {0.05},
		},
		abilities = {
			name = {
				[1] = 'Toil and Trouble',
				[2] = 'Alchemism',
				[3] = 'Witching Hour',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Increases your chance of dropping {{Gold|Ingredients}} during the {{Purple|Year of the Witch}} by {0}.',
				[2] = 'Reduces how long {{Purple|Potions}} take to brew by {1}.',
				[3] = 'Increases the base stats of this pet by {2} during the {{Purple|Year of the Witch}}.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Increases your chance of dropping/&6Ingredients &7during the &5Year of the/&5Witch by &a{0}%&7.',
				[2] = '&7Reduces how long &5Potions &7take to/&7brew by &a{1}%&7.',
				[3] = '&7Increases the base stats of this pet/&7by &a1% &7during the &5Year of the Witch&7.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '{0} more chance per level',
				[2] = '{1} more reduction per level',
				[3] = '{2} more increase per level',
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.5,
					color = 'Green',
					suffix = '%%',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.75,
					color = 'Green',
					suffix = '%%',
				},
			},
			rare = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.75,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.4,
					color = 'Green',
					suffix = '%%',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 1,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.5,
					color = 'Green',
					suffix = '%%',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 1,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.5,
					color = 'Green',
					suffix = '%%',
				},
				[2] = {
					per_lvl = 1,
					color = 'Green',
					suffix = '%%',
				}
			},
		},
	},

	['Wither Skeleton'] = {
		id = 'WITHER_SKELETON',
		rarities = { 'C', 'U', 'R', 'E', 'L' },
		petType = 'Mining Pet',
		stats = {
			str = {0.25},
			cd = {0.25},
			def = {0.25},
			int = {0.25},
			cc = {0.05},
		},
		abilities = {
			name = {
				[1] = 'Stronger Bones',
				[2] = 'Wither Blood',
				[3] = 'Death\'s Touch',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Take {0} less damage from {{mt|Skeletal}} mobs.',
				[2] = 'Deal {1} more damage against {{mt|Wither}} mobs.',
				[3] = 'Upon hitting an enemy inflict the wither effect for {2} damage over 3 seconds. <DARK_GRAY>Does not stack</DARK_GRAY>',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Take &a{0}% &7less damage from &f🦴/&fSkeletal &7mobs.',
				[2] = '&7Deal &a{1}% &7more damage to &8☠ Wither/&7mobs.',
				[3] = '&7Upon hitting an enemy inflict/&7the wither effect for &a{2}%/&7damage over 3 seconds./&8Does not stack',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '{0} less damage per level',
				[2] = '+{1} more damage per level',
				[3] = '+{2} more damage per level',
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
			},
			rare = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 1,
					color = 'Green',
					suffix = '%%',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.3,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 1,
					color = 'Green',
					suffix = '%%',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.3,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 1,
					color = 'Green',
					suffix = '%%',
				},
				[2] = {
					per_lvl = 2,
					color = 'Green',
					suffix = '%%',
				},
			},
		},
	},
	['Wolf'] = {
		id = 'WOLF',
		rarities = { 'C', 'U', 'R', 'E', 'L' },
		petType = 'Combat Pet',
		stats = {
			hp = {0.5},
			spd = {0.2},
			tdef = {0.1},
			cd = {0.1},
		},
		abilities = {
			name = {
				[1] = 'Alpha Dog',
				[2] = 'Pack Leader',
				[3] = 'Combat Wisdom Boost',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Take {0} less damage from wolves.',
				[2] = 'Gain {1} STAT_CD for every nearby wolf <DARK_GRAY>(max 10 wolves)</DARK_GRAY>.',
				[3] = 'Grants <DARK_AQUA>+</DARK_AQUA>{2}STAT_CW.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Take &a{0}% &7less damage from/&7wolves.',
				[2] = '&7Gain &a{1} &9☠ Crit Damage/&9&7for every nearby wolf monsters./&8Max 10 wolves',
				[3] = '&7Grants &3+{2}☯ Combat/&3Wisdom&7.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} less damage per level',
				[2] = '+{1} more STAT_CD per wolf per level',
				[3] = '+{2} higher STAT_CW boost per level',
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
			},
			rare = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.2,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					per_lvl = 0.3,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.15,
					color = 'Green',
					suffix = '%%',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					per_lvl = 0.3,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					per_lvl = 0.15,
					color = 'Green',
					suffix = '%%',
				},
				[2] = {
					per_lvl = 0.3,
					color = 'Dark_Aqua',
				},
			},
		},
	},
	['Zombie'] = {
		id = 'ZOMBIE',
		rarities = { 'C', 'U', 'R', 'E', 'L' },
		petType = 'Combat Pet',
		stats = {
			hp = {1},
			cd = {0.3},
		},
		abilities = {
			name = {
				[1] = 'Bite Shield',
				[2] = 'Rotten Blade',
				[3] = 'Living Dead',
			},
			desc = {
				-- the description of abilities used in the two top cells
				[1] = 'Reduce the damage taken from zombies by {0}.',
				[2] = 'Deal {1}% more damage to <DARK_GREEN>༕ Undead</DARK_GREEN> mobs',
				[3] = 'Increases stats of all <DARK_GREEN>Undead ༕</DARK_GREEN> armor by {2}.',
			},
			tooltip = {
				-- the description of abilities used in the tooltip
				[1] = '&7Reduce the damage taken from/&7zombies by &a{0}%&7.',
				[2] = '&7Deal &a{1}% &7more damage to &2༕ Undead/&7mobs', -- full stop missing at the end, as of 0.24.3
				[3] = '&7Increases all stats on/&2Undead ༕ &7armor by &a{2}%.',
			},
			bonus_desc = {
				-- the description of abilities used in the bottom cell.
				[1] = '+{0} more damage reduction per level',
				[2] = '+{1} more damage per level',
				[3] = '+{2} higher stats boost per level',
			},
		},
		variables = {
			common = {
				ability_count = 1,
				[0] = {
					base = 5,
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
			},
			uncommon = {
				ability_count = 1,
				[0] = {
					base = 10,
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
			},
			rare = {
				ability_count = 2,
				[0] = {
					base = 10,
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					base = 25,
					per_lvl = 1.25,
					color = 'Green',
					suffix = '%%',
				},
			},
			epic = {
				ability_count = 2,
				[0] = {
					base = 15,
					per_lvl = 0.1,
					color = 'Green',
					suffix = '%%',
				},
				[1] = {
					base = 25,
					per_lvl = 1.25,
					color = 'Green',
					suffix = '%%',
				},
			},
			legendary = {
				ability_count = 3,
				[0] = {
					base = 15,
					per_lvl = 0.1,
					color = 'Green',
				},
				[1] = {
					base = 25,
					per_lvl = 1.25,
					color = 'Green',
					suffix = '%%',
				},
				[2] = {
					per_lvl = 0.25,
					color = 'Green',
					suffix = '%%',
				},
			},
		},
	},
}
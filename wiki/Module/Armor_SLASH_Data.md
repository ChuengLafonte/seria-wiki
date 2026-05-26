--<pre>
--[[Quick Copy
	
	Long
	[''] = {
		
		stats = {
			head = {
				str = ,
				cc  = ,
				cd  = ,
				as  = ,
				int = ,
				spd = ,
				def = ,
				hp  = ,
				scc = ,
				td  = ,
				
				image = '',
				
				specialEffect = '',	  
				pcb_name = '',
				pcb_desc = '',
				pcb2_name = '',
				pcb2_desc = '',
				
				ia = {
					name = '',
					desc = '',
					cost = ,
					cd   = ,
				}
			},
			chest = {
				str = ,
				cc  = ,
				cd  = ,
				as  = ,
				int = ,
				spd = ,
				def = ,
				hp  = ,
				scc = ,
				td  = ,
				
				image = '',
				
				specialEffect = '',
				pcb_name = '',
				pcb_desc = '',
				pcb2_name = '',
				pcb2_desc = '',
				
				ia = {
					name = '',
					desc = '',
					cost = ,
					cd   = ,
				}
			},
			legs = {
				str = ,
				cc  = ,
				cd  = ,
				as  = ,
				int = ,
				spd = ,
				def = ,
				hp  = ,
				scc = ,
				td  = ,
				
				image = '',
				
				specialEffect = '',
				pcb_name = '',
				pcb_desc = '',
				pcb2_name = '',
				pcb2_desc = '',
				
				ia = {
					name = '',
					desc = '',
					cost = ,
					cd   = ,
				}
			},
			boots = {
				str = ,
				cc  = ,
				cd  = ,
				as  = ,
				int = ,
				spd = ,
				def = ,
				hp  = ,
				scc = ,
				td  = ,
				
				image = '',
				
				specialEffect = '',
				pcb_name = '',
				pcb_desc = '',
				pcb2_name = '',
				pcb2_desc = '',
				
				ia = {
					name = '',
					desc = '',
					cost = ,
					cd   = ,
				}
			},
		
			total = {
				str = ,
				cc  = ,
				cd  = ,
				as  = ,
				int = ,
				spd = ,
				def = ,
				hp  = ,
				scc = ,
				
				fsb_name = '',
				fsb_desc = '',
				
				fsb2_name = '',
				fsb2_desc = '',
			},
		},
		merchant = '',
		merchantPrice = '',
		source = '',
		collection = '',
		rarity = '',
		materials = {
			{name='',amount=},
			{name='',amount=},
			{name='',amount=},
			{name='',amount=},
			{name='',amount=},
			{name='',amount=},
			{name='',amount=},
			{name='',amount=},
			{name='',amount=},
		}
	},
	
	Short
	[''] = {
		
		stats = {
			head = {
				int = ,
				spd = ,
				def = ,
				hp  = ,
			},
			chest = {
				int = ,
				spd = ,
				def = ,
				hp  = ,
			},
			legs = {
				int = ,
				spd = ,
				def = ,
				hp  = ,
			},
			boots = {
				int = ,
				spd = ,
				def = ,
				hp  = ,
			},
		
			total = {
				int = ,
				spd = ,
				def = ,
				hp  = ,
				
				fsb_name = '',
				fsb_desc = '',
			},
		},
		source = '',
		collection = '',
		rarity = '',
		materials = {{name='',amount=},{name='',amount=},{name='',amount=}}
	},
--]]
return {
	['farm suit'] = {
		
		stats = {
			head = {
				def = 15,
			},
			chest = {
				def = 40,
			},
			legs = {
				def = 35,
			},
			boots = {
				def = 15,
			},
		
			total = {
				def = 100,
				
				fsb_name = 'Bonus Speed',
				fsb_desc = 'Increases your {{Statname|speed}} by {{Green|+20%}} while worn near Farming [[Minions]] or in the [[Farm]], The [[Barn]], and [[Mushroom Desert]]',
				
				
				fsb2_name = 'Farmer Aura',
				fsb2_desc = 'Increases the regrowth rate of nearby crops on the public islands, regrowing an extra crop every {{G|3}} seconds. {{Gray|<br>(stacks with the [[Farmer Orb]])}}',
				
			},
		},
		source = 'crafting',
		collection = 'Wheat III',
		rarity = 'c',
		materials = {{name='Wheat',amount=216}}
	},

	['mushroom armor'] = {
		
		stats = {
			head = {
				hp  = 20,
			},
			chest = {
				def = 10,
				hp  = 10,
			},
			legs = {
				def = 5,
				hp  = 10,
			},
			boots = {
				hp  = 15,
			},
		
			total = {
				def = 15,
				hp  = 55,
				
				fsb_name = 'Night Affinity',
				fsb_desc = 'Grants the wearer with {{G|permanent}} {{PotN|Night Vision}} while worn, and during the night, the stats of the armor pieces are {{G|tripled}}.',
			},
		},
		source = 'Crafting',
		collection = 'Red Mushroom III',
		rarity = 'c',
		materials = {{name='Red Mushroom',amount=24}}
	},

	['angler armor'] = {
		
		stats = {
			head = {
				def = 15,
			},
			chest = {
				def = 40,
			},
			legs = {
				def = 30,
			},
			boots = {
				def = 15,
			},
		
			total = {
				def = 100,
				
				fsb_name = 'Depth Champion',
				fsb_desc = 'Take {{g|-30%}} {{stat|damage}} from [[Sea Creatures]]. Increase their spawn rate by {{Yellow|4%}}',
				
				fsb2_name = 'Deepness Within',
				fsb2_desc = 'Gain {{Stat|hp|10}} per [[Fishing]] Level',
			},
		},
		source = 'Crafting',
		collection = 'Raw Fish V',
		rarity = 'c',
		materials = {{name='Raw Fish',amount=24},}
	},

	['pumpkin armor'] = {
		
		stats = {
			head = {
				def = 8,
				hp  = 8,
			},
			chest = {
				def = 14,
				hp  = 14,
			},
			legs = {
				def = 10,
				hp  = 10,
			},
			boots = {
				def = 8,
				hp  = 8,
			},
		
			total = {
				def = 40,
				hp  = 40,
				
				fsb_name = 'Pumpkin Buff',
				fsb_desc = 'Grants {{G|+10.0%}} {{Stat|damage}} reduction against all {{Stat|damage}} sources and {{G|+10.0%}} {{Stat|damage}}',
			},
		},
		source = 'Crafting',
		collection = 'Pumpkin II',
		rarity = 'c',
		materials = {{name='Pumpkin',amount=24}}
	},

	['cactus armor'] = {
		
		stats = {
			head = {
				def = 10,
				hp  = 5,
			},
			chest = {
				def = 25,
				hp  = 15,
			},
			legs = {
				def = 20,
				hp  = 10,
			},
			boots = {
				def = 10,
				hp  = 5,
			},
		
			total = {
				def = 60,
				hp  = 35,
				
				fsb_name = 'Deflect',
				fsb_desc = 'Rebound {{G|33.0%}} of the {{Stat|damage}} you take back at your enemy.',
			},
		},
		source = 'Crafting',
		collection = 'Cactus II',
		rarity = 'c',
		materials = {{name='Cactus',amount=24}}
	},

	['leaflet armor'] = {
		
		stats = {
			head = {
				hp  = 20,
				
				label = 'Hat',
			},
			chest = {
				hp  = 35,
				
				label = 'Tunic',
			},
			legs = {
				hp  = 30,
				
				label = 'Pants'
			},
			boots = {
				hp  = 15,
				
				label = 'Sandals'
			},
		
			total = {
				hp  = 100,
				
				fsb_name = 'Energy of the Forest',
				fsb_desc = 'While in a forest zone, you regain {{Green|5.0}} {{Statname|Health}} every second',
			},
		},
		source = 'Crafting',
		collection = 'Oak Wood III',
		rarity = 'c',
		materials = {{name='Oak Leaves',amount=24}}
	},

	['lapis armor'] = {
		
		stats = {
			head = {
				def = 25,
				
				specialEffect = '{{G|+50%}} Bonus Experience when mining ores',
				name = 'Lapis Armor Helmet',
			},
			chest = {
				def = 40,
				
				specialEffect = '{{G|+50%}} Bonus Experience when mining ores',
				name = 'Lapis Armor Chestplate',
			},
			legs = {
				def = 35,
				
				specialEffect = '{{G|+50%}} Bonus Experience when mining ores',
				name = 'Lapis Armor Leggings',
			},
			boots = {
				def = 20,
				
				specialEffect = '{{G|+50%}} Bonus Experience when mining ores',
				name = 'Lapis Armor Boots',
			},
		
			total = {
				def = 120,
				
				fsb_name = 'Health',
				fsb_desc = 'Increases the wearer\'s maximum {{Stat|hp}} by {{G|60}}',
			},
		},
		mobSource = 'Lapis Zombie',
		source = 'Drops|Mob Drop',
		rarity = 'u',
		dropChance = 1,
	},

	['miner\'s outfit'] = {
		
		stats = {
			head = {
				def = 15,
			},
			chest = {
				def = 40,
			},
			legs = {
				def = 30,
			},
			boots = {
				def = 15,
			},
		
			total = {
				def = 100,
				
				fsb_name = '',
				fsb_desc = '',
			},
		},
		source = 'Crafting',
		collection = 'Cobblestone VII',
		rarity = 'u',
		materials = {{name='Cobblestone',amount=3840}}
	},

	['golem armor'] = {
		
		stats = {
			head = {
				def = 45,
				hp  = 45,
				name = 'Golem Armor Helmet',
			},
			chest = {
				def = 90,
				hp  = 65,
				name = 'Golem Armor Chestplate',
			},
			legs = {
				def = 75,
				hp  = 55,
				name = 'Golem Armor Leggings',
			},
			boots = {
				def = 40,
				hp  = 40,
				name = 'Golem Armor Boots',
			},
		
			total = {
				def = 250,
				hp  = 205,
				
				fsb_name = 'Absorption',
				fsb_desc = 'Grants the wearer {{PotionName|Abs III}} for {{Green|20 seconds}} when they kill an enemy.',
			},
		},
		source = 'Crafting',
		collection = 'Iron Ingot',
		rarity = 'r',
		materials = {{name='Iron Ingot',amount=38400}}
	},

	['miner armor'] = {
		
		stats = {
			head = {
				def = {5, '+45 Inside of a Mine'},
				
				specialEffect = 'Each piece of this [[armor]] dramatically increases your {{Statname|def}} bonus when inside of a mine',
			},
			chest = {
				def = {5, '+95 Inside of a Mine'},
				
				specialEffect = 'Each piece of this [[armor]] dramatically increases your {{Statname|def}} bonus when inside of a mine',
			},
			legs = {
				def = {5, '+70 Inside of a Mine'},
				
				specialEffect = 'Each piece of this [[armor]] dramatically increases your {{Statname|def}} bonus when inside of a mine',
			},
			boots = {
				def = {5, '+45 Inside of a Mine'},
				
				specialEffect = 'Each piece of this [[armor]] dramatically increases your {{Statname|def}} bonus when inside of a mine.',
			},
		
			total = {
				def = {20, '+255 Inside of a Mine'},
				
				fsb_name = 'Regeneration',
				fsb_desc = 'Regenerates {{Green|5%}} of your max {{Statname|health}} every second if you have been out of combat for the last {{Green|8}} seconds.',
			},
		},
		mobSource = 'Zombie|Diamond Zombie]], [[Skeleton|Diamond Skeleton',
		source = 'Drops|Mob Drop',
		dropChance = 1,
		rarity = 'r',
	},

	['hardened diamond armor'] = {
		
		stats = {
			head = {
				def = 60,
			},
			chest = {
				def = 120,
			},
			legs = {
				def = 95,
			},
			boots = {
				def = 55,
			},
		
			total = {
				def = 330,
			},
		},
		source = 'Crafting',
		collection = 'Diamond VII',
		rarity = 'r',
		materials = {{name='Diamond',amount=3840}}
	},

	['fairy armor'] = {
		
		stats = {
			head = {
				def = 1,
				hp  = 1,
				spd = 10,
				int = -1,
				
				label = 'Fedora',
				image = 'Fairy\'s Fedora.gif',
			},
			chest = {
				def = 1,
				hp  = 1,
				spd = 10,
				int = -1,
				
				label = 'Polo',
				image = 'Fairy\'s Polo.gif',
			},
			legs = {
				def = 1,
				hp  = 1,
				spd = 10,
				int = -1,
				
				label = 'Trousers',
				image = 'Fairy\'s Trousers.gif',
			},
			boots = {
				def = 1,
				hp  = 1,
				spd = 10,
				int = -1,
				
				label = 'Galoshes',
				image = 'Fairy\'s Galoshes.gif',
			},
		
			total = {
				def = 4,
				hp  = 4,
				spd = 40,
				int = -4,
				
				fsb_name = 'Fairy\'s Outfit',
				fsb_desc = 'Increases {{Statname|speed}} by {{Green|+10%}}. Gain {{Stat|hp|1}} per [[Fairy Soul]] found.<br><br>Also alerts the player if they are near a fairy soul they havent discovered yet.<ref>[[Changelog/2019/December 18]]</ref>',
			},
		},
		mobSource = 'Sea Witch',
		source = 'Fishing|Fishing (Sea Witch drop)',
		rarity = 'r',
	},

	['farm armor'] = {
		
		stats = {
			head = {
				def = 40,
				hp  = 20,
				
				name = 'Farm Armor Helmet',
			},
			chest = {
				def = 75,
				hp  = 20,
				
				name = 'Farm Armor Chestplate',
			},
			legs = {
				def = 50,
				hp  = 20,
				
				name = 'Farm Armor Leggings',
			},
			boots = {
				def = 35,
				hp  = 20,
				
				name = 'Farm Armor Boots',
			},
		
			total = {
				def = 200,
				hp  = 80,
				
				fsb_name = 'Bonus Speed',
				fsb_desc = 'Increases your {{Stat|speed}} by {{G|+25%}} while worn near [[Minions|Farming Minions]] or in the [[Farm]], [[The Barn]], and [[ Mushroom Desert]].',
			},
		},
		source = 'Crafting',
		collection = 'Wheat IX',
		rarity = 'r',
		materials = {{name='Wheat',amount=31104},}
	},

	['armor of growth'] = {
		
		stats = {
			head = {
				def = 30,
				hp  = {50, '+150 With Max Kills'},
				
				name = 'Helmet of Growth',
				ia = {
					name = 'Growth',
					desc = 'Heals the wearer for {{Green|1.0%}} {{Statname|health}} after killing a [[mobs|monster]]. It also increases max {{Statname|health}} bonus for each piece of [[armor]] by {{Green|1}}<br>{{DG|(Maximum bonus of 100)}}.',
					cd = 4,
				}
			},
			chest = {
				def = 50,
				hp  = {100, '+200 With Max Kills'},
				
				name = 'Chestplate of Growth',
				ia = {
					name = 'Growth',
					desc = 'Heals the wearer for {{Green|1.0%}} {{Statname|health}} after killing a [[mobs|monster]]. It also increases max {{Statname|health}} bonus for each piece of [[armor]] by {{Green|1}}<br>{{DG|(Maximum bonus of 100)}}.',
					cd = 4,
				}
			},
			legs = {
				def = 40,
				hp  = {80, '+180 With Max Kills'},
				
				name = 'Leggings of Growth',
				ia = {
					name = 'Growth',
					desc = 'Heals the wearer for {{Green|1.0%}} {{Statname|health}} after killing a [[mobs|monster]]. It also increases max {{Statname|health}} bonus for each piece of [[armor]] by {{Green|1}}<br>{{DG|(Maximum bonus of 100)}}.',
					cd = 4,
				}
			},
			boots = {
				def = 25,
				hp  = {50, '+150 With Max Kills'},
				
				name = 'Boots of Growth',
				ia = {
					name = 'Growth',
					desc = 'Heals the wearer for {{Green|1.0%}} {{Statname|health}} after killing a [[mobs|monster]]. It also increases max {{Statname|health}} bonus for each piece of [[armor]] by {{Green|1}}<br>{{DG|(Maximum bonus of 100)}}.',
					cd = 4,
				}
			},
		
			total = {
				def = 145,
				hp  = {280, '+680 With Max Kills'},
			},
		},
		source = 'Crafting',
		collection = 'Dark Oak IX',
		rarity = 'r',
		materials = {{name='Dark Oak Wood',amount=245760},}
	},

	['monster hunter armor'] = {
		
		stats = {
			head = {
				def = 75,
				
				name = 'Skeleton\'s Helmet',
				image = 'Skeleton\'s Helmet.png',
				specialEffect = '{{Ia|Bone Shield}}<br>A [[Bone]] Shield will surround you, nullifying {{stat|damage}} you take but consuming a [[bone]] in the process. Bones regenerate every {{G|30}} seconds.',
				labelText = '{{Rc|r|Skeleton\'s Helmet}}',
				collection = 'Bone VIII',
			},
			chest = {
				def = 50,
				hp  = 20,
				
				name = 'Guardian Chestplate',
				image = 'Guardian Chestplate.png',
				specialEffect = '{{ia|Block Damage}}<br>If you are at full {{stat|hp}}, the first hit from any mob wil deal no {{Stat|damage}}.<br>{{Cd|60}}',
				labelText = '{{Rc|r|Guardian Chestplate}}',
				collection = 'Prismarine Crystals V',
			},
			legs = {
				def = 65,
				hp  = 200,
				
				name = 'Creeper Pants',
				image = 'Creeper Pants.png',
				specialEffect = '{{Ia|Detonate}}<br>Causes an explosion when dropping below {{G|20.0%}} {{stat|HP}}, damaging and knocking back all monsters around you.<br>{{cd|60}}',
				labelText = '{{Rc|r|Creeper Pants}}',
				collection = 'Gunpowder VIII',
			},
			boots = {
				def = 45,
				int = 50,
				spd = 5,
				
				name = 'Spider\'s Boots',
				image = 'Spider\'s Boots.png',
				specialEffect = '{{Ia|Double Jump}}<br>Allows you to double jump!<br>{{mc|50}}',
				labelText = '{{Rc|r|Spider\'s Boots}}',
				collection = 'String VIII',
			},
		
			total = {
				def = 235,
				hp  = 220,
				spd = 5,
				int = 50,
				
				secretFsbName = 'Monster Hunter',
				secretFsbDesc = 'Take {{G|-25%}} {{stat|damage}} when being attacked by Monsters, and deal {{G|+25%}} {{Stat|damage}} when attacking Monsters.',
			},
		},
		rarity = 'r',
		totalLabel = '{{Rc|r|Monster Hunter Armor}}',
		source = 'Crafting',
		materials = {
			{name='Bone',amount=51200},
			{name='Prismarine Crystals',amount=256},
			{name='Prismarine Shard',amount=256},
			{name='Gunpowder',amount=35840},
			{name='String',amount=49152}
			
		}
	},

	['monster raider armor'] = {
		
		stats = {
			head = {
				def = 75,
				
				name = 'Skeleton\'s Helmet',
				image = 'Skeleton\'s Helmet.png',
				specialEffect = '{{Ia|Bone Shield}}<br>A [[Bone]] Shield will surround you, nullifying {{stat|damage}} you take but consuming a [[bone]] in the process. Bones regenerate every {{G|30}} seconds.',
				labelText = '{{Rc|r|Skeleton\'s Helmet}}',
				collection = 'Bone VIII',
			},
			chest = {
				def = 50,
				hp  = 20,
				
				name = 'Guardian Chestplate',
				image = 'Guardian Chestplate.png',
				specialEffect = '{{ia|Block Damage}}<br>If you are at full {{stat|hp}}, the first hit from any mob wil deal no {{Stat|damage}}.<br>{{Cd|60}}',
				labelText = '{{Rc|r|Guardian Chestplate}}',
				collection = 'Prismarine Crystals V',
			},
			legs = {
				def = 65,
				hp  = 200,
				
				name = 'Creeper Pants',
				image = 'Creeper Pants.png',
				specialEffect = '{{Ia|Detonate}}<br>Causes an explosion when dropping below {{G|20.0%}} {{stat|HP}}, damaging and knocking back all monsters around you.<br>{{cd|60}}',
				labelText = '{{Rc|r|Creeper Pants}}',
				collection = 'Gunpowder VIII',
			},
			boots = {
				def = 100,
				hp  = 70,
				int = 50,
				spd = 5,
				
				name = 'Tarantula Boots',
				image = 'Tarantula Boots.png',
				specialEffect = '{{Ia|Double Jump}}<br>Allows you to double jump!<br>{{mc|40}}',
				labelText = '{{Rc|e|Tarantula\'s Boots}}',
				collection = 'Spider Slayer IV',
			},
		
			total = {
				def = 290,
				hp  = 290,
				int = 50,
				spd = 5,
				
				secretFsbName = 'Monster Raider',
				secretFsbDesc = 'Take {{G|-35%}} {{stat|damage}} when being attacked by Monsters, and deal {{G|+35%}} {{Stat|damage}} when attacking Monsters.',
			},
		},
		source = 'Crafting',
		customRarity = '{{R|r}}-{{R|e}}',
		totalLabel = '{{Rc|r|Monster Hunter Armor}}',
		materials = {
			{name='Bone',amount=51200},
			{name='Prismarine Crystals',amount=256},
			{name='Prismarine Shard',amount=256},
			{name='Gunpowder',amount=35840},
			{name='String',amount=49152},
			{name='Iron Ingot',amount=30720},
			{name='Flint',amount=32*160*4},
			{name='Tarantula Web',amount=128*4},
			{name='Spider Catalyst',amount=1,cost=250000},
			
		}
	},

	['perfect armor'] = {
		
		stats = {
			head = {
				def = 110,
			},
			chest = {
				def = 160,
			},
			legs = {
				def = 140,
			},
			boots = {
				def = 90,
			},
		
			total = {
				def = 500,
			},
		},
		source = 'Crafting',
		collection = 'Diamond IX',
		rarity = 'r',
		materials = {{name='Diamond',amount=614400}}
	},

	['armor of the pack'] = {
		
		stats = {
			head = {
				def = {80, '+130 against animals'},
				hp  = 145,
				td = {0, '+5 against animals'},
				
				name = 'Helmet of the Pack',
			},
			chest = {
				def = {110, '+185 against animals'},
				hp  = 175,
				td = {0, '+5 against animals'},
				
				name = 'Chestplate of the Pack',
			},
			legs = {
				def = {70, '+120 against animals'},
				hp  = 150,
				td = {0, '+5 against animals'},
				
				name = 'Leggings of the Pack',
			},
			boots = {
				def = {60, '+110 against animals'},
				hp  = 125,
				td = {0, '+5 against animals'},
				
				name = 'Boots of the Pack',
			},
		
			total = {
				def = {320, '+545 against animals'},
				hp  = 595,
				td = {0, '+20 against animals'},
				
				fsb_name = 'Armor of the Pack',
				fsb_desc = 'Gain {{stat|str|+35}} and {{stat|def|+80}} for each Armor of the Pack wearers within {{G|30}} blocks. Max of {{G|3}} players',
			},
		},
		source = 'Crafting',
		collection = 'Wolf Slayer VI',
		rarity = 'e',
		materials = {{name='Gold Ingot',amount=51200},{name='Mutton',amount=81920},{name='Wolf Tooth',amount=1280}}
	},

	['armor of magma'] = {
		
		stats = {
			head = {
				def = 50,
				hp  = 15,
			},
			chest = {
				def = 30,
				hp  = 100,
			},
			legs = {
				def = 25,
				hp  = 75,
			},
			boots = {
				def = 15,
				hp  = 45,
			},
		
			total = {
				int = {0, 'Max +200'},
				def = 85,
				hp  = {270, 'Max +470'},
				
				fsb_name = 'Absorb',
				fsb_desc = 'Every {{G|10}} [[Magma Cube|Magma Cubes]] killed gives the wearer {{stat|Health|+1}} and {{Stat|Intelligence|+1}} while wearing the set. Max {{G|200}} each.',
			},
		},
		source = 'Crafting',
		collection = 'Magma Cream VII',
		rarity = 'e',
		materials = {{name='Magma Cream',amount=46080}}
	},

	['emerald armor'] = {
		
		stats = {
			head = {
				def = 50,
			},
			chest = {
				def = 100,
			},
			legs = {
				def = 75,
			},
			boots = {
				def = 45,
			},
		
			total = {
				def = {270, 'Max +620'},
				hp  = {0, 'Max +350'},
				
				fsb_name = 'Tank',
				fsb_desc = 'Increases the wearers maximum {{Stat|Health}} and {{Stat|Defense}} by {{G|+1}} for every {{G|3,000}} [[Emeralds]] in your collection.<br>{{DG|Max +350 each}}',
			},
		},
		source = 'Crafting',
		collection = 'Emerald IX',
		rarity = 'e',
		materials = {{name='Emerald',amount=614400}}
	},

	['ember armor'] = {
		
		stats = {
			head = {
				def = 35,
				hp  = 40,
				int = 5,
			},
			chest = {
				def = 60,
				hp  = 65,
				int = 10,
			},
			legs = {
				def = 55,
				hp  = 60,
				int = 5,
			},
			boots = {
				def = 30,
				hp  = 35,
				int = 5,
			},
		
			total = {
				def = 180,
				hp  = 200,
				int = 25,
				
				fsb_name = 'Nether Lord',
				fsb_desc = '[[Obsidian]] will be created below you when walking on [[Lava]]. Also increases the chance of Nether monsters dropping an item by {{G|20%}}. Wearing this full set will also prevent you from taking {{Red|Lava}} and {{red|Fire Damage}}.',
			},
		},
		source = 'Crafting',
		rarity = 'e',
		materials = {{name='Ember Fragment',amount=24,cost=40000}},
		mobSource = 'Magma Cube Boss'
	},

	['crystal armor'] = {
		
		stats = {
			head = {
				def = {20, 'Max +40 with max light level ({{G|15}})'},
				int = {65, 'Max +130 with max light level ({{G|15}})'},
			},
			chest = {
				def = {35, 'Max +70 with max light level ({{G|15}})'},
				int = {120, 'Max +240 with max light level ({{G|15}})'},
			},
			legs = {
				def = {30, 'Max +60 with max light level ({{G|15}})'},
				int = {100, 'Max +200 with max light level ({{G|15}})'},
			},
			boots = {
				def = {15, 'Max +30 with max light level ({{G|15}})'},
				int = {60, 'Max +120 with max light level ({{G|15}})'},
			},
		
			total = {
				def = {100, 'Max +200 with max light level ({{G|15}})'},
				int = {345, 'Max +690 with max light level ({{G|15}})'},
				
				fsb_name = 'Refraction',
				fsb_desc = 'The stats of this armor change from {{G|0}} to {{G|200%}} depending on the current light level.',
			},
		},
		source = 'Crafting',
		rarity = 'e',  
		materials = {{name='Crystal Fragment',amount=24}}
	},

	['zombie armor'] = {
		
		stats = {

			chest = {
				def = 40,
				hp  = 200,
			},
			legs = {
				def = 30,
				hp  = 160,
			},
			boots = {
				def = 25,
				hp  = 120,
			},
		
			total = {
				def = 100,
				hp  = 480,
				
				fsb_name = 'Projectile Absorption',
				fsb_desc = 'Heals the wearer for {{Stat|HP|10}} per second for {{G|5 seconds}} when hit by a projectile',
			},
		},
		source = 'Crafting',
		collection = 'Rotten Flesh VIII',
		rarity = 'e',
		materials = {{name='Rotten Flesh',amount=370240}}
	},

	['blaze armor'] = {
		
		stats = {
			head = {
				def = 80,
				str = 10,
				spd = 2,
			},
			chest = {
				def = 150,
				str = 10,
				spd = 2,
			},
			legs = {
				def = 110,
				str = 10,
				spd = 2,
			},
			boots = {
				def = 70,
				str = 10,
				spd = 2,
			},
		
			total = {
				def = 410,
				str  = 40,
				spd = 8,
				
				fsb_name = 'Blazing Aura',
				fsb_desc = 'Damages mobs within {{Green|5}} blocks for {{Green|3%}} of their max {{Statname|Health}} per second. Max {{Statname|damage}}{{G|/s}} increased by {{Red|+100 }} per {{orange|5,000}} rods.<br>{{DG|(5000 max damage cap)}}.<br><br>Also grants permanent {{Red|Fire}} and {{Red|Lava}} immunity',
			},
		},
		source = 'Crafting',
		collection = 'Blaze Rod VIII',
		rarity = 'e',
		materials = {{name='Blaze Rod',amount=614400}}
	},

	['frozen blaze armor'] = {
		
		stats = {
			head = {
				def = {110, '+154[[#stats-note|<sup><span style="font: 20px monospace; line-height: 0;">*</span></sup>]]'},
				str = {40, '+56[[#stats-note|<sup><span style="font: 20px monospace; line-height: 0;">*</span></sup>]]'},
				spd = {2, '+2.8[[#stats-note|<sup><span style="font: 20px monospace; line-height: 0;">*</span></sup>]]'},
			},
			chest = {
				def = {180, '+252[[#stats-note|<sup><span style="font: 20px monospace; line-height: 0;">*</span></sup>]]'},
				str = {40, '+56[[#stats-note|<sup><span style="font: 20px monospace; line-height: 0;">*</span></sup>]]'},
				spd = {2, '+2.8[[#stats-note|<sup><span style="font: 20px monospace; line-height: 0;">*</span></sup>]]'},
			},
			legs = {
				def = {140, '+196[[#stats-note|<sup><span style="font: 20px monospace; line-height: 0;">*</span></sup>]]'},
				str = {40, '+56[[#stats-note|<sup><span style="font: 20px monospace; line-height: 0;">*</span></sup>]]'},
				spd = {2, '+2.8[[#stats-note|<sup><span style="font: 20px monospace; line-height: 0;">*</span></sup>]]'},
			},
			boots = {
				def = {100, '+140[[#stats-note|<sup><span style="font: 20px monospace; line-height: 0;">*</span></sup>]]'},
				str = {40, '+56[[#stats-note|<sup><span style="font: 20px monospace; line-height: 0;">*</span></sup>]]'},
				spd = {2, '+2.8 with[[#stats-note|<sup><span style="font: 20px monospace; line-height: 0;">*</span></sup>]]'},
			},
		
			total = {
				def = {510, '+721[[#stats-note|<sup><span style="font: 20px monospace; line-height: 0;">*</span></sup>]]'},
				str = {160, '+224[[#stats-note|<sup><span style="font: 20px monospace; line-height: 0;">*</span></sup>]]'},
				spd = {8, '+11.2[[#stats-note|<sup><span style="font: 20px monospace; line-height: 0;">*</span></sup>]]'},
				
				fsb_name = 'Frozen Blazing Aura',
				fsb_desc = 'Damages mobs within {{Green|5}} block range for {{Green|300}} base {{Statname|damage}} + {{Green|3%}} of their max {{Statname|Health}} every second and applies {{PotN|Slowness 1}} for {{orange|4}} seconds. Max {{Statname|damage}}{{G|/s}} increased by {{red|+100}} per {{orange|5,000}} rods in collection<br>{{DG|(5000 max damage cap at 225,000 rods in collection)}}<br><br>Also grants permanent {{Red|Fire}} and {{Red|Lava}} immunity.',
			},
		},
		source = 'Crafting',
		collection = 'Ice IX',
		rarity = 'l',
		materials = {{name='Ice',amount=6553600},{name='Blaze Rod',amount=614400}}
	},

	['cheap tuxedo'] = {
		
		stats = {
			chest = {
				cd  = 50,
				int = 50,
				
				label = ' Jacket'
			},
			legs = {
				cd  = 25,
				int = 25,
				
				label = ' Pants'
			},
			boots = {
				cd  = 25,
				int = 25,
				
				label = ' Oxfords'
			},
		
			total = {
				cd  = 100,
				int = 100,
				
				fsb_name = 'Dashing!',
				fsb_desc = 'Max health set to {{hp|75}}. Deal {{Red|+50%}} more {{Stat|damage}}!',
			},
		},
		source = 'Merchant',
		rarity = 'e',
		merchant = 'Seymour',
	},

	['ender armor'] = {
		
		stats = {
			head = {
				def = {35, '+70 While on the [[End Island]]'},
				hp  = {20, '+40 While on the [[End Island]]'},
				
				specialEffect = 'All Stats of this [[Armor]] are {{Red|doubled}} while on the [[End Island]]',
			},
			chest = {
				def = {60, '+120 While on the [[End Island]]'},
				hp  = {30, '+60 While on the [[End Island]]'},
				
				specialEffect = 'All Stats of this [[Armor]] are {{Red|doubled}} while on the [[End Island]]',
			},
			legs = {
				def = {50, '+100 While on the [[End Island]]'},
				hp  = {25, '+50 While on the [[End Island]]'},
				
				specialEffect = 'All Stats of this [[Armor]] are {{Red|doubled}} while on the [[End Island]]',
			},
			boots = {
				def = {25, '+50 While on the [[End Island]]'},
				hp  = {15, '+30 While on the [[End Island]]'},
				
				specialEffect = 'All Stats of this [[Armor]] are {{Red|doubled}} while on the [[End Island]]',
			},
		
			total = {
				def = {170, '+340 While on the [[End Island]]'},
				hp  = {90, '+180 While on the [[End Island]]'},
				
			},
		},
		source = 'Mob drop',
		mobSource = 'Enderman',
		rarity = 'e',
	},

	['speedster armor'] = {
		
		stats = {
			head = {
				def = 70,
				spd = 15,
			},
			chest = {
				def = 120,
				spd = 15,
			},
			legs = {
				def = 95,
				spd = 15,
			},
			boots = {
				def = 65,
				spd = 15,
			},
		
			total = {
				def = 350,
				spd = {60, '+80% With {{Full set Bonus}}'},
				
				fsb_name = 'Bonus Speed',
				fsb_desc = 'Increases your {{Stat|Speed}} by {{G|+20}}',
			},
		},
		source = 'Crafting',
		collection = 'Sugar Cane 9',
		rarity = 'e',
		materials = {{name='Sugar Cane',amount=614400}}
	},

	['sponge armor'] = {
		
		stats = {
			head = {
				def = {80, '+160 While in [[water]]'},
				scc = 1.8,
			},
			chest = {
				def = {145, '+290 While in [[water]]'},
				scc = 1.8,
			},
			legs = {
				def = {100, '+200 While in [[water]]'},
				scc = 1.8,
			},
			boots = {
				def = {60, '+120 While in [[water]]'},
				scc = 1.8,
				
				name = 'Spongy Shoes',
				image = 'Sponge Boots.png',
			},
		
			total = {
				def = {385, '+770 While in [[water]]'},
				
				fsb_name = 'Absorb',
				fsb_desc = 'Doubles your {{Stat|def}} while in [[water]].',
			},
		},
		source = 'Crafting',
		collection = 'Sponge 9',
		rarity = 'e',
		materials = {{name='Sponge',amount=38400}}
	},

	['mastiff armor'] = {
		
		stats = {
			head = {
				def = -1e6,
				hp  = 500,
				int = 125,
				
				name = 'Mastiff Crown',
			},
			chest = {
				def = -1e6,
				hp  = 500,
			},
			legs = {
				def = -1e6,
				hp  = 500,
			},
			boots = {
				def = -1e6,
				hp  = 500,
				int = 25,
			},
		
			total = {
				def = -4e6,
				hp  = 2000,
				int = 150,
				
				fsb_name = 'Absolute Unit',
				fsb_desc = '{{Stat|hp|+50}} per {{Statname|crit damage|1%}}. Regain {{G|2%}} of max {{StatS|hp}} when hit {{DG|(1s cooldown)}}. Receive {{Green|-20%}} {{Stat|damage}} from [[Wolf|wolves]]. Your {{Stat|crit damage}} is {{G|50%}} less effective.',
			},
		},
		source = 'Crafting',
		collection = 'Wolf Slayer 4',
		rarity = 'e',
		materials = {
			{name='Dark Oak Wood',amount=245760},
			{name='Diamond',amount=20480},
			{name='Gold Ingot',amount=102400},
			{name='Wolf Tooth',amount=2048},
		}
	},

	['tarantula armor'] = {
		
		stats = {
			head = {
				def = 80,
				hp  = 100,
				int = 100,
				
				pcb_name = 'Radioactive',
				pcb_desc = 'Gain {{Red|+1%}} {{Stat|Cd}} per {{G|10}} {{Stat|Strength}}',
				
				pcb2_name = 'Spider Bulwark',
				pcb2_desc = 'Kill [[Spider]]s to accumulate {{stat|def}} against them.',
				collection = 'Spider Slayer 5',
			},
			chest = {
				def = 100,
				hp  = 120,
				int = 100,
				
				pcb_name = 'Anti-Toxin',
				pcb_desc = 'Gain immunity to healing reduction.',
				
				pcb2_name = 'Spider Bulwark',
				pcb2_desc = 'Kill [[Spider]]s to accumulate {{stat|def}} against them.',
				collection = 'Spider Slayer 5',
			},
			legs = {
				def = 20,
				hp  = 60,
				
				pcb_name = 'Spider Bulwark',
				pcb_desc = 'Kill [[Spider]]s to accumulate {{stat|def}} against them.',
				collection = 'Spider Slayer 4',
			},
			boots = {
				def = 100,
				hp  = 70,
				int = 50,
				spd = 5,
				
				pcb2_name = 'Spider Bulwark',
				pcb2_desc = 'Kill [[Spider]]s to accumulate {{stat|def}} against them.',
				collection = 'Spider Slayer 4',
				
				ia = {
					name = 'Double Jump',
					desc = 'Allows you to double jump!',
					cost = 40,
				}
			},
		
			total = {
				def = 300,
				hp  = 350,
				int = 250,
				spd = 5,
				
				fsb_name = 'Octodexterity',
				fsb_desc = 'Every {{Gold|4th}} strike, deal {{Red|double damage}} and apply {{DarkGreen|Venom}} reducing healing by {{G|40%}} for {{red|4}} seconds.',
			},
		},
		source = 'Crafting',
		rarity = 'e',
		materials = {
			{name='Tarantula Web',amount=1792},
			{name='Flint',amount=71680},
			{name='Iron Ingot',amount=133120},
			{name='String',amount=49152},
			{name='Spider Catalyst',amount=1,cost=250000},
		}
	},

	['revenant armor'] = {
		
		stats = {
			chest = {
				def = 70,
				hp  = 180,
				
				pcb_name = 'Zombie Bulwark',
				pcb_desc = 'Kill [[Zombie]]s to accumulate {{Stat|def}} against them.',
			},
			legs = {
				def = 50,
				hp  = 130,
				
				pcb_name = 'Zombie Bulwark',
				pcb_desc = 'Kill [[Zombie]]s to accumulate {{Stat|def}} against them.',
			},
			boots = {
				def = 30,
				hp  = 100,
				
				pcb_name = 'Zombie Bulwark',
				pcb_desc = 'Kill [[Zombie]]s to accumulate {{Stat|def}} against them.',
			},
		
			total = {
				def = 150,
				hp  = 400,
				
				fsb_name = 'Trolling The Reaper',
				fsb_desc = 'Healing Wands are {{G|+50%}} more effective. Gain {{Stat|def|+100}} against [[Zombie]]s.',
			},
		},
		source = 'Crafting',
		rarity = 'e',
		materials = {
			{name='Diamond',amount=40960},
			{name='Revenant Flesh',amount=1024},
			{name='String',amount=46152},
			{name='Rotten Flesh',amount=164480},
		}
	},

	['spooky armor'] = {
		
		stats = {
			head = {
				def = 25,
			},
			chest = {
				def = 50,
			},
			legs = {
				def = 35,
			},
			boots = {
				def = 25,
			},
		
			total = {
				def = 135,
				
				fsb_name = 'Candy Man',
				fsb_desc = 'Grants a {{G|+5%}} chance to find rare [[candy]]',
			},
		},
		source = 'Merchant',
		merchant = 'Fear Mongerer',
		rarity = 'e',
		materials = {{name='Purple Candy',amount=256}}
	},

	['snow suit'] = {
		
		stats = {
			head = {
				def = 30,
				hp  = 70,
				
				specialEffect = 'Each piece grants {{G|+5%}} {{red|bonus gift}} chance for every present you earn from the [[Gift Attack]] minigame!<br><br>All stats of this armor piece {{Blue|are doubled}} on the [[Winter Island]]!',
			},
			chest = {
				def = 40,
				hp  = 100,
				
				specialEffect = 'Each piece grants {{G|+5%}} {{red|bonus gift}} chance for every present you earn from the [[Gift Attack]] minigame!<br><br>All stats of this armor piece {{Blue|are doubled}} on the [[Winter Island]]!',
			},
			legs = {
				def = 30,
				hp  = 75,
				
				specialEffect = 'Each piece grants {{G|+5%}} {{red|bonus gift}} chance for every present you earn from the [[Gift Attack]] minigame!<br><br>All stats of this armor piece {{Blue|are doubled}} on the [[Winter Island]]!',
			},
			boots = {
				def = 25,
				hp  = 65,
				
				specialEffect = 'Each piece grants {{G|+5%}} {{red|bonus gift}} chance for every present you earn from the [[Gift Attack]] minigame!<br><br>All stats of this armor piece {{Blue|are doubled}} on the [[Winter Island]]!',
			},
		
			total = {
				def = 125,
				hp  = 310,
				
				fsb_name = 'Cold Thumb',
				fsb_desc = ' Allows the wearer to {{Blue|shoot unlimited snowballs}} from [[Frosty the Snow Cannon]]/[[Frosty the Snow Blaster]].',
			},
		},
		source = 'Gifts|Rare Drop from Gifts',
		mobSource = 'Gift',
		dropChance = 1,
		rarity = 'e',
	},

	['bat person armor'] = {
		
		stats = {
			head = {
				def = 15,
				
				specialEffect = 'Each [[armor]] piece grants {{G|x2}} item stats during the night or {{G|x3}} during the [[Spooky Festival]]! Additionally, it gives a {{G|+5%}} chance to get [[Candy]] from [[mob]]s during the [[event]].',
			},
			chest = {
				def = 30,
				
				specialEffect = 'Each [[armor]] piece grants {{G|x2}} item stats during the night or {{G|x3}} during the [[Spooky Festival]]! Additionally, it gives a {{G|+5%}} chance to get [[Candy]] from [[mob]]s during the [[event]].',
			},
			legs = {
				def = 25,
				
				specialEffect = 'Each [[armor]] piece grants {{G|x2}} item stats during the night or {{G|x3}} during the [[Spooky Festival]]! Additionally, it gives a {{G|+5%}} chance to get [[Candy]] from [[mob]]s during the [[event]].',
			},
			boots = {
				def = 15,
				
				specialEffect = 'Each [[armor]] piece grants {{G|x2}} item stats during the night or {{G|x3}} during the [[Spooky Festival]]! Additionally, it gives a {{G|+5%}} chance to get [[Candy]] from [[mob]]s during the [[event]].',
			},
		
			total = {
				def = 85,
				
				fsb_name = 'Bat Powers Activate!',
				fsb_desc = 'Upgrades your [[Grappling Hook]] and turns you into a true vigilante! Grants a {{G|+5%}} chance to find {{R|Rare}} [[Candy]]'..
				'<ul><li><b>Effect:</b><br>Removes the cooldown on the grappling hook, and its velocity is greatly increased</li></ul>.',
			},
		},
		source = 'Merchant',
		merchant = 'Fear Mongerer',
		rarity = 'l',
		materials = {{name='Purple Candy',amount=256},{name='Spooky Shard',amount=24}}
	},

	['diver\'s armor'] = {
		
		stats = {
			head = {
				def = 65,
				hp  = 120,
				scc = 2,
				
				label = 'Mask'
			},
			chest = {
				def = 200,
				hp  = 100,
				scc = 2,
				
				label = 'Shirt'
			},
			legs = {
				def = 170,
				hp  = 75,
				scc = 2,
				
				label = 'Trunks'
			},
			boots = {
				def = 110,
				hp  = 60,
				scc = 2,
			},
		
			total = {
				def = 600,
				hp  = 300,
				scc = 8,
				
				fsb_name = 'One with the Fish',
				fsb_desc = 'While touching the water you move {{blue|incredibly fast}} and can {{blue|breathe permanently (sneak to slow down)}}',
			},
		},
		source = 'Crafting',
		rarity = 'l',
		materials = {{name='Emperor\'s Skull',amount=24,cost=200000}}
	},

	['fancy tuxedo'] = {
		
		stats = {
			chest = {
				cd  = 80,
				int = 150,
				
				label = ' Jacket',
			},
			legs = {
				cd  = 35,
				int = 75,
				
				 label = ' Pants',
			},
			boots = {
				cd  = 35,
				int = 75,
				
				label = ' Oxfords',
			},
		
			total = {
				cd  = 150,
				int = 300,
				
				fsb_name = 'Dashing!',
				fsb_desc = 'Max health set to {{Stat|hp|150}}. Deal {{Red|+100%}} more {{stat|damage}}!',
			},
		},
		source = 'Merchant',
		merchant = 'Seymour',
		merchantPrice = 20000000,
		rarity = 'l',
	},
   
	['elegant tuxedo'] = {
		
		stats = {
			chest = {
				cd  = 100,
				int = 300,
				
				label = ' Jacket',
			},
			legs = {
				cd  = 50,
				int = 100,
				
				label = ' Pants',
			},
			boots = {
				cd  = 50,
				int = 100,
				spd = 10,
				
				label = ' Oxfords',
			},
		
			total = {
				cd  = 200,
				int = 500,
				spd = 10,
				
				fsb_name = 'Dashing!',
				fsb_desc = '',
			},
		},
		source = 'Merchant',
		merchant = 'Seymour',
		merchantPrice = 74999999,
		rarity = 'l',
	},

	['young dragon armor'] = {
		
		stats = {
			head = {
				def = 110,
				hp  = 70,
				spd = 20,
			},
			chest = {
				def = 160,
				hp  = 120,
				spd = 20,
			},
			legs = {
				def = 140,
				hp  = 100,
				spd = 20,
			},
			boots = {
				def = 90,
				hp  = 60,
				spd = 20,
			},
		
			total = {
				def = 500,
				hp  = 350,
				spd = 80,
				
				fsb_name = 'Young Blood',
				fsb_desc = 'Gain {{G|+70}} Walk {{Stat|Speed}} when you are above {{Stat|hp|50%}}.<br>{{DG|+100 Walk Speed Cap}}',
			},
		},
		source = 'Crafting',
		rarity = 'l',
		materials = {{name='Young Dragon Fragment',amount=240}}
	},

	['old dragon armor'] = {
		
		stats = {
			head = {
				def = 90,
				hp  = 110,
			},
			chest = {
				def = 150,
				hp  = 160,
			},
			legs = {
				def = 140,
				hp  = 130,
			},
			boots = {
				def = 90,
				hp  = 80,
			},
		
			total = {
				def = 500,
				hp  = 450,
				
				fsb_name = 'Old Blood',
				fsb_desc = '',
			},
		},
		source = 'Crafting',
		rarity = 'l',
		materials = {{name='Old Dragon Fragment',amount=240}}
	},
	
	['wise dragon armor'] = {
		
		stats = {
			head = {
				def = 110,
				hp  = 70,
				int = 125,
			},
			chest = {
				def = 160,
				hp  = 120,
				int = 75,
			},
			legs = {
				def = 140,
				hp  = 100,
				int = 75,
			},
			boots = {
				def = 90,
				hp  = 60,
				int = 75,
			},
		
			total = {
				def = 500,
				hp  = 350,
				int = 350,
				
				fsb_name = 'Wise Blood',
				fsb_desc = 'All abilities cost {{G|33%}} less {{Stat|mana}}.',
			},
		},
		source = 'Crafting',
		rarity = 'l',
		materials = {{name='Wise Dragon Fragment',amount=240}}
	},

	['protector dragon armor'] = {
		
		stats = {
			head = {
				def = 135,
				hp  = 70,
			},
			chest = {
				def = 185,
				hp  = 120,
			},
			legs = {
				def = 165,
				hp  = 100,
			},
			boots = {
				def = 115,
				hp  = 60,
			},
		
			total = {
				def = 600,
				hp  = 350,
				
				fsb_name = 'Protective Blood',
				fsb_desc = 'Increases the {{Stat|def}} bonus of each armor piece by {{G|1%}} for each percent of missing {{Stat|hp}}.',
			},
		},
		source = 'Crafting',
		rarity = 'l',
		materials = {{name='Protector Dragon Fragment',amount=240}}
	},

	['strong dragon armor'] = {
		
		stats = {
			head = {
				def = 110,
				hp  = 70,
				str = 25,
			},
			chest = {
				def = 160,
				hp  = 120,
				str = 25,
			},
			legs = {
				def = 140,
				hp  = 100,
				str = 25,
			},
			boots = {
				def = 90,
				hp  = 60,
				str = 25,
			},
		
			total = {
				def = 500,
				hp  = 350,
				str = 100,
				
				fsb_name = 'Strong Blood',
				fsb_desc = 'Improves the [[Aspect of the End]]:<div>\n*{{Red|+75 Base}} {{Stat|dmg}}\n*<b>Ability Improved:</b>\n**{{G|+2}} Teleport distance\n**{{G|+3}} seconds of duration\n**{{Stat|str|+5}} on cast</div>',
			},
		},
		source = 'Crafting',
		rarity = 'l',
		materials = {{name='Strong Dragon Fragment',amount=240}}
	},

	['unstable dragon armor'] = {
		
		stats = {
			head = {
				def = 110,
				hp  = 70,
				int = 25,
				cd  = 15,
				cc  = 5,
			},
			chest = {
				def = 160,
				hp  = 120,
				cd  = 15,
				cc  = 5,
			},
			legs = {
				def = 140,
				hp  = 100,
				cd  = 15,
				cc  = 5,
			},
			boots = {
				def = 90,
				hp  = 60,
				cd  = 15,
				cc  = 5,
			},
		
			total = {
				def = 500,
				hp  = 350,
				int = 25,
				cd  = 60,
				cc  = 20,
				
				fsb_name = 'Unstable Blood',
				fsb_desc = 'Every {{G|10}} seconds, strike nearby mobs within a {{G|7}} block radius dealing {{Red|3000}} {{stat|dmg}}!',
			},
		},
		source = 'Crafting',
		rarity = 'l',
		materials = {{name='Unstable Dragon Fragment',amount=240}}
	},

	['superior dragon armor'] = {
		
		stats = {
			head = {
				def = 130,
				hp  = 90,
				spd = 3,
				int = 25,
				str = 10,
				cc  = 2,
				cd  = 8,
			},
			chest = {
				def = 190,
				hp  = 150,
				spd = 3,
				int = 25,
				str = 10,
				cc  = 2,
				cd  = 8,
			},
			legs = {
				def = 170,
				hp  = 130,
				spd = 3,
				int = 25,
				str = 10,
				cc  = 2,
				cd  = 8,
			},
			boots = {
				def = 110,
				hp  = 80,
				spd = 3,
				int = 25,
				str = 10,
				cc  = 2,
				cd  = 8,
			},
		
			total = {
				def = 600,
				hp  = 450,
				spd = 12,
				int = 100,
				str = 40,
				cc  = 8,
				cd  = 40,
				
				fsb_name = 'Superior Blood',
				fsb_desc = 'All your stats are increased by {{G|5%}} and [[Aspect of the Dragons]] ability deals 50% more {{Stat|Ability Damage}}.',
			},
		},
		source = 'Crafting',
		rarity = 'l',
		materials = {{name='Superior Dragon Fragment',amount=240}}
	},

	['holy dragon armor'] = {
		
		stats = {
			head = {
				def = 110,
				hp  = 110,
			},
			chest = {
				def = 160,
				hp  = 180,
			},
			legs = {
				def = 140,
				hp  = 155,
			},
			boots = {
				def = 90,
				hp  = 100,
			},
		
			total = {
				def = 500,
				hp  = 545,
				
				fsb_name = 'Holy Blood',
				fsb_desc = 'Increases the natural {{stat|health}} regeneration of you and all [[player]]s in a {{G|6}} block radius by {{G|3x}}.',
			},
		},
		source = 'Crafting',
		rarity = 'l',
		materials = {{name='Holy Dragon Fragment',amount=240}}
	},
	
	['rotten armor'] = {
		customRarity = '{{Rarity|r}} or {{Rarity|e}}',
		stats = {
					
			head = {
				def = {lower=15, upper=22.5},
			},
			chest = {
				hp = {lower=140, upper=210},
				def = {lower=15, upper=22.5},
			},
			legs = {
				def = {lower=15, upper=22.5},
				hp = {lower=112, upper=168},
			},
			boots = {
				def = {lower=15, upper=22.5},
			},
			total = {
				hp= {lower=252, upper=378},
				def= {lower=60, upper=90},
			
				fsb_name='Sieve Body',
				fsb_desc='Gain additional {{yellow|20%}} knockback resistance to arrows.',
			},
		},
		source = 'Dungeons',
		rarity = 'e',
	},
	
	['heavy armor'] = {
		rarity='e',
		customRarity='{{Rarity|r}} or {{Rarity|e}}',
		stats = {
			
			head = {
				hp= 75,
				def= '+77-125',
				spd= -5,
			},
			chest = {
				hp= 75,
				def= '+127-213',
				spd= -5,
			},
			legs = {
				hp= 75,
				def= '+107-179',
				spd= -5,
			},
			boots = {
				hp= 75,
				def= '+72-116',
				spd= -5,
			},
			
			total = {
				hp=300,
				def='+383-633',
				spd=-20,
		
				fsb_name='Vindicate',
				fsb_desc='Grants {{White|1 walk speed}} for every {{Green|50}} defense that you have.',
			},
		},
		source='dungeons',
	},
 
	['skeleton grunt armor'] = {
		customRarity='{{Rarity|e}} or {{Rarity|l}}',
		stats = {
			head = {
				hp= '+14-25',
				def= '+23-41',
				cd = '+15-27%',
			},
			chest = {
				hp= '+23-42',
				def= '+38-66',
				cd = '+15-27%',
			},
			legs = {
				hp= '+22-40',
				def= '+34-62',
				cd = '+15-27%',
			},
			boots = {
				hp= '+13-21',
				def= '+20-35',
				cd = '+15-27%',
			},
			total = {
				hp='+72-128',
				def='+115-204',
				cd='+60-108',
		
				specialEffect='Increases the {{Stat|damage}} you deal with arrows by {{Red|5%}} per piece.',
			},
		},
		source='dungeons',
		rarity = 'e',
	},
	
	['skeleton soldier armor'] = {
		customRarity='{{Rarity|e}} or {{Rarity|l}}',
		stats = {
			head = {
				hp= '92-107',
				def= '43-65',
				cc = 3,
				cd = '18-30',
			},
			chest = {
				hp= '+102-126',
				def= '58-96',
				cc = 3,
				cd = '18-30',
			},
			legs = {
				hp= '100-122',
				def= '55-90',
				cc = 3,
				cd = '18-30',
			},
			boots = {
				hp= '90-102',
				def= '38-59',
				cc = 3,
				cd = '18-30',
			},
			total = {
				hp='+384-457',
				def='+194-310',
				cc=12,
				cd='72-120',
				
				specialEffect='Increases the damage you deal with arrows by {{Red|5%}} per piece.',
				fsb_name='Skeleton Soldier', 
				fsb_desc='Increase the damage you deal with arrows by {{Red|25%}}.',
			},
		},
		source='dungeons',
		rarity = 'e',
	},
	
	['skeleton master armor'] = {
		customRarity='{{Rarity|e}} or {{Rarity|l}}',
		stats = {
			head = {
				hp= '91-157',
				def= '41-75',
				cc = '22-41',
				cd = '2-3',
			},
			chest = {
				hp= '101-176',
				def= '57-106',
				cc = '22-41',
				cd = '2-3',
			},
			legs = {
				hp= '99-172',
				def= '53-100',
				cc = '22-41',
				cd = '2-3',
			},
			boots = {
				hp= '89-152',
				def= '37-69',
				cc = '22-41',
				cd = '2-3',
			},
			total = {
				hp='380-657',
				def='188-350',
				cc='88-164',
				cd='8-12',
				
				specialEffect='Increases the damage you deal with arrows by {{Red|5%}} per piece<br>{{DG|(Chestplate only)}} Your bows don\'t consume arrows',
				fsb_name='Skeleton Master', 
				fsb_desc='Increase the damage you deal with arrows by {{Red|25%}}',
			},
		},
		source='dungeons',
		rarity='e',
	},
	
	['zombie soldier armor'] = {
		customRarity='{{Rarity|e}} or {{Rarity|l}}',
		stats = {
			head = {
				hp= '',
				def= '',
			},
			chest = {
				hp= '',
				def= '',
			},
			legs = {
				hp= '',
				def= '',
			},
			boots = {
				hp= '',
				def= '',
			},
			total = {
				hp=415,
				def=291,
				
				fsb_name='Shoal',
				fsb_desc='Gain +30 Defense for each Zombie Soldier Set within 30 Blocks.',
			},
		},
		source='dungeons',
	},
	
	['zombie commander armor'] = {
		--[==[{{InfoNeeded}}
		{{InfoNeeded}}
		{{InfoNeeded}}
		--]==]
	},
		
	['zombie knight armor'] = {
		customRarity='{{Rarity|e}} or {{Rarity|l}}',
		stats = {
			head = {
				hp= '',
				def= '',
			},
			chest = {
				hp= '',
				def= '',
			},
			legs = {
				hp= '',
				def= '',
			},
			boots = {
				hp= '',
				def= '',
			},
			total = {
				hp=300,
				def=341,
				str=55,
				spd=20,
		
				fsb_name='Zombie Knight',
				fsb_desc='Gain {{Green|50}} {{Statname|Defense}} when used with [[Zombie Knight Sword]]',
			},
		},
		source='dungeons',
	},
	
	['skeletor armor'] = {
		customRarity='{{Rarity|e}} or {{Rarity|l}}',
		stats = {
			head = {
				hp= '',
				def= '',
			},
			chest = {
				hp= '',
				def= '',
			},
			legs = {
				hp= '',
				def= '',
			},
			boots = {
				hp= '',
				def= '',
			},
			total = {
				hp=375,
				def=181,
		
				specialEffect='Each piece grants a {{Aqua|1}} second cooldown reduction on bone plating.',
				fsb_name='Skeletor',
				fsb_desc='Grants 1 {{Statname|str}} and 1 {{Statname|cc}} for every {{Aqua|10}} Skeletor Kills',
			},
		},
		source='dungeons',
	},
	
	['super heavy armor'] = {
		customRarity='{{Rarity|e}} or {{Rarity|l}}',
		stats = {
			head = {
				hp= '',
				def= '',
			},
			chest = {
				hp= '',
				def= '',
			},
			legs = {
				hp= '',
				def= '',
			},
			boots = {
				hp= '',
				def= '',
			},
			total = {
				hp=300,
				def=403,
				speed=-40,
			
				specialEffect='Each piece of this armor reduces the cooldown of {{Blue|Seismic Wave}} by {{Green|5s}}.',
				fsb_name='Vindicate',
				fsb_desc='Grants {{Stat|spd|+1}} for every {{Green|+50}} {{Stat|defense}} that you have.',
			}
		},
		source='dungeons',
	},
	
	['adaptive armor'] = {
		rarity='e',
		stats = {
			head = {
				hp= '',
				def= '',
			},
			chest = {
				hp= '',
				def= '',
			},
			legs = {
				hp= '',
				def= '',
			},
			boots = {
				hp= '',
				def= '',
			},
			total = {
				hp=515,
				def=245,
				str=60,
				int=60,
		
				fsb_name='Efficient training',
				fsb_desc='Every {{Aqua|5}} Catacombs levels, this armor piece gains {{Green|+2%}} stats.',
			},
		},
		source='dungeons',
	},
	
	['shadow assassin armor'] = {
		rarity='e',
		stats = {
			head = {
				hp= '',
				def= '',
			},
			chest = {
				hp= '',
				def= '',
			},
			legs = {
				hp= '',
				def= '',
			},
			boots = {
				hp= '',
				def= '',
			},
			total = {
				hp=735,
				def=330,
				strength=100,
				speed=28,
				cd=100,
			
				fsb_name='Shadow Assassin',
				fsb_desc='Collect the shadows of the enemies you kill increasing your {{stat|damage}} for the rest of the dungeon while wearing this set. {{stat|str|+1}} every kill'
			},
		},
		source='dungeons',
	},
	
	['bouncy armor'] = {
		Rarity= "r",
		stats = {
					
			head = {
				hp = '65',
				def = '15',
			},
			chest = {
				hp = '120',
				def = '15',
			},
			legs = {
				hp = '105',
				def = '15',
			},
			boots = {
				hp = '55',
				def = '15',
			},
			total = {
				hp= '345',
				def= '60',
			
				fsb_name='Bouncing Arrow',
				fsb_desc='Your arrows have a {{yellow|25%}} chance to bounce to another target after it hits something.',
			},
		},
		source = 'Dungeons',
		rarity = 'r',
	},
	
	['necromancer lord armor'] = {
		rarity='l',
		stats = {
			head = {
				hp= '',
				def= '',
			},
			chest = {
				hp= '',
				def= '',
			},
			legs = {
				hp= '',
				def= '',
			},
			boots = {
				hp= '',
				def= '',
			},
			total = {
				hp=930,
				def=780,
				int=45,
		
				fsb_name='Soul Whisper',
				fsb_desc='Increase the damage of your necromancer summoned mobs by {{G|+20%}}.',
			},
		},
		source='dungeons',
	},

	--[[
	[''] = {
		stats = {
			head = {
				def = ,
				hp  = ,
			},
			chest = {
				def = ,
				hp  = ,
			},
			legs = {
				def = ,
				hp  = ,
			},
			boots = {
				def = ,
				hp  = ,
			},
		
			total = {
				def = ,
				hp  = ,
				
				fsb_name = '',
				fsb_desc = '',
			},
		},
		source = '',
		collection = '',
		rarity = '',
		materials = {{name='',amount=},{name='',amount=},{name='',amount=}}
	},

	[''] = {
		
		stats = {
			head = {
				def = ,
				hp  = ,
			},
			chest = {
				def = ,
				hp  = ,
			},
			legs = {
				def = ,
				hp  = ,
			},
			boots = {
				def = ,
				hp  = ,
			},
		
			total = {
				def = ,
				hp  = ,
				
				fsb_name = '',
				fsb_desc = '',
			},
		},
		source = '',
		collection = '',
		rarity = '',
		materials = {{name='',amount=},{name='',amount=},{name='',amount=}}
	},

	[''] = {
		
		stats = {
			head = {
				def = ,
				hp  = ,
			},
			chest = {
				def = ,
				hp  = ,
			},
			legs = {
				def = ,
				hp  = ,
			},
			boots = {
				def = ,
				hp  = ,
			},
		
			total = {
				def = ,
				hp  = ,
				
				fsb_name = '',
				fsb_desc = '',
			},
		},
		source = '',
		collection = '',
		rarity = '',
		materials = {{name='',amount=},{name='',amount=},{name='',amount=}}
	},

	[''] = {
		
		stats = {
			head = {
				def = ,
				hp  = ,
			},
			chest = {
				def = ,
				hp  = ,
			},
			legs = {
				def = ,
				hp  = ,
			},
			boots = {
				def = ,
				hp  = ,
			},
		
			total = {
				def = ,
				hp  = ,
				
				fsb_name = '',
				fsb_desc = '',
			},
		},
		source = '',
		collection = '',
		rarity = '',
		materials = {{name='',amount=},{name='',amount=},{name='',amount=}}
	},
	
	[''] = {
		
		stats = {
			head = {
				def = ,
				hp  = ,
			},
			chest = {
				def = ,
				hp  = ,
			},
			legs = {
				def = ,
				hp  = ,
			},
			boots = {
				def = ,
				hp  = ,
			},
		
			total = {
				def = ,
				hp  = ,
				
				fsb_name = '',
				fsb_desc = '',
			},
		},
		source = '',
		collection = '',
		rarity = '',
		materials = {{name='',amount=},{name='',amount=},{name='',amount=}}
	},

	[''] = {
		
		stats = {
			head = {
				def = ,
				hp  = ,
			},
			chest = {
				def = ,
				hp  = ,
			},
			legs = {
				def = ,
				hp  = ,
			},
			boots = {
				def = ,
				hp  = ,
			},
		
			total = {
				def = ,
				hp  = ,
				
				fsb_name = '',
				fsb_desc = '',
			},
		},
		source = '',
		collection = '',
		rarity = '',
		materials = {{name='',amount=},{name='',amount=},{name='',amount=}}
	},

	[''] = {
		
		stats = {
			head = {
				def = ,
				hp  = ,
			},
			chest = {
				def = ,
				hp  = ,
			},
			legs = {
				def = ,
				hp  = ,
			},
			boots = {
				def = ,
				hp  = ,
			},
		
			total = {
				def = ,
				hp  = ,
				
				fsb_name = '',
				fsb_desc = '',
			},
		},
		source = '',
		collection = '',
		rarity = '',
		materials = {{name='',amount=},{name='',amount=},{name='',amount=}}
	} --]] --]=]
}

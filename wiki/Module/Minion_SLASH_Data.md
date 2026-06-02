return {
	--------------------------------
	-- Farming
	--------------------------------
	['Wheat'] = {
		type = 'Farming',
		collection = 'Wheat I',
		items = {
			{ item = 'Wheat', avg = 1, exp = 0.2 },
			{ item = 'Seeds', avg = 1.5, exp = 0.1 },
		},
		drops = {
			none = {
				{ item = 'Wheat', avg = 1, exp = '0.2 Farming' }, -- exp not tested
				{ item = 'Seeds', avg = 1.5, exp = '0.1 Farming' },
			},
			compactor = {
				{ item = 'Hay Bale', exp = '1.8 Farming', from = { item = 'Wheat', num = 9 } }, -- exp not tested
			},
			sc3000 = {
				{ item = 'Enchanted Bread', exp = '12 Farming', from = { item = 'Wheat', num = 60 } }, -- exp:tested
				{ item = 'Enchanted Wheat', exp = '32 Farming', from = { item = 'Wheat', num = 160 } }, -- exp not tested
				{ item = 'Enchanted Hay Bale', exp = '5120 Farming', from = { item = 'Enchanted Wheat', num = 160 } }, -- exp not tested
				{ item = 'Enchanted Seeds', exp = '16 Farming', from = { item = 'Seeds', num = 160 } }, -- exp:tested
				{ item = 'Box of Seeds', exp = '2560 Farming', from = { item = 'Enchanted Seeds', num = 160 } }, -- exp not tested
			},
		},
		recipes = {
			['Hay Bale'] = { {'Wheat', 9 } },
			['Enchanted Bread'] = { {'Wheat', 60 } },
			['Enchanted Wheat'] = { {'Wheat', 160 } },
			['Enchanted Hay Bale'] = { {'Enchanted Wheat', 160 } },
			['Enchanted Seeds'] = { {'Seeds', 160 } },
			['Box of Seeds'] = { {'Enchanted Seeds', 160 } },
		},
		stats = {
			{ tba = 15, storage = 128, crafting = { item = 'Wheat', num = 10, B2 = 'Wooden Hoe' } },
			{ tba = 15, storage = 256, crafting = { item = 'Wheat', num = 20 } },
			{ tba = 13, storage = 256, crafting = { item = 'Wheat', num = 40 } },
			{ tba = 13, storage = 384, crafting = { item = 'Wheat', num = 64 } },
			{ tba = 11, storage = 384, crafting = { item = 'Enchanted Wheat', num = 1 } },
			{ tba = 11, storage = 576, crafting = { item = 'Enchanted Wheat', num = 2 } },
			{ tba = 10, storage = 576, crafting = { item = 'Enchanted Wheat', num = 4 } },
			{ tba = 10, storage = 768, crafting = { item = 'Enchanted Wheat', num = 8 } },
			{ tba = 9, storage = 768, crafting = { item = 'Enchanted Wheat', num = 16 } },
			{ tba = 9, storage = 960, crafting = { item = 'Enchanted Wheat', num = 32 } },
			{ tba = 8, storage = 960, crafting = { item = 'Enchanted Wheat', num = 64 } },
			{ tba = 7, storage = 960, trade = {
				{ item = 'Enchanted Wheat', num = 1024 },
				{ item = 'Pelt', num = 75 },
			}, tradeNpc = 'Tony' },
		},
		description = '&7Place this minion and it will/&7start generating and harvesting/&7wheat. Requires dirt or soil/&7nearby so wheat can be planted./&7Minions also work when you are/&7offline!'
	},
	['Sunflower'] = {
			type = 'Farming',
			collection = 'Sunflower II',
			items = {
				{ item = 'Sunflower', avg = 3, exp = 0.1 }, -- 2-4
				{ item = 'Moonflower', avg = 3, exp = 0.1 },
			},
			drops = {
				none = {
					{ item = 'Sunflower', avg = 3, exp = '0.1 Farming' },
					{ item = 'Moonflower', avg = 3, exp = '0.1 Farming' },
				},
				sc3000 = {
					{ item = 'Enchanted Sunflower', exp = '16 Farming', from = { item = 'Sunflower', num = 160 } },
					{ item = 'Enchanted Moonflower', exp = '2560 Farming', from = { item = 'Moonflower', num = 160 } },
					{ item = 'Compacted Sunflower', exp = '16 Farming', from = { item = 'Enchanted Sunflower', num = 160 } },
					{ item = 'Compacted Moonflower', exp = '2560 Farming', from = { item = 'Enchanted Moonflower', num = 160 } },
				},
			},
			recipes = {
				['Enchanted Sunflower'] = { {'Sunflower', 160 } },
				['Enchanted Moonflower'] = { {'Moonflower', 160 } },
				['Compacted Sunflower'] = { {'Enchanted Sunflower', 160 } },
				['Compacted Moonflower'] = { {'Enchanted Moonflower', 160 } },
			},
			stats = {
				{ tba = 24, storage = 128, crafting = { item = 'Sunflower', num = 16, B2 = 'Wooden Hoe' } },
				{ tba = 23, storage = 192, crafting = { item = 'Sunflower', num = 32 } },
				{ tba = 22, storage = 320, crafting = { item = 'Sunflower', num = 64 } },
				{ tba = 21, storage = 384, crafting = { item = 'Enchanted Sunflower', num = 1 } },
				{ tba = 20, storage = 448, crafting = { item = 'Enchanted Sunflower', num = 3 } },
				{ tba = 19, storage = 512, crafting = { item = 'Enchanted Sunflower', num = 8 } },
				{ tba = 18, storage = 576, crafting = { item = 'Enchanted Sunflower', num = 16 } },
				{ tba = 17, storage = 704, crafting = { item = 'Enchanted Sunflower', num = 32 } },
				{ tba = 16, storage = 768, crafting = { item = 'Enchanted Sunflower', num = 64 } },
				{ tba = 15, storage = 896, crafting = { item = 'Compacted Sunflower', num = 1 } },
				{ tba = 14, storage = 960, crafting = { item = 'Compacted Sunflower', num = 2 } },
			},
			description = '&7Place this minion and it will/&7start generating sunflowers during the day,/&7 and moonflowers at night./&7 Minions also work when/&7you are offline!'
		},
	['Carrot'] = {
		type = 'Farming',
		collection = 'Carrot I',
		items = {
			{ item = 'Carrot', avg = 3, exp = 0.1 }, -- 2-4
		},
		drops = {
			none = {
				{ item = 'Carrot', avg = 3, exp = '0.1 Farming' },
			},
			sc3000 = {
				{ item = 'Enchanted Carrot', exp = '16 Farming', from = { item = 'Carrot', num = 160 } },
				{ item = 'Enchanted Golden Carrot', exp = '2560 Farming', from = { item = 'Enchanted Carrot', num = 160 } }, -- exp not tested
			},
		},
		recipes = {
			['Enchanted Carrot'] = { {'Carrot', 160 } },
			['Enchanted Golden Carrot'] = { {'Enchanted Carrot', 160 } },
		},
		stats = {
			{ tba = 20, storage = 64, crafting = { item = 'Carrot', num = 16, B2 = 'Wooden Hoe' } },
			{ tba = 20, storage = 192, crafting = { item = 'Carrot', num = 32 } },
			{ tba = 18, storage = 192, crafting = { item = 'Carrot', num = 64 } },
			{ tba = 18, storage = 384, crafting = { item = 'Enchanted Carrot', num = 1 } },
			{ tba = 16, storage = 384, crafting = { item = 'Enchanted Carrot', num = 3 } },
			{ tba = 16, storage = 576, crafting = { item = 'Enchanted Carrot', num = 8 } },
			{ tba = 14, storage = 576, crafting = { item = 'Enchanted Carrot', num = 16 } },
			{ tba = 14, storage = 768, crafting = { item = 'Enchanted Carrot', num = 32 } },
			{ tba = 12, storage = 768, crafting = { item = 'Enchanted Carrot', num = 64 } },
			{ tba = 12, storage = 960, crafting = { item = 'Enchanted Golden Carrot', num = 1 } },
			{ tba = 10, storage = 960, crafting = { item = 'Enchanted Golden Carrot', num = 2 } },
			{ tba = 8, storage = 960, trade = {
				{ item = 'Enchanted Golden Carrot', num = 32 },
				{ item = 'Pelt', num = 75 },
			}, tradeNpc = 'Tony' },
		},
		description = '&7Place this minion and it will/&7start generating and harvesting/&7carrots. Requires dirt or soil/&7nearby so carrots can be planted./&7Minions also work when you are/&7offline!'
	},
	['Potato'] = {
		type = 'Farming',
		collection = 'Potato I',
		items = {
			{ item = 'Potato', avg = 3, exp = 0.1 }, -- 2-4
		},
		drops = {
			none = {
				{ item = 'Potato', avg = 3, exp = '0.1 Farming' },
			},
			sc3000 = {
				{ item = 'Enchanted Potato', exp = '16 Farming', from = { item = 'Potato', num = 160 } },
				{ item = 'Enchanted Baked Potato', exp = '2560 Farming', from = { item = 'Enchanted Potato', num = 160 } },
			},
			hunterknife = {
				{ item = 'French Fries', from = { item = 'Potato', num = 1 } },
			}
		},
		recipes = {
			['Enchanted Potato'] = { {'Potato', 160 } },
			['Enchanted Baked Potato'] = { {'Enchanted Potato', 160 } },
		},
		stats = {
			{ tba = 20, storage = 64, crafting = { item = 'Potato', num = 16, B2 = 'Wooden Hoe' } },
			{ tba = 20, storage = 192, crafting = { item = 'Potato', num = 32 } },
			{ tba = 18, storage = 192, crafting = { item = 'Potato', num = 64 } },
			{ tba = 18, storage = 384, crafting = { item = 'Enchanted Potato', num = 1 } },
			{ tba = 16, storage = 384, crafting = { item = 'Enchanted Potato', num = 3 } },
			{ tba = 16, storage = 576, crafting = { item = 'Enchanted Potato', num = 8 } },
			{ tba = 14, storage = 576, crafting = { item = 'Enchanted Potato', num = 16 } },
			{ tba = 14, storage = 768, crafting = { item = 'Enchanted Potato', num = 32 } },
			{ tba = 12, storage = 768, crafting = { item = 'Enchanted Potato', num = 64 } },
			{ tba = 12, storage = 960, crafting = { item = 'Enchanted Baked Potato', num = 1 } },
			{ tba = 10, storage = 960, crafting = { item = 'Enchanted Baked Potato', num = 2 } },
			{ tba = 8, storage = 960, trade = {
				{ item = 'Enchanted Baked Potato', num = 32 },
				{ item = 'Pelt', num = 75 },
			}, tradeNpc = 'Tony' },
		},
		description = '&7Place this minion and it will/&7start generating and harvesting/&7potatoes. Requires dirt or soil/&7nearby so potatoes can be/&7planted. Minions also work when/&7you are offline!'
	},
	['Pumpkin'] = {
		type = 'Farming',
		collection = 'Pumpkin I',
		items = {
			{ item = 'Pumpkin', avg = 1, exp = 0.3 }, -- Using offline calculation, however pumpkins give an item EVERY action, instead of every other one if the player is on their island.
		},
		drops = {
			none = {
				{ item = 'Pumpkin', avg = 1, exp = '0.3 Farming' },
			},
			sc3000 = {
				{ item = 'Enchanted Pumpkin', exp = '48 Farming', from = { item = 'Pumpkin', num = 160 } },
				{ item = 'Polished Pumpkin', exp = '7680 Farming', from = { item = 'Enchanted Pumpkin', num = 160 } },
			},
		},
		recipes = {
			['Enchanted Pumpkin'] = { {'Pumpkin', 160 } },
			['Polished Pumpkin'] = { {'Enchanted Pumpkin', 160 } },
		},
		stats = {
			{ tba = 32, storage = 64, crafting = { item = 'Pumpkin', num = 10, B2 = 'Wooden Hoe' } },
			{ tba = 32, storage = 192, crafting = { item = 'Pumpkin', num = 20 } },
			{ tba = 30, storage = 192, crafting = { item = 'Pumpkin', num = 40 } },
			{ tba = 30, storage = 384, crafting = { item = 'Pumpkin', num = 64 } },
			{ tba = 27, storage = 384, crafting = { item = 'Enchanted Pumpkin', num = 1 } },
			{ tba = 27, storage = 576, crafting = { item = 'Enchanted Pumpkin', num = 2 } },
			{ tba = 24, storage = 576, crafting = { item = 'Enchanted Pumpkin', num = 4 } },
			{ tba = 24, storage = 768, crafting = { item = 'Enchanted Pumpkin', num = 8 } },
			{ tba = 20, storage = 768, crafting = { item = 'Enchanted Pumpkin', num = 16 } },
			{ tba = 20, storage = 960, crafting = { item = 'Enchanted Pumpkin', num = 32 } },
			{ tba = 16, storage = 960, crafting = { item = 'Enchanted Pumpkin', num = 64 } },
			{ tba = 12, storage = 960, trade = {
				{ item = 'Enchanted Pumpkin', num = 1024 },
				{ item = 'Pelt', num = 75 },
			}, tradeNpc = 'Tony' },
		},
		description = '&7Place this minion and it will/&7start generating and harvesting/&7pumpkins! Requires an open area/&7to place pumpkins. Minions also/&7work when you are offline!'
	},
	['Melon'] = {
		type = 'Farming',
		collection = 'Melon Slice I',
		items = {
			{ item = 'Melon Slice', avg = 5, exp = 0.1 }, -- 3-7 ; Using offline calculation, however melons give an item EVERY action, instead of every other one if the player is on their island.
		},
		drops = {
			none = {
				{ item = 'Melon Slice', avg = 5, exp = '0.1 Farming' },
			},
			compactor = {
				{ item = 'Melon', exp = '0.9 Farming', from = { item = 'Melon Slice', num = 9 } },
			},
			sc3000 = {
				{ item = 'Enchanted Melon Slice', exp = '16 Farming', from = { item = 'Melon Slice', num = 160 } },
				{ item = 'Enchanted Melon', exp = '2560 Farming', from = { item = 'Enchanted Melon Slice', num = 160 } },
			},
		},
		recipes = {
			['Melon'] = { {'Melon Slice', 9 } },
			['Enchanted Melon Slice'] = { {'Melon Slice', 160 } },
			['Enchanted Melon'] = { {'Enchanted Melon Slice', 160 } },
		},
		stats = {
			{ tba = 24, storage = 64, crafting = { item = 'Melon Slice', num = 32, B2 = 'Wooden Hoe' } },
			{ tba = 24, storage = 192, crafting = { item = 'Melon Slice', num = 64 } },
			{ tba = 22.5, storage = 192, crafting = { item = 'Melon', num = 16 } },
			{ tba = 22.5, storage = 384, crafting = { item = 'Melon', num = 32 } },
			{ tba = 21, storage = 384, crafting = { item = 'Melon', num = 64 } },
			{ tba = 21, storage = 576, crafting = { item = 'Enchanted Melon Slice', num = 8 } },
			{ tba = 18.5, storage = 576, crafting = { item = 'Enchanted Melon Slice', num = 16 } },
			{ tba = 18.5, storage = 768, crafting = { item = 'Enchanted Melon Slice', num = 32 } },
			{ tba = 16, storage = 768, crafting = { item = 'Enchanted Melon Slice', num = 64 } },
			{ tba = 16, storage = 960, crafting = { item = 'Enchanted Melon', num = 1 } },
			{ tba = 13, storage = 960, crafting = { item = 'Enchanted Melon', num = 2 } },
			{ tba = 10, storage = 960, trade = {
				{ item = 'Enchanted Melon', num = 32 },
				{ item = 'Pelt', num = 75 },
			}, tradeNpc = 'Tony' },
		},
		description = '&7Place this minion and it will/&7start generating and harvesting/&7melons! Requires an open area/&7to place melons. Minions also work/&7when you are offline!'
	},
	['Mushroom'] = {
		type = 'Farming',
		collection = 'Mushroom I',
		items = {
			-- { item = 'Mushroom', avg = 1 }, -- Broken into the following:
			{ item = 'Brown Mushroom', avg = 0.5, exp = 0.5 },
			{ item = 'Red Mushroom', avg = 0.5, exp = 0.5 },
		},
		drops = {
			none = {
				{ item = 'Red Mushroom', avg = 0.5, exp = '0.3 Farming' }, -- exp not tested
				{ item = 'Brown Mushroom', avg = 0.5, exp = '0.3 Farming' }, -- exp not tested
			},
			compactor = {
				{ item = 'Red Mushroom Block', exp = '2.7 Farming', from = { item = 'Red Mushroom', num = 9 } }, -- exp not tested
				{ item = 'Brown Mushroom Block', exp = '2.7 Farming', from = { item = 'Brown Mushroom', num = 9 } }, -- exp not tested
			},
			sc3000 = {
				{ item = 'Enchanted Red Mushroom', exp = '48 Farming', from = { item = 'Red Mushroom', num = 160 } }, -- exp not tested
				{ item = 'Enchanted Brown Mushroom', exp = '48 Farming', from = { item = 'Brown Mushroom', num = 160 } }, -- exp not tested
				{ item = 'Enchanted Red Mushroom Block', exp = '7680 Farming', from = { item = 'Enchanted Red Mushroom', num = 160 } }, -- exp not tested
				{ item = 'Enchanted Brown Mushroom Block', exp = '7680 Farming', from = { item = 'Enchanted Brown Mushroom', num = 160 } }, -- exp not tested
			},
		},
		recipes = {
			-- Normal recipes allow either type of mushroom
			['Enchanted Mushroom'] = { {'Mushroom', 160 } },
			-- Tier 12 requires both red and brown
			['Enchanted Red Mushroom'] = { {'Red Mushroom', 160 } },
			['Enchanted Brown Mushroom'] = { {'Brown Mushroom', 160 } },
		},
		stats = {
			{ tba = 30, storage = 64, crafting = { item = 'Red Mushroom', num = 10, B2 = 'Wooden Hoe' } },
			{ tba = 30, storage = 192, crafting = { item = 'Red Mushroom', num = 20 } },
			{ tba = 28, storage = 192, crafting = { item = 'Red Mushroom', num = 40 } },
			{ tba = 28, storage = 384, crafting = { item = 'Red Mushroom', num = 64 } },
			{ tba = 26, storage = 384, crafting = { item = 'Enchanted Red Mushroom', num = 1 } },
			{ tba = 26, storage = 576, crafting = { item = 'Enchanted Red Mushroom', num = 2 } },
			{ tba = 23, storage = 576, crafting = { item = 'Enchanted Red Mushroom', num = 4 } },
			{ tba = 23, storage = 768, crafting = { item = 'Enchanted Red Mushroom', num = 8 } },
			{ tba = 20, storage = 768, crafting = { item = 'Enchanted Red Mushroom', num = 16 } },
			{ tba = 20, storage = 960, crafting = { item = 'Enchanted Red Mushroom', num = 32 } },
			{ tba = 16, storage = 960, crafting = { item = 'Enchanted Red Mushroom', num = 64 } }, 
			{ tba = 12, storage = 960, trade = {
				{ item = 'Enchanted Brown Mushroom', num = 512 },
				{ item = 'Enchanted Red Mushroom', num = 512 },
				{ item = 'Pelt', num = 75 },
			}, tradeNpc = 'Tony' },
		},
		description = '&7Place this minion and it will/&7start generating and harvesting/&7red and brown mushrooms!/&7Requires an area that is/&7suitable for mushrooms to be/&7placed. Minions also work when/&7you are offline!'
	},
	['Cocoa Beans'] = {
		type = 'Farming',
		collection = 'Cocoa Beans I',
		items = {
			{ item = 'Cocoa Beans', avg = 3, exp = 0.2 },
		},
		drops = {
			none = {
				{ item = 'Cocoa Beans', avg = 3, exp = '0.2 Farming' },
			},
			sc3000 = {
				{ item = 'Enchanted Cocoa Beans', exp = '32 Farming', from = { item = 'Cocoa Beans', num = 160 } },
			},
		},
		recipes = {
			['Enchanted Cocoa Beans'] = { {'Cocoa Beans', 160 } },
			['Enchanted Cookie'] = {
				{'Enchanted Cocoa Beans', 128 },
				{'Wheat', 32 }, 
			},
		},
		stats = {
			{ tba = 27, storage = 64, crafting = { item = 'Cocoa Beans', num = 10, B2 = 'Wooden Hoe' } },
			{ tba = 27, storage = 192, crafting = { item = 'Cocoa Beans', num = 20 } },
			{ tba = 25, storage = 192, crafting = { item = 'Cocoa Beans', num = 40 } },
			{ tba = 25, storage = 384, crafting = { item = 'Cocoa Beans', num = 64 } },
			{ tba = 23, storage = 384, crafting = { item = 'Enchanted Cocoa Beans', num = 1 } },
			{ tba = 23, storage = 576, crafting = { item = 'Enchanted Cocoa Beans', num = 3 } },
			{ tba = 21, storage = 576, crafting = { item = 'Enchanted Cocoa Beans', num = 8 } },
			{ tba = 21, storage = 768, crafting = { item = 'Enchanted Cocoa Beans', num = 16 } },
			{ tba = 18, storage = 768, crafting = { item = 'Enchanted Cocoa Beans', num = 32 } },
			{ tba = 18, storage = 960, crafting = { item = 'Enchanted Cocoa Beans', num = 64 } },
			{ tba = 15, storage = 960, crafting = { item = 'Enchanted Cookie', num = 1 } },
			{ tba = 12, storage = 960, trade = {
				{ item = 'Enchanted Cookie', num = 16 },
				{ item = 'Pelt', num = 75 },
			}, tradeNpc = 'Tony' },
		},
		description = '&7Place this minion and it will/&7start generating and harvesting/&7cocoa beans. Requires jungle logs/&7nearby so cocoa can be/&7placed, or air nearby so jungle/&7logs can be placed. Minions also/&7work when you are offline!'
	},
	['Cactus'] = {
		type = 'Farming',
		collection = 'Cactus I',
		items = {
			-- CHECK OFFLINE?
			{ item = 'Cactus', avg = 3, exp = 0.2 },
			{ item = 'Cactus Green', avg = 3, condition = 'Auto Smelter', converts = 'Cactus', exp = 0.2 },
		},
		drops = {
			none = {
				{ item = 'Cactus', avg = 3, exp = '0.2 Farming' },
			},
			smelter = {
				{ item = 'Cactus Green', exp = '0.2 Farming', from = { item = 'Cactus', num = 1 } },
			},
			smelter_sc3000 = {
				{ item = 'Enchanted Cactus Green', exp = '80 Farming', from = { item = 'Cactus Green', num = 160 } }, -- exp not tested
				{ item = 'Enchanted Cactus', exp = '12800 Farming', from = { item = 'Enchanted Cactus Green', num = 160 } }, -- exp not tested
			},
		},
		recipes = {
			['Enchanted Cactus Green'] = { {'Cactus', 160 } },
			['Enchanted Cactus'] = { {'Enchanted Cactus Green', 160 } },
		},
		stats = {
			{ tba = 27, storage = 64, crafting = { item = 'Cactus', num = 16, B2 = 'Wooden Hoe' } },
			{ tba = 27, storage = 192, crafting = { item = 'Cactus', num = 32 } },
			{ tba = 25, storage = 192, crafting = { item = 'Cactus', num = 64 } },
			{ tba = 25, storage = 384, crafting = { item = 'Enchanted Cactus Green', num = 1 } },
			{ tba = 23, storage = 384, crafting = { item = 'Enchanted Cactus Green', num = 3 } },
			{ tba = 23, storage = 576, crafting = { item = 'Enchanted Cactus Green', num = 8 } },
			{ tba = 21, storage = 576, crafting = { item = 'Enchanted Cactus Green', num = 16 } },
			{ tba = 21, storage = 768, crafting = { item = 'Enchanted Cactus Green', num = 32 } },
			{ tba = 18, storage = 768, crafting = { item = 'Enchanted Cactus Green', num = 64 } },
			{ tba = 18, storage = 960, crafting = { item = 'Enchanted Cactus', num = 1 } },
			{ tba = 15, storage = 960, crafting = { item = 'Enchanted Cactus', num = 2 } },
			{ tba = 12, storage = 960, trade = {
				{ item = 'Enchanted Cactus', num = 32 },
				{ item = 'Pelt', num = 75 },
			}, tradeNpc = 'Tony' },
		},
		description = '&7Place this minion and it will/&7start generating and harvesting/&7cactus. Requires sand nearby so/&7cacti can be planted. Minions/&7also work when you are offline!'
	},
	['Sugar Cane'] = {
		type = 'Farming',
		collection = 'Sugar Cane I',
		items = {
			-- CHECK OFFLINE?
			{ item = 'Sugar Cane', avg = 3, exp = 0.1 },
		},
		drops = {
			none = {
				{ item = 'Sugar Cane', avg = 3, exp = '0.1 Farming' },
			},
			sc3000 = {
				{ item = 'Enchanted Sugar', exp = '16 Alchemy', from = { item = 'Sugar Cane', num = 160 } },
				{ item = 'Enchanted Sugar Cane', exp = '2560 Alchemy', from = { item = 'Enchanted Sugar', num = 160 } },
			},
		},
		recipes = {
			['Enchanted Sugar'] = { {'Sugar Cane', 160 } },
			['Enchanted Sugar Cane'] = { {'Enchanted Sugar', 160 } },
		},
		stats = {
			{ tba = 22, storage = 64, crafting = { item = 'Sugar Cane', num = 16, B2 = 'Wooden Hoe' } },
			{ tba = 22, storage = 192, crafting = { item = 'Sugar Cane', num = 32 } },
			{ tba = 20, storage = 192, crafting = { item = 'Sugar Cane', num = 64 } },
			{ tba = 20, storage = 384, crafting = { item = 'Enchanted Sugar', num = 1 } },
			{ tba = 18, storage = 384, crafting = { item = 'Enchanted Sugar', num = 3 } },
			{ tba = 18, storage = 576, crafting = { item = 'Enchanted Sugar', num = 8 } },
			{ tba = 16, storage = 576, crafting = { item = 'Enchanted Sugar', num = 16 } },
			{ tba = 16, storage = 768, crafting = { item = 'Enchanted Sugar', num = 32 } },
			{ tba = 14.5, storage = 768, crafting = { item = 'Enchanted Sugar', num = 64 } },
			{ tba = 14.5, storage = 960, crafting = { item = 'Enchanted Sugar Cane', num = 1 } },
			{ tba = 12, storage = 960, crafting = { item = 'Enchanted Sugar Cane', num = 2 } },
			{ tba = 9, storage = 960, trade = {
				{ item = 'Enchanted Sugar Cane', num = 32 },
				{ item = 'Pelt', num = 75 },
			}, tradeNpc = 'Tony' },
		},
		description = '&7Place this minion and it will/&7start generating and harvesting/&7sugar canes! Requires an area/&7that is suitable for sugar cane/&7to be/&7placed. Minions also work/&7when you are offline!'
	},
	['Chicken'] = {
		type = 'Farming',
		collection = 'Raw Chicken I',
		items = {
			{ item = 'Raw Chicken', avg = 1, exp = 0.1 },
			{ item = 'Feather', avg = 1, exp = 0.2 },
			{ item = 'Egg', avg = 1, exp = 0.2, condition = 'Enchanted Egg' },
		},
		drops = {
			none = {
				{ item = 'Raw Chicken', avg = 1, exp = '0.1 Farming' },
				{ item = 'Feather', avg = 1, exp = '0.2 Farming' },
			},
			enchantedegg = {
				{ item = 'Egg', avg = 1, exp = '0.2 Farming' },
			},
			sc3000 = {
				{ item = 'Enchanted Raw Chicken', exp = '16 Farming', from = { item = 'Raw Chicken', num = 160 } },
				{ item = 'Enchanted Feather', exp = '32 Farming', from = { item = 'Feather', num = 160 } },
			},
			enchantedegg_sc3000 = {
				{ item = 'Enchanted Egg', exp = '115 Farming', from = { item = 'Egg', num = 144 } }, -- exp not tested
				{ item = 'Super Enchanted Egg', exp = '16560 Farming', from = { item = 'Enchanted Egg', num = 144 } }, -- exp not tested
			},
		},
		recipes = {
			['Enchanted Raw Chicken'] = { {'Raw Chicken', 160 } },
			['Enchanted Feather'] = { {'Feather', 160 } },
			['Enchanted Egg'] = { {'Egg', 144 } },
			['Super Enchanted Egg'] = { {'Enchanted Egg', 144 } },
		},
		stats = {
			{ tba = 26, storage = 192, crafting = { item = 'Raw Chicken', num = 8, B2 = 'Wooden Sword' } },
			{ tba = 26, storage = 320, crafting = { item = 'Raw Chicken', num = 16 } },
			{ tba = 24, storage = 320, crafting = { item = 'Raw Chicken', num = 32 } },
			{ tba = 24, storage = 384, crafting = { item = 'Raw Chicken', num = 64 } },
			{ tba = 22, storage = 384, crafting = { item = 'Enchanted Raw Chicken', num = 1 } },
			{ tba = 22, storage = 576, crafting = { item = 'Enchanted Raw Chicken', num = 2 } },
			{ tba = 20, storage = 576, crafting = { item = 'Enchanted Raw Chicken', num = 4 } },
			{ tba = 20, storage = 768, crafting = { item = 'Enchanted Raw Chicken', num = 8 } },
			{ tba = 18, storage = 768, crafting = { item = 'Enchanted Raw Chicken', num = 16 } },
			{ tba = 18, storage = 960, crafting = { item = 'Enchanted Raw Chicken', num = 32 } },
			{ tba = 15, storage = 960, crafting = { item = 'Enchanted Raw Chicken', num = 64 } }, 
			{ tba = 12, storage = 960, trade = {
				{ item = 'Enchanted Raw Chicken', num = 1024 },
				{ item = 'Pelt', num = 75 },
			}, tradeNpc = 'Tony' },
		},
		description = '&7Place this minion and it will/&7start generating and slaying/&7Chickens! Minions also work when/&7you are offline!'
	},
	['Cow'] = {
		type = 'Farming',
		collection = 'Leather I',
		items = {
			{ item = 'Raw Beef', avg = 1, exp = 0.1 },
			{ item = 'Leather', avg = 1, exp = 0.2 },
		},
		drops = {
			none = {
				{ item = 'Raw Beef', avg = 1, exp = '0.1 Farming' },
				{ item = 'Leather', avg = 1, exp = '0.2 Farming' },
			},
			sc3000 = {
				{ item = 'Enchanted Raw Beef', exp = '16 Farming', from = { item = 'Raw Beef', num = 160 } },
				{ item = 'Enchanted Leather', exp = '32 Farming', from = { item = 'Leather', num = 160 } }, -- exp not tested
			},
		},
		recipes = {
			['Enchanted Raw Beef'] = { {'Raw Beef', 160 } },
			['Enchanted Leather'] = { {'Leather', 160 } },
		},
		stats = {
			{ tba = 26, storage = 128, crafting = { item = 'Raw Beef', num = 8, B2 = 'Wooden Sword' } },
			{ tba = 26, storage = 256, crafting = { item = 'Raw Beef', num = 16 } },
			{ tba = 24, storage = 256, crafting = { item = 'Raw Beef', num = 32 } },
			{ tba = 24, storage = 384, crafting = { item = 'Raw Beef', num = 64 } },
			{ tba = 22, storage = 384, crafting = { item = 'Enchanted Raw Beef', num = 1 } },
			{ tba = 22, storage = 576, crafting = { item = 'Enchanted Raw Beef', num = 3 } },
			{ tba = 20, storage = 576, crafting = { item = 'Enchanted Raw Beef', num = 8 } },
			{ tba = 20, storage = 768, crafting = { item = 'Enchanted Raw Beef', num = 16 } },
			{ tba = 17, storage = 768, crafting = { item = 'Enchanted Raw Beef', num = 32 } },
			{ tba = 17, storage = 960, crafting = { item = 'Enchanted Raw Beef', num = 64 } },
			{ tba = 13, storage = 960, crafting = { item = 'Enchanted Leather', num = 64 } },
			{ tba = 10, storage = 960, trade = {
				{ item = 'Enchanted Leather', num = 1028 },
				{ item = 'Pelt', num = 75 },
			}, tradeNpc = 'Tony' },
		},
		description = '&7Place this minion and it will/&7start generating and slaying/&7Cows! Minions also work when you/&7are offline!'
	},
	['Pig'] = {
		type = 'Farming',
		collection = 'Raw Porkchop I',
		items = {
			{ item = 'Raw Porkchop', avg = 1, exp = 0.2 },
		},
		drops = {
			none = {
				{ item = 'Raw Porkchop', avg = 1, exp = '0.2 Farming' },
			},
			sc3000 = {
				{ item = 'Enchanted Raw Porkchop', exp = '32 Farming', from = { item = 'Raw Porkchop', num = 160 } },
				{ item = 'Enchanted Cooked Porkchop', exp = '5120 Farming', from = { item = 'Enchanted Raw Porkchop', num = 160 } },
			},
		},
		recipes = {
			['Enchanted Raw Porkchop'] = { {'Raw Porkchop', 160 } },
			['Enchanted Cooked Porkchop'] = { {'Enchanted Raw Porkchop', 160 } },
		},
		stats = {
			{ tba = 26, storage = 64, crafting = { item = 'Raw Porkchop', num = 8, B2 = 'Wooden Sword' } },
			{ tba = 26, storage = 192, crafting = { item = 'Raw Porkchop', num = 16 } },
			{ tba = 24, storage = 192, crafting = { item = 'Raw Porkchop', num = 32 } },
			{ tba = 24, storage = 384, crafting = { item = 'Raw Porkchop', num = 64 } },
			{ tba = 22, storage = 384, crafting = { item = 'Enchanted Raw Porkchop', num = 1 } },
			{ tba = 22, storage = 576, crafting = { item = 'Enchanted Raw Porkchop', num = 3 } },
			{ tba = 20, storage = 576, crafting = { item = 'Enchanted Raw Porkchop', num = 8 } },
			{ tba = 20, storage = 768, crafting = { item = 'Enchanted Raw Porkchop', num = 16 } },
			{ tba = 17, storage = 768, crafting = { item = 'Enchanted Raw Porkchop', num = 32 } },
			{ tba = 17, storage = 960, crafting = { item = 'Enchanted Raw Porkchop', num = 64 } },
			{ tba = 13, storage = 960, crafting = { item = 'Enchanted Cooked Porkchop', num = 1 } },
			{ tba = 10, storage = 960, trade = {
				{ item = 'Enchanted Cooked Porkchop', num = 16 },
				{ item = 'Pelt', num = 75 },
			}, tradeNpc = 'Tony' },
		},
		description = '&7Place this minion and it will/&7start generating and slaying/&7Pigs! Minions also work when you/&7are offline!'
	},
	['Sheep'] = {
		type = 'Farming',
		collection = 'Raw Mutton I',
		items = {
			{ item = 'Raw Mutton', avg = 1, exp = 0.1 },
			{ item = 'White Wool', avg = 1, exp = 0.1 },
		},
		drops = {
			none = {
				{ item = 'Raw Mutton', avg = 1, exp = '0.1 Farming' },
				{ item = 'White Wool', avg = 1, exp = '0.1 Farming' },
			},
			sc3000 = {
				{ item = 'Enchanted Raw Mutton', exp = '16 Farming', from = { item = 'Raw Mutton', num = 160 } },
				{ item = 'Enchanted Cooked Mutton', exp = '2560 Farming', from = { item = 'Enchanted Raw Mutton', num = 160 } },
				{ item = 'Enchanted Wool', exp = '16 Farming', from = { item = 'White Wool', num = 160 } },
			},
		},
		recipes = {
			['Enchanted Raw Mutton'] = { {'Raw Mutton', 160 } },
			['Enchanted Cooked Mutton'] = { {'Enchanted Raw Mutton', 160 } },
			['Enchanted Wool'] = { {'White Wool', 160 } },
		},
		stats = {
			{ tba = 24, storage = 128, crafting = { item = 'Raw Mutton', num = 8, B2 = 'Wooden Sword' } },
			{ tba = 24, storage = 256, crafting = { item = 'Raw Mutton', num = 16 } },
			{ tba = 22, storage = 256, crafting = { item = 'Raw Mutton', num = 32 } },
			{ tba = 22, storage = 384, crafting = { item = 'Raw Mutton', num = 64 } },
			{ tba = 20, storage = 384, crafting = { item = 'Enchanted Raw Mutton', num = 1 } },
			{ tba = 20, storage = 576, crafting = { item = 'Enchanted Raw Mutton', num = 3 } },
			{ tba = 18, storage = 576, crafting = { item = 'Enchanted Raw Mutton', num = 8 } },
			{ tba = 18, storage = 768, crafting = { item = 'Enchanted Raw Mutton', num = 16 } },
			{ tba = 16, storage = 768, crafting = { item = 'Enchanted Raw Mutton', num = 32 } },
			{ tba = 16, storage = 960, crafting = { item = 'Enchanted Raw Mutton', num = 64 } },
			{ tba = 12, storage = 960, crafting = { item = 'Enchanted Cooked Mutton', num = 1 } },
			{ tba = 9, storage = 960, trade = {
				{ item = 'Enchanted Cooked Mutton', num = 16 },
				{ item = 'Pelt', num = 75 },
			}, tradeNpc = 'Tony' },
		},
		description = '&7Place this minion and it will/&7start generating and slaying/&7Sheep! Minions also work when/&7you are offline!'
	},
	['Rabbit'] = {
		type = 'Farming',
		collection = 'Raw Rabbit I',
		items = {
			-- Averages taken from this sample: ??
			{ item = 'Raw Rabbit', avg = 1, exp = 0.1 },
			{ item = 'Rabbit\'s Foot', avg = 0.35, exp = 0.2 },
			{ item = 'Rabbit Hide', avg = 0.35, exp = 0.2 },
		},
		drops = {
			none = {
				{ item = 'Raw Rabbit', avg = 1, exp = '0.1 Farming' },
				{ item = 'Rabbit\'s Foot', avg = 0.35, exp = '0.2 Farming' },
				{ item = 'Rabbit Hide', avg = 0.35, exp = '0.2 Farming' },
			},
			sc3000 = {
				{ item = 'Enchanted Raw Rabbit', exp = '16 Farming', from = { item = 'Raw Rabbit', num = 160 } },
				{ item = 'Enchanted Cooked Rabbit', exp = '2560 Farming', from = { item = 'Enchanted Raw Rabbit', num = 160 } }, -- exp not tested
				{ item = 'Enchanted Rabbit Foot', exp = '32 Farming', from = { item = 'Rabbit\'s Foot', num = 160 } },
				{ item = 'Enchanted Rabbit Hide', exp = '32 Farming', from = { item = 'Rabbit Hide', num = 160 } }, -- exp not tested
			},
		},
		recipes = {
			['Enchanted Raw Rabbit'] = { {'Raw Rabbit', 160 } },
			['Enchanted Cooked Rabbit'] = { {'Enchanted Raw Rabbit', 160 } },
		},
		stats = {
			{ tba = 26, storage = 192, crafting = { item = 'Raw Rabbit', num = 8, B2 = 'Wooden Sword' } },
			{ tba = 26, storage = 320, crafting = { item = 'Raw Rabbit', num = 16 } },
			{ tba = 24, storage = 320, crafting = { item = 'Raw Rabbit', num = 32 } },
			{ tba = 24, storage = 448, crafting = { item = 'Raw Rabbit', num = 64 } },
			{ tba = 22, storage = 448, crafting = { item = 'Enchanted Raw Rabbit', num = 1 } },
			{ tba = 22, storage = 576, crafting = { item = 'Enchanted Raw Rabbit', num = 3 } },
			{ tba = 20, storage = 576, crafting = { item = 'Enchanted Raw Rabbit', num = 8 } },
			{ tba = 20, storage = 768, crafting = { item = 'Enchanted Raw Rabbit', num = 16 } },
			{ tba = 17, storage = 768, crafting = { item = 'Enchanted Raw Rabbit', num = 32 } },
			{ tba = 17, storage = 960, crafting = { item = 'Enchanted Raw Rabbit', num = 64 } },
			{ tba = 13, storage = 960, crafting = { item = 'Enchanted Cooked Rabbit', num = 1 } },
			{ tba = 10, storage = 960, trade = {
				{ item = 'Enchanted Cooked Rabbit', num = 16 },
				{ item = 'Pelt', num = 75 },
			}, tradeNpc = 'Tony' },
		},
		description = '&7Place this minion and it will/&7start generating and slaying/&7Rabbits! Minions also work when/&7you are offline!'
	},
	['Nether Wart'] = {
		type = 'Farming',
		collection = 'Nether Wart I',
		items = {
			{ item = 'Nether Wart', avg = 2.5, exp = 0.2 },
		},
		drops = {
			none = {
				{ item = 'Nether Wart', avg = 2.5, exp = '0.2 Alchemy' },
			},
			sc3000 = {
				{ item = 'Enchanted Nether Wart', exp = '48 Alchemy', from = { item = 'Nether Wart', num = 160 } }, -- exp not tested
				{ item = 'Mutant Nether Wart', exp = '7680 Alchemy', from = { item = 'Enchanted Nether Wart', num = 160 } }, -- exp not tested
			},
		},
		recipes = {
			['Enchanted Nether Wart'] = { {'Nether Wart', 160 } },
			['Mutant Nether Wart'] = { {'Enchanted Nether Wart', 160 } },
		},
		stats = {
			{ tba = 50, storage = 64, crafting = { item = 'Nether Wart', num = 10, B2 = 'Wooden Hoe' } },
			{ tba = 50, storage = 192, crafting = { item = 'Nether Wart', num = 20 } },
			{ tba = 47, storage = 192, crafting = { item = 'Nether Wart', num = 40 } },
			{ tba = 47, storage = 384, crafting = { item = 'Nether Wart', num = 64 } },
			{ tba = 44, storage = 384, crafting = { item = 'Enchanted Nether Wart', num = 1 } },
			{ tba = 44, storage = 576, crafting = { item = 'Enchanted Nether Wart', num = 2 } },
			{ tba = 41, storage = 576, crafting = { item = 'Enchanted Nether Wart', num = 4 } },
			{ tba = 41, storage = 768, crafting = { item = 'Enchanted Nether Wart', num = 8 } },
			{ tba = 38, storage = 768, crafting = { item = 'Enchanted Nether Wart', num = 16 } },
			{ tba = 38, storage = 960, crafting = { item = 'Enchanted Nether Wart', num = 32 } },
			{ tba = 32, storage = 960, crafting = { item = 'Enchanted Nether Wart', num = 64 } },
			{ tba = 27, storage = 960, trade = {
				{ item = 'Enchanted Nether Wart', num = 1024 },
				{ item = 'Pelt', num = 75 },
			}, tradeNpc = 'Tony' },
		},
		description = '&7Place this minion and it will/&7start generating and harvesting/&7cocoa beans. Requires soul sand/&7nearby so nether warts can be/&7planted. Minions also work when/&7you are offline!'
	},
	--------------------------------
	-- Mining
	--------------------------------
	['Cobblestone'] = {
		type = 'Mining',
		collection = 'Cobblestone I',
		items = {
			{ item = 'Cobblestone', avg = 1, exp = 0.1 },
		},
		drops = {
			none = {
				{ item = 'Cobblestone', avg = 1, exp = '0.1 Mining' },
			},
			smelter = {
				{ item = 'Stone', exp = '0.1 Mining', from = { item = 'Cobblestone', num = 1 } },
			},
			sc3000 = {
				{ item = 'Enchanted Cobblestone', exp = '16 Mining', from = { item = 'Cobblestone', num = 160 } },
			},
		},
		recipes = {
			['Enchanted Cobblestone'] = { {'Cobblestone', 160 } },
		},
		stats = {
			{ tba = 14, storage = 64, crafting = { item = 'Cobblestone', num = 10, B2 = 'Wooden Pickaxe' } },
			{ tba = 14, storage = 192, crafting = { item = 'Cobblestone', num = 20 } },
			{ tba = 12, storage = 192, crafting = { item = 'Cobblestone', num = 40 } },
			{ tba = 12, storage = 384, crafting = { item = 'Cobblestone', num = 64 } },
			{ tba = 10, storage = 384, crafting = { item = 'Enchanted Cobblestone', num = 1 } },
			{ tba = 10, storage = 576, crafting = { item = 'Enchanted Cobblestone', num = 2 } },
			{ tba = 9, storage = 576, crafting = { item = 'Enchanted Cobblestone', num = 4 } },
			{ tba = 9, storage = 768, crafting = { item = 'Enchanted Cobblestone', num = 8 } },
			{ tba = 8, storage = 768, crafting = { item = 'Enchanted Cobblestone', num = 16 } },
			{ tba = 8, storage = 960, crafting = { item = 'Enchanted Cobblestone', num = 32 } },
			{ tba = 7, storage = 960, crafting = { item = 'Enchanted Cobblestone', num = 64 } },
			{ tba = 6, storage = 960, trade = {
				{ item = 'Enchanted Cobblestone', num = 1024 },
				{ item = 'Coin', num = 2000000 },
			}, tradeNpc = 'Bulvar' },
		},
		description = '&7Place this minion and it will/&7start generating and mining/&7cobblestone! Requires an open/&7area to place cobblestone./&7Minions also work when you are/&7offline!'
	},
	['Coal'] = {
		type = 'Mining',
		collection = 'Coal I',
		items = {
			{ item = 'Coal', avg = 1, exp = 0.3 },
		},
		drops = {
			none = {
				{ item = 'Coal', avg = 1, exp = '0.3 Mining' },
			},
			compactor = {
				{ item = 'Block of Coal', exp = '2.7 Mining', from = { item = 'Coal', num = 9 } },
			},
			sc3000 = {
				{ item = 'Enchanted Coal', exp = '48 Mining', from = { item = 'Coal', num = 160 } },
				{ item = 'Enchanted Coal Block', exp = '7680 Mining', from = { item = 'Enchanted Coal', num = 160 } },
			},
		},
		recipes = {
			['Enchanted Coal'] = { {'Coal', 160 } },
			['Enchanted Coal Block'] = { {'Enchanted Coal', 160 } },
		},
		stats = {
			{ tba = 15, storage = 64, crafting = { item = 'Coal', num = 10, B2 = 'Wooden Pickaxe' } },
			{ tba = 15, storage = 192, crafting = { item = 'Coal', num = 20 } },
			{ tba = 13, storage = 192, crafting = { item = 'Coal', num = 40 } },
			{ tba = 13, storage = 384, crafting = { item = 'Coal', num = 64 } },
			{ tba = 12, storage = 384, crafting = { item = 'Enchanted Coal', num = 1 } },
			{ tba = 12, storage = 576, crafting = { item = 'Enchanted Coal', num = 3 } },
			{ tba = 10, storage = 576, crafting = { item = 'Enchanted Coal', num = 8 } },
			{ tba = 10, storage = 768, crafting = { item = 'Enchanted Coal', num = 16 } },
			{ tba = 9, storage = 768, crafting = { item = 'Enchanted Coal', num = 32 } },
			{ tba = 9, storage = 960, crafting = { item = 'Enchanted Coal', num = 64 } },
			{ tba = 7, storage = 960, crafting = { item = 'Enchanted Coal Block', num = 1 } },
			{ tba = 6, storage = 960, trade = {
				{ item = 'Enchanted Coal Block', num = 16 },
				{ item = 'Coin', num = 2000000 },
			}, tradeNpc = 'Bulvar' },
		},
		description = '&7Place this minion and it will/&7start generating and mining coal/&7ore! Requires an open area to/&7place coal ore. Minions also/&7work when you are offline!'
	},
	['Iron'] = {
		type = 'Mining',
		collection = 'Iron Ingot I',
		items = {
			{ item = 'Iron Ore', avg = 1, exp = 0.3 },
			{ item = 'Iron Ingot', avg = 1, condition = 'Auto Smelter', converts = 'Iron Ore', exp = 0.3 },
		},
		drops = {
			none = {
				{ item = 'Iron Ore', avg = 1, exp = '0.3 Mining' },
			},
			smelter = {
				{ item = 'Iron Ingot', exp = '0.3 Mining', from = { item = 'Iron Ore', num = 1 } },
			},
			smelter_compactor = {
				{ item = 'Block of Iron', exp = '2.7 Mining', from = { item = 'Iron Ingot', num = 9 } },
			},
			smelter_sc3000 = {
				{ item = 'Enchanted Iron Ingot', exp = '48 Mining', from = { item = 'Iron Ingot', num = 160 } },
				{ item = 'Enchanted Iron Block', exp = '7680 Mining', from = { item = 'Enchanted Iron Ingot', num = 160 } },
			},
		},
		recipes = {
			['Enchanted Iron Ingot'] = { {'Iron Ingot', 160 } },
			['Enchanted Iron Block'] = { {'Enchanted Iron Ingot', 160 } },
		},
		stats = {
			{ tba = 17, storage = 64, crafting = { item = 'Iron Ingot', num = 10, B2 = 'Wooden Pickaxe' } },
			{ tba = 17, storage = 192, crafting = { item = 'Iron Ingot', num = 20 } },
			{ tba = 15, storage = 192, crafting = { item = 'Iron Ingot', num = 40 } },
			{ tba = 15, storage = 384, crafting = { item = 'Iron Ingot', num = 64 } },
			{ tba = 14, storage = 384, crafting = { item = 'Enchanted Iron Ingot', num = 1 } },
			{ tba = 14, storage = 576, crafting = { item = 'Enchanted Iron Ingot', num = 3 } },
			{ tba = 12, storage = 576, crafting = { item = 'Enchanted Iron Ingot', num = 8 } },
			{ tba = 12, storage = 768, crafting = { item = 'Enchanted Iron Ingot', num = 16 } },
			{ tba = 10, storage = 768, crafting = { item = 'Enchanted Iron Ingot', num = 32 } },
			{ tba = 10, storage = 960, crafting = { item = 'Enchanted Iron Ingot', num = 64 } },
			{ tba = 8, storage = 960, crafting = { item = 'Enchanted Iron Block', num = 1 } },
			{ tba = 7, storage = 960, trade = {
				{ item = 'Enchanted Iron Block', num = 16 },
				{ item = 'Coin', num = 2000000 },
			}, tradeNpc = 'Bulvar' },
		},
		description = '&7Place this minion and it will/&7start generating and mining iron/&7ore! Requires an open area to/&7place iron ore. Minions also/&7work when you are offline!'
	},
	['Gold'] = {
		type = 'Mining',
		collection = 'Gold Ingot I',
		items = {
			{ item = 'Gold Ore', avg = 1, exp = 0.4 },
			{ item = 'Gold Ingot', avg = 1, condition = 'Auto Smelter', converts = 'Gold Ore', exp = 0.4 },
		},
		drops = {
			none = {
				{ item = 'Gold Ore', avg = 1, exp = '0.4 Mining' },
			},
			smelter = {
				{ item = 'Gold Ingot', exp = '0.4 Mining', from = { item = 'Gold Ore', num = 1 } },
			},
			smelter_compactor = {
				{ item = 'Block of Gold', exp = '3.6 Mining', from = { item = 'Gold Ingot', num = 9 } },
			},
			smelter_sc3000 = {
				{ item = 'Enchanted Gold Ingot', exp = '64 Mining', from = { item = 'Gold Ingot', num = 160 } },
				{ item = 'Enchanted Gold Block', exp = '10240 Mining', from = { item = 'Enchanted Gold Ingot', num = 160 } },
			},
		},
		recipes = {
			['Enchanted Gold Ingot'] = { {'Gold Ingot', 160 } },
			['Enchanted Gold Block'] = { {'Enchanted Gold Ingot', 160 } },
		},
		stats = {
			{ tba = 22, storage = 64, crafting = { item = 'Gold Ingot', num = 10, B2 = 'Wooden Pickaxe' } },
			{ tba = 22, storage = 192, crafting = { item = 'Gold Ingot', num = 20 } },
			{ tba = 20, storage = 192, crafting = { item = 'Gold Ingot', num = 40 } },
			{ tba = 20, storage = 384, crafting = { item = 'Gold Ingot', num = 64 } },
			{ tba = 18, storage = 384, crafting = { item = 'Enchanted Gold Ingot', num = 1 } },
			{ tba = 18, storage = 576, crafting = { item = 'Enchanted Gold Ingot', num = 3 } },
			{ tba = 16, storage = 576, crafting = { item = 'Enchanted Gold Ingot', num = 8 } },
			{ tba = 16, storage = 768, crafting = { item = 'Enchanted Gold Ingot', num = 16 } },
			{ tba = 14, storage = 768, crafting = { item = 'Enchanted Gold Ingot', num = 32 } },
			{ tba = 14, storage = 960, crafting = { item = 'Enchanted Gold Ingot', num = 64 } },
			{ tba = 11, storage = 960, crafting = { item = 'Enchanted Gold Block', num = 1 } },
			{ tba = 9, storage = 960, trade = {
				{ item = 'Enchanted Gold Block', num = 16 },
				{ item = 'Coin', num = 2000000 },
			}, tradeNpc = 'Bulvar' },
		},
		description = '&7Place this minion and it will/&7start generating and mining gold/&7ore! Requires an open area to/&7place gold ore. Minions also/&7work when you are offline!'
	},
	['Diamond'] = {
		type = 'Mining',
		collection = 'Diamond I',
		items = {
			{ item = 'Diamond', avg = 1, exp = 0.4 },
		},
		drops = {
			none = {
				{ item = 'Diamond', avg = 1, exp = '0.4 Mining' },
			},
			compactor = {
				{ item = 'Block of Diamond', exp = '3.6 Mining', from = { item = 'Diamond', num = 9 } },
			},
			sc3000 = {
				{ item = 'Enchanted Diamond', exp = '64 Mining', from = { item = 'Diamond', num = 160 } },
				{ item = 'Enchanted Diamond Block', exp = '10240 Mining', from = { item = 'Enchanted Diamond', num = 160 } },
			},
		},
		recipes = {
			['Enchanted Diamond'] = { {'Diamond', 160 } },
			['Enchanted Diamond Block'] = { {'Enchanted Diamond', 160 } },
		},
		stats = {
			{ tba = 29, storage = 64, crafting = { item = 'Diamond', num = 10, B2 = 'Wooden Pickaxe' } },
			{ tba = 29, storage = 192, crafting = { item = 'Diamond', num = 20 } },
			{ tba = 27, storage = 192, crafting = { item = 'Diamond', num = 40 } },
			{ tba = 27, storage = 384, crafting = { item = 'Diamond', num = 64 } },
			{ tba = 25, storage = 384, crafting = { item = 'Enchanted Diamond', num = 1 } },
			{ tba = 25, storage = 576, crafting = { item = 'Enchanted Diamond', num = 3 } },
			{ tba = 22, storage = 576, crafting = { item = 'Enchanted Diamond', num = 8 } },
			{ tba = 22, storage = 768, crafting = { item = 'Enchanted Diamond', num = 16 } },
			{ tba = 19, storage = 768, crafting = { item = 'Enchanted Diamond', num = 32 } },
			{ tba = 19, storage = 960, crafting = { item = 'Enchanted Diamond', num = 64 } },
			{ tba = 15, storage = 960, crafting = { item = 'Enchanted Diamond Block', num = 1 } },
			{ tba = 12, storage = 960, trade = {
				{ item = 'Enchanted Diamond Block', num = 16 },
				{ item = 'Coin', num = 2000000 },
			}, tradeNpc = 'Bulvar' },
		},
		description = '&7Place this minion and it will/&7start generating and mining/&7diamond ore! Requires an open/&7area to place diamond ore./&7Minions also work when you are/&7offline!'
	},
	['Lapis'] = {
		type = 'Mining',
		collection = 'Lapis Lazuli I',
		items = {
			{ item = 'Lapis Lazuli', avg = 6, exp = 0.1 },
		},
		drops = {
			none = {
				{ item = 'Lapis Lazuli', avg = 6, exp = '0.1 Mining' }, -- avg not tested
			},
			compactor = {
				{ item = 'Block of Lapis Lazuli', exp = '0.9 Mining', from = { item = 'Lapis Lazuli', num = 9 } },
			},
			sc3000 = {
				{ item = 'Enchanted Lapis Lazuli', exp = '16 Mining', from = { item = 'Lapis Lazuli', num = 160 } },
				{ item = 'Enchanted Lapis Lazuli Block', exp = '2560 Mining', from = { item = 'Enchanted Lapis Lazuli', num = 160 } },
			},
		},
		recipes = {
			['Enchanted Lapis Lazuli'] = { {'Lapis Lazuli', 160 } },
			['Enchanted Lapis Lazuli Block'] = { {'Enchanted Lapis Lazuli', 160 } },
		},
		stats = {
			{ tba = 29, storage = 64, crafting = { item = 'Lapis Lazuli', num = 32, B2 = 'Wooden Pickaxe' } },
			{ tba = 29, storage = 192, crafting = { item = 'Lapis Lazuli', num = 64 } },
			{ tba = 27, storage = 192, crafting = { item = 'Enchanted Lapis Lazuli', num = 1 } },
			{ tba = 27, storage = 384, crafting = { item = 'Enchanted Lapis Lazuli', num = 3 } },
			{ tba = 25, storage = 384, crafting = { item = 'Enchanted Lapis Lazuli', num = 8 } },
			{ tba = 25, storage = 576, crafting = { item = 'Enchanted Lapis Lazuli', num = 16 } },
			{ tba = 23, storage = 576, crafting = { item = 'Enchanted Lapis Lazuli', num = 32 } },
			{ tba = 23, storage = 768, crafting = { item = 'Enchanted Lapis Lazuli', num = 64 } },
			{ tba = 21, storage = 768, crafting = { item = 'Enchanted Lapis Lazuli Block', num = 1 } },
			{ tba = 21, storage = 960, crafting = { item = 'Enchanted Lapis Lazuli Block', num = 2 } },
			{ tba = 18, storage = 960, crafting = { item = 'Enchanted Lapis Lazuli Block', num = 4 } },
			{ tba = 16, storage = 960, trade = {
				{ item = 'Enchanted Lapis Lazuli Block', num = 64 },
				{ item = 'Coin', num = 2000000 },
			}, tradeNpc = 'Bulvar' },
		},
		description = '&7Place this minion and it will/&7start generating and mining/&7lapis ore! Requires an open area/&7to place lapis ore. Minions also/&7work when you are offline!'
	},
	['Emerald'] = {
		type = 'Mining',
		collection = 'Emerald I',
		items = {
			{ item = 'Emerald', avg = 1, exp = 0.4 },
		},
		drops = {
			none = {
				{ item = 'Emerald', avg = 1, exp = '0.4 Mining' },
			},
			compactor = {
				{ item = 'Block of Emerald', exp = '3.6 Mining', from = { item = 'Emerald', num = 9 } },
			},
			sc3000 = {
				{ item = 'Enchanted Emerald', exp = '64 Mining', from = { item = 'Emerald', num = 160 } },
				{ item = 'Enchanted Emerald Block', exp = '10240 Mining', from = { item = 'Enchanted Emerald', num = 160 } },
			},
		},
		recipes = {
			['Enchanted Emerald'] = { {'Emerald', 160 } },
			['Enchanted Emerald Block'] = { {'Enchanted Emerald', 160 } },
		},
		stats = {
			{ tba = 28, storage = 64, crafting = { item = 'Emerald', num = 10, B2 = 'Wooden Pickaxe' } },
			{ tba = 28, storage = 192, crafting = { item = 'Emerald', num = 20 } },
			{ tba = 26, storage = 192, crafting = { item = 'Emerald', num = 40 } },
			{ tba = 26, storage = 384, crafting = { item = 'Emerald', num = 64 } },
			{ tba = 24, storage = 384, crafting = { item = 'Enchanted Emerald', num = 1 } },
			{ tba = 24, storage = 576, crafting = { item = 'Enchanted Emerald', num = 3 } },
			{ tba = 21, storage = 576, crafting = { item = 'Enchanted Emerald', num = 8 } },
			{ tba = 21, storage = 768, crafting = { item = 'Enchanted Emerald', num = 16 } },
			{ tba = 18, storage = 768, crafting = { item = 'Enchanted Emerald', num = 32 } },
			{ tba = 18, storage = 960, crafting = { item = 'Enchanted Emerald', num = 64 } },
			{ tba = 14, storage = 960, crafting = { item = 'Enchanted Emerald Block', num = 1 } },
			{ tba = 12, storage = 960, trade = {
				{ item = 'Enchanted Emerald Block', num = 16 },
				{ item = 'Coin', num = 2000000 },
			}, tradeNpc = 'Bulvar' },
		},
		description = '&7Place this minion and it will/&7start generating and mining/&7emerald ore! Requires an open/&7area to place emerald ore./&7Minions also work when you are/&7offline!'
	},
	['Redstone'] = {
		type = 'Mining',
		collection = 'Redstone Dust I',
		items = {
			{ item = 'Redstone Dust', avg = 4.5, exp = 0.2 },
		},
		drops = {
			none = {
				{ item = 'Redstone Dust', avg = 4.5, exp = '0.2 Mining' },
			},
			compactor = {
				{ item = 'Block of Redstone', exp = '1.8 Mining', from = { item = 'Redstone Dust', num = 9 } },
			},
			sc3000 = {
				{ item = 'Enchanted Redstone Dust', exp = '32 Mining', from = { item = 'Redstone Dust', num = 160 } },
				{ item = 'Enchanted Redstone Block', exp = '5120 Mining', from = { item = 'Enchanted Redstone Dust', num = 160 } },
			},
		},
		recipes = {
			['Enchanted Redstone Dust'] = { {'Redstone Dust', 160 } },
			['Enchanted Redstone Block'] = { {'Enchanted Redstone Dust', 160 } },
		},
		stats = {
			{ tba = 29, storage = 64, crafting = { item = 'Redstone Dust', num = 16, B2 = 'Wooden Pickaxe' } },
			{ tba = 29, storage = 192, crafting = { item = 'Redstone Dust', num = 32 } },
			{ tba = 27, storage = 192, crafting = { item = 'Redstone Dust', num = 64 } },
			{ tba = 27, storage = 384, crafting = { item = 'Enchanted Redstone Dust', num = 1 } },
			{ tba = 25, storage = 384, crafting = { item = 'Enchanted Redstone Dust', num = 3 } },
			{ tba = 25, storage = 576, crafting = { item = 'Enchanted Redstone Dust', num = 8 } },
			{ tba = 23, storage = 576, crafting = { item = 'Enchanted Redstone Dust', num = 16 } },
			{ tba = 23, storage = 768, crafting = { item = 'Enchanted Redstone Dust', num = 32 } },
			{ tba = 21, storage = 768, crafting = { item = 'Enchanted Redstone Dust', num = 64 } },
			{ tba = 21, storage = 960, crafting = { item = 'Enchanted Redstone Block', num = 1 } },
			{ tba = 18, storage = 960, crafting = { item = 'Enchanted Redstone Block', num = 2 } },
			{ tba = 16, storage = 960, trade = {
				{ item = 'Enchanted Redstone Block', num = 32 },
				{ item = 'Coin', num = 2000000 },
			}, tradeNpc = 'Bulvar' },
		},
		description = '&7Place this minion and it will/&7start generating and mining/&7redstone ore! Requires an open/&7area to place redstone ore./&7Minions also work when you are/&7offline!'
	},
	['Quartz'] = {
		type = 'Mining',
		collection = 'Nether Quartz I',
		items = {
			{ item = 'Nether Quartz', avg = 1, exp = 0.3 },
		},
		drops = {
			none = {
				{ item = 'Nether Quartz', avg = 1, exp = '0.3 Mining' },
			},
			compactor = {
				{ item = 'Block of Quartz', exp = '1.2 Mining', from = { item = 'Nether Quartz', num = 4 } },
			},
			sc3000 = {
				{ item = 'Enchanted Nether Quartz', exp = '48 Mining', from = { item = 'Nether Quartz', num = 160 } },
				{ item = 'Enchanted Quartz Block', exp = '7680 Mining', from = { item = 'Enchanted Nether Quartz', num = 160 } },
			},
		},
		recipes = {
			['Enchanted Nether Quartz'] = { {'Nether Quartz', 160 } },
			['Enchanted Quartz Block'] = { {'Enchanted Nether Quartz', 160 } },
		},
		stats = {
			{ tba = 22.5, storage = 64, crafting = { item = 'Nether Quartz', num = 10, B2 = 'Wooden Pickaxe' } },
			{ tba = 22.5, storage = 192, crafting = { item = 'Nether Quartz', num = 20 } },
			{ tba = 21, storage = 192, crafting = { item = 'Nether Quartz', num = 40 } },
			{ tba = 21, storage = 384, crafting = { item = 'Nether Quartz', num = 64 } },
			{ tba = 19, storage = 384, crafting = { item = 'Enchanted Nether Quartz', num = 1 } },
			{ tba = 19, storage = 576, crafting = { item = 'Enchanted Nether Quartz', num = 3 } },
			{ tba = 17, storage = 576, crafting = { item = 'Enchanted Nether Quartz', num = 8 } },
			{ tba = 17, storage = 768, crafting = { item = 'Enchanted Nether Quartz', num = 16 } },
			{ tba = 14.5, storage = 768, crafting = { item = 'Enchanted Nether Quartz', num = 32 } },
			{ tba = 14.5, storage = 960, crafting = { item = 'Enchanted Nether Quartz', num = 64 } },
			{ tba = 11.5, storage = 960, crafting = { item = 'Enchanted Quartz Block', num = 1 } },
			{ tba = 10, storage = 960, trade = {
				{ item = 'Enchanted Quartz Block', num = 16 },
				{ item = 'Coin', num = 2000000 },
			}, tradeNpc = {'Hilda', 'Marthos'} },
		},
		description = '&7Place this minion and it will/&7start generating and mining/&7quartz ore! Requires an open/&7area to place quartz ore./&7Minions also work when you are/&7offline!'
	},
	['Obsidian'] = {
		type = 'Mining',
		collection = 'Obsidian I',
		items = {
			{ item = 'Obsidian', avg = 1, exp = 0.4 },
		},
		drops = {
			none = {
				{ item = 'Obsidian', avg = 1, exp = '0.4 Mining' },
			},
			sc3000 = {
				{ item = 'Enchanted Obsidian', exp = '64 Mining', from = { item = 'Obsidian', num = 160 } },
			},
		},
		recipes = {
			['Enchanted Obsidian'] = { {'Obsidian', 160 } },
		},
		stats = {
			{ tba = 45, storage = 64, crafting = { item = 'Obsidian', num = 10, B2 = 'Wooden Pickaxe' } },
			{ tba = 45, storage = 192, crafting = { item = 'Obsidian', num = 20 } },
			{ tba = 42, storage = 192, crafting = { item = 'Obsidian', num = 40 } },
			{ tba = 42, storage = 384, crafting = { item = 'Obsidian', num = 64 } },
			{ tba = 39, storage = 384, crafting = { item = 'Enchanted Obsidian', num = 1 } },
			{ tba = 39, storage = 576, crafting = { item = 'Enchanted Obsidian', num = 2 } },
			{ tba = 35, storage = 576, crafting = { item = 'Enchanted Obsidian', num = 4 } },
			{ tba = 35, storage = 768, crafting = { item = 'Enchanted Obsidian', num = 8 } },
			{ tba = 30, storage = 768, crafting = { item = 'Enchanted Obsidian', num = 16 } },
			{ tba = 30, storage = 960, crafting = { item = 'Enchanted Obsidian', num = 32 } },
			{ tba = 24, storage = 960, crafting = { item = 'Enchanted Obsidian', num = 64 } },
			{ tba = 21, storage = 960, trade = {
				{ item = 'Enchanted Obsidian', num = 1024 },
				{ item = 'Coin', num = 2000000 },
			}, tradeNpc = 'Bulvar' },
		},
		description = '&7Place this minion and it will/&7start generating and mining/&7obsidian! Requires an open area/&7to place obsidian. Minions also/&7work when you are offline!'
	},
	['Glowstone'] = {
		type = 'Mining',
		collection = 'Glowstone Dust I',
		items = {
			{ item = 'Glowstone Dust', avg = 3, exp = 0.2 },
		},
		drops = {
			none = {
				{ item = 'Glowstone Dust', avg = 3, exp = '0.2 Mining' },
			},
			compactor = {
				{ item = 'Glowstone', exp = '0.8 Mining', from = { item = 'Glowstone Dust', num = 4 } },
			},
			sc3000 = {
				{ item = 'Enchanted Glowstone Dust', exp = '32 Mining', from = { item = 'Glowstone Dust', num = 160 } },
				{ item = 'Enchanted Glowstone', exp = '6144 Mining', from = { item = 'Enchanted Glowstone Dust', num = 192 } },
			},
		},
		recipes = {
			['Enchanted Glowstone Dust'] = { {'Glowstone Dust', 160 } },
			['Enchanted Glowstone'] = { {'Enchanted Glowstone Dust', 192 } },
		},
		stats = {
			{ tba = 25, storage = 64, crafting = { item = 'Glowstone Dust', num = 16, B2 = 'Wooden Pickaxe' } },
			{ tba = 25, storage = 192, crafting = { item = 'Glowstone Dust', num = 32 } },
			{ tba = 23, storage = 192, crafting = { item = 'Glowstone Dust', num = 64 } },
			{ tba = 23, storage = 384, crafting = { item = 'Enchanted Glowstone Dust', num = 1 } },
			{ tba = 21, storage = 384, crafting = { item = 'Enchanted Glowstone Dust', num = 3 } },
			{ tba = 21, storage = 576, crafting = { item = 'Enchanted Glowstone Dust', num = 8 } },
			{ tba = 19, storage = 576, crafting = { item = 'Enchanted Glowstone Dust', num = 16 } },
			{ tba = 19, storage = 768, crafting = { item = 'Enchanted Glowstone Dust', num = 32 } },
			{ tba = 16, storage = 768, crafting = { item = 'Enchanted Glowstone Dust', num = 64 } },
			{ tba = 16, storage = 960, crafting = { item = 'Enchanted Glowstone', num = 1 } },
			{ tba = 13, storage = 960, crafting = { item = 'Enchanted Glowstone', num = 2 } },
			{ tba = 11, storage = 960, trade = {
				{ item = 'Enchanted Glowstone', num = 32 },
				{ item = 'Coin', num = 2000000 },
			}, tradeNpc = {'Hilda', 'Marthos'} },
		},
		description = '&7Place this minion and it will/&7start generating and mining/&7glowstone! Requires an open area/&7to place glowstone. Minions also/&7work when you are offline!'
	},
	['Gravel'] = {
		type = 'Mining',
		collection = 'Gravel I',
		items = {
			{ item = 'Gravel', avg = 1, exp = 0.2 },
			{ item = 'Flint', avg = 1, condition = 'Flint Shovel', converts = 'Gravel', exp = 0.2 },
		},
		drops = {
			none = {
				{ item = 'Gravel', avg = 1, exp = '0.2 Mining' },
			},
			flintshovel = {
				{ item = 'Flint', exp = '0.2 Mining', from = { item = 'Gravel', num = 1 } },
			},
			flintshovel_sc3000 = {
				{ item = 'Enchanted Flint', exp = '32 Mining', from = { item = 'Flint', num = 160 } },
			},
		},
		recipes = {
			['Enchanted Flint'] = { {'Flint', 160 } },
		},
		stats = {
			{ tba = 26, storage = 128, crafting = { item = 'Gravel', num = 10, B2 = 'Wooden Shovel' } },
			{ tba = 26, storage = 256, crafting = { item = 'Gravel', num = 20 } },
			{ tba = 24, storage = 256, crafting = { item = 'Gravel', num = 40 } },
			{ tba = 24, storage = 384, crafting = { item = 'Gravel', num = 64 } },
			{ tba = 22, storage = 384, crafting = { item = 'Enchanted Flint', num = 1 } },
			{ tba = 22, storage = 576, crafting = { item = 'Enchanted Flint', num = 2 } },
			{ tba = 19, storage = 576, crafting = { item = 'Enchanted Flint', num = 4 } },
			{ tba = 19, storage = 768, crafting = { item = 'Enchanted Flint', num = 8 } },
			{ tba = 16, storage = 768, crafting = { item = 'Enchanted Flint', num = 16 } },
			{ tba = 16, storage = 960, crafting = { item = 'Enchanted Flint', num = 32 } },
			{ tba = 13, storage = 960, crafting = { item = 'Enchanted Flint', num = 64 } },
		},
		description = '&7Place this minion and it will/&7start generating and mining/&7gravel! Requires an open area to/&7place gravel. Minions also work/&7when you are offline!'
	},
	['Ice'] = {
		type = 'Mining',
		collection = 'Ice I',
		items = {
			{ item = 'Ice', avg = 1, exp = 0.5 },
		},
		drops = {
			none = {
				{ item = 'Ice', avg = 1, exp = '0.5 Mining' },
			},
			compactor = {
				{ item = 'Packed Ice', exp = '4.5 Mining', from = { item = 'Ice', num = 9 } },
			},
			sc3000 = {
				{ item = 'Enchanted Ice', exp = '80 Mining', from = { item = 'Ice', num = 160 } },
				{ item = 'Enchanted Packed Ice', exp = '12800 Mining', from = { item = 'Enchanted Ice', num = 160 } },
			},
		},
		recipes = {
			['Packed Ice'] = { {'Ice', 9 } },
			['Enchanted Ice'] = { {'Ice', 160 } },
			['Enchanted Packed Ice'] = { {'Enchanted Ice', 160 } },
		},
		stats = {
			{ tba = 14, storage = 64, crafting = { item = 'Ice', num = 10, B2 = 'Wooden Pickaxe' } },
			{ tba = 14, storage = 192, crafting = { item = 'Ice', num = 20 } },
			{ tba = 12, storage = 192, crafting = { item = 'Ice', num = 40 } },
			{ tba = 12, storage = 384, crafting = { item = 'Ice', num = 64 } },
			{ tba = 10, storage = 384, crafting = { item = 'Packed Ice', num = 16 } },
			{ tba = 10, storage = 576, crafting = { item = 'Packed Ice', num = 32 } },
			{ tba = 9, storage = 576, crafting = { item = 'Packed Ice', num = 64 } },
			{ tba = 9, storage = 768, crafting = { item = 'Enchanted Ice', num = 8 } },
			{ tba = 8, storage = 768, crafting = { item = 'Enchanted Ice', num = 16 } },
			{ tba = 8, storage = 960, crafting = { item = 'Enchanted Ice', num = 32 } },
			{ tba = 7, storage = 960, crafting = { item = 'Enchanted Ice', num = 64 } },
			{ tba = 6, storage = 960, trade = {
				{ item = 'Enchanted Ice', num = 1024 },
				{ item = 'Coin', num = 1000000 },
				{ item = 'North Star', num = 300 },
			}, tradeNpc = 'Einary' }, 
		},
		description = '&7Place this minion and it will/&7start generating and mining ice!/&7Requires an open area to place/&7ice. Minions also work when you/&7are offline!'
	},
	['Sand'] = {
		type = 'Mining',
		collection = 'Sand I',
		items = {
			{ item = 'Sand', avg = 1, exp = 0.2 },
		},
		drops = {
			none = {
				{ item = 'Sand', avg = 1, exp = '0.2 Mining' },
			},
			smelter = {
				{ item = 'Glass', exp = nil, from = { item = 'Sand', num = 1 } },
			},
			sc3000 = {
				{ item = 'Enchanted Sand', exp = '32 Mining', from = { item = 'Sand', num = 160 } },
			},
		},
		recipes = {
			['Enchanted Sand'] = { {'Sand', 160 } },
		},
		stats = {
			{ tba = 26, storage = 64, crafting = { item = 'Sand', num = 10, B2 = 'Wooden Shovel' } },
			{ tba = 26, storage = 192, crafting = { item = 'Sand', num = 20 } },
			{ tba = 24, storage = 192, crafting = { item = 'Sand', num = 40 } },
			{ tba = 24, storage = 384, crafting = { item = 'Sand', num = 64 } },
			{ tba = 22, storage = 384, crafting = { item = 'Enchanted Sand', num = 1 } },
			{ tba = 22, storage = 576, crafting = { item = 'Enchanted Sand', num = 2 } },
			{ tba = 19, storage = 576, crafting = { item = 'Enchanted Sand', num = 4 } },
			{ tba = 19, storage = 768, crafting = { item = 'Enchanted Sand', num = 8 } },
			{ tba = 16, storage = 768, crafting = { item = 'Enchanted Sand', num = 16 } },
			{ tba = 16, storage = 960, crafting = { item = 'Enchanted Sand', num = 32 } },
			{ tba = 13, storage = 960, crafting = { item = 'Enchanted Sand', num = 64 } },
		},
		description = '&7Place this minion and it will/&7start generating and mining/&7sand! Requires an open area to/&7place sand. Minions also work/&7when you are offline!'
	},
	['End Stone'] = {
		type = 'Mining',
		collection = 'End Stone I',
		items = {
			{ item = 'End Stone', avg = 1, exp = 0.4 },
		},
		drops = {
			none = {
				{ item = 'End Stone', avg = 1, exp = '0.4 Mining' },
			},
			sc3000 = {
				{ item = 'Enchanted End Stone', exp = '64 Mining', from = { item = 'End Stone', num = 160 } },
			},
		},
		recipes = {
			['Enchanted End Stone'] = { {'End Stone', 160 } },
		},
		stats = {
			{ tba = 26, storage = 64, crafting = { item = 'End Stone', num = 10, B2 = 'Wooden Pickaxe' } },
			{ tba = 26, storage = 192, crafting = { item = 'End Stone', num = 20 } },
			{ tba = 24, storage = 192, crafting = { item = 'End Stone', num = 40 } },
			{ tba = 24, storage = 384, crafting = { item = 'End Stone', num = 64 } },
			{ tba = 22, storage = 384, crafting = { item = 'Enchanted End Stone', num = 1 } },
			{ tba = 22, storage = 576, crafting = { item = 'Enchanted End Stone', num = 2 } },
			{ tba = 19, storage = 576, crafting = { item = 'Enchanted End Stone', num = 4 } },
			{ tba = 19, storage = 768, crafting = { item = 'Enchanted End Stone', num = 8 } },
			{ tba = 16, storage = 768, crafting = { item = 'Enchanted End Stone', num = 16 } },
			{ tba = 16, storage = 960, crafting = { item = 'Enchanted End Stone', num = 32 } },
			{ tba = 13, storage = 960, crafting = { item = 'Enchanted End Stone', num = 64 } },
		},
		description = '&7Place this minion and it will/&7start generating and mining end/&7stone!/&7Requires an open area to/&7place end stone. Minions also/&7work when you are offline!'
	},
	['Mithril'] = {
		type = 'Mining',
		collection = 'Mithril I',
		items = {
			{ item = 'Mithril', avg = 2, exp = 0.4 },
		},
		drops = {
			none = {
				{ item = 'Mithril', avg = 2, exp = '0.4 Mining' },
			},
			sc3000 = {
				{ item = 'Enchanted Mithril', exp = '64 Mining', from = { item = 'Mithril', num = 160 } },
				-- No higher drops - tested
			},
		},
		recipes = {
			['Enchanted Mithril'] = { {'Mithril', 160 } },
			['Refined Mithril'] = { {'Enchanted Mithril', 160 } },
		},
		stats = {
			{ tba = 80, storage = 64, crafting = { item = 'Mithril', num = 10, B2 = 'Wooden Pickaxe' } },
			{ tba = 80, storage = 192, crafting = { item = 'Mithril', num = 20, } },
			{ tba = 75, storage = 192, crafting = { item = 'Mithril', num = 40, } },
			{ tba = 75, storage = 384, crafting = { item = 'Mithril', num = 64, } },
			{ tba = 70, storage = 384, crafting = { item = 'Enchanted Mithril', num = 1, } },
			{ tba = 70, storage = 576, crafting = { item = 'Enchanted Mithril', num = 3, } },
			{ tba = 65, storage = 576, crafting = { item = 'Enchanted Mithril', num = 8, } },
			{ tba = 65, storage = 768, crafting = { item = 'Enchanted Mithril', num = 16, } },
			{ tba = 60, storage = 768, crafting = { item = 'Enchanted Mithril', num = 32, } },
			{ tba = 60, storage = 960, crafting = { item = 'Enchanted Mithril', num = 64, } },
			{ tba = 55, storage = 960, crafting = { item = 'Refined Mithril', num = 1, } },
			{ tba = 50, storage = 960, trade = {
				{ item = 'Refined Mithril', num = 16 },
				{ item = 'Coin', num = 2000000 },
			}, tradeNpc = 'Bulvar' },
		},
		description = '&7Place this minion and it will/&7start generating and mining Mithril!/&7Requires an open area to/&7place Mithril. Minions also/&7work when you are offline!'
	},
	['Hard Stone'] = {
		type = 'Mining',
		collection = 'Hard Stone I',
		items = {
			-- Hard Stone currently gives no mining experience when collected from minions, this might change later
			{ item = 'Hard Stone', avg = 2, exp = 0.0 },
		},
		drops = {
			none = {
				{ item = 'Hard Stone', avg = 2, exp = '0.1 Mining' },
			},
			sc3000 = {
				{ item = 'Enchanted Hard Stone', exp = '57.6 Mining', from = { item = 'Hard Stone', num = 576 } }, -- exp not tested
				{ item = 'Concentrated Stone', exp = '33177.6 Mining', from = { item = 'Enchanted Hard Stone', num = 576 } }, -- drop/exp not tested
			},
		},
		recipes = {
			['Enchanted Hard Stone'] = { {'Hard Stone', 576 } },
			['Concentrated Stone'] = { {'Enchanted Hard Stone', 576 } },
		},
		stats = {
			{ tba = 14, storage = 64, crafting = { item = 'Hard Stone', num = 32, B2 = 'Wooden Pickaxe' } },
			{ tba = 14, storage = 192, crafting = { item = 'Hard Stone', num = 64, } },
			{ tba = 12, storage = 192, crafting = { item = 'Enchanted Hard Stone', num = 1, } },
			{ tba = 12, storage = 384, crafting = { item = 'Enchanted Hard Stone', num = 2, } },
			{ tba = 10, storage = 384, crafting = { item = 'Enchanted Hard Stone', num = 4, } },
			{ tba = 10, storage = 576, crafting = { item = 'Enchanted Hard Stone', num = 8, } },
			{ tba = 9, storage = 576, crafting = { item = 'Enchanted Hard Stone', num = 16, } },
			{ tba = 9, storage = 768, crafting = { item = 'Enchanted Hard Stone', num = 32, } },
			{ tba = 8, storage = 768, crafting = { item = 'Enchanted Hard Stone', num = 64, } },
			{ tba = 8, storage = 960, crafting = { item = 'Concentrated Stone', num = 1, A1 = '', A3 = '', C1 = '', C3 = '' } },
			{ tba = 7, storage = 960, crafting = { item = 'Concentrated Stone', num = 1, } },
			{ tba = 6, storage = 960, trade = {
				{ item = 'Concentrated Stone', num = 16 },
				{ item = 'Coin', num = 2000000 },
			}, tradeNpc = 'Bulvar' },
		},
		description = '&7Place this minion and it will/&7start generating and mining Hard/&7Stone! Requires an open area to/&7place Hard Stone. Minions also/&7work when you are offline!'
	},
	['Mycelium'] = {
		type = 'Mining',
		collection = 'Mycelium I',
		items = {
			{ item = 'Mycelium', avg = 1, exp = 3.2 },
		},
		drops = {
			none = {
				{ item = 'Mycelium', avg = 1, exp = '0.2 Mining' },
			},
			sc3000 = {
				{ item = 'Enchanted Mycelium', exp = '32 Mining', from = { item = 'Mycelium', num = 160 } },
				{ item = 'Enchanted Mycelium Cube', exp = '5120 Mining', from = { item = 'Enchanted Mycelium', num = 160 } },
			},
		},
		recipes = {
			['Enchanted Mycelium'] = { {'Mycelium', 160 } },
			['Enchanted Mycelium Cube'] = { {'Enchanted Mycelium', 160 } },
		},
		stats = {
			{ tba = 26, storage = 64, req = '{{Reputation|Mage|500}}', crafting = { item = 'Mycelium', num = 10, B2 = 'Wooden Shovel' } },
			{ tba = 25, storage = 128, req = '{{Reputation|Mage|1000}}', crafting = { item = 'Mycelium', num = 32, } },
			{ tba = 24, storage = 192, req = '{{Reputation|Mage|1500}}', crafting = { item = 'Mycelium', num = 64, } },
			{ tba = 23, storage = 320, req = '{{Reputation|Mage|2000}}', crafting = { item = 'Enchanted Mycelium', num = 2, } },
			{ tba = 22, storage = 384, req = '{{Reputation|Mage|3000}}', crafting = { item = 'Enchanted Mycelium', num = 4, } },
			{ tba = 21, storage = 512, req = '{{Reputation|Mage|4000}}', crafting = { item = 'Enchanted Mycelium', num = 8, } },
			{ tba = 20, storage = 576, req = '{{Reputation|Mage|5500}}', crafting = { item = 'Enchanted Mycelium', num = 16, } },
			{ tba = 19, storage = 704, req = '{{Reputation|Mage|6500}}', crafting = { item = 'Enchanted Mycelium', num = 32, } },
			{ tba = 18, storage = 768, req = '{{Reputation|Mage|7500}}', crafting = { item = 'Enchanted Mycelium', num = 64, } },
			{ tba = 16, storage = 896, req = '{{Reputation|Mage|9000}}', crafting = { item = 'Enchanted Mycelium Cube', num = 1, } },
			{ tba = 13, storage = 960, req = '{{Reputation|Mage|10000}}', crafting = { item = 'Enchanted Mycelium Cube', num = 2, } },
			{ tba = 11, storage = 960, req = '{{Reputation|Mage|12000}}', trade = {
				{ item = 'Enchanted Mycelium Cube', num = 32 },
				{ item = 'Coin', num = 2000000 },
			}, tradeNpc = 'Hilda' }, 
		},
		description = '&7Place this minion and it will/&7start generating and mining/&7mycelium! Requires an open area/&7to place mycelium . Minions also/&7work when you are offline!'
	},
	['Red Sand'] = {
		type = 'Mining',
		collection = 'Red Sand I',
		items = {
			{ item = 'Red Sand', avg = 1, exp = 3.2 },
		},
		drops = {
			none = {
				{ item = 'Red Sand', avg = 1, exp = '0.2 Mining' },
			},
			sc3000 = {
				{ item = 'Enchanted Red Sand', exp = '32 Mining', from = { item = 'Red Sand', num = 160 } },
				{ item = 'Enchanted Red Sand Cube', exp = '5120 Mining', from = { item = 'Enchanted Red Sand', num = 160 } },
			},
		},
		recipes = {
			['Enchanted Red Sand'] = { {'Red Sand', 160 } },
			['Enchanted Red Sand Cube'] = { {'Enchanted Red Sand', 160 } },
		},
		stats = {
			{ tba = 26, storage = 64, req = '{{Reputation|Barbarian|500}}', crafting = { item = 'Red Sand', num = 10, B2 = 'Wooden Shovel' } },
			{ tba = 25, storage = 128, req = '{{Reputation|Barbarian|1000}}', crafting = { item = 'Red Sand', num = 32, } },
			{ tba = 24, storage = 192, req = '{{Reputation|Barbarian|1500}}', crafting = { item = 'Red Sand', num = 64, } },
			{ tba = 23, storage = 320, req = '{{Reputation|Barbarian|2000}}', crafting = { item = 'Enchanted Red Sand', num = 2, } },
			{ tba = 22, storage = 384, req = '{{Reputation|Barbarian|3000}}', crafting = { item = 'Enchanted Red Sand', num = 4, } },
			{ tba = 21, storage = 512, req = '{{Reputation|Barbarian|4000}}', crafting = { item = 'Enchanted Red Sand', num = 8, } },
			{ tba = 20, storage = 576, req = '{{Reputation|Barbarian|5500}}', crafting = { item = 'Enchanted Red Sand', num = 16, } },
			{ tba = 19, storage = 704, req = '{{Reputation|Barbarian|6500}}', crafting = { item = 'Enchanted Red Sand', num = 32, } },
			{ tba = 18, storage = 768, req = '{{Reputation|Barbarian|7500}}', crafting = { item = 'Enchanted Red Sand', num = 64, } },
			{ tba = 16, storage = 896, req = '{{Reputation|Barbarian|9000}}', crafting = { item = 'Enchanted Red Sand Cube', num = 1, } },
			{ tba = 13, storage = 960, req = '{{Reputation|Barbarian|10000}}', crafting = { item = 'Enchanted Red Sand Cube', num = 2, } },
			{ tba = 11, storage = 960, req = '{{Reputation|Barbarian|12000}}', trade = {
				{ item = 'Enchanted Red Sand Cube', num = 32 },
				{ item = 'Coin', num = 2000000 },
			}, tradeNpc = 'Marthos' }, 
		},
		description = '&7Place this minion and it will/&7start generating and mining/&7red sand! Requires an open area/&7to place red sand. Minions also/&7work when you are offline!'
	},
	['Snow'] = {
		type = 'Mining',
		obtaining = '[[Season of Jerry]] [[Gifts]]',
		items = {
			{ item = 'Snowball', avg = 4, exp = 0.1 },
		},
		drops = {
			none = {
				{ item = 'Snowball', avg = 4, exp = '0.1 Mining' },
			},
			compactor = {
				{ item = 'Snow Block', exp = '0.4 Mining', from = { item = 'Snowball', num = 4 } },
			},
			sc3000 = {
				{ item = 'Enchanted Snow Block', exp = '64 Mining', from = { item = 'Snowball', num = 640 } },
			},
		},
		recipes = {
			['Snow Block'] = { {'Snowball', 4 } },
			['Enchanted Snow Block'] = { {'Snow Block', 160 } },
		},
		stats = {
			{ tba = 13, storage = 64, crafting = { item = 'Snow Block', num = 0, info = '[[White Gift]] - Obtained<br>from [[Season of Jerry]]' } },
			{ tba = 13, storage = 192, crafting = { item = 'Snow Block', num = 4 } },
			{ tba = 12, storage = 192, crafting = { item = 'Snow Block', num = 8 } },
			{ tba = 12, storage = 384, crafting = { item = 'Snow Block', num = 16 } },
			{ tba = 11, storage = 384, crafting = { item = 'Snow Block', num = 32 } },
			{ tba = 11, storage = 576, crafting = { item = 'Snow Block', num = 64 } },
			{ tba = 9.5, storage = 576, crafting = { item = 'Enchanted Snow Block', num = 1 } },
			{ tba = 9.5, storage = 768, crafting = { item = 'Enchanted Snow Block', num = 2 } },
			{ tba = 8, storage = 768, crafting = { item = 'Enchanted Snow Block', num = 4 } },
			{ tba = 8, storage = 960, crafting = { item = 'Enchanted Snow Block', num = 8 } },
			{ tba = 6.5, storage = 960, crafting = { item = 'Enchanted Snow Block', num = 16 } },
			{ tba = 5.8, storage = 960, trade = {
				{ item = 'Enchanted Snow Block', num = 1024 },
				{ item = 'Coin', num = 2000000 },
				{ item = 'North Star', num = 500 },
			}, tradeNpc = 'Einary' }, 
		},
		description = '&7Place this minion and it will/&7start generating and shovelling/&7snow! Requires an open area to/&7place snow. Minions also work/&7when you are offline!'
	},
	--------------------------------
	-- Combat
	--------------------------------
	['Zombie'] = {
		type = 'Combat',
		collection = 'Rotten Flesh I',
		items = {
			{ item = 'Rotten Flesh', avg = 1, exp = 0.3 },
			{ item = 'Poisonous Potato', avg = 0.05, exp = 0.0 },
			{ item = 'Potato', avg = 0.01, exp = 0.1 },
			{ item = 'Carrot', avg = 0.01, exp = 0.1 },
		},
		drops = {
			none = {
				{ item = 'Rotten Flesh', avg = 1, exp = '0.3 Combat' },
				{ item = 'Poisonous Potato', avg = 0.05 },
				{ item = 'Carrot', avg = 0.01, exp = '0.1 Farming' },
				{ item = 'Potato', avg = 0.01, exp = '0.1 Farming' },
			},
			sc3000 = {
				{ item = 'Enchanted Rotten Flesh', exp = '48 Combat', from = { item = 'Rotten Flesh', num = 160 } },
				{ item = 'Enchanted Poisonous Potato', from = { item = 'Poisonous Potato', num = 160 } },
				{ item = 'Enchanted Carrot', exp = '16 Farming', from = { item = 'Carrot', num = 160 } },
				{ item = 'Enchanted Potato', exp = '16 Farming', from = { item = 'Potato', num = 160 } },
				{ item = 'Enchanted Baked Potato', exp = '2560 Farming', from = { item = 'Enchanted Potato', num = 160 } },
			},
		},
		recipes = {
			['Enchanted Rotten Flesh'] = { {'Rotten Flesh', 160 } },
			['Enchanted Poisonous Potato'] = { {'Poisonous Potato', 160 } },
			['Enchanted Carrot'] = { {'Carrot', 160 } },
			['Enchanted Potato'] = { {'Potato', 160 } },
			['Enchanted Baked Potato'] = { {'Enchanted Potato', 160 } },
		},
		stats = {
			{ tba = 26, storage = 64, crafting = { item = 'Rotten Flesh', num = 10, B2 = 'Wooden Sword' } },
			{ tba = 26, storage = 192, crafting = { item = 'Rotten Flesh', num = 20 } },
			{ tba = 24, storage = 192, crafting = { item = 'Rotten Flesh', num = 40 } },
			{ tba = 24, storage = 384, crafting = { item = 'Rotten Flesh', num = 64 } },
			{ tba = 22, storage = 384, crafting = { item = 'Enchanted Rotten Flesh', num = 1 } },
			{ tba = 22, storage = 576, crafting = { item = 'Enchanted Rotten Flesh', num = 2 } },
			{ tba = 20, storage = 576, crafting = { item = 'Enchanted Rotten Flesh', num = 4 } },
			{ tba = 20, storage = 768, crafting = { item = 'Enchanted Rotten Flesh', num = 8 } },
			{ tba = 17, storage = 768, crafting = { item = 'Enchanted Rotten Flesh', num = 16 } },
			{ tba = 17, storage = 960, crafting = { item = 'Enchanted Rotten Flesh', num = 32 } },
			{ tba = 13, storage = 960, crafting = { item = 'Enchanted Rotten Flesh', num = 64 } },
		},
		description = '&7Place this minion and it will/&7start generating and slaying/&7Zombies! Minions also work when/&7you are offline!'
	},
	['Skeleton'] = {
		type = 'Combat',
		collection = 'Bone I',
		items = {
			{ item = 'Bone', avg = 1, exp = 0.2 },
		},
		drops = {
			none = {
				{ item = 'Bone', avg = 1, exp = '0.2 Combat' },
			},
			sc3000 = {
				{ item = 'Enchanted Bone', exp = '32 Combat', from = { item = 'Bone', num = 160 } },
			},
		},
		recipes = {
			['Enchanted Bone'] = { {'Bone', 160 } },
		},
		stats = {
			{ tba = 26, storage = 64, crafting = { item = 'Bone', num = 10, B2 = 'Wooden Sword' } },
			{ tba = 26, storage = 192, crafting = { item = 'Bone', num = 20 } },
			{ tba = 24, storage = 192, crafting = { item = 'Bone', num = 40 } },
			{ tba = 24, storage = 384, crafting = { item = 'Bone', num = 64 } },
			{ tba = 22, storage = 384, crafting = { item = 'Enchanted Bone', num = 1 } },
			{ tba = 22, storage = 576, crafting = { item = 'Enchanted Bone', num = 2 } },
			{ tba = 20, storage = 576, crafting = { item = 'Enchanted Bone', num = 4 } },
			{ tba = 20, storage = 768, crafting = { item = 'Enchanted Bone', num = 8 } },
			{ tba = 17, storage = 768, crafting = { item = 'Enchanted Bone', num = 16 } },
			{ tba = 17, storage = 960, crafting = { item = 'Enchanted Bone', num = 32 } },
			{ tba = 13, storage = 960, crafting = { item = 'Enchanted Bone', num = 64 } },
		},
		description = '&7Place this minion and it will/&7start generating and slaying/&7Skeletons! Minions also work/&7when you are offline!'
	},
	['Spider'] = {
		type = 'Combat',
		collection = 'String I',
		items = {
			{ item = 'String', avg = 1, exp = 0.2 },
			{ item = 'Spider Eye', avg = 0.5, exp = 0.3 },
		},
		drops = {
			none = {
				{ item = 'String', avg = 1, exp = '0.2 Combat' },
				{ item = 'Spider Eye', avg = 0.5, exp = '0.3 Combat' },
			},
			sc3000 = {
				{ item = 'Enchanted String', exp = '32 Combat', from = { item = 'String', num = 160 } },
				{ item = 'Enchanted Spider Eye', exp = '48 Combat', from = { item = 'Spider Eye', num = 160 } },
			},
		},
		recipes = {
			['Enchanted String'] = { {'String', 160 } },
			['Enchanted Spider Eye'] = { {'Spider Eye', 160 } },
		},
		stats = {
			{ tba = 26, storage = 64, crafting = { item = 'String', num = 10, B2 = 'Wooden Sword' } },
			{ tba = 26, storage = 192, crafting = { item = 'String', num = 20 } },
			{ tba = 24, storage = 192, crafting = { item = 'String', num = 40 } },
			{ tba = 24, storage = 384, crafting = { item = 'String', num = 64 } },
			{ tba = 22, storage = 384, crafting = { item = 'Enchanted String', num = 1 } },
			{ tba = 22, storage = 576, crafting = { item = 'Enchanted String', num = 2 } },
			{ tba = 20, storage = 576, crafting = { item = 'Enchanted String', num = 4 } },
			{ tba = 20, storage = 768, crafting = { item = 'Enchanted String', num = 8 } },
			{ tba = 17, storage = 768, crafting = { item = 'Enchanted String', num = 16 } },
			{ tba = 17, storage = 960, crafting = { item = 'Enchanted String', num = 32 } },
			{ tba = 13, storage = 960, crafting = { item = 'Enchanted String', num = 64 } },
		},
		description = '&7Place this minion and it will/&7start generating and slaying/&7Spiders! Minions also work when/&7you are offline!'
	},
	['Cave Spider'] = {
		type = 'Combat',
		collection = 'Spider Eye I',
		items = {
			{ item = 'Spider Eye', avg = 1, exp = 0.3 },
			{ item = 'String', avg = 0.5, exp = 0.2 },
		},
		drops = {
			none = {
				{ item = 'String', avg = 0.5, exp = '0.2 Combat' },
				{ item = 'Spider Eye', avg = 1, exp = '0.3 Combat' },
			},
			sc3000 = {
				{ item = 'Enchanted String', exp = '32 Combat', from = { item = 'String', num = 160 } },
				{ item = 'Enchanted Spider Eye', exp = '48 Combat', from = { item = 'Spider Eye', num = 160 } },
			},
		},
		recipes = {
			['Enchanted String'] = { {'String', 160 } },
			['Enchanted Spider Eye'] = { {'Spider Eye', 160 } },
			['Sugar'] = { {'Sugar Cane', 1 } },
			['Enchanted Fermented Spider Eye'] = {
				{'Enchanted Spider Eye', 64 },
				{'Brown Mushroom', 64 },
				{'Sugar', 64 },
			},
		},
		stats = {
			{ tba = 26, storage = 128, crafting = { item = 'Spider Eye', num = 10, B2 = 'Wooden Sword' } },
			{ tba = 26, storage = 256, crafting = { item = 'Spider Eye', num = 20 } },
			{ tba = 24, storage = 256, crafting = { item = 'Spider Eye', num = 40 } },
			{ tba = 24, storage = 384, crafting = { item = 'Spider Eye', num = 64 } },
			{ tba = 22, storage = 384, crafting = { item = 'Enchanted Spider Eye', num = 1 } },
			{ tba = 22, storage = 576, crafting = { item = 'Enchanted Spider Eye', num = 3 } },
			{ tba = 20, storage = 576, crafting = { item = 'Enchanted Spider Eye', num = 8 } },
			{ tba = 20, storage = 768, crafting = { item = 'Enchanted Spider Eye', num = 16 } },
			{ tba = 17, storage = 768, crafting = { item = 'Enchanted Spider Eye', num = 32 } },
			{ tba = 17, storage = 960, crafting = { item = 'Enchanted Spider Eye', num = 64 } },
			{ tba = 13, storage = 960, crafting = { item = 'Enchanted Fermented Spider Eye', num = 2 } },
		},
		description = '&7Place this minion and it will/&7start generating and slaying/&7Cave Spiders! Minions also work/&7when you are offline!'
	},
	['Creeper'] = {
		type = 'Combat',
		collection = 'Gunpowder I',
		items = {
			{ item = 'Gunpowder', avg = 1, exp = 0.3 },
		},
		drops = {
			none = {
				{ item = 'Gunpowder', avg = 1, exp = '0.3 Combat' },
			},
			sc3000 = {
				{ item = 'Enchanted Gunpowder', exp = '48 Combat', from = { item = 'Gunpowder', num = 160 } },
			},
		},
		recipes = {
			['Enchanted Gunpowder'] = { {'Gunpowder', 160 } },
			['Enchanted Firework Rocket'] = {
				{'Enchanted Gunpowder', 64 },
				{'Paper', 16 },
			},
		},
		stats = {
			{ tba = 27, storage = 64, crafting = { item = 'Gunpowder', num = 10, B2 = 'Wooden Sword' } },
			{ tba = 27, storage = 192, crafting = { item = 'Gunpowder', num = 20 } },
			{ tba = 25, storage = 192, crafting = { item = 'Gunpowder', num = 40 } },
			{ tba = 25, storage = 384, crafting = { item = 'Gunpowder', num = 64 } },
			{ tba = 23, storage = 384, crafting = { item = 'Enchanted Gunpowder', num = 1 } },
			{ tba = 23, storage = 576, crafting = { item = 'Enchanted Gunpowder', num = 3 } },
			{ tba = 21, storage = 576, crafting = { item = 'Enchanted Gunpowder', num = 8 } },
			{ tba = 21, storage = 768, crafting = { item = 'Enchanted Gunpowder', num = 16 } },
			{ tba = 18, storage = 768, crafting = { item = 'Enchanted Gunpowder', num = 32 } },
			{ tba = 18, storage = 960, crafting = { item = 'Enchanted Gunpowder', num = 64 } },
			{ tba = 14, storage = 960, crafting = { item = 'Enchanted Firework Rocket', num = 2 } },
		},
		description = '&7Place this minion and it will/&7start generating and slaying/&7Creepers! &cBEWARE OF/&cEXPLOSIONS! &7Minions also work/&7when you are offline!'
	},
	['Enderman'] = {
		type = 'Combat',
		collection = 'Ender Pearl I',
		items = {
			{ item = 'Ender Pearl', avg = 1, exp = 0.3 },
		},
		drops = {
			none = {
				{ item = 'Ender Pearl', avg = 1, exp = '0.3 Combat' }, -- exp:tested
			},
			sc3000 = {
				{ item = 'Enchanted Ender Pearl', exp = '48 Combat', from = { item = 'Ender Pearl', num = 20 } }, -- exp:tested
				{ item = 'Absolute Ender Pearl', exp = '7680 Combat', from = { item = 'Enchanted Ender Pearl', num = 80 } }, -- exp:tested
			},
		},
		recipes = {
			['Enchanted Ender Pearl'] = { {'Ender Pearl', 20 } },
			['Absolute Ender Pearl'] = { {'Enchanted Ender Pearl', 80 } },
			['Blaze Powder'] = { {'Blaze Rod', 0.5 } },
			['Enchanted Eye of Ender'] = {
				{'Enchanted Ender Pearl', 16 },
				{'Blaze Powder', 64 },
			},
		},
		stats = {
			{ tba = 32, storage = 64, crafting = { item = 'Ender Pearl', num = 8, B2 = 'Wooden Sword' } },
			{ tba = 32, storage = 192, crafting = { item = 'Ender Pearl', num = 16 } },
			{ tba = 30, storage = 192, crafting = { item = 'Enchanted Ender Pearl', num = 1 } },
			{ tba = 30, storage = 384, crafting = { item = 'Enchanted Ender Pearl', num = 3 } },
			{ tba = 28, storage = 384, crafting = { item = 'Enchanted Ender Pearl', num = 6 } },
			{ tba = 28, storage = 576, crafting = { item = 'Enchanted Ender Pearl', num = 12 } },
			{ tba = 25, storage = 576, crafting = { item = 'Enchanted Eye of Ender', num = 1 } },
			{ tba = 25, storage = 768, crafting = { item = 'Enchanted Eye of Ender', num = 3 } },
			{ tba = 22, storage = 768, crafting = { item = 'Enchanted Eye of Ender', num = 6 } },
			{ tba = 22, storage = 960, crafting = { item = 'Enchanted Eye of Ender', num = 12 } },
			{ tba = 18, storage = 960, crafting = { item = 'Enchanted Eye of Ender', num = 24 } },
		},
		description = '&7Place this minion and it will/&7start generating and slaying/&7Endermen! Minions also work when/&7you are offline!'
	},
	['Ghast'] = {
		type = 'Combat',
		collection = 'Ghast Tear I',
		items = {
			{ item = 'Ghast Tear', avg = 1, exp = 0.5 },
		},
		drops = {
			none = {
				{ item = 'Ghast Tear', avg = 1, exp = '0.5 Combat' }, -- exp tested
			},
			sc3000 = {
				{ item = 'Enchanted Ghast Tear', exp = '7.5 Combat', from = { item = 'Ghast Tear', num = 5 } }, -- exp tested
				-- { item = 'Silver Fang', exp = '187.5 Combat', from = { item = 'Enchanted Ghast Tear', num = 25 } }, -- availability/exp not tested
			},
		},
		recipes = {
			['Enchanted Ghast Tear'] = { {'Ghast Tear', 5 } },
			['Silver Fang'] = { {'Enchanted Ghast Tear', 25 } },
		},
		stats = {
			{ tba = 50, storage = 64, crafting = { item = 'Ghast Tear', num = 8, B2 = 'Wooden Sword' } },
			{ tba = 50, storage = 192, crafting = { item = 'Ghast Tear', num = 16 } },
			{ tba = 47, storage = 192, crafting = { item = 'Ghast Tear', num = 32 } },
			{ tba = 47, storage = 384, crafting = { item = 'Ghast Tear', num = 64 } },
			{ tba = 44, storage = 384, crafting = { item = 'Enchanted Ghast Tear', num = 32 } },
			{ tba = 44, storage = 576, crafting = { item = 'Enchanted Ghast Tear', num = 64 } },
			{ tba = 41, storage = 576, crafting = { item = 'Silver Fang', num = 4 } },
			{ tba = 41, storage = 768, crafting = { item = 'Silver Fang', num = 8 } },
			{ tba = 38, storage = 768, crafting = { item = 'Silver Fang', num = 16 } },
			{ tba = 38, storage = 960, crafting = { item = 'Silver Fang', num = 32 } },
			{ tba = 32, storage = 960, crafting = { item = 'Silver Fang', num = 64 } },
			{ tba = 30, storage = 960, trade = {
				{ item = 'Silver Fang', num = 1024 },
				{ item = 'Coin', num = 2000000 },
			}, tradeNpc = {'Hilda', 'Marthos'} },
		},
		description = '&7Place this minion and it will/&7start generating and slaying/&7Ghasts! &cBEWARE OF/&cEXPLOSIONS! &7Minions also work/&7when you are offline!'
	},
	['Slime'] = {
		type = 'Combat',
		collection = 'Slimeball I',
		items = {
			-- taken from the famous minion spreadsheet
			{ item = 'Slimeball', avg = 1.8, exp = 0.2 },
		},
		drops = {
			none = {
				{ item = 'Slimeball', avg = 1.8, exp = '0.2 Combat' }, -- avg tested
			},
			compactor = {
				{ item = 'Slime Block', exp = '1.8 Combat', from = { item = 'Slimeball', num = 9 } },
			},
			sc3000 = {
				{ item = 'Enchanted Slimeball', exp = '32 Combat', from = { item = 'Slimeball', num = 160 } },
				{ item = 'Enchanted Slime Block', exp = '5120 Combat', from = { item = 'Enchanted Slimeball', num = 160 } },
			},
		},
		recipes = {
			['Enchanted Slimeball'] = { {'Slimeball', 160 } },
			['Enchanted Slime Block'] = { {'Enchanted Slimeball', 160 } },
		},
		stats = {
			{ tba = 26, storage = 64, crafting = { item = 'Slimeball', num = 10, B2 = 'Wooden Sword' } },
			{ tba = 26, storage = 192, crafting = { item = 'Slimeball', num = 20 } },
			{ tba = 24, storage = 192, crafting = { item = 'Slimeball', num = 40 } },
			{ tba = 24, storage = 384, crafting = { item = 'Slimeball', num = 64 } },
			{ tba = 22, storage = 384, crafting = { item = 'Enchanted Slimeball', num = 1 } },
			{ tba = 22, storage = 576, crafting = { item = 'Enchanted Slimeball', num = 3 } },
			{ tba = 19, storage = 576, crafting = { item = 'Enchanted Slimeball', num = 8 } },
			{ tba = 19, storage = 768, crafting = { item = 'Enchanted Slimeball', num = 16 } },
			{ tba = 16, storage = 768, crafting = { item = 'Enchanted Slimeball', num = 32 } },
			{ tba = 16, storage = 960, crafting = { item = 'Enchanted Slimeball', num = 64 } },
			{ tba = 12, storage = 960, crafting = { item = 'Enchanted Slime Block', num = 1 } },
		},
		description = '&7Place this minion and it will/&7start generating and slaying/&7Slimes! Minions also work when/&7you are offline!'
	},
	['Blaze'] = {
		type = 'Combat',
		collection = 'Blaze Rod I',
		items = {
			{ item = 'Blaze Rod', avg = 1, exp = 0.3 },
		},
		drops = {
			none = {
				{ item = 'Blaze Rod', avg = 1, exp = '0.3 Combat' },
			},
			sc3000 = {
				{ item = 'Enchanted Blaze Powder', exp = '48 Combat', from = { item = 'Blaze Rod', num = 160 } },
				{ item = 'Enchanted Blaze Rod', exp = '7680 Combat', from = { item = 'Enchanted Blaze Powder', num = 160 } },
			},
		},
		recipes = {
			['Enchanted Blaze Powder'] = { {'Blaze Rod', 160 } },
			['Enchanted Blaze Rod'] = { {'Enchanted Blaze Powder', 160 } },
		},
		stats = {
			{ tba = 33, storage = 64, crafting = { item = 'Blaze Rod', num = 10, B2 = 'Wooden Sword' } },
			{ tba = 33, storage = 192, crafting = { item = 'Blaze Rod', num = 20 } },
			{ tba = 31, storage = 192, crafting = { item = 'Blaze Rod', num = 40 } },
			{ tba = 31, storage = 384, crafting = { item = 'Blaze Rod', num = 64 } },
			{ tba = 28.5, storage = 384, crafting = { item = 'Enchanted Blaze Powder', num = 1 } },
			{ tba = 28.5, storage = 576, crafting = { item = 'Enchanted Blaze Powder', num = 3 } },
			{ tba = 25, storage = 576, crafting = { item = 'Enchanted Blaze Powder', num = 8 } },
			{ tba = 25, storage = 768, crafting = { item = 'Enchanted Blaze Powder', num = 16 } },
			{ tba = 21, storage = 768, crafting = { item = 'Enchanted Blaze Powder', num = 32 } },
			{ tba = 21, storage = 960, crafting = { item = 'Enchanted Blaze Powder', num = 64 } },
			{ tba = 16.5, storage = 960, crafting = { item = 'Enchanted Blaze Rod', num = 1 } },
			{ tba = 15, storage = 960, trade = {
				{ item = 'Enchanted Blaze Rod', num = 16 },
				{ item = 'Coin', num = 2000000 },
			}, tradeNpc = {'Hilda', 'Marthos'} },
		},
		description = '&7Place this minion and it will/&7start generating and slaying/&7Blaze! Minions also work when/&7you are offline!'
	},
	['Magma Cube'] = {
		type = 'Combat',
		collection = 'Magma Cream I',
		items = {
			-- taken from the famous minion spreadsheet
			{ item = 'Magma Cream', avg = 1.8, exp = 0.2 },
		},
		drops = {
			none = {
				{ item = 'Magma Cream', avg = 1.8, exp = '0.2 Combat' },
			},
			sc3000 = {
				{ item = 'Enchanted Magma Cream', exp = '32 Combat', from = { item = 'Magma Cream', num = 160 } },
			},
		},
		recipes = {
			['Enchanted Magma Cream'] = { {'Magma Cream', 160 } },
		},
		stats = {
			{ tba = 32, storage = 64, crafting = { item = 'Magma Cream', num = 10, B2 = 'Wooden Sword' } },
			{ tba = 32, storage = 192, crafting = { item = 'Magma Cream', num = 20 } },
			{ tba = 30, storage = 192, crafting = { item = 'Magma Cream', num = 40 } },
			{ tba = 30, storage = 384, crafting = { item = 'Magma Cream', num = 64 } },
			{ tba = 28, storage = 384, crafting = { item = 'Enchanted Magma Cream', num = 1 } },
			{ tba = 28, storage = 576, crafting = { item = 'Enchanted Magma Cream', num = 2 } },
			{ tba = 25, storage = 576, crafting = { item = 'Enchanted Magma Cream', num = 4 } },
			{ tba = 25, storage = 768, crafting = { item = 'Enchanted Magma Cream', num = 8 } },
			{ tba = 22, storage = 768, crafting = { item = 'Enchanted Magma Cream', num = 16 } },
			{ tba = 22, storage = 960, crafting = { item = 'Enchanted Magma Cream', num = 32 } },
			{ tba = 18, storage = 960, crafting = { item = 'Enchanted Magma Cream', num = 64 } },
			{ tba = 16, storage = 960, trade = {
				{ item = 'Enchanted Magma Cream', num = 1024 },
				{ item = 'Coin', num = 2000000 },
			}, tradeNpc = {'Hilda', 'Marthos'} },
		},
		description = '&7Place this minion and it will/&7start generating and slaying/&7Magma Cubes! Minions also work/&7when you are offline!'
	},

	['Vampire'] = {
		type = 'Combat',
		collection = 'Hemovibe I',
		items = {
			{ item = 'Hemovibe', avg = 1, exp = 0 },
		},
		drops = {
			none = {
				{ item = 'Hemovibe', avg = 1, exp = '5 Combat' },
			},
			sc3000 = {
				{ item = 'Hemoglass', exp = '800 Combat', from = { item = 'Hemovibe', num = 160 } },
			},
		},
		recipes = {
			['Hemoglass'] = { {'Hemovibe', 160 } },
		},
		stats = {
			{ tba = 190, storage = 64, crafting = { item = 'Hemovibe', num = 10, B2 = 'Bat Person Helmet' } },
			{ tba = 190, storage = 192, crafting = { item = 'Hemovibe', num = 20, B2 = 'Vampire Minion I' } },
			{ tba = 175, storage = 192, crafting = { item = 'Hemovibe', num = 40, B2 = 'Vampire Minion II' } },
			{ tba = 175, storage = 384, crafting = { item = 'Hemovibe', num = 64, B2 = 'Vampire Minion III' } },
			
			{ tba = 160, storage = 384, crafting = { item = 'Hemoglass', num = 1, B2 = 'Vampire Minion IV' } },
			{ tba = 160, storage = 576, crafting = { item = 'Hemoglass', num = 2, B2 = 'Vampire Minion V' } },
			{ tba = 140, storage = 576, crafting = { item = 'Hemoglass', num = 4, B2 = 'Vampire Minion VI' } },
			{ tba = 140, storage = 768, crafting = { item = 'Hemoglass', num = 8, B2 = 'Vampire Minion VII' } },
			{ tba = 117, storage = 768, crafting = { item = 'Hemoglass', num = 16, B2 = 'Vampire Minion VIII' } },
			{ tba = 117, storage = 960, crafting = { item = 'Hemoglass', num = 32, B2 = 'Vampire Minion IX' } },
			{ tba = 95, storage = 960, crafting = { item = 'Hemoglass', num = 64, B2 = 'Vampire Minion X' } },
		},
		description = '&7Place this minion and it will/&7start generating and slaying/&7Vampire Scions! Minions also/&7work when you are offline!'
	},
	--------------------------------
	-- Slayer
	--------------------------------
	['Revenant'] = {
		type = 'Slayer',
		collection = 'Zombie Slayer V',
		items = {
			-- taken from the famous minion spreadsheet
			{ item = 'Rotten Flesh', avg = 3, exp = 0.3 },
			{ item = 'Diamond', avg = 0.2, exp = 0.4 },
		},
		drops = {
			none = {
				-- taken from the famous minion spreadsheet
				{ item = 'Rotten Flesh', avg = 3, exp = '0.3 Combat' },
				{ item = 'Diamond', avg = 0.2, exp = '0.4 Mining' },
			},
			compactor = {
				{ item = 'Block of Diamond', exp = '3.6 Mining', from = { item = 'Diamond', num = 9 } },
			},
			sc3000 = {
				{ item = 'Enchanted Rotten Flesh', exp = '48 Combat', from = { item = 'Rotten Flesh', num = 160 } },
				{ item = 'Enchanted Diamond', exp = '64 Mining', from = { item = 'Diamond', num = 160 } },
				{ item = 'Enchanted Diamond Block', exp = '10240 Mining', from = { item = 'Enchanted Diamond', num = 160 } },
			},
		},
		recipes = {
			['Enchanted Rotten Flesh'] = { {'Rotten Flesh', 160 } },
			['Enchanted Diamond'] = { {'Diamond', 160 } },
			['Enchanted Diamond Block'] = { {'Enchanted Diamond', 160 } },
			['Enchanted String'] = { {'String', 160 } },
			['Revenant Viscera'] = {
				{'Revenant Flesh', 128 },
				{'Enchanted String', 32 },
			},
		},
		stats = {
			{ tba = 29, storage = 64, crafting = { item = 'Revenant Flesh', num = 10, B2 = 'Crystallized Heart' } },
			{ tba = 29, storage = 192, crafting = { item = 'Revenant Flesh', num = 20, B3 = 'Zombie Minion I' } },
			{ tba = 26, storage = 192, crafting = { item = 'Revenant Flesh', num = 40, B3 = 'Zombie Minion II' } },
			{ tba = 26, storage = 384, crafting = { item = 'Revenant Flesh', num = 64, B3 = 'Zombie Minion III' } },
			{ tba = 23, storage = 384, crafting = { item = 'Revenant Viscera', num = 1, B3 = 'Zombie Minion IV' } },
			{ tba = 23, storage = 576, crafting = { item = 'Revenant Viscera', num = 2, B3 = 'Zombie Minion V' } },
			{ tba = 19, storage = 576, crafting = { item = 'Revenant Viscera', num = 4, B3 = 'Zombie Minion VI' } },
			{ tba = 19, storage = 768, crafting = { item = 'Revenant Viscera', num = 8, B3 = 'Zombie Minion VII' } },
			{ tba = 14.5, storage = 768, crafting = { item = 'Revenant Viscera', num = 16, B3 = 'Zombie Minion VIII' } },
			{ tba = 14.5, storage = 960, crafting = { item = 'Revenant Viscera', num = 32, B3 = 'Zombie Minion IX' } },
			{ tba = 10, storage = 960, crafting = { item = 'Revenant Viscera', num = 64, B3 = 'Zombie Minion X' } },
			{ tba = 8, storage = 960, trade = {
				{ item = 'Revenant Viscera', num = 64 },
				{ item = 'Coin', num = 2000000 },
			}, tradeNpc = 'Bartender' },
		},
		description = '&7Place this minion and it will/&7start generating and struggling/&7with Revenants! Minions also/&7work when you are offline!'
	},
	['Tarantula'] = {
		type = 'Slayer',
		collection = 'Spider Slayer V',
		items = {
			-- taken from the famous minion spreadsheet
			{ item = 'String', avg = 3.16, exp = 0.2 },
			{ item = 'Spider Eye', avg = 1, exp = 0.3 },
			{ item = 'Iron Ingot', avg = 0.2, exp = 0.3 },
		},
		drops = {
			none = {
				{ item = 'String', avg = 3.16, exp = '0.2 Combat' },
				{ item = 'Spider Eye', avg = 1, exp = '0.3 Combat' },
				{ item = 'Iron Ingot', avg = 0.2, exp = '0.3 Mining' },
			},
			compactor = {
				{ item = 'Block of Iron', exp = '2.7 Mining', from = { item = 'Iron Ingot', num = 9 } },
			},
			sc3000 = {
				{ item = 'Enchanted String', exp = '32 Combat', from = { item = 'String', num = 160 } },
				{ item = 'Enchanted Spider Eye', exp = '48 Combat', from = { item = 'Spider Eye', num = 160 } },
				{ item = 'Enchanted Iron Ingot', exp = '48 Mining', from = { item = 'Iron Ingot', num = 160 } },
				{ item = 'Enchanted Iron Block', exp = '7680 Mining', from = { item = 'Enchanted Iron Ingot', num = 160 } },
			},
		},
		recipes = {
			['Enchanted String'] = { {'String', 160 } },
			['Enchanted Spider Eye'] = { {'Spider Eye', 160 } },
			['Enchanted Iron Ingot'] = { {'Iron Ingot', 160 } },
			['Enchanted Iron Block'] = { {'Enchanted Iron Ingot', 160 } },
			['Enchanted Flint'] = { {'Flint', 160 } },
			['Tarantula Silk'] = {
				{'Tarantula Web', 128 },
				{'Enchanted Flint', 32 },
			},
		},
		stats = {
			{ tba = 29, storage = 64, crafting = { item = 'Tarantula Web', num = 10, B2 = 'Enchanted Fermented Spider Eye' } },
			{ tba = 29, storage = 192, crafting = { item = 'Tarantula Web', num = 20, B3 = 'Spider Minion I' } },
			{ tba = 26, storage = 192, crafting = { item = 'Tarantula Web', num = 40, B3 = 'Spider Minion II' } },
			{ tba = 26, storage = 384, crafting = { item = 'Tarantula Web', num = 64, B3 = 'Spider Minion III' } },
			
			{ tba = 23, storage = 384, crafting = { item = 'Tarantula Silk', num = 1, B3 = 'Spider Minion IV' } },
			{ tba = 23, storage = 576, crafting = { item = 'Tarantula Silk', num = 2, B3 = 'Spider Minion V' } },
			{ tba = 19, storage = 576, crafting = { item = 'Tarantula Silk', num = 4, B3 = 'Spider Minion VI' } },
			{ tba = 19, storage = 768, crafting = { item = 'Tarantula Silk', num = 8, B3 = 'Spider Minion VII' } },
			{ tba = 14.5, storage = 768, crafting = { item = 'Tarantula Silk', num = 16, B3 = 'Spider Minion VIII' } },
			{ tba = 14.5, storage = 960, crafting = { item = 'Tarantula Silk', num = 32, B3 = 'Spider Minion IX' } },
			{ tba = 10, storage = 960, crafting = { item = 'Tarantula Silk', num = 64, B3 = 'Spider Minion X' } },
		},
		description = '&7Place this minion and it will/&7start generating and squashing/&7Tarantulas! Minions also work/&7 when you are offline!'
	},
	['Voidling'] = {
		type = 'Slayer',
		collection = 'Enderman Slayer IV',
		items = {
			-- I don't know if these numbers are correct, I got them from the minion page
			{ item = 'Nether Quartz', avg = 0.4, exp = 0.3 },
			{ item = 'Obsidian', avg = 2.42, exp = 0.4 },
			{ item = 'Enchanted Ender Pearl', avg = 0.000625, exp = 48 },
		},
		drops = {
			none = {
				{ item = 'Nether Quartz', avg = 0.4, exp = '0.3 Mining' },
				{ item = 'Obsidian', avg = 2.42, exp = '0.4 Mining' },
				{ item = 'Enchanted Ender Pearl', avg = 0.000625, onein = 1600, exp = '48 Combat' }, -- exp tested in enderman
			},
			sc3000 = {
				{ item = 'Enchanted Nether Quartz', exp = '48 Mining', from = { item = 'Nether Quartz', num = 160 } },
				{ item = 'Enchanted Obsidian', exp = '64 Mining', from = { item = 'Obsidian', num = 160 } },
				{ item = 'Enchanted Quartz Block', exp = '7680 Mining', from = { item = 'Enchanted Nether Quartz', num = 160 } },
				{ item = 'Absolute Ender Pearl', exp = '7680 Combat', from = { item = 'Enchanted Ender Pearl', num = 80 } }, -- availability/exp not tested
			},
		},
		recipes = {
			['Enchanted Nether Quartz'] = { {'Nether Quartz', 160 } },
			['Enchanted Obsidian'] = { {'Obsidian', 160 } },
			['Enchanted Quartz Block'] = { {'Enchanted Nether Quartz', 160 } },
			['Absolute Ender Pearl'] = { {'Enchanted Ender Pearl', 80 } },
			['Null Ovoid'] = {
				{'Null Sphere', 128 },
				{'Enchanted Obsidian', 32 },
			},
		},
		stats = {
			{ tba = 45, storage = 64, crafting = { item = 'Null Sphere', num = 10, B2 = 'Enderman Minion I' } },
			{ tba = 45, storage = 192, crafting = { item = 'Null Sphere', num = 20, B3 = 'Obsidian Minion I' } },
			{ tba = 42, storage = 192, crafting = { item = 'Null Sphere', num = 40, B3 = 'Enderman Minion II' } },
			{ tba = 42, storage = 384, crafting = { item = 'Null Sphere', num = 64, B3 = 'Obsidian Minion III' } },
			{ tba = 39, storage = 384, crafting = { item = 'Null Ovoid', num = 1, B3 = 'Enderman Minion IV' } },
			{ tba = 39, storage = 576, crafting = { item = 'Null Ovoid', num = 2, B3 = 'Obsidian Minion V' } },
			{ tba = 35, storage = 576, crafting = { item = 'Null Ovoid', num = 4, B3 = 'Enderman Minion VI' } },
			{ tba = 35, storage = 768, crafting = { item = 'Null Ovoid', num = 8, B3 = 'Obsidian Minion VII' } },
			{ tba = 30, storage = 768, crafting = { item = 'Null Ovoid', num = 16, B3 = 'Enderman Minion VIII' } },
			{ tba = 30, storage = 960, crafting = { item = 'Null Ovoid', num = 32, B3 = 'Obsidian Minion IX' } },
			{ tba = 24, storage = 960, crafting = { item = 'Null Ovoid', num = 64, B3 = 'Enderman Minion X' } },
		},
		description = '&7Place this minion and it will/&7start generating and slaying/&7Voidlings! Minions also work/&7when you are offline!'
	},
	['Inferno'] = {
		type = 'Slayer',
		collection = 'Blaze Slayer III',
	 	items = {
			{ item = 'Crude Gabagool', avg = 1 },
	 	},
		drops = {
			none = {
				{ item = 'Crude Gabagool', avg = 1 },
			},
			legendaryinfernofuel = {
				{ item = 'Chili Pepper', avg = 0.007352, onein = 136 },
				{ item = 'Inferno Vertex', avg = 0.0001681, onein = 5950 },
				{ item = 'Inferno Apex', avg = 0.0000007639, onein = 1309091 },
				{ item = 'Reaper Pepper', avg = 0.000002183, onein = 458182 },
				{ item = 'Gabagool The Fish', avg = 0.0000002546, onein = 3927273 },
			},
		},
		recipes = {
			['Amalgamated Crimsonite'] = {
				{'Enchanted Red Sand', 4 },
				{'Enchanted Mycelium', 4 },
				{'Enchanted Glowstone Dust', 16 },
				{'Enchanted Magma Cream', 16 },
				{'Enchanted Blaze Powder', 16 },
				{'Enchanted Nether Wart', 16 },
			},
			['Molten Powder'] = {
				{'Derelict Ashe', 128 },
				{'Amalgamated Crimsonite', 1 },
			},
		},
		abilities = {
			{ req = 1, '&6Ability: Rising Celsius/&7Each Inferno minion increases/&7the speed of all Inferno minions/&7by &a18%&7.' },
			{ req = 10, '&6Ability: Apex Minion/&7When creating an Inferno Apex,/&7create 2.' }
		},
		stats = {
			{ tba = 1013, storage = 64, crafting = { item = 'Derelict Ashe', num = 10, B2 = 'Blaze Minion I' } },
			{ tba = 982, storage = 192, crafting = { item = 'Derelict Ashe', num = 40 } },
			{ tba = 950, storage = 192, crafting = { item = 'Molten Powder', num = 1 } },
			{ tba = 919, storage = 384, crafting = { item = 'Molten Powder', num = 2 } },
			{ tba = 886, storage = 384, crafting = { item = 'Molten Powder', num = 4 } },
			{ tba = 855, storage = 576, crafting = { item = 'Molten Powder', num = 8 } },
			{ tba = 823, storage = 576, crafting = { item = 'Molten Powder', num = 16 } },
			{ tba = 792, storage = 768, crafting = { item = 'Molten Powder', num = 32 } },
			{ tba = 760, storage = 768, crafting = { item = 'Molten Powder', num = 64, B1 = 'Inferno Vertex,4', A2 = 'Inferno Vertex,4', C2 = 'Inferno Vertex,4', B3 = 'Inferno Vertex,4' } },
			{ tba = 728, storage = 960, crafting = { item = 'Molten Powder', num = 64, B1 = 'Inferno Vertex,12', A2 = 'Inferno Vertex,12', C2 = 'Inferno Vertex,12', B3 = 'Inferno Vertex,12' } },
			{ tba = 697, storage = 960, crafting = { item = 'Molten Powder', num = 64, B1 = 'Inferno Apex', A2 = 'Inferno Vertex,24', C2 = 'Inferno Vertex,24', B3 = 'Inferno Minion VIII' } },
		},
	 	description = '&7Place this minion and it will/&7start generating and slaying/&7Infernals! Minions also work/&7when you are offline!'
	},
	--------------------------------
	-- Foraging
	--------------------------------
	['Oak'] = {
		type = 'Foraging',
		collection = 'Oak Log I',
		items = {
			{ item = 'Oak Log', avg = 4, exp = 0.1 },
		},
		drops = {
			none = {
				{ item = 'Oak Log', avg = 4, exp = '0.1 Foraging' },
			},
			smelter = {
				{ item = 'Coal', exp = '0.3 Mining', from = { item = 'Oak Log', num = 1 } },
			},
			sc3000 = {
				{ item = 'Enchanted Oak Log', exp = '16 Foraging', from = { item = 'Oak Log', num = 160 } },
			},
			smelter_sc3000 = {
				{ item = 'Enchanted Coal', exp = '48 Mining', from = { item = 'Coal', num = 160 } },
				{ item = 'Enchanted Coal Block', exp = '7680 Mining', from = { item = 'Enchanted Coal', num = 160 } },
			},
		},
		recipes = {
			['Enchanted Oak Log'] = { {'Oak Log', 160 } },
		},
		stats = {
			{ tba = 48, storage = 64, crafting = { item = 'Oak Log', num = 10, B2 = 'Wooden Axe' } },
			{ tba = 48, storage = 192, crafting = { item = 'Oak Log', num = 20 } },
			{ tba = 45, storage = 192, crafting = { item = 'Oak Log', num = 40 } },
			{ tba = 45, storage = 384, crafting = { item = 'Oak Log', num = 64 } },
			{ tba = 42, storage = 384, crafting = { item = 'Enchanted Oak Log', num = 1 } },
			{ tba = 42, storage = 576, crafting = { item = 'Enchanted Oak Log', num = 2 } },
			{ tba = 38, storage = 576, crafting = { item = 'Enchanted Oak Log', num = 4 } },
			{ tba = 38, storage = 768, crafting = { item = 'Enchanted Oak Log', num = 8 } },
			{ tba = 33, storage = 768, crafting = { item = 'Enchanted Oak Log', num = 16 } },
			{ tba = 33, storage = 960, crafting = { item = 'Enchanted Oak Log', num = 32 } },
			{ tba = 27, storage = 960, crafting = { item = 'Enchanted Oak Log', num = 64 } },
		},
		description = '&7Place this minion and it will/&7start generating and chopping/&7oak logs! Requires an open/&7area to plant trees. Minions/&7also work when you are offline!'
	},
	['Spruce'] = {
		type = 'Foraging',
		collection = 'Spruce Log I',
		items = {
			{ item = 'Spruce Log', avg = 4, exp = 0.1 },
		},
		drops = {
			none = {
				{ item = 'Spruce Log', avg = 4, exp = '0.1 Foraging' },
			},
			smelter = {
				{ item = 'Coal', exp = '0.3 Mining', from = { item = 'Spruce Log', num = 1 } },
			},
			sc3000 = {
				{ item = 'Enchanted Spruce Log', exp = '16 Foraging', from = { item = 'Spruce Log', num = 160 } },
			},
			smelter_sc3000 = {
				{ item = 'Enchanted Coal', exp = '48 Mining', from = { item = 'Coal', num = 160 } },
				{ item = 'Enchanted Coal Block', exp = '7680 Mining', from = { item = 'Enchanted Coal', num = 160 } },
			},
		},
		recipes = {
			['Enchanted Spruce Log'] = { {'Spruce Log', 160 } },
		},
		stats = {
			{ tba = 48, storage = 64, crafting = { item = 'Spruce Log', num = 10, B2 = 'Wooden Axe' } },
			{ tba = 48, storage = 192, crafting = { item = 'Spruce Log', num = 20 } },
			{ tba = 45, storage = 192, crafting = { item = 'Spruce Log', num = 40 } },
			{ tba = 45, storage = 384, crafting = { item = 'Spruce Log', num = 64 } },
			{ tba = 42, storage = 384, crafting = { item = 'Enchanted Spruce Log', num = 1 } },
			{ tba = 42, storage = 576, crafting = { item = 'Enchanted Spruce Log', num = 2 } },
			{ tba = 38, storage = 576, crafting = { item = 'Enchanted Spruce Log', num = 4 } },
			{ tba = 38, storage = 768, crafting = { item = 'Enchanted Spruce Log', num = 8 } },
			{ tba = 33, storage = 768, crafting = { item = 'Enchanted Spruce Log', num = 16 } },
			{ tba = 33, storage = 960, crafting = { item = 'Enchanted Spruce Log', num = 32 } },
			{ tba = 27, storage = 960, crafting = { item = 'Enchanted Spruce Log', num = 64 } },
		},
		description = '&7Place this minion and it will/&7start generating and chopping/&7spruce logs! Requires an open/&7area to plant trees. Minions/&7also work when you are offline!'
	},
	['Birch'] = {
		type = 'Foraging',
		collection = 'Birch Log I',
		items = {
			{ item = 'Birch Log', avg = 4, exp = 0.1 },
		},
		drops = {
			none = {
				{ item = 'Birch Log', avg = 4, exp = '0.1 Foraging' },
			},
			smelter = {
				{ item = 'Coal', exp = '0.3 Mining', from = { item = 'Birch Log', num = 1 } },
			},
			sc3000 = {
				{ item = 'Enchanted Birch Log', exp = '16 Foraging', from = { item = 'Birch Log', num = 160 } },
			},
			smelter_sc3000 = {
				{ item = 'Enchanted Coal', exp = '48 Mining', from = { item = 'Coal', num = 160 } },
				{ item = 'Enchanted Coal Block', exp = '7680 Mining', from = { item = 'Enchanted Coal', num = 160 } },
			},
		},
		recipes = {
			['Enchanted Birch Log'] = { {'Birch Log', 160 } },
		},
		stats = {
			{ tba = 48, storage = 64, crafting = { item = 'Birch Log', num = 10, B2 = 'Wooden Axe' } },
			{ tba = 48, storage = 192, crafting = { item = 'Birch Log', num = 20 } },
			{ tba = 45, storage = 192, crafting = { item = 'Birch Log', num = 40 } },
			{ tba = 45, storage = 384, crafting = { item = 'Birch Log', num = 64 } },
			{ tba = 42, storage = 384, crafting = { item = 'Enchanted Birch Log', num = 1 } },
			{ tba = 42, storage = 576, crafting = { item = 'Enchanted Birch Log', num = 2 } },
			{ tba = 38, storage = 576, crafting = { item = 'Enchanted Birch Log', num = 4 } },
			{ tba = 38, storage = 768, crafting = { item = 'Enchanted Birch Log', num = 8 } },
			{ tba = 33, storage = 768, crafting = { item = 'Enchanted Birch Log', num = 16 } },
			{ tba = 33, storage = 960, crafting = { item = 'Enchanted Birch Log', num = 32 } },
			{ tba = 27, storage = 960, crafting = { item = 'Enchanted Birch Log', num = 64 } },
		},
		description = '&7Place this minion and it will/&7start generating and chopping/&7birch logs! Requires an open/&7area to plant trees. Minions/&7also work when you are offline!'
	},
	['Dark Oak'] = {
		type = 'Foraging',
		collection = 'Dark Oak Log I',
		items = {
			{ item = 'Dark Oak Log', avg = 4, exp = 0.1 },
		},
		drops = {
			none = {
				{ item = 'Dark Oak Log', avg = 4, exp = '0.1 Foraging' },
			},
			smelter = {
				{ item = 'Coal', exp = '0.3 Mining', from = { item = 'Dark Oak Log', num = 1 } },
			},
			sc3000 = {
				{ item = 'Enchanted Dark Oak Log', exp = '16 Foraging', from = { item = 'Dark Oak Log', num = 160 } },
			},
			smelter_sc3000 = {
				{ item = 'Enchanted Coal', exp = '48 Mining', from = { item = 'Coal', num = 160 } },
				{ item = 'Enchanted Coal Block', exp = '7680 Mining', from = { item = 'Enchanted Coal', num = 160 } },
			},
		},
		recipes = {
			['Enchanted Dark Oak Log'] = { {'Dark Oak Log', 160 } },
		},
		stats = {
			{ tba = 48, storage = 64, crafting = { item = 'Dark Oak Log', num = 10, B2 = 'Wooden Axe' } },
			{ tba = 48, storage = 192, crafting = { item = 'Dark Oak Log', num = 20 } },
			{ tba = 45, storage = 192, crafting = { item = 'Dark Oak Log', num = 40 } },
			{ tba = 45, storage = 384, crafting = { item = 'Dark Oak Log', num = 64 } },
			{ tba = 42, storage = 384, crafting = { item = 'Enchanted Dark Oak Log', num = 1 } },
			{ tba = 42, storage = 576, crafting = { item = 'Enchanted Dark Oak Log', num = 2 } },
			{ tba = 38, storage = 576, crafting = { item = 'Enchanted Dark Oak Log', num = 4 } },
			{ tba = 38, storage = 768, crafting = { item = 'Enchanted Dark Oak Log', num = 8 } },
			{ tba = 33, storage = 768, crafting = { item = 'Enchanted Dark Oak Log', num = 16 } },
			{ tba = 33, storage = 960, crafting = { item = 'Enchanted Dark Oak Log', num = 32 } },
			{ tba = 27, storage = 960, crafting = { item = 'Enchanted Dark Oak Log', num = 64 } },
		},
		description = '&7Place this minion and it will/&7start generating and chopping/&7dark oak logs! Requires an open/&7area to plant trees. Minions/&7also work when you are offline!'
	},
	['Acacia'] = {
		type = 'Foraging',
		collection = 'Acacia Log I',
		items = {
			{ item = 'Acacia Log', avg = 4, exp = 0.1 },
		},
		drops = {
			none = {
				{ item = 'Acacia Log', avg = 4, exp = '0.1 Foraging' },
			},
			smelter = {
				{ item = 'Coal', exp = '0.3 Mining', from = { item = 'Acacia Log', num = 1 } },
			},
			sc3000 = {
				{ item = 'Enchanted Acacia Log', exp = '16 Foraging', from = { item = 'Acacia Log', num = 160 } },
			},
			smelter_sc3000 = {
				{ item = 'Enchanted Coal', exp = '48 Mining', from = { item = 'Coal', num = 160 } },
				{ item = 'Enchanted Coal Block', exp = '7680 Mining', from = { item = 'Enchanted Coal', num = 160 } },
			},
		},
		recipes = {
			['Enchanted Acacia Log'] = { {'Acacia Log', 160 } },
		},
		stats = {
			{ tba = 48, storage = 64, crafting = { item = 'Acacia Log', num = 10, B2 = 'Wooden Axe' } },
			{ tba = 48, storage = 192, crafting = { item = 'Acacia Log', num = 20 } },
			{ tba = 45, storage = 192, crafting = { item = 'Acacia Log', num = 40 } },
			{ tba = 45, storage = 384, crafting = { item = 'Acacia Log', num = 64 } },
			{ tba = 42, storage = 384, crafting = { item = 'Enchanted Acacia Log', num = 1 } },
			{ tba = 42, storage = 576, crafting = { item = 'Enchanted Acacia Log', num = 2 } },
			{ tba = 38, storage = 576, crafting = { item = 'Enchanted Acacia Log', num = 4 } },
			{ tba = 38, storage = 768, crafting = { item = 'Enchanted Acacia Log', num = 8 } },
			{ tba = 33, storage = 768, crafting = { item = 'Enchanted Acacia Log', num = 16 } },
			{ tba = 33, storage = 960, crafting = { item = 'Enchanted Acacia Log', num = 32 } },
			{ tba = 27, storage = 960, crafting = { item = 'Enchanted Acacia Log', num = 64 } },
		},
		description = '&7Place this minion and it will/&7start generating and chopping/&7acacia logs! Requires an open/&7area to plant trees. Minions/&7also work when you are offline!'
	},
	['Jungle'] = {
		type = 'Foraging',
		collection = 'Jungle Log I',
		items = {
			{ item = 'Jungle Log', avg = 4, exp = 0.1 },
		},
		drops = {
			none = {
				{ item = 'Jungle Log', avg = 4, exp = '0.1 Foraging' },
			},
			smelter = {
				{ item = 'Coal', exp = '0.3 Mining', from = { item = 'Jungle Log', num = 1 } },
			},
			sc3000 = {
				{ item = 'Enchanted Jungle Log', exp = '16 Foraging', from = { item = 'Jungle Log', num = 160 } },
			},
			smelter_sc3000 = {
				{ item = 'Enchanted Coal', exp = '48 Mining', from = { item = 'Coal', num = 160 } },
				{ item = 'Enchanted Coal Block', exp = '7680 Mining', from = { item = 'Enchanted Coal', num = 160 } },
			},
		},
		recipes = {
			['Enchanted Jungle Log'] = { {'Jungle Log', 160 } },
		},
		stats = {
			{ tba = 48, storage = 64, crafting = { item = 'Jungle Log', num = 10, B2 = 'Wooden Axe' } },
			{ tba = 48, storage = 192, crafting = { item = 'Jungle Log', num = 20 } },
			{ tba = 45, storage = 192, crafting = { item = 'Jungle Log', num = 40 } },
			{ tba = 45, storage = 384, crafting = { item = 'Jungle Log', num = 64 } },
			{ tba = 42, storage = 384, crafting = { item = 'Enchanted Jungle Log', num = 1 } },
			{ tba = 42, storage = 576, crafting = { item = 'Enchanted Jungle Log', num = 2 } },
			{ tba = 38, storage = 576, crafting = { item = 'Enchanted Jungle Log', num = 4 } },
			{ tba = 38, storage = 768, crafting = { item = 'Enchanted Jungle Log', num = 8 } },
			{ tba = 33, storage = 768, crafting = { item = 'Enchanted Jungle Log', num = 16 } },
			{ tba = 33, storage = 960, crafting = { item = 'Enchanted Jungle Log', num = 32 } },
			{ tba = 27, storage = 960, crafting = { item = 'Enchanted Jungle Log', num = 64 } },
		},
		description = '&7Place this minion and it will/&7start generating and chopping/&7jungle logs! Requires an open/&7area to plant trees. Minions/&7also work when you are offline!'
	},
	['Flower'] = {
		type = 'Foraging',
		obtaining = '[[Dark Auction]]',
		items = {
				-- Amounts are approximate estimates, XP not tested
				{ item = 'Dandelion', avg = 0.35, onein = 2.86, exp = '0.1 Foraging' },
				{ item = 'Poppy', avg = 0.15, onein = 6.67, exp = '0.1 Foraging' },
				{ item = 'Allium', avg = 0.0417, onein = 24, exp = '0.1 Foraging' },
				{ item = 'Azure Bluet', avg = 0.0417, onein = 24, exp = '0.1 Foraging' },
				{ item = 'Blue Orchid', avg = 0.0417, onein = 24, exp = '0.1 Foraging' },
				{ item = 'Oxeye Daisy', avg = 0.0417, onein = 24, exp = '0.1 Foraging' },
				{ item = 'Red Tulip', avg = 0.0417, onein = 24, exp = '0.1 Foraging' },
				{ item = 'Orange Tulip', avg = 0.0417, onein = 24, exp = '0.1 Foraging' },
				{ item = 'White Tulip', avg = 0.0417, onein = 24, exp = '0.1 Foraging' },
				{ item = 'Pink Tulip', avg = 0.0417, onein = 24, exp = '0.1 Foraging' },
				{ item = 'Lilac', avg = 0.0417, onein = 24, exp = '0.2 Foraging' },
				{ item = 'Peony', avg = 0.0417, onein = 24, exp = '0.2 Foraging' },
				{ item = 'Rose Bush', avg = 0.0417, onein = 24, exp = '0.2 Foraging' },
				--{ item = 'Sunflower', avg = 0.0417, onein = 24, exp = '0.2 Foraging' },
		},
		drops = {
			none = {
				-- Amounts are approximate estimates, XP not tested
				{ item = 'Dandelion', avg = 0.35, onein = 2.86, exp = '0.1 Foraging' },
				{ item = 'Poppy', avg = 0.15, onein = 6.67, exp = '0.1 Foraging' },
				{ item = 'Allium', avg = 0.0417, onein = 24, exp = '0.1 Foraging' },
				{ item = 'Azure Bluet', avg = 0.0417, onein = 24, exp = '0.1 Foraging' },
				{ item = 'Blue Orchid', avg = 0.0417, onein = 24, exp = '0.1 Foraging' },
				{ item = 'Oxeye Daisy', avg = 0.0417, onein = 24, exp = '0.1 Foraging' },
				{ item = 'Red Tulip', avg = 0.0417, onein = 24, exp = '0.1 Foraging' },
				{ item = 'Orange Tulip', avg = 0.0417, onein = 24, exp = '0.1 Foraging' },
				{ item = 'White Tulip', avg = 0.0417, onein = 24, exp = '0.1 Foraging' },
				{ item = 'Pink Tulip', avg = 0.0417, onein = 24, exp = '0.1 Foraging' },
				{ item = 'Lilac', avg = 0.0417, onein = 24, exp = '0.2 Foraging' },
				{ item = 'Peony', avg = 0.0417, onein = 24, exp = '0.2 Foraging' },
				{ item = 'Rose Bush', avg = 0.0417, onein = 24, exp = '0.2 Foraging' },
				--{ item = 'Sunflower', avg = 0.0417, onein = 24, exp = '0.2 Foraging' },
			},
			sc3000 = {
				{ item = 'Enchanted Dandelion', exp = '16 Foraging', from = { item = 'Dandelion', num = 160 } },
				{ item = 'Enchanted Poppy', exp = '57.6 Foraging', from = { item = 'Poppy', num = 576 } }, -- exp not tested
			},
		},
		recipes = {
			['Enchanted Dandelion'] = { {'Dandelion', 160 } },
			['Enchanted Poppy'] = { {'Poppy', 576 } },
		},
		stats = {
			{ tba = 30, storage = 960, crafting = { item = 'Dandelion', num = 0, info = 'Bought from<br /&7>[[Dark Auction]]' } },
			{ tba = 29, storage = 960, crafting = { item = 'Dandelion', num = 20 } },
			{ tba = 28, storage = 960, crafting = { item = 'Dandelion', num = 40 } },
			{ tba = 27, storage = 960, crafting = { item = 'Dandelion', num = 64 } },
			{ tba = 26, storage = 960, crafting = { item = 'Enchanted Dandelion', num = 1 } },
			{ tba = 25, storage = 960, crafting = { item = 'Enchanted Dandelion', num = 3 } },
			{ tba = 24, storage = 960, crafting = { item = 'Enchanted Dandelion', num = 8 } },
			{ tba = 23, storage = 960, crafting = { item = 'Enchanted Dandelion', num = 16 } },
			{ tba = 22, storage = 960, crafting = { item = 'Enchanted Dandelion', num = 32 } },
			{ tba = 20, storage = 960, crafting = { item = 'Enchanted Dandelion', num = 64 } },
			{ tba = 18, storage = 960, crafting = { item = 'Enchanted Poppy', num = 1 } },
			{ tba = 15, storage = 960, crafting = { item = 'Enchanted Poppy', num = 2 } },
		},
		description = '&7Place this minion and it will/&7start generating and harvesting/&7flowers. Requires grass nearby/&7so flowers can be planted./&7Minions also work when you are/&7offline!'
	},
	--------------------------------
	-- Fishing
	--------------------------------
	['Fishing'] = {
		type = 'Fishing',
		collection = 'Raw Cod II',
		items = {
			-- according to data on Fishing Minion page | Fishing Minions collect an item EVERY action, instead of every other one
			{ item = 'Raw Cod', avg = 0.5*2, exp = 0.5 },
			{ item = 'Raw Salmon', avg = 0.25*2, exp = 0.7 },
			{ item = 'Pufferfish', avg = 0.12*2, exp = 1.0 },
			{ item = 'Tropical Fish', avg = 0.04*2, exp = 2.0 },
			{ item = 'Prismarine Crystals', avg = 0.03*2, exp = 0.25 },
			{ item = 'Prismarine Shard', avg = 0.03*2, exp = 0.25 },
			{ item = 'Sponge', avg = 0.03*2, exp = 0.5 },
		},
		drops = {
			none = {
				{ item = 'Raw Cod', avg = 0.5*2, exp = '0.5 Fishing' },
				{ item = 'Raw Salmon', avg = 0.25*2, exp = '0.7 Fishing' },
				{ item = 'Pufferfish', avg = 0.12*2, exp = '1 Fishing' },
				{ item = 'Tropical Fish', avg = 0.04*2, exp = '2 Fishing' },
				{ item = 'Prismarine Crystals', avg = 0.03*2, exp = '0.25 Fishing' }, -- exp not tested
				{ item = 'Prismarine Shard', avg = 0.03*2, exp = '0.25 Fishing' }, -- exp not tested
				{ item = 'Sponge', avg = 0.03*2, exp = '0.5 Fishing' },
			},
			sc3000 = {
				{ item = 'Enchanted Raw Cod', exp = '80 Fishing', from = { item = 'Raw Cod', num = 160 } },
				{ item = 'Enchanted Cooked Cod', exp = '12800 Fishing', from = { item = 'Enchanted Raw Cod', num = 160 } },
				{ item = 'Enchanted Raw Salmon', exp = '112 Fishing', from = { item = 'Raw Salmon', num = 160 } },
				{ item = 'Enchanted Cooked Salmon', exp = '17920 Fishing', from = { item = 'Enchanted Raw Salmon', num = 160 } },
				{ item = 'Enchanted Pufferfish', exp = '160 Fishing', from = { item = 'Pufferfish', num = 160 } },
				{ item = 'Enchanted Tropical Fish', exp = '320 Fishing', from = { item = 'Tropical Fish', num = 160 } },
				{ item = 'Enchanted Prismarine Crystals', exp = '40 Fishing', from = { item = 'Prismarine Crystals', num = 160 } }, -- exp not tested
				{ item = 'Enchanted Prismarine Shard', exp = '40 Fishing', from = { item = 'Prismarine Shard', num = 160 } }, -- exp not tested
				{ item = 'Enchanted Sponge', exp = '20 Fishing', from = { item = 'Sponge', num = 40 } },
				{ item = 'Enchanted Wet Sponge', exp = '800 Fishing', from = { item = 'Enchanted Sponge', num = 40 } },
			},
		},
		recipes = {
			['Enchanted Raw Cod'] = { {'Raw Cod', 160 } },
			['Enchanted Cooked Cod'] = { {'Enchanted Raw Cod', 160 } },
			['Enchanted Raw Salmon'] = { {'Raw Salmon', 160 } },
			['Enchanted Cooked Salmon'] = { {'Enchanted Raw Salmon', 160 } },
			['Enchanted Pufferfish'] = { {'Pufferfish', 160 } },
			['Enchanted Tropical Fish'] = { {'Tropical Fish', 160 } },
			['Enchanted Prismarine Crystals'] = { {'Prismarine Crystals', 160 } },
			['Enchanted Prismarine Shard'] = { {'Prismarine Shard', 160 } },
			['Enchanted Sponge'] = { {'Sponge', 40 } },
			['Enchanted Wet Sponge'] = { {'Enchanted Sponge', 40 } },
		},
		stats = {
			{ tba = 75, storage = 640, crafting = { item = 'Raw Cod', num = 8, B2 = 'Fishing Rod' } },
			{ tba = 75, storage = 640, crafting = { item = 'Raw Cod', num = 16 } },
			{ tba = 67, storage = 640, crafting = { item = 'Raw Cod', num = 32 } },
			{ tba = 67, storage = 704, crafting = { item = 'Raw Cod', num = 64 } },
			{ tba = 59, storage = 704, crafting = { item = 'Enchanted Raw Cod', num = 1 } },
			{ tba = 59, storage = 768, crafting = { item = 'Enchanted Raw Cod', num = 3 } },
			{ tba = 51, storage = 768, crafting = { item = 'Enchanted Raw Cod', num = 8 } },
			{ tba = 51, storage = 832, crafting = { item = 'Enchanted Raw Cod', num = 16 } },
			{ tba = 43, storage = 832, crafting = { item = 'Enchanted Raw Cod', num = 32 } },
			{ tba = 43, storage = 896, crafting = { item = 'Enchanted Raw Cod', num = 64 } },
			{ tba = 35, storage = 960, crafting = { item = 'Enchanted Cooked Cod', num = 1 } },
			{ tba = 30, storage = 960, crafting = { B3 = 'Fishing Minion XII Upgrade Stone' } },
		},
		description = '&7Place this minion and it will/&7start fishing. Requires water/&7nearby. Minions also work when/&7you are offline!'
	},
	['Clay'] = {
		type = 'Fishing',
		collection = 'Clay Ball I',
		items = {
			{ item = 'Clay Ball', avg = 4, exp = 0.1 },
		},
		drops = {
			none = {
				{ item = 'Clay Ball', avg = 4, exp = '0.1 Fishing' },
			},
			smelter = {
				{ item = 'Brick', exp = nil, from = { item = 'Clay Ball', num = 1 } }, -- exp not tested
			},
			compactor = {
				{ item = 'Clay', exp = '0.4 Fishing', from = { item = 'Clay Ball', num = 4 } },
			},
			smelter_compactor = {
				{ item = 'Bricks', exp = nil, from = { item = 'Brick', num = 4 } }, -- exp not tested
			},
			sc3000 = {
				{ item = 'Enchanted Clay Ball', exp = '16 Fishing', from = { item = 'Clay Ball', num = 160 } },
			},
		},
		recipes = {
			['Enchanted Clay Ball'] = { {'Clay Ball', 160 } },
		},
		stats = {
			{ tba = 32, storage = 64, crafting = { item = 'Clay Ball', num = 10, B2 = 'Wooden Shovel' } },
			{ tba = 32, storage = 192, crafting = { item = 'Clay Ball', num = 20 } },
			{ tba = 30, storage = 192, crafting = { item = 'Clay Ball', num = 40 } },
			{ tba = 30, storage = 384, crafting = { item = 'Clay Ball', num = 64 } },
			{ tba = 27.5, storage = 384, crafting = { item = 'Enchanted Clay Ball', num = 1 } },
			{ tba = 27.5, storage = 576, crafting = { item = 'Enchanted Clay Ball', num = 2 } },
			{ tba = 24, storage = 576, crafting = { item = 'Enchanted Clay Ball', num = 4 } },
			{ tba = 24, storage = 768, crafting = { item = 'Enchanted Clay Ball', num = 8 } },
			{ tba = 20, storage = 768, crafting = { item = 'Enchanted Clay Ball', num = 16 } },
			{ tba = 20, storage = 960, crafting = { item = 'Enchanted Clay Ball', num = 32 } },
			{ tba = 16, storage = 960, crafting = { item = 'Enchanted Clay Ball', num = 64 } },
			{ tba = 14, storage = 960, crafting = { B3 = 'Clay Minion XII Upgrade Stone' } },
		},
		description = '&7Place this minion and it will/&7start generating and mining/&7clay! Requires an open area to/&7place clay. Minions also work/&7when you are offline!'
	},
}
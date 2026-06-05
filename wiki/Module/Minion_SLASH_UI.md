local loader = require('Module:Loader')

local string, table, yesno, arguments, inventoryslot, craftingui, Interface, minionMdl =
	loader.lazy.require('String', 'Table', 'Yesno', 'Arguments', 'Inventory slot', 'Crafting/UI', 'UI/Core', 'Minion')

local getArgs = arguments.getArgs
local title = mw.title.getCurrentTitle().text

local p = {}

-- NPC text for p.minionUI
local npctext = {
	['Bulvar'] = {name = '&5Bulvar', loc = '&2Dwarven Mines'},
	['Tony'] = {name = '&5Tony', loc = '&bTrappers Den'},
}
npctext['Terry'] = npctext['Tony']

-----------------------------------------------------------------------------
-- Template:Minion recipe gallery
--
-- Makes a table of {{Slot}} to form the in-game ideal layout for a minion
-----------------------------------------------------------------------------
function p.minionRecipeGallery( frame )
	--local parameters = frame.args
	local args = getArgs(frame)
	
	local minion = args['minion'] or args[1]
	if not minion then minion = title end
	
	return p._minionRecipeGallery( minion )
end
function p._minionRecipeGallery( minionName )
	local minion = minionMdl.getMinion(minionName)
	
	-- Get a list of the desired tiers
	local tiers = {}
	local start = minion.stats[1] and (minion.stats[1].crafting.info and 2 or 1)
	
	local _, nCraftable = minionMdl.peakStat(minionName)
	for i = start, nCraftable do tiers[#tiers + 1] = i end
	
	-- Generate crafting tables
	local tables = {}
	for _,tier in ipairs(tiers) do
		local grid = minionMdl._getRecipe( minionName, tier )
		tables[#tables + 1] = grid and craftingui.craftingGrid(grid) or nil
	end
	
	-- Display all crafting tables in a grid
	local grid = mw.html.create('table')
	local row
	
	for i, ct in pairs(tables) do
		if (i - 1) % 3 == 0 then
			if row then row:done() end
			row = grid:tag('tr')
		end
		row:tag('td'):wikitext(ct):done()
	end
	
	row:done()
	grid:done()
	
	return tostring(grid)
end

-----------------------------------------------------------------------------
-- Template:Minion animated crafting table
--
-- Make an animated {{Crafting Table}} of all potential minion crafting recipes
-----------------------------------------------------------------------------
function p.minionAnimatedCraftingTable( frame )
	-- local parameters = frame.args
	local args = getArgs(frame)
	
	local minion = args['minion'] or args[1] or title
	local item = args['item']
	local from = args['from']
	local to = args['to']
	
	return mw.getCurrentFrame():preprocess(p._minionAnimatedCraftingTable( minion, item, from, to ))
end
function p._minionAnimatedCraftingTable( minionName, item, from, to )
	local function includes(tb, item)
		for k, v in pairs(tb) do
			if not tonumber(v) and v == item then return true end
		end
		return false
	end
	
	local minion = minionMdl.getMinion(minionName)
	local highestTier, highestCraftable = minionMdl.peakStat(minionName)
	
	-- Get a list of the desired tiers
	local tiers = {}
	if item then
		for i = 1, highestCraftable, 1 do
			local recp = minionMdl._getRecipe(minionName, i, 'materials')
			if table.some(recp or {}, function (k, v)
				return v.item == item
			end) then
				tiers[#tiers + 1] = i
			end
		end
		--ignore .info
	elseif from and to then
		if not tonumber(from) or not tonumber(to) then
			error('Range is not correct')
		end
		from, to = tonumber(from), tonumber(to)
		if not minion.stats[from] or not minion.stats[to] then
			error('Range is not correct')
		end
		if from > to then
			from, to = to, from
		end
		
		for i = from, to, 1 do tiers[#tiers + 1] = i end
	else
		local start = minion.stats[1].crafting.info and 2 or 1
		for i = start, highestCraftable, 1 do tiers[#tiers + 1] = i end
	end
	
	return ('{{Crafting Table%s}}'):format(table.concat(table.map(tiers, function(v)
		return ('|%s Minion %s'):format(minionName, string._toRoman(v))
	end)))
end

-----------------------------------------------------------------------------
-- Template:Minion ideal layout
--
-- Makes a table of {{Slot}} to form the in-game ideal layout for a minion
-----------------------------------------------------------------------------
function p.minionIdealLayoutTable( frame )
	--local parameters = frame.args
	local args = getArgs(frame)
	
	local minion = args['minion'] or args[1] or title
	local ideal = args['ideal']
	local border = args['border']
	local size = 5
	
	local slots = {}
	local rowLetter = { 'A', 'B', 'C', 'D', 'E', }
	for y = 1,size,1 do
		slots[y] = {}
		for x = 1,size,1 do
			slots[y][x] = args[rowLetter[x] .. y]
		end
	end
	
	return p.minionIdealLayout( minion, size, ideal, border, slots )
end

function p.minionIdealLayout( minion, size, ideal, border, customSlots )
	if border then size = size + 2 end
	local layoutUI = Interface({
		rows = size,
		cols = size,
		inline = true,
		noarrow = true,
		noclose = true,
	})
	for y = 1, size, 1 do
		for x = 1, size, 1 do
			local img
			if border and (y == 1 or y == size or x == 1 or x == size) then
				img = border
			elseif x == math.ceil(size / 2) and y == math.ceil(size / 2) then
				img = ('%s I'):format(minion)
				if customSlots[y][x] then
					img = ('%s;%s'):format(img, customSlots[y][x])
				end
			else
				img = border and (customSlots[y - 1][x - 1] or ideal) or (customSlots[y][x] or ideal)
			end
			layoutUI:setSlot(x, y, { img })
		end
	end
	return tostring(layoutUI)
end

-----------------------------------------------------------------------------
-- Template:Minion UI
--
-- Makes a table of {{Slot}} to form the in-game UI of a minion
-----------------------------------------------------------------------------
function p.minionUI( frame )
	--local parameters = frame.args
	local args = getArgs(frame)
	local minion = args['minion'] or args[1] or title
	return p._minionUI( minion )
end

function p._minionUI( minion )
	local name, tier = minion:match('(.-)%s?[Mm]?[Ii]?[Nn]?[Ii]?[Oo]?[Nn]?%s([%divxIVX]+)')
	if tier then
		tier = tonumber(tier) or string._toArabic(tier)
	else
		name = minion:gsub('%s*[Mm][Ii][Nn][Ii][Oo][Nn]', '')
		tier = 1
	end
	
	local dt = minionMdl.getMinion(name)
	if not dt.stats[tier] then
		error(name .. 'Minion has no such tier (Tier ' .. tier .. ')')
	end
	
	local highestTier, highestCraftable = minionMdl.peakStat(name)
	
	local storageTier = {}
	
	for slotno = 1, 15, 1 do -- Minions have 15 total slots
		for y = 1, 10, 1 do -- All slots unlocked at tier 10
			local avail = dt.stats[y].storage / 64
			storageTier[slotno] = y
			if avail >= slotno then
				break
			end
		end
	end
	
	local function available( num )
		if tier >= storageTier[num]
			then return { '' } -- Empty Slot
			else return {
				'White Stained Glass Pane',
				title = '&ePenyimpanan terbuka pada tingkat ' .. string._toRoman(storageTier[num]),
				text = 'none',
				link = 'none',
			}
		end
	end
	
	local title = name .. ' Minion ' .. string._toRoman(tier)
	local titleLink = name .. ' Minion#' .. string._toRoman(tier)
	local upgradeMessage = ''
	local upgradeMessageView = ''
	local upgradeMessageUpgrade = ''
	
	if tier == highestTier then
		upgradeMessage = '&aTingkat tertinggi telah dicapai!'
		upgradeMessageView = 'Tingkat tertinggi dari minion ini/telah dicapai//' .. upgradeMessage
		upgradeMessageUpgrade = '&cMinion ini telah mencapai/tingkat maksimum.'
	elseif tier == highestCraftable then
		local tradenpc = dt.stats[tier + 1].tradeNpc
		upgradeMessage = '&aTingkat tertinggi yang bisa dibuat telah/&adicapai!'
		upgradeMessageView = '&7Tingkat tertinggi yang bisa dibuat dari/&7minion ini telah dicapai/&7Bicara dengan ' .. (npctext[tradenpc] and npctext[tradenpc].name or tradenpc) .. ' &r&7in the/&7' .. (npctext[tradenpc] and npctext[tradenpc].loc or '(unknown)') .. ' &r&7untuk membuka/tingkat berikutnya!//' .. upgradeMessage
		upgradeMessageUpgrade = '&cThis minion has reached the/&cmaximum tier.'
	elseif dt.stats[tier + 1].storage > dt.stats[tier].storage then
		upgradeMessage = '&7Waktu Antar Aksi: &e' .. dt.stats[tier].tba .. 's/&7Penyimpanan Maksimal: &8' .. dt.stats[tier].storage .. ' ➜ &a' .. dt.stats[tier + 1].storage
		upgradeMessageView = '&7Lihat item yang dibutuhkan untuk/&7meningkatkan minion ini ke/&7tingkat berikutnya.//' .. upgradeMessage .. '//&eKlik untuk melihat!'
		upgradeMessageUpgrade = upgradeMessage .. '//&eKlik untuk meningkatkan!'
	else
		upgradeMessage = '&7Waktu Antar Aksi: &8' .. dt.stats[tier].tba .. 's ➜ &a' .. dt.stats[tier + 1].tba .. 's/&7Penyimpanan Maksimal: &e' .. dt.stats[tier].storage
		upgradeMessageView = '&7Lihat item yang dibutuhkan untuk/&7meningkatkan minion ini ke/&7tingkat berikutnya.//' .. upgradeMessage .. '//&eKlik untuk melihat!'
		upgradeMessageUpgrade = upgradeMessage .. '//&eKlik untuk meningkatkan!'
	end
	
	local ui = Interface({
		title,
		noarrow = true,
		noclose = true,
	})
	ui:setSlot(1, 4, {
		'Redstone Torch',
		title = '&aTata Letak Ideal',
		text = '&7Lihat letak paling efisien untuk/&7menempatkan minion ini.',
		link = 'none',
	})
	ui:setSlot(1, 5, {
		title,
		title = '&9' .. title,
		text = ('&7%s//&7Waktu Antar Aksi: &a%ss/&7Penyimpanan Maksimal: &e%s/&7Sumber Daya Dihasilkan: &b0'):format(
			dt.description or 'Tidak ada deskripsi',
			dt.stats[tier].tba, dt.stats[tier].storage
		),
	})
	ui:setSlot(1, 6, {
		'Gold Ingot',
		title = '&aTingkat Berikutnya',
		text = upgradeMessageView,
		link = 'none',
	})
	ui:setSlot(2, 2, {
		'Lime Stained Glass Pane',
		title = '&aSlot Skin Minion',
		text = '&7Kamu bisa memasukkan Skin Minion/&7di sini untuk mengubah penampilan/&7dari minion milikmu.',
		link = 'none',
	})
	ui:setSlot(3, 2, {
		'Orange Stained Glass Pane',
		title = '&aBahan Bakar',
		text = '&7Tingkatkan kecepatan/&7minion kamu dengan menambahkan item bahan bakar/&7di sini.//&cCatatan: &7Kamu tidak bisa mengambil/&7bahan bakar kembali setelah/&7kamu meletakkannya di sini!',
		link = 'none',
	})
	ui:setSlot(4, 2, {
		'Blue Stained Glass Pane',
		title = '&aPengiriman Otomatis',
		text = '&7Add a &bBudget Hopper&7\\,/&bEnchanted Hopper&7 or a/&bPerfect Hopper&7 here to make/&7your minion automatically sell/&7generated items after its/&7inventory is full.',
		link = 'none',
	})
	ui:setSlot(5, 2, {
		'Yellow Stained Glass Pane',
		title = '&aSlot Peningkatan',
		text = '&7Kamu bisa meningkatkan minion kamu dengan/&7menambahkan item peningkatan minion/&7di sini.',
		link = 'none',
	})
	ui:setSlot(6, 2, {
		'Yellow Stained Glass Pane',
		title = '&aSlot Peningkatan',
		text = '&7Kamu bisa meningkatkan minion kamu dengan/&7menambahkan item peningkatan minion/&7di sini.',
		link = 'none',
	})
	ui:setSlot(6, 4, {
		'Chest',
		title = '&aKumpulkan Semua',
		text = '&eKlik untuk Mengumpulkan semua item!',
		link = 'none',
	})
	ui:setSlot(6, 6, {
		'Diamond',
		title = '&aPeningkatan Cepat Minion',
		text = '&7Klik di sini untuk meningkatkan/&7minion kamu ke tingkat berikutnya.//' .. upgradeMessageUpgrade,
		link = 'none',
	})
	ui:setSlot(6, 9, {
		'Bedrock',
		title = '&aAmbil Minion',
		text = '&eKlik untuk mengambil!',
		link = 'none',
	})
	
	for i = 0, 14, 1 do
		ui:setSlot(math.floor(i / 5) + 3, i % 5 + 4, available(i + 1))
	end
	
	return tostring(ui)
end

return p
-- Module:Cache
-- Provides cache helpers for Module:Inventory slot, Module:UI, etc.

local p = {}

-- Simple in-memory cache object (no VarsCacheMap dependency)
local function makeSimpleCache()
	local store = {}
	return {
		get = function(self, key, mode)
			return store[key]
		end,
		set = function(self, key, value)
			store[key] = value
		end,
	}
end

-- Inventory slot caches (simplified — always miss, so aliases from loadData are used instead)
p.invslotCache1 = makeSimpleCache()
p.invslotCache2 = makeSimpleCache()
p.slotAliasesCache = makeSimpleCache()

-- Item Variants cache (simplified — always miss)
p.itemVariantsCache = makeSimpleCache()

-- Other caches
p.itemApiDataCache    = makeSimpleCache()
p.itemApiAliasesCache = makeSimpleCache()
p.craftingAliasesCache = makeSimpleCache()
p.minionDataCache     = makeSimpleCache()

-- Tooltips Cache Access, for Module:Inventory slot and Module:Collection/UI
function p.getInvslotCache(key, mode)
	if key == nil then return nil end
	return p.invslotCache1:get(key, mode) or p.invslotCache2:get(key, mode)
end

function p.refreshSlotAliasesCache()
	-- no-op in simplified version
end

return p

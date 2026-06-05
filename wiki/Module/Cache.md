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
local function makeVariantsCache()
	local variantsTable = nil
	return {
		get = function(self, key, mode)
			if variantsTable == nil then
				local status, variantsModule = pcall(require, 'Module:Item/Variants')
				if not status then
					error("Failed to load Module:Item/Variants: " .. tostring(variantsModule))
				end
				variantsTable = variantsModule or {}
			end
			return variantsTable[key]
		end,
		set = function(self, key, value)
		end,
	}
end
p.itemVariantsCache = makeVariantsCache()
local function makeModuleCache(moduleName)
	local cachedTable = nil
	return {
		get = function(self, key, mode)
			if cachedTable == nil then
				local status, mod = pcall(require, moduleName)
				if not status then
					error("Failed to load " .. moduleName .. ": " .. tostring(mod))
				end
				cachedTable = mod or {}
			end
			if cachedTable.items and cachedTable.lastUpdated then
				return cachedTable.items[key]
			end
			return cachedTable[key]
		end,
		set = function(self, key, value)
		end,
	}
end

-- Other caches
p.itemApiDataCache    = makeModuleCache('Module:Item/ApiData')
p.itemApiAliasesCache = makeModuleCache('Module:Item/ApiAliases')
p.craftingAliasesCache = makeModuleCache('Module:Crafting/Aliases')
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
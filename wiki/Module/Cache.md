-- <pre>
local varsCacheMap = require('Module:VarsCacheMap')
local cacheUtil = require('Module:CacheUtil')

local p = {}

-- Inventory slot
local INVSLOT_1_PREFIX = 'invslot_02_'--don't index number unless cache has gone to complete hell; don't change this variable unless you know what you're doing please
p.invslotCache1 = varsCacheMap.create({ prefix=INVSLOT_1_PREFIX, dataModule='Inventory slot/Datasheet' })
local INVSLOT_2_PREFIX = 'invslot_03_'
p.invslotCache2 = varsCacheMap.create({ prefix=INVSLOT_2_PREFIX, dataModule='Inventory slot/Datasheet' })

local SLOT_ALIASES_PREFIX = 'slotaliases_04_'
p.slotAliasesCache = varsCacheMap.create({ prefix=SLOT_ALIASES_PREFIX, dataModule='Inventory slot/Aliases' })

-- Item Variants
local ITEM_VARIANTS_PREFIX = 'itemvariants_01_'
p.itemVariantsCache = varsCacheMap.create({ prefix=ITEM_VARIANTS_PREFIX, dataModule='Item/Variants' })
-- Item API data
local ITEM_API_DATA_PREFIX = 'itemapidata_01_'
p.itemApiDataCache = varsCacheMap.create({ prefix=ITEM_API_DATA_PREFIX, dataModule='Item/ApiData/AsCacheTable' })
-- Item API aliases
local ITEM_API_ALIASES_PREFIX = 'itemapialiases_01_'
p.itemApiAliasesCache = varsCacheMap.create({ prefix=ITEM_API_ALIASES_PREFIX, dataModule='Item/ApiAliases' })

-- Crafting aliases
local CRAFTING_ALIASES_PREFIX = 'craftingaliases_01_'
p.craftingAliasesCache = varsCacheMap.create({ prefix=CRAFTING_ALIASES_PREFIX, dataModule='Crafting/Aliases' })

-- Crafting aliases
local MINION_DATA_PREFIX = 'miniondata_01_'
p.minionDataCache = varsCacheMap.create({ prefix=MINION_DATA_PREFIX, dataModule='Minion/Data' })

--------------------------
-- Cache Refresh Helpers
--------------------------
-- called by tooltip editor
function p.refreshSlotAliasesCache()
	p.slotAliasesCache:refreshCache()
end

-- Tooltips Cache Access, for Module:Inventory slot and Module:Collection/UI
function p.getInvslotCache(key, mode)
    if (key == nil) then
    	return nil
    end
    
    if (cacheUtil.whichTooltipCache(key) == 1) then
        return p.invslotCache1:get(key, mode)
    else
        return p.invslotCache2:get(key, mode)
    end
end

return p

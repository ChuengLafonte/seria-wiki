local util_vars = require('Module:VariablesLuaUtil')
local makeClass = require('Module:Class')
local libU = require('Module:LibU')
local cache = require('mw.ext.LuaCache')

local p = {}

local lang = mw.getLanguage('en')

local Cache = makeClass "Cache"

local checkType = libU.checkType

function Cache.prototype:constructor(attrs)
	checkType(1, attrs, 'table', true)
	attrs = attrs or {}
	
	self.prefix = attrs.prefix
	self.dataModule = attrs.dataModule
	
	return self
end

function Cache.prototype:makeKey(localKey)
	return self.prefix .. lang:lc(localKey)
end

-- localKey is the key found in the source data file
-- Modes: 0-Default 1-No Fallback (not loadData in any circumstanace)
function Cache.prototype:get(localKey, mode)
	mode = mode or 0
	local key = self:makeKey(localKey)
	
	-- Get from variable storage (page storage, fastest)
	local data = util_vars.getObject(key)
	if not data then
		-- Else get from cache (site storage, slower but still fast)
		data = cache.get(key)
		if not data and mode ~= 1 then
			-- Otherwise fallback to accessing data from `loadData`
			-- We shouldn't hit here ideally, but best to have a fallback
			-- Note: cache should be pre-populated to avoid falling back here, this is only meant as a backup
			data = mw.loadData('Module:'..self.dataModule)[localKey]
			-- update cache for future calls
			cache.set(key, data)
		end
		-- update vars for future calls
		util_vars.setObject(key, data)
	end
	return data
end

-- Note: this shouldn't be used inside normal modals, and should only be called by refresh scripts
function Cache.prototype:addAllDataToCache()
	local data = require('Module:'..self.dataModule) -- has to be a require to allow looping
	for key, val in pairs(data) do
		-- mw.log( self:makeKey(key) )
		cache.set(self:makeKey(key), val)
	end
end

-- Deletes all keys pertaining to this cache, to allow for a cleaner refresh
-- Note: this shouldn't be used inside normal modals, and should only be called by refresh scripts
function Cache.prototype:deleteCache()
	local data = require('Module:'..self.dataModule) -- has to be a require to allow looping
	for key, _ in pairs(data) do
		cache.delete(self:makeKey(key))
	end
end

function Cache.prototype:refreshCache()
	self:deleteCache()
	self:addAllDataToCache()
end

function p.create(attrs)
	return Cache(attrs)
end

return p

-- <pre>
-- Modul utilitas untuk manajemen cache di Scribunto Lua.

local getArgs = require('Module:Arguments').getArgs
local cache = require('mw.ext.LuaCache')

local h = {}

local p = {}
function p.query(frame)
	local args = getArgs( mw.getCurrentFrame() )
	local data = cache.get(args[1])
	if not data then
		return ('Cache does not exist for %s'):format(args[1])
	end
	local tbl = {}
	for k, v in pairs(data) do
		tbl[#tbl+1] = k .. ', ' .. tostring(v)
	end
	return table.concat(tbl,'<br>')
end

function p.delete(frame)
	local args = getArgs( mw.getCurrentFrame() )
	return cache.delete(args[1])
end

function p.set(frame)
	local args = getArgs( mw.getCurrentFrame() )
	return p._set(args[1], args[2])
end

function p._set(key, value)
	return cache.set(key, value)
end

function p.get(frame)
	local args = getArgs( mw.getCurrentFrame() )
	return p._get(args[1])
end

function p._get(key)
	local ret = cache.get(key)
	return ret
end

function p.deleteAll(frame)
	local args = getArgs( frame or mw.getCurrentFrame() )
	local data = require('Module:' .. args[1])
	local prefix = args.prefix or ''
	for key, _ in pairs(data) do
		cache.delete(prefix .. key)
	end
end

function p.resetAll(frame)
	local args = getArgs( mw.getCurrentFrame() )
	p.deleteAll(frame)
	local data = require('Module:' .. args[1])
	local f = require('Module:' .. args.module)[args.f or 'main']
	for key, _ in pairs(data) do
		f(key)
	end
end

local varsCacheMap = require('Module:VarsCacheMap')
function p.resetTooltips(frame)
	local args = getArgs( mw.getCurrentFrame() )
	p.deleteAll({args[1], prefix = args.prefix1})
	p.deleteAll({args[1], prefix = args.prefix2})

	prefix1 = args.prefix1
	prefix2 = args.prefix2

    local data = require('Module:' .. args[1])
	for key, val in pairs(data) do
        if (p.whichTooltipCache(key) == 1) then
			p._set(makeKey(prefix1, key), val)
		else
			p._set(makeKey(prefix2, key), val)
		end
	end
end

local lang = mw.getLanguage('en')

function makeKey(prefix, localKey)
	return prefix .. lang:lc(localKey)
end

function p.whichTooltipCache(key)
	first_char_code = string.byte(string.lower(key), 1)
	if (first_char_code == nil) then
		return nil
	end
	
	if (first_char_code < 109) then
    	return 1
	else
		return 2
	end
end

function p.resetAllSimple(frame)
	local args = getArgs( frame or mw.getCurrentFrame() )
	p.deleteAll(frame)
	varsCacheMap.create{ prefix=args.prefix, dataModule=args[1] }:addAllDataToCache()
end

return p

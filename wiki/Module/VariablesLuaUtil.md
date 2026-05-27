-- Code from: https://lol.fandom.com/wiki/Module:VarsUtil
-- Helper module for accessing https://www.mediawiki.org/wiki/Extension:VariablesLua
local yesno = require ('Module:Yesno')
local binser = require('binser') -- included with install of mw.ext.LuaCache
local VariablesLua = mw.ext.VariablesLua

local p = {}

function p.getVar(var)
	local val = VariablesLua.var(var)
	if val == '' then
		return nil
	end
	return val
end

function p.getBool(var)
	local val = p.getVar(var)
	return yesno(val) -- util_args.castAsBool(val)
end

function p.setBool(var, val)
	if type(val) == 'string' then
		val = yesno(val) -- util_args.castAsBool(val)
	end
	if val then
		p.setVar(var, 'Yes')
		return
	end
	p.setVar(var, 'No')
end

function p.setVar(var, val)
	VariablesLua.vardefine(var, val)
	return val
end

function p.setVarOnlyIf(var, val)
	if not val then return end
	p.setVar(var, val)
end

function p.getGlobalIndex(name)
	local val = p.getVar('luaGlobalIndex' .. name)
	return tonumber(val) or 0
end

function p.setGlobalIndex(name)
	local n = p.getGlobalIndex(name) + 1
	p.setVar('luaGlobalIndex' .. name, n)
	return n
end

function p.resetGlobalIndex(name, val)
	val = val or 0
	p.setVar('luaGlobalIndex' .. name, val)
	return val
end

function p.appendToList(name, val, sep)
	-- this is just for helping to debug and shouldn't actually be used ever probably
	sep = sep or ', '
	local old_val = p.getVar(name) or ''
	p.setVar(name, old_val .. sep .. val)
end

function p.log(val)
	if type(val) == 'table' then
		p.logObject(val)
		return
	end
	p.appendToList('log', tostring(val))
end

function p.logObject(val)
	local tbl = {}
	for k, v in pairs(val) do
		tbl[#tbl+1] = k .. ': ' .. tostring(v)
	end
	p.appendToList('log', table.concat(tbl,', '))
end

function p.clearAll(tbl)
	for _, v in ipairs(tbl) do
		p.setVar(v, '')
	end
end

function p.setTypedVar(var, val)
	local val_to_store = binser.serialize(val)
	p.setVar(var, val_to_store)
end

function p.getTypedVar(var)
	local val = p.getVar(var)
	if not val then
		return nil
	end
	return binser.deserialize(val)[1]
end

local LEADING_MARKER = '"'
local TRAILING_MARKER = '"'

function p.setObject(var, val)
	local val_to_store = LEADING_MARKER .. binser.serialize(val) .. TRAILING_MARKER -- "Markers" to ensure leading and trailing spaces are preserved.
	p.setVar(var, val_to_store)
end

function p.getObject(var)
	local val = p.getVar(var)
	if not val then
		return nil
	end
	-- code below is hardcoded version of: val = val:sub(#LEADING_MARKER + 1, -(#TRAILING_MARKER + 1))
    val = val:sub(2, -2) -- Get contents within "Marker"
	return binser.deserialize(val)[1]
end

return p
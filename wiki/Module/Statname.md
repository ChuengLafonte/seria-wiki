local getArgs = require('Module:Arguments').getArgs
local loader = require('Module:Loader')

local string, stringT, yesno, color, safeResponse = loader.require('String', 'String/Templates', 'Yesno', 'Color', 'SafeResponse')

local aliases, statData = loader.loadData('Statname/Aliases', 'Statname/Data')

local p = {}

-- <SafeResponse:enabled>
function p._getstatdata(statname, noerrormsg)
	if type(statname) ~= 'string' then
		if noerrormsg then
			return nil
		end
		error({ type='Statname/BadStat', format={tostring(_stat)} })
	end
	
	local stat = string.trim(tostring(statname):lower()):gsub('_', ' ')
	local dt = statData[aliases[stat] or stat]
	
	if not dt then
		for k, v in pairs(statData) do
			if stat == v.name:lower()
				or stat == v.shortcode:lower()
				or stat == v.nameShort:lower()
				or stat == v.nameSuperShort:lower() then
				dt = v
				break
			end
		end
	end
	
	if not dt then
		if noerrormsg then
			return nil
		end
		error({ type='Statname/BadStat', format={tostring(_stat)} })
	end
	
	return dt
end

---------------------------------------------------------------------------------
-- Template: Statname
-- 
-- Makes a formatted stat with an image
---------------------------------------------------------------------------------
function p.stat(frame)
	local args = getArgs(frame)
	local short = args[3] or args['short']
	
	local success, result = safeResponse.call(p._stat, {
		stat = args[1],
		valBefore = args[2],
		isShort = yesno(short),
		isSuperShort = short == 'ss',
		isCram = args.cram,
		icononly = args.icononly,
	})
	return result
end

---------------------------------------------------------------------------------
-- function: stat(stat, valBefore, isShort, isSuperShort)
-- 
-- Makes a formatted stat with an image
-- <SafeResponse:enabled>
---------------------------------------------------------------------------------
function p._stat(...)
	local _stat, valBefore, isShort, isSuperShort, isCram, icononly
	if type(({...})[1]) == 'table' then
		local u = ({...})[1]
		_stat, valBefore, isShort, isSuperShort, isCram, icononly =
			u.stat or u[1],
			u.valBefore,
			u.isShort,
			u.isSuperShort,
			u.isCram,
			u.icononly
	else
		_stat, valBefore, isShort, isSuperShort, isCram, icononly = ...
	end
	if not _stat then
		error({ type='Statname/BadStat', format={tostring(_stat)} })
	end
	local tValBefore, stat = _stat:lower():match('^([%-%+]?[%d%.]+%%?)%s*(.+)$')
	
	if not stat then
		stat = _stat
	else
		valBefore = tValBefore
	end
	
	stat = p._getstatdata(stat, true)
	if not stat then
		error({ type='Statname/BadStat', format={tostring(_stat)} })
	end
	
	local text = stat.character .. (icononly and '' or '&nbsp;' .. (isSuperShort and stat.nameSuperShort or (isShort and stat.nameShort or stat.name)))
	
	return string.wrapHtml{
		{
			valBefore and color.colorText(stat.color, valBefore) .. '&nbsp;' or '',
			string.makeLink(
				stat.link or stat.name,
				color.colorText(stat.color, text)
			)
		},
		'<span>', {
			class = 'hsw-gamefont ' .. (isCram and ' cram' or '')
		}
	}
end

---------------------------------------------------------------------------------
-- Template: StatSymbol
-- 
-- Makes a stat symbol, formatted only with the hsw-gamefont CSS class
---------------------------------------------------------------------------------
function p.statSymbol(frame)
	local args = getArgs(frame)
	
	local success, result = safeResponse.call(p._statSymbol, {
		stat = args[1]
	})
	return result
end

---------------------------------------------------------------------------------
-- function: statSymbol(stat)
-- 
-- Rerturns a stat symbol, formatted only with the hsw-gamefont CSS class
-- <SafeResponse:enabled>
---------------------------------------------------------------------------------
function p._statSymbol(...)
	local _stat
	if type(({...})[1]) == 'table' then
		local u = ({...})[1]
		_stat = u.stat or u[1]
	else
		_stat, _ = ...
	end
	
	if not _stat then
		error({ type='Statname/BadStat', format={tostring(_stat)} })
	end
	
	local stat = p._getstatdata(_stat, true)
	if not stat then
		error({ type='Statname/BadStat', format={tostring(_stat)} })
	end
	
	return string.wrapHtml{
		{ stat.character },
		'<span>', {
			class = 'hsw-gamefont'
		}
	}
end

---------------------------------------------------------------------------------
-- function: isStatAlias(s: string)
-- 
-- Checks if a string is a valid stat name or alias.
---------------------------------------------------------------------------------
function p.isStatAlias(s)
	return not not aliases[s]
end

-- For backwards compatabillity
p.getStatName = p.stat
p._getStatName = p._stat

return p
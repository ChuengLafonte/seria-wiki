--<pre>
--Start Module
local p = {}

--Get Other Required Modules
local getArgs = require([[Module:Arguments]]).getArgs
local string = require([[Module:String]])
local yesno = require('Module:Yesno')

--Invokes {{IfNot}}
--Gets Input from template
function p.ifNot(frame)
    local args = getArgs(frame)
    
    --Local Arguments
    local a = args[1]
    local b = args[2]
    local c = args[3]
    
    return p._ifNot(a, b , c)
end

--{{IfNot}} Module Access Point
function p._ifNot(a, b, c)
    if not a or a == '' or a == nil or a == false
        then return b
        else return c
    end
end

--Invokes{{IfString}}
--Gets Input From Template
function p.ifString(frame)
    local args = getArgs(frame)
    
    --Local Arguments
    local a = args[1]
    local b = args[2]
    local c = args[3] or ""
    local d = args[4] or ""
    
    if not a or not b then return _error('\"IfString\" requires at least 2 arguments.') end

    local success, response = pcall(p._ifString, a, b, c, d)
    return success and response or string.error(response)
end

--{{IfString}} Module Access point
function p._ifString(a, b, c, d)
    
    if string.match(a, b)
        then return c
        else return d
    end
end

function p.len(frame)
    local args = getArgs(frame)
    local str = args[1]
    
    if not str then return _error('Invalid Arguments: \"Len\" requires inputs.') end
    
    return string.len(str)
end

---------------------------------------------------------------------------------
-- Template: Sub
--
-- returns a substring of the length specified by the limit
---------------------------------------------------------------------------------
function p.sub(frame)
    local args = getArgs(frame)
    local str = args[1]
    local start = args[2]
    local len = args[3]
    
    return string.sub(str, start, len)
end

function p.replace(frame)
    local args = getArgs(frame, {removeBlanks = false, trim=false})
    
    local text = args[1]
    local search = args[2]
    local repl = args[3]
    local lim = args[4]
    
    if not search or not text then return _error('\"replace\" requires at least 2 arguments.') end
    
    return p._replace(text, search, repl, lim)
end

local replTable = {
	['t'] = '\t',
	['n'] = '\n',
	['r'] = '\r',
	['v'] = '\v',
	['b'] = '\b',
	['a'] = '\a',
}

function p._replace(text, search, repl, lim)
    local ret = string.gsub(text, search:gsub('\\(%a)', replTable), repl or '', tonumber(lim))
    
    return ret
end

function p.pos(frame)
	local args = getArgs(frame)
	local target_str = args[1] or ''
	local pos = tonumber(args[2]) or 0

	if pos == 0 or math.abs(pos) > string.len(target_str) then
		return _error('String index out of range')
	end

	return string.sub(target_str, pos, pos)
end

function p.ifNotEq(frame)
    local args = getArgs(frame)

    local text1 = args[1]
    local text2 = args[2]
    local tVal = args[3]
    local fVal = args[4]
    
    if text1 ~= text2
        then return tVal
        else return fVal
    end
end

function p.split(frame)
	local args = getArgs(frame, { removeBlanks=false, trim=false })
	assertTrue(args[1] and args[2], 'arguments #1 and #2 must be provided', 2)
	local split = string.split(args[1], args[2], yesno(args['p'] or args['plain'], false))
	local index = tonumber(args[3] or 1)
	
	assertTrue(index, 'index must be valid, got %q', 2, args[3])
	assertTrue(split[index], 'index #%d does not exist in split result', 2, index or 1)
	return split[index]
end

---------------------------------------------------------------------------------
-- function: match(frame: table|frame)
-- 
-- Invoked by {{Match}}.
---------------------------------------------------------------------------------
function p.match(frame)
	local args = getArgs(frame, { removeBlanks=false, trim=false })
	
	if not args[1] and args[2] then return string.error('"Match" requires atleast 2 arguments.') end
	
	local matches = { args[1]:match(args[2]) }
	return #matches == 1 and matches[1] or matches[args[3] or 1] or ''
end
--Finish Module
return p
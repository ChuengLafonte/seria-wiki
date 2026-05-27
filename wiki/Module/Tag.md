local p = {}

local getArgs = require('Module:Arguments').getArgs
local _error = require('Module:String')._error

function p.nowiki(frame)
    local args = getArgs(frame)
    
    local text = args[1]
    
    return mw.text.nowiki(text)
end

function p.insetCode(frame)
    local args = getArgs(frame, {removeBlanks = false})
    
    local text = args[1]
    local addCode = function(j)
        return '<span class="inset-code">'..j..'</span>'
    end
    
    return frame:preprocess(addCode('<nowiki>'..text..'</nowiki>'))
end

function p.syntaxhighlight(frame)
    local args = getArgs(frame)
    
    local text = args["t"] or args["text"] or args[1]
    local lang = args["lang"] or args["l"]
    local bypass = args["bypass"] or args["b"]
    
    if not text then return _error('Invalid argument to \"text": Inputs expected, got nothing') end
    
    local addCode = function(j)
        if lang then
            return '<syntaxhighlight lang="'..lang..'">'..j..'</syntaxhighlight>'
            else return j
        end
    end
    local addCodeBox = function(k)
        local codeBox = mw.html.create('div'):addClass('dark-code-box'):wikitext(k)
        return tostring(codeBox)
    end
    
    local ret = frame:preprocess(addCode(text))
    if not lang then ret = addCodeBox(ret) end
    
    return ret
end

return p
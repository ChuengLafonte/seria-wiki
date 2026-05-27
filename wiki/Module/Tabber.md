-- <pre>
local getArgs = require('Module:Arguments').getArgs
 
local p = {}

local function preprocess(text)
    local frame = mw.getCurrentFrame()
    
    return frame:preprocess(text)
end

function p.optionalTabber(frame)
    local args = getArgs(frame)
    
    local t = {}
    for i = 1,32,1 do
        if args["name"..i] and args["body"..i] then
            t[#t+1] = "|-|"..args["name"..i].."="..args["body"..i]
        end
    end
    
    return frame:preprocess('<tabber>\n'..table.concat(t, "\n")..'\n</tabber>')
end
 

function p._optionalTabber(t)
    local ret = {}
    for i, v in ipairs(t) do
        ret[#ret+1] = "|-|"..(
                t[i].name
                or t[i].n 
            ).."="..(
                t[i].body 
                or t[i].b 
                or t[i].text 
                or t[i].t
            )
    end
    ret = '<tabber>\n'..table.concat(ret, "\n")..'\n</tabber>'
    
    return mw.getCurrentFrame() and preprocess(ret) or ret
end

-- {{UI Tabber}}
function p.uiTabber(frame)
    local args = getArgs(frame)
    
    return p._uiTabber(args);
end
function p._uiTabber(tabs)
    local cont = mw.html.create("div"):addClass("sbw-ui-tabber")
    for key,val in pairs(tabs) do
        local tabcontent = cont:tag("div"):attr("id", "ui-"..key):addClass("sbw-ui-tab-content"):wikitext(val)
        if key ~= "default" then
            tabcontent:addClass("hidden"):css("display", "none")
        end
    end
    return tostring(cont)
end

--End Module 
return p
--'[[Category:General Wiki Modules]]'
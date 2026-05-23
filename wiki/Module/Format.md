--<pre>
--Required modules
local getArgs = require('Module:Arguments').getArgs
local yesno = require('Module:Yesno')

local p = {}

function p.format(frame)
    local prep = function(k) return frame:preprocess(k) end
    local args = getArgs(frame)
    
    local text = args[1]
    --booleans
    local bold = args["bold"] or args["b"]
    local italic = args["italic"] or args["i"]
    local underline = args["underline"] or args["u"]
    local strikethrough = args["strikethrough"] or args["strike"] or args["del"] or args["s"]
    local smallcaps = args["smallcapital"] or args["smallcaps"] or args["scaps"] or args["sc"]
    local code = args["code"] or args["cd"]
    local sup = args["sup"] or args["superscript"] or args["super"]
    local subS = args["sub"] or args["subscript"] or args["subs"]
    --text
    local abbr = args["abbr"] or args["abr"] or args["ab"]
    local hovertext = args["hovertext"] or args["hover"] or args["h"] or args["title"]
    --style
    local align = args["align"] or args["a"]
    local link = args["link"] or args["l"]
    local color = args["color"] or args["c"]
    local fontsize = args["size"] or args["fontsize"] or args["fs"]
    local font = args["font"] or args["fontfamily"] or args["ffam"]
    local bgcolor = args["bgcolor"] or args["bg"]
    local shadow = args["shadow"] or args["shdw"] or args["sh"]
    
    --error for incompatible tags
    if subS and sup then return prep('{{TError|Incompatible tags specified: "{{lt}}sup{{gt}}" and "{{lt}}sub{{gt}}" are incompatible.}}') end
    
    --abbr      overrides      underline, hovertext
    --code      overrides      smallcaps, font
    --link      overrides      underline
    
    -- wrap text with any tags that were requested
    local output_text = text
    output_text = p._makeColor(color, output_text)
    output_text = p._makeAbbr(abbr, output_text)
    output_text = p._makeSimpleTag("sub", subS, output_text)
    output_text = p._makeSimpleTag("sup", sup, output_text)
    output_text = p._makeSimpleTag("code", code, output_text)
    output_text = p._makeSimpleTag("del", strikethrough, output_text)
    output_text = p._makeUnderline(underline, link, abbr, color, output_text)
    output_text = p._makeSimpleTag("i", italic, output_text)
    output_text = p._makeSimpleTag("b", bold, output_text)
    output_text = p._makeMainSpan(bgcolor, fontsize, shadow, font, smallcaps, hovertext, abbr, code, output_text)
    output_text = p._makeLink(link, text, output_text)
    output_text = p._makeAlign(align, output_text)
    
    return output_text
end

-- various tag-adding function

function p._makeSimpleTag(tag, check, content)
    if not check then return content end
    return "<"..tag..">"..content.."</"..tag..">"
end

function p._makeAbbr(abbr, content)
    if not abbr then return content end
    return "<abbr title='" .. abbr .. "'>" .. content .. "</abbr>"
end

function p._makeColor(color, content)
    if not color then return content end
    return "<font style='color: " .. color .. "'>" .. content .. "</font>"
end

function p._makeUnderline(underline, link, abbr, color, content)
    if not underline then return content end
    
    if not link and not abbr then 
        if color then 
            return "<u style='color: " .. color .. "'>" .. content .. "</u>"
        else
            return "<u>" .. content .. "</u>"
        end
    else
        return content
    end
end

function p._makeLink(link, text, content)
    if not link then return content end
    
    if yesno(link, false) then
        return "[[" .. text .. "|" .. content .. "]]"
    elseif string.find(link, "http(s)://.*\.") then
        link = string.gsub(link, "]", "")
        link = string.gsub(link, "[", "")
        return '[' .. link .. " " .. content .. "]"
    else 
        return "[[" .. link .. "|" .. content .. "]]"
    end
end

function p._makeAlign(align, content)
    if not align then return content end
    
    local align_aliases = {
        ['l'] = 'left',
        ['c'] = 'center',
        ['r'] = 'right',
        ['float left'] = 'floatleft',
        ['fl'] = 'floatleft',
        ['float right'] = 'floatright',
        ['fr'] = 'floatright',
        ['j'] = 'justify'
    }
    align = align_aliases[align] or align
    if align == "floatleft" or align == "floatright" then
        return '<div class="' .. align .. '">' .. content .. '</div>'
    else
        return "<div style='text-align: " .. align .. "'>" .. content .. "</div>"
    end
end

function p._makeMainSpan(bgcolor, fontsize, shadow, font, smallcaps, hovertext, abbr, code, content)
    if not (bgcolor or fontsize or shadow or font or smallcaps or hovertext) then
        return content
    end
    
    local spanAttrs = {}
    
    --process params that use <span>
    
    --if hovertext is specified, apply it. if any other params are specified, add "style=", if not, then close </span>. If hovertext is not speified, check if other params are specified.
    if hovertext and not abbr then
        spanAttrs[#spanAttrs+1] = "title='"..hovertext.."'"
    end
    
    if bgcolor or fontsize or shadow or font or smallcaps then
        local cssRules = {}
        
        if font and not code then
            cssRules[#cssRules+1] = "font-family:" .. font
        end
        
        if bgcolor then
             cssRules[#cssRules+1] = "background:" .. bgcolor
        end
        
        if fontsize then
            --aliases for <small> and <big> tags, also for coming back to normal font size
            fontsize_aliases = {
                ['small'] = 12,
                ['big'] = 17,
                ['normal'] = 14
            }
            fontsize = fontsize_aliases[fontsize] or fontsize
            fontsize = string.gsub(fontsize, "px", "")
            cssRules[#cssRules+1] = "font-size:" .. fontsize .. "px"
        end
        
        if shadow then
            cssRules[#cssRules+1] = "text-shadow:" .. shadow
        end
        
        if smallcaps and not code then
            cssRules[#cssRules+1] = "font-variant:small-caps" 
        end
        
        spanAttrs[#spanAttrs+1] = "style='"..table.concat(cssRules, ";").."'"
    end
    
    return "<span " .. table.concat(spanAttrs, " ") .. ">" .. content .. "</span>"
end
 
return p


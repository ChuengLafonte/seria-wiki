local p = {}

local getArgs = require('Module:Arguments').getArgs
local mergeArgsSyntax = require('Module:Arguments').mergeArgsSyntax
local string = require('Module:String')
local aliases = require('Module:Page Actions/Aliases')
local action_data = require('Module:Page Actions/Data')

local title = mw.title.getCurrentTitle()
local pagename = title.prefixedText:gsub(' ', '_')
local namespace = title.nsText
local url = mw.uri.fullUrl

local format_aliases = {
        
            ['l']='list';
            ['list']='list';
            ['bl']='list';
            ['bull l']='list';
            ['bullet l']='list';
            ['b list']='list';
            ['bullet list']='list';
            
            ['inline']='inline';
            ['single l']='inline';
            ['inl']='inline';
            ['in']='inline';
            ['il']='inline';
            ['single line']='inline';
            ['s line']='inline';
            ['sing l']='inline';
            ['sing line']='inline';
            ['i']='inline';
            
            ['p']='parentheses';
            ['parentheses']='parentheses';
            ['parenth']='parentheses';
            ['paren']='parentheses';
            ['par']='parentheses';
            
        }
        
function p.main(frame)
    local args = getArgs(frame) 
    
    local format = args["format"] or args["f"] or args["for"] or args["type"] or args["t"] or args["tp"]
    if format then format = format:lower() end
    
    local attrs = {
            style = args["style"] or args["s"],
            class = args["class"] or args["cl"] or args["c"],
            id = args["id"] or args["i"],
        }
        
    if not args[1] then return string._error('Bad argument to "Page Actions" Input expected, got none') end
    
    if args[1]:match('%,')
        then text = mw.text.split(args[1], '%s*,%s*')
        else text = mergeArgsSyntax(args)
    end
    
    return p._main(text, format, attrs)
end

function p._main(input , format, attrs)
    if not input 
        then error('bad argument #1 to \'pageActions\' (string expected, got nil)', 3) 
    end
    
    local ret = {}
    
    local format = format_aliases[format] or 'inline'
    if format == 'list'
            then sep = ''
        elseif format == 'inline'
            then sep = ' • '
        elseif format == 'parentheses'
            then sep = ' | '
    end
    
    for i = 1,#text,1 do
        if text[i] == (nil or "") then table.remove(text, i) end
    end
    
    for i = 1,#text,1 do
        if text[i]:match('(.*)%s*%((.*)%)')
            then text[i], urlActions = text[i]:match('(.*)%s*%((.*)%)')
            text[i] = aliases[text[i]:lower()] 
            data = action_data[text[i]]
            urlActions = (data.action and '&' or '?')..urlActions:gsub('%s*-%s*', '='):gsub('%s*;%s*', '&')
            else urlActions = ''
        end
        
        if not aliases[text[i]:lower()]
            then error('Invalid list entry #'..i..' for Page Actions: invalid input "'..text[i]..'"')
        end
        
        text[i] = aliases[text[i]:lower()] 
        data = action_data[text[i]]
        
        if data.urlExtras and urlActions == '' then
            urlExtras = data.urlExtras
            for i = 1, #urlExtras, 1 do
                urlExtras[i][2] = mw.uri.encode(urlExtras[i][2])
                urlExtras[i] = table.concat(urlExtras[i], '=')
            end
            urlExtras = '&'..table.concat(urlExtras, '&')
            
            else urlExtras = ''
        end
        
        local specialPageAction = data.specialPageAction
        if data.action
            then pageAction = '?'..data.action[1]..'='..data.action[2]..urlActions
            else pageAction = ''..urlActions
        end
        
        if specialPageAction
            then if data.page
                then pagePrefix = 'Special:'..specialPageAction..'/'..data.page
                else pagePrefix = 'Special:'..specialPageAction
            end
            else pagePrefix = pagename
        end
        
        ret[#ret+1] = '[https://hypixel-skyblock.fandom.com/wiki/'..pagePrefix..pageAction..urlExtras..' '..string.wrapHtml(data.display_text, 'span', {title=data.title})..']'
    end
    if format == 'list'
        then for i = 1,#ret,1 do
            ret[i] = string.wrapHtml(ret[i], 'li')
        end
    else 
    	ret = table.concat(ret, ' • ')
    end
    
    if format == 'parentheses'
            then ret = '('..ret..')'
        elseif format == 'list' then
        	ret.sep = sep
            ret = string.wrapHtml(ret, 'ul')
    end
    
    return string.wrapHtml(string.wrapHtml('Page Actions: ', 'b')..ret, 'span', attrs)
end

return p
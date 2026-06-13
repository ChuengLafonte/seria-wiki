local p = {}

local rarityColors = {
    ['common'] = '#FFFFFF',
    ['uncommon'] = '#55FF55',
    ['rare'] = '#5555FF',
    ['epic'] = '#AA00AA',
    ['legendary'] = '#FFAA00',
    ['mythic'] = '#FF55FF',
    ['divine'] = '#55FFFF',
    ['special'] = '#FF5555',
    ['very special'] = '#FF5555',
    ['admin'] = '#FF5555'
}

local function trim(s)
    return (s:gsub("^%s*(.-)%s*$", "%1"))
end

local function addStat(name, icon, value, color)
    if not value or trim(value) == '' then return '' end
    local c = color or '#FF5555' -- Default stat color (like Damage/Strength)
    return string.format('<div style="color: #AAAAAA;">%s %s: <span style="color: %s;">%s</span></div>', name, icon, c, value)
end

local function addProp(name, value)
    if not value or trim(value) == '' then return '' end
    return string.format('<div style="color: #AAAAAA;">%s: <span style="color: #FFFFFF;">%s</span></div>', name, value)
end

function p.render(frame)
    local args = frame:getParent().args
    if not args.title and frame.args.title then args = frame.args end
    
    local title = args.title or mw.title.getCurrentTitle().text
    local rarity = (args.rarity or 'common'):lower()
    local titleColor = rarityColors[rarity] or '#FFFFFF'
    
    -- Auto hook sell price
    if not args.sell and args.id then
        local itemMdl = require('Module:Item')
        local sellP = itemMdl._sellPrice(args.id)
        if sellP and tostring(sellP) ~= '' then
            -- We need to mock args since it's read-only in some cases
            -- So we'll use a local variable instead
        end
    end
    
    local sellPriceStr = args.sell
    if not sellPriceStr and args.id then
        local itemMdl = require('Module:Item')
        local sellP = itemMdl._sellPrice(args.id)
        if sellP and tostring(sellP) ~= '' then
            sellPriceStr = sellP .. ' ⏺ [[Gins]]'
        end
    elseif sellPriceStr and not sellPriceStr:match('Gins') and not sellPriceStr:match('⏺') then
        sellPriceStr = sellPriceStr .. ' ⏺ [[Gins]]'
    end
    
    local html = {}
    
    -- Main Container
    table.insert(html, '<div class="skyblock-tooltip" style="float: right; clear: right; width: 320px; background-color: #110111; border: 2px solid #280528; border-radius: 4px; padding: 10px; margin: 0 0 1em 1em; font-family: Minecraft, sans-serif; font-size: 14px; line-height: 1.4; color: #AAAAAA;">')
    
    -- Title
    table.insert(html, string.format('<div style="text-align: center; font-size: 1.2em; font-weight: bold; color: %s; margin-bottom: 8px;">%s</div>', titleColor, title))
    
    -- Image
    local image = args.image or string.format('[[File:%s.png|200px]]', title)
    table.insert(html, string.format('<div style="text-align: center; margin-bottom: 10px;">%s</div>', image))
    
    -- Slot
    local slot = args.slot or title
    table.insert(html, string.format('<div style="margin: 5px auto 10px auto; width: 32px; height: 32px; background-color: #8b8b8b; border: 2px solid; border-color: #373737 #fff #fff #373737; display: flex; justify-content: center; align-items: center; box-sizing: content-box;">[[File:%s.png|32px]]</div>', slot))
    
    -- Gallery
    if args.gallery and trim(args.gallery) ~= '' then
        table.insert(html, string.format('<div style="text-align: center; margin-top: 5px; padding-top: 5px; border-top: 1px solid #280528; margin-bottom: 10px;">%s</div>', args.gallery))
    end
    
    -- Separator
    table.insert(html, '<div style="width: 100%; height: 2px; background-color: #280528; margin: 5px 0;"></div>')
    
    -- Basic Info
    table.insert(html, addProp('Also known as', args.aka))
    table.insert(html, addProp('Type', args.type or 'Item'))
    table.insert(html, string.format('<div style="color: #AAAAAA;">Rarity: <span style="color: %s; font-weight: bold; text-transform: uppercase;">%s</span></div>', titleColor, rarity))
    
    -- Stats
    local hasStats = false
    local statsHtml = {}
    local function processStat(name, icon, key, color)
        local s = addStat(name, icon, args[key], color)
        if s ~= '' then hasStats = true; table.insert(statsHtml, s) end
    end
    
    processStat('Damage', '❁', 'damage', '#FF5555')
    processStat('Strength', '❁', 'strength', '#FF5555')
    processStat('Crit Chance', '☣', 'crit_chance', '#5555FF')
    processStat('Crit Damage', '☠', 'crit_damage', '#5555FF')
    processStat('Bonus Attack Speed', '⚔', 'bonus_attack_speed', '#FFFF55')
    processStat('Sea Creature Chance', 'α', 'sea_creature_chance', '#55FFFF')
    processStat('Ferocity', '⫽', 'ferocity', '#FF5555')
    processStat('Ability Damage', '๑', 'ability_damage', '#FF5555')
    
    processStat('Health', '❤', 'health', '#55FF55')
    processStat('Defense', '❈', 'defense', '#55FF55')
    processStat('True Defense', '❂', 'true_defense', '#FFFFFF')
    processStat('Speed', '✦', 'speed', '#FFFFFF')
    processStat('Intelligence', '✎', 'intelligence', '#55FFFF')
    processStat('Magic Find', '✯', 'magic_find', '#55FFFF')
    processStat('Pet Luck', '♣', 'pet_luck', '#FF55FF')
    
    processStat('Mining Speed', '⸕', 'mining_speed', '#FFAA00')
    processStat('Mining Fortune', '☘', 'mining_fortune', '#FFAA00')
    processStat('Farming Fortune', '☘', 'farming_fortune', '#FFAA00')
    processStat('Foraging Fortune', '☘', 'foraging_fortune', '#FFAA00')
    processStat('Pristine', '✧', 'pristine', '#AA00AA')
    
    if hasStats then
        table.insert(html, '<div style="margin-top: 8px;">')
        for _, s in ipairs(statsHtml) do table.insert(html, s) end
        table.insert(html, '</div>')
    end
    
    -- Requirements
    local reqHtml = {}
    if args.combat_level_requirement then table.insert(reqHtml, addProp('Combat Level', args.combat_level_requirement)) end
    if args.dungeon_level_requirement then table.insert(reqHtml, addProp('Dungeon Level', args.dungeon_level_requirement)) end
    if args.slayer_level_requirement then table.insert(reqHtml, addProp('Slayer Level', args.slayer_level_requirement)) end
    if args.hotm_requirement then table.insert(reqHtml, addProp('HotM Level', args.hotm_requirement)) end
    if args.other_level_requirement then table.insert(reqHtml, addProp('Skill Level', args.other_level_requirement)) end
    if args.collection then table.insert(reqHtml, addProp('Collection', args.collection)) end
    
    if #reqHtml > 0 then
        table.insert(html, '<div style="width: 100%; height: 2px; background-color: #280528; margin: 5px 0;"></div>')
        for _, s in ipairs(reqHtml) do table.insert(html, s) end
    end
    
    -- Ability
    if args.ability_name and trim(args.ability_name) ~= '' then
        table.insert(html, '<div style="width: 100%; height: 2px; background-color: #280528; margin: 5px 0;"></div>')
        table.insert(html, string.format('<div style="color: #FFAA00; font-weight: bold;">Ability: %s <span style="color: #FFFF55;">%s</span></div>', args.ability_name, args.ability_activation or ''))
        if args.ability_desc then table.insert(html, string.format('<div style="color: #AAAAAA; margin-bottom: 5px;">%s</div>', args.ability_desc)) end
        if args.mana_cost then table.insert(html, string.format('<div style="color: #555555;">Mana Cost: <span style="color: #55FFFF;">%s</span></div>', args.mana_cost)) end
        if args.cooldown then table.insert(html, string.format('<div style="color: #555555;">Cooldown: <span style="color: #55FF55;">%s</span></div>', args.cooldown)) end
    end
    
    -- Material Tiers
    if (args.prev_material and trim(args.prev_material) ~= '') or (args.next_material and trim(args.next_material) ~= '') then
        table.insert(html, '<div style="width: 100%; height: 2px; background-color: #280528; margin: 5px 0;"></div>')
        table.insert(html, '<div style="color: #555555; text-align: center; margin-bottom: 4px;">Material Tiers</div>')
        table.insert(html, '<div style="display: flex; justify-content: space-between; font-size: 0.9em;">')
        table.insert(html, string.format('<div>← %s</div>', args.prev_material or 'None'))
        table.insert(html, string.format('<div>%s →</div>', args.next_material or 'None'))
        table.insert(html, '</div>')
    end
    
    -- Shop
    local shopHtml = {}
    if sellPriceStr then table.insert(shopHtml, addProp('Sell', sellPriceStr)) end
    if args.sell_shard then table.insert(shopHtml, addProp('Sell Shard', args.sell_shard)) end
    if args.sell_serium then table.insert(shopHtml, addProp('Sell Serium', args.sell_serium)) end
    if args.buy then table.insert(shopHtml, addProp('Buy', args.buy)) end
    if args.buy_shard then table.insert(shopHtml, addProp('Buy Shard', args.buy_shard)) end
    if args.buy_serium then table.insert(shopHtml, addProp('Buy Serium', args.buy_serium)) end
    
    if #shopHtml > 0 then
        table.insert(html, '<div style="width: 100%; height: 2px; background-color: #280528; margin: 5px 0;"></div>')
        table.insert(html, '<div style="color: #555555; text-align: center; margin-bottom: 4px;">Shop</div>')
        for _, s in ipairs(shopHtml) do table.insert(html, s) end
    end
    
    -- Block Details
    local blockHtml = {}
    if args.skill_xp_given then table.insert(blockHtml, addProp('Skill XP Given', args.skill_xp_given)) end
    if args.breaking_power then table.insert(blockHtml, addProp('Breaking Power', args.breaking_power)) end
    if args.tool then table.insert(blockHtml, addProp('Preferred Tool', args.tool)) end
    if args.breaking_power_required then table.insert(blockHtml, addProp('Breaking Power Required', args.breaking_power_required)) end
    
    if #blockHtml > 0 then
        table.insert(html, '<div style="width: 100%; height: 2px; background-color: #280528; margin: 5px 0;"></div>')
        table.insert(html, '<div style="color: #555555; text-align: center; margin-bottom: 4px;">Block Details</div>')
        for _, s in ipairs(blockHtml) do table.insert(html, s) end
    end
    
    -- Properties
    local propsHtml = {}
    if args.salable then table.insert(propsHtml, addProp('Salable', args.salable)) end
    if args.tradeable then table.insert(propsHtml, addProp('Tradeable', args.tradeable)) end
    if args.auctionable then table.insert(propsHtml, addProp('Auctionable', args.auctionable)) end
    if args.museum then table.insert(propsHtml, addProp('Museum', args.museum)) end
    
    if #propsHtml > 0 then
        table.insert(html, '<div style="width: 100%; height: 2px; background-color: #280528; margin: 5px 0;"></div>')
        table.insert(html, '<div style="color: #555555; text-align: center; margin-bottom: 4px;">Properties</div>')
        for _, s in ipairs(propsHtml) do table.insert(html, s) end
    end
    
    -- Other Details
    local detailsHtml = {}
    if args.id then table.insert(detailsHtml, addProp('Item ID', args.id)) end
    if args.source then table.insert(detailsHtml, addProp('Source', args.source)) end
    if args.upgrades_from then table.insert(detailsHtml, addProp('Upgrades From', args.upgrades_from)) end
    if args.upgrades_to then table.insert(detailsHtml, addProp('Upgrades To', args.upgrades_to)) end
    if args.raw_materials then table.insert(detailsHtml, addProp('Raw Materials', args.raw_materials)) end
    if args.material_cost then table.insert(detailsHtml, addProp('Material Cost', args.material_cost)) end
    
    if #detailsHtml > 0 then
        table.insert(html, '<div style="width: 100%; height: 2px; background-color: #280528; margin: 5px 0;"></div>')
        table.insert(html, '<div style="color: #555555; text-align: center; margin-bottom: 4px;">Details</div>')
        for _, s in ipairs(detailsHtml) do table.insert(html, s) end
    end
    
    table.insert(html, '</div>')
    return table.concat(html, '\n')
end

return p

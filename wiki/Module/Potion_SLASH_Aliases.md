-- All of the aliases names without "pot" or "potion"; those will be programatically added at the end
local aliasBases = {
    ['speed'] = 'Speed',
    ['spd'] = 'Speed',

    ['jb'] = 'Jump Boost',
    ['jmp bst'] = 'Jump Boost',
    ['jump'] = 'Jump Boost',
    ['jump boost'] = 'Jump Boost',
    
    ['exp'] = 'Experience',
    ['experience'] = 'Experience',
    
    ['adr'] = 'Adrenaline',
    ['adrenaline'] = 'Adrenaline',
    
    ['wnded'] = 'Wounded',
    ['wounded'] = 'Wounded',
    ['wnd'] = 'Wounded',
    
    ['nv'] = 'Night Vision',
    ['ngt vision'] = 'Night Vision',
    ['ngt v'] = 'Night Vision',
    ['night v'] = 'Night Vision',
    ['night vision'] = 'Night Vision',
    ['n vision'] = 'Night Vision',
    
    ['invisibility'] = 'Invisibility',
    ['invisible'] = 'Invisibility',
    ['invis'] = 'Invisibility',
    ['inv'] = 'Invisibility',
    
    ['pois'] = 'Poison',
    ['poison'] = 'Poison',
    
    ['heal'] = 'Healing',
    ['healing'] = 'Healing',
    
    ['fire resistance'] = 'Fire Resistance',
    ['fire res'] = 'Fire Resistance',
    ['flame resistance'] = 'Fire Resistance',
    ['flame res'] = 'Fire Resistance',
    
    ['water'] = 'Water Breathing',
    ['water breathing'] = 'Water Breathing',
    ['underwater breath'] = 'Water Breathing',
    ['underwater breathing'] = 'Water Breathing',
    ['water breath'] = 'Water Breathing',
    ['wtr brthing'] = 'Water Breathing',
    
    ['reg'] = 'Regeneration',
    ['regen'] = 'Regeneration',
    ['regeneration'] = 'Regeneration',
    
    ['str'] = 'Strength',
    ['strength'] = 'Strength',
    ['strong'] = 'Strength',
    
    ['weak'] = 'Weakness',
    ['wk'] = 'Weakness',
    ['weakness'] = 'Weakness',
    
    ['blind'] = 'Blindness',
    ['blindness'] = 'Blindness',
    
    ['slow'] = 'Slowness',
    ['slowness'] = 'Slowness',
    
    ['dmg'] = 'Damage',
    ['damage'] = 'Damage',
    ['instant damage'] = 'Damage',
    ['instant dmg'] = 'Damage',
    
    ['haste'] = 'Haste',
    ['fast mining'] = 'Haste',
    
    ['burn'] = 'Burning',
    ['burning'] = 'Burning',
    ['fire'] = 'Burning',
    ['fire aspect'] = 'Burning',




    ['kb'] = 'Knockback',
    ['knockb'] = 'Knockback',
    ['knockback'] = 'Knockback',
    ['kback'] = 'Knockback',

    ['stun'] = 'Stun',
    ['stunned'] = 'Stun',

    ['arch'] = 'Archery',
    ['archery'] = 'Archery',
    ['bow'] = 'Archery',
    ['achery'] = 'Archery',

    ['ab'] = 'Absorption',
    ['abs'] = 'Absorption',
    ['absorb'] = 'Absorption',
    ['absorption'] = 'Absorption',

    ['dodge'] = 'Dodge',
    ['miss'] = 'Dodge',

    ['res'] = 'Resistance',
    ['resist'] = 'Resistance',
    ['resistance'] = 'Resistance',
    ['def'] = 'Resistance',
    ['defence'] = 'Resistance',

    ['mana'] = 'Mana',
    ['int'] = 'Mana',
    ['intel'] = 'Mana',
    ['intelligence'] = 'Mana',
    ['mana regen'] = 'Mana',

    ['agil'] = 'Agility',
    ['agile'] = 'Agility',
    ['agility'] = 'Agility',

    ['rab'] = 'Rabbit',
    ['rabbit'] = 'Rabbit',
    ['rabbit feet'] = 'Rabbit',
    ['rab feet'] = 'Rabbit',

    ['crit'] = 'Critical',
    ['critical'] = 'Critical',
    ['crit dmg'] = 'Critical',
    ['crit chnc'] = 'Critical',
    ['crit damage'] = 'Critical',
    ['crit chance'] = 'Critical',
    ['critical damage'] = 'Critical',

    ['tru res'] = 'True Resistance',
    ['true res'] = 'True Resistance',
    ['true resis'] = 'True Resistance',
    ['true resistance'] = 'True Resistance',
    ['true def'] = 'True Resistance',
    ['true defense'] = 'True Resistance',
    
    ['spelunker'] = 'Spelunker',
    ['spelunk'] = 'Spelunker',
    ['splnkr'] = 'Spelunker',
    ['spe'] = 'Spelunker',

    ['spirit'] = 'Spirit',
    ['spir'] = 'Spirit',
    ['ghost'] = 'Spirit',

    ['mf'] = "Magic Find",
    ['mag'] = 'Magic Find',
    ['magic'] = 'Magic Find',
    ['magic find'] = 'Magic Find',
    ['mag fnd'] = 'Magic Find',
    ['mag find'] = 'Magic Find',
    ['magic fnd'] = 'Magic Find',

    ['stam'] = 'Stamina',
    ['stamina'] = 'Stamina',
    ['health and mana'] = 'Stamina',

    ['v'] = 'Venomous',
    ['veno'] = 'Venomous',
    ['venomous'] = 'Venomous',
    
    ['pet luck'] = 'Pet Luck',
    ['pet lck'] = 'Pet Luck',
    ['pt lck'] = 'Pet Luck',
    ['pl'] = 'Pet Luck',

    ['farm'] = 'Farming XP Boost',
    ['farming'] = 'Farming XP Boost',
    ['farming xp boost'] = 'Farming XP Boost',
    ['farming xp'] = 'Farming XP Boost',
    ['farm xp b'] = 'Farming XP Boost',
    ['farming xp b'] = 'Farming XP Boost',

    ['mine'] = 'Mining XP Boost',
    ['mining'] = 'Mining XP Boost',
    ['mining xp'] = 'Mining XP Boost',
    ['mining xp boost'] = 'Mining XP Boost',
    ['mine xp b'] = 'Mining XP Boost',
    ['mining xp b'] = 'Mining XP Boost',

    ['combat'] = 'Combat XP Boost',
    ['fight'] = 'Combat XP Boost',
    ['combat xp boost'] = 'Combat XP Boost',
    ['fighting'] = 'Combat XP Boost',
    ['combat xp'] = 'Combat XP Boost',
    ['combat xp b'] = 'Combat XP Boost',

    ['lumberjack'] = 'Foraging XP Boost',
    ['foraging'] = 'Foraging XP Boost',
    ['foraging xp boost'] = 'Foraging XP Boost',
    ['foraging xp b'] = 'Foraging XP Boost',
    ['foraging xp'] = 'Foraging XP Boost',
    ['foraging boost'] = 'Foraging XP Boost',

    ['fish'] = 'Fishing XP Boost',
    ['fishing'] = 'Fishing XP Boost',
    ['fishing xp boost'] = 'Fishing XP Boost',
    ['fishing xp b'] = 'Fishing XP Boost',
    ['fishing xp'] = 'Fishing XP Boost',
    ['fishing boost'] = 'Fishing XP Boost',

    ['enchant'] = 'Enchanting XP Boost',
    ['enchanting'] = 'Enchanting XP Boost',
    ['enchanting xp boost'] = 'Enchanting XP Boost',
    ['enchanting xp b'] = 'Enchanting XP Boost',
    ['enchanting xp'] = 'Enchanting XP Boost',
    ['enchanting table'] = 'Enchanting XP Boost',
    ['enchant xp b'] = 'Enchanting XP Boost',

    ['alchemy'] = 'Alchemy XP Boost',
    ['alchemy xp boost'] = 'Alchemy XP Boost',
    ['alchemy xp b'] = 'Alchemy XP Boost',
    ['alchemy xp'] = 'Alchemy XP Boost',
    ['alch'] = 'Alchemy XP Boost',
    ['alch xp b'] = 'Alchemy XP Boost',
    ['brewing'] = 'Alchemy XP Boost',
    ['brewing xp boost'] = 'Alchemy XP Boost',
    ['bewing xp'] = 'Alchemy XP Boost',
    ['brewing xp b'] = 'Alchemy XP Boost',
    ['potion xp b'] = 'Alchemy XP Boost',
    
    ['dungeon'] = 'Dungeon',
    ['dungeons'] = 'Dungeon',
    ['dung'] = 'Dungeon',
    
    ['king\'s scent'] = 'King\'s Scent',
    ['kings scent'] = 'King\'s Scent',
    
    ['obsidian skin'] = 'Obsidian Skin',

    ['smoldering polarization'] = 'Smoldering Polarization',

    ['coldfusion'] = 'Coldfusion',

    ['wisp\'s ice flavored water'] = 'Wisp\'s Ice-Flavored Water',
    ['wisps ice flavored water'] = 'Wisp\'s Ice-Flavored Water',

    ['mushed glowy tonic'] = 'Mushed Glowy Tonic',
    ['mgt'] = 'Mushed Glowy Tonic',
    ['mushed'] = 'Mushed Glowy Tonic',
    
    ['harvest harbinger'] = 'Harvest Harbinger',
    
    ['poisoned candy'] = 'Poisoned Candy',
    
    ['pest repellent'] = 'Pest Repellant',
    
    ['cold resistance'] = 'Cold Resistance',
    ['cold res'] = 'Cold Resistance',
    
    ['douce pluie de stinky cheese'] = 'Douce Pluie de Stinky Cheese',
}

-- Programatically add duplicated of all aliases with "pot" andn "potion" at the end, to avoid manually adding them in the table above
local aliases = {}
for key,val in pairs(aliasBases) do
    aliases[key] = val
    aliases[key.." pot"] = val
    aliases[key.." potion"] = val
end

return aliases
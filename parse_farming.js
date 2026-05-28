const fs = require('fs');

// Simple parser for the specific YAML structure since we don't have npm installed
const yamlContent = fs.readFileSync('e:/dev/seria-cave/plugins/SeriaCollection/collections/farming.yml', 'utf8');

const lines = yamlContent.split('\n');
let currentCollection = null;
let currentTier = null;
let collections = {};

let parsingRewards = false;

for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) continue;

    // Detect collection start (indent 4, ends with ':')
    if (line.startsWith('    ') && !line.startsWith('      ') && trimmed.endsWith(':') && trimmed !== 'collections:') {
        currentCollection = trimmed.slice(0, -1);
        collections[currentCollection] = { name: '', minion: '', tiers: {} };
        continue;
    }

    if (!currentCollection) continue;

    if (trimmed.startsWith('name:') && line.startsWith('      name:')) {
        collections[currentCollection].name = trimmed.slice(5).replace(/["']/g, '').replace(/<[^>]+>/g, '').trim();
    }

    // Detect tier start
    if (line.startsWith('        ') && !line.startsWith('          ') && /^\d+:$/.test(trimmed)) {
        currentTier = parseInt(trimmed.slice(0, -1));
        collections[currentCollection].tiers[currentTier] = { requirement: 0, rewards: [] };
        parsingRewards = false;
        continue;
    }

    if (!currentTier) continue;

    if (trimmed.startsWith('requirement:')) {
        collections[currentCollection].tiers[currentTier].requirement = parseInt(trimmed.slice(12).trim());
    }

    if (trimmed === 'display-rewards:') {
        parsingRewards = true;
        continue;
    } else if (trimmed.endsWith(':') && trimmed !== 'display-rewards:') {
        parsingRewards = false;
    }

    if (parsingRewards && trimmed.startsWith('-')) {
        let rewardStr = trimmed.slice(1).replace(/["']/g, '').trim();
        collections[currentCollection].tiers[currentTier].rewards.push(rewardStr);
    }
}

function processReward(rewardStr) {
    let clean = rewardStr.replace(/<[^>]+>/g, '').replace('☘', '').replace('🌾', '').trim();
    
    if (clean.includes('Recipe')) {
        let name = clean.replace(/\s*Recipes?$/i, '').trim();
        return `{ '${name}', type = 'Recipe' }`;
    }
    
    if (clean.includes('Trade')) {
        let name = clean.replace(/\s*Trade$/i, '').trim();
        return `{ '${name}', type = 'Trade' }`;
    }
    
    if (clean.includes('EXP')) {
        let match = clean.match(/\+?([\d\.]+)\s+(.*?)\s+EXP/i);
        if (match) {
            let amt = match[1].replace(/\./g, '');
            let ctype = match[2].trim();
            return `{ ${amt}, type = '${ctype} Experience' }`;
        }
    }
    
    if (clean.includes('Fortune')) {
        let match = clean.match(/\+?(\d+)\s+(.*?)\s+Fortune/i);
        if (match) {
            let amt = match[1];
            let ftype = match[2].trim();
            return `{\n\t\t\t\t\t'{{Gold|+${amt}}} {{G|${ftype} Fortune}}',\n\t\t\t\t\ttype = 'Custom',\n\t\t\t\t\tnolink = true,\n\t\t\t\t\trewardstr = '&6+${amt}~~ ${ftype} Fortune',\n\t\t\t\t}`;
        }
    }
    
    if (clean.includes('Bundle')) {
        let name = clean.replace(/\s*\[.*?\]/g, '').trim();
        return `{ '${name}', type = 'Reward' }`;
    }
    
    if (clean.includes('Akses ke')) {
        return `{\n\t\t\t\t\t'${clean}',\n\t\t\t\t\ttype = 'Custom',\n\t\t\t\t\tnolink = true,\n\t\t\t\t\trewardstr = '&7Akses ke &aChuville &7Farming Area',\n\t\t\t\t}`;
    }
    
    return `{ '${clean}', type = 'Custom', nolink = true, rewardstr = '&7${clean}' }`;
}

let outLines = [];
for (let cid in collections) {
    let cdata = collections[cid];
    let name = cdata.name;
    outLines.push(`\t['${name}'] = {`);
    
    // minion
    let minion = name;
    if (name.endsWith(' Seeds')) {
        minion = name; // Just match what the game has or use standard convention
    }
    outLines.push(`\t\tminion = '${minion}',`);
    
    let tiers = Object.keys(cdata.tiers).sort((a, b) => parseInt(a) - parseInt(b));
    for (let tier of tiers) {
        let tdata = cdata.tiers[tier];
        outLines.push(`\t\t[${tier}] = {`);
        outLines.push(`\t\t\trequired = ${tdata.requirement},`);
        outLines.push(`\t\t\treward = {`);
        
        for (let rStr of tdata.rewards) {
            outLines.push(`\t\t\t\t${processReward(rStr)},`);
        }
        
        outLines.push(`\t\t\t},`);
        outLines.push(`\t\t},`);
    }
    outLines.push(`\t},`);
}

fs.writeFileSync('e:/Project Wiki/farming_parsed.txt', outLines.join('\n'));
console.log('Done!');

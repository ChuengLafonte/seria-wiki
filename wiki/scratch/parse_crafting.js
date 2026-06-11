const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');

const dataDir = path.resolve('../../crafting data');
const outFile = path.resolve('../Module/Crafting_SLASH_Data.md');

function toTitleCase(s) {
    if (!s) return "";
    return s.split('_').map(w => w.charAt(0).toUpperCase() + w.slice(1).toLowerCase()).join(' ');
}

function parseSlotItem(itemStr) {
    itemStr = itemStr.trim();
    if (itemStr.startsWith('v AIR') || !itemStr) return null;

    let parts = itemStr.split(' ');
    let amount = "1";
    let name = "Unknown";

    if (itemStr.startsWith('v ')) {
        let material = parts[1];
        name = toTitleCase(material);
        for (let p of parts) {
            if (p.includes('..')) amount = p.split('.')[0];
        }
    } else if (itemStr.startsWith('m ')) {
        let idPart;
        let idx = parts.indexOf('-');
        if (idx !== -1) {
            idPart = parts[idx - 1];
        } else {
            idPart = parts[2];
        }
        name = toTitleCase(idPart);
        for (let p of parts) {
            if (p.includes('..')) amount = p.split('.')[0];
        }
    }

    if (!isNaN(parseInt(amount)) && parseInt(amount) > 1) {
        return name + "," + amount;
    }
    return name;
}

let luaTable = {};

let files = fs.readdirSync(dataDir).filter(f => f.endsWith('.yml'));

for (let file of files) {
    let filePath = path.join(dataDir, file);
    try {
        let content = fs.readFileSync(filePath, 'utf8');
        let data = yaml.load(content);
        if (!data) continue;

        for (let rootKey in data) {
            let items = data[rootKey];
            if (typeof items !== 'object') continue;

            for (let itemKey in items) {
                let itemData = items[itemKey];
                if (typeof itemData !== 'object') continue;

                let craftAmount = itemData['craft-amount'] || 1;
                let outputName = toTitleCase(itemKey);
                let outputVal = String(craftAmount) !== '1' ? outputName + "," + craftAmount : outputName;

                let crafting = itemData['crafting'] || {};
                let shaped = crafting['shaped'] || {};

                let frames = [];
                let shapeKeys = Object.keys(shaped).sort((a, b) => {
                    let anum = parseInt(a);
                    let bnum = parseInt(b);
                    if (!isNaN(anum) && !isNaN(bnum)) return anum - bnum;
                    return a.localeCompare(b);
                });

                for (let shapeKey of shapeKeys) {
                    let shapeData = shaped[shapeKey];
                    let inputs = shapeData['input'] || [];

                    let rows = [...inputs];
                    while (rows.length < 3) {
                        rows.push('v AIR 0 1..|v AIR 0 1..|v AIR 0 1..');
                    }

                    let frameQrs = [];
                    let rowLetters = ['A', 'B', 'C'];
                    
                    for (let rIdx = 0; rIdx < 3; rIdx++) {
                        let cols = rows[rIdx].split('|');
                        while (cols.length < 3) {
                            cols.push('v AIR 0 1..');
                        }
                        for (let cIdx = 0; cIdx < 3; cIdx++) {
                            let slotId = rowLetters[rIdx] + (cIdx + 1);
                            let itemName = parseSlotItem(cols[cIdx]);
                            if (itemName) {
                                frameQrs.push(slotId + ' "' + itemName + '"');
                            }
                        }
                    }

                    if (frameQrs.length > 0) {
                        frames.push(frameQrs.join(' '));
                    }
                }

                if (frames.length > 0) {
                    let qrsString = frames.join(' // ');
                    
                    let keyName = outputName;
                    let count = 2;
                    while (luaTable[keyName]) {
                        keyName = outputName + ' ' + count;
                        count++;
                    }

                    if (outputVal === outputName) {
                        luaTable[keyName] = [qrsString];
                    } else {
                        luaTable[keyName] = [qrsString, { Output: outputVal }];
                    }
                }
            }
        }
    } catch (e) {
        console.error("Error processing " + file, e);
    }
}

let luaLines = ["return {"];
for (let k in luaTable) {
    let v = luaTable[k];
    let escapedK = k.replace(/'/g, "\\'");
    if (v.length === 1) {
        luaLines.push("    ['" + escapedK + "'] = '" + v[0] + "',");
    } else {
        let outVal = String(v[1].Output).replace(/'/g, "\\'");
        luaLines.push("    ['" + escapedK + "'] = { '" + v[0] + "', Output = '" + outVal + "' },");
    }
}
luaLines.push("}");

fs.writeFileSync(outFile, luaLines.join('\n'), 'utf8');
console.log("Parsed " + Object.keys(luaTable).length + " items successfully.");

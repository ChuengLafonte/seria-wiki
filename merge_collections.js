const fs = require('fs');

const wikiData = fs.readFileSync('e:/Project Wiki/wiki/Module/Collection_SLASH_Data.md', 'utf8');
const parsedFarming = fs.readFileSync('e:/Project Wiki/farming_parsed.txt', 'utf8');

// The items we are replacing
const items = ['Wheat Seeds', 'Wheat', 'Potato', 'Carrot', 'Beetroot'];

let modifiedData = wikiData;

// Regex to remove existing collections
for (let item of items) {
    // We look for a line starting with exactly one tab, then ['ItemName'] = {
    // and match everything up to the next line starting with exactly one tab and },
    const regex = new RegExp(`^\\t\\['${item}'\\] = \\{[\\s\\S]*?^\\t\\},?\\r?\\n?`, 'gm');
    
    // Check if it exists
    if (regex.test(modifiedData)) {
        console.log(`Found and removing existing ${item}`);
        modifiedData = modifiedData.replace(regex, '');
    } else {
        console.log(`${item} not found in existing data.`);
    }
}

// Now insert the parsed farming data just before the final return statement or closing brace.
// The file ends with:
// }
//
// return { all_collections = all_collections }
// Or just:
// }
const insertRegex = /^}/gm;
// Find the last occurrence of ^} which closes the all_collections table.
let match;
let lastIndex = -1;
while ((match = insertRegex.exec(modifiedData)) !== null) {
    lastIndex = match.index;
}

if (lastIndex !== -1) {
    modifiedData = modifiedData.slice(0, lastIndex) + parsedFarming + '\n' + modifiedData.slice(lastIndex);
    fs.writeFileSync('e:/Project Wiki/wiki/Module/Collection_SLASH_Data.md', modifiedData);
    console.log('Successfully updated Collection/Data');
} else {
    console.error('Could not find closing brace for all_collections');
}

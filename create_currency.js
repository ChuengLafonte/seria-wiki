const fs = require('fs');
const path = require('path');

const templates = {
    'Gins.md': `<span style="color: #FFAA00; font-weight: bold;">{{{1}}} ⛃ Gins</span><noinclude>[[Category:Templates]]</noinclude>`,
    'Shard.md': `<span style="color: #55FFFF; font-weight: bold;">{{{1}}} ✧ Shards</span><noinclude>[[Category:Templates]]</noinclude>`,
    'Serium.md': `<span style="color: #FF55FF; font-weight: bold;">{{{1}}} ❂ Serium</span><noinclude>[[Category:Templates]]</noinclude>`
};

for (const [filename, content] of Object.entries(templates)) {
    fs.writeFileSync(path.join('e:/Project Wiki/wiki/Template/Lainnya', filename), content);
}
console.log("Currency templates created.");

const https = require('https');
const fs = require('fs');
const path = require('path');

const titles = [
  'Template:Infobox/Location',
  'Template:Infobox location',
  'Template:Nav/Locations',
  'Template:Zone',
  'Template:ZoneText',
  'Template:Zone List',
  'Module:Location/Aliases',
  'Module:Location/Sprites',
  'Module:Zone',
  'Module:Zone/Aliases',
  'Module:Zone/Data'
];

const outDir = path.join(__dirname, 'fandom_data');
if (!fs.existsSync(outDir)) fs.mkdirSync(outDir);

titles.forEach(title => {
  const url = `https://hypixel-skyblock.fandom.com/api.php?action=query&prop=revisions&rvprop=content&rvslots=main&format=json&titles=${encodeURIComponent(title)}`;
  
  https.get(url, (res) => {
    let data = '';
    res.on('data', chunk => data += chunk);
    res.on('end', () => {
      try {
        const json = JSON.parse(data);
        const pages = json.query.pages;
        const page = Object.values(pages)[0];
        if (page.revisions && page.revisions.length > 0) {
          const content = page.revisions[0].slots.main['*'];
          const filename = title.replace(/[:\/]/g, '_') + '.md';
          fs.writeFileSync(path.join(outDir, filename), content);
          console.log(`Saved ${filename}`);
        } else {
          console.log(`No content for ${title}`);
        }
      } catch (e) {
        console.error(`Error parsing ${title}:`, e);
      }
    });
  }).on('error', (e) => {
    console.error(`Error fetching ${title}:`, e);
  });
});

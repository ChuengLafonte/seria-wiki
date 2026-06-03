const https = require('https');

const title = 'Module:Infobox/Mechanic';
const url = `https://hypixel-skyblock.fandom.com/api.php?action=query&prop=revisions&rvprop=content&rvslots=main&format=json&titles=${encodeURIComponent(title)}`;

https.get(url, (res) => {
  let data = '';
  res.on('data', chunk => data += chunk);
  res.on('end', () => {
    const json = JSON.parse(data);
    if (json.query && json.query.pages) {
      const page = Object.values(json.query.pages)[0];
      if (page.revisions && page.revisions.length > 0) {
        console.log(page.revisions[0].slots.main['*'].substring(0, 1000));
      }
    }
  });
});

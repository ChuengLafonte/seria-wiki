const https = require('https');

const url = `https://hypixel-skyblock.fandom.com/api.php?action=query&prop=revisions&rvprop=content&rvslots=main&format=json&titles=Template:TextSection`;

https.get(url, (res) => {
  let data = '';
  res.on('data', chunk => data += chunk);
  res.on('end', () => {
    console.log(JSON.parse(data).query.pages[Object.keys(JSON.parse(data).query.pages)[0]].revisions[0].slots.main['*']);
  });
});

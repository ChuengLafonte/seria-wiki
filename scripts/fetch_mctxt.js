const https = require('https');
const url = `https://hypixel-skyblock.fandom.com/api.php?action=query&prop=revisions&rvprop=content&rvslots=main&format=json&titles=Module:Mctxt`;
https.get(url, (res) => {
  let data = '';
  res.on('data', chunk => data += chunk);
  res.on('end', () => {
    const page = Object.values(JSON.parse(data).query.pages)[0];
    if(page.revisions) {
      console.log(page.revisions[0].slots.main['*'].substring(0, 1000));
    }
  });
});

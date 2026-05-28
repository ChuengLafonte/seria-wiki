import urllib.request, json
url = 'https://seria.fandom.com/api.php?action=query&prop=revisions&titles=MediaWiki:Common.js/mcui.js&rvprop=content&rvslots=main&format=json'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
res = urllib.request.urlopen(req)
data = json.loads(res.read().decode('utf-8'))
content = list(data['query']['pages'].values())[0]['revisions'][0]['slots']['main']['*']
with open('mcui_test.js', 'w', encoding='utf-8') as f:
    f.write(content)

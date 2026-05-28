import urllib.request, json, re
url = 'https://seria.fandom.com/api.php?action=parse&page=Collections/UI&prop=text&format=json'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
res = urllib.request.urlopen(req)
data = json.loads(res.read().decode('utf-8'))
html = data['parse']['text']['*']

matches = re.findall(r'<div[^>]*class="[^"]*sbw-ui-tab-content[^"]*"[^>]*>', html)
for m in matches:
    print(m)

import urllib.request, json, re
url = 'https://seria.fandom.com/api.php?action=parse&page=Collections/UI&prop=text&format=json'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
res = urllib.request.urlopen(req)
data = json.loads(res.read().decode('utf-8'))
html = data['parse']['text']['*']

matches = re.findall(r'<span class="invslot[^\"]*goto-collection-farming.*?</span></span>', html)
if matches:
    print(matches[0][:500])
else:
    print('Not found')

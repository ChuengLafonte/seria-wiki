import urllib.request, json, re
url = 'https://seria.fandom.com/api.php?action=parse&page=Collections/UI&prop=text&format=json'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
res = urllib.request.urlopen(req)
data = json.loads(res.read().decode('utf-8'))
html = data['parse']['text']['*']
print('sbw-ui-tabber count:', html.count('sbw-ui-tabber'))
matches = re.findall(r'<div class="sbw-ui-tabber">.*?</div>', html, re.DOTALL)
if matches:
    print('Found sbw-ui-tabber block!')
else:
    print('Not found sbw-ui-tabber block covering the whole thing!')

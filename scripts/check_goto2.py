import urllib.request, json, re
url = 'https://seria.fandom.com/api.php?action=parse&page=Project_Seria_Wiki:Sandbox&prop=text&format=json'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
res = urllib.request.urlopen(req)
data = json.loads(res.read().decode('utf-8'))
html = data['parse']['text']['*']
matches = re.findall(r'<div[^>]*class="[^"]*invslot[^"]*goto-[^"]*"[^>]*>.*?</div>', html, re.DOTALL)
for match in matches:
    print(match[:200])

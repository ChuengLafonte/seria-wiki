import urllib.request, json, re
url = 'https://seria.fandom.com/api.php?action=parse&page=Project_Seria_Wiki:Sandbox&prop=text&format=json'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    res = urllib.request.urlopen(req)
    data = json.loads(res.read().decode('utf-8'))
    html = data['parse']['text']['*']
    match = re.search(r'<span class="invslot-item[^>]*>.*?</span>', html, re.DOTALL)
    if match:
        print(match.group(0))
except Exception as e:
    print('Error:', e)

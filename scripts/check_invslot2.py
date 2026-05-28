import urllib.request, json, re
url = 'https://seria.fandom.com/api.php?action=parse&page=Project_Seria_Wiki:Sandbox&prop=text&format=json'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
res = urllib.request.urlopen(req)
data = json.loads(res.read().decode('utf-8'))
html = data['parse']['text']['*']

if 'invslot-item' in html:
    print('invslot-item IS in the HTML.')
else:
    print('invslot-item NOT FOUND.')

if 'invslot' in html:
    print('invslot IS in the HTML.')
else:
    print('invslot NOT FOUND.')

if 'minetip' in html:
    print('minetip IS in the HTML.')
else:
    print('minetip NOT FOUND.')

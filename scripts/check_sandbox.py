import urllib.request, json, re
url = 'https://seria.fandom.com/api.php?action=parse&page=Project_Seria_Wiki:Sandbox&prop=text&format=json'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    res = urllib.request.urlopen(req)
    data = json.loads(res.read().decode('utf-8'))
    html = data['parse']['text']['*']
    # Look for Script error
    errors = re.findall(r'<strong class="error"><span class="scribunto-error[^>]*>(.*?)</span></strong>', html)
    if errors:
        for err in errors:
            print('Lua Error:', err)
    else:
        print('No Scribunto Lua errors found.')
    
    # Also print any raw wikicode that failed to parse
    if '{{' in html:
        print("Unparsed template found in HTML!")
except Exception as e:
    print('Error:', e)

import urllib.request, json, re, html as html_parser
url = 'https://seria.fandom.com/api.php?action=parse&page=Project_Seria_Wiki:Sandbox&prop=text&format=json'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    res = urllib.request.urlopen(req)
    data = json.loads(res.read().decode('utf-8'))
    html = data['parse']['text']['*']
    # Look for the lua traceback in HTML
    errors = re.findall(r'<div class="scribunto-error[^>]*>(.*?)</div>', html, re.DOTALL)
    for err in errors:
        print(html_parser.unescape(re.sub('<[^<]+>', '', err)).strip())
except Exception as e:
    print('Error:', e)

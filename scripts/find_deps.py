import urllib.request, json, re
url = 'https://seria.fandom.com/api.php?action=query&prop=revisions&titles=Module:Crafting/UI|Module:UI|Module:UI/Core&rvprop=content&rvslots=main&format=json'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    res = urllib.request.urlopen(req)
    data = json.loads(res.read().decode('utf-8'))
    pages = data['query']['pages']
    for page_id in pages:
        title = pages[page_id]['title']
        if 'missing' not in pages[page_id]:
            content = pages[page_id]['revisions'][0]['slots']['main']['*']
            requires = re.findall(r'require\s*\(\s*[\'\"]([^\'\"]+)[\'\"]\s*\)', content)
            print(f'{title} requires: {requires}')
except Exception as e:
    print('Error:', e)

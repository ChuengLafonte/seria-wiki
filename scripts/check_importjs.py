import urllib.request, json
url = 'https://seria.fandom.com/api.php?action=query&prop=revisions&titles=MediaWiki:ImportJS&rvlimit=5&rvprop=timestamp|user|comment|content&rvslots=main&format=json'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    res = urllib.request.urlopen(req)
    data = json.loads(res.read().decode('utf-8'))
    revisions = list(data['query']['pages'].values())[0]['revisions']
    for rev in revisions:
        print(f"[{rev['timestamp']}] {rev['user']}: {rev['comment']}")
        print(rev['slots']['main']['*'])
        print('---')
except Exception as e:
    print('Error:', e)

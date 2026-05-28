import urllib.request
url = 'https://seria.fandom.com/load.php?lang=en&modules=site.styles&only=styles&skin=fandomdesktop'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
try:
    res = urllib.request.urlopen(req)
    css = res.read().decode('utf-8')
    if '#minetip-tooltip' in css:
        print('CSS is PRESENT')
    else:
        print('CSS is MISSING')
        print('CSS Length:', len(css))
except Exception as e:
    print('Error fetching CSS:', e)

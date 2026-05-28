import urllib.request, json, os, mwclient

username = os.environ.get('FANDOM_USERNAME')
password = os.environ.get('FANDOM_PASSWORD')
site = mwclient.Site('seria.fandom.com', path='/')
site.login(username, password)

page = site.pages['MediaWiki:Common.js']
text = page.text()

if 'wiki-use.css' not in text:
    append_js = """
// Load Minecraft Font and other external CSS (since @import is blocked in Common.css)
var externalCSS = [
    'https://cdn.jsdelivr.net/gh/skyblock-wiki/wiki-assets@1.0/fonts/font-import/lib/wiki-use.css',
    'https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,700;1,700&display=swap',
    'https://fonts.googleapis.com/css2?family=Noto+Sans:ital,wght@0,400;0,600;0,700;1,400;1,600;1,700&display=swap'
];
for (var i = 0; i < externalCSS.length; i++) {
    mw.util.addCSS('@import url("' + externalCSS[i] + '");');
}
"""
    page.edit(text + append_js, summary='Dynamically load external fonts via JS')
    print('Added font loader to Common.js!')
else:
    print('Font loader already exists.')

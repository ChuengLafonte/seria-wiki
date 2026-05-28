import urllib.request, json, os, mwclient

username = os.environ.get('FANDOM_USERNAME')
password = os.environ.get('FANDOM_PASSWORD')
site = mwclient.Site('seria.fandom.com', path='/')
site.login(username, password)

page_js = site.pages['MediaWiki:Common.js']
text_js = page_js.text()
import_str = "\n\n// Fallback loading of minetip and mcui if ImportJS fails\nimportArticle({type: 'script', article: 'MediaWiki:Common.js/minetip-v4.js'});\nimportArticle({type: 'script', article: 'MediaWiki:Common.js/mcui-v4.js'});\n"

if import_str in text_js:
    text_js = text_js.replace(import_str, '')
    page_js.edit(text_js, summary='Remove broken importArticle that might be throwing JS errors')
    print('Removed broken JS load.')
else:
    print('Not found.')

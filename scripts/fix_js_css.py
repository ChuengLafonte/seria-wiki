import urllib.request, json, os, mwclient

username = os.environ.get('FANDOM_USERNAME')
password = os.environ.get('FANDOM_PASSWORD')
site = mwclient.Site('seria.fandom.com', path='/')
site.login(username, password)

# 1. Update Common.js to import scripts safely
page_js = site.pages['MediaWiki:Common.js']
text_js = page_js.text()
if 'importArticle({type:' not in text_js:
    append_js = "\n\n// Fallback loading of minetip and mcui if ImportJS fails\nimportArticle({type: 'script', article: 'MediaWiki:Common.js/minetip-v4.js'});\nimportArticle({type: 'script', article: 'MediaWiki:Common.js/mcui-v4.js'});\n"
    page_js.edit(text_js + append_js, summary='Add importArticles for UI scripts')
    print('Updated Common.js')

# 2. Update Common.css to add z-index to #minetip-tooltip
page_css = site.pages['MediaWiki:Common.css']
text_css = page_css.text()
if 'z-index: 9999999' not in text_css:
    text_css = text_css.replace(
        '#minetip-tooltip {\n    position: fixed;\n    top: 0;\n    left: 0;\n  }',
        '#minetip-tooltip {\n    position: fixed;\n    top: 0;\n    left: 0;\n    z-index: 9999999;\n  }'
    )
    page_css.edit(text_css, summary='Add z-index to minetip tooltip')
    print('Updated Common.css')

import urllib.request, json, os, mwclient

username = os.environ.get('FANDOM_USERNAME')
password = os.environ.get('FANDOM_PASSWORD')
site = mwclient.Site('seria.fandom.com', path='/')
site.login(username, password)

page = site.pages['Template:Submodules']
content = """<includeonly>
<div class="dablink" style="font-style: italic; padding-left: 1.6em;">
See all submodules for this page: '''[[Special:PrefixIndex/Module:{{{1|{{ROOTPAGENAME}}}}}/|Special:PrefixIndex/Module:{{{1|{{ROOTPAGENAME}}}}}/]]'''
</div>
</includeonly><noinclude>{{Documentation}}</noinclude>
"""

page.edit(content, summary='Rewrite Template:Submodules to use Special:PrefixIndex since DPL is not supported on Fandom anymore')
print('Updated Template:Submodules')

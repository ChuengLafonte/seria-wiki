import urllib.request, json, os, mwclient

username = os.environ.get('FANDOM_USERNAME')
password = os.environ.get('FANDOM_PASSWORD')
site = mwclient.Site('seria.fandom.com', path='/')
site.login(username, password)

sandbox_content = """
= Minecraft UI Test =
This page serves to test the functionality of MCText, Minetip, and MCUI.

== 1. MCText ==
Testing color codes and formatting:
* {{Mctxt|&cThis is red text}}
* {{Mctxt|&lThis is bold text}}
* {{Mctxt|&a&lGreen and Bold}}

== 2. Minetip (Hover Tooltips) ==
Testing tooltips:
* Hover over this: <span class="tooltip" title="&cMagic Damage: &a+100">[Mystic Sword]</span>
* Hover over an inventory slot item below.

== 3. MCUI (Crafting Table) ==
Testing a basic Crafting UI:
{{Crafting UI
|A1= |B1= Diamond |C1= 
|A2= |B2= Diamond |C2= 
|A3= |B3= Stick   |C3= 
|Output= Diamond Sword
}}
"""

page = site.pages['Project Seria Wiki:Sandbox']
page.edit(sandbox_content, summary='Create Sandbox page to test MCUI, MCText, and Tooltips')
print('Created Project Seria Wiki:Sandbox')

{{Documentation subpage}}

== Overview ==
{{Lua|Collection/UI}}
{{T|Collection UI}} is a template used to create a collection rewards UI.
{{Tc}}


== Syntax ==
{{Ts|CUI}}
{{T|Collection UI
|collection, goto (Optional)
|rewards, type (Optional), rarity (Optional)
|id{{=}}id
|return_id{{=}}return_id
|goback{{=}}return_id
|clickable{{=}}clickable
|fulldepth{{=}}fulldepth
|m=1
}}

===Parameters===
* {{S|collection}} - The collection to use. This will be an unenchanted version of any input item. Accepts inputs like "[[Diamond]]".
** {{S|goto (Optional)}} The ID of the UI to go to when clicked. Use comma to separate this and the previous item.
* {{S|rewards}} - The rewards for the collection. Accepts a bullet list of collection tier requirements, and rewards (Maximum of 27 tiers). Level one of the list represents the collection tier requirements, followed by an optional [[Project:Style Manual/UIs#Tabbers|go-to ID]]  linking it to another UI to show the collection rewards, separated by a comma. Level 2 of the list represents the rewards for that collection tier, followed by an optional reward type, followed by an optional item rarity, all separated by commas. See below for examples.
** {{S|type (Optional)}} Specifies the type of the reward (the grey trailing words in tooltip). For example, 'Trade', 'Coming Soon', '<Skill> Experience'. Default is 'Recipe(s)'. Set it to 'None' to not display a type. Use comma to separate this and the previous item.
** {{S|rarity (Optional)}} The template will attempt to get the rarity of the item from [[Module:Inventory slot/Tooltips]]. The default rarity is {{r|c}}. Use comma to separate this and the previous item.
* {{S|clickable}} - Whether to enclose (wrap) it with a {{Code|<nowiki><div class="sbw-ui-tabber"></nowiki>}}. Default false.
* {{S|fulldepth}} - Whether to generate all children UIs of it. Default true.
* The parameters {{S|id}}, {{s|return_id}}, and {{S|return_text}} are the same as {{T|UI}}. See the documentation on those parameters for further info. (See [[Project:Style Manual/UIs|here for further info]])

== List Syntax ==
The collection rewards use a bullet list syntax to make writing collection UI's alot easier.
The list syntax has two parts to it: 
* The first level, which is the collection requirement, followed by an optional [[Project:Style Manual/UIs#Tabbers|go-to ID]], separated by a comma.
* The second level, which is the collection rewards, followed by an optional reward type, followed by an optional reward rarity, all separeted by a comma.

===Examples===
For example, if you wanted to create a collection tier that required {{G|50,000}} [[Diamond|Diamonds]], and rewarded [[Perfect Armor]] recipes, and linked to the rewards UI named {{code|perfect-rewards}}, you would use the following syntax:
<pre>
*50k, perfect-rewards
**Perfect Helmet - Tier I
**Perfect Chestplate - Tier I
**Perfect Leggings - Tier I
**Perfect Boots - Tier I
</pre>
==Examples==
===An Example Collection===
Note: This is a completely made-up example to show the usage of this template. This collection does not exist in-game.
<pre>
{{Collection UI|fulldepth=false|Barrier|
*10
**Barrier Minion
*20
**500, Social Experience
*50 
**Barrier Upgrade
*75
**Barrier Head, None, Legendary
*100
**Coming Soon, Coming Soon
*250 
**Barrier, Trade
*1k 
**Reforged Barrier, Coming Soon
}}
</pre>
;Produces
{{Collection UI|fulldepth=false|Barrier|
*10
**Barrier Minion
*20
**500, Social Experience
*50 
**Barrier Upgrade
*75
**Barrier Head, None, Legendary
*100
**Coming Soon, Coming Soon
*250 
**Barrier, Trade
*1k 
**Reforged Barrier, Coming Soon
}}

===Diamond Collection===

<pre>{{Collection UI|Diamond|
*50 
**Diamond Minion 
*100
**Enchanted Book (Execute IV)
*250 
**Portal To The Deep Caverns
*1k 
**Enchanted Diamond
*2.5k 
**Enchanted Book (Critical IV)
*e5k 
**Diamond Spreading
*e10k 
**Hardened Diamond Helmet
**Hardened Diamond Chestplate
**Hardened Diamond Leggings
**Hardened Diamond Boots
*e25k 
**Enchanted Diamond Block
*50k 
**Perfect Helmet - Tier I
**Perfect Chestplate - Tier I
**Perfect Leggings - Tier I
**Perfect Boots - Tier I
}}</pre>
;Produces
{{Collection UI|Diamond|
*50 
**Diamond Minion
*100
**Enchanted Book (Execute IV)
*250 
**Portal To The Deep Caverns
*1k 
**Enchanted Diamond
*2.5k 
**Enchanted Book (Critical IV)
*e5k 
**Diamond Spreading
*e10k 
**Hardened Diamond Helmet
**Hardened Diamond Chestplate
**Hardened Diamond Leggings
**Hardened Diamond Boots
*e25k 
**Enchanted Diamond Block
*50k 
**Perfect Helmet - Tier I
**Perfect Chestplate - Tier I
**Perfect Leggings - Tier I
**Perfect Boots - Tier I
}}
===Redstone Dust Collection===
<pre>{{Collection UI|Redstone Dust|fulldepth=y|clickable=y}}
</pre>
;Produces
{{Collection UI|Redstone Dust|fulldepth=y|clickable=y}}

== See Also ==
{{FeatureSet/UI}}

<!-- Place template categories here -->
<includeonly>
[[Category:UI Templates]]
[[Category:UI Collection Templates]]
</includeonly>
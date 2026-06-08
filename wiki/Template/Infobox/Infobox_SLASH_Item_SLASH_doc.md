{{Documentation subpage}}
{{Lua|Infobox/Item}}
To use this template, add the {{T|Infobox/Item}} template and fill in the appropriate fields. Fields left blank will not appear in articles. This infobox template uses [[Help:Infobox|Fandom's infobox syntax]].

Sellable is not a word, but Salable and Saleable are. It is VERY intentional, please do not change it.

== Syntax ==
<pre>
{{Infobox/Item
 | title             = (optional - default: PAGENAME)
 | image             = [e.g. "Example.jpg"] (optional - default: PAGENAME.png)
 | imagecaption      = 

 | slot_item          = Any input allowed by {{Slot}} in the <1> parameter, can also be "no" to disable the slot entirely
 | slot_title         = Any input allowed by {{Slot}} in the <title> parameter
 | slot_text          = Any input allowed by {{Slot}} in the <text> parameter
 | slot_link          = Any input allowed by {{Slot}} in the <link> parameter
  
 | aka               = 
 | rarity            = Any input allowed by {{Rarity}}
 | type              = (default: Item)
 | collection        = Any input allowed by {{CollectionLink}}
 | source            = 
 | lore              = 

 | obtain            = 
 | drop_chance       = 
 | uses              = 

 | effects           = 
 | stats             = 
 | duration          = 

 | gemstone_slots    = Any input allowed by {{Gemstone slots}}

 | enchant           = (Yes/No)
 | reforge           = (Yes/No)
 | salable           = (Yes/No - default: No)
 | auctionable       = (Yes/No - default: Yes)
 | tradeable         = (Yes/No - default: Yes)
 | donatable         = (Yes/No - default: No)

 | merchant          = Any input allowed by {{NPCSprite}}
 | buy               = Any input allowed by {{Gins}}
 | sell              = Any input allowed by {{Gins}}

 | upgrades_from     = 
 | upgrades_to       = 
 
 | lower_tier        = 
 | higher_tier       = 

 | bazaar            = A valid productId (see {{BazaarData}} for details)

 | raw_materials     = Use {{Plainlist}}
 | material_cost     = 
 | daily_limit       = 
 | mat_cost_bazaar   = dotted list (using *); see {{BazaarPurchaseCalc}} for details
 | bazaar_not_including = Items not covered by [[Bazaar]]
 | mat_not_including = 

 | trade.requirement = 
 | trade.from        = 
 | trade.to          = 
 
 |tab2               = (optional) Puts all data with a "2" after the param (ex: mat_not_including2, type2) under a tab with this name
 {same fields as above, but with a 2 after}

 <...>
}}
</pre>

== Notes ==
;imagecaption
:Used for annotate item render, <em>not</em> for item description.

;lore
:For item types, do not change/add if unsure. Info such as "brewing ingredient", "crafting ingredient" belongs in '''uses'''

;lore
:Used for the exact item description in-game.

<includeonly>[[Category:Infobox templates|Item]]</includeonly>
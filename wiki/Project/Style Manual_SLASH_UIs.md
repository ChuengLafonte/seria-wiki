{{Policy|UI|UIs|SM/UI}}
:< [[Project:Policies|Wiki Policies]] | < [[Project:Style Manual|Style Manual]]
'''UIs''' Are custom interactable user interfaces that emulate the real thing in-game. 
All UI's use custom fonts. They may range from [[Project Seria Caveblock]] UI's to vanilla UIs.

==Templates Used==
Since UI's are a huge topic, many different templates are used to help reduce the strain on editors and the source code size on pages.

The templates used are as follows:

*{{T|Slot}} - The core template of UIs, which generates a basic inventory slot UI. The module that implements this may be found at [[Module:Inventory slot]].
*{{T|Crafting Table}} - A template that creates a Vanilla Minecraft crafting table. Although [[Project Seria Caveblock]] uses a different UI than the vanilla one, the two are so similar in function that it does not cause any issues for readers.
*{{T|Brewing Stand}} - A template that creates Vanilla Minecraft [[Brewing Stand]] UI. As with the same as above, the UIs are so similar that a deviation from vanilla is not needed.
*{{T|Furnace}} - A template that creates Vanilla Minecraft [[Furnace]] UI.
*{{T|UI}} - A Generic template that creates a [[Project Seria Caveblock]] Inventory UI. Highly configurable.
*{{T|UIPage}} - For transclusion of {{T|UI}}s on other pages. Custom settings can be passed to the '''first''' UI that is transcluded.
*{{T|Collection UI}} - A template that creates a [[Collection]] UI.
*{{T|Collection Rewards UI}} - A template that creates a [[Collection]] Rewards UI.
*{{T|Collection Recipe}} - A template that works in the same manner as {{T|Crafting Table}}, but as an Inventory UI showcase.
*{{T|Enchanted Collection Recipe}} - Same as {{T|Collection Recipe}}, but for enchanted items.
*{{T|Minion Recipes UI}} - Same as {{T|Collection Rewards UI}}, but for [[Minions]].
*{{T|Potion UI}} - Creates a [[Potion]] [[brewing]] recipe UI.
*{{T|UIText}} - Makes creating complicated UI tooltips a breeze.

**See the categories [[:Category:Inventory templates]] and [[:Category:UI Templates]] for all templates relating to UI's.

===Unused Vanilla UIs===
*{{Code|{{((}}Grindstone{{))}}}} - A template that creates Vanilla Minecraft '''Grindstone''' UI. Not currently used due to [[Project Seria Caveblock]] not implementing this item.
*{{Code|{{((}}Loom{{))}}}} - A template that creates Vanilla Minecraft '''Loom''' UI. Not currently used due to [[Project Seria Caveblock]] not implementing this item.
*{{Code|{{((}}Anvil{{))}}}} - A template that creates Vanilla Minecraft [[Anvil]] UI. Not currently used due to [[Project Seria Caveblock]] not implementing this item.
*{{Code|{{((}}Smithing{{))}}}} - A template that creates Vanilla Minecraft '''Smithing Table''' UI. Not currently used due to [[Project Seria Caveblock]] not implementing this item.

==Project Seria Caveblock UI layout==
Project Seria Caveblock UIs comprise of the following layout:
*The main table, which is a class called {{code|mcui}}.
*The main title, which is made out of a custom minecraft font.
*The UI slots, which are individual table cells with HTML.
**All css related to this may be found at [[MediaWiki:Custom-common.less/inventory.less]].
**Most UI templates that use lua are found in [[Module:UI]].
For a collection UI, please note the following:
*The page for a collection can be created with {{T|Collection UI}}
*Sub-pages for that collection (if any) shall be created with the following exceptions:
**The sub-page "XX Rewards" that separates the main page and the recipe, can be omitted
**For Minion Recipes, which are created with {{T|Minion Recipes UI}}, only the page with all the minions need to be created
**For Potion Recipes, which currently should be created with {{T|UI}}, only the page with all the potions need to be created
**For Armor Set Recipes, which are created with {{T|UI}}, '''should further link to subpages of individual recipes'''

==Tooltips==
Since Project Seria Caveblock makes extensive use of custom tooltips, the wiki also uses them. These tooltips are generated with [[MediaWiki:Common.js/minetip.js]].
These can be added to inventory slots with {{T|Slot}}.

When {{T|Slot}} is called, it first draws from an aliases module ([[Module:Inventory slot/Aliases]] and [[Module:Inventory slot/Tooltips]]) to see if there are any preloaded tooltips. If not manual tooltips may be added.

===Fonts===
In tooltips, custom colors may be used. The syntax for tooltips is quite simple:
*For custom colors, {{GP|minecraft:Formatting_Codes|Formatting Codes}} such as {{code|&a}} or {{code|&l}} may be used.
*For newlines, the character {{code|/}} is used. This may be prevented by escaping it as follows: {{code|\/}}

==Tabbers==
In [[Project Seria Caveblock]], UI's may link/open other UI's. The {{SITENAME}} replicates this with '''UI Tabbers'''. These may be activated by adding an element with a class called {{code|sbw-ui-tabber}} and placing UI's inside.

When a UI is placed inside, a slot with a class with the prefix {{code|goto-}} (this may be generated using {{T|Slot}} and the {{s|class}} paramater) will attempt to find a UI with the matching ID with the {{Code|ui-}} prefix.

When it succeeds, it will open the other UI. The JS that works this may be found in [[MediaWiki:Common.js]].

A Child UI is hidden at first, so it is only shown when a UI tabber is activated.

An example of such a tabber is as follows:
<pre>
<div class="sbw-ui-tabber">
<!-- Main -->
{{UI|Main|id=default
|3, 5 = Barrier
}}<!--
  ~~ any description here ~~
-->{{UI|Tab|
|3, 5 = Barrier
|return_to=default
}}
</div>
</pre>

To prevent unnecessary new lines being added before lower-level tabs, the extra lines in-between should be commented out as shown above.

{{Policies}}

{{Documentation subpage}}
{{Lua|Inventory slot}}
{{Template shortcut|Slot|clear=true}}
The inventory slot template creates an interface element which looks and acts like an in-game inventory slot.

== Item Syntax ==
<code>''[<span style="color:green">...Title</span>]<span style="color:blue">...Image</span>:<span style="color:magenta">...Name</span>,<span style="color:red">...Amount</span>[<span style="color:orange">...Description</span>]''</code>

(This wiki's Item Syntax follows the ''Basic UI Framework'', modeled after the inventory slot framework of the Minecraft Wiki first seen in 2014.)

The first parameter should supply a string in the Item Syntax. To define a single item:
* Each of the five parameters can be defined using {{Code|1=[<span style="color:green">Title</span>]<span style="color:blue">Image</span>:<span style="color:magenta">Name</span>,<span style="color:red">Amount</span>[<span style="color:orange">Description</span>]}}
* {{Code|1=<span style="color:magenta">Name</span>}} must be present; All other parameters are optional.
* If the rules above are not observed, the program will by default treat the whole input string as {{Code|item}}
* The punctuations {{Code|<nowiki>: ; , [ ]</nowiki>}} (colon, semicolon, left/right square brackets) must be escaped as {{Code|<nowiki>\: \; \, \[ \]</nowiki>}} to be correctly treated as text within a value.
* Parameters like ''link'', ''title'', and ''text'' accepts {{Code|none}} to disable the feature.

; Some Examples
First, {{Code|<nowiki>{{Slot|}}</nowiki>}} creates an empty slot: {{Slot|}}<br>
Now, we add an item {{Code|<nowiki>{{Slot|Poppy}}</nowiki>}}. By default, the whole string will be treated as the item: {{Slot|Poppy}}<br>
Now see this example. We use the proper syntax to allow us to define more things. Each available parameter will be explained later.<br>
{{Code|<nowiki>{{Invslot|[Burrito]God Potion:none,3[It's a burrito/&61,000,000 Coins]}}</nowiki>}}<br>
Results in: {{Slot|[Burrito]God Potion:none,3[It's a burrito/&61,000,000 Coins]}}

; Multiple Items
Multiple items can be defined separated by {{Code|;}}. Those items will display in an animation cycle. For example:<br>
{{Code|<nowiki>{{Slot|Poppy ; Dandelion,2 ; Sunflower,3}}</nowiki>}}<br>
Results in: {{Slot|Poppy ; Dandelion,2 ; Sunflower,3}}

; Item Variants
''[[#Predefined Tooltips|Predefined]]'' item variants can be invoked by preceding item with {{Code|*}} (for normal sequence) or {{Code|?}} (for randomized sequence). For example:<br>
{{Code|<nowiki>{{Slot|*Tulip,2 ; Dandelion,10}}</nowiki>}} gets expanded into {{Code|<nowiki>{{Slot|Red Tulip,2 ; Orange Tulip,2 ; White Tulip,2 ; Pink Tulip,2 ; Dandelion,10}}</nowiki>}}<br>
Results in: {{Slot|*Tulip,2 ; Dandelion,10}}

Parameters available to an item definition are explained below:
* {{Param|1=<span style="color:magenta">Name</span>}} - The item name, which represents the default link, image, and tooltip title.
* {{Param|1=<span style="color:red">Amount</span>}} (optional) - The stack number. Best used to display a single number M or a number range M-N. Theoretically can display any text.
* {{Param|1=<span style="color:blue">Image</span>}} (optional) - Changes the image displayed. For any slot, an image file will be expected. The default expected image name is {{Code|1=<<span style="color:magenta">Name</span>>.png}}.
* {{Param|1=<span style="color:green">Title</span>}} (optional) - Tooltip title to show on mouseover. See [[#Tooltip Formatting|''tooltip formatting'']]. Accepts {{Code|%inherit%}} to retrieve whole value from ''[[#Predefined Tooltips|predefined tooltips]]''. The default is the item name.
* {{Param|1=<span style="color:orange">Description</span>}} (optional) - Tooltip text to show on mouseover. See [[#Tooltip Formatting|''tooltip formatting'']]. Accepts {{Code|%inherit%}} to retrieve whole value from ''[[#Predefined Tooltips|predefined tooltips]]''.

== Full Syntax ==
{{T|Slot|item1[; item2; ...]|default|align|link|title|text|class|style|imgclass|numstyle}}

*{{S|item}} - The first parameter is the name of the item(s) or item declaration(s).
** The item name, link, title, text and image can be displayed accordingly to what is predefined (See [[#Tooltips Definitions]]).
** All of the above can be overridden with calling {{T|Slot}} with additional parameters.
** Additional information {{Code|, Amount}} can be appended to the name of the item. The number will be displayed at the bottom-right corner of a slot.
** Multi-frame slot can be typed in display sequence and delimited by {{Code|;}}; they will be display one after another if JavaScript is enabled.
*{{S|default}} (optional) - Image always shown under the main image
*{{S|align}} (optional) - Sets the vertical alignment
*{{S|link}} (optional) - Overrides the link
*{{S|title}} (optional) - Title to show on mouseover
*{{S|text}} (optional) - Text to show on mouseover
*{{S|class}} (optional) - Adds additional classes to the {{Code|.invslot}} class
*{{S|style}} (optional) - Adds styling to the {{Code|.invslot}}
*{{S|imgclass}} (optional) - Adds styling to the {{Code|.invitem}}
*{{S|numstyle}} (optional) - Adds styling to the stack number

== Tooltip Formatting ==
The ''title'' and ''text'' accepts Color/Formatting Codes specified in [[w:c:minecraft:Formatting codes#Color codes]] with Java version behaviour, with the following rules:
* Use {{Code|&}} followed by a letter representing a Color/Formatting Code. The specified color/formatting(s) will affect the rest of the string. For example, {{Code|&c}} starts a string colored in red, and {{Code|&a&l}} starts a string colored in green and in bold font.
* When going into a new line or when {{Code|&r}} is used, all previous Color/Formatting Codes are discarded.
* When using a color code ({{Mctxt|0|0}}-{{Mctxt|9|9}}, {{Mctxt|a|a}}-{{Mctxt|f|f}}), all previous formatting code ({{Mctxt|7|k-o}}) are discarded.
* A new line can be inserted with {{Code|/}}.
* In ''title'' and ''text'', the ampersand and the forward slash {{Code|& /}} must be escaped as {{Code|\& \/}} to be treated correctly as normal text.

== Predefined Tooltips ==
The following modules manage all '''predefined tooltips''':
* General Tooltip Definition - [[Module:Inventory slot/Tooltips]]
* Item Templates Definition - [[Module:Inventory slot/Templates]]
* Other Aliases/Final Processor - [[Module:Inventory slot/Aliases]]

All predifined tooltips can be accessed through the item name. Default values will be first be retrieved, and can be overridden by those defined in Item Syntax or Full Syntax.

The following modules manage '''predefined item variants''':
* Item Variants - [[Module:Item/Variants]]

Some special usage convensions for {{T|Slot}}:
* Pet Tooltips ''with Rarity'': {{T|Slot|'(<rarity>) <pet name>'}} (Example {{T|Slot|'Rare Monkey Pet'}})
* Potion/Enchantment Tooltips: {{T|Slot|'<potion name> <level>'}} or {{T|Slot|'Enchanted Book (<enchantment> <level>)'}}, where <level> can be an arabic or roman number

Some of these modules are [[Project:Lua#Caching|cached]] to save processing time.

== Attributions ==
Template and its Documentation initially taken from: https://minecraft.fandom.com/wiki/Template:Inventory_slot

== See Also ==
{{FeatureSet/UI}}

<includeonly>
[[Category:Inventory templates]]
</includeonly>
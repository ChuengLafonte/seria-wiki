{{Documentation subpage}}

== Overview ==
{{Lua|Crafting/UI}}

{{T|Crafting UI}} is a template used to create a crafting table UI. It functions very similar to [[Template:Crafting Table]].<br>
{{T|Collection Recipe}} works similarly, but it specifically handles collection recipe UIs.

{{Tc}}

== Usage ==
=== Parameters ===
* {{S|A1-C3}}, {{S|Output}} - The items to use in the crafting grid. There are 10 total slots, plus the output, each using {{T|Slot}}. See [[Template:Slot]] For further details. Custom code may be used by supplying the {{S|custom}} parameter.
** Each Slot parameter has the following corresponding parameters: {{S|A-C_link1-3}}, {{S|A-C_link1-3}}, {{S|A-C_class1-3}}, {{S|A-C_text1-3}}, {{S|A-C_title1-3}}.<br>These parameters represent extra options to the {{T|Slot}} templates used in this template.
* {{S|title}} - The UI title. This will override the default title of the unenchanted version of the item.
* {{s|custom}} - Disables the automatic use of {{T|Slot}} in the parameters {{S|A1-C3}} and {{S|Output}}. This will allow for custom template use.
* {{s|return_text}} - The alternate text for the back button. This parameter is optional.
* {{S|return_id}} - The id to return to when the back arrow is used (without the {{code|ui-}} prefix). This is needed when using multiple UI's through the use of [[Project Seria Wiki:Style Manual/UIs#Tabbers|UI Tabbers]].
* {{S|id}} - The id of the UI (without the {{code|ui-}} prefix). This is needed when using multiple UI's through the use of [[Project Seria Wiki:Style Manual/UIs#Tabbers|UI Tabbers]].
* {{S|hide}} - Hides the UI. Needed for [[Project Seria Wiki:Style Manual/UIs#Tabbers|UI Tabbers]]. Default '''ON'''.

=== Parameters (for Collection Recipe only) ===
* {{s|1}} - The collection to label. This will set the Interface title and the go-back tooltip.

== Examples ==
<pre>
{{Crafting UI
|A1=                      |B1= Enchanted Diamond,32 |C1= 
|A2= Enchanted Diamond,32 |B2= Enchanted Diamond,32 |C2= Enchanted Diamond,32
|A3=                      |B3= Enchanted Diamond,32 |C3= 
|Output= Enchanted Diamond Block
|id=enchanted-diamond-block
}}
</pre>
; Produces
{{Crafting UI
|A1=                      |B1= Enchanted Diamond,32 |C1= 
|A2= Enchanted Diamond,32 |B2= Enchanted Diamond,32 |C2= Enchanted Diamond,32
|A3=                      |B3= Enchanted Diamond,32 |C3= 
|Output= Enchanted Diamond Block
|id=enchanted-diamond-block
}}

=== Example with Collection Recipe + Using Stacks ===
Many recipes in Seria Caveblock require stacks of objects. In these case use a comma followed by the number, like so:
<pre>
{{Collection Recipe|Diamond
|A1=                      |B1= Enchanted Diamond,32 |C1= 
|A2= Enchanted Diamond,32 |B2= Enchanted Diamond,32 |C2= Enchanted Diamond,32
|A3=                      |B3= Enchanted Diamond,32 |C3= 
|Output= Enchanted Diamond Block
|id=enchanted-diamond-block
}}</pre>
; Produces
{{Collection Recipe|Diamond
|A1=                      |B1= Enchanted Diamond,32 |C1= 
|A2= Enchanted Diamond,32 |B2= Enchanted Diamond,32 |C2= Enchanted Diamond,32
|A3=                      |B3= Enchanted Diamond,32 |C3= 
|Output= Enchanted Diamond Block
|id=enchanted-diamond-block
}}

=== Animated ===
To make the slots animate, you make a list of blocks and objects you want to show, separated by semi-colons.
<pre>
{{Crafting UI
|A1= ; Lapis Lazuli |B1=                   ; Lapis Lazuli |C1= ; Lapis Lazuli
|A2= ; Lapis Lazuli |B2= Lapis Lazuli Block; Lapis Lazuli |C2= ; Lapis Lazuli
|A3= ; Lapis Lazuli |B3=                   ; Lapis Lazuli |C3= ; Lapis Lazuli
|Output= Lapis Lazuli,9; Lapis Lazuli Block
|id=lapis-block
}}
</pre>
; Produces
{{Crafting UI
|A1= ; Lapis Lazuli |B1=                   ; Lapis Lazuli |C1= ; Lapis Lazuli
|A2= ; Lapis Lazuli |B2= Lapis Lazuli Block; Lapis Lazuli |C2= ; Lapis Lazuli
|A3= ; Lapis Lazuli |B3=                   ; Lapis Lazuli |C3= ; Lapis Lazuli
|Output= Lapis Lazuli,9; Lapis Lazuli Block
|id=lapis-block
}}

<pre>
{{Crafting UI|title=Iron Ingot Recipe
|A1= Iron Ingot; Gold Ingot; Diamond; Lapis Lazuli
|B1= Iron Ingot; Gold Ingot; Diamond; Lapis Lazuli
|C1= Iron Ingot; Gold Ingot; Diamond; Lapis Lazuli
 |A2= Iron Ingot; Gold Ingot; Diamond; Lapis Lazuli
 |B2= Iron Ingot; Gold Ingot; Diamond; Lapis Lazuli
 |C2= Iron Ingot; Gold Ingot; Diamond; Lapis Lazuli
  |A3= Iron Ingot; Gold Ingot; Diamond; Lapis Lazuli
  |B3= Iron Ingot; Gold Ingot; Diamond; Lapis Lazuli
  |C3= Iron Ingot; Gold Ingot; Diamond; Lapis Lazuli
|Output= Block of Iron; Block of Gold; Block of Diamond; Lapis Lazuli Block
|id=multi-block
}}
</pre>
; Produces
{{Crafting UI|title=Iron Ingot Recipe
|A1= Iron Ingot; Gold Ingot; Diamond; Lapis Lazuli
|B1= Iron Ingot; Gold Ingot; Diamond; Lapis Lazuli
|C1= Iron Ingot; Gold Ingot; Diamond; Lapis Lazuli
 |A2= Iron Ingot; Gold Ingot; Diamond; Lapis Lazuli
 |B2= Iron Ingot; Gold Ingot; Diamond; Lapis Lazuli
 |C2= Iron Ingot; Gold Ingot; Diamond; Lapis Lazuli
  |A3= Iron Ingot; Gold Ingot; Diamond; Lapis Lazuli
  |B3= Iron Ingot; Gold Ingot; Diamond; Lapis Lazuli
  |C3= Iron Ingot; Gold Ingot; Diamond; Lapis Lazuli
|Output= Block of Iron; Block of Gold; Block of Diamond; Lapis Lazuli Block
|id=multi-block
}}

== Quick Copy/Paste ==
<pre>
{{Crafting UI
|A1=  |B1=  |C1= 
|A2=  |B2=  |C2= 
|A3=  |B3=  |C3= 
|Output= 
|id=
|return_id=
|return_text=
|title=
|custom=
|hide=
}}
</pre>

== See Also ==
{{FeatureSet/UI}}

<!-- Place template categories here -->
<includeonly>
[[Category:UI Templates]]
[[Category:UI Collection Templates]]
</includeonly>
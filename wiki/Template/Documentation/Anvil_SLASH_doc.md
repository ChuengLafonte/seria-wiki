{{Documentation subpage}}
{{Lua|UI}}

{{T|Anvil}} is a template used to generate an [[w:c:minecraft:Anvil|Minecraft Anvil]] interface.
{{Tc}}

== Syntax ==
{{T|Anvil|Input1|Input2|Output|cost}}
* {{Param|Input1}} - The left-hand side input slot, defined with [[Template:Inventory slot#Item Syntax|Inventory Slot Item Syntax]].
* {{Param|Input2}} - The right-hand side input slot, defined with [[Template:Inventory slot#Item Syntax|Inventory Slot Item Syntax]].
* {{Param|Output}} - The output slot, defined with [[Template:Inventory slot#Item Syntax|Inventory Slot Item Syntax]].
* {{Param|header}} - The UI header. Default "Repair & Name".
* {{Param|title}} - The text in GUI textbox. Default value of {{Param|Output}} or {{Param|Input1}}, whichever exists, with strings inside square brackets, inside round brackets, before a colon, after a comma, or after a semicolon removed.
* {{Param|cost}} - The Exp Levels cost shown. Optional. Shown as "Enchantment Cost: <cost>". If set to "expensive", displays the "Too expensive!" message instead.
* {{Param|costtext}} - Text to set as the cost text without using the formatting that {{Param|cost}} uses.
* {{Param|expensive}} - Whether the Exp Levels cost should be shown in red. Default false.
* {{Param|crossed}} - Whether the recipe arrow is crossed out.

== Examples ==
<pre>
{{Anvil
|Input1=Enchanted Book (Rend I)
|Input2=Enchanted Book (Rend I)
|Output=Enchanted Book (Rend II)
}}
</pre>
; Produces
{{Anvil
|Input1=Enchanted Book (Rend I)
|Input2=Enchanted Book (Rend I)
|Output=Enchanted Book (Rend II)
}}

<pre>
{{Anvil
|header=Combine Items
|title=Rend II
|Input1=Enchanted Book (Rend I)
|Input2=Enchanted Book (Rend I)
|Output=Enchanted Book (Rend II)
|cost=56
|expensive=true
|crossed=true
}}
</pre>
; Produces
{{Anvil
|header=Combine Items
|title=Rend II
|Input1=Enchanted Book (Rend I)
|Input2=Enchanted Book (Rend I)
|Output=Enchanted Book (Rend II)
|cost=56
|expensive=true
|crossed=true
}}

== See Also ==
{{FeatureSet/UI}}
{{Documentation subpage}}
{{Lua|UI}}

{{T|AnvilSB}} modifies {{T|Anvil}} with some parameter changes, to generate a [[w:c:minecraft:Anvil|Minecraft Anvil]] interface for SkyBlock items.
{{Tc}}

== Syntax ==
The interface can be modified with [[Template:Anvil#Syntax|any Anvil parameters]]. Note that:
* {{Param|header}} defaults to Combine Items.
* {{Param|title}} by default goes through a custom string modifier that has the following features:
** Change "Enchanted Book (Enchantment Name)" to "Enchantment Name".
* {{Param|cost}} by default shows as "Exp Level Cost: <cost>". Cost default to 0 instead of not showing up.

== Examples ==
<pre>
{{AnvilSB
|Input1=Enchanted Book (Rend I)
|Input2=Enchanted Book (Rend I)
|Output=Enchanted Book (Rend II)
|cost=12
}}
</pre>
; Produces
{{AnvilSB
|Input1=Enchanted Book (Rend I)
|Input2=Enchanted Book (Rend I)
|Output=Enchanted Book (Rend II)
|cost=12
}}

== See Also ==
{{FeatureSet/UI}}
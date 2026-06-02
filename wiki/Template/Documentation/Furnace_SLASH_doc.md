{{Documentation subpage}}
{{lua|UI}}
This template is used to create an interface that looks similar to the Furnace's.

See [[Template:Inventory slot]] for basic slot usage, this documentation page will cover additional or different functions. 
== Usage ==

=== Definition ===
<pre>
{{Furnace
|Input  = InputName,Amount
|Output = OutputName,Amount
|Fuel   = FuelName,Amount
}}
</pre>

=== Standard usage ===

<pre>
{{Furnace
|Input=  Sand,17
|Output= Glass,2
|Fuel=   Coal,3
}}</pre>

;produces:
{{Furnace
|Input=  Sand,17
|Output= Glass,2
|Fuel=   Coal,3
}}

=== Animated ===
To make the slots animate, you make a list of blocks and objects you want to show, separated by semicolons.
<pre>
{{Furnace
|Input=  Sand,17; Oak Wood,10
|Output= Glass,2; Charcoal,10
|Fuel=   Coal,3
}}</pre>

;produces:
{{Furnace
|Input=  Sand,17; Oak Wood,10
|Output= Glass,2; Charcoal,10
|Fuel=   Coal,3
}}

== See Also ==
{{FeatureSet/UI}}

<includeonly>
[[Category:Inventory templates]]
</includeonly>
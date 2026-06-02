{{Documentation subpage}}
{{lua|UI}}
This template is used to create an interface that looks similar to the [[Brewing Stand|Brewing Stand's]].

See [[Template:Inventory slot]] for basic slot usage, this documentation page will cover additional or different functions. 

== Usage ==
<pre style="width: 218px">{{Brewing Stand
|Input=   Nether Wart
|Output1= Awkward Potion
|Output2= Awkward Potion
|Output3= Awkward Potion
}}</pre>

;will result in:
{{Brewing Stand
|Input=   Nether Wart
|Output1= Awkward Potion
|Output2= Awkward Potion
|Output3= Awkward Potion
}}

=== Animated ===
To make the slots animate, you make a list of items you want to show, separated by semicolons.
<pre style="width: 388px">{{Brewing Stand
|Input=   Nether Wart,10; Redstone,64
|Output1= Awkward Potion; Magic Find Potion
|Output2= Awkward Potion; Magic Find Potion
|Output3= Awkward Potion; Magic Find Potion
}}</pre>

;will result in:
{{Brewing Stand
|Input=   Nether Wart,10; Redstone,64
|Output1= Awkward Potion; Magic Find Potion
|Output2= Awkward Potion; Magic Find Potion
|Output3= Awkward Potion; Magic Find Potion
}}

== See Also ==
{{FeatureSet/UI}}

<includeonly>
[[Category:Image templates]]
[[Category:Inventory templates]]
</includeonly>
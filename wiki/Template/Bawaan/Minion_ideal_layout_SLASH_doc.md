{{Documentation subpage}}
{{Lua|Minion/UI}}
Displays a minion's ideal layout.

== Syntax ==
{{T|Minion ideal layout|minion|ideal|border|A1..E5}}
* {{S|minion}} -  Full minion name (without the tier at the end)
* {{S|ideal}} -  What the center area is filled with
* {{S|border}} - (optional) what the border is made of (if there is one)
* {{S|A1...E5}} -  In some cases the "ideal" isn't just a solid type; in these cases, A1-A5 to E1-E5 can be used in the same manor as a crafting table template to display an item there
* In the case of a minion requiring air, the value should be "<code>Air (minion)</code>".

== Examples ==
<pre>
{{Minion ideal layout|minion=Cocoa Beans Minion|ideal=Air (minion)
|A1=Jungle Wood|C1=Jungle Wood|E1=Jungle Wood
|A3=Jungle Wood               |E3=Jungle Wood
|A5=Jungle Wood|C5=Jungle Wood|E5=Jungle Wood
}}
</pre>
{{Minion ideal layout|minion=Cocoa Beans Minion|ideal=Air (minion)
|A1=Jungle Wood|C1=Jungle Wood|E1=Jungle Wood
|A3=Jungle Wood               |E3=Jungle Wood
|A5=Jungle Wood|C5=Jungle Wood|E5=Jungle Wood
}}

<pre>{{Minion ideal layout|minion=Spider Minion|ideal=Air (minion)|border=Oak Fence}}</pre>
{{Minion ideal layout|minion=Spider Minion|ideal=Air (minion)|border=Oak Fence}}

<includeonly>[[Category:General wiki templates]]</includeonly>
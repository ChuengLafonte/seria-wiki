{{Documentation subpage}}
{{Lua|Link}}
Creates a link to a specific tier of a collection. Also works with slayer types.

==Syntax==
{{Template shortcut|Coll}}
{{t|CollectionLink|1|2|showIcon}} where:
*{{S|1}} is the collection name.
*{{S|2}} is the collection tier. Use either roman or arabic numerals. Case doesn't matter. This parameter is optional.
*{{S|showIcon}} or {{S|icon}} or {{S|image}} or {{S|img}} - (optional) if a "yes" value, then the collection icon will appear before link.

For each of use in templates, variable 1 can be both the the collection and tier (ex: "Wheat II"). In this case variable 2 must be left blank.

==Examples==
;Example 1
:Using parameters {{S|1}} and {{S|2}}.
<pre>
{{CollectionLink|Redstone|11}}
</pre>
produces 

{{CollectionLink|Redstone|11}}
;Example 2
:Using parameters {{S|1}}, {{S|2}} and {{S|showIcon}}.
<pre>
{{CollectionLink|Cobblestone|IV|showIcon=yes}}
</pre>
produces

{{CollectionLink|Cobblestone|IV|showIcon=yes}}
;Example 3
:Using parameters {{S|1}} and {{S|2}}, using [[Slayer]] collection.
<pre>
{{CollectionLink|Wolf Slayer|4}}
</pre>
produces

{{CollectionLink|Wolf Slayer|4}}
;Example 4
:Using only {{S|1}} parameter, with tier.
<pre>
{{CollectionLink|Wheat II}}
</pre>
produces

{{CollectionLink|Wheat II}}
;Example 5
:Using only {{S|1}} parameter, without tier.
<pre>
{{CollectionLink|Potato}}
</pre>
produces

{{CollectionLink|Potato}}

==See Also==
*{{T|EnchantmentsLink}}
*{{T|ReforgingLink}}
*{{T|PotionsLink}}
*{{T|PotionName}}

<includeonly>
[[Category:Linking Templates]]
</includeonly>
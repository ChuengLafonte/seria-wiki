{{Documentation subpage}}
==Overview==
{{Lua|Collection/UI}}
{{T|Collection Rewards UI}} is a template used to create a collection rewards UI.
{{Tc}}


==Syntax==
{{T|Collection Rewards UI|
|collection
|tier
|rewards list
|return_id{{=}}return_id
|return_text{{=}}return_text
|id{{=}}id
|hide{{=}}hide
|clickable{{=}}clickable
|fulldepth{{=}}fulldepth
|m=1
}}
*{{S|collection}} - The collection to use. This can be an item like [[Diamond]]
*{{S|tier}} - The tier of collection to use. This can an integer.
*{{S|rewards list}} - The list of rewards to list in the collection. The rewards will be arranged depending of the amount of items provided in the list.
**A list entry follows this format:
**The list entry can be just an item like [[Diamond]], or a comma-separated list. The list is as follows: The first item is the same as if the list was not used, the second item is the [[HSW:Style Manual/UIs#Tabbers|Go-To ID]] of the slot (without the {{code|goto-}} prefix, the third item is the slot's custom title, and the fourth and final item is the slot's custom text. All but the first element may be empty.
** An example of this format is: {{code|Diamond, example-id, &aCustom Title, &cCustom Text}}
** This would produce a slot like this: {{Slot|Diamond|link=none|id=goto-example-id|title=&aCustom Title|text=&cCustom Text}}
* {{S|clickable}} - Whether to enclose (wrap) it with a {{Code|<nowiki><div class="sbw-ui-tabber"></nowiki>}}. Default false.
* {{S|fulldepth}} - Whether to generate all children UIs of it. Default true.
* The parameters {{S|id}}, {{s|return_id}}, and {{S|return_text}} are the same as {{T|UI}}. See the documentation on those parameters for further info.

==Examples==
===[[Diamond]]===

<pre>{{Collection Rewards UI|Diamond|2|
*Enchanted Book (Execute IV)
}}</pre>
;Produces
{{Collection Rewards UI|Diamond|2|
*Enchanted Book (Execute IV)
|return_id=Test
}}

===[[Redstone]]===

<pre>{{Collection Rewards UI|Redstone|3|
*Enchanted Book (Efficiency IV)
}}</pre>
;Produces
{{Collection Rewards UI|Redstone|3|
*Enchanted Book (Efficiency IV)
}}

== See Also ==
{{FeatureSet/UI}}

<!-- Place template categories here -->
<includeonly>
[[Category:UI Templates]]
[[Category:UI Collection Templates]]
</includeonly>
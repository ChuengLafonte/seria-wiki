{{Documentation subpage}}
This template is used to streamline the [[Template:Collection Recipe]] template specifically for the recipes of enchanted items, for other items use [[Template:Collection Recipe]]. The parameters {{s|id}}, {{s|id}}, {{s|return_id}}, {{s|return_text}}, {{s|title}} are the same as [[Template:Collection Recipe]].

== Usage ==
<pre>{{Enchanted Collection Recipe}}</pre>
The parameter {{s|input_goto}} may be used to specify for when multiple pages are used.
;produces (on [[Cobblestone]] page):
{{Enchanted Collection Recipe|Input=Cobblestone|Output=Enchanted Cobblestone}}

==Changing input and output==
By default the page name is used as ingredients and 'Enchanted (page name)' is used for the input. These parameter can be used for items with differnt name formats or the recipe of the enchanted item in the enchanted form's article.
<pre>{{Enchanted Collection Recipe|Potato|Input = Enchanted Potato|Output = Enchanted Baked Potato}}</pre>

{{Enchanted Collection Recipe|Potato|Input=Enchanted Potato|Output= Enchanted Baked Potato}}

==Changing input count==
For recipes which needs more/less than 32 items per slot add a comma to the end, i.e. Ender Pearl --> Enchanted Ender Pearl
<pre>{{Enchanted Collection Recipe|Input = Ender Pearl,4|Output = Enchanted Ender Pearl}}</pre>

{{Enchanted Collection Recipe|Input=Ender Pearl,4|Output = Enchanted Ender Pearl}}

==Changing output count==
For recipes which craft more than one item add a comma to the end, i.e. Redstone Blocks --> Enchanted Redstone
<pre>{{Enchanted Collection Recipe|Output = Enchanted Redstone,9}}</pre>

{{Enchanted Collection Recipe|Input=Block of Redstone|Output= Enchanted Redstone,9}}

==Using Shapeless Recipes==
If desired, shapeless recipes may be used in place of normal enchanted recipes by setting {{s|shapeless}} to true.
<pre>{{Enchanted Collection Recipe|Input=Block of Redstone|Output= Enchanted Redstone,9|shapeless=1}}</pre>

{{Enchanted Collection Recipe|Input=Block of Redstone|Output= Enchanted Redstone,9|shapeless=1}}
== See Also ==
{{FeatureSet/UI}}
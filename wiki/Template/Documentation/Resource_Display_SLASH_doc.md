{{Documentation subpage}}
==Overview==
{{Lua|Item}}
The '''Resource Display''' template is used to display item, alongside its amount and image. This template is very similar to {{T|Item Display}}, but accepts the amount too.
{{Tc}}

==Syntax==
{{Ts|RD}}
{{T|Resource Display|1|image|nolink|noerror|ignoreodds|noimgpad}}
*{{S|1}} - the item string, structured as shown here: {{Code|&#60;amount&#62;x &#60;item string&#62;}}. Note that the {{Code|x}} character is not required.
**Amount should resemble any of the following:
***Singular amount, such as {{Code|5x [something]}}.
***Range-like amount, such as {{Code|5-12x [something]}}. This is usually used to indicate that a certain mob drop is usually dropped in different quantities (in this example, ranging from 5 to 12).
***An "or" type amount, such as {{Code|0 or 4x [something]}}. This should be used to indicate that there are two options: in this example, either {{Code|0}} or {{Code|4}}. This is usually used to indicate that a certain mob drop is not guaranteed. Should be paired with the "odds" component (see [[#Odds]]).
**:Range-like and "or" type amounts can be combined, creating something like <span style="white-space:nowrap;">{{Code|0 or 18-28x [something]}}</span>.<br/>If the value typed in is higher than 64, a hover text counting item stacks will be added (example: {{Code|160x}} will result in: {{G|{{Abbr|160x|2 stacks of 64 and 32 items (160 items total)}}}})
**Item string should contain the name of the item. Can also contain the following:
***Alternate text - separated from the item name by {{Code|!}} character, such as {{Code|item name!alt text}}. If the {{Code|!}} character is not used, every feature below can be used freely.
***Comment - all words after the first {{Code|;}} character will be treated as comment. It will not be treated as an item string.
***Drop chance - contained in between two {{Code|%}} characters, such as {{Code|item name %drop chance%}}. Between the two {{Code|%}} characters, anything can be typed - examples include: 
****{{Code|%1 in 200%}} (result: <sup>(1 in 200)</sup>)
****{{Code|%20%%}} (result: <sup>(20%)</sup>)
****{{Code|%something%}} (result: <sup>(something)</sup>)
****{{Code|%{{((}}Red{{!}}text{{))}}%}} (result: <sup>({{Red|text}})</sup>). 
****Most templates can be used in there too, although some may break.
**:It doesn't matter if the drop chance string is placed before or after the {{Code|!}} character - it will still work properly. The result of this operation is always located at the very end of the output string.
***Enchantment - contained in between two {{Code|&}} characters, such as {{Code|item name &enchantment&}}. Between the two {{Code|&}} characters, any valid enchantment string can be typed (see [[Template:EnchantmentsLink/doc]]). It doesn't matter if the enchantment string is placed before or after the {{Code|!}} character - it will still work properly. The result of this operation is always located after the item name and before the drop chance.
***Rarity - contained in between two {{Code|$}} characters, such as {{Code|item name $rarity$}}. Between the two {{Code|$}} characters, any valid rarity string can be typed (see [[Template:Rarity/doc]]). It '''DOES''' matter  if the enchantment string is placed before or after the {{Code|!}} character - it will only work when used after the {{Code|!}} (otherwise it is ignored). The location of this feature matters - the rarity will be placed in the exact same place where it is used in the input.
***If the item name is set to something like {{Code|Miner Armor piece}}, the link and image will be adjusted to work properly. The output would be: {{Item Display|Miner Armor piece}}. The image will always be a helmet image.
*{{S|image}} or {{S|img}} or {{S|i}} - whether or not images should be displayed. Default to {{Code|true}}.
*{{S|nolink}} or {{S|nl}} - whether or not links should be used. Default to {{Code|false}}.
*{{S|noerror}} or {{S|ne}} - whether or not text should be displayed despite errors occurring. Default to {{Code|false}}. If set to {{Code|true}}, the whole input is returned.
*{{S|ignoreodds}} - if on, even when there is value for odds, it will not be displayed. Default off.
*{{S|noimgpad}} - if on, an item name without a file will not be padded with a blank space in front. Default off.

==Examples==
;Example 1
:Plain and simple
<pre>
{{Resource Display|320x Dirt}}
</pre>
produces
:{{Resource Display|320x Dirt}}
<br/>
;Example 2
:With range-like amount
<pre>
{{Resource Display|1-4x String}}
</pre>
produces
:{{Resource Display|1-4x String}}
<br/>
;Example 3
:With "or" type amount and drop chance
<pre>
{{Resource Display|0 or 1x Weak Wolf Catalyst %1 in 200%}}
</pre>
produces
:{{Resource Display|0 or 1x Weak Wolf Catalyst %1 in 200%}}
<br/>
;Example 4
:With standard amount and enchant
<pre>
{{Resource Display|1x Enchanted Book &Smite 6&}}
</pre>
produces
:{{Resource Display|1x Enchanted Book &Smite 6&}}
<br/>
;Example 5
:With standard amount and rarity
<pre>
{{Resource Display|1x $rare$ Enderman Pet}}
</pre>
produces
:{{Resource Display|1x $rare$ Enderman Pet}}
<br/>
;Example 6
:With alternate text
<pre>
{{Resource Display|1x Stone!Diamond}}
</pre>
produces
:{{Resource Display|1x Diamond!Stone}}
<br/>
;Example 7
:With no link
<pre>
{{Resource Display|1x Stone!Lorem Ipsum|nolink=true}}
</pre>
produces
:{{Resource Display|1x Stone!Lorem Ipsum|nolink=true}}
<br/>
;Example 8
:With everything combined
<pre>
{{Resource Display|0 or 18-28x Iron Ingot!$supreme$ Gold Ingot %5%% &Fortune 1&}}
</pre>
produces
:{{Resource Display|0 or 18-28x Iron Ingot!$supreme$ Gold Ingot %5%% &Fortune 1&}}

==See Also==
*{{T|Resource List}}
*{{T|Item Display}}

<includeonly>
[[Category:Templates]]
</includeonly>

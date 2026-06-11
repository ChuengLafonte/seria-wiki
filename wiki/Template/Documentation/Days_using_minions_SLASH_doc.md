{{Documentation subpage}}
{{Lua|Minion}}
This template adds a table that auto calculates how long it would take to crafting something using only a minion.

Note: Not all minions are currently supported. All mining and wood cutting are, as are most farming ones. no combat or "other" ones are.

==Syntax==
{{T|Days using minions|minion|amount|item|split|fullwidth}}

===Parameters===
*{{S|minion}} - Name of minion (without "minion") - This is case sensitive
*{{S|amount}} - Number of resources attempting to gain
*{{S|item}} - (Optional, only when the item that is needed is not the main item collected from the minion) Name of minion (without "minion") - This is case sensitive
*{{S|split}} - Whether to split the table into two rows; default true
*{{S|fullwidth}}/{{S|noscroll}} - Setting this to true will force the row to show in full width and without a scroll bar; default false

==Example==
<pre>{{Days using minions|minion=Dark Oak|amount=245760}}</pre>
{{Days using minions|minion=Dark Oak|amount=245760}}

==Math==
This template does the following math for each minion tier:

<math>actionsPerDay = \frac{60}{secondsPerAction \times 2} \times 60 \times 24</math>

<math>daysToGetItem = \frac{neededItems}{actPerDay \times itemsPerAct}</math>

<includeonly>[[Category:Table templates]]</includeonly>

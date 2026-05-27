The '''Link''' module contains all templates directly related to links.
{{Md|Arguments|Yesno|String|Collection|Color}}
==Loading the module==
To load this module, Add this line of code to the start of your module:
{{darkCodeBox|lang=lua|t=
local mLink = require('Module:Link')
}}
All methods described below will be available under the loaded table.

==Methods==
All methods are available below as fields under the required object name.
__TOC__
===collectionLink===
{{Dm|Armor}}{{Dt|clear=true|CollectionLink}}
{{M|_collectionLink|collection;str|tier;num,nr|showIcon;bool,nr}}<br/>
This method returns a link to a collection specified in {{S|collection}}, with a Roman tier number specified in {{S|tier}} (input can be both arabic and roman). If {{S|showIcon}} is {{Code|true}}, an image will also show up. Tier number can also be contained in {{S|collection}}, separated with a single space.
{{Clear}}

===enchantmentsLink===
{{Dt|clear=true|EnchantmentsLink}}
{{M|_enchantmentsLink|enchant;str|alt;str|options;table}}
{{Clear}}

<div></div>
This module provides methods relating to rarities and their data.
{{dm|Arguments|Loader|String|Table|Yesno|Color|Mainonly|RarityTier/Aliases|RarityTier/Data|Color/Data}}
{{Tc}}

== Submodules ==
{{submodules}}

== Loading the module ==
To load this module and make its method available for use, Add this line of code to the start of your module:
{{darkCodeBox|lang=lua|t=
local rarityTier = require('Module:RarityTier')
}}
The methods documented below will be available for use under the variable name you loaded this module in.

Alternatively, you can use this module using the code below by using {{Code|[[Module:LoadLib]]}}.
{{darkCodeBox|lang=lua|t=
local loadLib = require('Module:LoadLib')

_G = loadLib(_G, {
    rarityTier='Module:RarityTier',
    -- Place any other modules to load in here...
})
}}
Depending on the settings you used in {{m|loadLib|link=Module:LoadLib}}, the methods of this module may be available under their respective variables in the module this module was loaded in.

== Methods ==
The methods documented below will be available for use under the variable name you loaded this module in.
=== {{M|._getRarity|tierid;string}} ===
This method returns the data table relating to the tier of data provided in {{Param|tierid}}. The parameter {{Param|tierid}} is not case sensitive, and can deal with both full names and aliases for the rarity tiers.

=== {{M|._getTier|tierid;string,number}} ===
This method returns the data table relating to the tier of data provided in {{Param|tierid}}, as well as the key to such data, in the order {{Code|tier}}, {{Code|key}}. The parameter {{Param|tierid}} is not case sensitive, and can deal with both full names and aliases for the rarity tiers. It can also be a number, or a number formatted as a string, and the tier with the corresponding {{Code|order}} value in the data will be chosen.

=== {{M|._getTierIterable}} ===
This method returns returns an iterable version of {{Code|p._getTier}}. This is used when the order of the tiers is important, as using pairs() on [[Module:RarityTier/Data]] will not retain the order.

=== {{M|._orderedTiers}} ===
This method returns returns the rarity tier data in an ordered array, starting from the lowest rarity.

=== {{M|.getHexColor|r;string,number}} ===
This method returns returns hex color of the rarity provided in the parameter {{Param|r}}. The parameter {{Param|r}} can be formatted in the same way as the parameter for {{Code|p._getTier}}.

=== {{M|.link|frame;frame}} ===
This method returns a formatted link for the rarity entered. The first positional value of the {{Param|frame}} specifies the rarity to make a link for and can be formatted in the same way as the parameter for {{Code|p._getTier}}. The second positional value of the {{Param|frame}} provides alternate text to be displayed, rather than the rarity name. The {{Code|addcategory}} value of the {{Param|frame}} parameter, which defaults to false, adds the category for the rarity to the page. The {{Code|nolink}} value of the {{Param|frame}} parameter, which defaults to false, removes the link to the Rarity page. The {{Code|ordered}} value of the {{Param|frame}} parameter, which defaults to false, adds an invisible order number in front for table sorting.

=== {{M|.orderedLink|frame;frame}} ===
This method returns a formatted link for the rarity entered. The first positional value of the {{Param|frame}} specifies the rarity to make a link for and can be formatted in the same way as the parameter for {{Code|p._getTier}}. The second positional value of the {{Param|frame}} provides alternate text to be displayed, rather than the rarity name. The {{Code|addcategory}} value of the {{Param|frame}} parameter, which defaults to false, adds the category for the rarity to the page. The {{Code|nolink}} value of the {{Param|frame}} parameter, which defaults to false, removes the link to the Rarity page.

=== {{M|._link|tierid;string,number|linkText;string|addcategory;boolean,string|nolink;boolean|ordered;boolean,string}} ===
This method returns a formatted link for the rarity entered. {{Param|tierid}} specifies the rarity to make a link for and can be formatted in the same way as the parameter for {{Code|p._getTier}}. {{Param|linkText}} provides alternate text to be displayed, rather than the rarity name. The {{Parameter|addcategory}} parameter, which defaults to false, adds the category for the rarity to the page. The parameter {{Param|nolink}}, which defaults to false, removes the link to the Rarity page. The {{Param|ordered}} parameter, which defaults to false, adds an invisible order number in front for table sorting.

=== {{M|._colorText|tierid;table|text;string|withFormat;boolean|link;string|nolink;boolean}} ===
This method returns colored text based on the color of the rarity specified in the parameter {{Param|tierid}}. The parameter {{Param|text}} specifies the string to be colored. The parameter {{Param|withFormat}}, which defaults to true, specifies whether the text should be bolded. The parameter {{Param|link}} specifies a link destination for the text. The parameter {{Param|nolink}}, which defaults to false, specifies whether a link should be used destination for the text, overriding the previous parameter.

=== {{M|._switch|tierid;string|cases;table}} ===
This method returns the value from a lua table based on the rarity passed in. Aliases are accounted for (ex: tierid='c' will trigger the 'common' key in the table). As an example, the function: _switch('rare', { common='a', uncommon='b', rare='c' }) would return 'c'.

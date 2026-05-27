This module is focused on wrapping text with html or wikitext tags.
{{dm|Arguments|String}}
{{Tc}}

== Loading the module ==
To load this module and make its method available for use, Add this line of code to the start of your module:
{{darkCodeBox|lang=lua|t=
local tag = require('Module:Tag')
}}
The methods documented below will be available for use under the variable name you loaded this module in.

Alternatively, you can use this module using the code below by using {{Code|[[Module:LoadLib]]}}.
{{darkCodeBox|lang=lua|t=
local loadLib = require('Module:LoadLib')

_G = loadLib(_G, {
    tag='Module:Tag',
    -- Place any other modules to load in here...
})
}}
Depending on the settings you used in {{m|loadLib|link=Module:LoadLib}}, the methods of this module may be available under their respective variables in the module this module was loaded in.

== Methods ==
The methods documented below will be available for use under the variable name you loaded this module in.
=== {{M|.nowiki|frame;frame}} ===
This method returns the text provided in the first positional argument of the {{Parameter|frame}} parameter, with the same behavior as being wrapped with the nowiki tag.

=== {{M|.insetCode|frame;frame}} ===
This method returns a formatted string representing code. The text represented is determined by the first positional argument of the {{Parameter|frame}} parameter.

=== {{M|.syntaxhighlight|frame;frame}} ===
This method returns syntax highlighted text. The text to be syntax highlighted is determined by the {{Code|text}}, {{Code|t}}, or first positional argument of the {{Parameter|frame}} parameter. The programming language that the text is meant to be interpreted as is determined by the {{Code|lang}} or {{Code|l}} arguments of the {{Parameter|frame}} parameter.
{{Lua doc subpage}}
This module is used to build a [[mw:Help:Extension:tabber|tabber]] using lua code. Unlike the wikitext version, this version is capable of doing nested tabbers.
==Syntax==
===Function Syntax===
{{LuaT|_optionalTabber|{name, body}||{name, body}|t=1}}
===Invoke syntax===
*{{S|name}} is the name of the tabber head. This can be anything that outputs raw text.
*{{S|body}} is the text of the body. This can be anything.
**The format for the syntax is the following: {{code|{name{{=}}<name>, body{{=}}<body>{{)}}}}

===Loading===
You can add the following line of code to a module to load this function:
{{DarkCodeBox|lang=lua|t=
local optionalTabber = require('Module:Tabber')._optionalTabber
}}

==Examples==
===Wikitext===
<pre>{{#invoke:Tabber|optionalTabber|name1=foo|body1=baz}}</pre>
;Produces
{{#invoke:Tabber|optionalTabber|name1=foo|body1=baz}}
===Function===
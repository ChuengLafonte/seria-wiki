{{Documentation subpage}}

==Overview==
{{Lua|LuaFunction}}
{{T|LuaFunction}} is a template similar to {{T|T}}, used to explain the syntax of a Lua function.
{{Tc}}

==Syntax==
{{Ts|LuaT|M}}
{{T|LuaFunction|1|2|3|...|∞}}, where:
*{{S|1}} is the name of the function. Can be anything. Strictly required.
*{{S|2}}, {{S|3}} and later ones are the arguments for a function. Optional.
**Use {{Code|;}} to specify the flags of the variable, seperated by {{code|,}}. The correct usage is: {{Code|arg;type1, type2, ...}}. {{Code|type}} can be any of these:
***{{Code|;}} can be used as a trailing value to disable the flags display all together.
{| class="wikitable"
!Flag
!Aliases
!Output
|-
|{{Code|number}}
|{{PL|
*{{Code|num}}
*{{Code|n}}
}}
|<code><sup>(<abbr title="Number value. Can only contain numbers from 0 to 9.">{{LightPurple|num}}</abbr>)</sup></code>
|-
|{{Code|hexadecimal}}
|{{Code|hex}}<br/>{{Code|h}}
|<code><sup>(<abbr title="Hexadecimal value. Can only contain numbers from 0 to 9 and letters from A to F.">{{LightPurple|hex}}</abbr>)</sup></code>
|-
|{{Code|red green blue}}
|{{Code|rgb}}
|<code><sup>(<abbr title="Red Green Blue value (String).">{{Red|R}}{{Green|G}}{{Blue|B}}</abbr>)</sup></code>
|-
|{{Code|string}}
|{{PL|
{{Code|text}}
*{{Code|str}}
*{{Code|t}}
}}
|<code><sup>(<abbr title="String or text value.">{{Aqua|text}}</abbr>)</sup></code>
|-
|{{Code|boolean}}
|{{PL|
{{Code|bool}}
*{{Code|b}}
*{{Code|yes/no}}
*{{Code|yesno}}
*{{Code|y/n}}
*{{Code|yn}}
}}
|<code><sup>(<abbr title="Boolean value. Put simply, a yes/no value.">{{Orange|bool}}</abbr>)</sup></code>
|-
|{{Code|table}}
|{{PL|
*{{Code|t}}
*{{code|tab}}
*{{code|tbl}}
*{{code|tabl}}
*{{code|array}}
*{{code|arr}}
*{{code|obj}}
*{{code|object}}
}}
|<code><sup>(<abbr title="Table value. This table can contain other values of any type, or even other tables.">{{Green|table}}</abbr>)</sup></code>
|-
|{{Code|frame}}
|{{PL|
*{{Code|fr}}
*{{code|fra}}
*{{code|fram}}
*{{code|frme}}
}}
|<code><sup>(<abbr title="Frame (Table) value. This value is generated automatically when the function is called by #invoke, or can be called manually by passing a frame object to it by using mw.getCurrentFrame()">{{Color|#b52a2a|frame}}</abbr>)</sup></code>
|-
|{{Code|frame}}
|{{PL|
*{{Code|fr}}
*{{code|fra}}
*{{code|fram}}
*{{code|frme}}
}}
|<code><sup>(<abbr title="Function value. This function is likely a callback function in the module.">{{Color|white|function}}</abbr>)</sup></code>
|-
|{{Code|not required}}
|{{PL|
*{{Code|nr}}
*{{code|not r}}
*{{code|notreq}}
}}
|<code><sup>(<abbr title="This field is not required.">{{Color|#8972e5|NR}}</abbr>)</sup></code>
|-
|{{Code|nil}}
|{{PL|
*{{Code|ni}}
*{{code|null}}
*{{code|undefined}}
*{{code|undef}}
*{{code|nll}}
}}
|<code><sup>(<abbr title="Nil value. This parameter may be omitted from the function call.">{{Color|#f9b3b3|nil}}</abbr>)</sup></code>
|-
|{{Code|any}}
|{{PL|
*{{Code|an}}
*{{code|a}}
*{{code|al}}
*{{code|all}}
}}
|<code><sup>(<abbr title="Any value is allowed.">{{Color|LightPurple|a}}{{Color|Aqua|n}}{{Color|Green|y}}</abbr>)</sup></code>
|}

==Examples==
;Example 1
:As simple as possible
<pre>
{{LuaFunction|myFunction}}
</pre>
produces
{{LuaFunction|myFunction}}

;Example 2
:With function name and couple of arguments
<pre>
{{LuaFunction|myFunction|arg1|arg2|arg3-8}}
</pre>
produces
{{LuaFunction|myFunction|arg1|arg2|arg3-8}}

;Example 3
:With function name, couple of arguments and corresponding types
<pre>
{{LuaFunction|myFunction|arg1;num|arg2;text|arg3;bool}}
</pre>
produces
{{LuaFunction|myFunction|arg1;num|arg2;text|arg3;bool}}

;Example 3
:With function name, couple of arguments and multiple corresponding types and one argument with no types
<pre>
{{LuaFunction|myFunction|arg1;num,str|arg2;text,hex|arg3;bool,func,nr|arg4;}}
</pre>
produces
{{LuaFunction|myFunction|arg1;num,str|arg2;text,hex|arg3;bool,func,nr|arg4;}}

== See Also ==
{{FeatureSet/Documentations}}

<includeonly>
[[Category:Templates]]
[[Category:General wiki templates]]
</includeonly>
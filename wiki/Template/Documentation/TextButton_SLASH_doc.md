{{Documentation subpage}}

{{T|TextButton}} is a template used to create a button.
{{Tc}}

== Syntax ==
{{T|TextButton|text|id|style|class|type}}
* {{Param|text}} - Button text.
* {{Param|id}} - An id for the button. Optional.
* {{Param|style}} - Additional style for the button. Optional.
* {{Param|class}} - Additional class for the button. Optional.
* {{Param|type}} - Base type of the button. Optional. Defaults to {{Code|default}}. Allowed: {{Code|default}}, {{Code|wds}}

TextButton also has the following "is-attributes":
{| class="wikitable"
! Attribute !! Description !! Usable on types
|-
| {{Param|isfill}} || Whether the button fills the width of the display || default, wds
|-
| {{Param|issecondary}} || Whether the button uses the "secondary" outlook || default, wds
|-
| {{Param|istext}} || Whether the button uses the "text" outlook || wds
|-
| {{Param|isfill}} || Whether the button uses the "active" outlook || wds
|-
| {{Param|isforward}} || Whether the button uses the "forward" outlook || default
|}

== Examples ==
<pre>
{{TextButton|A Default Button}} {{TextButton|A WDS Button|type=wds}}
</pre>
; Produces
{{TextButton|A Default Button}} {{TextButton|A WDS Button|type=wds}}

<pre>
{{TextButton|A Default Secondary Button|issecondary=true}}
{{TextButton|A Default Forward Button|isforward=true}}
<br />
{{TextButton|A WDS Secondary Button|type=wds|issecondary=true}}
{{TextButton|A WDS Text Button|type=wds|istext=true}}
{{TextButton|A WDS Active Button|type=wds|isactive=true}}
<br />
{{TextButton|A WDS Full-width Button|type=wds|isfill=true}}
<br />
{{TextButton|A Default Full-width Button|isfill=true}}
</pre>
; Produces
{{TextButton|A Default Secondary Button|issecondary=true}}
{{TextButton|A Default Forward Button|isforward=true}}
<br />
{{TextButton|A WDS Secondary Button|type=wds|issecondary=true}}
{{TextButton|A WDS Text Button|type=wds|istext=true}}
{{TextButton|A WDS Active Button|type=wds|isactive=true}}
<br />
{{TextButton|A WDS Full-width Button|type=wds|isfill=true}}
<br />
{{TextButton|A Default Full-width Button|isfill=true}}
{{Documentation subpage}}
==Overview==
{{T|Policy}} is a template used to denote policy pages.
{{Tc}}

==Syntax==
{{Ts|POL}}
{{T|Policy|shortcut 1|shortcut 2||shortcut 6|legal}}
*{{S|shortcut 1|shortcut 6}} - The shortcuts for the policy page. All shortcuts are converted to uppercase and are automatically prefixed with {{code|HSW}}, so there is no need to apply a namespace prefix. All that is needed is a phrase like {{code|IMAGE}}
*{{S|legal}} or {{s|l}} - Whether the policy takes into account legal considerations.

==Examples==
===Example 1===
<pre>{{Policy|}}</pre>
;Produces
{{Policy|}}

===Example 2===
<pre>{{Policy|IMAGES}}</pre>
;Produces
{{Policy|IMAGES}}

===Example 3===
<pre>{{Policy|IMAGE|legal=1}}</pre>
;Produces
{{Policy|IMAGES|legal=1}}

==See Also==
*{{T|Information Page}} - Very similar to this template, but for less formal pages/information pages.
*{{T|Shortcut}}
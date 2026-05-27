{{Documentation subpage}} {{Lua|RightBox}}
This template provides a box on the side of a page that lists all shortcuts that link to that page (using [[Help:redirects|redirects]]). It should not be used on article pages (main space).
This template has 2 syntax methods, a list, or a list of unnamed arguments.

For one designed for templates see {{t|Template shortcut}}.
==Syntax==
{{T|Shortcut|1 or bullet list|2||∞}}
*{{S|1}} - The first shortcut entry or a bullet list. The list entry is the page shortcut title.
*{{S|2|∞}} - The page names of the shortcuts to link to.
==Example 1 using first syntax method==
<pre>{{Shortcut|HSW:Images|HSW:BLOCK|HSW:STAFFREQ}}</pre>
;produces&#58;
{{Shortcut|HSW:Images|HSW:BLOCK|HSW:STAFFREQ}}

{{Clear}}
==Example 2 using second syntax method==
<pre>{{Shortcut|
*HSW:Images
*HSW:BLOCK
*HSW:STAFFREQ
}}</pre>
;produces&#58;
{{Shortcut|
*HSW:Images
*HSW:BLOCK
*HSW:STAFFREQ
}}

<includeonly>[[Category:General wiki templates]]</includeonly>
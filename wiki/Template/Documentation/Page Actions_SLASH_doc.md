{{Documentation subpage}}
==Overview==
{{Lua|Page Actions}}
{{T|Page Actions}} is a template used to display a list of page actions. The inputs can be configured to use custom urls.
{{Tc}}


==Syntax==
{{Ts|PA}}
{{T|Page Actions|1|2|...|∞|format|style|class|id}}
*{{S|1}} or {{S|1|2|∞}} - The argument to the list or a bullet list or a list of items seperated by commas.
**[[#List entry example|See This section for any valid inputs.]]
*{{S|format}} or {{S|f}} - This is The format of the list of actions. This can be set to the following: {{Code|Parenthases, List, or Inline}}
*{{S|style}} or {{S|s}} - Any {{Code|CSS}} styles you want to apply go here.
*{{S|class}} or {{S|c}} - Any valid {{Code|CSS}} classes you want to apply go here.
*{{S|id}} or {{S|i}} - The id of the element.
==List entry example==
This can be any valid action to a page or the following action:
*{{Code|Subpages}}
*{{Code|Logs (Filter log, deletion log, block log, protection log, move log)}}
*{{Code|What links here}}
*{{Code|Protect}}
*{{Code|Delete}}
*{{Code|Move}}
You can also add a parentheses at the end of the action for any extra url actions you want to add to the link.
*Note this extension is optional. It is recommenced you familiarize yourself with MediaWiki urls before using this option.
;Example
<pre>
Move (wpNewTitle{{=}}Example&wpOldTitle{{=}}Example old title)
</pre>
You can seperate URL parameters using {{Code|&}} or {{Code|;}}.
You can also use {{Code|-}} in place of {{Code|{{=}}}} as it needs to be escaped using {{T|{{=}}}}.
==Examples==
===Example 1 using a Bullet List===

<pre>{{Page Actions|
*Delete
*move
*protect
*subpages
*filter log
}}</pre>
;Produces
{{Page Actions|
*Delete
*move
*protect
*subpages
*filter log}}
===Example 2 using a arguments list===

<pre>{{Page Actions
|Delete
|move
|protect
|subpages
|filter log
}}</pre>
;Produces
{{Page Actions
|Delete
|move
|protect
|subpages
|filter log
}}
===Example 3 using a comma list===

<pre>{{Page Actions|
Delete,
move,
protect,
subpages,
filter log
}}</pre>
;Produces
{{Page Actions|
Delete,
move,
protect,
subpages,
filter log
}}

===Example 4 using Advanced Urls===

<pre>{{Page Actions|
|Delete(redlink{{=}}1)
|move(wpNewTitle{{=}}Example; wpOldTitle{{=}}{{FULLPAGENAMEE}})
}}</pre>
;Produces
{{Page Actions
|Delete(redlink{{=}}1)
|move(wpNewTitle{{=}}Example; wpOldTitle-{{FULLPAGENAMEE}})
}}

==See Also==
*{{T|PageType}}
*{{T|NAMESPACENUMBER}}

<!-- Place template categories here -->
<includeonly>
[[Category:Navigation templates]]<!--
[[Category: Template category 1 ]]
[[Category: Template category 2 ]]-->
</includeonly>
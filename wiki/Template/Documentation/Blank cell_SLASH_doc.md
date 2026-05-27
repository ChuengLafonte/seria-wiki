{{Documentation subpage}}
{{Template shortcut|Bc}}
When a cell is empty, this template should be added if the reason for it being blank is there is no information to be added. If the information is simply missing/needed, this template should not be used.

== Syntax ==
<pre>{{Blank cell
|data-sort-value = (optional) allows you to specify the cell's data type
}}</pre>
'''data-sort-value''' can be useful when wanting to [[Wikipedia:Help:Sorting|sort a table]].

== Example ==
<pre>{| class="wikitable oddrow"
!Col1
!Col2
!Col3
|-
|Normal
|{{blank cell}}
|Normal
|-
|Normal
|Normal
|{{blank cell}}
|-
|Normal
|Normal
|{{blank cell}}
|}</pre>

{| class="wikitable oddrow"
!Col1
!Col2
!Col3
|-
|Normal
|{{blank cell}}
|Normal
|-
|Normal
|Normal
|{{blank cell}}
|-
|Normal
|Normal
|{{blank cell}}
|}

<includeonly>[[Category:Table cell templates]]</includeonly>
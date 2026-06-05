{{Documentation subpage}}{{Lua|Infobox/Mechanic}}
To use this template, add the {{T|Infobox/Minion}} template and fill in the appropriate fields. Fields left blank will not appear in articles. This infobox template uses [[Help:Infobox|Fandom's infobox syntax]].

== Syntax ==
<pre>
{{ Infobox/Minion
 | tab[1-10]      = headers for different tabs (should only really be used if needed on infoboxes with more than 1 tab)
 
 | title           =
 | image           =
 
 | category        =
 | collection      = Any input accepted by {{CollectionLink}}
 | upgrade_with    =
 | collects        =
 
 | super_compactor = Any yes/no value for styling; otherwise uses exact value entered
 | compactor       = Any yes/no value for styling; otherwise uses exact value entered
 | auto_smelter    = Any yes/no value for styling; otherwise uses exact value entered
 
 | ideal_layout    = Use {{Minion ideal layout}}
 | id              = The minion item ID
}}
</pre>
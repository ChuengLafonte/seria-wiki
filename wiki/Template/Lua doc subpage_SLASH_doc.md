{{Documentation subpage}}
{{TextMessageBox|box_color=red|text=Unlike {{T|Documentation subpage}}, this template is used by [[MediaWiki:Scribunto-doc-page-header]], and normally does not need to be added manually.}}

{{T|Lua doc subpage}} is a message box used to show a page is a module documentation subpage.

{{Tc}}

== Syntax ==
{{T|Lua doc subpage|docnotice|}}
* {{Param|override}} - Optional, default "doc". This defines the page ending check. The message box will only show if there is a matching page ending with this parameter. This prevents displaying on transclusion.
* {{Param|docnotice}} - Optional, default "show". If specified other than "show", the main notice will not show.
* {{Param|defaultsort}} - Optional, default PAGENAME. If specified, it changes the [[wp:Template:DEFAULTSORT|sort key]].
* {{Param|inhibit}} - Optional, default nothing. If specified other than nothing, category will not be added.

== See Also ==
{{FeatureSet/Documentations}}

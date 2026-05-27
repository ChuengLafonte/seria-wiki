{{Documentation subpage}}

== Overview ==
{{Lua|Tabview}}

{{T|Tabview}} is used to recreate Tab View on the Project Seria Caveblock Wiki as Fandom might discontinue it. You can read [[Help:Tab view]] for full details.

To enable Tab View, besides JavaScript, "PartialLoadTool" from [[Special:Preferences#mw-prefsection-gadgets|Gadget]] must also be enabled.

With JavaScript and PartialLoadTool enabled:
* For multiple pages, it is a tabber that loads (and transcludes) a page when it is selected. The content will be generated as tabbers that will not be loaded until selected.
* For single page, a "load content" button will be generated for loading its content, UNLESS {{Code|forceTabber}} is set to true.
When disabled or on mobile, the content will be displayed as links.

{{Tc}}

== Syntax ==
Tabview is configured in this order:
<pre>
{{Tabview
|-|PAGENAME|TITLE|CACHE
|-|...
|active=<active>
|button=<button>
|forceTabber=<forceTabber>
|noTabs=<noTabs>
}}
</pre>
* {{S|PAGENAME}} - The link to a page.
* {{S|TITLE}} - The displayed name on the tab. Default {{Code|Tab (n)}}. Optional.
* {{S|CACHE}} - Whether to cache the page content. If a page is showing very frequently updated information, you may want to force the tab to check for new content on each page load. This can be done with a second pipe, followed by the word "false." Optional.

Additionally (these are all optional),
* {{S|active}} determines which tab should be opened first, with 1 being the first tab. Default 1. Optional. Only has effect when there is more than one page of input.
* {{S|button}} will change the button label. Only has effect when there is only one page of input.
* {{S|forceTabber}} will force the output into a tabber. Only used to override the one-page button behaviour.
* {{S|noTabs}} will remove the tab links on the top for selecting pages. Not recommended when having more than 1 page.

Note: When there is only one page of input, {{S|CACHE}} and {{S|active}} does not have any effect when there is only one page of input; {{S|TITLE}} will still show for mobile users but not as a tab name.

== Examples ==
=== Example 1 with custom displayed names ===
<pre>
{{Tabview
|-|Mayor Election/Year 101-120|Year 101-120
|-|Mayor Election/Year 121-140|Year 121-140
}}
</pre>
;Produces
{{Tabview
|-|Mayor Election/Events/Year 101-120|Year 101-120
|-|Mayor Election/Events/Year 121-140|Year 121-140
}}

=== Example 2 with Tab 2 loaded first, and Tab 1 not cached ===
<pre>
{{Tabview
|-|Mayor Election/Events/Year 101-120||false
|-|Mayor Election/Events/Year 121-140
|active=2
}}
</pre>
;Produces
{{Tabview
|-|Mayor Election/Events/Year 101-120||false
|-|Mayor Election/Events/Year 121-140
|active=2
}}

=== Example 3 with Single Page ===
<pre>
{{Tabview
|-|Mayor Election/Events/Year 101-120
}}
</pre>
;Produces
{{Tabview
|-|Mayor Election/Events/Year 101-120
}}

=== Example 4 with Nested Tabview ===
<pre>
{{Tabview
|-|/Tab 1
|-|/Tab 2
}}
</pre>
;Produces
{{Tabview
|-|<includeonly>/doc</includeonly>/Tab 1
|-|<includeonly>/doc</includeonly>/Tab 2
}}
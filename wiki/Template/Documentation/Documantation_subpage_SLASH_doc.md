{{Documentation subpage}}
{{T|Documentation subpage}} Is a template used to mark documentation subpages.
== Usage ==
{{Ts|Doc sp}}
: {{t|Documentation subpage}}
: or
: {{t|Documentation subpage |&#91;&#91;Page where the documentation [[Wikipedia:Transclusion|transcluded]]&#93;&#93;}}

===Text customization===
The parameters <code>|text1=</code> and/or <code>|text2=</code> can be used to set the text of, respectively, the template's first and second lines. If ''text1'' is set but not ''text2'', both lines' text will derive from ''text1'':

;With ''text1'' and ''text2'':
<code><nowiki>{{Documentation subpage |text1='''''text1 appears here''''' |text2='''''text2 appears here'''''}}</nowiki></code>
{{Documentation subpage |[''page''] |text1='''''text1 appears here''''' |text2='''''text2 appears here''''' |override={{lc:{{SUBPAGENAME}}<!-- Hack to allow example to appear, even when viewed from [[Template:Documentation subpage]] -->}}}}

;With ''text2'' only:
<code><nowiki>{{Documentation subpage |text2='''''text2 appears here'''''}}</nowiki></code>
{{Documentation subpage |[''page''] |text2='''''text2 appears here''''' |override={{lc:{{SUBPAGENAME}}<!-- Hack to allow example to appear, even when viewed from [[Template:Documentation subpage]] -->}}}}

;With ''text1'' only:
<code><nowiki>{{Documentation subpage |text1='''''text1 appears here'''''}}</nowiki></code>
{{Documentation subpage |[''page''] |text1='''''text1 appears here''''' |override={{lc:{{SUBPAGENAME}}<!-- Hack to allow example to appear, even when viewed from [[Template:Documentation subpage]] -->}}}}

===Other parameters===
<code>|inhibit=yes</code> will prevent this template from generating any categories. (By default, "''Namespace'' documentation pages" (usually [[:Category:Template documentation]]) is added, or [[:Category:Documentation subpages without corresponding pages]] if the main page doesn't exist.)

== Display ==
This template should normally be placed at the top of /doc pages. It changes output depending on where it is viewed:
* On a /doc page, it displays a box explaining template documentation and links to the template page.
* On other pages&nbsp;– i.e. pages transcluding the /doc page&nbsp;– the template will not show. The template page itself (which contains {{t|Documentation}}) will automatically note that the documentation is [[Wikipedia:Transclusion|transcluded]] from a subpage.

== Functions ==
In addition to its message, the template adds pages to [[:Category:Template documentation]], [[:Category:Project documentation]], or similar (named after the subject space), but only for documentation pages in namespaces with the subpage feature. It defaults the [[metawikimedia:Help:Categories#Sort order|sort key]] to the page name without namespace: Template:Foo, for example, would be sorted as "Foo", i.e. under "F".

== See Also ==
{{FeatureSet/Documentations}}

<includeonly>
[[Category:Message Boxes]]
</includeonly>

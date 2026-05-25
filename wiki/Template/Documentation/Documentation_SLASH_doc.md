{{Documentation subpage}}
:''Also see {{T|Documentation subpage}}''
{{Lua|Documentation}}
This template is used to insert descriptions on template pages. This Template also has tools for users to quickly drafts and documentation subpages, and provides automatic notices for the template's state (ex: protection levels). 

==Syntax==
{{Ts|Doc}}
:Type <code><nowiki><noinclude></nowiki><nowiki>{{documentation}}</nowiki><nowiki></noinclude></nowiki></code> at the end of the template page.

Under '''special''' cases when the documentation for a template is not located at Template:pagename/doc (such as with Navbox, which is used in other templates and automatically inserts Template:Navbox/doc onto any template that uses a navbox), you can tell it to display a different page by giving it a parameter such as:
:<code><nowiki><noinclude>{{Documentation|Template:Navbox/doc}}</noinclude></nowiki></code> at the end of the template page.

==General usage==
===On the Template page===
<pre>
Template code
<includeonly>Any categories to be inserted into articles by the template</includeonly>
<noinclude>{{documentation}}</noinclude>
</pre>

===On the Template/doc page===
:'' Main Article: [[Project Seria Wiki:Style Manual/Template Documentation|Style Manual / Template Documentation]]''
<pre>
{{Documentation subpage}}
What this template is meant to do

==Syntax==
{{templatename
|field1 = 
|field2 = 
}}

==Example==
&lt;pre>{{templatename|foo}}&lt;/pre>
{{templatename|foo}}

<includeonly>Any categories for the template itself</includeonly>
</pre>

Use any or all of the above description/syntax/sample output sections. You may also want to add "see also" or further usage information sections.

== See Also ==
{{FeatureSet/Documentations}}

<includeonly>[[Category:General wiki templates]]</includeonly>

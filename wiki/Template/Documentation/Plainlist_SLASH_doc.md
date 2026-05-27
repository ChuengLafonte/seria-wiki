{{Documentation subpage}}
This template provides a [[Wikipedia:Web Content Accessibility Guidelines|WCAG]]/ISO-standards-compliant accessible alternative to <code><nowiki><br /></nowiki></code> separated lists, per [[Wikipedia:WP:UBLIST]] and [[Wikipedia:WP:PLIST]].

Template taken from [[Wikipedia:Template:Plainlist]].

NOTE: Since custom CSS does not work on mobile, lists using this template will appear as a bulleted list on mobile devices.

==Usage==
{{Ts|PL|PList}}{{t|plainlist}} starts a plain (i.e. unbulleted) list, such as:

{{plainlist|
* [[horse]]
* [[cow]]
* [[sheep]]
* [[pig]]
}}

It uses proper HTML list markup, which is more standards-compliant and more accessible than separating list items with <code><nowiki><br /></nowiki></code>. Detailed reasons for using this template can be found at [[Wikipedia:WP:UBLIST]].

==Example==
<pre>
{{plainlist|
* [[horse]]
* [[cow]]
* [[sheep]]
* [[pig]]
}}
</pre>
{{plainlist|
* [[horse]]
* [[cow]]
* [[sheep]]
* [[pig]]
}}

==Technical details==
{{t|Plainlist}} works by constructing a [[Wikipedia:span and div|div]] with the [[Wikipedia:Cascading Style Sheets|CSS]] class "plainlist" which has the following style (see [[MediaWiki:Common.css]]):
<syntaxhighlight lang="css">
.plainlist ul {
    line-height: inherit;
    list-style: none none;
    margin: 0;
}
.plainlist ul li {
    margin-bottom: 0;
}
</syntaxhighlight>

<includeonly>[[Category:General wiki templates]]</includeonly>
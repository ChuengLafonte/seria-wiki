{{Doc sp}}
==Overview==
This template is used to detect the namespace and return a string based off the namespace.
==Syntax==
{{T|PageType|namespace|lowercase}}
*{{S|namespace}} - The namespace of the page. If left unspecified, the default is the parent page's namespace.
*{{S|lowercase}} or {{S|l}} - (Optional) converts the returned string to lowercase.
==Examples==
<pre>{{PageType}}</pre>
Produces...<br>
{{PageType}}
<pre>{{PageType|Template|lowercase=true}}</pre>
Produces...<br>
{{PageType|Template|lowercase=true}}
<includeonly>[[Category:General wiki templates]]</includeonly>
{{Documentation subpage}}
==Overview==
{{T|NAMESPACENUMBER}} is a template used to display the pages/inputs namespace number. It is used in place of the magic word {{Code|{<!---->{NAMESPACENUMBER}<!---->}<!---->}} due to the magic word not working on the version of mediawiki this wiki uses. This template functions very similar to the actual magic word.
{{Tc}}
==Syntax==
{{Ts|NSN}}{{T|NAMESPACENUMBER|namespace}}
*{{S|namespace}} - The namespace. This is case insensitive. If the input is invalid, it will defualt to 0 (main). If not specified, it will default to the current page's namespace.

==Examples==
===Example 1 using The current namespace===
<pre>{{NAMESPACENUMBER}}</pre>
;Produces
{{NAMESPACENUMBER}}
===Example 2 using inputs===
<pre>{{NAMESPACENUMBER|module}}</pre>
;Produces
{{NAMESPACENUMBER|module}}
==See Also==
*{{T|PageType}}
<includeonly>{{#vardefine:replpttn|[%s'",;:.]}}<!--
-->{{#vardefine:csHeadAttr|class="mw-collapsible mw-{{#switch:{{lc:{{{collapsible}}}}}<!--
-->|un|uncollapsed|notcollapsed=uncollapsed<!--
-->|#default=collapsed<!--
-->}} textsection {{{class|}}}" {{#if:{{{id|}}}|id="mw-customcollapsible-{{Replace|{{lc:{{{id|}}}}}|{{#var:replpttn}}|-}}"}}<!--
-->}}<!--
-->{{#vardefine:csHead|<div {{#var:csHeadAttr}}>}}<!--
-->{{#vardefine:csBody|{{{text|{{{1|}}}}}}}}<!--
-->{{#vardefine:csEnd|</div>}}<!--
-->{{#switch:{{{mode|}}}
|attr={{#var:csHeadAttr}}
|begin={{#var:csHead}}
|end={{#var:csEnd}}
|#default={{#var:csHead}}
{{#var:csBody}}
{{#var:csEnd}}
}}[[Category:Pages with Collapsible Section]]</includeonly><noinclude>
{{Documentation}}[[Category:Templates]]
</noinclude>

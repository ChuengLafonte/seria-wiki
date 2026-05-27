<includeonly>{{#vardefine:btntype|{{#switch:{{{type|}}}
|wds=wds
|<!--default-->default
}}}}{{#vardefine:btnclass|<!--
--> {{#switch:{{#var:btntype}}|wds=wds-button|default=button}}<!--
--> {{#if:{{{class|}}}|{{{class}}}}}<!--
--> {{#if:{{{isfill|}}}|{{#ifeq:{{#var:btntype}}|wds|wds-is-full-width}}{{#ifeq:{{#var:btntype}}|default|full-width-button}}}}<!--
--> {{#if:{{{issecondary|}}}|{{#ifeq:{{#var:btntype}}|wds|wds-is-secondary}}{{#ifeq:{{#var:btntype}}|default|secondary}}}}<!--
--> {{#if:{{{istext|}}}|{{#ifeq:{{#var:btntype}}|wds|wds-is-text}}}}<!--
--> {{#if:{{{isactive|}}}|{{#ifeq:{{#var:btntype}}|wds|wds-is-active}}}}<!--
--> {{#if:{{{isforward|}}}|{{#ifeq:{{#var:btntype}}|default|forward-button}}}}<!--
-->}}<!--

--><span {{#if:{{{id|}}}|id="{{{id|}}}"}} class="{{#var:btnclass}}" style="{{{style|}}}">{{{text|{{{1|}}}}}}</span><!--
--></includeonly><noinclude>
{{Documentation}}
</noinclude>
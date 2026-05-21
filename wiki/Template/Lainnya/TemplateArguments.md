<includeonly>
<!-- The template example -->
<div style="display: block; line-height: 1.3em; margin: 1em 0px; color: #000; background-color: #f8f9fa; border: 1px solid #eaecf0; padding: 1em; font-family: monospace,monospace;">
{{{{{templateName|{{BASEPAGENAME}}}}} <br><!--
-->{{#vardefine: reqNote | false}}<!--
-->{{#vardefine: i | 1 }}<!--
-->{{#while: <!-- Loops through all values of arg# -->
	| {{{arg{{#var: i }}|}}}
	| <nowiki />
	{{#if: {{{replace{{#var: i }}|}}} 
		| {{!}} {{{replace{{#var: i }}}}} {{#ifeq:{{{req{{#var: i }}}}}|true|<nowiki> *</nowiki>}}<br>
		| {{!}} {{{arg{{#var: i }}}}} =  {{#ifeq:{{{req{{#var: i }}}}}|true|<nowiki> *</nowiki>}}<br>
	}}
	{{#vardefine: i | {{#expr: {{#var: i }} + 1 }}}} {{#ifeq: {{{req{{#var: i}}}}} | true | {{#vardefine: reqNote | true }}}}
}}
}}
</div>
{{#ifeq:{{#var: reqNote}} | true | '''Note:''' The <code>*</code> symbol denotes required arguments <br />}}<!--
-->{{#vardefine: i | 1 }}<!--
-->{{#while: <!-- Loops through all values of note# -->
	| {{{note{{#var: i }}|}}}
	| <nowiki />
	'''Note:''' {{{note{{#var: i }}}}} <br />
	{{#vardefine: i | {{#expr: {{#var: i }} + 1 }}}}
}}


<!-- The argument breakdown table -->
{| class="wikitable"
! style="width: 20%; min-width:150px;" | Argument
! style="width: 50%" min-width:400px;| Description
! style="width: 30%" min-width:250px;| Default Value
|-
{{#vardefine: i | 1 }} <!-- Variable used for while loop 
-->{{#while: <!-- Loops through all values of arg# -->
	| {{{arg{{#var: i }}|}}}
	| <nowiki />
	{{!}} <code>{{{arg{{#var: i }}|}}}{{#ifeq:{{{req{{#var: i }}}}}|true|<nowiki> *</nowiki>}}</code>
	{{!}} {{{desc{{#var: i }}|}}}
	{{!}} {{{def{{#var: i }}|}}}
	{{!}}- 
	{{#vardefine: i | {{#expr: {{#var: i }} + 1 }}}}
}}
|}</includeonly>
<noinclude>{{Doc}}</noinclude>
<includeonly>
<div class="nomobile">
<table style="{{{style|}}}" class="plainlinks ambox {{#ifeq:{{{format|}}}|tiny|ambox-tiny}} {{#switch:{{{border|}}}
  | red      = ambox-red
  | orange   = ambox-orange
  | yellow   = ambox-yellow
  | purple   = ambox-purple
  | blue     = ambox-blue
  | green    = ambox-green
  | gray     = ambox-gray
  | #default = ambox-green
}} {{{class|}}}">
<tr>
<td class="ambox-image" style="/* HACK */ padding: 10px 0;>{{{image|[[File:{{{icon|Information.png{{!}}48px}}}|{{#ifeq:{{{format|}}}|tiny|x20px}}|alt=]]}}}</td>
<td class="ambox-text">{{{type|}}}
{{#if:{{{info|}}}|{{#ifeq:{{{format|}}}|tiny||<div class="amsmalltext">
{{{info}}}
</div>}}}}</td></tr></table>
</div>
<div class="mobileonly" style="text-align:center; font-size: 16px;">
<b>{{{type|}}}</b><br>{{{info|}}}
</div></includeonly><noinclude>{{doc}}</noinclude>
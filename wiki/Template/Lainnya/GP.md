{{#vardefine:wiki|{{#explode:{{{1}}}|:|0}}}}<!--
-->{{#vardefine:page|{{#replace:{{#explode:{{{1}}}|:|1}}| |_}}}}<!--
--><span class="plainlinks">{{#if:{{{2|}}}<!--
-->|[https://{{#var:wiki}}.gamepedia.com/{{#var:page}} {{{2}}}]<!--
-->|[https://{{#var:wiki}}.gamepedia.com/{{#var:page}} gamepedia:{{#var:wiki}}{{#if:{{#var:page}}|:}}{{#replace:{{#var:page}}|_| }}]<!--
-->}}</span><!--

--><noinclude>{{Documentation}}</noinclude>
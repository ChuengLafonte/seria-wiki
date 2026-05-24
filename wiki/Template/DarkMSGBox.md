<includeonly><div class="darkmsgbox nomobile {{#if:{{{box_color|}}}|boxcol-{{{box_color|}}}}} {{{box_class|}}}" style="{{#if:{{{box_style|}}}|{{Replace|{{{box_style}}}|[\n\t]}}}}">
{{#if:{{{image|}}}|
<div class="darkmsgbox-image darkmsgbox-image-left" style="{{#if:{{{image_style|}}}|{{Replace|{{{image_style}}}|[\n\t]}}}}"><!--
--><div class="content">{{{image}}}</div></div>
}}
<div class="darkmsgbox-text" style="{{#if:{{{text_style|}}}|{{Replace|{{{text_style}}}|[\n\t]}}}}"><!--
--><div class="content">{{{text|}}}{{#if:{{{note|}}}|<br><small><b>Note: </b>{{{note}}}</small>}}</div></div>
{{#if:{{{image_right|}}}|
<div class="darkmsgbox-image darkmsgbox-image-right" style="{{#if:{{{image_right_style|}}}|{{Replace|{{{image_right_style}}}|[\n\t]}}}}"><!--
--><div class="content">{{{image_right}}}</div></div>
}}
{{#if:{{{bottom_text|}}}|
<div class="darkmsgbox-bottom" style="{{#if:{{{bottom_style|}}}|{{Replace|{{{bottom_style}}}|[\n\t]}}}}"><!--
--><div class="content">{{{bottom_text}}}</div></div>
}}
</div></includeonly><!--

-->{{#if:{{{{category|}}}|{{#ifeq:{{ns:10}}|{{NAMESPACE}}||{{#if:{{{category|}}}|[[Category:{{{category}}}]]}}}}}}<!--

-->{{#if:{{{template_cat|}}}|{{#ifeq:{{ns:10}}|{{NAMESPACE}}|<!--
-->{{Replace|{{{template_cat|}}}|([%w%s%(%)%$%^%@%;%:%\%/]+)%s*[,;]?%s*|<!--
--><includeonly><noinclude></includeonly>[[Category:%1]]<includeonly></noinclude></includeonly>}}}}}}<!--

-->{{#ifeq:{{ns:10}}|{{NAMESPACE}}|{{IfString|{{PAGENAME}}|/||[[Category:Message Boxes]]}}|}}<!--
--><noinclude>{{Documentation}}</noinclude><noinclude>
[[Category:Templates]]</noinclude>

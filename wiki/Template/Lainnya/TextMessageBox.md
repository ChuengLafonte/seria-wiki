<includeonly><div class="messagebox{{#ifeq:{{yesno|{{{inline|}}}|yes=yes}}|yes|-inline|}}{{#ifeq:{{yesno|{{{boxed|}}}|yes=yes}}|yes|-boxed|}} {{#if:{{{box_color|}}}|boxcol-{{{box_color|}}}|}} {{{box_class|}}}" style="{{#if:{{{box_style|}}}|{{Replace|{{{box_style}}}|[\n\t]}}}}">
<div class="messagebox-main">
{{#if: {{{image|}}}
|<div class="messagebox-image nomobile {{{image_class|}}}" style="{{#if:{{{image_style|}}}|{{Replace|{{{image_style}}}|[\n\t]}}}}">
{{{image}}}
</div>
}}
{{#if: {{{text|}}}
|<div class="messagebox-text" style="{{#if:{{{text_style|}}}|{{Replace|{{{text_style}}}|[\n\t]}}}}">
{{{text}}}
</div>
}}
</div><!-- end div.messagebox-main -->
<div class="messagebox-aside">
{{#if: {{{rtext|}}}
|<div class="messagebox-rtext" style="{{#if:{{{rtext_style|}}}|{{Replace|{{{rtext_style}}}|[\n\t]}}}}">
{{{rtext}}}
</div>
}}
</div><!-- end div.messagebox-aside -->
</div><!-- end div.messagebox -->
</includeonly><!--

-->{{#if:{{{{category|}}}|{{#ifeq:{{ns:10}}|{{NAMESPACE}}||{{#if:{{{category|}}}|[[Category:{{{category}}}]]}}}}}}<!--

-->{{#if:{{{template_cat|}}}|{{#ifeq:{{ns:10}}|{{NAMESPACE}}|<!--
-->{{Replace|{{{template_cat|}}}|([%w%s%(%)%$%^%@%;%:%\%/]+)%s*[,;]?%s*|<!--
--><includeonly><noinclude></includeonly>[[Category:%1]]<includeonly></noinclude></includeonly>}}}}}}<!--

-->{{#ifeq:{{ns:10}}|{{NAMESPACE}}|{{IfString|{{PAGENAME}}|/||[[Category:Message Boxes]]}}|}}<!--
--><noinclude>{{Documentation}}
[[Category:Templates]]</noinclude>
<includeonly>{{#vardefine:mainBoxClass|textsection{{#ifeq:{{yesno|{{{inline|}}}|yes=yes}}|yes|-inline|}}{{#ifeq:{{yesno|{{{boxed|}}}|yes=yes}}|yes|-boxed|}}}}<!--
-->{{#vardefine:colorClass|{{#if:{{{box_color|}}}|boxcol-{{{box_color|}}}|}}}}<!--
--><div class="{{#var:mainBoxClass}} {{#var:colorClass}} {{{box_class|}}}" style="{{#if:{{{box_style|}}}|{{Replace|{{{box_style}}}|[\n\t]}}}}">
{{{text|}}}
</div><!-- end div.messagebox -->
</includeonly><!--

-->{{#if:{{{{category|}}}|{{#ifeq:{{ns:10}}|{{NAMESPACE}}||{{#if:{{{category|}}}|[[Category:{{{category}}}]]}}}}}}<!--

-->{{#if:{{{template_cat|}}}|{{#ifeq:{{ns:10}}|{{NAMESPACE}}|<!--
-->{{Replace|{{{template_cat|}}}|([%w%s%(%)%$%^%@%;%:%\%/]+)%s*[,;]?%s*|<!--
--><includeonly><noinclude></includeonly>[[Category:%1]]<includeonly></noinclude></includeonly>}}}}}}<!--

--><noinclude>{{Documentation}}[[Category:Templates For Templates]]</noinclude><noinclude>
[[Category:Templates]]</noinclude>
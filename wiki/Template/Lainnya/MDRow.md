<!-- if the ingredient is in the table
        if it's guaranteed, make it a table with "Guaranteed Drop" appended on top
        else, display the ingredient regularly using ItemData/ingredient/display 
     else, mark it with an error category
--><includeonly>{{#if:{{QueryIngredients|Ingredients.name LIKE "{{{item}}}"}}|{{#ifeq:{{{is_guaranteed|0}}}|1|
<div style="display:inline-block;vertical-align:top">
{{{!}}
{{!}} align='center' style="position:relative; top: 12px;" {{!}} '''Guaranteed Drop'''
{{!-}}
{{!}} {{QueryIngredients|Ingredients.name LIKE "{{{item}}}"}}
{{!}}}
</div>|{{QueryIngredients|Ingredients.name LIKE "{{{item}}}"}}}}|The ingredient [[{{{item|}}}]] does not have a page on the wiki yet. You can help by [[{{{item|}}}|creating]] it.<br>[[Category:Pages with MDRow errors]]}}<!--

-->{{#if:{{NAMESPACE}}||
{{#cargo_store:_table=MobDrops
| mob={{PAGENAME}}
| item={{{item|}}}
| is_guaranteed={{{is_guaranteed|0}}}
}}<!-- end if namespace -->}}</includeonly><noinclude>

{{#cargo_declare:_table=MobDrops
| mob=String
| item=String
| is_guaranteed=Boolean
}}

For documentation, see [[Template:MobDrops]].
[[Category:Cargo Templates]]
</noinclude>
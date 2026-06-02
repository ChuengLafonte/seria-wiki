{{Documentation subpage}}
{{Lua|Crafting/UI}}
{{T|Crafting Table}} is used to create an interface that looks similar to the Crafting Table's. {{T|Crafting Grid}} is used to display only the recipe grid, not the whole UI.

See [[Template:Inventory slot]] for basic usage, this documentation page will cover additional or different functions.

==Syntax==
Note: All parameters are ''entirely optional''.<br>
{{T|Crafting Grid
|...
|qrs{{=}}recipe declaration
|A1-C3{{=}}recipe declaration for each slot
|ver{{=}}recipe locator version for recipe declarations using qrs or A1-C3
|Output{{=}}output item ("crafted item")
|bazaar{{=}}to display bazaar price
}}<br>
{{T|Crafting Table
|...
|qrs{{=}}recipe declaration using Quick Recipe Syntax
|A1-C3{{=}}recipe declaration for each slot
|ver{{=}}Recipe Syntax Version for recipe declarations using qrs or A1-C3
|Output{{=}}output item ("crafted item")
|Ilink{{=}}input item link
|Olink{{=}}output item link
|bazaar{{=}}to display bazaar price
}}

Recipe Declaration. Usually only one method is used, unless in situations of overridding.
*{{S|...}} - Recipe(s) from database to display. See next section for details.
** To make a single recipe, simply call {{Code|{{((}}Crafting Table/Grid{{!}}Recipe Required{{))}}}} Example: <code>{{Code|{{((}}Crafting Table/Grid{{!}}Enchanted Cobblestone{{))}}}}</code>
** To make an animated table/grid using more than one database recipes, either [1. pass as a single string with each item separated with * (similar to a wikitext unordered list)] or [2. pass as separate positional arguments]. Example: <code>{{Code|{{((}}Crafting Table/Grid{{!}}Enchanted Grilled Pork|Enchanted Pork{{))}}}}</code> and <code>{{Code|{{((}}Crafting Table/Grid{{!}}*Enchanted Grilled Pork *Enchanted Pork{{))}}}}</code> are equivallent
*{{S|qrs}} - Items for each Crafting Table/Grid slot. Can be used to override any slots declared in {{S|...}}. See next section for details.
*{{S|A1-C3}} - Items for each Crafting Table/Grid slot. Can be any item. Can be used to override any slots declared in {{S|...}} and {{S|qrs}}. See next section for details.

Recipe Declaration Config
*{{S|ver}} - Version number for syntax. Affects how A1-C3 is mapped. Default to 1. See next section for details.

Other Parameters
*{{S|Output}} - The item crafted. Can be any item.
** For {{T|Crafting Table}}, when using a recipe existing in database, the Output is automatically assigned a value. Such will be displayed as a slot unless overridden.
** For {{T|Crafting Grid}}, the text passed to Output will be displayed on top of the grid.
*{{S|bazaar}} - Whether to display bazaar prices of the recipe. Default no.

Exclusive for {{T|Crafting Table}}
*{{S|Ilink}} - A link for input items. Set this to 'none' to disable linking.
*{{S|Olink}} - A link for output items. Set this to 'none' to disable linking.

== Database, QRS and RSV ==
=== Database ===
To set recipes to database, use [[Module:Crafting/Data]] with [[Module:Crafting/Templates]]. The recipes must be declared in RSV ver=2.

=== QRS ===
The '''Quick Recipe Syntax (QRS)''' is used as follows:<br>
<code><span style="color:green">Slot declaration</span> "<span style="color:magenta">Recipe item</span>" <span style="color:green">Slot declaration 2</span> "<span style="color:magenta">Slot value 2</span>" ...</code>
* <code><span style="color:green">Slot declaration</span></code>: (The list is unordered)
** ex1: {{Code|A123B13C123}} gives <code>{ 'A1', 'A2', 'A3', 'B1', 'B3', 'C1', 'C2', 'C3' }</code>
** ex2: {{Code|A*B13C*}} also gives <code>{ 'A1', 'A2', 'A3', 'B1', 'B3', 'C1', 'C2', 'C3' }</code>
** ex3: {{Code|*13A2C2}} gives <code>{ 'A1', 'B1', 'C1', 'A3', 'B3', 'C3', 'A2', 'C2' }</code> (unordered; result is equivallent to ex1 and ex2)
** ex4: {{Code|**}} gives all nine slots <code>{ 'A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3' }</code>
* Example: The recipe for Aspect of the End is {{Code|A2B2 "Enchanted Eye of Ender,16" C2 "Enchanted Diamond"}} in RSV ver=2, and {{Code|B12 "Enchanted Eye of Ender,16" B3 "Enchanted Diamond"}} in RSV ver=1

Animated slots:<br>
* Method 1: <code><span style="color:green">Frame 1 Slot declaration 1</span> "<span style="color:magenta">Frame 1 Slot value 1</span>" <span style="color:green">Frame 1 Slot declaration 2</span> "<span style="color:magenta">Frame 1 Slot value 2</span>" ... // <span style="color:green">Frame 2 Slot declaration 1</span> "<span style="color:magenta">Frame 2 Slot value 1</span>" ... // ...</code>
* Do not use the traditional way of separating each recipe item using ';' separators! It will cause problems when making animated recipes.

=== RSV ===
The '''Recipe Syntax Version''' is the version in which the slot positions are named. Since most of the recipes are declared in RSV ver=1, it is the default. When using ver=2, unless declaring through Crafting/Data (which is forced to use ver=2), one must specify explicitly {{Code|{{!}}ver{{=}}2}}.
{| class="wikitable" style="text-align: center;"
!
! colspan = 3 | RSV ver=1 <small>("Older" Version)</small>
!
! colspan = 3 | RSV ver=2 <small>("Newer" Version)</small>
|-
! !! A !! B !! C !! !! 1 !! 2 !! 3
|-
! 1
| A1 || B1 || C1
! A
| A1 || A2 || A3
|-
! 2
| A2 || B2 || C2
! B
| B1 || B2 || B3
|-
! 3
| A3 || B3 || C3
! C
| C1 || C2 || C3
|}
If you know linear algebra, you should be able to immediately tell that ver=2 can be obtained by transposing the matrix ver=1, and vice versa.<br>
When using RSV ver=2 (new version), think horizontally. (A, B, C represents the rows; 1, 2, 3 represents the columns.) RSV ver=2 is now the recommended syntax to use as it should be more intuitive.{{Confirm}}<br>
When using RSV ver=1 (traditional version), think vertically. (A, B, C represents the columns; 1, 2, 3 represents the rows.)

== Example ==
Note: Only this example uses crafting grid. All other examples also works with crafting grid.
Using A1-C3 slot declaration with RVS ver=1:
<pre>
{{Crafting Grid
|A1=  |B1= Move Jerry |C1= 
|A2=  |B2= Move Jerry |C2= 
|A3=  |B3= Stick      |C3= 
}}
</pre>
;Produces:
{{Crafting Grid
|A1=  |B1= Move Jerry |C1= 
|A2=  |B2= Move Jerry |C2= 
|A3=  |B3= Stick      |C3= 
}}
Using A1-C3 slot declaration with RVS ver=2 with "Output":
<pre>
{{Crafting Grid|ver=2
|A1=  |A2= Move Jerry |A3= 
|B1=  |B2= Move Jerry |B3= 
|C1=  |C2= Stick      |C3= 
|Output= Aspect of the Jerry
}}
</pre>
;Produces:
{{Crafting Grid|ver=2
|A1=  |A2= Move Jerry |A3= 
|B1=  |B2= Move Jerry |B3= 
|C1=  |C2= Stick      |C3= 
|Output= Aspect of the Jerry
}}
Using QRS recipe declaration with RVS ver=2:
<pre>
{{Crafting Grid|qrs=A2B2 "Move Jerry" C2 "Stick"|ver=2}}
</pre>
;Produces:
{{Crafting Grid|qrs=A2B2 "Move Jerry" C2 "Stick"|ver=2}}

===Example using database recipes===
<pre>
{{Crafting Table|Enchanted Cooked Porkchop}}
</pre>
;Produces:
{{Crafting Table|Enchanted Cooked Porkchop}}

Multiple items, but also overridding the output:
<pre>
{{Crafting Table|
*Redstone Minion IV
*Cobblestone Minion XI
*Flower Minion VII
|Output=Barrier;Barrier;Barrier
}}
</pre>
;Produces:
{{Crafting Table|
*Redstone Minion IV
*Cobblestone Minion XI
*Flower Minion VII
|Output=Barrier;Barrier;Barrier
}}

===Example using stacks===
Many recipes in skyblock require stacks of objects. In these case use a comma followed by the number. This example also shows how to disable links by modifying {{S|Ilink}} and {{S|Olink}}.

Using A1-C3 slot declaration with RVS ver=1:
<pre>{{Crafting Table
|A1=                      |B1= Enchanted Diamond,32 |C1= 
|A2= Enchanted Diamond,32 |B2= Enchanted Diamond,32 |C2= Enchanted Diamond,32
|A3=                      |B3= Enchanted Diamond,32 |C3= 
|Output= Enchanted Diamond Block
|Ilink=none
|Olink=none
}}</pre>
;Produces:
{{Crafting Table
|A1=                      |B1= Enchanted Diamond,32 |C1= 
|A2= Enchanted Diamond,32 |B2= Enchanted Diamond,32 |C2= Enchanted Diamond,32
|A3=                      |B3= Enchanted Diamond,32 |C3= 
|Output= Enchanted Diamond Block
|Ilink=none
|Olink=none
}}

Using QRS slot declaration with RVS ver=1:
<pre>{{Crafting Table|qrs=A2B*C2 "Enchanted Diamond, 32"|Output=Enchanted Diamond Block}}</pre>
;Produces:
{{Crafting Table|qrs=A2B*C2 "Enchanted Diamond, 32"|Output=Enchanted Diamond Block}}

=== Animated ===
To make the slots animate, you make a list of blocks and objects you want to show, separated by semi-colons.

Using A1-C3 with RVS ver=1:
<pre style="max-width: 616px">{{Crafting Table
|A1= ; Lapis Lazuli |B1=                   ; Lapis Lazuli |C1= ; Lapis Lazuli
|A2= ; Lapis Lazuli |B2= Lapis Lazuli Block; Lapis Lazuli |C2= ; Lapis Lazuli
|A3= ; Lapis Lazuli |B3=                   ; Lapis Lazuli |C3= ; Lapis Lazuli
|Output= Lapis Lazuli,9; Lapis Lazuli Block
}}</pre>
;Produces:
{{Crafting Table
|A1= ; Lapis Lazuli |B1=                   ; Lapis Lazuli |C1= ; Lapis Lazuli
|A2= ; Lapis Lazuli |B2= Lapis Lazuli Block; Lapis Lazuli |C2= ; Lapis Lazuli
|A3= ; Lapis Lazuli |B3=                   ; Lapis Lazuli |C3= ; Lapis Lazuli
|Output= Lapis Lazuli,9; Lapis Lazuli Block
}}

Another example, using QRS with RVS ver=1:
<pre style="max-width: 602px">{{Crafting Table
|qrs= ** "Iron Ingot" // ** "Gold Ingot" // ** "Lapis Lazuli"
|Output= Block of Iron; Block of Gold; Lapis Lazuli Block
}}</pre>
;Produces:
{{Crafting Table
|qrs= ** "Iron Ingot" // ** "Gold Ingot" // ** "Lapis Lazuli"
|Output= Block of Iron; Block of Gold; Lapis Lazuli Block
}}

==Links==
Taken from / inspired by https://minecraft.gamepedia.com/Template:Crafting_Table

== See Also ==
{{FeatureSet/UI}}

<includeonly>
[[Category:Inventory templates]]
</includeonly>
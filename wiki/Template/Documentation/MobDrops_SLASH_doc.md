{{doc/start}}

This template creates a table for the item drops of a mob. Can also be used without naming any items. When called without any items, the template will state the mob has no ingredient drops and categorize it under [[:Category:Has no ingredient drops]].
== Usage == 

<pre>
{{MobDrops
|{{MDRow|item= |is_guaranteed= }}
|{{MDRow|item= |is_guaranteed= }}
|{{MDRow|item= |is_guaranteed= }}
...
}}
</pre> 

Each parameter should call [[Template:MDRow]] and provide the name of the item and whether it is guaranteed.
The title of the table will always be the page name.
* <code>item</code> - the name of the item the mob can drop
* <code>is_guaranteed</code> - 0 or 1: whether the mob is guaranteed to drop this item
== Examples == 
{| style="background-color: #E6EFF4; border: 1px solid #BBC2C6; padding: 10px"
!Example !!Result
|-
| style="padding:0 15px; border-right: 1px solid #BBC2C6" |<pre>{{MobDrops
  |{{MDRow|item=Rotten Flesh|is_guaranteed=0}}
  |{{MDRow|item=Sturdy Flesh|is_guaranteed=0}}
}}</pre>
| style="padding: 0 15px" | {{MobDrops
  |{{MDRow|item=Rotten Flesh|is_guaranteed=0}}
  |{{MDRow|item=Sturdy Flesh|is_guaranteed=0}}
}}
|-
| style="padding:0 15px; border-right: 1px solid #BBC2C6" | <pre><nowiki>{{MobDrops}}</nowiki></pre>
| style="padding:0 15px" |{{MobDrops}}
|-
| style="padding:0 15px; border-right: 1px solid #BBC2C6" | <pre>{{MobDrops|mob = Nesting Spider}}
|{{MDRow|item=Forest Web|is_guaranteed=0}}
|{{MDRow|item=Spider Fang|is_guaranteed=0}}
|{{MDRow|item=Poisonous Spider Eye|is_guaranteed=0}}
|{{MDRow|item=Lucky Spider Egg|is_guaranteed=0}}
|{{MDRow|item=Luxurious Silk|is_guaranteed=0}}
}}</pre>
| style="padding: 0 15px" |{{MobDrops
|{{MDRow|item=Forest Web|is_guaranteed=0}}
|{{MDRow|item=Spider Fang|is_guaranteed=0}}
|{{MDRow|item=Poisonous Spider Eye|is_guaranteed=0}}
|{{MDRow|item=Lucky Spider Egg|is_guaranteed=0}}
|{{MDRow|item=Luxurious Silk|is_guaranteed=0}}
|mob = Forest Spider
}}
|}
{{doc/end}}
<includeonly>
[[Category:Table templates]][[Category:Cargo Templates]]
</includeonly>
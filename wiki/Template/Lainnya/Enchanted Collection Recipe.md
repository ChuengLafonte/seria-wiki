<includeonly>{{#vardefine:input_goto
|{{#if:{{{input_goto|}}}
|goto-{{Replace|{{{input_goto|}}}|goto%-}}}}}}<!--
-->{{#vardefine:item|{{{Input|{{{1|{{ROOTPAGENAME}}}}}}}}, 32}}<!--
-->{{#vardefine:shapeless|{{Yesno|{{{shapeless|}}}|blank=|def=|no=|yes=yes}}}}<!--
-->{{#vardefine:output|{{Replace|{{{1|{{{Output|{{ROOTPAGENAME}}}}}}}}|%s*[,;]%s*(.+)$}}}}<!--
-->{{#vardefine:linkItem|{{replace|{{#var:item}}|%s*[,;]%s*(.+)$}}}}<!--
-->{{#vardefine:collection
|{{Replace|{{Replace|{{Replace
|{{#var:output}}|of|}}
|Encha?n?t?e?d?|}}
|%s*Block%s*|}}}}

{{Collection Recipe|{{#var:collection}}

|A1 = {{#if:{{#var:shapeless}}
|{{Slot|{{#var:item}}
|link={{#if:{{#var:input_goto}}
|none|{{#var:linkItem}}}}
|class={{#var:input_goto}}}}
|{{Slot|}}}} 

|B1 = {{Slot|{{#var:item}}
|link={{#if:{{#var:input_goto}}
|none|{{#var:linkItem}}}}
|class={{#var:input_goto}}}} 

|C1 = {{#if:{{#var:shapeless}}
|{{Slot|{{#var:item}}
|link={{#if:{{#var:input_goto}}
|none|{{#var:linkItem}}}}
|class={{#var:input_goto}}}}
|{{Slot|}}}}


|A2 = {{Slot|{{#var:item}}
|link={{#if:{{#var:input_goto}}
|none|{{#var:linkItem}}}}
|class={{#var:input_goto}}}} 

|B2 = {{Slot|{{#var:item}}
|link={{#if:{{#var:input_goto}}
|none|{{#var:linkItem}}}}
|class={{#var:input_goto}}}} 

|C2 = {{#if:{{#var:shapeless}}
|{{Slot|}}
|{{Slot|{{#var:item}}
|link={{#if:{{#var:input_goto}}
|none|{{#var:linkItem}}}}
|class={{#var:input_goto}}}}}}


|A3 = {{Slot|}}

|B3 = {{#if:{{#var:shapeless}}
|{{Slot|}}
|{{Slot|{{#var:item}}
|link={{#if:{{#var:input_goto}}
|none|{{#var:linkItem}}}}
|class={{#var:input_goto}}}}}} 

|C3 = {{Slot|}}

|Output={{Slot|{{{Output| Enchanted {{{1|{{ROOTPAGENAME}}}}}}}}}}
|id={{{id|}}}
|return_id={{{return_id|{{{return_to|default}}}}}}
|return_text={{{return_text|{{{goback|{{#var:collection}} Collection}}}}}}
|title={{{title|{{#var:output}} Recipe}}}
|custom=1
}}
</includeonly>
<noinclude>{{Documentation}}</noinclude>
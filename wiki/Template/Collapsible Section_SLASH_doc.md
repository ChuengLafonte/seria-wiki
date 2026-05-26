{{Documentation subpage}}
'''Collapsible Section''' and '''Collapsible Section Button''' are templates used to easily create collapsible sections and buttons used to show/hide a portion of content.

== Syntax ==
=== Collapsible Section Button ===
{{Template shortcut|Coll S B|CSB}}
{{T|Collapsible Section Button|text/name/1|id|id{2-9}}} where:
* {{s|text}} or {{s|name}} or {{s|1}} is the name of the button (shown on the button itself). Default to "Show/Hide".
* {{s|id}} and {{s|id2}} through {{s|id9}} are the ids of the collapsed section that the button should trigger. (The ids should be meaningful names representing the collapsible sections.)

Besides, this template can use all parameters on [[Template:TextButton]] except {{param|id}}. The description follows the one on [[Template:TextButton]] if not already mentioned above.

=== Collapsible Section ===
{{Template shortcut|Coll S|CS}}
{{T|Collapsible Section|1/text|id|collapsible|mode}} where:
* {{s|1}} or {{s|text}} is the content inside the collapsible section.
* {{s|id}} is the id of the collapsible section. (The id should be a meaningful name representing the collapsible section.)
* {{s|class}} is the additional classes for the button. Optional.
* {{s|collapsible}} (optional - default: collapsed) is whether or not the content should be collapsed automatically. Possible inputs are: <code>uncollapsed</code> or <code>un</code>
* {{s|mode}} (optional) is to specify a special output mode to output part of the template. {{Code|begin}} mode only outputs the beginning div for the section. {{Code|end}} mode only outputs the ending div for the section. {{Code|attr}} mode only outputs attributes to collapse a section. This is useful when collapsing a row.

== Examples ==
=== Example 1 ===
<pre>
{{Collapsible Section Button|id=example-button|name=Show/Hide Example 1}}
{{Collapsible Section|Content hidden under the button|id=example-button}}
</pre>
; Produces
{{Collapsible Section Button|id=example-button|name=Show/Hide Example 1}}
{{Collapsible Section|Content hidden under the button|id=example-button}}

=== Example 2: Using begin-end ===
<pre>
{{Collapsible Section Button|id=example-button-2|name=Show/Hide Example 2}}
{{Collapsible Section|id=example-button-2|mode=begin}}
{| class="wikitable"
! A table can be naturally written into the collapsed section,
|-
| no problem whatsoever.
|}
{{Collapsible Section|mode=end}}
</pre>
; Produces
{{Collapsible Section Button|id=example-button-2|name=Show/Hide Example 2}}
{{Collapsible Section|id=example-button-2|mode=begin}}
{| class="wikitable"
! A table can be naturally written into the collapsed section,
|-
| no problem whatsoever.
|}
{{Collapsible Section|mode=end}}

=== Example 3: Full-width Button ===
Full-width button provides the advantage of extending the button to full width, and adding extra margin below the button to separate it from the content below.
<pre>
{{Collapsible Section Button|id=example-button-3|class=full-width-button|name=Show/Hide Example 3}}
{{Collapsible Section|Content hidden under the button|id=example-button-3}}
</pre>
; Produces
{{Collapsible Section Button|id=example-button-3|class=full-width-button|name=Show/Hide Example 3}}
{{Collapsible Section|Content hidden under the button|id=example-button-3}}

== See Also ==
{{FeatureSet/BasicContainers}}

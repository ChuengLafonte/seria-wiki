{{Documentation subpage}}
{{Lua|Collection/UI}}

== Overview ==
{{T|Minion Recipes UI}} is a template used to Create a [[Minion]] Rewards UI. Uses {{T|Collection Rewards UI}}
{{Tc}}

== Syntax ==
{{T|Minion Recipes UI
|minion
|tier
|collection{{=}}minion
|reward_tier{{=}}tier
|return_id{{=}}return_id
|return_text{{=}}return_text
|id{{=}}id
|hide{{=}}hide
|clickable{{=}}clickable
|fulldepth{{=}}fulldepth
|m=1
}}
* {{S|minion}} or {{S|collection}} - The minion to use. May be any valid [[Minion]]. {{S|collection}} is for backwards compatibility.
* {{S|tier}} or {{S|reward_tier}} - The Collection tier. Normally, this defaults to 1. It can be set to another value. This is optional. {{S|reward_tier}} is for backwards compatibility.
* The parameters {{S|id}}, {{s|return_id}}, and {{S|return_text}} are the same as {{T|UI}}. See the documentation on those parameters for further info. (See [[Project:Style Manual/UIs|here for further info]])

== Examples ==
===[[Diamond Minion]]===

<pre>{{Minion Recipes UI|Diamond}}</pre>
;Produces
{{Minion Recipes UI|Diamond}}
===[[Redstone Minion]]===

<pre>{{Minion Recipes UI|Redstone|2}}</pre>
;Produces
{{Minion Recipes UI|Redstone|2}}

== See Also ==
{{FeatureSet/UI}}

<!-- Place template categories here -->
<includeonly>
[[Category:UI Templates]]
[[Category:UI Collection Templates]]
</includeonly>
{{Policy}}
<!-- ORIGINALLY TAKEN FROM The WIKIPEDIA -->
'''Modules''' are scripts written with the [[mw:Extension:Scribunto|Scribunto]] [[wp:MediaWiki extension]] in the programming language [[wp:Lua (programming language)|Lua]]. Using "{{Code|<nowiki>{{#invoke:}}</nowiki>}}" in Wikitext, one can call an exported function of a module. This extension supports Lua 5.1 as of July 2025.

== Introduction to Lua Scripting With Scribunto ==
On Wikitext, an exported function of a module is run using the {{ParserLink|invoke}} parser function. This is much like what a template does: you give it arguments, it processes them, and you get a result.

Overall, when invoked from Wikitext, a module function can only get input as text strings passed to <code><nowiki>{{#invoke:}}</nowiki></code> and what can be fetched via {{code|lang=lua|mw.title.new(...):getContent()}} and {{code|lang=lua|frame:expandTemplate()}}. Lua output will not be preprocessed unless {{code|lang=lua|frame:preprocess()}} is explicitly called, meaning that template calls, parser functions, etc. in the output will not be expanded. Also, the combined Lua computation required by a page is limited to 10 seconds CPU time (you can look in the source code of a rendered page to see how long a template or module took to parse). Compared to standard Lua, Scribunto's Lua lacks all sorts of functions (see [[mw:Extension:Scribunto/Lua reference manual#Differences from standard Lua|mw:Extension:Scribunto/Lua reference manual § Differences from standard Lua]]).

Lua code in Scribunto is only run when the page is being parsed. Therefore, the only user input that Lua can receive is by ''page editing'' – it cannot create a box that calculates the square root of a number you type in, or recalculate a piece of the Mandelbrot set depending on which part of the parent set you click on.

Transcluded wiki headers frequently contain a hidden code such as "UNIQ5ae8f2aa414ff233-h-3--QINU" which may need to be stripped out in order for them to be parsed effectively.

Wikilinks using the [[Wikipedia:Help:Pipe trick|Pipe trick]] <kbd ><nowiki>[[My Link| ]]</nowiki></kbd> won't work if returned as output – they need to be written explicitly as <kbd><nowiki>[[My Link|Help]]</nowiki></kbd>. Other pre-save transforms, such as replacing <kbd>~~<nowiki/>~~</kbd > with signatures, will also fail to be processed. Template transclusions, parser function calls, and variable substitutions (i.e. anything with a {{Code|<nowiki>{{...}}</nowiki>}}) will not be processed, nor will tags such as {{tag|ref|o}} or {{tag|nowiki|o}}.

== Guidelines ==

=== Guidelines for Writing Modules ===
# Use module categories where necessary. See [[#Module Categories|#Module Categories]].
# Where applicable, unless specified by other rules, follow the naming convention of [https://google.github.io/styleguide/tsguide.html#naming Google TypeScript Style Guide] or the [https://google.github.io/styleguide/jsguide.html#naming Google JavaScript Style Guide] {{Sup|([[Project:Modules/ADR/Identifier-Style|ADR/Identifier-Style]])}}. Notably,
#* Use {{Code|UpperCamelCase}} for class / interface / type / enum / decorator / type parameter
#* Use {{Code|lowerCamelCase}} for variable / parameter / function / method / property
#* Use {{Code|CONSTANT_CASE}} for global constant value, including enum value
# Use {{Code|snake_case}} for frame arguments of template controllers (i.e. functions that take a frame and return a Wikitext string) {{Sup|([[Project:Modules/ADR/Template-Parameter-Style|ADR/Template-Parameter-Style]])}}.
# Within modules that contain one or more template controllers,
#* Use {{Code|lowerCamelCase}} with no preceding underscore for template controller exported members;
#* Use {{Code|lowerCamelCase}} with one preceding underscore for other exported functions;
#* Use any {{Code|lowerCamelCase}} styles for non-exported functions.
# In a template controller, handle only input and presentation concerns, including Wikitext formatting concerns. Handle other concerns, if any, by calling non-controllers.

=== Guidelines for Wikitext Pages using Modules ===
# A content page should only invoke a module function through a template.
# On the documentation subpage of all templates that depends on one or more modules, use {{t|Lua|<...Module>}} to indicate module dependencies. It will help to better communicate usage.

=== Module Categories ===

; Highly-visible Modules
Highly-visible modules (HVMs) are modules that are used for parsing a large amount of articles. Articles are the end product visible to readers, hence the name "highly-visible". These modules shall be kept operational and updated as much as possible. These modules may be semi or fully protected.

; Meta-modules
Meta-modules (MMs) are modules that are written with the purpose of use on other modules, usually assigned to perform high used routines. These modules can be choke-points for performance to their dependent modules, hence shall be kept operational, efficient, and updated as much as possible. These modules may be semi or fully protected.

== Learn ==
=== Caching ===
This wiki uses the Lua Caching technology for some data modules. Putting large data modules into site cache saves processing time. The cached data will require clicking a button to update.

To refresh cache for a data:
<div style="border:1px double white; padding: 1em 1em; margin: 1em 1em;">
This part requires {{Code|RefreshLuaCache}} to be enabled in [[Special:Preferences#mw-prefsection-gadgets|your gadget settings]]. Otherwise, no refresh handle will be loaded. This gadget is default off, so please check.

See if there is a "refresh cache" handle on the module page or on [[Module:Cache]]. Click on the button to refresh its cache.

Think of the datasheet as drawers we call "entries", with each entry associated with a key used to address the entry. We can put data into a data entry like we put things into a drawer.

Refreshing the cache will update all data in entries of existing keys, and add data entries for new keys; but it will not delete entries of existing keys that no longer exists, even when the key no longer exists in the data module that is being cached.
</div>

To hard refresh a cache:
<div style="border:1px double white; padding: 1em 1em; margin: 1em 1em;">
This part requires the {{Sr|Content Moderator}} user right or higher to complete. Please find [[Project:Staff Assistance|Staff Assistance]] if you need help.

To truly erase data entries of keys that no longer exist in a cached data module, one must use hard refresh. On [[Module:Cache]], increase the corresponding PREFIX variable. For example, change {{Code|slotaliases_01_}} to {{Code|slotaliases_02_}}.

This may cause a spike on Lua time for the following minute. Technically, the previous cache is not removed (only not used), but should be removed after some variable amount of time.
</div>

To hook a data module to cache:
<div style="border:1px double white; padding: 1em 1em; margin: 1em 1em;">
This part requires the {{Sr|Code Editor}} user right or higher to complete. Please find [[Project:Staff Assistance|Staff Assistance]] if you need help.

Step 1: Edit [[Module:Cache]]. Example:
<syntaxhighlight lang="lua">
-- Crafting aliases
local CRAFTING_ALIASES_PREFIX = 'craftingaliases_01_'
p.craftingAliasesCache = varsCacheMap.create({ prefix=CRAFTING_ALIASES_PREFIX, dataModule='Crafting/Aliases' })
</syntaxhighlight>

Step 2: Add page to {{code|supportedCaches}} on [[MediaWiki:Gadget-RefreshLuaCache.js]]. Example:
<syntaxhighlight lang="javascript">
var supportedCaches = {
	...
	crafting_aliases: { type:"simple", dataModule:"Crafting/Aliases", mainModule:"Cache", prefixVar:'CRAFTING_ALIASES_PREFIX' },
},
</syntaxhighlight>

Step 3: Add the hook type to {{T|RefreshCache}}. For example, to add the hook type {{CodeTag|crafting}} that refreshes for {{CodeTag|Module:Crafting/Aliases}}, add the module name(s) in the first "switch" and the button definition in the second "switch", as shown below:
<syntaxhighlight lang="html+handlebars">
...
{{#switch:{{{1|}}}
|crafting=Module:Crafting/Aliases
}}
...
{{#switch:{{{1|}}}
|crafting=<div class="refresh-lua-cache button" data-cache-id="crafting_aliases" style="display:none;">Refresh Aliases Cache</div>
}}
</syntaxhighlight>

Tips: Hook types are grouped based on functionalities. There can be more than one module pages and refresh buttons for one hook type.

Step 4: Add the RefreshCache message on [[Module:Cache/doc]] and other module documentation pages you need access on:
<syntaxhighlight lang="html+handlebars">
{{RefreshCache|<type>}}
</syntaxhighlight>
</div>

Related extensions/scripts:
* The [[mw:Extension:VariablesLua|VariablesLua]] and [[w:c:help:Extension:LuaCache|LuaCache]] extensions
* [[MediaWiki:Gadget-RefreshLuaCache.js]]
* [[Module:Cache]], [[Module:VarsCacheMap]]

== See Also ==
* [[Special:PrefixIndex/Module:]] – tracking of Lua modules can be done by using [[Special:PrefixIndex]]
* [[wp:Help:Lua debugging|Help:Lua debugging]] – a how-to guide about [[Wikipedia:debugging|debugging]] Lua modules
* [[Module:Sandbox]] provides a pseudo-namespace for experimenting with Lua modules
* [[:Category:Lua-based templates]] – groups of Lua-based templates
* [[mw:Manual:Coding conventions/Lua|Manual:Coding conventions/Lua]] – standards to improve the readability of code through consistency
* [[mw:Extension:Scribunto/Lua reference manual]] and all [[mw:Special:PrefixIndex/Module:|Modules]].
* [[WP:Project:Advanced template coding]]

== Notes and References ==
{{reflist}}

{{Policies}}
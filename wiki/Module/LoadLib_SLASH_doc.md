This module is used to ease the loading of other modules. It does this by utilizing the global variable table, which allows for more flexibility in variables. It will also automatically load several modules.
__NOTOC__

==Loading the module==
To load this module and make it available for use, Add this line of code to the start of your module:
{{darkCodeBox|lang=lua|t=
local loadLib = require('Module:LoadLib')
}}

=== Auto-loaded Modules ===
This module automatically loads a preset list of commonly used modules. These names will be accessible through the Global Table of your code environment ({{Code|_G.name}} or {{Code|name}}). To better identify names for code tracing, see [[#Autoloads]] for a list of names.

==Syntax==
{{m|loadLib|_G;table|t;table|options}}
* {{P|_G}} - The {{p|_G}} parameter is the global table. This must be the specific variable {{Code|_G}} or the function will fail.
* {{p|t}} - The collection of modules to load. Each key name in this table represents the variable to save the loaded module under. each key may be a table, with the table containing options for the loader for that specific module. See [[#Use|the section below]] for more details.

==Use==
This module provides a singe function to load other modules.

This function has options that emulate normal lua code.
{{format|Note that when ever using this function, you must use the following code format or this function or it will fail|b=1|u=1}}.
{{darkCodeBox|lang=lua|t=
_G = loadLib(_G, {
    -- Any modules to load go here
})
}}
Note that in these examples, sometimes the named table index is not omitted, which prevents the entire module from being loaded.
If the table index is omitted, the loader will load the module under the index name.
===Variable setting===
You can also add the field {{code|setVars}} to {{code|true}} to make the loader set each method in the module as a variable in the loaded module.
====Example====
{{darkCodeBox|lang=lua|t=
_G = loadLib(_G, {
    moduleName={ 'Module:ModuleName', setVars=true },
    -- Any other modules to load go here
})
}}
Once this code is added to the module, any methods described in {{Code|Module:ModuleName}} will be available as variables in the loaded modules with the variable name being the respective method in {{Code|Module:ModuleName}}.
===Paths===
This module also provides basic relative paths and substitution variables.
Any relative paths are substituted to absolute paths.
These basic relative paths are the following:
*'''Note in these examples that the current page name is {{Code|Module:String/Data}}.'''
*A {{code|/}} at the start of the module name denotes a subpage of the parent (not the root) module.
**Example: {{Code|/Test}} → {{Code|Module:String/Test}}
**Example: {{Code|/Foo/Test}} → {{Code|Module:String/Foo/Test}}
*A {{Code|./}} at the start of the module name denotes a subpage of the root module.
**Example: {{Code|./Test}} → {{Code|Module:String/Test}}
**Example: {{Code|./Foo/Test}} → {{Code|Module:String/Foo/Test}}
*A {{Code|../}} at the start of the module name denotes a subpage of the current module.
**Example: {{Code|../Test}} → {{Code|Module:String/Data/Test}}
**Example: {{Code|../Foo/Test}} → {{Code|Module:String/Data/Foo/Test}}

===Autoloads===
{{:Module:LoadLib/Autoloads/doc}}

===Variables===
You can also use variables (denoted by {{code|${<name>}|}}) in the paths.
These variables are substituted with the contents they repersent.
The list of built-in variables is as follows:
*{{Code|${root}|}} denotes the root page name.
*{{code|${page}|}} denotes the current page name.
*{{code|${subpage}|}} denotes the current subpage name.
*{{code|${base}|}} and {{code|${parent}|}} denotes the base (not root) page name.
*{{code|${fullpage}|}} denotes the current page name (with the namespace prefix).

Custom variables can be created by adding a table in the {{code|subst}} or {{code|substVars}} field in the {{p|options}} parameter.
The table index in the table for variables represents the variable name, and the table value its contents.
A custom variable may be called with the following syntax: {{code|${var:<name>}|}}
====Example====
The example variable here is set to {{code|Foo}} and it's name is {{code|foo}}.
The page name in the example is {{code|Module:Test}}
*{{code|Module:Test/${page}/${var:foo}|}} → {{code|Module:Test/Test/Foo}}
*{{code|Module:${var:foo}/${page}|}} → {{code|Module:Foo/Test}}
====Code Example====
The current page name in this example is {{Code|Module:String}}.
Note that the current path {{code|lang=lua|"Module:Test/${page}/${var:foo}"}} will get subsituted to  {{code|lang=lua|code="Module:Test/String/Foo"|inline=yes}}.
{{code|lang=lua|inline=|code=
loadLib(_G, {
    test="Module:Test/${page}/${var:foo}",
}, {
    substVars={ foo="Foo" },
})
}}
Note the module will throw an error if a custom variable does not exist or there is no substitution table to draw from.
All methods from {{Code|Module:Test/String/Foo}} will now be availible under the {{code|test}} object in the module the function was used.

==Options==
The following consists of different options for the loader to load the module.
Note that you can group each of these options together in one {{m|loadLib}} call.

=== Option: Simple Module Loading ===
This option replicates a standard {{m|require}} call.
See the [[#Replicated code 1|section below]] for the Replicated code.
{{darkCodeBox|lang=lua|t=
_G = loadLib(_G, {
    moduleName='Module:ModuleName'
    -- Any other modules to load go here
})
}}

Once this line of code is added to your module, the module and its methods are available under the table index name.
In this case, all methods of {{Code|Module:ModuleName}} are available under the variable {{code|moduleName}}.
====Replicated code====
{{darkCodeBox|lang=lua|t=
local moduleName = require('Module:ModuleName')
}}

=== Option: Using Field ===
This option only loads a field from a library to the global table.

==== 1 ====
This option replicates a {{m|require}} call and getting a single field from the module and setting that field name as the variable to be used.
See the [[#Replicated code 2|section below]] for the emulated code.
{{darkCodeBox|lang=lua|t=
_G = loadLib(_G, {
    { 'Module:ModuleName', field='foo' }
    -- Any other modules to load go here
})
}}
Once this code is added, the method {{m|foo}} from {{Code|Module:ModuleName}} is available under the {{code|foo}} variable.
==== Replicated code ====
{{darkCodeBox|lang=lua|t=
local foo = require('Module:ModuleName').foo
}}

==== 2 ====
This option replicates a {{m|require}} call and getting a single field from the module and setting that field name as a different variable from the method name.
See the [[#Replicated code 3|section below]] for the emulated code.
{{darkCodeBox|lang=lua|t=
_G = loadLib(_G, {
    bar = { 'Module:ModuleName', field='foo' }
    -- Any other modules to load go here
})
}}
Once this code is added, the method {{m|foo}} from {{Code|Module:ModuleName}} is available under the {{code|bar}} variable.
====Replicated code====
{{darkCodeBox|lang=lua|t=
local bar = require('Module:ModuleName').foo
}}

=== Option: Using Values ===
==== 1 ====
This option replicates a {{m|require}} call and getting multiple fields from the module and setting that field name as the variable to be used.
See the [[#Replicated code 4|section below]] for the emulated code.
{{darkCodeBox|lang=lua|t=
_G = loadLib(_G, {
    { 'Module:ModuleName', values={ 'foo', 'bar', 'baz' }
    -- Any other modules to load go here
})
}}
Once this code is added, the methods {{m|foo}}, {{m|bar}}, and {{m|baz}} from {{Code|Module:ModuleName}} is available under the {{code|foo}}, {{code|bar}}, and {{code|baz}} variables respectively.
====Replicated code====
{{darkCodeBox|lang=lua|t=
local foo = require('Module:ModuleName').foo
local bar = require('Module:ModuleName').bar
local baz = require('Module:ModuleName').baz
}}

==== 2 ====
This option replicates a {{m|require}} call and getting multiple fields from the module and setting that field name as a different variable from the respective method name.
See the [[#Replicated code 5|section below]] for the emulated code.
{{darkCodeBox|lang=lua|t=
_G = loadLib(_G, {
    { 'Module:ModuleName', values={ qux='foo', lorem='bar', ipisum='baz' }
    -- Any other modules to load go here
})
}}
Once this code is added, the methods {{m|foo}}, {{m|bar}}, and {{m|baz}} from {{Code|Module:ModuleName}} is available under the {{code|qux}}, {{code|lorem}}, and {{code|ipisum}} variables respectively.
====Replicated code====
{{darkCodeBox|lang=lua|t=
local qux = require('Module:ModuleName').foo
local lorem = require('Module:ModuleName').bar
local ipisum = require('Module:ModuleName').baz
}}

==== 3 ====
This option uses the value field in the two methods above, but adds a key. This will load the library into the global table besides the values.
See the [[#Replicated code 6|section below]] for the emulated code.
{{darkCodeBox|lang=lua|t=
_G = loadLib(_G, {
    moduleName = { 'Module:ModuleName', values={ qux='foo', lorem='bar', ipisum='baz' }
    -- Any other modules to load go here
})
}}
Once this code is added, the methods {{m|foo}}, {{m|bar}}, and {{m|baz}} from {{Code|Module:ModuleName}} is available under the {{code|qux}}, {{code|lorem}}, and {{code|ipisum}} variables respectively. Also, all methods of {{Code|Module:ModuleName}} are available under the variable {{code|moduleName}}.
====Replicated code====
{{darkCodeBox|lang=lua|t=
local moduleName = require('Module:ModuleName')
local qux = moduleName.foo
local lorem = moduleName.bar
local ipisum = moduleName.baz
}}

== Submodules ==
{{submodules}}

== See Also ==
{{FeatureSet/LuaLibraries}}
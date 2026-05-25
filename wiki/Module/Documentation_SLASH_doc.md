This module implements {{T|Documentation}} and {{T|LuaDocumentation}}. It is best to see those pages, as they are mainly used there. It also has methods so it can be used in regular modules. It provides automatic template notices based off of the template's state (ex: protection levels).
{{dm|Arguments|Yesno|String|Table|Documentation/Config}}
{{Tc}}
==Loading the module==
To load this module and make its method available for use, Add this line of code to the start of your module:
{{darkCodeBox|lang=lua|t=
local Doc = require('Module:Documentation')
}}
All methods described below will be available under the loaded table.

Alternatively, you can use this module using the code below by using {{Code|[[Module:LoadLib]]}}.
{{darkCodeBox|lang=lua|t=
local loadLib = require('Module:LoadLib')

_G = loadLib(_G, {
    Doc='Module:Documentation',
    -- Place any other modules to load in here...
})
}}
Depending on the settings you used in {{m|loadLib|link=Module:LoadLib}}, the methods of this module may be available under their respective variables in the module this module was loaded in.

==Main function/Constructor==
The table this module returns is a class, meaning you can call it as a normal function (Be sure to name the variable you require it under uppercase, as it is considered a best practice in coding to name classes uppercase). This also means you can use it as a normal module.
===Syntax===
{{M|Doc|title;s|type;s,nr|noNotices;boolean,nr|b=1}}
*{{p|title}} - The template/module name to transclude the documentation subpage from. The namespace prefix depends on the type of documentation specified.
*{{p|type}} - The type of documentation box to display. This can be either {{code|Module}} or {{code|Template}}. Templates do not have a testcases unit, and will display a hidden template notice. Modules will have no notice, but will have a testcases unit. Each link in the module is changed according to the type specified. This defaults to {{code|Module}}.
*{{p|noNotices}} - Disables automatic template notices like {{T|Protected}}.
===Example===
{{Code|lang=lua|inline=|code=
local Doc = require('Module:Documentation')

function foo()
    local args = getArgs(frame)
    return Doc("Sandbox", "Module")
end

return foo()
}}
;Produces:
{{#invoke:Documentation|_module|sandbox}}
====Alternative Usage====
{{Code|lang=lua|inline=|code=
local Doc = require('Module:Documentation')

function foo()
    local args = getArgs(frame)
    return Doc.template("!")
end

return foo()
}}
;Produces:
{{#invoke:Documentation|_template|!}}

==Methods==
All methods are available below as fields under the required object name.
__TOC__
==={{M|.main|frame;t,fr}}===
This method returns the documentation box in the mode provided by {{p|main}} with the transclusion title as {{p|title}}, with the optional parameter {{p|noNotices}} to disable notices. See [[#Example]] for example output.

==={{M|.module|title;s|noNotices;bool,nr}}===
This method returns the documentation box in module mode with the transclusion title as {{p|title}}, with the optional parameter {{p|noNotices}} to disable notices. . See [[#Example]] for example output.


==={{M|.template|title;s|noNotices;bool,nr}}===
This method returns the documentation box in template mode with the transclusion title as {{p|title}}., with the optional parameter {{p|noNotices}} to disable notices.  See [[#Example]] for example output.
==Exporting==
This module comes with a configuration to make it easier to port it to other wikis and translate.
This configuration can be found at [[Module:Documentation/Config]].
This is so you do not need to directly edit the code, just the configuration.
All keys are commented to show which ones belong to which.

You can change the message values accordingly to your wiki's needs.

==See Also==
*{{T|LuaDocumentation}}
*{{T|Documentation}}
*{{T|Documentation subpage}}
*{{T|Lua doc subpage}}

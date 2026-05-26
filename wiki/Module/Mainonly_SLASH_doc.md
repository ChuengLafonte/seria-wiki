This module houses functions which are used to determine whether or not the page from which the function is invoked is in the main namespace.

== Loading the module ==
To load this module and make its method available for use, Add this line of code to the start of your module:
{{darkCodeBox|lang=lua|t=
local mainonly = require('Module:Mainonly')
}}
The methods documented below will be available for use under the variable name you loaded this module in.

Alternatively, you can use this module using the code below by using {{Code|[[Module:LoadLib]]}}.
{{darkCodeBox|lang=lua|t=
local loadLib = require('Module:LoadLib')

_G = loadLib(_G, {
    mainonly='Module:Mainonly',
    -- Place any other modules to load in here...
})
}}
Depending on the settings you used in {{m|loadLib|link=Module:LoadLib}}, the methods of this module may be available under their respective variables in the module this module was loaded in.

== Methods ==
The methods documented below will be available for use under the variable name you loaded this module in.
=== {{M|.main|frame;frame}} ===
If this method is called from the main namespace, it returns the value of the first argument in the {{Parameter|frame}} parameter. Otherwise, it returns an empty string.

=== {{M|._main|text;string}} ===
If this method is called from the main namespace, it returns the string in the {{Parameter|text}} parameter. Otherwise, it returns an empty string.

=== {{M|.on_main}} ===
This method returns true if the method is called from the main namespace, and false if called from any other namespace.

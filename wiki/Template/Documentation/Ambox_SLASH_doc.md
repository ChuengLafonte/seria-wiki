{{doc/start}}
This template is a base template for many notice templates.

==Usage==
{{TemplateArguments
|arg1= icon
|desc1= Image file name for use on the left, e.g. "Stub.png"

|arg2= image
|desc2= Left (image) cell content, overrides <code>|icon=</code> if provided.

|arg3= type
|desc3= The top line of test
|req3= true

|arg4= info
|desc4= List of extra info

|arg5= border
|desc5= The colour of the Ambox border. <br>
Possible Values:
* red (serious issue)
* yellow (mild issue)
* green (good!)
* purple (technical change)
* blue (notice)
* orange(stub colour)
* gray
|def5= green

|arg6= format
|desc6= Set value to <code>tiny</code> to display a small, left-aligned box showing only the <code><nowiki>|type=</nowiki></code> value.

|arg7= style
|desc7= Any extra HTML style attributes
}}
== Examples ==

<pre>{{Ambox
| type = I am type
| info = I am info
}}</pre>
Produces:
{{Ambox
| type = I am type
| info = I am info
}}

<pre>{{Ambox
| type = I am tiny
| icon = Icon-template.png
| format = tiny
}}</pre>
Prodcues:
{{Ambox
| type = I am tiny
| icon = Icon-template.png
| format = tiny
}}

<pre>{{Ambox
| image = [[Image:Icon-boilerplate.png]]
| border = red
| type = I am type
| info =
* I am info
}}</pre>
Produces:
{{Ambox
| image = [[Image:Icon-boilerplate.png]]
| border = red
| type = I am type
| info =
* I am info
}}


<pre>{{Ambox
| border = yellow
| type = I am type
| info =
* I am info
}}</pre>
Produces:
{{Ambox
| border = yellow
| type = I am type
| info =
* I am info
}}

<pre>{{Ambox
| border = green
| type = I am type
| info =
* I am info
}}</pre>
Produces:
{{Ambox
| border = green
| type = I am type
| info =
* I am info
}}

<pre>{{Ambox
| border = purple
| type = I am type
| info =
* I am info
}}</pre>
Produces:
{{Ambox
| border = purple
| type = I am type
| info =
* I am info
}}

<pre>{{Ambox
| border = blue
| type = I am type
| info =
* I am info
}}</pre>
Produces:
{{Ambox
| border = blue
| type = I am type
| info =
* I am info
}}

<pre>{{Ambox
| border = orange
| type = I am type
| info =
* I am info
}}</pre>
Produces:
{{Ambox
| border = orange
| type = I am type
| info =
* I am info
}}

<pre>{{Ambox
| border = gray
| type = I am type
| info =
* I am info
}}</pre>
Produces:
{{Ambox
| border = gray
| type = I am type
| info =
* I am info
}}

[[Category:Notice templates]]
{{doc/end}}
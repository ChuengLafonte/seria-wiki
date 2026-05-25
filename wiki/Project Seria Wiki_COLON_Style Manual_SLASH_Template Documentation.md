{{Policy|TD|TEMPLATEDOC|TEMPDOC|DOC}}
:< [[Project:Policies|Policies]]
'''Template Documentation''' are pages documenting how to use a template. In general, they should follow a specific Format. Documentation (Doc for short) pages should also be easy to understand. They can come in any format, but should in general follow this format.
Doc are always subpages of the parent template they are describing.
==Templates to use for Doc Pages==
The Following Templates are used for doc pages to describe a page.
*{{T|T}} - Allows for formatting of template parameters and/or linking templates
*{{T|Lua}} - Creates a {{Code|Float-right}} box that indicates this template invokes [[Help:Lua|lua]].
*{{T|Template shortcut}} - Indicates the template has a shortcut, or alias created through a redirect to the template's main page.
*{{T|Documentation subpage}} - Used at the top of every template documentation to categorize and notify the readers.
*{{Code|<nowiki><pre></nowiki>}} - Used for Displaying the source code of examples, sometimes used for a template that has too many parameters to display with {{T|T}}.
*{{T|Code}} - Used to format code for arguments.
*{{T|Param}} - Formats text to represent a template argument/parameter
*{{T|Documentation}} - Transcludes the documentation on the template page.
==General Layout==
On the parent template, add the following code to transclude the documentation page:
{{Code|<nowiki><noinclude>{{Documentation}}</noinclude></nowiki>}}
This will make the documentation subpage appear on the parent template.
===Overview Section===
The Documentation page should start with {{T|Documentation subpage}}. Then you should write a short summary of what the template does.
If the template uses lua, place {{T|Lua}} on the top of the page. After that you should add {{T|TocClear}} to the end of the section. This will move any excess elements away from the section and add a {{Code|TOC}} (Table of contents).
*This is not the only way to write the top section. If you feel the Need to add more information, please feel free to do so.
===Syntax===
This is the most important part. This will describe how to use the template to the reader. There are many styles of syntax documentation, but in general, the following methods are used.
:When describing a parameter, write the parameter name with {{T|Param}}, then go into further detail about the template argument.
:When a Template has a shortcut, be sure to use {{T|Template shortcut}} at the beginning of the section to notify the reader of the existence of a shortcut.
;Method 1 using {{T|T}} 
*Example: [[Template:Green/doc]]
*Start the section with the {{T|T}}. Then add any parameters the template has. Example: {{T|Green|Text}}<br>Then, use {{T|Param}} to describe any parameters the template has in further details.
**Most Documentation pages will use this method, it is the most intuitive and easy to read.
**If the template has too many parameters to fit into 1 line, you can add the {{code|m}} parameter to {{T|T}} to make each line house a parameter instead of just all of the parameters on a single line.
;Method 2 using {{Tag|pre}} 
*Example: [[Template:ArmorStats/doc]]
*Start the Section with {{Tag|pre}}. Then Write all the template parameters blank, as if you were to actually use the template. Then, In the Parameter arguments, Write a general description of the parameter.
**This method is less easy to read, and should in general only be used if the template has too many parameters to use with {{T|T}}.
;Method 3 Using a Table
*Start the Section with a wikitable. The table layout should follow the following format:<br>
{| class="wikitable" style="margin: 1em;"
!Parameter
!Possible Input
!Use
|-
|colspan="3" style="text-align: center;"|<span style="font-family: monospace;">...</span>
|}
*Next, Fill the {{Code|Parameter}} with the parameter name. Then, in the next column, put its possible inputs. Examples Include A few words, numbers or just anything. In the Third column, elaborate on the parameters uses. This will explain what the parameter does to the output of the template.
**This Method is easier to read than the {{Tag|pre}} method, and is best for templates for a large number of parameters.
;Syntax Section Notes
*If the Parameters are complex even for 1 of these methods, you can create a second section where you elaborate even further on the parameters.
*You can add notes to any of the parameters to alert the user of bugs or other issues or thing that reader should be alerted of.

===Examples===
The examples section of a documentation page shows examples of using the template. This section is just as important if not more than the {{Code|Syntax}} section. 
;1 example
*Start the section with {{Tag|pre}}. Write the template example's code in the tag. This shows what source code is shown in the example. Then add a {{B|Produces}} (Can be bold text or a heading) separator between the template output and the source code. Then copy the text in the {{tag|pre}} tag and paste it below the {{Code|Produces}} heading.
;Multiple examples 
*Start the section with the same method as above. Then between the examples, add some sort of separator indicating a different example.
;Notes
*It is best to have more than 1 example, it helps the reader think to how to use the template.
===Other Sections===
It is recommended to have other sections besides the ones listed above, to help the reader even more. Possible other sections include
{{Code|See Also, Template Parameter Definitions}} and more.
*Any Other Sections Should go below the {{Code|Examples}} Section.

==Example Documentation Subpage==
{{/source}}
==Best Practices==
*When creating a documentation subpage, try to make it as understandable as possible. It helps the reader to use their intuition to understand how to use the template.
{{Policies}}

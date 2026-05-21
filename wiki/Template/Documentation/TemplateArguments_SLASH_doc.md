{{Doc/start}}
This is a template used to display arguments of templates

==Usage==
{{TemplateArguments
|note1 = The <code>#</code> symbol must be replaced by a number, multiple arguments can be added by changing this number. (Minimum of 1)

|arg1= templateName
|desc1= The name of the template
|def1= The base page name

|arg2= note#
|desc2= Notes to be placed between the example and table, they are automatically prefixed with <code>'''Note:'''</code>. The <code>*</code> for required arguments is automatically placed and does not require a note. 

|arg3= arg#
|desc3= The name of the #th argument (the input value)
|req3= true

|arg4= desc#
|desc4= A description of what the #th argument is used for

|arg5= def#
|desc5= The default value of the #th argument

|arg6= req#
|desc6= Set to true if the #th argument is required
|def6= false

|arg7= replace#
|desc7= Replacement argument text for the #th argument in the template example (Used for numerical values that don't need to be impicitly mentioned)
|def7= <nowiki>| arg# = </nowiki> 
}}

==Examples==
<pre>{{TemplateArguments
|templateName= UnderConstruction
|arg1= 1
|replace1= translation
|desc1= Text to display inside the banner (Used for translation purposes)
|def1= '''Attention:''' This page is still under construction and is incomplete.
}}</pre>
Produces:
{{TemplateArguments
|templateName= UnderConstruction
|arg1= 1
|replace1= translation
|desc1= Text to display inside the banner (Used for translation purposes)
|def1= '''Attention:''' This page is still under construction and is incomplete.
}}

<pre>{{TemplateArguments
|templateName= Trade
|note1 = The <code>#</code> symbol must be replaced by a number, multiple arguments can be added by changing this number. (Minimum of 1 and Maximum of 20)

|arg1= merchant
|desc1= The name of the merchant, displayed as the heading 
|def1= The name of the current page

|arg2= tradeLabel
|desc2= The label used for the merchant header (Used for translation purposes)
|def2= Trades

|arg3= priceLabel
|desc3= The label used for the price header (Used for translation purposes)
|def3= Price

|arg4= productLabel
|desc4= The label used for the product header (Used for translation purposes
|def4= Product

|arg5= in#
|desc5= The item for the #th trades input 
|def5= Emerald

|arg6= in#amount
|desc6= The amount for the #th trades input 
|def6= 1

|arg7= in#img
|desc7= The image for the #th trades input 
|def7= <code><nowiki>{{WynnIcon|{{{in#}}}}}</nowiki></code>

|arg8= out#
|desc8= The item for the #th trades output 
|req8= true

|arg9= out#amount
|desc9= The amount for the #th trades output 
|def9= 1

|arg10= out#img
|desc10= The image for the #th trades output 
|def10= <code><nowiki>{{WynnIcon|{{{out#}}}}}</nowiki></code>

|arg11= note#
|desc11= A note for the #th trade
}}</pre>
Produces:
{{TemplateArguments
|templateName= Trade
|note1 = The <code>#</code> symbol must be replaced by a number, multiple arguments can be added by changing this number. (Minimum of 1 and Maximum of 20)

|arg1= merchant
|desc1= The name of the merchant, displayed as the heading 
|def1= The name of the current page

|arg2= tradeLabel
|desc2= The label used for the merchant header (Used for translation purposes)
|def2= Trades

|arg3= priceLabel
|desc3= The label used for the price header (Used for translation purposes)
|def3= Price

|arg4= productLabel
|desc4= The label used for the product header (Used for translation purposes
|def4= Product

|arg5= in#
|desc5= The item for the #th trades input 
|def5= Emerald

|arg6= in#amount
|desc6= The amount for the #th trades input 
|def6= 1

|arg7= in#img
|desc7= The image for the #th trades input 
|def7= <code><nowiki>{{WynnIcon|{{{in#}}}}}</nowiki></code>

|arg8= out#
|desc8= The item for the #th trades output 
|req8= true

|arg9= out#amount
|desc9= The amount for the #th trades output 
|def9= 1

|arg10= out#img
|desc10= The image for the #th trades output 
|def10= <code><nowiki>{{WynnIcon|{{{out#}}}}}</nowiki></code>

|arg11= note#
|desc11= A note for the #th trade
}}

{{Doc/end}}
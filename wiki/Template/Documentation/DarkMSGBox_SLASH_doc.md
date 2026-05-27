{{Doc sp}}

{{T|DarkMSGbox}} is a template used to make making wiki-color aligned message boxes very easy. It supports multiple colors.

== Syntax ==
{| class="article-table"
!Parameter || Use || Valid Inputs
|-
|{{S|image}} || Adds an image on the left. || anything
|-
|{{S|image_right}} || (Optional) Adds a image on the right. || anything
|-
|{{S|text}} || Adds Text to the Main box body. || anything
|-
|{{S|note}} || Adds a note below the main text body. || anything
|-
|{{s|bottom_text}} || Adds Text to the bottom section of the box. || anything
|-
|{{S|category}} || Adds a Category the Message box. This category will be added to pages which the message box is trancluded. || Category Name
|-
|{{s|template_cat}} || Adds a category for the template. Seperate categories with commas. || text
|-
!colspan="3" | Style parameters
|-
|{{s|image_right_style}} || CSS parameters for the right image box. || CSS parameters
|-
|{{s|bottom_style}} || CSS parameters for the bottom box. || CSS parameters
|-
|{{S|box_class}} || Additional classes for the box. || anything
|-
|{{S|box_color}} || Changes the color of the message box. || Available Colors
|-
|{{s|box_style}} || CSS parameters for the main box. || CSS parameters
|-
|{{s|text_style}} || CSS parameters for the text box. || CSS parameters
|-
|{{s|image_style}} || CSS parameters for the image box. || CSS parameters
|}

{| class="wikitable"
! colspan=3 | Supported Colors
|-
! Color !! Param !! Effect (shown with inline message boxes)
|-
| None (Use wiki accent color) || {{Bc}} || {{DarkMessageBox|image=&nbsp;|text=This is an example.}}
|-
| Blue || {{Code|1=box_color=blue}} || {{DarkMessageBox|image=&nbsp;|text=This is an example.|box_color=blue}}
|-
| Green || {{Code|1=box_color=green}} || {{DarkMessageBox|image=&nbsp;|text=This is an example.|box_color=green}}
|-
| Gray || {{Code|1=box_color=gray}} || {{DarkMessageBox|image=&nbsp;|text=This is an example.|box_color=gray}}
|-
| Magenta || {{Code|1=box_color=magenta}} || {{DarkMessageBox|image=&nbsp;|text=This is an example.|box_color=magenta}}
|-
| Orange || {{Code|1=box_color=orange}} || {{DarkMessageBox|image=&nbsp;|text=This is an example.|box_color=orange}}
|-
| Purple || {{Code|1=box_color=purple}} || {{DarkMessageBox|image=&nbsp;|text=This is an example.|box_color=purple}}
|-
| Red || {{Code|1=box_color=red}} || {{DarkMessageBox|image=&nbsp;|text=This is an example.|box_color=red}}
|-
| Yellow || {{Code|1=box_color=yellow}} || {{DarkMessageBox|image=&nbsp;|text=This is an example.|box_color=yellow}}
|}

== Examples ==
=== Example 1 ===
<pre>{{DarkMSGbox
|image = [[File:Wiki.png|60px]]
|text = Example Text.
}}</pre>
;Produces
{{DarkMSGbox
|image = [[File:Wiki.png|60px]]
|text = Example Text.
}}

=== Example 2: With Bottom Text ===
<pre>{{DarkMSGbox
|image = [[File:Wiki.png|60px]]]]
|image_right = [[File:Wiki.png|60px]]
|text = {{B|Example Text.}} {{Lorem}}
|bottom_text = Example Text.
}}</pre>
;Produces
{{DarkMSGbox
|image = [[File:Wiki.png|60px]]
|image_right = [[File:Wiki.png|60px]]
|text = {{B|Example Text.}} {{Lorem}}
|bottom_text = Example Text.
}}

== See Also ==
{{FeatureSet/BasicContainers}}
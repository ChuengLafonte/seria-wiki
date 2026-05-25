<includeonly><!--
 -->{{#ifeq:{{lc:{{SUBPAGENAME}}}} |{{{override|doc}}}
     | <!--(this template has been transcluded on a /doc or /{{{override}}} page)-->
</includeonly><!--

      -->{{#ifeq:{{{doc-notice|show}}} |show
          | <table class="messagebox" style="margin-bottom: 0.8em;"><tr>
<td>[[File:Dev icon.png|x50px]]</td>
<td style="width:100%; padding:0.25em 0.9em;">'''This is a [[Project:Lua|module]] documentation [[Wikipedia:Wikipedia:Subpages|subpage]] for {{#replace:{{{1|[[:{{SUBJECTSPACE}}:{{#replace:{{BASEPAGENAME}}|/doc}}]]}}}|/doc}}'''.<br />It contains usage information, [[Wikipedia:Wikipedia:Categorization|categories]] and other content that is not part of the original {{#if:{{{text2|}}} |{{{text2}}} |{{#if:{{{text1|}}} |{{{text1}}} |{{#ifeq:{{SUBJECTSPACE}} |{{ns:User}} |{{lc:{{SUBJECTSPACE}}}} template page |{{#if:{{SUBJECTSPACE}} |{{lc:{{SUBJECTSPACE}}}} page|article}}}}}}}}. </td>
</tr></table>
         }}<!--

      -->{{DEFAULTSORT:{{{defaultsort|{{PAGENAME}}}}}}}<!--

      -->{{#if:{{{inhibit|}}} |<!--(don't categorize)-->
          |   <includeonly><!--
               -->{{#ifexist:{{#replace:{{SUBJECTPAGENAME}}|/doc}}
                   | [[Category:{{#switch:{{SUBJECTSPACE}} |Template=Template |Module=Module |User=User |#default=Project}} documentation]]
                   | [[Category:Documentation subpages without corresponding pages]]
                  }}<!--
           --></includeonly>
         }}<!--

(completing initial #ifeq: at start of template:)
--><includeonly>
     | <!--(this template has not been transcluded on a /doc or /{{{override}}} page)-->
    }}<!--
--></includeonly><noinclude>{{Documentation}}</noinclude>

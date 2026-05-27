<includeonly><!--
 -->{{#ifeq:{{lc:{{SUBPAGENAME}}}} |{{{override|doc}}}
     | <!--(this template has been transcluded on a /doc or /{{{override}}} page)--><!--
(Add messagebox:)
      -->{{#ifeq:{{{doc-notice|show}}} |show
          | {{TextMessageBox
|image=[[File:Paper Nuavo.png|60px]]
|text='''This is a [[Wikipedia:Wikipedia:Template documentation|documentation]] [[Wikipedia:Wikipedia:Subpages|subpage]] for {{{1|[[:{{SUBJECTSPACE}}:{{BASEPAGENAME}}]]}}}'''.<br />It contains usage information, [[Wikipedia:Wikipedia:Categorization|categories]] and other content that is not part of the original {{#if:{{{text2|}}} |{{{text2}}} |{{#if:{{{text1|}}} |{{{text1}}} |{{#ifeq:{{SUBJECTSPACE}} |{{ns:User}} |{{lc:{{SUBJECTSPACE}}}} template page |{{#if:{{SUBJECTSPACE}} |{{lc:{{SUBJECTSPACE}}}} page|article}}}}}}}}.
}}
         }}<!--
(Add defaultsort:)
      -->{{DEFAULTSORT:{{{defaultsort|{{PAGENAME}}}}}}}<!--
(Add category:)
      -->{{#if:{{{inhibit|}}} |<!--(don't categorize)-->
          |   <!--
               -->{{#ifexist:{{{1|{{NAMESPACE}}:{{BASEPAGENAME}}}}}
                   | [[Category:{{#switch:{{SUBJECTSPACE}} |Template=Template |Module=Module |User=User |#default=Project}} documentation]]
                   | [[Category:Documentation subpages without corresponding pages]]
                  }}<!--
           -->
         }}<!--
(Completing initial #ifeq: at start of template:)
-->
     | <!--(this template has not been transcluded on a /doc or /{{{override}}} page)-->
}}<!--
--></includeonly><noinclude>{{Documentation}}</noinclude>
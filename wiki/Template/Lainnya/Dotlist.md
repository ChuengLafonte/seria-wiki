<includeonly>{{#vardefine:list|}}{{#vardefine:list|[[{{trim|{{#explode: {{{1|}}}|,|0}}}}]]}}{{#vardefine:i|1}}{{#while:
  | {{#explode: {{{1|}}}|,|{{#var:i}} }}
  | {{#vardefine:list| {{#var:list}}{{*}}[[{{trim|{{#explode: {{{1|}}}|,|{{#var:i}}}}}}]]}}{{#vardefine: i | {{#expr: {{#var:i}} + 1}} }}
}}{{#var:list}}{{#vardefine:list|}}</includeonly><noinclude>{{doc}}[[Category:Formatting templates]]</noinclude>
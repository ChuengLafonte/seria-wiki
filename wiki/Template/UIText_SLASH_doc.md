{{Documentation subpage}}
==Overview==
{{Lua|UIText}}
{{T|UIText}} is a template used to make making UI's a lot easier. It also allows you to use unicode code points like {{Code|\u{10F}|}} or {{code|\u134}}, and other shorthands like {{code|\stat{Str}|}}.
{{Tc}}

==Syntax==
{{T|UIText|text}}
*{{S|text}} - The text to input. Unicode codepoints like {{code|\u{2fc4}|}} or {{code|\uA32}} maybe used. Other escapes like {{code|\stat{<stat>}|}} may be used. See below for more details.
==Shorthands==
{| class="wikitable"
!Shorthand Prefix !! Possible Values !! Description !! Example
|-
|<center>{{Code|u}}</center> || Any valid Unicode sequence || Represents a Unicode codepoint || {{code|\u{2fc4}|}} → {{code|⿄}}
|-
|<center>{{Code|stat}}</center> || Any valid stat name or alias (see {{t|Stat}}) || Represents a statname like {{stat|str}} || {{code|\stat{str}|}} → {{code|&c❁ Strength&r}}
|-
|<center>{{Code|potion}}</center> || Any valid potion or alias (see {{t|PotionName}}) || Represents a statname like {{potN|haste}}. Tiers and the "potion" suffix may be used. || {{PL|
*{{code|\potion{haste}|}} → {{code|&eHaste&r}}
*{{code|\potion{haste iv pot}|}} → {{code|&eHaste IV Potion&r}}
*{{code|\potion{haste iv}|}} → {{code|&eHaste IV&r}}
}}
|-
|<center>{{Code|rarity}}</center> || Any valid rarity or alias (see {{t|Rarity}}) || Represents a rarity like {{r|r}}.|| {{code|\rarity{rare}|}} → {{code|&9&lRARE&r}}
|-
|<center>{{Code|enchant}}</center> || Any valid enchantment or alias (see {{t|EnchantmentsLink}}) || Represents an enchantment like {{ench|gk}}.||
{{code|\enchant{giant killer iv}|}} → {{code|&9&Giant Killer IV&r}}
|}

==Examples==
===Example 1===
<pre>{{UIText|\u201}}</pre>
;Produces
{{UIText|\u201}}

===Example 2===
<pre>{{UIText|\ench{giant killer iv}}}</pre>
;Produces
{{UIText|\enchant{giant killer iv}|}}

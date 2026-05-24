{{Documentation subpage}}
{{Lua|UI}}

{{T|UI}} is a template used to create a generic UI.

{{T|UIPage}} is a template used to transclude another UI page to your page with custom settings.
{{Tc}}

== UI Syntax ==
{{T|UI
|title
|...
|arrow{{=}}arrow
|close{{=}}close
|id{{=}}id
|return_id/goback_id{{=}}return_id
|return_text/goback_text/goback{{=}}return_text
|return_link/goback_link{{=}}return_link
|hide{{=}}hide
|fill{{=}}fill
|defaultnolink/dnl{{=}}defaultnolink
}}
=== Parameters ===
* {{S|title}} - The UI title. This can be any form of text.
* {{S|...}} - The UI Slots. This can be a unnamed argument list, where each parameter can be a slot item, or custom html, or a comma-separated list of options.
** You can use {{Code|-}} to force a new UI row. This will make all remaining slots in the row blanks. If the amount of slots on the row exceeds 9, it will automatically go to a new line.
** The first comma-separated item is the slot item, the second is the slot's optional [[Hypixel SkyBlock Wiki:Style Manual/UIs#Tabbers|Go-To id]], the third is the custom slot title, the fourth is the custom slot text.
** You can leave a list argument to be empty, it will not be interpreted.
** The syntax for a list entry would be {{code|<item>[; count][, [<id>[; <link>]][, [<title>][, <text>]]]}}.
** An example list entry where you wanted to a link to another UI called {{code|diamond}}, where the display item would be an [[Enchanted Diamond]], and it would have custom Text.
::: <pre>Enchanted Diamond; 32, diamond, &aCustom Title, &cCustom Text</pre>
:::* Produces:{{Slot|Enchanted Diamond, 32|class=goto-diamond|title=&aCustom Title|text=&cCustom Text}}
::: <pre>Enchanted Emerald; 32, custom-id; none, &aCustom Title, &cCustom Text</pre>
:::* Produces:{{Slot|Enchanted Emerald, 32|class=goto-custom-id|title=&aCustom Title|text=&cCustom Text|link=none}}
:* To manually set by coordinates, you can supply a parameter like {{code|1, 5}} at the beginning. The format for such an argument is {{code|<row>, <column>{{=}}<values>}}.
:::* Source code example: {{code|{{!}}1, 5{{=}}Diamond}}
:* You can also supply a parameter like {{code|row 1}} or {{code|row1}} to set an entire UI row to the value provided. This argument will represent {{G|9}} slots, and is an iteration. The max number for an argument like this is {{G|6}}.
:* You can do the same thing for columns by using parameters like {{code|column 1}} or {{code|col 3}}. The maximum number to start/end is {{G|9}}.
:* You can insert {{code|$n}} into the argument to repersent the current iteration number.
::* This subsitution can be escaped with {{code|\$n}}.
:* An option for this argument delimited by a semicolon at the end of the input is the starting/ending number for the iteration. The format for such an argument is {{code|<values>; <start>[, <end>]}}, which would start the iteration at {{g|<start>}} and end at {{G|<end>}}, and set row 1 to the values provided. {{G|<end>}} defaults to the end of row and can be omitted.
::* Source code example: {{code|{{!}}row 1{{=}}Diamond; 6, 8}}
:* If instead written in the format of {{code|<values>; <num>, <num>, <num>, [<num>, ...]}}, the corresponding columns denoted by each {{g|<num>}} of row 1 will be set to the values provided.
::* Source code example: {{code|{{!}}row 1{{=}}Diamond; 1, 3, 6, 8, 9}}
* {{S|arrow}} - Repositions the automatic "Go Back" [[Arrow]] in the UI, with the format of {{code|<row>, <column>}}. Setting this to "none" disables the automatic "Go Back" Arrow in the UI. {{S|noarrow}} can also be used to disable it.
* {{S|close}} - Repositions the automatic "Close" [[Barrier]] in the UI, with the format of {{code|<row>, <column>}}. Setting this to "none" disables the automatic "Close" Barrier in the UI. {{S|noclose}} can also be used to disable it.
* {{S|id}} - The ID of the UI (without the {{code|ui-}} prefix). This is needed for when [[Hypixel SkyBlock Wiki:Style Manual/UIs#Tabbers|UI Tabbers]] are used.
* {{S|return_id}} - The ID of the UI to return to (without the {{code|ui-}} prefix) when the "Go Back" Arrow is clicked. This is needed for when UI Tabbers are used and if this UI is a child UI.
* {{S|return_text}} - The text of the "Go Back" Arrow in the UI.
* {{S|return_link}} - The link of the "Go Back" Arrow in the UI.
* {{S|hide}} - Hides the UI. This is needed for when UI Tabbers are used and if this UI is a child UI. Default off.
* {{s|fill}}  - The fill mode. Defualts true. Setting to {{Code|true}} will default all slots to "Blank". Setting to {{Code|false}} will default all slots to an "Empty" slot. Setting to {{Code|border}} will default border slots to be "Blank" and all other slots "Empty".
* {{s|rows}} - The maximum number of rows for the UI. This may be any number, but it UI's are traditionally 6 rows tall. Defaults to 6.
* {{s|cols}} - The maximum number of columns for the UI. This may be any number, but it UI's are traditionally 9 columns tall. Defaults to 9.
* {{s|defaultnolink}} - Whether {{code|<link>}}s unspecified should be set to none automatically, instead of linking to the page name of slot item. Default off.

== UIPage Syntax ==
{{T|UIPage
|page name
|custom option 1{{=}}value
|custom option 2{{=}}value
|...
}}

Only the '''first''' UI will be substituted with the custom options. Templates that do not start with {{code|{{((}}UI{{!}}}} will NOT be transcluded.

=== Parameters ===
* {{S|page name}} - The page name that contains the UI(s) you want to transclude. This can be any page that exists on the (main) namespace.
* {{S|custom option(s)}} - Any optional parameters that can be used with {{T|UI}}. This will replace/add to the options of the '''first''' transcluded UI.

== Examples ==
'''Note:''' All examples have {{code|hide}} set to {{code|false}}.
=== Skills UI ===
{{Collapsible Section Button|Show/Hide Source Code|id=skills}}
{{Collapsible Section
|
<pre>
{{UI|Your Skills
|1, 5=Diamond Sword, none, &aYour Skills, &7View your Skill progression and/&7rewards.//&eClick to show rankings!
|-
|-
|3, 2=Golden Hoe, none, &aFarming, &7Harvest crops and shear sheep to/&7earn Farming XP!//&7Progress to Level I: &e0%/&f-------------------- &e0&6\/&e50//&7Level I Rewards:/  &eFarmhand I/    &7&fGrants &a+&a4&f &6☘ Farming/    &6Fortune&r\, which increases your/    &rchance for multiple crops./  &7&8+&a2 HP &c❤ Health/  &7&aAccess to &bThe Barn/  &7&8+&625 &7Coins//&eClick to view!
|3, 3=Stone Pickaxe, none, &aMining, &7Spelunk islands for ores and/&7valuable materials to earn/&7Mining XP!//&7Progress to Level I: &e0%/&f-------------------- &e0&6\/&e50//&7Level I Rewards:/  &eSpelunker I/    &7&fGrants &a+&a4&f &6☘ Mining/    &6Fortune&r\, which increases your/    &rchance for multiple ore drops./  &7&8+&a1 &a❈ Defense/  &7&aAccess to &6Gold Mine/  &7&9Jerry Stone &7Reforge/  &7&8+&625 &7Coins//&eClick to view!
|3, 4=Stone Sword, none, &aCombat, &7Fight mobs and players to earn/&7Combat XP!//&7Progress to Level I: &e0%/&f-------------------- &e0&6\/&e50//&7Level I Rewards:/  &eWarrior I/    &7&fDeal &a4%&f more damage to/    &fmobs./  &7&8+&a0.5% &9☣ Crit Chance/  &7&aAccess to &cSpider's Den/  &7&8+&625 &7Coins//&eClick to view!
|3, 5=Jungle Sapling, none, &aForaging, &7Cut trees and forage for other/&7plants to earn Foraging XP!//&7Progress to Level I: &e0%/&f-------------------- &e0&6\/&e50//&7Level I Rewards:/  &eLogger I/    &7&fGrants &a+&a4&f &6☘ Foraging/    &6Fortune&r\, which increases your/    &rchance for multiple logs./  &7&8+&a1 &c❁ Strength/  &7&aAccess to &aBirch Park/  &7&8+&625 &7Coins//&eClick to view!
|3, 6=Fishing Rod, none, &aFishing, &7Visit your local pond to fish/&7and earn Fishing XP!//&7Progress to Level I: &e0%/&f-------------------- &e0&6\/&e50//&7Level I Rewards:/  &7&f???&3 Sea Creature/  &eTreasure Hunter I/    &7&fIncreases the chance to find/    &ftreasure when fishing by/    &f&a0.2%&f./  &7&8+&a2 HP &c❤ Health/  &7&8+&625 &7Coins//&eClick to view!
|3, 7=Enchantment Table, none, &aEnchanting, &7Enchant items to earn Enchanting/&7XP!//&7Progress to Level I: &e0%/&f-------------------- &e0&6\/&e50//&7Level I Rewards:/  &eConjurer I/    &7&fGain &a4%&f more experience/    &forbs from any source./  &7&8+&a0.5% &c๑ Ability Damage/  &7&8+&a1 &b✎ Intelligence/  &7&aScavenger Enchantment/  &7&8+&625 &7Coins//&eClick to view!
|3, 8=Brewing Stand, none, &aAlchemy, &7Brew potions to earn Alchemy XP!//&7Progress to Level I: &e0%/&f-------------------- &e0&6\/&e50//&7Level I Rewards:/  &eBrewer I/    &7&fPotions that you brew have a/    &f&a1%&f longer duration./  &7&8+&a1 &b✎ Intelligence/  &7&8+&625 &7Coins//&eClick to view!
|-
|4, 3=Crafting Table, none, &cCarpentry, &7Unlock this skill by talking to/&7the Carpenter in the SkyBlock/&7Hub.//&bNot unlocked yet!
|4, 4=Magma Cream, none, &aRunecrafting, &7Slay bosses\, runic mobs & fuse/&7runes to earn Runecrafting XP!//&7Progress to Level I: &e0%/&f-------------------- &e0&6\/&e50//&7Level I Reward:/  &7&7Access to Level &51 &7Runes//&7&dLevel up Runecrafting to activate/&dthe effects of rune-bearing items!//&eClick to view!
|4, 5=Emerald, none, &aSocial, &7Gain Social XP for every new/&7unique guest\, hosting guests and/&7visiting islands!//&7Progress to Level I: &e0%/&f-------------------- &e0&6\/&e50//&7Level I Rewards:/  &7&fAbility to purchase &dParkour/  &dBlocks &fat Amelia in the Hub/  &7&8+&625 &7Coins//&eClick to view!
|4, 6=Spawn Egg, none, &aTaming, &7Level up pets to earn Taming XP!//&7Progress to Level I: &e0%/&f-------------------- &e0&6\/&e50//&7Level I Rewards:/  &eZoologist I/    &7&fGain &a1%&f extra pet exp./  &7&8+&a1 &d♣ Pet Luck/  &7&8+&625 &7Coins//&eClick to view!
|4, 7=Mort Skull, none, &aDungeoneering, &7Complete Dungeons to level up/&7your classes! Unlock new gear/&7and class upgrades by completing/&7higher tier dungeons!//&7Requires &bCombat Level V&7/&7to enter a Dungeon.//&eClick to view!
|-
|-
|id=skills-default
|goback=&7To SkyBlock Menu
|dnl=true
}}
</pre>
|id=skills}}
<div class="sbw-ui">
{{UI|Your Skills
|1, 5=Diamond Sword, none, &aYour Skills, &7View your Skill progression and/&7rewards.//&eClick to show rankings!
|-
|-
|3, 2=Golden Hoe, none, &aFarming, &7Harvest crops and shear sheep to/&7earn Farming XP!//&7Progress to Level I: &e0%/&f-------------------- &e0&6\/&e50//&7Level I Rewards:/  &eFarmhand I/    &7&fGrants &a+&a4&f &6☘ Farming/    &6Fortune&r\, which increases your/    &rchance for multiple crops./  &7&8+&a2 HP &c❤ Health/  &7&aAccess to &bThe Barn/  &7&8+&625 &7Coins//&eClick to view!
|3, 3=Stone Pickaxe, none, &aMining, &7Spelunk islands for ores and/&7valuable materials to earn/&7Mining XP!//&7Progress to Level I: &e0%/&f-------------------- &e0&6\/&e50//&7Level I Rewards:/  &eSpelunker I/    &7&fGrants &a+&a4&f &6☘ Mining/    &6Fortune&r\, which increases your/    &rchance for multiple ore drops./  &7&8+&a1 &a❈ Defense/  &7&aAccess to &6Gold Mine/  &7&9Jerry Stone &7Reforge/  &7&8+&625 &7Coins//&eClick to view!
|3, 4=Stone Sword, none, &aCombat, &7Fight mobs and players to earn/&7Combat XP!//&7Progress to Level I: &e0%/&f-------------------- &e0&6\/&e50//&7Level I Rewards:/  &eWarrior I/    &7&fDeal &a4%&f more damage to/    &fmobs./  &7&8+&a0.5% &9☣ Crit Chance/  &7&aAccess to &cSpider's Den/  &7&8+&625 &7Coins//&eClick to view!
|3, 5=Jungle Sapling, none, &aForaging, &7Cut trees and forage for other/&7plants to earn Foraging XP!//&7Progress to Level I: &e0%/&f-------------------- &e0&6\/&e50//&7Level I Rewards:/  &eLogger I/    &7&fGrants &a+&a4&f &6☘ Foraging/    &6Fortune&r\, which increases your/    &rchance for multiple logs./  &7&8+&a1 &c❁ Strength/  &7&aAccess to &aBirch Park/  &7&8+&625 &7Coins//&eClick to view!
|3, 6=Fishing Rod, none, &aFishing, &7Visit your local pond to fish/&7and earn Fishing XP!//&7Progress to Level I: &e0%/&f-------------------- &e0&6\/&e50//&7Level I Rewards:/  &7&f???&3 Sea Creature/  &eTreasure Hunter I/    &7&fIncreases the chance to find/    &ftreasure when fishing by/    &f&a0.2%&f./  &7&8+&a2 HP &c❤ Health/  &7&8+&625 &7Coins//&eClick to view!
|3, 7=Enchantment Table, none, &aEnchanting, &7Enchant items to earn Enchanting/&7XP!//&7Progress to Level I: &e0%/&f-------------------- &e0&6\/&e50//&7Level I Rewards:/  &eConjurer I/    &7&fGain &a4%&f more experience/    &forbs from any source./  &7&8+&a0.5% &c๑ Ability Damage/  &7&8+&a1 &b✎ Intelligence/  &7&aScavenger Enchantment/  &7&8+&625 &7Coins//&eClick to view!
|3, 8=Brewing Stand, none, &aAlchemy, &7Brew potions to earn Alchemy XP!//&7Progress to Level I: &e0%/&f-------------------- &e0&6\/&e50//&7Level I Rewards:/  &eBrewer I/    &7&fPotions that you brew have a/    &f&a1%&f longer duration./  &7&8+&a1 &b✎ Intelligence/  &7&8+&625 &7Coins//&eClick to view!
|-
|4, 3=Crafting Table, none, &cCarpentry, &7Unlock this skill by talking to/&7the Carpenter in the SkyBlock/&7Hub.//&bNot unlocked yet!
|4, 4=Magma Cream, none, &aRunecrafting, &7Slay bosses\, runic mobs & fuse/&7runes to earn Runecrafting XP!//&7Progress to Level I: &e0%/&f-------------------- &e0&6\/&e50//&7Level I Reward:/  &7&7Access to Level &51 &7Runes//&7&dLevel up Runecrafting to activate/&dthe effects of rune-bearing items!//&eClick to view!
|4, 5=Emerald, none, &aSocial, &7Gain Social XP for every new/&7unique guest\, hosting guests and/&7visiting islands!//&7Progress to Level I: &e0%/&f-------------------- &e0&6\/&e50//&7Level I Rewards:/  &7&fAbility to purchase &dParkour/  &dBlocks &fat Amelia in the Hub/  &7&8+&625 &7Coins//&eClick to view!
|4, 6=Spawn Egg, none, &aTaming, &7Level up pets to earn Taming XP!//&7Progress to Level I: &e0%/&f-------------------- &e0&6\/&e50//&7Level I Rewards:/  &eZoologist I/    &7&fGain &a1%&f extra pet exp./  &7&8+&a1 &d♣ Pet Luck/  &7&8+&625 &7Coins//&eClick to view!
|4, 7=Mort Skull, none, &aDungeoneering, &7Complete Dungeons to level up/&7your classes! Unlock new gear/&7and class upgrades by completing/&7higher tier dungeons!//&7Requires &bCombat Level V&7/&7to enter a Dungeon.//&eClick to view!
|-
|-
|id=skills-default
|goback=&7To SkyBlock Menu
|dnl=true
}}
</div>

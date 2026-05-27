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
** The first comma-separated item is the slot item, the second is the slot's optional [[Project Seria Caveblock Wiki:Style Manual/UIs#Tabbers|Go-To id]], the third is the custom slot title, the fourth is the custom slot text.
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
* {{S|id}} - The ID of the UI (without the {{code|ui-}} prefix). This is needed for when [[Project Seria Caveblock Wiki:Style Manual/UIs#Tabbers|UI Tabbers]] are used.
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
|4, 3=Crafting Table, none, &cCarpentry, &7Unlock this skill by talking to/&7the Carpenter in the Project Seria Caveblock/&7Hub.//&bNot unlocked yet!
|4, 4=Magma Cream, none, &aRunecrafting, &7Slay bosses\, runic mobs & fuse/&7runes to earn Runecrafting XP!//&7Progress to Level I: &e0%/&f-------------------- &e0&6\/&e50//&7Level I Reward:/  &7&7Access to Level &51 &7Runes//&7&dLevel up Runecrafting to activate/&dthe effects of rune-bearing items!//&eClick to view!
|4, 5=Emerald, none, &aSocial, &7Gain Social XP for every new/&7unique guest\, hosting guests and/&7visiting islands!//&7Progress to Level I: &e0%/&f-------------------- &e0&6\/&e50//&7Level I Rewards:/  &7&fAbility to purchase &dParkour/  &dBlocks &fat Amelia in the Hub/  &7&8+&625 &7Coins//&eClick to view!
|4, 6=Spawn Egg, none, &aTaming, &7Level up pets to earn Taming XP!//&7Progress to Level I: &e0%/&f-------------------- &e0&6\/&e50//&7Level I Rewards:/  &eZoologist I/    &7&fGain &a1%&f extra pet exp./  &7&8+&a1 &d♣ Pet Luck/  &7&8+&625 &7Coins//&eClick to view!
|4, 7=Mort Skull, none, &aDungeoneering, &7Complete Dungeons to level up/&7your classes! Unlock new gear/&7and class upgrades by completing/&7higher tier dungeons!//&7Requires &bCombat Level V&7/&7to enter a Dungeon.//&eClick to view!
|-
|-
|id=skills-default
|goback=&7To Project Seria Caveblock Menu
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
|4, 3=Crafting Table, none, &cCarpentry, &7Unlock this skill by talking to/&7the Carpenter in the Project Seria Caveblock/&7Hub.//&bNot unlocked yet!
|4, 4=Magma Cream, none, &aRunecrafting, &7Slay bosses\, runic mobs & fuse/&7runes to earn Runecrafting XP!//&7Progress to Level I: &e0%/&f-------------------- &e0&6\/&e50//&7Level I Reward:/  &7&7Access to Level &51 &7Runes//&7&dLevel up Runecrafting to activate/&dthe effects of rune-bearing items!//&eClick to view!
|4, 5=Emerald, none, &aSocial, &7Gain Social XP for every new/&7unique guest\, hosting guests and/&7visiting islands!//&7Progress to Level I: &e0%/&f-------------------- &e0&6\/&e50//&7Level I Rewards:/  &7&fAbility to purchase &dParkour/  &dBlocks &fat Amelia in the Hub/  &7&8+&625 &7Coins//&eClick to view!
|4, 6=Spawn Egg, none, &aTaming, &7Level up pets to earn Taming XP!//&7Progress to Level I: &e0%/&f-------------------- &e0&6\/&e50//&7Level I Rewards:/  &eZoologist I/    &7&fGain &a1%&f extra pet exp./  &7&8+&a1 &d♣ Pet Luck/  &7&8+&625 &7Coins//&eClick to view!
|4, 7=Mort Skull, none, &aDungeoneering, &7Complete Dungeons to level up/&7your classes! Unlock new gear/&7and class upgrades by completing/&7higher tier dungeons!//&7Requires &bCombat Level V&7/&7to enter a Dungeon.//&eClick to view!
|-
|-
|id=skills-default
|goback=&7To Project Seria Caveblock Menu
|dnl=true
}}
</div>

=== [[Storage]] ===
{{Collapsible Section Button|Show/Hide Source Code|id=storage}}
{{Collapsible Section
|<pre>
<div class="sbw-ui-tabber">
<!-- STORAGE -->
{{UI|Storage
|1, 5=Ender Chest, none;none, &aEnder Chest, &7Store global items you can/&7access anywhere in your/&7ender chest.
|-
|2, 1=Purple Stained Glass Pane, enderchest-one;none, &aEnder Chest Page 1, /&eLeft-click to open!/&eRight-click to change icon!
|2, 2=Purple Stained Glass Pane, enderchest-two;none, &aEnder Chest Page 2, /&eLeft-click to open!/&eRight-click to change icon!
|2, 3=Purple Stained Glass Pane, enderchest-three;none, &aEnder Chest Page 3, /&eLeft-click to open!/&eRight-click to change icon!
|row 2=Red Stained Glass Pane, none;none, &cLocked Page, &7Unlock more Ender Chest/&7pages in the community/&7shop!;4, 9
|-
|3, 5=Chest, none;none, &aBackpacks, &7Place backpack items in/&7these slots to use them as/&7additional storage that can/&7be accessed anywhere.
|-
|4, 1=Jumbo Backpack, backpack-one;none, &6Backpack Slot 1, &6Jumbo Backpack/&7&7This backpack has &a45&7/&7slots./ /&7&eLeft-click to open!/&7&eRight-click to remove!
|4, 2=Greater Backpack, backpack-two;none, &6Backpack Slot 2, &5Greater Backpack/&7&7This backpack has &a36&7/&7slots./ /&7&eLeft-click to open!/&7&eRight-click to remove!
|4, 3=Large Backpack, backpack-three;none, &6Backpack Slot 3, &5Large Backpack/&7&7This backpack has &a27&7/&7slots./ /&7&eLeft-click to open!/&7&eRight-click to remove!
|4, 4=Medium Backpack, backpack-four;none, &6Backpack Slot 4, &9Medium Backpack/&7&7This backpack has &a18&7/&7slots./ /&7&eLeft-click to open!/&7&eRight-click to remove!
|4, 5=Small Backpack, backpack-five;none, &6Backpack Slot 5, &aSmall Backpack/&7&7This backpack has &a9&7/&7slots./ /&7&eLeft-click to open!/&7&eRight-click to remove!
|4, 6=Brown Stained Glass Pane, none;none, &cEmpty Backpack Slot 6,  /&7&eLeft-click a backpack/&eitem on this slot to place/&eit!
|4, 7=Brown Stained Glass Pane, none;none, &cEmpty Backpack Slot 7,  /&7&eLeft-click a backpack/&eitem on this slot to place/&eit!
|4, 8=Brown Stained Glass Pane, none;none, &cEmpty Backpack Slot 8,  /&7&eLeft-click a backpack/&eitem on this slot to place/&eit!
|4, 9=Brown Stained Glass Pane, none;none, &cEmpty Backpack Slot 9,  /&7&eLeft-click a backpack/&eitem on this slot to place/&eit!
|-
|5, 1=Brown Stained Glass Pane, none;none, &cEmpty Backpack Slot 10,  /&7&eLeft-click a backpack/&eitem on this slot to place/&eit!
|5, 2=Brown Stained Glass Pane, none;none, &cEmpty Backpack Slot 11,  /&7&eLeft-click a backpack/&eitem on this slot to place/&eit!
|5, 3=Brown Stained Glass Pane, none;none, &cEmpty Backpack Slot 12,  /&7&eLeft-click a backpack/&eitem on this slot to place/&eit!
|5, 4=Brown Stained Glass Pane, none;none, &cEmpty Backpack Slot 13,  /&7&eLeft-click a backpack/&eitem on this slot to place/&eit!
|5, 5=Brown Stained Glass Pane, none;none, &cEmpty Backpack Slot 14,  /&7&eLeft-click a backpack/&eitem on this slot to place/&eit!
|5, 6=Brown Stained Glass Pane, none;none, &cEmpty Backpack Slot 15,  /&7&eLeft-click a backpack/&eitem on this slot to place/&eit!
|5, 7=Brown Stained Glass Pane, none;none, &cEmpty Backpack Slot 16,  /&7&eLeft-click a backpack/&eitem on this slot to place/&eit!
|5, 8=Brown Stained Glass Pane, none;none, &cEmpty Backpack Slot 17,  /&7&eLeft-click a backpack/&eitem on this slot to place/&eit!
|5, 9=Brown Stained Glass Pane, none;none, &cEmpty Backpack Slot 18,  /&7&eLeft-click a backpack/&eitem on this slot to place/&eit!
|id= storage
}}<!--
  ~~ ENDER CHEST 1 ~~
-->
{{UI|Ender Chest (1/9)
|1, 1=Close, none;none
|1, 2=Arrow, storage, &eBack, none
|1, 8=Next Page Icon, enderchest-two, &aNext Page →
|1, 9=Last Page Icon, enderchest-three, &eLast Page »
|row 1=Blank;3, 7
|id=enderchest-one
|return_id=storage
|noclose=true
|noarrow=true
|fill=false
|hide=true
}}<!--
  ~~ ENDER CHEST 2 ~~
-->
{{UI|Ender Chest (2/9)
|1, 1=Close, none;none
|1, 2=Arrow, storage, &eBack, none
|1, 6=First Page Icon, enderchest-one, &e« First Page
|1, 7=Previous Page Icon, enderchest-one, &a← Previous Page
|1, 8=Next Page Icon, enderchest-three, &aNext Page →
|1, 9=Last Page Icon, enderchest-three, &eLast Page »
|row 1=Blank;3, 5
|id=enderchest-two
|return_id=storage
|noclose=true
|noarrow=true
|fill=false
|hide=true
}}<!--
  ~~ ENDER CHEST 3 ~~  
-->
{{UI|Ender Chest (3/9)
|1, 1=Close, none;none
|1, 2=Arrow, storage, &eBack, none
|1, 6=First Page Icon, enderchest-one, &e« First Page
|1, 7=Previous Page Icon, enderchest-two, &a← Previous Page
|row 1=Blank;3, 4, 5, 8, 9
|id=enderchest-three
|return_id=storage
|noclose=true
|noarrow=true
|fill=false
|hide=true
}}<!--
  ~~ BACKPACK 1 ~~  
-->
{{UI|Jumbo Backpack (1/18)
|1, 1=Close, none;none
|1, 2=Arrow, storage, &eBack, none
|1, 8=Next Page Icon, backpack-two, &aNext Page →
|1, 9=Last Page Icon, backpack-five, &eLast Page »
|row 1=Blank;3, 7
|id=backpack-one
|return_id=storage
|noclose=true
|noarrow=true
|fill=false
|hide=true
}}<!--
  ~~ BACKPACK 2 ~~  
-->
{{UI|Greater Backpack (2/18)
|1, 1=Close, none;none
|1, 2=Arrow, storage, &eBack, none
|1, 6=First Page Icon, backpack-one, &e« First Page
|1, 7=Previous Page Icon, backpack-one, &a← Previous Page
|1, 8=Next Page Icon, backpack-three, &aNext Page →
|1, 9=Last Page Icon, backpack-five, &eLast Page »
|row 1=Blank;3, 5
|id=backpack-two
|return_id=storage
|noclose=true
|noarrow=true
|fill=false
|hide=true
|rows=5
}}<!--
  ~~ BACKPACK 3 ~~  
-->
{{UI|Large Backpack (3/18)
|1, 1=Close, none;none
|1, 2=Arrow, storage, &eBack, none
|1, 6=First Page Icon, backpack-one, &e« First Page
|1, 7=Previous Page Icon, backpack-two, &a← Previous Page
|1, 8=Next Page Icon, backpack-four, &aNext Page →
|1, 9=Last Page Icon, backpack-five, &eLast Page »
|row 1=Blank;3, 5
|id=backpack-three
|return_id=storage
|noclose=true
|noarrow=true
|fill=false
|hide=true
|rows=4
}}<!--
  ~~ BACKPACK 4 ~~  
-->
{{UI|Medium Backpack (4/18)
|1, 1=Close, none;none
|1, 2=Arrow, storage, &eBack, none
|1, 6=First Page Icon, backpack-one, &e« First Page
|1, 7=Previous Page Icon, backpack-three, &a← Previous Page
|1, 8=Next Page Icon, backpack-five, &aNext Page →
|1, 9=Last Page Icon, backpack-five, &eLast Page »
|row 1=Blank;3, 5
|id=backpack-four
|return_id=storage
|noclose=true
|noarrow=true
|fill=false
|hide=true
|rows=3
}}<!--
  ~~ BACKPACK 5 ~~  
-->
{{UI|Small Backpack (5/18)
|1, 1=Close, none;none
|1, 2=Arrow, storage, &eBack, none
|1, 6=First Page Icon, backpack-one, &e« First Page
|1, 7=Previous Page Icon, backpack-four, &a← Previous Page
|row 1=Blank;3, 4, 5, 8, 9
|id=backpack-five
|return_id=storage
|noclose=true
|noarrow=true
|fill=false
|hide=true
|rows=2
}}
</div>
</pre>
|id=storage}}
<div class="sbw-ui-tabber">
<!-- STORAGE -->
{{UI|Storage
|1, 5=Ender Chest, none;none, &aEnder Chest, &7Store global items you can/&7access anywhere in your/&7ender chest.
|-
|2, 1=Purple Stained Glass Pane, enderchest-one;none, &aEnder Chest Page 1, /&eLeft-click to open!/&eRight-click to change icon!
|2, 2=Purple Stained Glass Pane, enderchest-two;none, &aEnder Chest Page 2, /&eLeft-click to open!/&eRight-click to change icon!
|2, 3=Purple Stained Glass Pane, enderchest-three;none, &aEnder Chest Page 3, /&eLeft-click to open!/&eRight-click to change icon!
|row 2=Red Stained Glass Pane, none;none, &cLocked Page, &7Unlock more Ender Chest/&7pages in the community/&7shop!;4, 9
|-
|3, 5=Chest, none;none, &aBackpacks, &7Place backpack items in/&7these slots to use them as/&7additional storage that can/&7be accessed anywhere.
|-
|4, 1=Jumbo Backpack, backpack-one;none, &6Backpack Slot 1, &6Jumbo Backpack/&7&7This backpack has &a45&7/&7slots./ /&7&eLeft-click to open!/&7&eRight-click to remove!
|4, 2=Greater Backpack, backpack-two;none, &6Backpack Slot 2, &5Greater Backpack/&7&7This backpack has &a36&7/&7slots./ /&7&eLeft-click to open!/&7&eRight-click to remove!
|4, 3=Large Backpack, backpack-three;none, &6Backpack Slot 3, &5Large Backpack/&7&7This backpack has &a27&7/&7slots./ /&7&eLeft-click to open!/&7&eRight-click to remove!
|4, 4=Medium Backpack, backpack-four;none, &6Backpack Slot 4, &9Medium Backpack/&7&7This backpack has &a18&7/&7slots./ /&7&eLeft-click to open!/&7&eRight-click to remove!
|4, 5=Small Backpack, backpack-five;none, &6Backpack Slot 5, &aSmall Backpack/&7&7This backpack has &a9&7/&7slots./ /&7&eLeft-click to open!/&7&eRight-click to remove!
|4, 6=Brown Stained Glass Pane, none;none, &cEmpty Backpack Slot 6,  /&7&eLeft-click a backpack/&eitem on this slot to place/&eit!
|4, 7=Brown Stained Glass Pane, none;none, &cEmpty Backpack Slot 7,  /&7&eLeft-click a backpack/&eitem on this slot to place/&eit!
|4, 8=Brown Stained Glass Pane, none;none, &cEmpty Backpack Slot 8,  /&7&eLeft-click a backpack/&eitem on this slot to place/&eit!
|4, 9=Brown Stained Glass Pane, none;none, &cEmpty Backpack Slot 9,  /&7&eLeft-click a backpack/&eitem on this slot to place/&eit!
|-
|5, 1=Brown Stained Glass Pane, none;none, &cEmpty Backpack Slot 10,  /&7&eLeft-click a backpack/&eitem on this slot to place/&eit!
|5, 2=Brown Stained Glass Pane, none;none, &cEmpty Backpack Slot 11,  /&7&eLeft-click a backpack/&eitem on this slot to place/&eit!
|5, 3=Brown Stained Glass Pane, none;none, &cEmpty Backpack Slot 12,  /&7&eLeft-click a backpack/&eitem on this slot to place/&eit!
|5, 4=Brown Stained Glass Pane, none;none, &cEmpty Backpack Slot 13,  /&7&eLeft-click a backpack/&eitem on this slot to place/&eit!
|5, 5=Brown Stained Glass Pane, none;none, &cEmpty Backpack Slot 14,  /&7&eLeft-click a backpack/&eitem on this slot to place/&eit!
|5, 6=Brown Stained Glass Pane, none;none, &cEmpty Backpack Slot 15,  /&7&eLeft-click a backpack/&eitem on this slot to place/&eit!
|5, 7=Brown Stained Glass Pane, none;none, &cEmpty Backpack Slot 16,  /&7&eLeft-click a backpack/&eitem on this slot to place/&eit!
|5, 8=Brown Stained Glass Pane, none;none, &cEmpty Backpack Slot 17,  /&7&eLeft-click a backpack/&eitem on this slot to place/&eit!
|5, 9=Brown Stained Glass Pane, none;none, &cEmpty Backpack Slot 18,  /&7&eLeft-click a backpack/&eitem on this slot to place/&eit!
|id= storage
}}<!--
  ~~ ENDER CHEST 1 ~~
-->
{{UI|Ender Chest (1/9)
|1, 1=Close, none;none
|1, 2=Arrow, storage, &eBack, none
|1, 8=Next Page Icon, enderchest-two, &aNext Page →
|1, 9=Last Page Icon, enderchest-three, &eLast Page »
|row 1=Blank;3, 7
|id=enderchest-one
|return_id=storage
|noclose=true
|noarrow=true
|fill=false
|hide=true
}}<!--
  ~~ ENDER CHEST 2 ~~
-->
{{UI|Ender Chest (2/9)
|1, 1=Close, none;none
|1, 2=Arrow, storage, &eBack, none
|1, 6=First Page Icon, enderchest-one, &e« First Page
|1, 7=Previous Page Icon, enderchest-one, &a← Previous Page
|1, 8=Next Page Icon, enderchest-three, &aNext Page →
|1, 9=Last Page Icon, enderchest-three, &eLast Page »
|row 1=Blank;3, 5
|id=enderchest-two
|return_id=storage
|noclose=true
|noarrow=true
|fill=false
|hide=true
}}<!--
  ~~ ENDER CHEST 3 ~~  
-->
{{UI|Ender Chest (3/9)
|1, 1=Close, none;none
|1, 2=Arrow, storage, &eBack, none
|1, 6=First Page Icon, enderchest-one, &e« First Page
|1, 7=Previous Page Icon, enderchest-two, &a← Previous Page
|row 1=Blank;3, 4, 5, 8, 9
|id=enderchest-three
|return_id=storage
|noclose=true
|noarrow=true
|fill=false
|hide=true
}}<!--
  ~~ BACKPACK 1 ~~  
-->
{{UI|Jumbo Backpack (1/18)
|1, 1=Close, none;none
|1, 2=Arrow, storage, &eBack, none
|1, 8=Next Page Icon, backpack-two, &aNext Page →
|1, 9=Last Page Icon, backpack-five, &eLast Page »
|row 1=Blank;3, 7
|id=backpack-one
|return_id=storage
|noclose=true
|noarrow=true
|fill=false
|hide=true
}}<!--
  ~~ BACKPACK 2 ~~  
-->
{{UI|Greater Backpack (2/18)
|1, 1=Close, none;none
|1, 2=Arrow, storage, &eBack, none
|1, 6=First Page Icon, backpack-one, &e« First Page
|1, 7=Previous Page Icon, backpack-one, &a← Previous Page
|1, 8=Next Page Icon, backpack-three, &aNext Page →
|1, 9=Last Page Icon, backpack-five, &eLast Page »
|row 1=Blank;3, 5
|id=backpack-two
|return_id=storage
|noclose=true
|noarrow=true
|fill=false
|hide=true
|rows=5
}}<!--
  ~~ BACKPACK 3 ~~  
-->
{{UI|Large Backpack (3/18)
|1, 1=Close, none;none
|1, 2=Arrow, storage, &eBack, none
|1, 6=First Page Icon, backpack-one, &e« First Page
|1, 7=Previous Page Icon, backpack-two, &a← Previous Page
|1, 8=Next Page Icon, backpack-four, &aNext Page →
|1, 9=Last Page Icon, backpack-five, &eLast Page »
|row 1=Blank;3, 5
|id=backpack-three
|return_id=storage
|noclose=true
|noarrow=true
|fill=false
|hide=true
|rows=4
}}<!--
  ~~ BACKPACK 4 ~~  
-->
{{UI|Medium Backpack (4/18)
|1, 1=Close, none;none
|1, 2=Arrow, storage, &eBack, none
|1, 6=First Page Icon, backpack-one, &e« First Page
|1, 7=Previous Page Icon, backpack-three, &a← Previous Page
|1, 8=Next Page Icon, backpack-five, &aNext Page →
|1, 9=Last Page Icon, backpack-five, &eLast Page »
|row 1=Blank;3, 5
|id=backpack-four
|return_id=storage
|noclose=true
|noarrow=true
|fill=false
|hide=true
|rows=3
}}<!--
  ~~ BACKPACK 5 ~~  
-->
{{UI|Small Backpack (5/18)
|1, 1=Close, none;none
|1, 2=Arrow, storage, &eBack, none
|1, 6=First Page Icon, backpack-one, &e« First Page
|1, 7=Previous Page Icon, backpack-four, &a← Previous Page
|row 1=Blank;3, 4, 5, 8, 9
|id=backpack-five
|return_id=storage
|noclose=true
|noarrow=true
|fill=false
|hide=true
|rows=2
}}
</div>

=== [[Heart of the Mountain]] ===
{{Collapsible Section Button|Show/Hide Source Code|id=hotm}}
{{Collapsible Section
|<pre>
<div class="sbw-ui-tabber"><!--
  ~~ HOTM-one ~~
-->
{{UI|Heart Of the Mountain
|id=hotm-one

|{{Slot
|Lime Stained Glass Pane
|link=none 
|title=&aTier 5
|text={{UIText|&7You have unlocked this tier. All
perks and abilities on this tier 
are available for unlocking with
&5Token of the Mountain.

&8+&52 Token of the Mountain
&8+&6New Forgeable Items

&aUNLOCKED
}}}}
|{{Slot|Blank}}|{{Slot 
|Diamond
|link=none 
|title=&aGoblin Killer
|text={{UIText| 
&7Killing a &6Golden Goblin&7
gives &2200 &7extra &2Mithril 
Powder&7, while killing other
Goblins gives some based on 
their wits.

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot 
|Block of Redstone
|link=none 
|title=&aPeak of the Mountain
|text={{UIText| 
&7Level 5

&8+&c1 Pickaxe Ability Level
&8+&51 Token of the Mountain
&8+&a1 Forge Slot
&8+&a1 Commission Slot
&8+&21 Mithril Powder &7when
Mining Mithril.
&8+&51 Token of the Mountain

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot 
|Diamond
|link=none 
|title=&aStar Powder
|text={{UIText| 
&7Mining Mithril Ore near &5Fallen 
Crystals &7gives &a+3 &7extra Mithril
Powder

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot
|Scroll Up
|title=&aScroll Up
|text=&eLeft-click &7to scroll up!//&eRight-click &7to go to the top tier!
|image=Arrow
|class=goto-hotm-two
|link=none
}}
|-
|{{Slot 
|Lime Stained Glass Pane
|link=none 
|title=&aTier 4
|text={{UIText|&7You have unlocked this tier. All
perks and abilities on this tier 
are available for unlocking with
&5Token of the Mountain.

&7Rewards
&8+&52 Token of the Mountain
&8+&a1 Forge Slot
&8+&6New Forgeable Items

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aSky Mall
|text={{UIText| 
&7Every Project Seria Caveblock day, you receive
a random buff in the &2Dwarven Mines&7.

Possible Buffs
&8 ■ &7Gain &a+100 &6\stat{Mining Speed}
&8 ■ &7Gain &a+50 &6\stat{Mining Fortune}
&8 ■ &7Gain &a+15% &7Powder from mining
&8 ■ &7Reduce Pickaxe Ability cooldown
     &7by &a20%
&8 ■ &7&a10x &7chance to find Goblins
     &7while mining
&8 ■ &7Gain &a5x &9Titanium &7drops

&aUNLOCKED
}}}}
|{{Slot 
|Diamond 
|link=none 
|title=&aMining Madness
|text={{UIText| 
&7Grants &6+50 \stat{Mining Speed} &7and
&6Fortune&7.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aSeasoned Mineman
|text={{UIText| 
&7Level 100

&7Increases your mining experience
gain by &a15%&7.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aEfficient Miner
|text={{UIText| 
&7Level 100

&7When mining ores, you have a &a50%
&7chance to mine 6 adjacent ores.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aOrbiter
|text={{UIText| 
&7Level 80

&7When mining ores, you have a &a1%
&7chance to get a random amount of
experience orbs.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond 
|link=none 
|title=&aFront Loaded
|text={{UIText| 
&7Grants &a+100&7 \stat{Mining Speed} &7and 
&6Mining Fortune &7for the first 
1,000 ores you mine in a day.

&aUNLOCKED 
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aPrecision Mining 
|text={{UIText| 
&7When mining ore, a particle 
target appears on the block 
that increases your 
\stat{Mining Speed} &7by &a30% &7when
aiming at it.

&aUNLOCKED 
}}}}
|{{Slot|Blank}}
|-
|{{Slot
|Lime Stained Glass Pane
|link=none
|title=&aTier 3
|text={{UIText|&7You have unlocked this tier. All 
perks and abilities on this tier
are available for unlocking with
&5Token of the Mountain&7.

Rewards
&8+&52 Token of the Mountain
&8+&a1 Forge Slot
&8+&6New Forgeable Items

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot
|Diamond
|link=none
|title=&aLuck of the Cave
|text={{UIText|
&7Level 45

Increases the chance for you to
trigger rare occurrences in
&2Dwarven Mines &7by &a50%&7.

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot
|Diamond
|link=none
|title=&aDaily Powder
|text={{UIText|
&7Level 100

Gain &a3964 Powder&7 from
the first ore you mine every
day. Works for all Powder types.

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot
|Diamond
|link=none
|title=&aCrystallized
|text={{UIText|
&7Level 30

Grants &a+200 \stat{Mining Speed} 
&7and a &a200% &7chance to deal 
&a+1 &7extra damage near &5Fallen
Crystals&7.

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot|Blank}}
|-
|{{Slot
|Lime Stained Glass Pane
|link=none
|title=&aTier 2
|text={{UIText|&7You have unlocked this tier. All 
perks and abilities on this tier
are available for unlocking with
&5Token of the Mountain&7.

Rewards
&8+&52 Token of the Mountain
&6Access to the Forge
&8+&6New Forgeable Items

&aUNLOCKED 
}}}}
|{{Slot|Blank}}
|{{Slot
|Enchanted Emerald Block
|link=none
|title=&aMining Speed Boost
|text={{UIText|
&6Pickaxe Ability: Mining Speed Boost
&7Grants &a+300% \stat{Mining
Speed}&7 for &a20s&7.
&8Cooldown: &a 120s

&8Pickaxe Abilities apply to all
of your pickaxes. You can select
a Pickaxe Ability from your
Heart of the Mountain.

Upgrade your Pickaxe Abilities
by unlocking &c Peak of the
Mountain &8in this menu!

&aSELECTED
}}}}
|{{Slot
|Diamond
|link=none
|title=&aTitanium Insanium
|text={{UIText|
&7Level 50

When mining Mithril Ore, you
have a &a7%&7 chance to
convert the block into Titanium
Ore.

&aUNLOCKED
}}}}
|{{Slot
|Diamond
|link=none
|title=&aMining Fortune
|text={{UIText|
&7Level 50

Grants &a+250 \stat{Mining
Fortune}&7.

&aUNLOCKED
}}}}
|{{Slot
|Diamond
|link=none
|title=&aQuick Forge
|text={{UIText|
&7Level 20

Decrease the time it takes to 
forge by &a30%&7.

&aUNLOCKED
}}}}
|{{Slot
|Enchanted Emerald Block
|link=none
|title=&aPickobulus
|text={{UIText|
&6Pickaxe Ability: Pickobulus
&7Throw your pickaxe to create an 
explosion on impact, mining all
ores within a &a2 &7block radius.
&8Cooldown: &a110s

&8Pickaxe Abilities apply to all
of your pickaxes. You can select
a Pickaxe Ability from your
Heart of the Mountain.

Upgrade your Pickaxe Abilities
by unlocking &c Peak of the
Mountain &8in this menu!

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot|Blank}}
|-
|{{Slot
|Lime Stained Glass Pane
|link=none
|title=&aTier 1
|text={{UIText|&7You have unlocked this tier. All
perks and abilities on this tier
are available for unlocking with
&5Token of the Mountain&7.

Rewards
&8+&51 Token of the Mountain

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot|Blank}}
|{{Slot|Blank}}
|{{Slot
|Diamond
|link=none
|title=&aMining Speed
|text={{UIText|
&7Level 50

Grants &a+1000 &6 \stat{Mining
Speed}&7.

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot|Blank}}
|{{Slot|Blank}}
|{{Slot|Blank}}
|-
|{{Slot|Close}}
|{{Slot|Blank}}
|{{Slot|Blank}}
|{{Slot|arrow|title=&aGo Back|text=&7To Project Seria Caveblock Menu|link=none|class=goto-default}}
|{{Slot
|Heart of the Mountain
|link=none
|title=&5Heart of the Mountain
|text={{UIText|
&7Token of the Mountain: &50

&8Unlock more &5Token of the
Mountain &8by leveling up your
Heart of the Mountain tiers.

&9\u1805 Powder
Powders &8 are dropped from
mining ores in the &2Dwarven
Mines &8 and are used to upgrade
the perks you've unlocked!

&7Mithril Powder: &20
}}}}
|{{Slot|Crystal Hollows Crystals Icon|title=&5Crystal Hollows Crystals|text=&8Crystals are used to forge/Gems into &dPerfect &8Gems. They/can be found hidden within the/&5Crystal Hollows&8.//Find and place the full set of/&55 &8Crystals in the &5Crystal/Nucleus &8to unlock &6rare loot/chests&8!//&dYour &5Crystal Nucleus/　&aJade &c✖ Not Found/　&6Amber &c✖ Not Found/　&5Amethyst &c✖ Not Found/　&bSapphire &c✖ Not Found/　&eTopaz &c✖ Not Found//&dYour Other Crystals/　&dJasper &c✖ Not Found/　&cRuby &c✖ Not Found|link=Gemstone Crystals}}
|{{Slot|Blank}}
|{{Slot|Reset Heart of the Mountain
 |link=none
 |title=&cReset Heart of the Mountain
 |text={{UIText|
&7Resets the Perks and Abilities
of your &5Heart of the
Mountain&7, locking them 
and resetting their levels.

You will be reimbursed with all
of the &9Powder &7 and &5Token of
the Mountain &7that you have
spent.

You will &akeep &7any Tiers and 
&cPeak of the Mountain 
&7that you have unlocked.

Cost
&6100,000 Coins
&cYou can reset once every 24h.
}}}}
}}<!--
  ~~ HOTM-two ~~
-->
{{UI|Heart Of the Mountain
|id=hotm-two
|hide=true
|noarrow=true

|{{Slot
|Lime Stained Glass Pane
|link=none
|title=&aTier 6
|text={{UIText|&7You have unlocked this tier. All
perks and abilities on this tier 
are available for unlocking with
&5Token of the Mountain.

&8+&52 Token of the Mountain
&8+&6New Forgeable Items

&aUNLOCKED
}}}}
|{{Slot 
|Enchanted Emerald Block
|link=none 
|title=&aVein Seeker
|text={{UIText|
&6Pickaxe Ability: Vein Seeker
&7Points in the direction of the 
nearest vein and grants &a+2 
&6Mining Spread &7for &a12s&7.
&8Cooldown: &a 60s

&8Pickaxe Abilities apply to all
of your pickaxes. You can select
a Pickaxe Ability from your
Heart of the Mountain.

Upgrade your Pickaxe Abilities
by unlocking &c Peak of the
Mountain &8in this menu!

&aSELECTED
}}}}
|{{Slot 
|Diamond 
|link=none 
|title=&aLonesome Miner
|text={{UIText| 
&7Level 45

Increases &c❁ Strength, &9☣ Crit
Chance, ☠ Crit Damage, &a❈
Defense, and &c❤ Health
&7statistics gain by &a27%
&7while in the Crystal Hollows.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aProfessional
|text={{UIText| 
&7Level 140

&7Gain &a+750 &6⸕ Mining 
Speed &7when mining Gemstones.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aMole
|text={{UIText| 
&7Level 190

&7When mining hard stone, you have
a &a100% &7chance to mine &a10
&7adjacent hard stone blocks. 

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aFortunate
|text={{UIText| 
&7Level 20

&7Grants &a+100 &6☘ Mining 
Fortune &7when mining Gemstone.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond 
|link=none 
|title=&aGreat Explorer
|text={{UIText| 
&7Level 20

&7Grants &a+20% &7chance to
find treasure.

&aUNLOCKED 
}}}}
|{{Slot 
|Enchanted Emerald Block
|link=none 
|title=&aManiac Miner
|text={{UIText|
&6Pickaxe Ability: Maniac Miner
&7Spends all your Mana and grants
&a+1 \stat{Mining Speed} &7for 
every 10 Mana spent, for
&a12s&7.
&8Cooldown: &a 60s

&8Pickaxe Abilities apply to all
of your pickaxes. You can select
a Pickaxe Ability from your
Heart of the Mountain.

Upgrade your Pickaxe Abilities
by unlocking &c Peak of the
Mountain &8in this menu!

&aSELECTED
}}}}
|{{Slot
|Scroll Up
|title=&aScroll Up
|text=&eLeft-click &7to scroll up!//&eRight-click &7to go to the top tier!
|image=Arrow
|class=goto-hotm-three
|link=none
}}
|-
|{{Slot 
|Lime Stained Glass Pane
|link=none 
|title=&aTier 5
|text={{UIText|&7You have unlocked this tier. All
perks and abilities on this tier 
are available for unlocking with
&5Token of the Mountain.

&8+&52 Token of the Mountain
&8+&6New Forgeable Items

&aUNLOCKED
}}}}
|{{Slot|Blank}}|{{Slot 
|Diamond
|link=none 
|title=&aGoblin Killer
|text={{UIText| 
&7Killing a &6Golden Goblin&7
gives &2200 &7extra &2Mithril 
Powder&7, while killing other
Goblins gives some based on 
their wits.

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot 
|Block of Redstone
|link=none 
|title=&aPeak of the Mountain
|text={{UIText| 
&7Level 5

&8+&c1 Pickaxe Ability Level
&8+&51 Token of the Mountain
&8+&a1 Forge Slot
&8+&a1 Commission Slot
&8+&21 Mithril Powder &7when
Mining Mithril.
&8+&51 Token of the Mountain

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot 
|Diamond
|link=none 
|title=&aStar Powder
|text={{UIText| 
&7Mining Mithril Ore near &5Fallen 
Crystals &7gives &a+3 &7extra Mithril
Powder

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot|Blank}}
|-
|{{Slot 
|Lime Stained Glass Pane
|link=none 
|title=&aTier 4
|text={{UIText|&7You have unlocked this tier. All
perks and abilities on this tier 
are available for unlocking with
&5Token of the Mountain.

&7Rewards
&8+&52 Token of the Mountain
&8+&a1 Forge Slot
&8+&6New Forgeable Items

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aSky Mall
|text={{UIText| 
&7Every Project Seria Caveblock day, you receive
a random buff in the &2Dwarven Mines&7.

Possible Buffs
&8 ■ &7Gain &a+100 &6\stat{Mining Speed}
&8 ■ &7Gain &a+50 &6\stat{Mining Fortune}
&8 ■ &7Gain &a+15% &7Powder from mining
&8 ■ &7Reduce Pickaxe Ability cooldown
     &7by &a20%
&8 ■ &7&a10x &7chance to find Goblins
     &7while mining
&8 ■ &7Gain &a5x &9Titanium &7drops

&aUNLOCKED
}}}}
|{{Slot 
|Diamond 
|link=none 
|title=&aMining Madness
|text={{UIText| 
&7Grants &6+50 \stat{Mining Speed} &7and
&6Fortune&7.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aSeasoned Mineman
|text={{UIText| 
&7Level 100

&7Increases your mining experience
gain by &a15%&7.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aEfficient Miner
|text={{UIText| 
&7Level 100

&7When mining ores, you have a &a50%
&7chance to mine 6 adjacent ores.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aOrbiter
|text={{UIText| 
&7Level 80

&7When mining ores, you have a &a1%
&7chance to get a random amount of
experience orbs.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond 
|link=none 
|title=&aFront Loaded
|text={{UIText| 
&7Grants &a+100&7 \stat{Mining Speed} &7and 
&6Mining Fortune &7for the first 
1,000 ores you mine in a day.

&aUNLOCKED 
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aPrecision Mining 
|text={{UIText| 
&7When mining ore, a particle 
target appears on the block 
that increases your 
\stat{Mining Speed} &7by &a30% &7when
aiming at it.

&aUNLOCKED 
}}}}
|{{Slot|Blank}}
|-
|{{Slot
|Lime Stained Glass Pane
|link=none
|title=&aTier 3
|text={{UIText|&7You have unlocked this tier. All 
perks and abilities on this tier
are available for unlocking with
&5Token of the Mountain&7.

Rewards
&8+&52 Token of the Mountain
&8+&a1 Forge Slot
&8+&6New Forgeable Items

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot
|Diamond
|link=none
|title=&aLuck of the Cave
|text={{UIText|
&7Level 45

Increases the chance for you to
trigger rare occurrences in
&2Dwarven Mines &7by &a50%&7.

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot
|Diamond
|link=none
|title=&aDaily Powder
|text={{UIText|
&7Level 100

Gain &a3964 Powder&7 from
the first ore you mine every
day. Works for all Powder types.

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot
|Diamond
|link=none
|title=&aCrystallized
|text={{UIText|
&7Level 30

Grants &a+200 \stat{Mining Speed} 
&7and a &a200% &7chance to deal 
&a+1 &7extra damage near &5Fallen
Crystals&7.

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot|Blank}}
|-
|{{Slot
|Lime Stained Glass Pane
|link=none
|title=&aTier 2
|text={{UIText|&7You have unlocked this tier. All 
perks and abilities on this tier
are available for unlocking with
&5Token of the Mountain&7.

Rewards
&8+&52 Token of the Mountain
&6Access to the Forge
&8+&6New Forgeable Items

&aUNLOCKED 
}}}}
|{{Slot|Blank}}
|{{Slot
|Enchanted Emerald Block
|link=none
|title=&aMining Speed Boost
|text={{UIText|
&6Pickaxe Ability: Mining Speed Boost
&7Grants &a+300% \stat{Mining
Speed}&7 for &a20s&7.
&8Cooldown: &a 120s

&8Pickaxe Abilities apply to all
of your pickaxes. You can select
a Pickaxe Ability from your
Heart of the Mountain.

Upgrade your Pickaxe Abilities
by unlocking &c Peak of the
Mountain &8in this menu!

&aSELECTED
}}}}
|{{Slot
|Diamond
|link=none
|title=&aTitanium Insanium
|text={{UIText|
&7Level 50

When mining Mithril Ore, you
have a &a7%&7 chance to
convert the block into Titanium
Ore.

&aUNLOCKED
}}}}
|{{Slot
|Diamond
|link=none
|title=&aMining Fortune
|text={{UIText|
&7Level 50

Grants &a+250 \stat{Mining
Fortune}&7.

&aUNLOCKED
}}}}
|{{Slot
|Diamond
|link=none
|title=&aQuick Forge
|text={{UIText|
&7Level 20

Decrease the time it takes to 
forge by &a30%&7.

&aUNLOCKED
}}}}
|{{Slot
|Enchanted Emerald Block
|link=none
|title=&aPickobulus
|text={{UIText|
&6Pickaxe Ability: Pickobulus
&7Throw your pickaxe to create an 
explosion on impact, mining all
ores within a &a2 &7block radius.
&8Cooldown: &a110s

&8Pickaxe Abilities apply to all
of your pickaxes. You can select
a Pickaxe Ability from your
Heart of the Mountain.

Upgrade your Pickaxe Abilities
by unlocking &c Peak of the
Mountain &8in this menu!

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot|Blank}}
|-
|{{Slot|Close}}
|{{Slot|Blank}}
|{{Slot|Blank}}
|{{Slot|arrow|title=&aGo Back|text=&7To Project Seria Caveblock Menu|link=none|class=goto-default}}
|{{Slot
|Heart of the Mountain
|link=none
|title=&5Heart of the Mountain
|text={{UIText|
&7Token of the Mountain: &50

&8Unlock more &5Token of the
Mountain &8by leveling up your
Heart of the Mountain tiers.

&9\u1805 Powder
Powders &8 are dropped from
mining ores in the &2Dwarven
Mines &8 and are used to upgrade
the perks you've unlocked!

&7Mithril Powder: &20
}}}}
|{{Slot|Crystal Hollows Crystals Icon|title=&5Crystal Hollows Crystals|text=&8Crystals are used to forge/Gems into &dPerfect &8Gems. They/can be found hidden within the/&5Crystal Hollows&8.//Find and place the full set of/&55 &8Crystals in the &5Crystal/Nucleus &8to unlock &6rare loot/chests&8!//&dYour &5Crystal Nucleus/　&aJade &c✖ Not Found/　&6Amber &c✖ Not Found/　&5Amethyst &c✖ Not Found/　&bSapphire &c✖ Not Found/　&eTopaz &c✖ Not Found//&dYour Other Crystals/　&dJasper &c✖ Not Found/　&cRuby &c✖ Not Found|link=Gemstone Crystals}}
|{{Slot|Blank}}
|{{Slot|Reset Heart of the Mountain
 |link=none
 |title=&cReset Heart of the Mountain
 |text={{UIText|
&7Resets the Perks and Abilities
of your &5Heart of the
Mountain&7, locking them 
and resetting their levels.

You will be reimbursed with all
of the &9Powder &7 and &5Token of
the Mountain &7that you have
spent.

You will &akeep &7any Tiers and 
&cPeak of the Mountain 
&7that you have unlocked.

Cost
&6100,000 Coins
&cYou can reset once every 24h.
}}}}
|6, 9 = {{Slot|Scroll Down|title=&aScroll Down|text=&eLeft-click &7to scroll down!//&eRight-click &7to go to the bottom tier!|image=Arrow|class=goto-hotm-one|link=none}}
}}<!--
  ~~ HOTM-three ~~
-->
{{UI|Heart Of the Mountain
|id=hotm-three
|hide=true
|noarrow=true

|{{Slot
|Lime Stained Glass Pane
|link=none
|title=&aTier 7
|text={{UIText|&7You have unlocked this tier. All
perks and abilities on this tier
are available for unlocking with
&5Token of the Mountain&7.

&8+&52 Token of the Mountain
&8+&6New Forgeable Items

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot 
|Diamond 
|link=none 
|title=&aMining Speed II
|text={{UIText| 
&7Level 50

&7Grants &a+2000 &6⸕ Mining 
Speed&7.

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot 
|Diamond
|link=none 
|title=&aPowder Buff
|text={{UIText| 
&7Level 50

Gain &a50% &7more Mithril
Powder and Gemstone Powder.

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot 
|Diamond 
|link=none 
|title=&aMining Fortune II
|text={{UIText| 
&7Level 50

&7Grants &a+250 &6☘ Mining 
Fortune&7.

&aUNLOCKED 
}}}}
|{{Slot|Blank}}
|{{Slot|Blank}}
|-
|{{Slot
|Lime Stained Glass Pane
|link=none
|title=&aTier 6
|text={{UIText|&7You have unlocked this tier. All
perks and abilities on this tier 
are available for unlocking with
&5Token of the Mountain.

&8+&52 Token of the Mountain
&8+&6New Forgeable Items

&aUNLOCKED
}}}}
|{{Slot 
|Enchanted Emerald Block
|link=none 
|title=&aVein Seeker
|text={{UIText|
&6Pickaxe Ability: Vein Seeker
&7Points in the direction of the 
nearest vein and grants &a+2 
&6Mining Spread &7for &a12s&7.
&8Cooldown: &a 60s

&8Pickaxe Abilities apply to all
of your pickaxes. You can select
a Pickaxe Ability from your
Heart of the Mountain.

Upgrade your Pickaxe Abilities
by unlocking &c Peak of the
Mountain &8in this menu!

&aSELECTED
}}}}
|{{Slot 
|Diamond 
|link=none 
|title=&aLonesome Miner
|text={{UIText| 
&7Level 45

Increases &c❁ Strength, &9☣ Crit
Chance, ☠ Crit Damage, &a❈
Defense, and &c❤ Health
&7statistics gain by &a27%
&7while in the Crystal Hollows.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aProfessional
|text={{UIText| 
&7Level 140

&7Gain &a+750 &6⸕ Mining 
Speed &7when mining Gemstones.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aMole
|text={{UIText| 
&7Level 190

&7When mining hard stone, you have
a &a100% &7chance to mine &a10
&7adjacent hard stone blocks. 

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aFortunate
|text={{UIText| 
&7Level 20

&7Grants &a+100 &6☘ Mining 
Fortune &7when mining Gemstone.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond 
|link=none 
|title=&aGreat Explorer
|text={{UIText| 
&7Level 20

&7Grants &a+20% &7chance to
find treasure.

&aUNLOCKED 
}}}}
|{{Slot 
|Enchanted Emerald Block
|link=none 
|title=&aManiac Miner
|text={{UIText|
&6Pickaxe Ability: Maniac Miner
&7Spends all your Mana and grants
&a+1 \stat{Mining Speed} &7for 
every 10 Mana spent, for
&a12s&7.
&8Cooldown: &a 60s

&8Pickaxe Abilities apply to all
of your pickaxes. You can select
a Pickaxe Ability from your
Heart of the Mountain.

Upgrade your Pickaxe Abilities
by unlocking &c Peak of the
Mountain &8in this menu!

&aSELECTED
}}}}

|{{Slot|Blank}}
|-
|{{Slot 
|Lime Stained Glass Pane
|link=none 
|title=&aTier 5
|text={{UIText|&7You have unlocked this tier. All
perks and abilities on this tier 
are available for unlocking with
&5Token of the Mountain.

&8+&52 Token of the Mountain
&8+&6New Forgeable Items

&aUNLOCKED
}}}}
|{{Slot|Blank}}|{{Slot 
|Diamond
|link=none 
|title=&aGoblin Killer
|text={{UIText| 
&7Killing a &6Golden Goblin&7
gives &2200 &7extra &2Mithril 
Powder&7, while killing other
Goblins gives some based on 
their wits.

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot 
|Block of Redstone
|link=none 
|title=&aPeak of the Mountain
|text={{UIText| 
&7Level 5

&8+&c1 Pickaxe Ability Level
&8+&51 Token of the Mountain
&8+&a1 Forge Slot
&8+&a1 Commission Slot
&8+&21 Mithril Powder &7when
Mining Mithril.
&8+&51 Token of the Mountain

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot 
|Diamond
|link=none 
|title=&aStar Powder
|text={{UIText| 
&7Mining Mithril Ore near &5Fallen 
Crystals &7gives &a+3 &7extra Mithril
Powder

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot|Blank}}
|-
|{{Slot 
|Lime Stained Glass Pane
|link=none 
|title=&aTier 4
|text={{UIText|&7You have unlocked this tier. All
perks and abilities on this tier 
are available for unlocking with
&5Token of the Mountain.

&7Rewards
&8+&52 Token of the Mountain
&8+&a1 Forge Slot
&8+&6New Forgeable Items

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aSky Mall
|text={{UIText| 
&7Every Project Seria Caveblock day, you receive
a random buff in the &2Dwarven Mines&7.

Possible Buffs
&8 ■ &7Gain &a+100 &6\stat{Mining Speed}
&8 ■ &7Gain &a+50 &6\stat{Mining Fortune}
&8 ■ &7Gain &a+15% &7Powder from mining
&8 ■ &7Reduce Pickaxe Ability cooldown
     &7by &a20%
&8 ■ &7&a10x &7chance to find Goblins
     &7while mining
&8 ■ &7Gain &a5x &9Titanium &7drops

&aUNLOCKED
}}}}
|{{Slot 
|Diamond 
|link=none 
|title=&aMining Madness
|text={{UIText| 
&7Grants &6+50 \stat{Mining Speed} &7and
&6Fortune&7.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aSeasoned Mineman
|text={{UIText| 
&7Level 100

&7Increases your mining experience
gain by &a15%&7.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aEfficient Miner
|text={{UIText| 
&7Level 100

&7When mining ores, you have a &a50%
&7chance to mine 6 adjacent ores.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aOrbiter
|text={{UIText| 
&7Level 80

&7When mining ores, you have a &a1%
&7chance to get a random amount of
experience orbs.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond 
|link=none 
|title=&aFront Loaded
|text={{UIText| 
&7Grants &a+100&7 \stat{Mining Speed} &7and 
&6Mining Fortune &7for the first 
1,000 ores you mine in a day.

&aUNLOCKED 
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aPrecision Mining 
|text={{UIText| 
&7When mining ore, a particle 
target appears on the block 
that increases your 
\stat{Mining Speed} &7by &a30% &7when
aiming at it.

&aUNLOCKED 
}}}}
|{{Slot|Blank}}
|-
|{{Slot
|Lime Stained Glass Pane
|link=none
|title=&aTier 3
|text={{UIText|&7You have unlocked this tier. All 
perks and abilities on this tier
are available for unlocking with
&5Token of the Mountain&7.

Rewards
&8+&52 Token of the Mountain
&8+&a1 Forge Slot
&8+&6New Forgeable Items

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot
|Diamond
|link=none
|title=&aLuck of the Cave
|text={{UIText|
&7Level 45

Increases the chance for you to
trigger rare occurrences in
&2Dwarven Mines &7by &a50%&7.

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot
|Diamond
|link=none
|title=&aDaily Powder
|text={{UIText|
&7Level 100

Gain &a3964 Powder&7 from
the first ore you mine every
day. Works for all Powder types.

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot
|Diamond
|link=none
|title=&aCrystallized
|text={{UIText|
&7Level 30

Grants &a+200 \stat{Mining Speed} 
&7and a &a200% &7chance to deal 
&a+1 &7extra damage near &5Fallen
Crystals&7.

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot|Blank}}
|-
|{{Slot|Close}}
|{{Slot|Blank}}
|{{Slot|Blank}}
|{{Slot|arrow|title=&aGo Back|text=&7To Project Seria Caveblock Menu|link=none|class=goto-default}}
|{{Slot
|Heart of the Mountain
|link=none
|title=&5Heart of the Mountain
|text={{UIText|
&7Token of the Mountain: &50

&8Unlock more &5Token of the
Mountain &8by leveling up your
Heart of the Mountain tiers.

&9\u1805 Powder
Powders &8 are dropped from
mining ores in the &2Dwarven
Mines &8 and are used to upgrade
the perks you've unlocked!

&7Mithril Powder: &20
}}}}
|{{Slot|Crystal Hollows Crystals Icon|title=&5Crystal Hollows Crystals|text=&8Crystals are used to forge/Gems into &dPerfect &8Gems. They/can be found hidden within the/&5Crystal Hollows&8.//Find and place the full set of/&55 &8Crystals in the &5Crystal/Nucleus &8to unlock &6rare loot/chests&8!//&dYour &5Crystal Nucleus/　&aJade &c✖ Not Found/　&6Amber &c✖ Not Found/　&5Amethyst &c✖ Not Found/　&bSapphire &c✖ Not Found/　&eTopaz &c✖ Not Found//&dYour Other Crystals/　&dJasper &c✖ Not Found/　&cRuby &c✖ Not Found|link=Gemstone Crystals}}
|{{Slot|Blank}}
|{{Slot|Reset Heart of the Mountain
 |link=none
 |title=&cReset Heart of the Mountain
 |text={{UIText|
&7Resets the Perks and Abilities
of your &5Heart of the
Mountain&7, locking them 
and resetting their levels.

You will be reimbursed with all
of the &9Powder &7 and &5Token of
the Mountain &7that you have
spent.

You will &akeep &7any Tiers and 
&cPeak of the Mountain 
&7that you have unlocked.

Cost
&6100,000 Coins
&cYou can reset once every 24h.
}}}}
|6, 9 = {{Slot|Scroll Down|title=&aScroll Down|text=&eLeft-click &7to scroll down!//&eRight-click &7to go to the bottom tier!|image=Arrow|class=goto-hotm-two|link=none}}
}}
</pre>
|id=hotm}}
<div class="sbw-ui-tabber"><!--
  ~~ HOTM-one ~~
-->
{{UI|Heart Of the Mountain
|id=hotm-one

|{{Slot
|Lime Stained Glass Pane
|link=none 
|title=&aTier 5
|text={{UIText|&7You have unlocked this tier. All
perks and abilities on this tier 
are available for unlocking with
&5Token of the Mountain.

&8+&52 Token of the Mountain
&8+&6New Forgeable Items

&aUNLOCKED
}}}}
|{{Slot|Blank}}|{{Slot 
|Diamond
|link=none 
|title=&aGoblin Killer
|text={{UIText| 
&7Killing a &6Golden Goblin&7
gives &2200 &7extra &2Mithril 
Powder&7, while killing other
Goblins gives some based on 
their wits.

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot 
|Block of Redstone
|link=none 
|title=&aPeak of the Mountain
|text={{UIText| 
&7Level 5

&8+&c1 Pickaxe Ability Level
&8+&51 Token of the Mountain
&8+&a1 Forge Slot
&8+&a1 Commission Slot
&8+&21 Mithril Powder &7when
Mining Mithril.
&8+&51 Token of the Mountain

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot 
|Diamond
|link=none 
|title=&aStar Powder
|text={{UIText| 
&7Mining Mithril Ore near &5Fallen 
Crystals &7gives &a+3 &7extra Mithril
Powder

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot
|Scroll Up
|title=&aScroll Up
|text=&eLeft-click &7to scroll up!//&eRight-click &7to go to the top tier!
|image=Arrow
|class=goto-hotm-two
|link=none
}}
|-
|{{Slot 
|Lime Stained Glass Pane
|link=none 
|title=&aTier 4
|text={{UIText|&7You have unlocked this tier. All
perks and abilities on this tier 
are available for unlocking with
&5Token of the Mountain.

&7Rewards
&8+&52 Token of the Mountain
&8+&a1 Forge Slot
&8+&6New Forgeable Items

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aSky Mall
|text={{UIText| 
&7Every Project Seria Caveblock day, you receive
a random buff in the &2Dwarven Mines&7.

Possible Buffs
&8 ■ &7Gain &a+100 &6\stat{Mining Speed}
&8 ■ &7Gain &a+50 &6\stat{Mining Fortune}
&8 ■ &7Gain &a+15% &7Powder from mining
&8 ■ &7Reduce Pickaxe Ability cooldown
     &7by &a20%
&8 ■ &7&a10x &7chance to find Goblins
     &7while mining
&8 ■ &7Gain &a5x &9Titanium &7drops

&aUNLOCKED
}}}}
|{{Slot 
|Diamond 
|link=none 
|title=&aMining Madness
|text={{UIText| 
&7Grants &6+50 \stat{Mining Speed} &7and
&6Fortune&7.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aSeasoned Mineman
|text={{UIText| 
&7Level 100

&7Increases your mining experience
gain by &a15%&7.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aEfficient Miner
|text={{UIText| 
&7Level 100

&7When mining ores, you have a &a50%
&7chance to mine 6 adjacent ores.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aOrbiter
|text={{UIText| 
&7Level 80

&7When mining ores, you have a &a1%
&7chance to get a random amount of
experience orbs.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond 
|link=none 
|title=&aFront Loaded
|text={{UIText| 
&7Grants &a+100&7 \stat{Mining Speed} &7and 
&6Mining Fortune &7for the first 
1,000 ores you mine in a day.

&aUNLOCKED 
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aPrecision Mining 
|text={{UIText| 
&7When mining ore, a particle 
target appears on the block 
that increases your 
\stat{Mining Speed} &7by &a30% &7when
aiming at it.

&aUNLOCKED 
}}}}
|{{Slot|Blank}}
|-
|{{Slot
|Lime Stained Glass Pane
|link=none
|title=&aTier 3
|text={{UIText|&7You have unlocked this tier. All 
perks and abilities on this tier
are available for unlocking with
&5Token of the Mountain&7.

Rewards
&8+&52 Token of the Mountain
&8+&a1 Forge Slot
&8+&6New Forgeable Items

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot
|Diamond
|link=none
|title=&aLuck of the Cave
|text={{UIText|
&7Level 45

Increases the chance for you to
trigger rare occurrences in
&2Dwarven Mines &7by &a50%&7.

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot
|Diamond
|link=none
|title=&aDaily Powder
|text={{UIText|
&7Level 100

Gain &a3964 Powder&7 from
the first ore you mine every
day. Works for all Powder types.

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot
|Diamond
|link=none
|title=&aCrystallized
|text={{UIText|
&7Level 30

Grants &a+200 \stat{Mining Speed} 
&7and a &a200% &7chance to deal 
&a+1 &7extra damage near &5Fallen
Crystals&7.

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot|Blank}}
|-
|{{Slot
|Lime Stained Glass Pane
|link=none
|title=&aTier 2
|text={{UIText|&7You have unlocked this tier. All 
perks and abilities on this tier
are available for unlocking with
&5Token of the Mountain&7.

Rewards
&8+&52 Token of the Mountain
&6Access to the Forge
&8+&6New Forgeable Items

&aUNLOCKED 
}}}}
|{{Slot|Blank}}
|{{Slot
|Enchanted Emerald Block
|link=none
|title=&aMining Speed Boost
|text={{UIText|
&6Pickaxe Ability: Mining Speed Boost
&7Grants &a+300% \stat{Mining
Speed}&7 for &a20s&7.
&8Cooldown: &a 120s

&8Pickaxe Abilities apply to all
of your pickaxes. You can select
a Pickaxe Ability from your
Heart of the Mountain.

Upgrade your Pickaxe Abilities
by unlocking &c Peak of the
Mountain &8in this menu!

&aSELECTED
}}}}
|{{Slot
|Diamond
|link=none
|title=&aTitanium Insanium
|text={{UIText|
&7Level 50

When mining Mithril Ore, you
have a &a7%&7 chance to
convert the block into Titanium
Ore.

&aUNLOCKED
}}}}
|{{Slot
|Diamond
|link=none
|title=&aMining Fortune
|text={{UIText|
&7Level 50

Grants &a+250 \stat{Mining
Fortune}&7.

&aUNLOCKED
}}}}
|{{Slot
|Diamond
|link=none
|title=&aQuick Forge
|text={{UIText|
&7Level 20

Decrease the time it takes to 
forge by &a30%&7.

&aUNLOCKED
}}}}
|{{Slot
|Enchanted Emerald Block
|link=none
|title=&aPickobulus
|text={{UIText|
&6Pickaxe Ability: Pickobulus
&7Throw your pickaxe to create an 
explosion on impact, mining all
ores within a &a2 &7block radius.
&8Cooldown: &a110s

&8Pickaxe Abilities apply to all
of your pickaxes. You can select
a Pickaxe Ability from your
Heart of the Mountain.

Upgrade your Pickaxe Abilities
by unlocking &c Peak of the
Mountain &8in this menu!

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot|Blank}}
|-
|{{Slot
|Lime Stained Glass Pane
|link=none
|title=&aTier 1
|text={{UIText|&7You have unlocked this tier. All
perks and abilities on this tier
are available for unlocking with
&5Token of the Mountain&7.

Rewards
&8+&51 Token of the Mountain

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot|Blank}}
|{{Slot|Blank}}
|{{Slot
|Diamond
|link=none
|title=&aMining Speed
|text={{UIText|
&7Level 50

Grants &a+1000 &6 \stat{Mining
Speed}&7.

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot|Blank}}
|{{Slot|Blank}}
|{{Slot|Blank}}
|-
|{{Slot|Close}}
|{{Slot|Blank}}
|{{Slot|Blank}}
|{{Slot|arrow|title=&aGo Back|text=&7To Project Seria Caveblock Menu|link=none|class=goto-default}}
|{{Slot
|Heart of the Mountain
|link=none
|title=&5Heart of the Mountain
|text={{UIText|
&7Token of the Mountain: &50

&8Unlock more &5Token of the
Mountain &8by leveling up your
Heart of the Mountain tiers.

&9\u1805 Powder
Powders &8 are dropped from
mining ores in the &2Dwarven
Mines &8 and are used to upgrade
the perks you've unlocked!

&7Mithril Powder: &20
}}}}
|{{Slot|Crystal Hollows Crystals Icon|title=&5Crystal Hollows Crystals|text=&8Crystals are used to forge/Gems into &dPerfect &8Gems. They/can be found hidden within the/&5Crystal Hollows&8.//Find and place the full set of/&55 &8Crystals in the &5Crystal/Nucleus &8to unlock &6rare loot/chests&8!//&dYour &5Crystal Nucleus/　&aJade &c✖ Not Found/　&6Amber &c✖ Not Found/　&5Amethyst &c✖ Not Found/　&bSapphire &c✖ Not Found/　&eTopaz &c✖ Not Found//&dYour Other Crystals/　&dJasper &c✖ Not Found/　&cRuby &c✖ Not Found|link=Gemstone Crystals}}
|{{Slot|Blank}}
|{{Slot|Reset Heart of the Mountain
 |link=none
 |title=&cReset Heart of the Mountain
 |text={{UIText|
&7Resets the Perks and Abilities
of your &5Heart of the
Mountain&7, locking them 
and resetting their levels.

You will be reimbursed with all
of the &9Powder &7 and &5Token of
the Mountain &7that you have
spent.

You will &akeep &7any Tiers and 
&cPeak of the Mountain 
&7that you have unlocked.

Cost
&6100,000 Coins
&cYou can reset once every 24h.
}}}}
}}<!--
  ~~ HOTM-two ~~
-->
{{UI|Heart Of the Mountain
|id=hotm-two
|hide=true
|noarrow=true

|{{Slot
|Lime Stained Glass Pane
|link=none
|title=&aTier 6
|text={{UIText|&7You have unlocked this tier. All
perks and abilities on this tier 
are available for unlocking with
&5Token of the Mountain.

&8+&52 Token of the Mountain
&8+&6New Forgeable Items

&aUNLOCKED
}}}}
|{{Slot 
|Enchanted Emerald Block
|link=none 
|title=&aVein Seeker
|text={{UIText|
&6Pickaxe Ability: Vein Seeker
&7Points in the direction of the 
nearest vein and grants &a+2 
&6Mining Spread &7for &a12s&7.
&8Cooldown: &a 60s

&8Pickaxe Abilities apply to all
of your pickaxes. You can select
a Pickaxe Ability from your
Heart of the Mountain.

Upgrade your Pickaxe Abilities
by unlocking &c Peak of the
Mountain &8in this menu!

&aSELECTED
}}}}
|{{Slot 
|Diamond 
|link=none 
|title=&aLonesome Miner
|text={{UIText| 
&7Level 45

Increases &c❁ Strength, &9☣ Crit
Chance, ☠ Crit Damage, &a❈
Defense, and &c❤ Health
&7statistics gain by &a27%
&7while in the Crystal Hollows.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aProfessional
|text={{UIText| 
&7Level 140

&7Gain &a+750 &6⸕ Mining 
Speed &7when mining Gemstones.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aMole
|text={{UIText| 
&7Level 190

&7When mining hard stone, you have
a &a100% &7chance to mine &a10
&7adjacent hard stone blocks. 

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aFortunate
|text={{UIText| 
&7Level 20

&7Grants &a+100 &6☘ Mining 
Fortune &7when mining Gemstone.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond 
|link=none 
|title=&aGreat Explorer
|text={{UIText| 
&7Level 20

&7Grants &a+20% &7chance to
find treasure.

&aUNLOCKED 
}}}}
|{{Slot 
|Enchanted Emerald Block
|link=none 
|title=&aManiac Miner
|text={{UIText|
&6Pickaxe Ability: Maniac Miner
&7Spends all your Mana and grants
&a+1 \stat{Mining Speed} &7for 
every 10 Mana spent, for
&a12s&7.
&8Cooldown: &a 60s

&8Pickaxe Abilities apply to all
of your pickaxes. You can select
a Pickaxe Ability from your
Heart of the Mountain.

Upgrade your Pickaxe Abilities
by unlocking &c Peak of the
Mountain &8in this menu!

&aSELECTED
}}}}
|{{Slot
|Scroll Up
|title=&aScroll Up
|text=&eLeft-click &7to scroll up!//&eRight-click &7to go to the top tier!
|image=Arrow
|class=goto-hotm-three
|link=none
}}
|-
|{{Slot 
|Lime Stained Glass Pane
|link=none 
|title=&aTier 5
|text={{UIText|&7You have unlocked this tier. All
perks and abilities on this tier 
are available for unlocking with
&5Token of the Mountain.

&8+&52 Token of the Mountain
&8+&6New Forgeable Items

&aUNLOCKED
}}}}
|{{Slot|Blank}}|{{Slot 
|Diamond
|link=none 
|title=&aGoblin Killer
|text={{UIText| 
&7Killing a &6Golden Goblin&7
gives &2200 &7extra &2Mithril 
Powder&7, while killing other
Goblins gives some based on 
their wits.

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot 
|Block of Redstone
|link=none 
|title=&aPeak of the Mountain
|text={{UIText| 
&7Level 5

&8+&c1 Pickaxe Ability Level
&8+&51 Token of the Mountain
&8+&a1 Forge Slot
&8+&a1 Commission Slot
&8+&21 Mithril Powder &7when
Mining Mithril.
&8+&51 Token of the Mountain

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot 
|Diamond
|link=none 
|title=&aStar Powder
|text={{UIText| 
&7Mining Mithril Ore near &5Fallen 
Crystals &7gives &a+3 &7extra Mithril
Powder

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot|Blank}}
|-
|{{Slot 
|Lime Stained Glass Pane
|link=none 
|title=&aTier 4
|text={{UIText|&7You have unlocked this tier. All
perks and abilities on this tier 
are available for unlocking with
&5Token of the Mountain.

&7Rewards
&8+&52 Token of the Mountain
&8+&a1 Forge Slot
&8+&6New Forgeable Items

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aSky Mall
|text={{UIText| 
&7Every Project Seria Caveblock day, you receive
a random buff in the &2Dwarven Mines&7.

Possible Buffs
&8 ■ &7Gain &a+100 &6\stat{Mining Speed}
&8 ■ &7Gain &a+50 &6\stat{Mining Fortune}
&8 ■ &7Gain &a+15% &7Powder from mining
&8 ■ &7Reduce Pickaxe Ability cooldown
     &7by &a20%
&8 ■ &7&a10x &7chance to find Goblins
     &7while mining
&8 ■ &7Gain &a5x &9Titanium &7drops

&aUNLOCKED
}}}}
|{{Slot 
|Diamond 
|link=none 
|title=&aMining Madness
|text={{UIText| 
&7Grants &6+50 \stat{Mining Speed} &7and
&6Fortune&7.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aSeasoned Mineman
|text={{UIText| 
&7Level 100

&7Increases your mining experience
gain by &a15%&7.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aEfficient Miner
|text={{UIText| 
&7Level 100

&7When mining ores, you have a &a50%
&7chance to mine 6 adjacent ores.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aOrbiter
|text={{UIText| 
&7Level 80

&7When mining ores, you have a &a1%
&7chance to get a random amount of
experience orbs.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond 
|link=none 
|title=&aFront Loaded
|text={{UIText| 
&7Grants &a+100&7 \stat{Mining Speed} &7and 
&6Mining Fortune &7for the first 
1,000 ores you mine in a day.

&aUNLOCKED 
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aPrecision Mining 
|text={{UIText| 
&7When mining ore, a particle 
target appears on the block 
that increases your 
\stat{Mining Speed} &7by &a30% &7when
aiming at it.

&aUNLOCKED 
}}}}
|{{Slot|Blank}}
|-
|{{Slot
|Lime Stained Glass Pane
|link=none
|title=&aTier 3
|text={{UIText|&7You have unlocked this tier. All 
perks and abilities on this tier
are available for unlocking with
&5Token of the Mountain&7.

Rewards
&8+&52 Token of the Mountain
&8+&a1 Forge Slot
&8+&6New Forgeable Items

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot
|Diamond
|link=none
|title=&aLuck of the Cave
|text={{UIText|
&7Level 45

Increases the chance for you to
trigger rare occurrences in
&2Dwarven Mines &7by &a50%&7.

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot
|Diamond
|link=none
|title=&aDaily Powder
|text={{UIText|
&7Level 100

Gain &a3964 Powder&7 from
the first ore you mine every
day. Works for all Powder types.

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot
|Diamond
|link=none
|title=&aCrystallized
|text={{UIText|
&7Level 30

Grants &a+200 \stat{Mining Speed} 
&7and a &a200% &7chance to deal 
&a+1 &7extra damage near &5Fallen
Crystals&7.

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot|Blank}}
|-
|{{Slot
|Lime Stained Glass Pane
|link=none
|title=&aTier 2
|text={{UIText|&7You have unlocked this tier. All 
perks and abilities on this tier
are available for unlocking with
&5Token of the Mountain&7.

Rewards
&8+&52 Token of the Mountain
&6Access to the Forge
&8+&6New Forgeable Items

&aUNLOCKED 
}}}}
|{{Slot|Blank}}
|{{Slot
|Enchanted Emerald Block
|link=none
|title=&aMining Speed Boost
|text={{UIText|
&6Pickaxe Ability: Mining Speed Boost
&7Grants &a+300% \stat{Mining
Speed}&7 for &a20s&7.
&8Cooldown: &a 120s

&8Pickaxe Abilities apply to all
of your pickaxes. You can select
a Pickaxe Ability from your
Heart of the Mountain.

Upgrade your Pickaxe Abilities
by unlocking &c Peak of the
Mountain &8in this menu!

&aSELECTED
}}}}
|{{Slot
|Diamond
|link=none
|title=&aTitanium Insanium
|text={{UIText|
&7Level 50

When mining Mithril Ore, you
have a &a7%&7 chance to
convert the block into Titanium
Ore.

&aUNLOCKED
}}}}
|{{Slot
|Diamond
|link=none
|title=&aMining Fortune
|text={{UIText|
&7Level 50

Grants &a+250 \stat{Mining
Fortune}&7.

&aUNLOCKED
}}}}
|{{Slot
|Diamond
|link=none
|title=&aQuick Forge
|text={{UIText|
&7Level 20

Decrease the time it takes to 
forge by &a30%&7.

&aUNLOCKED
}}}}
|{{Slot
|Enchanted Emerald Block
|link=none
|title=&aPickobulus
|text={{UIText|
&6Pickaxe Ability: Pickobulus
&7Throw your pickaxe to create an 
explosion on impact, mining all
ores within a &a2 &7block radius.
&8Cooldown: &a110s

&8Pickaxe Abilities apply to all
of your pickaxes. You can select
a Pickaxe Ability from your
Heart of the Mountain.

Upgrade your Pickaxe Abilities
by unlocking &c Peak of the
Mountain &8in this menu!

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot|Blank}}
|-
|{{Slot|Close}}
|{{Slot|Blank}}
|{{Slot|Blank}}
|{{Slot|arrow|title=&aGo Back|text=&7To Project Seria Caveblock Menu|link=none|class=goto-default}}
|{{Slot
|Heart of the Mountain
|link=none
|title=&5Heart of the Mountain
|text={{UIText|
&7Token of the Mountain: &50

&8Unlock more &5Token of the
Mountain &8by leveling up your
Heart of the Mountain tiers.

&9\u1805 Powder
Powders &8 are dropped from
mining ores in the &2Dwarven
Mines &8 and are used to upgrade
the perks you've unlocked!

&7Mithril Powder: &20
}}}}
|{{Slot|Crystal Hollows Crystals Icon|title=&5Crystal Hollows Crystals|text=&8Crystals are used to forge/Gems into &dPerfect &8Gems. They/can be found hidden within the/&5Crystal Hollows&8.//Find and place the full set of/&55 &8Crystals in the &5Crystal/Nucleus &8to unlock &6rare loot/chests&8!//&dYour &5Crystal Nucleus/　&aJade &c✖ Not Found/　&6Amber &c✖ Not Found/　&5Amethyst &c✖ Not Found/　&bSapphire &c✖ Not Found/　&eTopaz &c✖ Not Found//&dYour Other Crystals/　&dJasper &c✖ Not Found/　&cRuby &c✖ Not Found|link=Gemstone Crystals}}
|{{Slot|Blank}}
|{{Slot|Reset Heart of the Mountain
 |link=none
 |title=&cReset Heart of the Mountain
 |text={{UIText|
&7Resets the Perks and Abilities
of your &5Heart of the
Mountain&7, locking them 
and resetting their levels.

You will be reimbursed with all
of the &9Powder &7 and &5Token of
the Mountain &7that you have
spent.

You will &akeep &7any Tiers and 
&cPeak of the Mountain 
&7that you have unlocked.

Cost
&6100,000 Coins
&cYou can reset once every 24h.
}}}}
|6, 9 = {{Slot|Scroll Down|title=&aScroll Down|text=&eLeft-click &7to scroll down!//&eRight-click &7to go to the bottom tier!|image=Arrow|class=goto-hotm-one|link=none}}
}}<!--
  ~~ HOTM-three ~~
-->
{{UI|Heart Of the Mountain
|id=hotm-three
|hide=true
|noarrow=true

|{{Slot
|Lime Stained Glass Pane
|link=none
|title=&aTier 7
|text={{UIText|&7You have unlocked this tier. All
perks and abilities on this tier
are available for unlocking with
&5Token of the Mountain&7.

&8+&52 Token of the Mountain
&8+&6New Forgeable Items

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot 
|Diamond 
|link=none 
|title=&aMining Speed II
|text={{UIText| 
&7Level 50

&7Grants &a+2000 &6⸕ Mining 
Speed&7.

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot 
|Diamond
|link=none 
|title=&aPowder Buff
|text={{UIText| 
&7Level 50

Gain &a50% &7more Mithril
Powder and Gemstone Powder.

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot 
|Diamond 
|link=none 
|title=&aMining Fortune II
|text={{UIText| 
&7Level 50

&7Grants &a+250 &6☘ Mining 
Fortune&7.

&aUNLOCKED 
}}}}
|{{Slot|Blank}}
|{{Slot|Blank}}
|-
|{{Slot
|Lime Stained Glass Pane
|link=none
|title=&aTier 6
|text={{UIText|&7You have unlocked this tier. All
perks and abilities on this tier 
are available for unlocking with
&5Token of the Mountain.

&8+&52 Token of the Mountain
&8+&6New Forgeable Items

&aUNLOCKED
}}}}
|{{Slot 
|Enchanted Emerald Block
|link=none 
|title=&aVein Seeker
|text={{UIText|
&6Pickaxe Ability: Vein Seeker
&7Points in the direction of the 
nearest vein and grants &a+2 
&6Mining Spread &7for &a12s&7.
&8Cooldown: &a 60s

&8Pickaxe Abilities apply to all
of your pickaxes. You can select
a Pickaxe Ability from your
Heart of the Mountain.

Upgrade your Pickaxe Abilities
by unlocking &c Peak of the
Mountain &8in this menu!

&aSELECTED
}}}}
|{{Slot 
|Diamond 
|link=none 
|title=&aLonesome Miner
|text={{UIText| 
&7Level 45

Increases &c❁ Strength, &9☣ Crit
Chance, ☠ Crit Damage, &a❈
Defense, and &c❤ Health
&7statistics gain by &a27%
&7while in the Crystal Hollows.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aProfessional
|text={{UIText| 
&7Level 140

&7Gain &a+750 &6⸕ Mining 
Speed &7when mining Gemstones.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aMole
|text={{UIText| 
&7Level 190

&7When mining hard stone, you have
a &a100% &7chance to mine &a10
&7adjacent hard stone blocks. 

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aFortunate
|text={{UIText| 
&7Level 20

&7Grants &a+100 &6☘ Mining 
Fortune &7when mining Gemstone.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond 
|link=none 
|title=&aGreat Explorer
|text={{UIText| 
&7Level 20

&7Grants &a+20% &7chance to
find treasure.

&aUNLOCKED 
}}}}
|{{Slot 
|Enchanted Emerald Block
|link=none 
|title=&aManiac Miner
|text={{UIText|
&6Pickaxe Ability: Maniac Miner
&7Spends all your Mana and grants
&a+1 \stat{Mining Speed} &7for 
every 10 Mana spent, for
&a12s&7.
&8Cooldown: &a 60s

&8Pickaxe Abilities apply to all
of your pickaxes. You can select
a Pickaxe Ability from your
Heart of the Mountain.

Upgrade your Pickaxe Abilities
by unlocking &c Peak of the
Mountain &8in this menu!

&aSELECTED
}}}}

|{{Slot|Blank}}
|-
|{{Slot 
|Lime Stained Glass Pane
|link=none 
|title=&aTier 5
|text={{UIText|&7You have unlocked this tier. All
perks and abilities on this tier 
are available for unlocking with
&5Token of the Mountain.

&8+&52 Token of the Mountain
&8+&6New Forgeable Items

&aUNLOCKED
}}}}
|{{Slot|Blank}}|{{Slot 
|Diamond
|link=none 
|title=&aGoblin Killer
|text={{UIText| 
&7Killing a &6Golden Goblin&7
gives &2200 &7extra &2Mithril 
Powder&7, while killing other
Goblins gives some based on 
their wits.

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot 
|Block of Redstone
|link=none 
|title=&aPeak of the Mountain
|text={{UIText| 
&7Level 5

&8+&c1 Pickaxe Ability Level
&8+&51 Token of the Mountain
&8+&a1 Forge Slot
&8+&a1 Commission Slot
&8+&21 Mithril Powder &7when
Mining Mithril.
&8+&51 Token of the Mountain

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot 
|Diamond
|link=none 
|title=&aStar Powder
|text={{UIText| 
&7Mining Mithril Ore near &5Fallen 
Crystals &7gives &a+3 &7extra Mithril
Powder

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot|Blank}}
|-
|{{Slot 
|Lime Stained Glass Pane
|link=none 
|title=&aTier 4
|text={{UIText|&7You have unlocked this tier. All
perks and abilities on this tier 
are available for unlocking with
&5Token of the Mountain.

&7Rewards
&8+&52 Token of the Mountain
&8+&a1 Forge Slot
&8+&6New Forgeable Items

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aSky Mall
|text={{UIText| 
&7Every Project Seria Caveblock day, you receive
a random buff in the &2Dwarven Mines&7.

Possible Buffs
&8 ■ &7Gain &a+100 &6\stat{Mining Speed}
&8 ■ &7Gain &a+50 &6\stat{Mining Fortune}
&8 ■ &7Gain &a+15% &7Powder from mining
&8 ■ &7Reduce Pickaxe Ability cooldown
     &7by &a20%
&8 ■ &7&a10x &7chance to find Goblins
     &7while mining
&8 ■ &7Gain &a5x &9Titanium &7drops

&aUNLOCKED
}}}}
|{{Slot 
|Diamond 
|link=none 
|title=&aMining Madness
|text={{UIText| 
&7Grants &6+50 \stat{Mining Speed} &7and
&6Fortune&7.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aSeasoned Mineman
|text={{UIText| 
&7Level 100

&7Increases your mining experience
gain by &a15%&7.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aEfficient Miner
|text={{UIText| 
&7Level 100

&7When mining ores, you have a &a50%
&7chance to mine 6 adjacent ores.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aOrbiter
|text={{UIText| 
&7Level 80

&7When mining ores, you have a &a1%
&7chance to get a random amount of
experience orbs.

&aUNLOCKED
}}}}
|{{Slot 
|Diamond 
|link=none 
|title=&aFront Loaded
|text={{UIText| 
&7Grants &a+100&7 \stat{Mining Speed} &7and 
&6Mining Fortune &7for the first 
1,000 ores you mine in a day.

&aUNLOCKED 
}}}}
|{{Slot 
|Diamond
|link=none 
|title=&aPrecision Mining 
|text={{UIText| 
&7When mining ore, a particle 
target appears on the block 
that increases your 
\stat{Mining Speed} &7by &a30% &7when
aiming at it.

&aUNLOCKED 
}}}}
|{{Slot|Blank}}
|-
|{{Slot
|Lime Stained Glass Pane
|link=none
|title=&aTier 3
|text={{UIText|&7You have unlocked this tier. All 
perks and abilities on this tier
are available for unlocking with
&5Token of the Mountain&7.

Rewards
&8+&52 Token of the Mountain
&8+&a1 Forge Slot
&8+&6New Forgeable Items

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot
|Diamond
|link=none
|title=&aLuck of the Cave
|text={{UIText|
&7Level 45

Increases the chance for you to
trigger rare occurrences in
&2Dwarven Mines &7by &a50%&7.

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot
|Diamond
|link=none
|title=&aDaily Powder
|text={{UIText|
&7Level 100

Gain &a3964 Powder&7 from
the first ore you mine every
day. Works for all Powder types.

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot
|Diamond
|link=none
|title=&aCrystallized
|text={{UIText|
&7Level 30

Grants &a+200 \stat{Mining Speed} 
&7and a &a200% &7chance to deal 
&a+1 &7extra damage near &5Fallen
Crystals&7.

&aUNLOCKED
}}}}
|{{Slot|Blank}}
|{{Slot|Blank}}
|-
|{{Slot|Close}}
|{{Slot|Blank}}
|{{Slot|Blank}}
|{{Slot|arrow|title=&aGo Back|text=&7To Project Seria Caveblock Menu|link=none|class=goto-default}}
|{{Slot
|Heart of the Mountain
|link=none
|title=&5Heart of the Mountain
|text={{UIText|
&7Token of the Mountain: &50

&8Unlock more &5Token of the
Mountain &8by leveling up your
Heart of the Mountain tiers.

&9\u1805 Powder
Powders &8 are dropped from
mining ores in the &2Dwarven
Mines &8 and are used to upgrade
the perks you've unlocked!

&7Mithril Powder: &20
}}}}
|{{Slot|Crystal Hollows Crystals Icon|title=&5Crystal Hollows Crystals|text=&8Crystals are used to forge/Gems into &dPerfect &8Gems. They/can be found hidden within the/&5Crystal Hollows&8.//Find and place the full set of/&55 &8Crystals in the &5Crystal/Nucleus &8to unlock &6rare loot/chests&8!//&dYour &5Crystal Nucleus/　&aJade &c✖ Not Found/　&6Amber &c✖ Not Found/　&5Amethyst &c✖ Not Found/　&bSapphire &c✖ Not Found/　&eTopaz &c✖ Not Found//&dYour Other Crystals/　&dJasper &c✖ Not Found/　&cRuby &c✖ Not Found|link=Gemstone Crystals}}
|{{Slot|Blank}}
|{{Slot|Reset Heart of the Mountain
 |link=none
 |title=&cReset Heart of the Mountain
 |text={{UIText|
&7Resets the Perks and Abilities
of your &5Heart of the
Mountain&7, locking them 
and resetting their levels.

You will be reimbursed with all
of the &9Powder &7 and &5Token of
the Mountain &7that you have
spent.

You will &akeep &7any Tiers and 
&cPeak of the Mountain 
&7that you have unlocked.

Cost
&6100,000 Coins
&cYou can reset once every 24h.
}}}}
|6, 9 = {{Slot|Scroll Down|title=&aScroll Down|text=&eLeft-click &7to scroll down!//&eRight-click &7to go to the bottom tier!|image=Arrow|class=goto-hotm-two|link=none}}
}}
</div>

== See Also ==
{{FeatureSet/UI}}

<!-- Place template categories here -->
<includeonly>
[[Category:UI Templates]]
</includeonly>
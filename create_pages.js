const fs = require('fs');
const path = require('path');

const pages = {
    'Wheat.md': `{{Infobox item
|id = WHEAT
|rarity = common
|sell = 1
}}
'''Wheat''' is a {{R|C}} item found when harvesting crops in [[Chuville]] or using a [[Wheat Minion]].

It is a primary ingredient in many farming recipes.

== Collection ==
Collecting Wheat increases the player's Wheat [[Collection/List|Collection]], which grants useful items and perks upon collecting certain amounts of Wheat.

{{CollectionTable|Wheat}}

[[Category:Farming]]
[[Category:Items]]`,

    'Wheat_Minion.md': `{{Infobox item
|id = WHEAT_MINION
|rarity = common
}}
'''Wheat Minion''' is a Minion that produces [[Wheat]] and [[Wheat Seeds]]. 

It can be placed on a player's private island to automate the collection of Wheat.

[[Category:Minions]]`,

    'Chuville.md': `'''Chuville''' is a Farming Area where players can harvest various crops such as [[Wheat]], [[Carrot]], [[Potato]], and [[Beetroot]].

Players can access this zone once they reach the required tier in their farming collections or quests.

[[Category:Zones]]`,

    'Trade.md': `'''Trade''' (or Trades) is a system where players can exchange certain items for other items, such as exchanging [[Wheat Seeds]] for [[Dirt]] or [[Clay]].

[[Category:Mechanics]]`,

    'Dirt.md': `{{Infobox item
|id = DIRT
|rarity = common
|sell = 1
}}
'''Dirt''' is a {{R|C}} block that can be obtained through [[Trade|Trading]] or mining on the private island. 

It is primarily used for building and expanding farms.

[[Category:Blocks]]
[[Category:Items]]`,

    'Clay.md': `{{Infobox item
|id = CLAY_BALL
|rarity = common
|sell = 2
}}
'''Clay''' is a {{R|C}} item that can be obtained through [[Trade|Trading]] or fishing.

It is used to craft blocks and other items.

[[Category:Items]]`
};

for (const [filename, content] of Object.entries(pages)) {
    fs.writeFileSync(path.join('e:/Project Wiki/wiki', filename), content);
}
console.log("Pages created successfully.");

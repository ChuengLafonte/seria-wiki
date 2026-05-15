= SeriaCollection =

'''SeriaCollection''' is a custom progression system where players earn rewards by gathering specific resources. Each resource belongs to a category (Foraging, Farming, or Mining) and has multiple tiers of progression.

== How It Works ==
As you break blocks (logs, crops, ores), you earn points for that specific collection. Reaching a certain milestone unlocks a new '''Tier'''.

=== Tiers & Rewards ===
Unlocking tiers provides various benefits:
* '''Stat Boosts''': Permanent increases to stats like Foraging Fortune, Farming Fortune, or Mining Fortune.
* '''Recipes''': Unlock custom crafting recipes for armor, tools, and magical items.
* '''Area Access''': Some tiers grant permission to enter exclusive farming or foraging zones.
* '''Minions''': Unlock the ability to craft and use Minions for that specific resource.

== Features & Integrations ==

=== 🤖 TopMinion Integration ===
SeriaCollection is now fully integrated with the **TopMinion** plugin. 
* '''Automatic Tracking''': Items withdrawn from Minion inventories are automatically counted towards your collection progress.
* '''Anti-Exploit''': A robust "taint" system prevents players from double-counting items by dropping and re-picking them up or moving them between inventories.

=== 📊 PlaceholderAPI Support ===
You can use the following placeholders in menus, chat, or other plugins:
* `%seriacollection_level_<id>%`: Current level/tier of the collection.
* `%seriacollection_amount_<id>%`: Total amount collected.
* `%seriacollection_progress_bar_<id>%`: A visual progress bar for the current tier.
* `%seriacollection_percent_<id>%`: Percentage completion towards the next tier.
* `%seriacollection_requirement_<id>%`: Amount needed for the next tier.
* `%seriacollection_name_<id>%`: Display name of the collection.

== Collection Categories ==

=== 🪓 Foraging ===
Focuses on gathering different types of wood.
* '''Oak Wood''': Includes rewards like the ''Woodcutter Axe'' and ''Oak Guardian Set''.
* '''Birch Wood''': Unlocks the ''Birch Bark Cleaver'' and ''Silver Log Slicer''.
* '''Acacia Wood''': Grants access to the ''Savannah Scout Set''.
* '''Spruce Wood''': Includes the ''Taiga Frost Blade'' and ''Spruce Sentinel Set''.

=== 🌾 Farming ===
Focuses on crops and agriculture.
* '''Wheat''': Unlocks ''Farmer Hoes'' and access to the '''Chuville''' farming area at Tier 6.
* '''Potato''': Provides the ''Potato Suit'' and ''Mystic Hoes''.
* '''Carrot''': Unlocks ''Constellation Hoes'' and enchanted food recipes.

=== ⛏ Mining ===
Focuses on ores and minerals.
* '''Coal''': The entry-level mining collection, providing early-game gear and fortune boosts.
* (More mining collections coming soon!)

== Configuration ==
The plugin now supports **Dynamic Folder Loading**:
* All `.yml` files located in the `/collections/` folder are automatically loaded.
* You can organize your collections into separate files (e.g., `farming.yml`, `mining.yml`) for better management.
* Collection IDs are now '''case-insensitive''', making configuration more flexible.

[[Category:Features]]
[[Category:Progress]]
[[Category:Integrations]]

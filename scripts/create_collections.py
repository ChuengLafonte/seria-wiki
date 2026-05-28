import os

pages = {
    "Collections_SLASH_UI.md": """{{UI Tips|back=[[Caveblock Menu/UI]]}}

{{UI|Seria Collection
|id=collection-default

|2,5 = Painting, none;Collection-ranked, &aCollection, &7View all of the items available/&7in Caveblock. Collect more of an/&7item to unlock rewards on your/&7way to mastering Caveblock!//&7Collections Unlocked: &e0&6%/&f-------------------- &e0&6\/&e6//&eClick to show rankings!
|3,5 = Spruce Sapling, none;Foraging/Collection UI, &aForaging Collections, &7View your Foraging Collections!//&7Collections Unlocked: &e0&6%/&f-------------------- &e0&6\/&e6//&eClick to view!
|4,3 = Wheat, none;Farming/Collection UI, &aFarming Collections, &7View your Farming Collections!//&7Collections Unlocked: &e0&6%/&f-------------------- &e0&6\/&e4//&eClick to view!
|4,4 = Diamond, none;Mining/Collection UI, &aMining Collections, &7View your Mining Collections!//&7Collections Unlocked: &e0&6%/&f-------------------- &e0&6\/&e9//&eClick to view!
|4,5 = Iron Sword, none;Combat/Collection UI, &aCombat Collections, &7View your Combat Collections!//&7Collections Unlocked: &e0&6%/&f-------------------- &e0&6\/&e11//&eClick to view!
|4,6 = Clownfish, none;Fishing/Collection UI, &aFishing Collections, &7View your Fishing Collections!//&7Collections Unlocked: &e0&6%/&f-------------------- &e0&6\/&e4//&eClick to view!
|4,7 = Sand, none;Excavating/Collection UI, &aExcavating Collections, &7View your Excavating Collections!//&7Collections Unlocked: &e0&6%/&f-------------------- &e0&6\/&e3//&eClick to view!
|5,5 = Wither Skeleton Skull, none;Bosses/Collection UI, &aBoss Collections, &7View your Boss Collections!//&7Collections Unlocked: &e0&6%/&f-------------------- &e0&6\/&e8//&eClick to view!
|6,5 = Barrier, none;Caveblock Menu/UI, &cClose
}}

<includeonly>[[Category:Pages with UIs]]</includeonly>
<noinclude>[[Category:UI Subpages]]</noinclude>
""",
    "Collection-ranked.md": """{{UI Tips|back=[[Collections/UI]]}}

{{UI|Seria Collection
|id=collection-ranked

|2,5 = Painting, none;Collections/UI, &aCollection, &7View all of the items available/&7in Caveblock. Collect more of an/&7item to unlock rewards on your/&7way to mastering Caveblock!//&7Collection Unlocked: &e0&6%/&f-------------------- &e0&6\/&e6
|3,5 = Enchanted Spruce Sapling, none;Foraging/Collection UI, &b&oForaging Collections, &7View your Foraging Collections!//&7Collections Unlocked: &e0&6%/&f-------------------- &e0&6\/&e6//&8No unlocked collections for rankings.//&eClick to view!
|4,3 = Enchanted Hay Bale, none;Farming/Collection UI, &b&oFarming Collections, &7View your Farming Collections!//&7Collections Unlocked: &e0&6%/&f-------------------- &e0&6\/&e4//&8No unlocked collections for rankings.//&eClick to view!
|4,4 = Enchanted Diamond, none;Mining/Collection UI, &b&oMining Collections, &7View your Mining Collections!//&7Collections Unlocked: &e0&6%/&f-------------------- &e0&6\/&e9//&8No unlocked collections for rankings.//&eClick to view!
|4,5 = Enchanted Iron Sword, none;Combat/Collection UI, &b&oCombat Collections, &7View your Combat Collections!//&7Collections Unlocked: &e0&6%/&f-------------------- &e0&6\/&e11//&8No unlocked collections for rankings.//&eClick to view!
|4,6 = Enchanted Clownfish, none;Fishing/Collection UI, &b&oFishing Collections, &7View your Fishing Collections!//&7Collections Unlocked: &e0&6%/&f-------------------- &e0&6\/&e4//&8No unlocked collections for rankings.//&eClick to view!
|4,7 = Enchanted Sand, none;Excavating/Collection UI, &b&oExcavating Collections, &7View your Excavating Collections!//&7Collections Unlocked: &e0&6%/&f-------------------- &e0&6\/&e3//&8No unlocked collections for rankings.//&eClick to view!
|5,5 = Wither Skeleton Skull, none;Bosses/Collection UI, &b&oBoss Collections, &7View your Boss Collections!//&7Collections Unlocked: &e0&6%/&f-------------------- &e0&6\/&e8//&8No unlocked collections for rankings.//&eClick to view!
|6,5 = Barrier, none;Caveblock Menu/UI, &cClose
}}

<includeonly>[[Category:Pages with UIs]]</includeonly>
<noinclude>[[Category:UI Subpages]]</noinclude>
""",
    "Farming_SLASH_Collection UI.md": """{{UI Tips|back=[[Collections/UI]]}}

{{UI|Farming
|id=collection-farming

|1,5 = Wheat, none;none, &aWheat, &7View your Wheat Collection progress.
|goback = none;Collections/UI
|return_id = collection-default
}}

<includeonly>[[Category:Pages with UIs]]</includeonly>
<noinclude>[[Category:UI Subpages]]</noinclude>
""",
    "Mining_SLASH_Collection UI.md": """{{UI Tips|back=[[Collections/UI]]}}

{{UI|Mining
|id=collection-mining

|1,5 = Diamond, none;none, &aDiamond, &7View your Diamond Collection progress.
|goback = none;Collections/UI
|return_id = collection-default
}}

<includeonly>[[Category:Pages with UIs]]</includeonly>
<noinclude>[[Category:UI Subpages]]</noinclude>
""",
    "Foraging_SLASH_Collection UI.md": """{{UI Tips|back=[[Collections/UI]]}}

{{UI|Foraging
|id=collection-foraging

|1,5 = Spruce Sapling, none;none, &aSpruce, &7View your Spruce Collection progress.
|goback = none;Collections/UI
|return_id = collection-default
}}

<includeonly>[[Category:Pages with UIs]]</includeonly>
<noinclude>[[Category:UI Subpages]]</noinclude>
""",
    "Combat_SLASH_Collection UI.md": """{{UI Tips|back=[[Collections/UI]]}}

{{UI|Combat
|id=collection-combat

|1,5 = Iron Sword, none;none, &aIron Sword, &7View your Combat Collection progress.
|goback = none;Collections/UI
|return_id = collection-default
}}

<includeonly>[[Category:Pages with UIs]]</includeonly>
<noinclude>[[Category:UI Subpages]]</noinclude>
""",
    "Fishing_SLASH_Collection UI.md": """{{UI Tips|back=[[Collections/UI]]}}

{{UI|Fishing
|id=collection-fishing

|1,5 = Clownfish, none;none, &aClownfish, &7View your Fishing Collection progress.
|goback = none;Collections/UI
|return_id = collection-default
}}

<includeonly>[[Category:Pages with UIs]]</includeonly>
<noinclude>[[Category:UI Subpages]]</noinclude>
""",
    "Excavating_SLASH_Collection UI.md": """{{UI Tips|back=[[Collections/UI]]}}

{{UI|Excavating
|id=collection-excavating

|1,5 = Sand, none;none, &aSand, &7View your Excavating Collection progress.
|goback = none;Collections/UI
|return_id = collection-default
}}

<includeonly>[[Category:Pages with UIs]]</includeonly>
<noinclude>[[Category:UI Subpages]]</noinclude>
""",
    "Bosses_SLASH_Collection UI.md": """{{UI Tips|back=[[Collections/UI]]}}

{{UI|Bosses
|id=collection-bosses

|1,5 = Wither Skeleton Skull, none;none, &aWither Skeleton, &7View your Boss Collection progress.
|goback = none;Collections/UI
|return_id = collection-default
}}

<includeonly>[[Category:Pages with UIs]]</includeonly>
<noinclude>[[Category:UI Subpages]]</noinclude>
"""
}

os.makedirs('wiki', exist_ok=True)
for name, content in pages.items():
    path = os.path.join('wiki', name)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created {path}")


<infobox theme="seria" layout="stacked">
    <title source="title">
        <default>{{PAGENAME}}</default>
    </title>
    
    <image source="image">
        <default>[[File:{{PAGENAME}}.png|200px]]</default>
    </image>

    <!-- Basic Information -->
    <group>
        <data source="aka">
            <label>Also known as</label>
        </data>
        <data source="type">
            <label>Type</label>
            <default>Item</default>
        </data>
        <data source="rarity">
            <label>Rarity</label>
        </data>
    </group>

    <!-- Stats -->
    <group collapse="open">
        <header>Stats</header>
        <!-- Offensive -->
        <data source="damage"><label>Damage ❁</label></data>
        <data source="strength"><label>Strength ❁</label></data>
        <data source="crit_chance"><label>Crit Chance ☣</label></data>
        <data source="crit_damage"><label>Crit Damage ☠</label></data>
        <data source="bonus_attack_speed"><label>Bonus Attack Speed ⚔</label></data>
        <data source="sea_creature_chance"><label>Sea Creature Chance α</label></data>
        <data source="ferocity"><label>Ferocity ⫽</label></data>
        <data source="ability_damage"><label>Ability Damage ๑</label></data>
        <!-- Defensive & Utility -->
        <data source="health"><label>Health ❤</label></data>
        <data source="defense"><label>Defense ❈</label></data>
        <data source="true_defense"><label>True Defense ❂</label></data>
        <data source="speed"><label>Speed ✦</label></data>
        <data source="intelligence"><label>Intelligence ✎</label></data>
        <data source="magic_find"><label>Magic Find ✯</label></data>
        <data source="pet_luck"><label>Pet Luck ♣</label></data>
        <!-- Skill Fortune -->
        <data source="mining_speed"><label>Mining Speed ⸕</label></data>
        <data source="mining_fortune"><label>Mining Fortune ☘</label></data>
        <data source="farming_fortune"><label>Farming Fortune ☘</label></data>
        <data source="foraging_fortune"><label>Foraging Fortune ☘</label></data>
        <data source="pristine"><label>Pristine ✧</label></data>
    </group>

    <!-- Requirements -->
    <group collapse="open">
        <header>Requirements</header>
        <data source="combat_level_requirement"><label>Combat Level</label></data>
        <data source="dungeon_level_requirement"><label>Dungeon Level</label></data>
        <data source="slayer_level_requirement"><label>Slayer Level</label></data>
        <data source="hotm_requirement"><label>HotM Level</label></data>
        <data source="other_level_requirement"><label>Skill Level</label></data>
        <data source="collection"><label>Collection</label></data>
    </group>

    <!-- Ability -->
    <group collapse="closed">
        <header>Ability</header>
        <data source="ability_name"><label>Ability Name</label></data>
        <data source="ability_activation"><label>Activation</label></data>
        <data source="ability_desc"><label>Description</label></data>
        <data source="mana_cost"><label>Mana Cost</label></data>
        <data source="cooldown"><label>Cooldown</label></data>
    </group>

    <!-- Material Tiers -->
    <group layout="horizontal">
        <header>Material Tiers</header>
        <data source="prev_material">
            <label>← Previous</label>
            <default>None</default>
        </data>
        <data source="next_material">
            <label>Next →</label>
            <default>None</default>
        </data>
    </group>

    <!-- Properties -->
    <group layout="horizontal">
        <header>Properties</header>
        <data source="salable">
            <label>Salable</label>
        </data>
        <data source="tradeable">
            <label>Tradeable</label>
        </data>
        <data source="auctionable">
            <label>Auctionable</label>
        </data>
        <data source="museum">
            <label>Museum</label>
        </data>
    </group>

    <!-- Shop -->
    <group>
        <header>Shop</header>
        <!-- Sell -->
        <data source="sell">
            <label>Sell</label>
        </data>
        <data source="sell_shard">
            <label>Sell</label>
        </data>
        <data source="sell_serium">
            <label>Sell</label>
        </data>
        <!-- Buy -->
        <data source="buy">
            <label>Buy</label>
        </data>
        <data source="buy_shard">
            <label>Buy</label>
        </data>
        <data source="buy_serium">
            <label>Buy</label>
        </data>
    </group>

    <!-- Other Details -->
    <group collapse="closed">
        <header>Details</header>
        <data source="id"><label>Item ID</label></data>
        <data source="source"><label>Source</label></data>
        <data source="upgrades_from"><label>Upgrades From</label></data>
        <data source="upgrades_to"><label>Upgrades To</label></data>
        <data source="raw_materials"><label>Raw Materials</label></data>
        <data source="material_cost"><label>Material Cost</label></data>
    </group>

</infobox>
<noinclude>
[[Category:Templates]]
Bagian ini adalah '''Portable Infobox''' yang diadaptasi dari struktur Hypixel, disematkan langsung menggunakan XML Native Fandom tanpa menggunakan Lua. Bagian Bazaar (seperti buy price / sell price fluktuatif) tidak disertakan sesuai kebutuhan Seria Wiki. Simbol stat (*stats icons*) telah ditanamkan secara otomatis pada label. Semua field diratakan ke tengah.
</noinclude>

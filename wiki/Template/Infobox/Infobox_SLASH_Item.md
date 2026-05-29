<infobox theme="default" layout="stacked">
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
            <format>&lt;div align="center"&gt;%s&lt;/div&gt;</format>
        </data>
        <data source="type">
            <label>Type</label>
            <default>Item</default>
            <format>&lt;div align="center"&gt;%s&lt;/div&gt;</format>
        </data>
        <data source="rarity">
            <label>Rarity</label>
            <format>&lt;div align="center"&gt;%s&lt;/div&gt;</format>
        </data>
    </group>

    <!-- Stats -->
    <group collapse="open">
        <header>Stats</header>
        <!-- Offensive -->
        <data source="damage"><label>Damage ❁</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
        <data source="strength"><label>Strength ❁</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
        <data source="crit_chance"><label>Crit Chance ☣</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
        <data source="crit_damage"><label>Crit Damage ☠</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
        <data source="bonus_attack_speed"><label>Bonus Attack Speed ⚔</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
        <data source="sea_creature_chance"><label>Sea Creature Chance α</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
        <data source="ferocity"><label>Ferocity ⫽</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
        <data source="ability_damage"><label>Ability Damage ๑</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
        <!-- Defensive & Utility -->
        <data source="health"><label>Health ❤</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
        <data source="defense"><label>Defense ❈</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
        <data source="true_defense"><label>True Defense ❂</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
        <data source="speed"><label>Speed ✦</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
        <data source="intelligence"><label>Intelligence ✎</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
        <data source="magic_find"><label>Magic Find ✯</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
        <data source="pet_luck"><label>Pet Luck ♣</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
        <!-- Skill Fortune -->
        <data source="mining_speed"><label>Mining Speed ⸕</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
        <data source="mining_fortune"><label>Mining Fortune ☘</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
        <data source="farming_fortune"><label>Farming Fortune ☘</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
        <data source="foraging_fortune"><label>Foraging Fortune ☘</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
        <data source="pristine"><label>Pristine ✧</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
    </group>

    <!-- Requirements -->
    <group collapse="open">
        <header>Requirements</header>
        <data source="combat_level_requirement"><label>Combat Level</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
        <data source="dungeon_level_requirement"><label>Dungeon Level</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
        <data source="slayer_level_requirement"><label>Slayer Level</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
        <data source="hotm_requirement"><label>HotM Level</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
        <data source="other_level_requirement"><label>Skill Level</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
        <data source="collection"><label>Collection</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
    </group>

    <!-- Ability -->
    <group collapse="closed">
        <header>Ability</header>
        <data source="ability_name"><label>Ability Name</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
        <data source="ability_activation"><label>Activation</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
        <data source="ability_desc"><label>Description</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
        <data source="mana_cost"><label>Mana Cost</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
        <data source="cooldown"><label>Cooldown</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
    </group>

    <!-- Material Tiers -->
    <group layout="horizontal">
        <header>Material Tiers</header>
        <data source="prev_material">
            <label>← Previous</label>
            <default>None</default>
            <format>&lt;div align="center"&gt;%s&lt;/div&gt;</format>
        </data>
        <data source="next_material">
            <label>Next →</label>
            <default>None</default>
            <format>&lt;div align="center"&gt;%s&lt;/div&gt;</format>
        </data>
    </group>

    <!-- Properties -->
    <group layout="horizontal">
        <header>Properties</header>
        <data source="salable">
            <label>Salable</label>
            <format>&lt;div align="center"&gt;%s&lt;/div&gt;</format>
        </data>
        <data source="tradeable">
            <label>Tradeable</label>
            <format>&lt;div align="center"&gt;%s&lt;/div&gt;</format>
        </data>
        <data source="auctionable">
            <label>Auctionable</label>
            <format>&lt;div align="center"&gt;%s&lt;/div&gt;</format>
        </data>
        <data source="museum">
            <label>Museum</label>
            <format>&lt;div align="center"&gt;%s&lt;/div&gt;</format>
        </data>
    </group>

    <!-- Shop -->
    <group>
        <header>Shop</header>
        <!-- Sell -->
        <data source="sell">
            <label>Sell</label>
            <format>&lt;div align="center"&gt;{{Gins|1=%s}}&lt;/div&gt;</format>
        </data>
        <data source="sell_shard">
            <label>Sell</label>
            <format>&lt;div align="center"&gt;{{Shard|1=%s}}&lt;/div&gt;</format>
        </data>
        <data source="sell_serium">
            <label>Sell</label>
            <format>&lt;div align="center"&gt;{{Serium|1=%s}}&lt;/div&gt;</format>
        </data>
        <!-- Buy -->
        <data source="buy">
            <label>Buy</label>
            <format>&lt;div align="center"&gt;{{Gins|1=%s}}&lt;/div&gt;</format>
        </data>
        <data source="buy_shard">
            <label>Buy</label>
            <format>&lt;div align="center"&gt;{{Shard|1=%s}}&lt;/div&gt;</format>
        </data>
        <data source="buy_serium">
            <label>Buy</label>
            <format>&lt;div align="center"&gt;{{Serium|1=%s}}&lt;/div&gt;</format>
        </data>
    </group>

    <!-- Other Details -->
    <group collapse="closed">
        <header>Details</header>
        <data source="id"><label>Item ID</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
        <data source="source"><label>Source</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
        <data source="upgrades_from"><label>Upgrades From</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
        <data source="upgrades_to"><label>Upgrades To</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
        <data source="raw_materials"><label>Raw Materials</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
        <data source="material_cost"><label>Material Cost</label><format>&lt;div align="center"&gt;%s&lt;/div&gt;</format></data>
    </group>

</infobox>
<noinclude>
[[Category:Templates]]
Bagian ini adalah '''Portable Infobox''' yang diadaptasi dari struktur Hypixel, disematkan langsung menggunakan XML Native Fandom tanpa menggunakan Lua. Bagian Bazaar (seperti buy price / sell price fluktuatif) tidak disertakan sesuai kebutuhan Seria Wiki. Simbol stat (*stats icons*) telah ditanamkan secara otomatis pada label. Semua field diratakan ke tengah.
</noinclude>
<infobox theme="seria">
    <title source="title">
        <default>{{PAGENAME}}</default>
    </title>
    
    <image source="image">
        <default>[[File:{{PAGENAME}}.png|200px]]</default>
    </image>
    
    <data source="slot">
        <format>
            <div style="margin: 5px auto 0 auto; width: 32px; height: 32px; background-color: #8b8b8b; border: 2px solid; border-color: #373737 #fff #fff #373737; display: flex; justify-content: center; align-items: center; box-sizing: content-box;">[[File:{{{slot|{{PAGENAME}}}}}.png|32px]]</div>
        </format>
    </data>

    <data source="gallery">
        <format>
            <div style="text-align: center; margin-top: 5px; padding-top: 5px; border-top: 1px solid #b8b8b8;">{{{gallery}}}</div>
        </format>
    </data>

    <!-- Basic Information -->
    <group>
        <data source="aka"><label>Also known as</label></data>
        <data source="type"><label>Type</label><default>Item</default></data>
        <data source="rarity"><label>Rarity</label></data>
        <data source="collection"><label>Collection</label></data>
        
        <!-- Requirements -->
        <data source="combat_level_requirement"><label>Combat Level Req</label></data>
        <data source="slayer_level_requirement"><label>Slayer Level Req</label></data>
        <data source="dungeon_level_requirement"><label>Dungeon Level Req</label></data>
        <data source="dungeon_floor_clearing_requirement"><label>Dungeon Completion</label></data>
        <data source="hotm_requirement"><label>HotM Requirement</label></data>
        <data source="other_level_requirement"><label>Skill Level Req</label></data>
        
        <data source="reforge_name"><label>Reforge / Power</label></data>
        <data source="source"><label>Source</label></data>
        <data source="obtained"><label>Obtained via</label></data>
        <data source="drop_chance"><label>Drop Chance</label></data>
        <data source="uses"><label>Uses</label></data>
        <data source="minion_xp"><label>Minion XP</label></data>
        <data source="lore"><label>Tooltip Text</label></data>
        <data source="mob"><label>Mob</label></data>
        <data source="rarities"><label>Rarities</label></data>
        <data source="essence"><label>Essence</label></data>
    </group>

    <!-- Sack Stats -->
    <group collapse="open">
        <header>Sack Stats</header>
        <data source="sack_capacity"><label>Max Capacity</label></data>
        <data source="sack_items"><label>Items</label></data>
    </group>

    <!-- Garden -->
    <group collapse="open">
        <header>Garden</header>
        <data source="organic_matter"><label>Organic Matter</label></data>
    </group>

    <!-- Block Details -->
    <group collapse="open">
        <header>Block Details</header>
        <data source="location"><label>Location</label></data>
        <data source="tool"><label>Preferred Tool</label></data>
        <data source="breaking_power_required"><label>Breaking Power Required</label></data>
        <data source="skill_xp_given"><label>Skill XP Given</label></data>
        <data source="experience_given"><label>Experience Given</label></data>
        <data source="normal_drop"><label>Normal Drop</label></data>
        <data source="silk_touch_drop"><label>Silk Touch Drop</label></data>
        <data source="smelting_touch_drop"><label>Smelting Touch Drop</label></data>
    </group>

    <!-- Function -->
    <group collapse="open">
        <header>Function</header>
        <data source="function"><label>Function</label></data>
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
        <!-- Other Stats -->
        <data source="swing_range"><label>Swing Range Ⓢ</label></data>
        <data source="shot_cooldown"><label>Shot Cooldown</label></data>
    </group>

    <!-- Special Effects -->
    <group collapse="open">
        <header>Special Effects</header>
        <data source="effects"><label>Effects</label></data>
        <data source="duration"><label>Duration</label></data>
        <data source="speed_boost"><label>Speed Boost</label></data>
        <data source="full_set_bonus"><label>Full Set Bonus</label></data>
        <data source="tiered_armor_bonus"><label>Tiered Armor Bonus</label></data>
        <data source="piece_bonus"><label>Piece Bonus</label></data>
        <data source="full_set_bonus2"><label>Full Set Bonus 2</label></data>
        <data source="tiered_armor_bonus_2"><label>Tiered Armor Bonus 2</label></data>
        <data source="piece_bonus2"><label>Piece Bonus 2</label></data>
    </group>

    <!-- Abilities -->
    <group collapse="open">
        <header>Ability 1</header>
        <data source="ability_name1"><label>Name</label></data>
        <data source="ability_desc1"><label>Description</label></data>
        <data source="soulflow_cost1"><label>Soulflow Cost</label></data>
        <data source="mana_cost1"><label>Mana Cost</label></data>
        <data source="health_cost1"><label>Health Cost</label></data>
        <data source="coin_cost1"><label>Coin Cost</label></data>
        <data source="cooldown1"><label>Cooldown</label></data>
        <data source="int_scaling1"><label>Intelligence Scaling</label></data>
        <data source="max_souls1"><label>Max Souls</label></data>
    </group>
    <group collapse="open">
        <header>Ability 2</header>
        <data source="ability_name2"><label>Name</label></data>
        <data source="ability_desc2"><label>Description</label></data>
        <data source="soulflow_cost2"><label>Soulflow Cost</label></data>
        <data source="mana_cost2"><label>Mana Cost</label></data>
        <data source="health_cost2"><label>Health Cost</label></data>
        <data source="coin_cost2"><label>Coin Cost</label></data>
        <data source="cooldown2"><label>Cooldown</label></data>
        <data source="int_scaling2"><label>Intelligence Scaling</label></data>
        <data source="max_souls2"><label>Max Souls</label></data>
    </group>
    <group collapse="open">
        <header>Ability 3</header>
        <data source="ability_name3"><label>Name</label></data>
        <data source="ability_desc3"><label>Description</label></data>
        <data source="soulflow_cost3"><label>Soulflow Cost</label></data>
        <data source="mana_cost3"><label>Mana Cost</label></data>
        <data source="health_cost3"><label>Health Cost</label></data>
        <data source="coin_cost3"><label>Coin Cost</label></data>
        <data source="cooldown3"><label>Cooldown</label></data>
        <data source="int_scaling3"><label>Intelligence Scaling</label></data>
        <data source="max_souls3"><label>Max Souls</label></data>
    </group>

    <!-- Material Tiers -->
    <group collapse="open" layout="horizontal">
        <header>Material Tiers</header>
        <data source="prev_material"><label>← Previous</label></data>
        <data source="next_material"><label>Next →</label></data>
    </group>

    <!-- Upgrades -->
    <group collapse="open" layout="horizontal">
        <header>Upgrades</header>
        <data source="upgrades_from"><label>Upgrades From</label></data>
        <data source="upgrades_to"><label>Upgrades To</label></data>
    </group>

    <!-- Tiers -->
    <group collapse="open" layout="horizontal">
        <header>Tiers</header>
        <data source="lower_tier"><label>Lower Tier</label></data>
        <data source="higher_tier"><label>Higher Tier</label></data>
    </group>

    <!-- Gemstone Upgrades -->
    <group collapse="open">
        <header>Gemstone Upgrades</header>
        <data source="gemstone_slots"><label>Gemstone Slots</label></data>
        <data source="gemstone_slots_fragged"><label>Fragged Slots</label></data>
    </group>

    <!-- Enchantment Requirements -->
    <group collapse="open">
        <header>Enchantment Requirements</header>
        <data source="min_level"><label>Min Level</label></data>
        <data source="max_level"><label>Max Level</label></data>
        <data source="applied_to"><label>Applied To</label></data>
        <data source="experience_cost"><label>Experience Cost</label></data>
        <data source="req_enchanting_level"><label>Enchanting Level Req</label></data>
    </group>

    <!-- Reforge Requirements -->
    <group collapse="open">
        <header>Reforge Requirements</header>
        <data source="req_item_rarity"><label>Item Rarity Req</label></data>
        <data source="apply_cost"><label>Apply Cost</label></data>
        <data source="req_skill_level"><label>Skill Level Req</label></data>
    </group>

    <!-- Properties -->
    <group collapse="open" layout="horizontal">
        <header>Properties</header>
        <data source="upgradeable"><label>Upgradeable</label></data>
        <data source="enchantable"><label>Enchantable</label></data>
        <data source="reforgeable"><label>Reforgeable</label></data>
        <data source="salable"><label>Sellable</label></data>
        <data source="tradeable"><label>Tradeable</label></data>
        <data source="auctionable"><label>Auctionable</label></data>
        <data source="rideable"><label>Rideable</label></data>
        <data source="donatable"><label>Museum</label></data>
        <data source="soulbound"><label>Soulbound</label></data>
        <data source="rift_transferrable"><label>Rift Transferrable</label></data>
        <data source="god_potion"><label>God Potion</label></data>
    </group>

    <!-- Color -->
    <group collapse="open">
        <header>Color</header>
        <data source="color"><label>Color</label></data>
    </group>

    <!-- Shop -->
    <group collapse="open">
        <header>Shop</header>
        <data source="merchant"><label>Merchant</label></data>
        <data source="daily_limit"><label>Daily Limit</label></data>
        <data source="buy"><label>Buy</label></data>
        <data source="sell"><label>Sell</label></data>
        <data source="motes_sell"><label>Sell (Motes)</label></data>
    </group>

    <!-- Materials -->
    <group collapse="open">
        <header>Materials</header>
        <data source="raw_materials"><label>Raw Materials</label></data>
        <data source="material_cost"><label>Material Cost</label></data>
        <data source="raw_materials_upgr"><label>Raw Materials (Upgr)</label></data>
        <data source="material_cost_upgr"><label>Material Cost (Upgr)</label></data>
    </group>

    <!-- Trade -->
    <group collapse="open">
        <header>Trade</header>
        <data source="trade_requirement"><label>Trade Requirement</label></data>
        <data source="trade_from"><label>Trade From</label></data>
        <data source="trade_to"><label>Trade To</label></data>
    </group>

    <!-- Next Event -->
    <group collapse="open">
        <header>Next Event</header>
        <data source="skydate_start"><label>Event Start</label></data>
        <data source="skydate_end"><label>Event End</label></data>
    </group>

    <!-- Other Details -->
    <group collapse="closed">
        <header>Details</header>
        <data source="id"><label>Item ID</label></data>
        <data source="pet_id"><label>Pet ID</label></data>
        <data source="helmet_id"><label>Helmet ID</label></data>
        <data source="chestplate_id"><label>Chestplate ID</label></data>
        <data source="leggings_id"><label>Leggings ID</label></data>
        <data source="boots_id"><label>Boots ID</label></data>
        <data source="head_texture"><label>Head Texture</label></data>
        <data source="nbt"><label>NBT</label></data>
    </group>
</infobox>
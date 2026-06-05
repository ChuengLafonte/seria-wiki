== Infobox/Mechanic Parameters ==
Infobox/Mechanic is a module providing support for multiple versions of infobox, and many data inputs are processed here. To convenient maintenance, each data is attached with a parameter index. A group is signified by a unique English letter before the number, known as group index. '''Groups need not be ordered in the alphabetical order of their group indexes; a new group using a new letter can be added in between existing groups.'''

To add a new parameter to the module, one must first prepare the data, and then insert it into the infobox. You may take reference from the precedent entries.

You must add a corresponding param index as comment in the code, on both locations, '''in the order of display'''. Also, you should add the parameter used to the following list, '''also in the order of display'''.

<div style="border:1px solid gray; padding: 1em 1em; margin: 1em 1em;">
{{Red|Last Group Letter Used: U}}<br>
{{Green|Next Letter: V}}
</div>

== List of Parameters ==
<pre>
0.   tab

1.   image (if gallery: |image_type = square/long/wide)
2.   caption
3.   slot_item
4.   aka
5.   type
6.   color

7.   appearance
8.   collection
9.   usage

10.  uses
11.  ways_to_increase

12.  category
13.  collects
14.  upgrade_with

15.  travel_scroll
16.  level
17.  sublocations
18.  fairy_souls
19.  enigma_souls

20.  election_wins

21.  amount

Dungeon Information
A0.  dungeon
A1.  floor
A2.  boss
A3.  status
A4.  dungeon_size
A5.  party_size
A6.  required_combat_level
A7.  required_catacombs_level
A8.  reqs
A9.  base_xp
A10. failable

Mob Information
B0.  mob_level
B1.  damage_deals
B2.  damage_rift
B3.  damage_resistance
B4.  spawn_location
B5.  spawn_condition
B6.  special
B7.  special_behavior
B8.  mob_type
B9.  entity_type
B10.  effective_enchant

Quest
C0.  requirements
C1.  rewards

Stats
D0.  stats
D1+. all other stats (refer to [[Module:Infobox/Item]] Group D)

Perks
E0+.  perk(n)_desc, perk(n)_name

Capacity
F0.  default_desc, default_name
F1+. upgrade(n)_desc, upgrade(n)_name

Location
G0.  xyz
G1.  coordinates
G2.  location
G3.  start_location
G4.  start_npc
G5.  prev_location
G6.  next_location

Inhabitants
H0.  mobs
H1.  npcs

Resources
I0.  drops
I1.  resources

Drops
R0.  mob_drops
R1.  xp
R2.  coins
R3.  experience
R4.  essence
R5.  attribute_shard

Values
J0.  base_value
J1.  max_value

Properties
K0.  unlock_requirement
K1.  max_level

Special Effects
L0.  skill_special_effect

Upgrades
M0.  super_compactor
M1.  compactor
M2.  auto_smelter

Player Interactions
N0.  quests
N1.  shop

Next Event
S0. datetime (using skydate_start)
S1. countdown (using skydate_start, skydate_end)

Minimap (at Coordinates)
O0.  minimap (note: normally uses location (if is link, stripped as text) - can use minimap_location to specify the minimap location that is different from location)

Ideal Layout
P0.  ideal_layout

Item Metadata
Q0.  id

Symbol Information
T0. symbol
T1. unicode
T2. icon

Sea Creature Properties
U0. sc_weight
U1. sc_location
U2. sc_type
U3. sc_fishing_req
U4. sc_hotspot
U5. sc_bait
U6. sc_hunter
U7. sc_time_req
U8. sc_event_req
U9. sc_other_req
</pre>

==List of Templates using Module:Infobox/Mechanic==
* [[Template:Infobox character]]
* [[Template:Infobox dungeon enemy]]
* [[Template:Infobox dungeon floor]]
* [[Template:Infobox location]]
* [[Template:Infobox mayor]]
* [[Template:Infobox minion]]
* [[Template:Infobox mob]]
* [[Template:Infobox puzzle]]
* <s>[[Template:Infobox quest]]</s>
* [[Template:Infobox stat]]
* [[Template:Infobox skill]]
* [[Template:Infobox upgrade]]
* [[Template:Infobox currency]]
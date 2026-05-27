/*<pre>*/
/***************************************
* CSS relating to minimaps
****************************************/
.hsw-minimap {
	position: relative;
	overflow: hidden;
	box-sizing: border-box;
	background-repeat: no-repeat;
	/* Prevent image blurring on scale */
	image-rendering: -moz-crisp-edges;
	image-rendering: -o-crisp-edges;
	image-rendering: -webkit-optimize-contrast;
	image-rendering: crisp-edges;
	image-rendering: pixelated;
}
.no-rendering {
	image-rendering: auto;
}
.minimap-caption {
	position: absolute;
	bottom: 0;
	left: 0;
	right: 0;
	text-align: center;
	background: #444a;
	line-height: 1.3;
	font-size: 12px;
}

/***************************************
* Map markers
****************************************/
.minimap-marker {
	position: absolute;
	top: 50%;
	left: 50%;
	transform: translate(-50%,-50%);
}

/***************************************
* Map images
* NOTE: When updating this part, one must re-calibrate values on [[Module:Minimap/Data]] !!
****************************************/
.minimap-hub {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/0/03/Hub_Island_(0.24.1)_(Top_View).png");
}
.minimap-hub-0_24_1 { /* pre-revamp */
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/0/03/Hub_Island_(0.24.1)_(Top_View).png");
}
.minimap-hub-0_24_aura {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/8/87/Hub_Island_(0.24)_(Aura)_(Top_View).png");
}
.minimap-hub-0_11_4 { /* was used as the main image for a while */
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/d/da/Hub_Island_(0.11.4)_(Top_View).png");
}
.minimap-hub-0_8 { /* Retained for [[Warren]] */
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/7/7f/Hub_Island_(0.8)_(Top_View).png");
}
.minimap-village {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/d/d5/Village_(top_view).png");
}
.minimap-museum {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/9/9f/Museum_(top_view).png");
}
.minimap-crypt {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/c/c7/Crypt_(top_view).png");
}
.minimap-dark-auction {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/5/56/Dark_Auction_(0.24.1)_(Top_View).png");
}
.minimap-backwater-bayou {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/6/6b/Backwater_Bayou_(Top_View).png");
}
.minimap-park {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/4/40/The_Park_(0.24.1)_(Top_View).png");
}
.minimap-birch-park {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/3/30/Birch_Park_(0.24.1)_(Top_View).png");
}
.minimap-spruce-woods {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/6/6b/Spruce_Woods_(0.24.1)_(Top_View).png");
}
.minimap-dark-thicket {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/f/fe/Dark_Thicket_(0.24.1)_(Top_View).png");
}
.minimap-savanna-woodland {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/6/6f/Savanna_Woodland_(0.24.1)_(Top_View).png");
}
.minimap-jungle-island {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/7/7b/Jungle_Island_(0.24.1)_(Top_View).png");
}
.minimap-howling-cave {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/1/15/Howling_Cave_(0.24.1)_(Top_View).png");
}
.minimap-spirit-cave {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/0/0c/Spirit_Cave_(0.24.1)_(Top_View).png");
}
.minimap-soul-cave {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/c/c2/Soul_Cave_(0.24.1)_(Top_View).png");
}
.minimap-rift {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/a/a0/Rift_Dimension_(0.19)_(Top_View).png");
}

/*** Combat Islands ***/
.minimap-spiders-den {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/b/b4/Spiders_Den_(0.13)_(Top_View).png");
}
.minimap-arachnes-burrow {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/e/e4/Arachne%27s_Burrow_(Top_View).png");
}
.minimap-blazing-fort { /* retained! */
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/f/f1/Blazing_Fortress_(0.1)_(Top_View).png");
}
.minimap-end {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/f/f8/The_End_(0.7)_(Top_View).png");
}
.minimap-stronghold { /* note: if no usage, no retain */
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/4/4d/Stronghold_(top_view).png");
}
.minimap-stronghold-1 { /* note: if no usage, no retain */
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/a/a8/Stronghold_(top_view)_1.png");
}
.minimap-stronghold-2 { /* note: if no usage, no retain */
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/8/81/Stronghold_(top_view)_2.png");
}
.minimap-crimson-isle {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/c/cb/Crimson_Isle_(0.13)_(Top_View).png");
}

/*** Farming Islands ***/
.minimap-barn {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/c/c6/The_Barn_(0.11.4)_(Top_View).png");
}
.minimap-mushroom-desert {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/7/7b/Mushroom_Desert_(0.11.4)_(Top_View).png");
}

/*** Mining Islands ***/
.minimap-gold-mine {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/9/9e/Gold_Mine_(0.1)_(Top_View).png");
}
.minimap-deep-caverns {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/3/3f/Deep_Caverns_(0.1)_(Top_View).png");
}
.minimap-gunpowder-mines {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/6/6f/Gunpowder_Mines_(0.1)_(Top_View).png");
}
.minimap-lapis-quarry {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/e/e1/Lapis_Quarry_(0.1)_(Top_View).png");
}
.minimap-pigmans-den {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/2/2b/Pigman%27s_Den_(0.1)_(Top_View).png");
}
.minimap-slimehill {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/1/15/Slimehill_(0.1)_(Top_View).png");
}
.minimap-diamond-reserve {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/4/4e/Diamond_Reserve_(0.1)_(Top_View).png");
}
.minimap-obsidian-sanctuary {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/6/6e/Obsidian_Sanctuary_(0.1)_(Top_View).png");
}
.minimap-dwarven-mines {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/2/2c/Dwarven_Mines_Map.png");
}
.minimap-dwarven-mines-dirt-cave {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/a/a3/Dwarven_Mines_Dirt_Cave_(0.24.1)_(Top_View).png");
}
.minimap-crystal-nucleus-higher {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/6/60/Crystal_Nucleus_(0.24.1)_(Top_View_Higher).png");
}
.minimap-crystal-nucleus-lower {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/b/b8/Crystal_Nucleus_(0.24.1)_(Top_View_Lower).png");
}
.minimap-dwarven-village {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/6/65/Dwarven_Village_(0.24.1)_(Top_View).png");
}
.minimap-ironmans-guild {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/4/4b/Ironman's_Guild_(0.24.1)_(Top_View).png");
}
.minimap-lava-springs {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/0/05/Lava_Springs_(0.24.1)_(Top_View).png");
}
.minimap-royal-mines-higher {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/3/3c/Royal_Mines_(0.24.1)_(Top_View_Higher).png");
}
.minimap-royal-mines-lower {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/6/64/Royal_Mines_(0.24.1)_(Top_View_Lower).png");
}
.minimap-palace-bridge {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/6/66/Palace_Bridge_(0.24.1)_(Top_View).png");
}
.minimap-royal-palace {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/f/fe/Royal_Palace_(0.24.1)_(Top_View).png");
}
.minimap-great-ice-wall-higher {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/c/c6/Great_Ice_Wall_(0.24.1)_(Top_View_Higher).png");
}
.minimap-great-ice-wall-lower {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/8/8e/Great_Ice_Wall_(0.24.1)_(Top_View_Lower).png");
}
.minimap-divans-gateway {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/c/ca/Divan's_Gateway_(0.24.1)_(Top_View).png");
}
.minimap-goblin-burrows {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/0/0d/Goblin_Burrows_(0.24.1)_(Top_View).png");
}
.minimap-far-reserve {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/e/e5/Far_Reserve_(0.24.1)_(Top_View).png");
}
.minimap-ramparts-quarry {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/f/fb/Rampart's_Quarry_(0.24.1)_(Top_View).png");
}
.minimap-upper-mines-lower {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/b/b0/Upper_Mines_(0.24.1)_(Top_View_Lower).png");
}
.minimap-upper-mines-higher {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/9/95/Upper_Mines_(0.24.1)_(Top_View_Higher).png");
}
.minimap-abandoned-quarry {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/9/9d/Abandoned_Quarry_(0.24.1)_(Top_View).png");
}
.minimap-the-forge {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/a/a8/The_Forge_(0.24.1)_(Top_View).png");
}
.minimap-the-mist {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/2/27/The_Mist_(0.24.1)_(Top_View).png");
}
.minimap-aristocrat-passage {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/4/40/Aristocrat_Passage_(0.24.1)_(Top_View).png");
}
.minimap-glacite-tunnels {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/c/c6/Glacite_Tunnels_(0.24.1)_(Top_View).png");
}

/*** Rift ***/
.minimap-dolphin-trainer {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/2/2f/Dolphin_Trainer_(0.24.1)_(Top_View).png");
}
.minimap-oubliette {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/b/ba/Oubliette_(0.24.1)_(Top_View).png");
}
.minimap-your-island {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/c/c2/%22Your%22_Island_(0.24.1)_(Top_View).png");
}
.minimap-barry-hq {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/d/d7/Barry_HQ_(0.24.1)_(Top_View).png");
}
.minimap-book-in-a-book {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/5/5c/Book_in_a_Book_(0.24.1)_(Top_View).png");
}
.minimap-rift-gallery {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/5/5a/Rift_Gallery_(0.24.1)_(Top_View).png");
}
.minimap-living-stillness {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/a/a3/Living_Stillness_(0.24.1)_(Top_View).png");
}
.minimap-pumpgrotto {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/d/de/Pumpgrotto_(0.24.1)_(Top_View).png");
}
.minimap-mountaintop-bottom {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/1/1d/The_Mountaintop_(0.24.1)_(Top_View_Bottom).png");
}
.minimap-mountaintop-middle {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/8/85/The_Mountaintop_(0.24.1)_(Top_View_Middle).png");
}
.minimap-walk-of-fame {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/6/65/Walk_of_Fame_(0.24.1)_(Top_View).png");
}
.minimap-time-chamber {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/0/04/Time_Chamber_(0.24.1)_(Top_View).png");
}
.minimap-mirrorverse-room-1 {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/7/70/Mirrorverse_Room_1_(0.24.1)_(Top_View).png");
}
.minimap-mirrorverse-room-2 {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/8/8e/Mirrorverse_Room_2_(0.24.1)_(Top_View).png");
}
.minimap-mirrorverse-room-2-and-3 {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/7/77/Mirrorverse_Room_2_and_3_(0.24.1)_(Top_View).png");
}
.minimap-mirrorverse-room-3 {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/d/db/Mirrorverse_Room_3_(0.24.1)_(Top_View).png");
}
.minimap-mirrorverse-room-4 {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/7/72/Mirrorverse_Room_4_(0.24.1)_(Top_View).png");
}
.minimap-mirrorverse-room-4-and-5 {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/b/be/Mirrorverse_Room_4_and_5_(0.24.1)_(Top_View).png");
}
.minimap-mirrorverse-room-5 {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/0/0a/Mirrorverse_Room_5_(0.24.1)_(Top_View).png");
}
.minimap-mirrorverse-room-6 {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/8/81/Mirrorverse_Room_6_(0.24.1)_(Top_View).png");
}
.minimap-mirrorverse-room-7 {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/1/12/Mirrorverse_Room_7_(0.24.1)_(Top_View).png");
}
.minimap-mirrorverse-room-8 {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/b/bd/Mirrorverse_Room_8_(0.24.1)_(Top_View).png");
}
.minimap-great-beanstalk {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/1/15/Great_Beanstalk_(0.24.1)_(Top_View).png");
}

/*** Event Islands ***/
.minimap-winter-island {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/a/a8/Winter_Island_(0.17)_(Top_View).png");
}
.minimap-hot-springs {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/f/f9/Hot_Springs_(0.24.1)_(Top_View).png");
}
.minimap-glacial-cave {
	background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/1/10/Glacial_Cave_(0.24.1)_(Top_View).png");
}
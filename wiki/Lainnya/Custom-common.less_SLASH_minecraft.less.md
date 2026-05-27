/*
// Inventory slot (Module:Inventory slot)
// Taken from corresponding template of same name on minecraft.gamepedia.com
// and modified for use on this wiki
*/
.mw-parser-output .invslot {
	position: relative;
	display: inline-block;
	background: #8B8B8B no-repeat center center / 32px 32px;
	border: 2px solid;
	border-color: #373737 #FFF #FFF #373737;
	width: 32px;
	height: 32px;
	font-size: 16px;
	line-height: 1;
	text-align: left;
	vertical-align: bottom;
	box-sizing: content-box;
}
.mw-parser-output .wikitable .invslot {
	box-sizing: content-box;
}
.invslot-item {
	position: relative;
	display: block;
	background-origin: content-box;
	background-clip: content-box;
	width: 32px;
	height: 32px;
	top: -2px;
	left: -2px;
	padding: 2px;
}
.invslot-item:not(.invslot-pickup):hover::before {
	background-color: rgba(255,255,255,0.5);
	position: absolute;
	height: 32px;
	width: 32px;
	content: "";
	background-position: center center;
	z-index: 3;
	pointer-events: none;
}
.invslot-stacksize {
	position: absolute;
	margin-right: 2px;
	margin-bottom: 2px;
	right: 0;
	bottom: 0;
	font-family: minecraft, unifontm, unifont, Rubik, serif, sans-serif;
	font-weight: normal;
	font-size: 16px;
	text-align: right;
	color: #FFF;
	text-shadow: 1.5px 1.5px 0 #3F3F3F;
	filter: dropshadow(color=#3F3F3F, offx=2, offy=2);
	pointer-events: none;
}
.invslot a[href],
.invslot[class*="goto-"] {
	cursor: pointer;
}
.invslot span[data-iid] {
	background-size: 32px 32px;
	background-repeat: no-repeat;
}
.invslot-pickup {
	position: absolute;
	width: 32px;
	height: 32px;
	z-index: 5;
}
.invslot-large {
	padding: 8px;
}
.invslot-item-image > span > a.new:first-child {
	display: block;
	background: url(//static.wikia.nocookie.net/hypixel-skyblock/images/3/30/Question.png) no-repeat center/contain;
	width: 32px;
	height: 32px;
	text-indent: -9999px;
	overflow: hidden;
}
.invslot-item-image img {
	padding: 2px;
	margin: -2px;
}

/*
// MC Interfaces (Generic)
*/
.mw-parser-output .mcui {
	display: inline-block;
	position: relative;
	background-color: #C6C6C6;
	border: 2px solid;
	border-color: #DBDBDB #5B5B5B #5B5B5B #DBDBDB;
	border-radius: 3px;
	margin: 12px 0;
	padding: 8px;
	width: fit-content;
	text-align: left;
	white-space: nowrap;
	vertical-align: bottom;
}
.mcui.mcui-centered {
	display: table;
	margin-left: auto;
	margin-right: auto;
}
.mw-parser-output .mcui-header {
	display: block;
	font-family: minecraft, unifontm, unifont, Rubik, serif, sans-serif;
	font-size: 14px;
	color: #2B2D2F;
	letter-spacing: .2px;
	overflow: hidden;
	text-overflow: ellipsis;
}
.mcui > .mcui-header {
	margin: -4px 4px 4px 4px;
}
.mcui-returnbutton {
	position: absolute;
	top: -2px;
	right: 20px;
	font-size: 22px;
	color: #B84000;
	cursor: pointer;
	transition: color 0.2s ease, transform 0.5s ease;
}
.mcui-returnbutton:hover {
	color: #e1926b;
	transform: rotate(20deg);
}

/*
// MC Interface (Common Features)
*/
.mcui-Chest > *, .mcui-Crafting_Table > *, .mcui-Furnace > *, .mcui-Anvil > * {
	display: inline-block;
	vertical-align: top;
}
.mcui-Chest .mcui-row, .mcui-Crafting_Table .mcui-row, .mcui-Anvil .mcui-row {
	display: flex;
}


/*
// MC Interface (Chest)
*/

/*
// MC Interface (Crafting Grid)
// Taken from minecraft.gamepedia.com
*/
.mw-parser-output .mcui-Crafting_Table {
	display: flex;
	align-items: center;
	gap: 4px;
}
.mcui-Crafting_Table > .mcui-arrow:before {
	content: url(//static.wikia.nocookie.net/hypixel-skyblock/images/8/86/Grid_layout_Arrow_%28small%29.png);
	display: flex;
}
.mcui-Crafting_Table > .mcui-icons {
	position: absolute;
	top: 0;
	right: 0;
}
.mcui-Crafting_Table .mcui-shapeless,
.mcui-Crafting_Table .mcui-fixed {
	display: inline-block;
	background-repeat: no-repeat;
	width: 19px;
	height: 15px;
	cursor: help;
}
.mcui-Crafting_Table .mcui-shapeless {
	background-image: url(//static.wikia.nocookie.net/hypixel-skyblock/images/a/a9/Grid_layout_Shapeless.png);
}
.mcui-Crafting_Table .mcui-fixed {
	background-image: url(//static.wikia.nocookie.net/hypixel-skyblock/images/b/b8/Grid_layout_Fixed.png);
}

/*
// MC Interface (Furnace)
// Taken from minecraft.gamepedia.com
*/
.mw-parser-output .mcui-Furnace {
	display: flex;
	gap: 14px;
	align-items: center;
}
.mcui-Furnace > .mcui-input {
	display: flex;
	flex-direction: column;
}
.mcui-Furnace .mcui-fuel {
	background: url(//static.wikia.nocookie.net/hypixel-skyblock/images/d/d8/Grid_layout_Fire.png) no-repeat;
	width: 36px;
	height: 36px;
}
.mcui-Furnace .mcui-fuel.mcui-inactive {
	background-image: url(//static.wikia.nocookie.net/hypixel-skyblock/images/a/ab/Grid_layout_Fire_%28in-active%29.png);
}
.mcui-Furnace > .mcui-arrow {
	background: url(//static.wikia.nocookie.net/hypixel-skyblock/images/8/8e/Grid_layout_Furnace_Progress.png) no-repeat;
	width: 44px;
	height: 32px;
	margin-right: 4px;
}
.mcui-Furnace > .mcui-arrow.mcui-inactive,
.mcui-Anvil .mcui-arrow {
	background-image: url(//static.wikia.nocookie.net/hypixel-skyblock/images/d/dc/Grid_layout_Furnace_Progress_%28in-active%29.png);
}

/*
// MC Interface (Brewing Stand)
// Taken from minecraft.gamepedia.com
*/
.mw-parser-output .mcui-Brewing_Stand {
	display: flex;
	flex-direction: column;
	align-items: center;
}
.mcui-Brewing_Stand > .mcui-input {
	display: flex;
}
.mcui-Brewing_Stand > .mcui-input > .invslot {
	margin-top: 3px;
}
.mcui-Brewing_Stand .mcui-bubbling,
.mcui-Brewing_Stand .mcui-arrow {
	background-repeat: no-repeat;
	width: 24px;
	height: 57px;
}
.mcui-Brewing_Stand .mcui-bubbling {
	background-image: url(//static.wikia.nocookie.net/hypixel-skyblock/images/6/65/Grid_layout_Brewing_Bubbles.gif);
}
.mcui-Brewing_Stand > .mcui-input.mcui-inactive > .mcui-bubbling {
	background-image: url(//static.wikia.nocookie.net/hypixel-skyblock/images/d/db/Grid_layout_Brewing_Bubbles_%28In-active%29.png);
}
.mcui-Brewing_Stand .mcui-arrow {
	background-image: url(//static.wikia.nocookie.net/hypixel-skyblock/images/4/4b/Grid_layout_Brewing_Arrow.png);
}
.mcui-Brewing_Stand > .mcui-input.mcui-inactive > .mcui-arrow {
	background-image: url(//static.wikia.nocookie.net/hypixel-skyblock/images/5/59/Grid_layout_Brewing_Arrow_%28In-active%29.png);
}
.mcui-Brewing_Stand > .mcui-paths {
	background: url(//static.wikia.nocookie.net/hypixel-skyblock/images/8/82/Grid_layout_Brewing_Paths.png) no-repeat;
	width: 60px;
	height: 40px;
	margin-top: -21px;
	margin-bottom: -16px;
	z-index: 1;
}
.mcui-Brewing_Stand > .mcui-output {
	display: flex;
	gap: 10px;
}
.mcui-Brewing_Stand .mcui-output .invslot {
	background-image: url(//static.wikia.nocookie.net/hypixel-skyblock/images/5/59/Grid_layout_Brewing_Empty.png);
}
.mcui-Brewing_Stand .mcui-output2 {
	margin-top: 14px;
}

/*
// MC Interface (Anvil)
*/
.mw-parser-output .mcui-Anvil {
	display: flex;
	flex-direction: column;
	justify-content: space-between;
	align-items: center;
	gap: 18px;
}
.mcui-Anvil .mcui-hammer {
	background: url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/8/80/Anvil_Hammer.png/revision/latest?cb=20211203051836&format=original);
	background-size: cover;
	width: 60px;
	height: 60px;
	margin-left: 20px;
}
.mcui-Anvil .mcui-top {
	display: flex;
	gap: 22px;
}
.mcui-Anvil .mcui-topleft {
	display: flex;
	flex-direction: column;
	justify-content: center;
}
.mcui-Anvil .mcui-guibar {
	background: url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/9/93/Anvil_GUI_bar.png/revision/latest?cb=20200518203811&amp;format=original);
	width: 220px;
	height: 32px;
}
.mcui-Anvil .mcui-guitext {
	color: #FCFCFC;
	margin: 4px 6px 0 6px;
}
.mcui-Anvil .mcui-bottom {
	display: flex;
	justify-content: center;
	align-items: center;
	gap: 18px;
	margin-bottom: 16px;
}
.mcui-Anvil .mcui-plus {
	background: url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/2/23/Anvil_Plus.png/revision/latest?cb=20200915220956&amp;version=latest&amp;format=original);
	width: 26px;
	height: 26px;
}
.mcui-Anvil .mcui-arrow {
	background-position-y: -2px;
	width: 44px;
	height: 30px;
}
.mcui-Anvil .mcui-arrow.mcui-disabled {
	background-position-y: 0;
	background-image: url(//static.wikia.nocookie.net/minecraft_gamepedia/images/c/cb/Grid_layout_Anvil_crossed.png);
}
.mcui-Anvil .mcui-cost {
	position: absolute;
	margin: 0;
	padding: 0 8px;
	right: 0;
	bottom: 0;
	max-width: 100%;
	color: #7EFC20;
	text-shadow: 0.125em 0.125em #203E08, 0.125em 0 #203E08, 0 0.125em #203E08;
}
.mcui-Anvil .mcui-cost.mcui-expensive {
	color: #FC5F5F;
	text-shadow: 0.125em 0.125em #3E1818, 0.125em 0 #3E1818, 0 0.125em #3E1818;
}

/* Book */
.mcui-Book_Page {
	position: relative;
	display: flex;
	flex-direction: column;
	padding: 33px 35px 33px 38px;
	margin: 0 auto;
	width: 292px;
	height: 360px;
	
	line-height: 22px;
	font-size: 15px;
	text-align: left;
	word-break: keep-all;
	
	background: url(https://static.wikia.nocookie.net/hypixel-skyblock/images/a/a1/Book_Background.png) no-repeat center top;
}
.mcui-Book_Page .mcui-text {
	color:black;
	font-size: 15px !important;
	text-shadow: unset;
}
.mcui-Book_Page .mcui-text * {
	text-shadow: unset !important;
}
.mcui-Book_Page .mcui-text .format-l {
	font-weight: bold;
}
/* Page content */
.mcui-Book_Page > .mcui-text {
	flex: 1;
}
.mcui-Book_Page .mcui-page-count {
	display: block;
	text-align: right;
	margin: 0 0 12px 0;
}
.mcui-Book_Page .mcui-page-nav {
	display: flex;
	justify-content: space-between;
}
.mcui-Book_Page .mcui-page-nav .invslot {
	all: unset !important;
}

/* Styling for minecraft style tooltip */
/* Taken from minecraft.gamepedia.com */
#minetip-tooltip {
	position: fixed;
	top: 0;
	left: 0;
}
.minetip-static {
	position: relative;
	width: fit-content;
}
#minetip-tooltip, .minetip-static {
	background-color: #100010;
	background-color: rgba(16, 0, 16, 0.94);
	margin: 0.125em 0.25em;
	padding: 0.375em;
	font-family: minecraft, unifontm, unifont, Rubik, serif, sans-serif;
	font-size: 16px;
	line-height: 1.25em;
	white-space: pre;
	z-index: 9999;
	/* white as default */
	color: #fff;
	text-shadow: 0.125em 0.125em #3F3F3F;
	&::before {
		content: "";
		position: absolute;
		top: 0.125em;
		right: -0.125em;
		bottom: 0.125em;
		left: -0.125em;
		border: 0.25em solid #100010;
		border-style: none solid;
		border-color: rgba(16, 0, 16, 0.94);
		pointer-events: none;
	}
	&::after {
		content: "";
		position: absolute;
		top: 0.125em;
		right: 0;
		bottom: 0.125em;
		left: 0;
		border: 0.125em solid #2D0A63;
		border-image: -webkit-linear-gradient(rgba(80, 0, 255, 0.31), rgba(40, 0, 127, 0.31)) 1;
		border-image: linear-gradient(rgba(80, 0, 255, 0.31), rgba(40, 0, 127, 0.31)) 1;
		pointer-events: none;
	}
	* + .minetip-description {
		display: block;
		margin-top: 0.25em
	}
}

/* Element Animator - used in conjunction with JS to cycle through multiple items */
/* Taken from minecraft.gamepedia.com */
#mw-content-text .animated>*:not(.animated-active),
#mw-content-text .animated>.animated-subframe>*:not(.animated-active) {
	display: none;
}
#mw-content-text div.animated.animated-visible,
#mw-content-text span.animated.animated-visible,
#mw-content-text span.animated.animated-visible>*,
#mw-content-text span.animated.animated-visible>.animated-subframe>* {
	display: inline-block;
}
#mw-content-text div.animated.animated-visible>*,
#mw-content-text div.animated.animated-visible>.animated-subframe>* {
	display: block;
}

/* Animator tweaks for this wiki */
#mw-content-text .animated-wrapper {
	position: relative;
	display: inline-block;
	overflow-x: auto;
	.animated-fakeimage {
		visibility: hidden;
		position: relative;
	}
	.animated {
		display: flex;
		justify-content: center;
		position: absolute;
		top: 0;
		height: 100%;
		width: 100%;
		align-items: center;
		&.animated-visible {
			display: inline-flex;
			justify-content: left;
			left: 0;
			.pi-image-thumbnail {
				max-width: none;
			}
		}
	}
}
.mcui.animated-paused::after,
.animated-container.animated-paused:after {
	content: "animations paused";
	position: absolute;
	top: -23px;
	right: -2px;
	font-family: minecraft, unifontm, unifont, Rubik, serif, sans-serif;
	font-size: 12px;
	color: #2B2D2F;
	text-align: right;
	white-space: pre;
	line-height: 12px;
	letter-spacing: .2px;
	background-color: #ae8a8a;
	padding: 3px 3px 5px 5px;
	border-radius: 3px;
	border-top: 2px solid #DBDBDB;
	border-right: 2px solid #5B5B5B;
}

/* Text & Dialogue */
.mcui-text {
	font-family: minecraft, unifontm, unifont, Rubik, serif, sans-serif;
	font-size: 14px;
	/* white as default */
	color: #fff;
	text-shadow: 0.125em 0.125em #3F3F3F;
	/* Experimental: dialogue background */
	padding-top: 0.125em;
	padding-bottom: 0.125em;
	.theme-fandomdesktop-light & {
		filter: brightness(75%); /* global dimming for light theme */
	}
}
.mcdialogue {
	width: fit-content;
	white-space: pre-wrap;
	/* Copy of mcui-text styling (except font-size) */
	font-family: minecraft, unifontm, unifont, Rubik, serif, sans-serif;
	font-size: 11px;
	/* white as default */
	color: #fff;
	text-shadow: 0.125em 0.125em #3F3F3F;
	/* Experimental: dialogue background */
	margin: 0.125em 0.25em;
	padding: 0.125em 0.5em;
	.theme-fandomdesktop-light & {
		background-color: rgba(0, 0, 0, 0.58);
	}
	/* Correct bottom padding */
	& + p {
		margin-top: 24px;
	}
}
/* Game font */
.page-content .hsw-gamefont {
	display: inline;
	font-family: minecrafts, minecraft, unifontm, unifont, Rubik, serif, sans-serif;
	&.cram {
		letter-spacing: -1px;
	}
}


/* Slots with Image ID */
/* Probably a dumb way to do it - but we can change it later */
.invslot span[data-iid="Blank:0"] {
	background-image: url(//static.wikia.nocookie.net/hypixel-skyblock/images/6/64/White_Stained_Glass_Pane.png);
}
.invslot span[data-iid="Blank:1"] {
	background-image: url(//static.wikia.nocookie.net/hypixel-skyblock/images/0/02/Orange_Stained_Glass_Pane.png);
}
.invslot span[data-iid="Blank:2"] {
	background-image: url(//static.wikia.nocookie.net/hypixel-skyblock/images/c/ca/Magenta_Stained_Glass_Pane.png);
}
.invslot span[data-iid="Blank:3"] {
	background-image: url(//static.wikia.nocookie.net/hypixel-skyblock/images/9/9e/Light_Blue_Stained_Glass_Pane.png);
}
.invslot span[data-iid="Blank:4"] {
	background-image: url(//static.wikia.nocookie.net/hypixel-skyblock/images/d/d7/Yellow_Stained_Glass_Pane.png);
}
.invslot span[data-iid="Blank:5"] {
	background-image: url(//static.wikia.nocookie.net/hypixel-skyblock/images/2/23/Lime_Stained_Glass_Pane.png);
}
.invslot span[data-iid="Blank:6"] {
	background-image: url(//static.wikia.nocookie.net/hypixel-skyblock/images/e/ec/Pink_Stained_Glass_Pane.png);
}
.invslot span[data-iid="Blank:7"] {
	background-image: url(//static.wikia.nocookie.net/hypixel-skyblock/images/5/54/Gray_Stained_Glass_Pane.png);
}
.invslot span[data-iid="Blank:8"] {
	background-image: url(//static.wikia.nocookie.net/hypixel-skyblock/images/6/67/Light_Gray_Stained_Glass_Pane.png);
}
.invslot span[data-iid="Blank:9"] {
	background-image: url(//static.wikia.nocookie.net/hypixel-skyblock/images/0/00/Cyan_Stained_Glass_Pane.png);
}
.invslot span[data-iid="Blank:10"] {
	background-image: url(//static.wikia.nocookie.net/hypixel-skyblock/images/7/77/Purple_Stained_Glass_Pane.png);
}
.invslot span[data-iid="Blank:11"] {
	background-image: url(//static.wikia.nocookie.net/hypixel-skyblock/images/3/33/Blue_Stained_Glass_Pane.png);
}
.invslot span[data-iid="Blank:12"] {
	background-image: url(//static.wikia.nocookie.net/hypixel-skyblock/images/a/a4/Brown_Stained_Glass_Pane.png);
}
.invslot span[data-iid="Blank:13"] {
	background-image: url(//static.wikia.nocookie.net/hypixel-skyblock/images/6/65/Green_Stained_Glass_Pane.png);
}
.invslot span[data-iid="Blank:14"] {
	background-image: url(//static.wikia.nocookie.net/hypixel-skyblock/images/b/bd/Red_Stained_Glass_Pane.png);
}
.invslot span[data-iid="Blank:15"] {
	background-image: url(//static.wikia.nocookie.net/hypixel-skyblock/images/6/60/Black_Stained_Glass_Pane.png);
}


/* Put this at the bottom! Add other things before this! */
/* MC Font color codes */
.format-0, .ace_format-0 {
	color: #000 !important;
	text-shadow: 0.125em 0.125em #000000;
}
.format-0 .format-l, .ace_format-0.ace_format_bold,
.format-l .format-0 {
	text-shadow: 0.75px 0, 1.5px 0, 1.5px 2px #000000, 2.35px 2px #000000, 3.2px 2px #000000;
}
.format-1, .ace_format-1 {
	color: #00A !important;
	text-shadow: 0.125em 0.125em #00002A;
}
.format-1 .format-l, .ace_format-1.ace_format_bold,
.format-l .format-1 {
	text-shadow: 0.75px 0, 1.5px 0, 1.5px 2px #00002A, 2.35px 2px #00002A, 3.2px 2px #00002A;
}
.format-2, .ace_format-2 {
	color: #0A0 !important;
	text-shadow: 0.125em 0.125em #002A00;
}
.format-2 .format-l, .ace_format-2.ace_format_bold,
.format-l .format-2 {
	text-shadow: 0.75px 0, 1.5px 0, 1.5px 2px #002A00, 2.35px 2px #002A00, 3.2px 2px #002A00;
}
.format-3, .ace_format-3 {
	color: #0AA !important;
	text-shadow: 0.125em 0.125em #002A2A;
}
.format-3 .format-l, .ace_format-3.ace_format_bold,
.format-l .format-3 {
	text-shadow: 0.75px 0, 1.5px 0, 1.5px 2px #002A2A, 2.35px 2px #002A2A, 3.2px 2px #002A2A;
}
.format-4, .ace_format-4 {
	color: #A00 !important;
	text-shadow: 0.125em 0.125em #2A0000;
}
.format-4 .format-l, .ace_format-4.ace_format_bold,
.format-l .format-4 {
	text-shadow: 0.75px 0, 1.5px 0, 1.5px 2px #2A0000, 2.35px 2px #2A0000, 3.2px 2px #2A0000;
}
.format-5, .ace_format-5 {
	color: #A0A !important;
	text-shadow: 0.125em 0.125em #2A002A;
}
.format-5 .format-l, .ace_format-5.ace_format_bold,
.format-l .format-5 {
	text-shadow: 0.75px 0, 1.5px 0, 1.5px 2px #2A002A, 2.35px 2px #2A002A, 3.2px 2px #2A002A;
}
.format-6, .ace_format-6 {
	color: #FA0 !important;
	text-shadow: 0.125em 0.125em #2A2A00;
}
.format-6 .format-l, .ace_format-6.ace_format_bold,
.format-l .format-6 {
	text-shadow: 0.75px 0, 1.5px 0, 1.5px 2px #2A2A00, 2.35px 2px #2A2A00, 3.2px 2px #2A2A00;
}
.format-7, .ace_format-7 {
	color: #AAA !important;
	text-shadow: 0.125em 0.125em #2A2A2A;
}
.format-7 .format-l, .ace_format-7.ace_format_bold,
.format-l .format-7 {
	text-shadow: 0.75px 0, 1.5px 0, 1.5px 2px #2A2A2A, 2.35px 2px #2A2A2A, 3.2px 2px #2A2A2A;
}
.format-8, .ace_format-8 {
	color: #555 !important;
	text-shadow: 0.125em 0.125em #151515;
}
.format-8 .format-l, .ace_format-8.ace_format_bold,
.format-l .format-8 {
	text-shadow: 0.75px 0, 1.5px 0, 1.5px 2px #151515, 2.35px 2px #151515, 3.2px 2px #151515;
}
.format-9, .ace_format-9 {
	color: #55F !important;
	text-shadow: 0.125em 0.125em #15153F;
}
.format-9 .format-l, .ace_format-9.ace_format_bold,
.format-l .format-9 {
	text-shadow: 0.75px 0, 1.5px 0, 1.5px 2px #15153F, 2.35px 2px #15153F, 3.2px 2px #15153F;
}
.format-a, .ace_format-a {
	color: #5F5 !important;
	text-shadow: 0.125em 0.125em #153F15;
}
.format-a .format-l, .ace_format-a.ace_format_bold,
.format-l .format-a {
	text-shadow: 0.75px 0, 1.5px 0, 1.5px 2px #153F15, 2.35px 2px #153F15, 3.2px 2px #153F15;
}
.format-b, .ace_format-b {
	color: #5FF !important;
	text-shadow: 0.125em 0.125em #153F3F;
}
.format-b .format-l, .ace_format-b.ace_format_bold,
.format-l .format-b {
	text-shadow: 0.75px 0, 1.5px 0, 1.5px 2px #153F3F, 2.35px 2px #153F3F, 3.2px 2px #153F3F;
}
.format-c, .ace_format-c {
	color: #F55 !important;
	text-shadow: 0.125em 0.125em #3F1515;
}
.format-c .format-l, .ace_format-c.ace_format_bold,
.format-l .format-c {
	text-shadow: 0.75px 0, 1.5px 0, 1.5px 2px #3F1515, 2.35px 2px #3F1515, 3.2px 2px #3F1515;
}
.format-d, .ace_format-d {
	color: #F5F !important;
	text-shadow: 0.125em 0.125em #3F153F;
}
.format-d .format-l, .ace_format-d.ace_format_bold,
.format-l .format-d {
	text-shadow: 0.75px 0, 1.5px 0, 1.5px 2px #3F153F, 2.35px 2px #3F153F, 3.2px 2px #3F153F;
}
.format-e, .ace_format-e {
	color: #FF5 !important;
	text-shadow: 0.125em 0.125em #3F3F15;
}
.format-e .format-l, .ace_format-e.ace_format_bold,
.format-l .format-e {
	text-shadow: 0.75px 0, 1.5px 0, 1.5px 2px #3F3F15, 2.35px 2px #3F3F15, 3.2px 2px #3F3F15;
}
.format-f, .ace_format-f {
	color: #FFF !important;
	text-shadow: 0.125em 0.125em #3F3F3F;
}
.format-f .format-l, .ace_format-f.ace_format_bold,
.format-l .format-f {
	text-shadow: 0.75px 0, 1.5px 0, 1.5px 2px #3F3F3F, 2.35px 2px #3F3F3F, 3.2px 2px #3F3F3F;
}
.format-l {
	letter-spacing: 1.5px;
}
.format-m, .ace_format-m {
	text-decoration: line-through;
}
.format-n, .ace_format-n {
	text-decoration: underline;
}
.format-m .format-n, .ace_format-m.ace_format-n,
.format-n .format-m {
	text-decoration: line-through underline;
}
.format-o {
	font-style: italic;
}
/* Don't add things below! Add them above! */
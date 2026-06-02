/* Custom container styling ("boxes") for this wiki */

/* Message Boxes & Text Sections */
/* Coloring impl attributed to Minecraft Wiki (minecraft.fandom.com) */
/* Template:MessageBoxPlus */
.messagebox, .messagebox-inline, .messagebox-boxed {
	--box-background-highlight: ~"rgba(var(--theme-accent-color--rgb), .05)";
	--box-border-highlight: var(--theme-accent-color);
	display: flex;
	justify-content: space-between;
	align-items: center;
	gap: 1em;
	margin: 1em 0;
	padding: .4em 1.6em;
	background-color: var(--box-background-highlight);
	box-shadow: inset 3px 0 0 0 var(--box-border-highlight), inset -3px 0 0 0 var(--box-border-highlight);
	border-radius: .5em;
	border: none;
	font-size: 14px;
	text-align: left;
	overflow: auto;
}
.textsection, .textsection-inline, .textsection-boxed {
	--box-border-highlight: ~"var(--theme-border-color)";
	padding: .5em 1.2em;
	border-radius: .5em;
	border: 1px solid var(--box-border-highlight);
	border-width: 1px 6px;
}
.wikia-menu-button + .textsection {
	margin-top: -14px;
}
.messagebox-inline, .textsection-inline {
	display: inline-flex;
	margin: 0 1em;
}
.messagebox-boxed, .textsection-boxed {
	display: table-cell;
	width: fit-content;
}
.messagebox-main {
	display: flex;
	align-items: center;
	gap: 1em;
}
table.messagebox td {
	/* for messageboxes that still uses a table */
	padding: 0 0.8em;
}
/* Other Message Boxes */
.messagebox-disambiguations {
	font-size: 95%;
	text-align: center;
	margin: 6px auto;
	padding: 0 10px;
	border-radius: 10px;
	display: table;
}
.messagebox-warn, .messagebox-error {
	box-shadow: inset 3px 0 0 0 var(--theme-page-text-color), inset -3px 0 0 0 var(--theme-page-text-color);
	color: #eee;
	a {
		color: #fec356;
	}
}
.messagebox-warn {
	background-color: #905f00;
}
.messagebox-error {
	background-color: #7F0000;
}
/* Dark Message Box - Template:DarkMessageBox */
.darkmsgbox, .quotebox {
	display: grid;
	grid-template-columns: auto 1fr auto;
	grid-template-rows: auto;
	grid-template-areas: "im1    text   im2   "
		"footer footer footer";
	> div {
		display: flex;
		justify-content: center;
		align-content: center;
		flex-direction: column;
	}
}
.darkmsgbox {
	margin: 1em 5px;
	.darkmsgbox-image {
		padding: 15px;
		box-shadow: 0 0 5px var(--box-border-highlight);
		border: 1px solid;
		border-color: var(--box-border-highlight);
		background-color: var(--box-border);
	}
	.darkmsgbox-text {
		padding: 3px 8px;
		box-shadow: 0 0 5px var(--box-border-highlight);
		border: 1px solid;
		border-color: var(--box-border-highlight);
		grid-area: text;
		background-color: var(--box-background-highlight);
	}
	.darkmsgbox-bottom {
		text-align: center;
		box-shadow: 0 0 5px var(--box-border-highlight);
		border: 1px solid;
		border-color: var(--box-border-highlight);
		grid-area: footer;
		.theme-fandomdesktop-dark & {
			background-color: var(--custom-adaptive-extradark);
		}
		.theme-fandomdesktop-light & {
			background-color: #c9c9c9; /* using grayscale */
		}
	}
	.theme-fandomdesktop-dark & {
		--box-background-highlight: var(--custom-adaptive-semidark);
		--box-border: var(--custom-adaptive-lighter);
		--box-border-highlight: var(--theme-accent-color);
	}
	.theme-fandomdesktop-light & {
		--box-background-highlight: var(--custom-adaptive-lighter);
		--box-border: var(--custom-adaptive-semidark);
		--box-border-highlight: var(--theme-accent-color);
	}
}

/* Quote Box */
.quotebox {
	.quotebox-image-left, .quotebox-image-right,
	.quotebox-text, .quotebox-bottom {
		padding: 4px 10px;
	}
	.quotebox-image-left, .quotebox-image-right {
		justify-content: flex-end;
	}
	.quotebox-image-left {
		rotate: 180deg;
	}
	.quotebox-bottom {
		grid-area: footer;
		text-align: right;
	}
}

/* AF Warning Styles */
.afwarning-box {
	.afwarning-mark {
		opacity: 75%;
		min-width: fit-content;
		.theme-fandomdesktop-light & {
			filter: invert(1);
		}
	}
	.afwarning-title {
		font-size: 2.3em;
	}
}
@media only screen and (max-width: 1023px) {
	.afwarning-box .afwarning-mark img {
		max-width: 250px;
		height: auto;
	}
}
@media only screen and (max-width: 785px) {
	.afwarning-box .messagebox-main {
		flex-direction: column;
	}
}

/* Custom widgetbox styling */
.widgetbox {
	--widgetbox-border: #404040;
	--widgetbox-background: var(--custom-adaptive-diffuse);
	--widgetbox-header-background: #432c03;
	--widgetbox-header-border: #c98304;
	.theme-fandomdesktop-light & {
		--widgetbox-border: #a9a9a9;
		--widgetbox-header-background: #ed9a01;
		--widgetbox-header-border: #583900;
	}
}
.widgetbox,
.widgetbox-header {
	margin-bottom: 5px;
}
.widgetbox-content,
.widgetbox-header,
.widgetbox-docktop,
.widgetbox-dockbottom {
	display: block;
	border-radius: 4px;
	padding: 15px;
	text-align: center;
}
.widgetbox-header {
	padding: 10px 15px;
	background-color: var(--widgetbox-header-background);
	font-size: 18px;
	font-weight: bold;
	line-height: 1.25;
	border-bottom: 2px solid var(--widgetbox-header-border);
}
.widgetbox-content,
.widgetbox-docktop,
.widgetbox-dockbottom {
	border-left: 4px solid var(--widgetbox-border);
	border-right: 4px solid var(--widgetbox-border);
}
.widgetbox-docktop,
.widgetbox-dockbottom {
	background: var(--widgetbox-background);
	padding: 3px 15px;
}
.widgetbox-docktop {
	border-radius: 4px 4px 0 0;
}
.widgetbox-dockbottom {
	border-radius: 0 0 4px 4px;
}
.widgetbox.hasdocktop .widgetbox-content {
	border-top-left-radius: 0;
	border-top-right-radius: 0;
}
.widgetbox.hasdockbottom .widgetbox-content {
	border-bottom-left-radius: 0;
	border-bottom-right-radius: 0;
}
.widgetbox .widgetbox-section + .widgetbox-section {
	padding-top: 1em;
}
/* Styling for right side infobox-like widgetbox */
.widgetbox.widgetright {
	float: right;
	margin: 0 0 18px 18px;
	position: relative;
	width: 270px;
}

/* Delete Box */
.delete-box {
	padding: 15px;
	margin: 5px;
	background-color: #7f1d1d;
	text-align: center;
	color: white;
	a {
		color: #fec356;
	}
	hr {
		margin: 0.1em 3px;
		border: 0.5px solid tan;
	}
	.button {
		padding: 10px;
		font-size: 1em;
		font-weight: bold;
		width: 100%;
		height: 100%;
	}
	.delete-box-buttons {
		margin-left: 2%;
		margin-right: 2%;
		font-size: 14px;
		td:first-of-type {
			text-align: left;
		}
		td:last-of-type {
			margin-right: 2em;
		}
	}
	.delete-box-reason {
		font-size: 14px;
	}
}

/* Rightbox */
.hsw-rightbox {
	&.small {
		float: right;
		margin: 5px 2px 2px 5px;
		padding: 14px;
		text-align: center;
		font-size: 75%;
	}
	&.medium {
		float: right;
		width: 240px;
		margin: .1em .1em .5em .25em;
		padding: 4px;
	}
	&.small, &.medium {
		border: 1px solid var(--theme-accent-color);
		box-shadow: 0 0 5px var(--theme-accent-color);
		.theme-fandomdesktop-light & {
			background-color: #ddd; /* using grayscale */
		}
		.theme-fandomdesktop-dark & {
			background-color: var(--custom-adaptive-dark);
		}
	}
	.hsw-rightbox-sep {
		border-bottom: 1px solid #555;
		padding: 0 3px;
		clear: right;
	}
	.hsw-rightbox-image {
		border-right: 0;
		padding: 0 12px;
	}
	.hsw-rightbox-content {
		border-left: 0;
		width: 100%;
		padding: 0 5px 0 0;
	}
}
.hsw-luabox {
	float: right;
	width: 240px;
	margin: .1em .1em .5em .25em;
	padding: 4px;
	box-shadow: 0 0 5px var(--theme-accent-color);
	border: 1px solid var(--theme-accent-color);
	.theme-fandomdesktop-light & {
		background-color: #ddd; /* using grayscale */
	}
	.theme-fandomdesktop-dark & {
		background-color: var(--custom-adaptive-dark);
	}
	.hsw-luabox-list {
		list-style-type: disc;
		margin: 0 0 0 15px;
		white-space: nowrap;
	}
	.hsw-luabox-actions {
		font-size: small;
	}
}
#content .hsw-luabox .hsw-luabox-content {
	border-left: 0;
	padding: 12px 12px 12px 0;
}
#content .hsw-luabox .hsw-luabox-icon {
	border-right: 0;
	padding: 0 12px;
}
.hsw-userbox-list {
	padding: 2.5px
}
.hsw-shortcut-list {
	font-weight: bold;
}
.hsw-archivebox {
	float: right;
	margin: 7px 0;
	border: 2px solid var(--theme-page-text-color);
	box-shadow: 0 0 15px #000000;
	
	.hsw-archivebox-header {
		padding: 1.5px;
	}
	.hsw-archivebox-content {
		padding: 2px 15px;
		background-color: var(--custom-adaptive-light);
	}
	.hsw-archivebox-text {
		padding: 0 15px;
		background-color: var(--custom-adaptive-light);
		text-align: center;
	}
	.hsw-archivebox-list {
		padding: 4px 14px;
		border-top: 2px solid var(--custom-adaptive-extralight);
		border-bottom: 2px solid var(--custom-adaptive-extralight);
	}
	.hsw-archivebox-search {
		padding: 4px;
	}
	.mw-ui-input {
		font-size: small;
	}
	.mw-ui-button {
		height: 32px;
	}
}
.hsw-archivelist {
	.hsw-archivelist-actions {
		font-size: 10px;
	}
}

/* SBTE - Template:CountdownBox */
.sbte-clock,
.sbte-routine {
	visibility: hidden;
}
.sbte-clock-time {
	font-family: minecraft, rubik, serif, sans-serif;
	font-size: 35px;
	margin: 0 0 -10px 0;
}
.sbte-clock-date {
	margin: 0 0 10px 0;
}
.sbte-timestamp,
.cd-waiting {
    color: #777;
}
.cd-ongoing {
    color: #4dcf4d;
	.theme-fandomdesktop-light & {
		color: #349134;
	}
}
.cd-stopped {
    color: #d87093;
}
.countdownbox::before,
.countdownbox::after {
	background-image: url(https://static.wikia.nocookie.net/minecraft_gamepedia/images/3/3e/Clock_JE3_BE3.gif);
	background-size: cover;
	content: "";
	display: block;
	position: absolute;
	width: 22px;
	height: 22px;
}
.countdownbox::before {
	top: 0;
	left: 0;
}
.countdownbox::after {
	bottom: 0;
	right: 0;
}

/* widgetbox */
.widgetbox-wrapper {
	display: flex;
	flex-direction: column;
	min-width: 22em;
	float: right;
	clear: right;
}

/* Tutorial box styling */
.tutorial-box-buttons {
	display: flex;
	justify-content: space-evenly;
	align-items: center;
}
.tutorial-box-inputbox {
	margin: 0 1em;
	max-width: 20em;
}

/* Retro userboxes */
.userbox-retro {
	.userbox-info {
		background-color: var(--custom-adaptive-extralight);
	}
	.userbox-id {
		background-color: var(--custom-adaptive-light);
	}
}

/* Documentation Boxes */
.hsw-documentation {
	border: 1.3px solid var(--theme-page-text-color);
	clear: both;
	
	.hsw-documentation-titlebox {
		padding: 18px 8px 2px 8px;
		margin: 4px 4px 0 4px;
		box-shadow: 0 0 2px var(--theme-page-text-color);
		
		.hsw-documentation-icon {
			float: left;
		}
		.hsw-documentation-header {
			font: bold x-large Arial;
			margin-left: 7px;
			text-align: center;
		}
		.hsw-documentation-actions {
			font-size: small;
			margin-left: 7px;
		}
		.hsw-documentation-tnote {
			font-size: small;
			font-style: italic;
		}
		.page-header__separator {
			background-color: var(--theme-accent-label-color);
			border: 0;
			height: 1px;
			margin-bottom: 3px;
			margin-top: 0;
			width: 100%;
		}
		p {
			margin: 0;
		}
	}
	.hsw-documentation-body {
		background-color: rgba(120,120,120,0.05);
		box-shadow: 0 0 2px var(--theme-page-text-color);
		padding: 0.5em;
		margin: 0 4px;
		padding: 20px 20px 10px;
		clear: both;
		
		.hsw-documentation-main-idk {
			display: none;
		}
		.hsw-documentation-main-pd {
			clear: both;
			margin-bottom: 5px;
		}
	}
	.hsw-documentation-bottombox {
		padding: 2px 8px;
		margin: 0 4px 4px 4px;
		box-shadow: 0 0 2px var(--theme-page-text-color);
		
		.hsw-documentation-hdtw {
			margin: 5px;
			font-weight: bold;
		}
	}
	.hsw-documentation-jtc, .hsw-documentation-btt {
		float: right;
		margin-top: 4px;
		font-style: italic;
		font-size: small;
	}
}

/* Dark Table (Front Page) */
.darkTable-wrapper {
	background: var(--custom-adaptive-dark);
	padding: .8em .6em;
	margin-bottom: 1em;
	border-radius: 12px;
	border-top: 4px solid #303030;
	border-bottom: 1px solid #303030;
	.theme-fandomdesktop-light & {
		background: var(--custom-adaptive-extralight);
		border-top-color: #adadad;
		border-bottom-color: #adadad;
	}
}
.darkTable-wrapper table, .darkTable {
	width: 100%;
	table-layout: fixed;
}
.darkTable-wrapper td, .darkTable td {
	vertical-align: top;
}
.darkTable-wrapper.hlist {
	text-align: center;
}
.darkTable-wrapper ul {
	margin-left: 8px;
	margin-right: 8px;
}
.darkTable-wrapper li {
	list-style-type: none;
}
.darkTable-wrapper li a {
	letter-spacing: 1.2px;
}
.darkTable-wrapper li img {
	margin-right: 10px;
}

/* Box Colors (Place at bottom) */
.mw-parser-output {
	.boxcol-blue {
		--box-background-highlight: var(--custom-background-blue-highlight);
		--box-border-highlight: var(--custom-border-blue-highlight);
		--box-background: var(--custom-background-blue);
		--box-border: var(--custom-border-blue);
	}
	.boxcol-green {
		--box-background-highlight: var(--custom-background-green-highlight);
		--box-border-highlight: var(--custom-border-green-highlight);
		--box-background: var(--custom-background-green);
		--box-border: var(--custom-border-green);
	}
	.boxcol-orange {
		--box-background-highlight: var(--custom-background-orange-highlight);
		--box-border-highlight: var(--custom-border-orange-highlight);
		--box-background: var(--custom-background-orange);
		--box-border: var(--custom-border-orange);
	}
	.boxcol-purple {
		--box-background-highlight: var(--custom-background-purple-highlight);
		--box-border-highlight: var(--custom-border-purple-highlight);
		--box-background: var(--custom-background-purple);
		--box-border: var(--custom-border-purple);
	}
	.boxcol-red {
		--box-background-highlight: var(--custom-background-red-highlight);
		--box-border-highlight: var(--custom-border-red-highlight);
		--box-background: var(--custom-background-red);
		--box-border: var(--custom-border-red);
	}
	.boxcol-yellow {
		--box-background-highlight: var(--custom-background-yellow-highlight);
		--box-border-highlight: var(--custom-border-yellow-highlight);
		--box-background: var(--custom-background-yellow);
		--box-border: var(--custom-border-yellow);
	}
	.boxcol-magenta {
		--box-background-highlight: var(--custom-background-magenta-highlight);
		--box-border-highlight: var(--custom-border-magenta-highlight);
		--box-background: var(--custom-background-magenta);
		--box-border: var(--custom-border-magenta);
	}
	.boxcol-gray {
		--box-background-highlight: var(--custom-background-grey); /* no highlight defined, yet */
		--box-border-highlight: var(--custom-border-grey); /* no highlight defined, yet */
		--box-background: var(--custom-background-grey);
		--box-border: var(--custom-border-grey);
	}
}
/**
 * This page is for stylings that are for classes that we create for our own use in certain site components
 * For fixes of site elements that are not created by us, consider using general.less
*/

/************************************/
/** COMMON CLASSES FOR GENERAL USE **/
/************************************/

/* Custom text styling */
body .page-content .ct,
body .page-content .centertext,
body .page-content .centertxt {
	text-align: center;
}
body .page-content .lefttext,
body .page-content .lefttxt {
	text-align: left;
}
body .page-content .righttext,
body .page-content .righttxt {
	text-align: right;
}
body .size-small, body .smalltxt {
	font-size: small;
}
.align-top {
	vertical-align: top;
}
.align-middle {
	vertical-align: middle;
}
.align-bottom {
	vertical-align: bottom;
}
.bold {
	font-weight: bold;
}
.italic {
	font-style: italic;
}
.narrow {
	letter-spacing: -0.5px;
}
.monospace {
	font-family: Consolas, monospace;
}
.font-initial {
	font-family: initial;
}
.txt-nowrap {
	white-space: nowrap;
}
.txt-wrap {
	white-space: normal;
}
.cursor-help {
	cursor: help;
}
.superscript {
	vertical-align: super;
}
.subscript {
	vertical-align: sub;
}
.pixelated {
	image-rendering: pixelated;
}

/* Custom image styling */
img.img-banner {
	border-radius: 6px;
	max-width: 100%;
	max-height: 600px;
	width: auto;
	height: auto;
}
img.img-width-100 {
	width: 100%;
	height: auto;
}
/*
img.img-width-90 {
	width: 90%;
	height: auto;
}
img.img-width-80 {
	width: 80%;
	height: auto;
}
img.img-width-70 {
	width: 70%;
	height: auto;
}
img.img-width-60 {
	width: 60%;
	height: auto;
}
img.img-width-50 {
	width: 50%;
	height: auto;
}
img.img-width-40 {
	width: 40%;
	height: auto;
}
*/

/* Custom padding/margins/widths/float */
body .p-margin {
	margin-bottom: 24px;
}
body .box-margin-1 {
	margin: 1em;
}
body .margin-centered {
	margin-left: auto;
	margin-right: auto;
}
.page-content .full-width-1 {
	min-width: 100%;
}
.page-content .full-width {
	margin-left: 0;
	margin-right: 0;
	width: 100%;
	width: -moz-available;
	width: -webkit-fill-available;
	width: fill-available;
}
.page-content .half-width {
	width: 50%;
}
.float-left {
	float: left;
}
.float-left-padded {
	float: left;
	margin-right: 25px;
}
.float-right {
	float: right;
}
.float-right-padded {
	float: right;
	margin-left: 25px;
}
.clear-left {
	clear: left;
}
.clear-right {
	clear: right;
}
.clear-both {
	clear: both;
}
.article-columns-2 {
	columns: 150px 2;
}
.article-columns-3 {
	columns: 100px 3;
}
.article-columns-2, .article-columns-3 {
	ul, ol {
		margin-top: 0;
		margin-bottom: 0;
	}
}
.page-content .inline-block {
	display: inline-block;
}

/* custom flexbox styling */
.display-flex {
	display: flex;
}
.simple-flexbox {
	display: flex;
	flex-wrap: wrap;
}
.display-table {
	display: table;
}

/* custom table styling */
.page-content table {
	&.table-margin-off {
		margin: 0;
	}
	tr td.table-margin-off {
		padding: 0;
	}
	.table-section-separator, .table-section-separator-top {
		border-top: 3px solid var(--theme-border-color);
		&.thick {
			border-top-width: 5px;
			border-top-color: var(--theme-accent-color);
		}
	}
	.table-section-separator-bottom {
		border-bottom: 3px solid var(--theme-border-color);
		&.thick {
			border-bottom-width: 5px;
			border-bottom-color: var(--theme-accent-color);
		}
	}
	.table-section-separator-left {
		border-left: 3px solid var(--theme-border-color);
		&.thick {
			border-left-width: 5px;
			border-left-color: var(--theme-accent-color);
		}
	}
	.table-section-separator-right {
		border-right: 3px solid var(--theme-border-color);
		&.thick {
			border-right-width: 5px;
			border-right-color: var(--theme-accent-color);
		}
	}
}
.table-nocollapse {
	display: table-row !important;
}
.table-vedbuttons {
	float: right;
	font-size: 11px;
}
.table-fixed {
	table-layout: fixed;
}
/* Vertical cell support */
.vertical th,
.vertical td,
td.vertical,
th.vertical {
	writing-mode: vertical-rl;
}
/* Darkens every other row */
.oddrow tr:nth-of-type(odd)>td,
tr.oddrow td {
	background: #85858530;
}
.oddrow2 tr:nth-of-type(odd)>td,
tr.oddrow2 td {
	background: #85858548;
}

/* Article Scrollbar Tweaks */
.article-scrollable {
	overflow: auto;
}
.article-scrollable, .table-wide-inner {
	/* Article Scrollbar Tweaks (Firefox) */
	scrollbar-width: thin;
	/*scrollbar-color: #897e81 #50373a;*/
	&::-webkit-scrollbar {
		width: 10px;
		height: 10px;
	}
	&::-webkit-scrollbar-track {
		background-color: rgba(80, 55, 58, 0.5);
	}
	&::-webkit-scrollbar-thumb {
		background-color: rgba(137, 126, 129, 0.5);
	}
	&::-webkit-scrollbar-thumb:hover {
		background-color: rgba(110, 101, 104, 0.5);
	}
}

/* Disables text highlighting on browsers */
.noselect, .invslot, .mcui {
	-webkit-touch-callout: none;
	-webkit-user-select: none;
	-khtml-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

/* Bull Character */
.bull-c::before {
	content: "\2022";
	margin: 0 4px;
}

/* General hide class to be used as necessary (pair to .mobile-hide) */
.desktop-hide, .hidden {
	display: none !important;
}

/* Blank Cells */
th:has(.blankCell),
td:has(.blankCell) {
	position: relative;
}
th .blankCell,
td .blankCell {
	display: flex;
	cursor: not-allowed;
	/*background: rgba(150, 150, 150, 0.15);*/
	text-align: center;
	font-size: 65%;
	color: transparent;
	/* We only want to show what is in ::after, but still want an actual character in the template so the character is selectable */
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
	&:after {
		content: "∅";
		flex: 1;
		align-self: center;
		color: rgba(185, 185, 185, 0.55);
	}
}

/* Dimmer */
/* Note: This is for use in scripts. Appending this to document.body will work */
@keyframes hsw-dimmer-effect {
	from {
		opacity: 0;
	}
	to {
		opacity: 0.8;
	}
}
.hsw-site-dimmer {
	content: '';
	position: fixed;
	z-index: -2;
	width: 100%;
	height: 100%;
	top: 0;
	left: 0;
	background-color: #000;
	opacity: 0;
	transition: opacity .7s linear 0s;
}

/***********************************/
/** SPECIFIC STYLING FOR ELEMEMTS **/
/***********************************/

/* Comment id */
.comment-id-display,
.reply-id-display {
	color: var(--theme-page-text-color);
	text-align: right;
}
.comment-id-display abbr,
.reply-id-display abbr {
	font-size: .8em;
	text-align: right;
	cursor: default;
	text-decoration: none;
	padding: .4em 1em;

	&:hover {
		background-color: rgba(254, 195, 86, .1);
		color: var(--theme-link-color);
	}
}
.comment-id-display {
	margin: 0 1em;
}

/* Article Comments Notice */
#articleCommentsNotice {
	text-align: left;
	margin-top: 1em;
	line-height: 1.8em;
	border: thin solid #F55;
	padding: 1em;
}

/* Fetchur request styling */
.article-fetchur-request {
	overflow-x: hidden;
	font-size: medium;
}

/* Preloaded Styles for Tooltips Editor */
.editTooltips-Loading {
	padding: 1em;
	outline: #a2a2a2 groove;
	border: thin transparent solid;
}
.editTooltips-Loading img {
	max-width: 100%;
	height: auto;
}

/* Preloaded Styles for JSCalculator */
.jcConfig {
	display: none;
}
.jcLoadspace {
	width: 40%;
	border: 1px var(--theme-accent-color) solid;
	margin: 2em 0;
	padding: 2em;
	color: var(--theme-accent-color);
}

/* Gemstone slots */
.gemstone-slot {
	position: relative;
	display: inline-flex;
	width: 25px;
	height: 25px;
	line-height: 25px;
	border: 1px solid currentColor;
	border-radius: 3px;
	justify-content: center;
	align-items: center;
	cursor: help;
	a {
		color: currentColor;
		cursor: help;
		width: 100%;
		text-align: center;
	}
	.gemstone-slot-lock {
		position: absolute;
		bottom: -2px;
		right: -2px;
		font-size: 10px;
		line-height: 1;

		&:after {
			content: '🔒';
		}
	}
}
.gemstone-slot-list {
	display: flex;
	gap: 3px;
	justify-content: center;
}

/* Highlight table */
/* Mediawiki:Highlight.js */
.lighttable tr {
	cursor: pointer;
}
.lighttable tr.highlight-over th,
.lighttable tr.highlight-over td {
	background-color: ~"rgba(var(--theme-accent-color--rgb), .23)";
}
.lighttable tr.highlight-on th {
	background-color: var(--theme-accent-color);
}
.lighttable tr.highlight-on td {
	background-color: ~"rgba(var(--theme-accent-color--rgb), .5)";
}
.highlight-over .tier-rare,
.highlight-on .tier-rare {
	text-shadow: none;
}

/* Keypress */
.keypress-diagram {
	white-space: nowrap;
	padding: 1px 6px;
	border: 1px solid #CCC;
	border-radius: 3px;
	box-shadow: 0.1em 0.2em 0.2em rgba(0, 0, 0, 0.2);
	font-size: 0.85em;
	font-family: Arial,Helvetica,sans-seri;
}

.article-new-feature {
	color: white;
	background: red;
	padding: 1px 3px;
	border-radius: 5px;
	border: 2px dotted darkred;
	text-decoration: underline dotted;
}

/* Template:ArmorStats Styling */
table.armorstats2x2 {
	margin-right: 0;
}
.armorstats2x2 th {
	min-width: 184px;
}
.armorstats2x2 .as2x2-icon {
	padding: 0 3px;
}
.armorstats2x2 .as2x2-item-stats {
	padding: 0 5px;
}
.armorstats2x2 .as2x2-item-stats ul {
	line-height: inherit;
	list-style: none none;
	margin: 0;
}

/* Edittools styling */
#editpage-custom-description {
	margin-top: 3em;
	margin-bottom: 0.7em;
}
#editpage-specialchars {
	background-color: rgba(120, 120, 120, 0.05);
	border-radius: 6px;
	padding: 12px;
	font-size: small;
	a {
		font-family: monospace;
	}
	hr {
		color: #e6e6e6;
	}
	.mw-charinsert-item {
		min-width: 1.2em;
	}
}
#editpage-custom-footer {
	float: right;
}

/* Recent change link box styling */
#recentchange-custom-links {
	font-family: Arial;
	background-color: rgba(120, 120, 120, 0.05);
	border-radius: 6px;
	padding: 12px;
	border: .5px solid #e6e6e6;
	hr {
		background-color: #e6e6e6;
		border: 0;
		height: 1px;
	}
}

/* Hide Pagestyles */
.pageStyles {
	display: none !important;
}

/* Treeview */
/* Attributed to: Minecraft Wiki (minecraft.fandom.com) */
.page-content .treeview {
	margin-top: 0.3em;
	overflow-x: auto;
	.treeview-header {
		padding-left: 3px;
		font-weight: bold;
		&:last-child {
			border-color: #636363 !important;
			border-left-style: dotted;
		}
		&:not(:last-child):before {
			content: none;
		}
		&:last-child:before {
			border-bottom: 0;
		}
	}
	ul, li {
		&, &:last-child {
			margin: 0;
			padding: 0;
			list-style-type: none;
			list-style-image: none;
		}
	}
	li li {
		&, &:last-child {
			position: relative;
			padding-left: 13px;
			margin-left: 7px;
			border-left: 1px solid #636363;
		}
		&:before {
			content: "";
			position: absolute;
			top: 0;
			left: -.8px;
			width: 11px;
			height: 11px;
			border-bottom: 1px solid #636363;
		}
		&:last-child:not(.treeview-continue) {
			border-color: transparent;
			&:before {
				border-left: 1px solid #636363;
				width: 10px;
			}
		}
	}
}

/** Element custom styling **/
/* preformatted text custom styling */
pre.dark, pre .dark {
	background-color: #002b36;
}
/* horizontal rule custom styling */
hr.tan-line, hr .tan-line {
	margin: 0.1em 2px;
	border: 0.5px solid tan;
}
hr.weak-line, hr .weak-line {
	background-color: #5e484a;
	border: 0;
	height: 1px;
}

/* code block custom styling */
.inset-code {
	background-color: #cacaca;
	padding: 1px 1px;
	border-radius: 3px;
	font-family: monospace;
	color: black;
	border: 1.1px solid #383838;
	display: inline;
	position: relative;
	vertical-align: bottom;
	white-space: pre;
}

/* Color Preview & Color Display styling */
.color-preview-box {
	position: relative;
	display: inline-block;
	background: #3f3233;
	padding: 0 10px;
	line-height: 30px;
}
.color-preview-block {
	position: relative;
	display: inline-block;
	top: 5px;
	height: 23px;
	width: 23px;
	margin-right: 5px;
	border: 1px solid white;
	border-radius: 12px;
}
.color-display-table {
	display: grid;
	grid-template-columns: max-content max-content;
	gap: 2px 16px;
	margin: 1em 0;
	.col-name {
		text-align: right;
	}
}
.color-display-block {
	padding: 0 8px;
	display: inline;
	border: 1px solid;
}

/* No article text styling */
.noarticletext-header {
	font: bold 150% Arial;
	border-bottom: 1px solid #5e484a;
	padding-bottom: .5em;
	margin: 1em 0;
}
.noarticletext-block {
	hr {
		margin-top: 2em;
	}
}

/* Page Header styling */
.article-pageheader {
	margin: 1em 0;
	box-shadow: 0 0 5px #fff;
}
.article-pageheader-title {
	padding: 1em 4em;
	background: ~"rgba(var(--theme-accent-color--rgb),0.7)";
}
.article-pageheader-body {
	padding: 1em 4em;
	background-color: ~"rgba(var(--theme-accent-color--rgb),0.2)";
}

/* Good article, featured article (Project:GA, Project:AOTM) */
.article-featured-article-icon,
.article-good-article-icon {
	display: inline-block;
	border-radius: 4px;
	padding: 0 6px;
	img {
		vertical-align: sub;
	}
}
.article-featured-article-icon {
	background-color: #65432130;
}
.article-good-article-icon {
	background-color: #21653230;
}

/* Pet display styling */
.article-petlevelstats-title {
	width: 70%;
	font-size: 3em;
	white-space: nowrap;
	padding: 0 1em !important;
}
.article-petlevelstats-level {
	font-size: 1.6em;
}
.article-petlevelstats-tier {
	font-size: 1.6em;
}
.article-petlevelstats-slot {
	float: right;
}
.page-content table.wikitable tr td.article-petlevelstats-main {
	padding: 1em 2em 0 2em !important;
}
.article-petstats-title {
	font-size: 1.6em;
	text-align: center;
	margin: .5em 0;
}
.article-petstats-abilities {
	list-style-type: circle;
	line-height: inherit;
}
.article-petstats-helditem {
	list-style-type: none;
	line-height: inherit;
}

/* Minion page styling */
.article-msTable-cumulative {
	display: flex;
	justify-content: space-between;
	align-items: center;
}
.article-minion-smallTabs {
	min-width: 3.8em;
}
.article-minion-coolLabel {
	font: bold 100% times new roman;
}

/* Used on potions and enchantments page */
.dual-table-grid {
	display: grid;
    grid-template-columns: 1fr 1fr;
    margin: 12px 0;
    overflow-x: auto;
    
    table {
		margin: 0;
		height: 100%;
	}
	.seperator-cell {
		border-bottom: 5px solid var(--theme-accent-color);
	}
	@media screen and (max-width: 800px) {
		grid-template-columns: 1fr;
	}
}

/* Enchantment table row */
.article-enchantments-table {
	.enchnamediv {
			display: flex;
			gap: 16px;
	}
	.enchreqdiv {
		flex: 1;
		text-align: right;
		font-weight: normal;
	}
	.enchdisctr {
		height: 100%;
		> td {
			text-align: left;
			vertical-align: top;
		}
	}
	.enchaffectsdiv {
		float: right;
		display: flex;
		align-items: center;
		gap: 1ex;
		margin: -3px -5.5px 0 10px;
		padding: 0 5px;
		border: 1px solid var(--theme-border-color);
		border-top: 0 !important;
		border-right: 0 !important;
		border-bottom-left-radius: 5px;
		> div {
			display: flex;
			gap: 0 1ex;
			text-align: center;
		}
	}
}

/* TOC styling */
.article-custom-toc {
	width: 55%;
	p {
		margin-bottom: 0;
	}
	.content {
		border-top: 1px solid #aaa;
		border-bottom: 1px solid #aaa;
		margin: 10px 0;
		padding: 10px 0;
		max-height: 400px;
		overflow: auto;
		.inner {
			columns: 100px 3;
		}
	}
}

/* Tutorials */
.tut-nav {
	display: grid;
	margin-top: 32px;
	gap: 16px;
	grid-template-columns: repeat(2,1fr);
}
.tut-nav a {
    display: block;
    color: var(--theme-accent-color);
    padding: 18px;
    border: 1px solid var(--theme-border-color);
    border-radius: 6px;
    line-height: 1.2;
    transition: border-color .2s ease-out;
    font-weight: 700;
    &::before {
	    color: var(--theme-body-text-color);
	    font-size: 95%;
	    font-weight: 600;
	}
	&:hover {
	    border-color: var(--theme-accent-color);
	    text-decoration: none;
	    .label {
			text-decoration: none;
		}
	}
}
.tut-next a {
    text-align: right;
    &::before {
	    content: "Next";
	}
    .label::after {
		content: " »";
	}
}
.tut-prev a {
	&::before {
	    content: "Previous";
	}
	.label::before {
		content: "« ";
	}
}
.tut-browse ul {
	display: grid;
	grid-template-columns: repeat(3, 1fr);
	gap: 6px 20px;
	list-style: none;
	margin-left: 0;
}
@media only screen and (max-width: 1023px) {
	.tut-browse ul {
		grid-template-columns: repeat(2, 1fr);
	}
}
.tut-browse li a {
	display: flex;
	padding-right: 14px;
	color: var(--theme-body-text-color);
	font-weight: 700;
	border-radius: 6px;
	height: 100%;
	&:hover {
		color: black;
		text-decoration: none;
		.theme-fandomdesktop-light & {
			color: white;
		}
		.label {
			text-decoration: none;
		}
	}
	&::before {
		content: "Tutorial ";
		display: flex;
		align-items: center;
		margin-right: 14px;
		padding: 5px 14px 5px 14px;
		border-radius: 6px 0 0 6px;
		color: black;
		.theme-fandomdesktop-light & {
			color: white;
		}
	}
	.label {
		align-self: center;
	}
}
.tut-browse li:nth-child(4n+1) a:hover {
	background: #b33636;
}
.tut-browse li:nth-child(4n+1) a::before {
	background: #e04141;
}
.tut-browse li:nth-child(4n+2) a:hover {
	background: #3e59ad;
}
.tut-browse li:nth-child(4n+2) a::before {
	background: #778ac4;
}
.tut-browse li:nth-child(4n+3) a:hover {
	background: #b1901d;
}
.tut-browse li:nth-child(4n+3) a::before {
	background: #d3b54e;
}
.tut-browse li:nth-child(4n+4) a:hover {
	background: #2e7a20;
}
.tut-browse li:nth-child(4n+4) a::before {
	background: #72a251;
}

/* Game icons */
.page-content .staticon {
	vertical-align: text-bottom;
}

/* Switches */
.hover-switch .hov, .hover-switch:hover .nohov {
    display: none;
}
.hover-switch:hover .hov {
    display: inherit;
}

/* Inline Tooltip */
.linetip {
	padding-bottom: 3px;
	border-bottom: 1px dotted currentColor;
	cursor: help;
}

/* Theme Adaptive Items */
.theme-fandomdesktop-light .themeadapt-dark {
	display: none;
}
.theme-fandomdesktop-dark .themeadapt-light {
	display: none;
}
.theme-fandomdesktop-light .themeinvert-light {
	filter: invert(1);
}
.theme-fandomdesktop-dark .themeinvert-dark {
	filter: invert(1);
}

/* Circled yes/no */
.circled-y:before, .circled-n:before {
	display: inline-flex;
	justify-content: center;
	width: 28px;
	height: 28px;
	margin-right: 5px;
	border-radius: 50%;
	line-height: 1.5;
}
.circled-y:before {
	border: 3px solid #7ec525;
	color: #7ec525;
	content: '✔';
}
.circled-n:before {
	border: 3px solid #aaa;
	color: #aaa;
	content: '✘';
}
.circled-y.centered, .circled-n.centered {
	display: block;
	text-align: center;
}

.cl-badge {
	padding: 2px 5px;
	border-radius: 4px;
	background-color: #007bff;
	line-height: 1.95;
	color: white;
	font-size: 80%;
	font-weight: bold;
	text-align: center;
}
a .cl-badge,
.cl-badge a {
	color: white;
}
a.external .cl-badge:after,
.cl-badge.cl-icon:after {
	content: "";
	background-size: cover;
	display: inline-block;
	position: relative;
	top: 2px;
	margin: 0 2px;
	width: 12px;
	height: 12px;
	filter: invert(1);
}
a.external .cl-badge:after {
	background-image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij48cGF0aCBkPSJNMjEgMTN2MTBoLTIxdi0xOWgxMnYyaC0xMHYxNWgxN3YtOGgyem0zLTEyaC0xMC45ODhsNC4wMzUgNC02Ljk3NyA3LjA3IDIuODI4IDIuODI4IDYuOTc3LTcuMDcgNC4xMjUgNC4xNzJ2LTExeiIvPjwvc3ZnPg==); /* https://iconmonstr.com/share-11-svg/ */
}
.cl-badge.cl-icon:after {
	background-image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij48cGF0aCBkPSJNMjIgNnYxNmgtMTZ2LTE2aDE2em0yLTJoLTIwdjIwaDIwdi0yMHptLTI0LTR2MjBoMnYtMThoMTh2LTJoLTIweiIvPjwvc3ZnPg==); /* https://iconmonstr.com/layer-1-svg/ */
}
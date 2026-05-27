/***** CSS placed here will be applied to all skins on the entire site. *****/

/* Core Layout */
.page-content, .page-content p {
    line-height: 1.95;
}
.page-header__bottom {
	align-items: flex-end;
}

/* Shrinked NS Prefix for Project Namespace */
.ns-4 .mw-page-title-namespace, .ns-4 .mw-page-title-separator {
	font-size: 24px;
}
.ns-4 .mw-page-title-main {
	display: block;
}

/* Page header styling */
.fandom-community-header__community-name {
	font-size: 22px;
	font-weight: 600;
}
.page-counter {
	font-weight: 600;
}
@media only screen and (max-width: 1279px) {
	.fandom-community-header__image img {
		object-position: 0 10px;
	}
}
@media only screen and (min-width: 1280px) {
	.fandom-community-header__community-name {
		font-size: 25px;
	}
}
body a.fandom-community-header__community-name:hover,
body a.fandom-community-header__community-name:active,
body a.fandom-community-header__community-name:focus,
body a.fandom-sticky-header__sitename:hover,
body a.fandom-sticky-header__sitename:active,
body a.fandom-sticky-header__sitename:focus {
	text-decoration: none;
}

/* Style all headings (h2, h3, etc) */
.page-content *:not(.toctitle)>h2:not([class]):not(#mw-previewheader),
.page-content h1:not([class]):not(#firstHeading) {
	.theme-fandomdesktop-light & {
		background-color: #e4e4e4;
		background-color: rgba(0, 0, 0, 0.1);
	}
	.theme-fandomdesktop-dark & {
		background-color: #2d1616;
		background-color: rgba(0, 0, 0, 0.1);
	}
	padding: 4px;
	text-transform: capitalize;
	a:not(.mw-editsection a) {
		color: inherit;
		&:hover {
			color: var(--theme-link-color--hover);
			text-decoration: none;
		}
	}
}
.page-content h1:not([class]):not(#firstHeading) {
	border-bottom: 1px solid var(--theme-border-color);
	overflow: hidden;
}
.page-content h2 {
	overflow: hidden;
}
/* Shrinks excessive space between content/headers and subheaders */
.page-content h3:not([class]),
.page-content h4:not([class]),
.page-content h5:not([class]),
.page-content h6:not([class]) {
	border-bottom: 1px solid var(--theme-border-color);
	padding: 4px 0;
	width: fit-content;
	a:not(.mw-editsection a) {
		color: inherit;
		&:hover {
			color: var(--theme-link-color--hover);
			text-decoration: none;
		}
	}
}
/* Alternating italic styles for h3/h4 and h5/h6 for level clarity */
.page-content h4:not([class]),
.page-content h6:not([class]) {
	font-style: italic;
}

/* Lists */
.mw-parser-output li:not([class]) {
	font-size: inherit !important;
	line-height: inherit !important;
}
.mw-parser-output li {
	line-height: 20px;
	font-size: 14px;
}
ul.lowmargin {
	margin-left: 1.5em;
}

/* Holiday Guy in userboxes (disabled) */
/* #userProfileApp .user-identity-box__wrapper {
	position: relative;
	background: url(https://static.wikia.nocookie.net/hypixel-skyblock/images/1/1f/Holiday_Guy.png/revision/latest/scale-to-width-down/175?cb=20201210211322) bottom right no-repeat;
} */

/* General Link fixes */
a.page-title-link:hover {
	text-decoration: underline;
}
/* Fix link icons */
/*
a[href*="/wiki/"].external:after,
a[href*=".fandom.com"].external:after,
a[href*=".wikia.org"].external:after {
	display: none !important;
}
*/
/* Fix redlinks */
/*
a[classname="new"]:hover {
	color: var(--theme-alert-color--hover) !important;
	-webkit-text-decoration-style: dashed !important;
	text-decoration-style: dashed !important;
}
a[classname="new"] {
	color: var(--theme-alert-color) !important;
	-webkit-text-decoration-style: dashed !important;
	text-decoration-style: dashed !important;
}
*/

/* Fix article Links having incorrect underline colors */
.mw-parser-output a:is(:hover, :active, :focus) * {
	text-decoration: underline;
	text-decoration-color: currentcolor;
}

/* Code Box Styling */
.code,
code.dark {
	background-color: rgba(0, 0, 0, 0.35) !important;
	padding: 1.5px !important;
	border-radius: 3px !important;
	tab-size: 4 !important;
	font-family: monospace !important;
	white-space: pre !important;
}
.dark-code-box {
	border: 1px solid #5e484a;
	line-height: 14px;
	overflow: auto;
	padding: 12px;
	word-wrap: normal;
	color: #93a1a1;
	font-family: monospace;
}

/* Abbr styling */
abbr[title],
span[title] {
	-webkit-text-decoration: underline dotted;
	text-decoration: underline dotted;
	cursor: help;
	border-bottom: none;
}
@media(hover: none) and (pointer: coarse) {
	abbr[title]:focus::before,
	span[title]:focus::before {
		content: attr(title);
		position: absolute;
		background-color: #1f1f1f;
		border: 1px solid var(--theme-border-color);
		border-radius: 4px;
		padding: 3px 8px;
		color: white;
		font-size: 14px;
		font-weight: 400;
		line-height: 1.5;
		text-align: left;
		text-transform: none;
		transform: translateY(1.6rem);
		white-space: pre-wrap;
		z-index: 100;
		.theme-fandomdesktop-light & {
			background-color: #5f5f5f;
		}
	}
}

/* <ref> <references /> styling */
ol.references li:target,
sup.reference:target {
	background: unset !important;
	border-color: #fff;
	border-radius: 3px;
}

/* changeslist Styling */
.mw-changeslist table {
	margin: 2px !important;
	margin-left: 0 !important;
}
.mw-changeslist-legend {
	background-color: rgba(0, 0, 0, 0.35) !important;
}

/* Removing the white-ish background from various elemnts */
.admin-dashboard__module,
.AdminDashboard .admin-dashboard-content .control-section,
.mw_metadata,
.CategorySelect.articlePage,
.cm-mw-skipformatting {
	background: unset;
}

/* <pre> styling */
.WikiaMainContent pre:not([class]),
.oo-ui-tagMultiselectWidget.oo-ui-widget-enabled.oo-ui-tagMultiselectWidget-outlined .oo-ui-tagMultiselectWidget-handle,
.ooui-theme-fandomooui .mw-rcfilters-ui-filterTagMultiselectWidget.oo-ui-widget-enabled .oo-ui-tagMultiselectWidget-handle+.mw-rcfilters-ui-table {
	background-color: rgba(0, 0, 0, 0.35);
}

/* Admin Dashboard */
.admin-dashboard__module,
.AdminDashboard .admin-dashboard-content .control-section {
	border: 1px solid #9b8d8e;
}
.AdminDashboardTabs .tab.active {
	background-color: rgba(248, 192, 85, 0.35);
	border-color: rgba(248, 192, 85, 0.8);
}
.AdminDashboardTabs .tab:hover {
	background-color: rgba(248, 192, 85, 0.5);
	transition-property: background, border;
	transition-delay: 0.3s;
}

/* Article-table and Wikitable CSS */
.mw-parser-output .wikitable.lowpadding th,
.mw-parser-output .wikitable.lowpadding td {
	padding: 2px;
}
.article-table th {
	text-align: center;
}
.wikitable td,
.article-table td {
	overflow: hidden;
	position: relative;
	padding: 4px;
	background-color: var(--theme-page-background-color);
	background-clip: padding-box;
}
.mw-parser-output .article-table tr th,
.mw-parser-output .wikitable tr th {
	padding: 2.8px 5.6px;
	background-clip: padding-box;
}
.wikitable tr th {
	.theme-fandomdesktop-light & {
		background-color: #e6e6e6; /* using grayscale */
	}
	.theme-fandomdesktop-dark & {
		background-color: #111; /* using grayscale */
	}
}

/* Table fixes */
table[align="center"] {
	margin: auto;
}
/* Fix Collapsed table headers */
table.mw-made-collapsible:not(.mw-collapsed)>thead>tr {
	display: table-row;
}

/* Table Highlighting */
/* Highlighting properties for targetted rows */
@toexcludetr: ~".article-row-main:target ~ .article-row-main ~ .article-row-bound, .article-row-before:target ~ .article-row-main ~ .article-row-main, .article-row-before:target ~ .article-row-main ~ .article-row-main ~ .article-row-bound";
@toexcludetd: ~".article-row-main:target ~ .article-row-main ~ .article-row-bound td, .article-row-before:target ~ .article-row-main ~ .article-row-main td, .article-row-before:target ~ .article-row-main ~ .article-row-main ~ .article-row-bound td";
@toexcludeth: ~".article-row-main:target ~ .article-row-main ~ .article-row-bound th, .article-row-before:target ~ .article-row-main ~ .article-row-main th, .article-row-before:target ~ .article-row-main ~ .article-row-main ~ .article-row-bound th";
#tablerowhighlightingstyl() {
	/*
	.row {
		background-color: rgba(119,0,0,0.2);
	}
	*/
	.cell {
		/*border-color: rgba(204,0,0,0.5);*/
		border-color: rgb(255, 100, 100);
		border-style: solid;
		border-width: unset;
	}
}
.page-content .wikitable,
.page-content .article-table {
	@temp: ~".article-row-before, @{toexcludetr}";
	/*
	tr:target:not(@{temp}) {
		#tablerowhighlightingstyl.row();
	}
	*/
	@temp2: ~".article-row-before td, @{toexcludetd}";
	@temp3: ~".article-row-before th, @{toexcludeth}";
	tr:target td:not(@{temp2}),
	tr:target th:not(@{temp3}) {
		#tablerowhighlightingstyl.cell();
	}
}
.page-content tr.article-row-main:target ~ tr.article-row-bound,
.page-content tr.article-row-before:target ~ tr.article-row-main,
.page-content tr.article-row-before:target ~ tr.article-row-bound {
	/*
	&:not(@{toexcludetr}) {
		#tablerowhighlightingstyl.row();
	}
	*/
	@temp: ~"@{toexcludetd}";
	@temp2: ~"@{toexcludeth}";
	td:not(@{temp}),
	th:not(@{temp2}) {
		#tablerowhighlightingstyl.cell();
	}
}

/* Images styling */
img.thumbimage {
	margin: 2px 0;
}
img.banner {
	border-radius: 6px;
	max-width: 100%;
	max-height: 600px;
	width: auto;
	height: auto;
}
/* Pixelate all images */
/*
.page-content img,
.media img {
	image-rendering: pixelated;
}
*/

/* https://en.wikipedia.org/wiki/Template:Plainlist */
.plainlist ul,
.pi-europa .pi-data-value .plainlist ul {
	line-height: inherit;
	list-style: none none;
	margin: 0;
}
.plainlist ul li,
.pi-europa .pi-data-value .plainlist ul li {
	margin: 0;
	padding: 0;
}

/* Abuse Filter styling */
table.mw-abuselog-details {
	margin: 1em 1em 1em 0 !important;
	.theme-fandomdesktop-dark & {
		background-color: #2f1616 !important;
	}
}
table.mw-abuselog-details th {
	.theme-fandomdesktop-dark & {
		background-color: #2e174b !important;
	}
}

/* DIFF styling */
.diff-context {
	border-color: #4d5065 !important;
}
.diff-deletedline .diffchange.diffchange-inline {
	background-color: #a44d4d !important;
}
td.diff-deletedline {
	.theme-fandomdesktop-dark & {
		background-color: #4d2626 !important;
	}
}
.diff-deletedline {
	border-color: #b02d2d !important;
}
.diffchange {
	.theme-fandomdesktop-dark & {
		background-color: #0f72a7 !important;
	}
}
.diff-addedline {
	border-color: #2a77bd !important;
	.theme-fandomdesktop-dark & {
		background-color: #24263a !important;
	}
}

/* Quickdiff modal styling */
#quickdiff-modal {
	background-color: var(--theme-page-background-color);
	color: inherit;
}
#quickdiff-modal {
	background-color: var(--theme-page-background-color);
	color: var(--qdmodal-text-color);
}
#quickdiff-modal table.diff tr:not(.diff-title) td:not(.diff-marker):not(.diff-lineno) {
	font-family: monospace;
}

/* Block list CSS */
.TablePager_col_ipb_params>ul>li:not(:last-child)::after {
	content: ",";
}
.TablePager_col_ipb_params>ul {
	list-style: none !important;
	margin: 0 !important;
}
.TablePager_col_ipb_reason {
	font-style: italic;
}
.TablePager_col_ipb_reason::before {
	content: "("
}
.TablePager_col_ipb_reason::after {
	content: ")"
}

/* Tabbers */
/*
@theme-buttons: #c15926;
@theme-header: #cc9933;
#mw-content-text ul.tabbernav {
	border-color: @theme-header;

	li a {
		@mycurbg: @theme-buttons;
		background-color: @mycurbg;
		background-image: -webkit-gradient(linear, 0% 0%, 0% 100%, color-stop(35%, lighten(@mycurbg, 10%)), color-stop(65%, @mycurbg));
		border: 1px solid #c15926;
		border-radius: 4px 4px 0 0;
		color: #fff !important;
		font-weight: normal;

		&:hover {
			@mycurbg: darken(@theme-buttons, 5%);
			background-color: @mycurbg;
			background-image: -webkit-gradient(linear, 0% 0%, 0% 100%, color-stop(35%, lighten(@mycurbg, 10%)), color-stop(65%, @mycurbg));
			color: #dadada !important;
		}
	}

	li.tabberactive a {
		@mycurbg: lighten(@theme-buttons, 5%);
		font-weight: bold;
		background-color: #b05123;
		background-image: -webkit-gradient(linear, 0% 0%, 0% 100%, color-stop(35%, lighten(@mycurbg, 10%)), color-stop(65%, @mycurbg));
		color: #eee !important;
		border-color: @theme-header;
		border-width: 1px;
		padding-left: 10px;
		padding-right: 10px;

		&:hover {
			@mycurbg: darken(@theme-buttons, 10%);
			font-weight: bold;
			background-color: #b05123;
			background-image: -webkit-gradient(linear, 0% 0%, 0% 100%, color-stop(35%, lighten(@mycurbg, 10%)), color-stop(65%, @mycurbg));
			color: #dadada !important;
			border-color: darken(@theme-header, 5%);
		}
	}
}
.mw-content-text .tabber .tabbertab {
	border-color: @theme-header;
}
*/
/* Enables H2 and H3 headers Tabber */
/*
.tabberlive {
	position: relative;
	// Needed for {{TabberLinks}}
	overflow-x: auto;
	// Fixes the tabbers overflowing over infoboxes or any other floating stuff
	.tabbertab {
		h2,
		h3 {
			display: block !important;
		}
	}
}
*/
/* Infobox tweaks */
.portable-infobox .pi-item[data-item-name="infobox-stats-list"] .pi-data-label {
	flex-basis: 110px;
}
.portable-infobox .pi-item[data-item-name="infobox-stats-list"] .pi-data {
	padding-top: 6px;
	padding-bottom: 6px;
}
.pi-horizontal-group .pi-header {
	text-align: center;
}
.pi-image-collection-tabs {
	margin: 0.6em;
	list-style: none;
}
.portable-infobox .pi-caption {
	font-size: 12px;
}
.pi-data-label.pi-secondary-font {
	overflow: initial;
}
/* Makes the infobox top navigation wrap onto multiple lines, since badly designed scrolling behavior is crap on desktop */
.portable-infobox .pi-section-navigation {
	justify-content: center;
	flex-wrap: wrap;
}
/* Prevent infobox images being too tall */
.pi-image {
	border-bottom: 1px solid var(--pi-border-color);
}
.pi-image-thumbnail img,
img.pi-image-thumbnail {
	max-height: 350px;
	width: auto;
	max-width: 100%;
	height: auto;
	padding: 26px 1px;
}
.pi-item:not(.pi-title + .pi-item, .pi-header, section section section) {
	margin: 0 3px;
}
.portable-infobox .pi-item.wds-tabber {
	border: 0;
	border-radius: 0;
}
.tabber.wds-tabber > .wds-tab__content {
	padding: 1em;
}
.portable-infobox .wds-tabber {
	border-color: inherit;
}
.page-content .portable-infobox .pi-title {
	margin: 3px 3px 0;
	border-radius: 3px 3px 0 0;
}
.portable-infobox .pi-smart-group-head .pi-smart-data-label,
.portable-infobox .pi-smart-group-body .pi-smart-data-value {
	margin: 0;
}
.pi-smart-group-head+.pi-smart-group-body {
	border-top: none;
}
.pi-data-value ul li:before {
	color: white;
}
.pi-data-value {
	width: 100%;
}

/* TOC tweaks - styling used is partially from: runescape.wiki */
#toc, .toc {
	border: none;
	border-left: 1px solid #555;
	padding-left: 8px;
}
#toc ul ul, .toc ul ul {
	padding-left: 0.5em;
	border-left: 1px dotted var(--theme-border-color);
}
.mw-content-ltr .toc ul ul, .mw-content-rtl .mw-content-ltr .toc ul ul {
	margin: 0 0 0 2em;
}
#toc .toctogglelabel, .toc .toctogglelabel {
	color: var(--theme-page-text-color);
}
#toc .toctitle, .toc .toctitle {
	margin: 0 6px;
	border: none;
}
#toc > ul {
	margin-left: 6px;
	margin-right: 6px;
	padding-left: 6px;
	border-top: 1px solid var(--theme-border-color);
}
#toc > ul * {
	font-size: 13px;
	line-height: inherit;
}
.tocnumber {
	display: none;
}
.toc ul li {
	margin-left: 0;
}
/* tocright styling */
@media only screen and (min-width: 785px) {
	.tocright {
		float: right;
		max-width: 40%;
		overflow: auto;
	}
	.tocright .toc, .tocright #toc {
		margin: 0 0 .5em .5em;
	}
}

/* Hatnotes */
.mw-parser-output .hatnote {
	font-style: italic;
}

.mw-parser-output div.hatnote {
    padding-left: 1.6em;
    margin-bottom: 0.5em;
}

/* Less modal */
body #less-close {
	background-color: var(--theme-accent-color);
}
body #less-modal,
body #less-content {
	background-color: var(--theme-page-background-color);
}
body #less-title,
body #less-content p {
	color: var(--theme-page-text-color);
}
body #less-content > p > a {
	color: var(--theme-link-color);
}
body #less-content a:hover {
	color: var(--theme-link-color--hover);
	transition: color 0.3s;
	text-decoration: underline var(--theme-link-color--hover);
}

/* Style normal text like Latex text (<math> tag) */
.math-text {
	font-family: times, rubik, helvetica, sans-serif;
	font-size: 1.2em;
	margin: 0 0.3em;
	color: white;
}
/* <math> tag styling */
.mwe-math-element {
	/*display: block;*/
	overflow: auto;
}
.mwe-math-fallback-image-inline {
	background-color: unset;
	padding: 1px;
	margin: 0 5px;
}
/* Add invert for dark theme */
.theme-fandomdesktop-dark .mwe-math-fallback-image-inline {
	-webkit-filter: invert(1);
	filter: invert(1);
}

/* Code block */
.page:not(.page-is-edit) code:not(.CodeMirror-line),
.page:not(.page-is-edit) pre:not(.CodeMirror-line),
#less-content>p {
	font-family: Consolas, monospace !important;
}

/* API sandbox fixes */
.mw-apisandbox-toolbar {
	background: none;
}

/* Error Styling */
.scribunto-error {
	font-size: 14px;
	font-weight: normal;
	color: #F55;
	font-family: Candara, Segoe UI, Rubik, Helvetica, Arial, sans-serif;
	display: inline-block;
	border: 1px solid currentColor;
	border-radius: 8px;
	padding: 0 10px;
}
.scribunto-error::before {
	content: "";
	background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' version='1.1' x='0px' y='0px' viewBox='0 0 100 100' enable-background='new 0 0 100 100' xml:space='preserve' fill='%23F55'%3E%3Cpath d='M50 5C25.1 5 5 25.1 5 50c0 24.9 20.1 45 45 45c24.9 0 45-20.1 45-45C95 25.1 74.9 5 50 5L50 5z M55.6 77 c0 3.2-2.5 5.6-5.6 5.6c-3.1 0-5.5-2.5-5.5-5.6v-1.1c0-3.1 2.5-5.6 5.5-5.6c3.1 0 5.6 2.5 5.6 5.6V77z M58.3 26.3l-2.8 34.2 c-0.3 3.2-3 5.4-6.1 5.2c-2.8-0.2-4.9-2.5-5.1-5.2l-2.8-34.2c-0.5-4.5 3.7-8.9 8.2-8.9C54.7 17.4 58.7 21.8 58.3 26.3z'/%3E%3C/svg%3E");
	width: 18px;
	height: 18px;
	display: inline-block;
	margin-right: 7px;
	top: 4px;
	position: relative;
}
.mw-body-content .error {
	font-size: inherit;
}

/* Smooth Scrolling */
html {
	scroll-behavior: smooth;
}

/* <syntaxhighlight> styling */
.mw-highlight.mw-content-ltr .lineno {
	margin-right: 1rem;
}
.mw-highlight.mw-content-ltr, .dark-code-box {
	background-color: #272727 !important;
	border-radius: 6px;
	border: 0;
	.theme-fandomdesktop-light & {
		background-color: #cbcbcb !important;
	}
}

/* Special:RecentChanges fixes */
.mw-rcfilters-ui-cell {
	color: white;
}
.mw-recentchanges-toplinks {
	border: 0 !important;
}

/* MediaWiki:Common.js/search.js */
.hsb-custom-search {
  display: flex;
  max-width: 500px;
}
.hsb-custom-search input[type="search"] {
  flex: 1;
  padding: 8px 8px;
}
.hsb-custom-search button:not(#articleComments) {
  display: none; /* hiding it as it currently serves no purpose */
  font-size: 2em;
  padding: 0 0.3em;
  text-align: center;
  height: auto;
}

/* User Profile styling */
/* #userProfileApp .user-identity-bio {
	margin-right: 10em;
} */
#userProfileApp .user-identity-header__tag {
	text-transform: uppercase;
	font-weight: normal;
	.theme-fandomdesktop-light & {
		background-color: #ddd;
	}
	.theme-fandomdesktop-dark & {
		background-color: #301212;
	}
}

/* Fixing ugly AF error box */
body .errorbox {
	background: none;
	border: none;
	color: inherit;
}

/* Styling for API output */
body.page-Special_ApiHelp {
	margin: 2em 8em;
	background-color: #353535;
	color: white;
	transition: margin .2s;
	h1, h2, h3, h4, h5, h6 {
		color: white;
	}
	a {
		color: #fec356;
	}
	.api-pretty-header {
		font-size: 14px;
		font-family: rubik,helvetica,arial,sans-serif;
	}
	.mw-highlight {
		background-color: #272727 !important;
		border-radius: 6px;
		border: 0;
	}
}
@media only screen and (max-width: 785px) {
    body.page-Special_ApiHelp {
         margin: 2em;
    }
}

/* Options list (e.g. on Special:Upload) fixes */
option[disabled] {
	background-color: #2b2a33;
}

/* Editor styling when no permission */
.permissions-errors ~ #wpTextbox1,
.permissions-errors ~ .wikiEditor-ui #wpTextbox1 {
	background-color: transparent;
	color: inherit;
	font: 14px Consolas,Eupheima UCAS,Ayuthaya,Menlo,monospace;
	width: 100%;
}

/* Hide the "Start here" cards on Special:Community */
.community-page-cards-module {
	display: none;
}

/* Other Stylings */
:focus {
	outline: unset;
}
.page-content {
	font-size: 14px;
}
#re-mirror-sandbox:hover {
	text-decoration: underline;
}
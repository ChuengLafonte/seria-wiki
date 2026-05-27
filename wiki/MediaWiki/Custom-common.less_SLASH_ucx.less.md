/* Contains UCX (FandomDesktop skin) Fixes */

/* Editor Toolbar */
.wikiEditor-toolbar-dialog.ui-dialog .ui-dialog-buttonset .ui-button {
	background: var(--theme-accent-color);
	margin: 0 2px;
}
#wikieditor-toolbar-replace-search,
#wikieditor-toolbar-replace-replace {
	font-family: monospace;
}

/* Fix elements making excessive space below */
.page-content p:last-child {
	margin-bottom: 0;
}
.page-content ul:last-child,
.page-content ol:last-child {
	margin-bottom: 6px;
}

/* Fix fieldsets/legends */
fieldset:not(.oo-ui-fieldsetLayout) {
	border: 1px solid var(--theme-border-color);
	margin: 1em 0;
	padding: 0 1em 1em;
}
legend {
	padding: .5em;
}

/* Add divider after page header */
.page-header::after {
	background-color: var(--theme-border-color);
	border-color: var(--theme-border-color);
	border-style: solid;
	border-width: 1px;
	border: 0;
	content: "";
	display: block;
	height: 1px;
	margin-bottom: 0;
	margin-inline-end: auto;
	margin-inline-start: auto;
	margin-top: 5px;
	overflow: hidden;
	unicode-bidi: isolate;
	width: 100%;
}

/* Add title for Special:Contributions, Special:UserProfileActivity, User Blog:, Message Wall:, and User: namespace */
body.ns-2.action-view #firstHeading::before,
body.ns-500.action-view #firstHeading::before,
body.ns-1200.action-view #firstHeading::before,
body.mw-special-UserProfileActivity #firstHeading::before {
	font-size: 36px;
	font-weight: 300;
	letter-spacing: .25px;
	line-height: 1.25;
	overflow-wrap: break-word;
	word-break: break-word;
}
/*
body.ns-500.action-view #firstHeading::before {
	content: "User Blog";
}
body.ns-1200.action-view #firstHeading::before {
	content: "User Message Wall";
}
body.mw-special-UserProfileActivity #firstHeading::before {
	content: "User Social Activity";
}
*/
body.mw-special-UserProfileActivity .page-header__page-subtitle {
	display: block !important;
}

/* Change accent of "Edit" button to be more visible */
.page-header__actions>.wds-button,
.page-header__actions>.wds-dropdown {
	color: var(--theme-accent-label-color);
	background-color: var(--theme-accent-color);
	margin-right: 10px;
	transition: all .2s ease-in;
}
.page-header__actions>.wds-button:hover,
.page-header__actions>.wds-dropdown:hover {
	background-color: var(--theme-accent-color--hover);
	transition: all .2s ease-out;
	color: var(--theme-accent-label-color);
}
.page-header__actions>.wds-dropdown {
	border-radius: 30px;
}
.page-header__actions>.wds-button {
	left: -5px;
}
.page-header__actions>.wds-dropdown>div::before {
	left: -10px;
	margin-right: 10px;
}
.mw-history-subtitle {
	display: inline-block;
}
.page-header__actions .wds-dropdown>.page-header__action-button {
	color: var(--theme-accent-label-color);
	cursor: pointer;
}

/* Also fix article comments button */
#article-comments-button {
	background-color: var(--theme-accent-label-color);
	color: var(--theme-link-label-color);
}

/* Page Action buttons fix */
a.page-header__action-button:first-of-type+a#ca-edit::before {
	left: -8px;
}
a.page-header__action-button:first-of-type+a#ca-edit {
	margin-left: 6px;
}

/* Fix ugly history selection colors */
#pagehistory li {
	border: 0 !important;
}
#pagehistory>li.selected {
	background-color: var(--theme-page-background-color--secondary);
	border: 1px dashed var(--theme-border-color) !important;
	color: inherit !important;
	padding: 1px 0px
}

/* Fix page subtitle going on new lines */
.page-header__subtitle>div.mw-history-subtitle {
	display: inline !important;
}

/* Disable category dropdown */
.wds-collapsible-panel.page-footer__categories>header {
	display: none !important
}
.wds-collapsible-panel.page-footer__categories {
	margin-top: 10px;
	padding: 5px;
	border: 1px solid var(--wds-collapsible-panel-border-color);
	font-size: 14px;
	padding-top: 8px;
}

/* Categories fix */
.page-header__categories {
	font-style: italic;
}
.page-footer__categories>div {
	display: inherit !important;
}
body:not(.ns-828) .wds-collapsible-panel.page-footer__categories {
	padding-bottom: 0;
	margin-bottom: 10px;
}
body:not(.ns-828) .wds-collapsible-panel.page-footer__categories {
	padding-bottom: 0;
	margin-bottom: 10px;
}
.special-categories {
	display: inherit !important;
}
body:not(.ns-828) .wds-collapsible-panel.page-footer__categories .container {
	padding: 0;
}

/* Fix notification position and colors */
#mw-notification-area {
	position: fixed;
}
#mw-notification-area .mw-notification {
	border-radius: 6px;
}

/* Fix colors of seperators */
.mw-changeslist-links>span:not(:first-child):before {
	color: inherit !important;
}

/* Fix positioning and arrow of "My Tools" */
#WikiaBarWrapper .mytools.menu:not(:hover)>svg {
	transform: rotate(180deg);
	transition: .25s all ease;
}
#WikiaBarWrapper .mytools.menu:hover>svg {
	transition: .25s all ease;
}

/* Wiki toolbar styling */
#my-tools-menu {
	min-width: fit-content;
	overflow-x: hidden;
	padding-right: 10px;
	max-height: 80%;
}

/* FandomDesktop tabber */
/* Custom tabber styling */
.wds-tabber, .partialLoad-tabber {
	background-color: var(--theme-page-background-color);
	/*border: 1px solid rgba(254, 195, 86, 0.75);*/
	border: ~"1px solid rgba(var(--theme-link-color--rgb),0.75)";
	border-radius: 3px;
}
.wds-tabs__tab,
.partialLoad-tabs__tab {
	border: 1px solid transparent;
	text-decoration: none;
}
.wds-tabs__tab {
	&:hover .wds-tabs__tab-label:not(.wds-tabs__tab.wds-is-current .wds-tabs__tab-label),
	&:hover a:not(.wds-tabs__tab.wds-is-current a) {
		color: var(--wds-tab-color--hover);
		box-shadow: inset 0 -3px 0 -1px var(--theme-link-color);
	}
}
.partialLoad-tabs__tab {
	&:hover .partialLoad-tabs__label:not(.partialLoad-tabs__tab.select .partialLoad-tabs__label),
	&:hover a:not(.partialLoad-tabs__tab.select a) {
		color: var(--wds-tab-color--hover);
		box-shadow: inset 0 -3px 0 -1px var(--theme-link-color);
	}
}
.wds-tabs__tab .wds-tabs__tab-label,
.partialLoad-tabs__tab .partialLoad-tabs__label {
	box-shadow: inset 0 -3px 0 -1px transparent;
	transition: all 0.2s;
	a {
		transition: all 0.2s;
	}
	a:focus {
		color: inherit;
	}
}
.wds-tabs__tab .wds-tabs__tab-label {
	& a:hover, & a:active, & a:focus-visible,
	&:hover, &:active, &:focus-visible {
		&:not(.wds-tabs__tab.wds-is-current .wds-tabs__tab-label, .wds-tabs__tab.wds-is-current a) {
			color: var(--wds-tab-color--hover);
			box-shadow: inset 0 -3px 0 -1px var(--theme-link-color);
		}
	}
}
.partialLoad-tabs__tab .partialLoad-tabs__label {
	& a:hover, & a:active, & a:focus-visible,
	&:hover, &:active, &:focus-visible {
		&:not(.partialLoad-tabs__tab.selected .partialLoad-tabs__label, .partialLoad-tabs__tab.selected a) {
			color: var(--wds-tab-color--hover);
			box-shadow: inset 0 -3px 0 -1px var(--theme-link-color);
		}
	}
}
.wds-tabs__tab.wds-is-current,
.partialLoad-tabs__tab.selected {
	/*border: 1px solid rgba(254, 195, 86, 0.4);*/
	border: ~"1px solid rgba(var(--theme-link-color--rgb),0.4)";
	border-top: none;
	/*background: rgba(254, 195, 86, 0.1);*/
	background-color: ~"rgba(var(--theme-link-color--rgb),0.1)";
}
/* Tabber fixes */
body .page-content ul.wds-tabs,
body .page-content ul.partialLoad-tabs {
	margin: 0;
}

/* Editing interface fixes */

/* Shrinks excessive space before ul/ol */
.page-content p:not(.mw-empty-elt) + ul,
.page-content dl + ul,
.page-content p:not(.mw-empty-elt) + ol,
.page-content dl + ol,
.page-content dt + p {
	margin-top: -18px;
}

/* Fix word colors */
.mcf-header {
	color: var(--theme-body-text-color);
}

/* Allows marginless paragraphs */
.article-margin-off p,
.article-margin-off ul,
.article-margin-off ol,
.article-margin-off dl {
	margin-top: 0 !important;
	margin-bottom: 0 !important;
}

/* Fix for new user pop-up buttons */
button.sc-fHCHyC,
button[data-testid='SimpleSurveyContent'] {
	box-sizing: content-box;
	height: 34px !important;
	display: flex !important;
}
button.sc-cbeScs,
button[data-testid='SimpleSurveyContent'] {
	box-sizing: content-box;
}
#SurveyModule.dvlmvB {
	height: inherit;
}

/* Keyboard shortcuts menu */
.global-shortcuts-help__list-item {
	margin-bottom: 0;
}
.global-shortcuts-help__disclaimer,
.global-shortcuts-help__explore-shortcuts {
	padding-top: 1em;
}

/* Header fixes */
.fandom-sticky-header {
	top: -47px;
}
.page-header__title {
	word-break: keep-all;
}
.page-header__bottom {
	flex-wrap: wrap;
	justify-content: flex-end;
}

/* Content Review (JSRT) */
.content-review__widget__header {
	margin-top: 0;
}
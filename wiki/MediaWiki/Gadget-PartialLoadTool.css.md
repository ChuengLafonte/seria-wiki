.page-content .partialLoad-tabber {
	--wds-tab-color: rgba(var(--theme-page-text-color--rgb),0.75);
	--wds-tab-color--active: var(--theme-link-color);
	--wds-tab-color--hover: var(--theme-page-text-color);
	--wds-tab-border-color: rgba(var(--theme-page-dynamic-color-1--rgb),0.25);
}
.page-content .partialLoad-tabs__wrapper {
	border-bottom: 1px solid var(--wds-tab-border-color);
	position: relative;
}
.page-content ul.partialLoad-tabs {
	-webkit-box-align: end;
	align-items: flex-end;
	display: -webkit-box;
	display: flex;
	list-style: none;
	margin: 0;
	padding: 0;
	position: relative;
}
.page-content .partialLoad-tabs__tab {
	border: 1px solid transparent;
	text-decoration: none;
	color: var(--wds-tab-color);
	cursor: default;
	flex-shrink: 0;
	line-height: 14px;
	-webkit-transition: -webkit-box-shadow .1s;
	transition: -webkit-box-shadow .1s;
	transition: box-shadow .1s;
	transition: box-shadow .1s,-webkit-box-shadow .1s;
}
.page-content .partialLoad-tabs__tab.selected {
	 -webkit-box-shadow: inset 0 -3px 0 -1px currentColor; 
	box-shadow: inset 0 -3px 0 -1px currentColor;
	color: var(--wds-tab-color--active);
}
.page-content .partialLoad-tabs__label {
	-webkit-box-align: center;
	align-items: center;
	display: -webkit-inline-box;
	display: inline-flex;
	font-size: 14px;
	font-weight: 500;
	height: 40px;
	letter-spacing: .5px;
	margin: 0 11px;
	text-align: center;
	text-decoration: none;
	-webkit-transition: color .1s;
	transition: color .1s;
	white-space: nowrap;
	transition: color .1s;
}
.page-content .partialLoad-tabs__tab a {
	-webkit-box-align: center;
	align-items: center;
	color: inherit;
	display: -webkit-inline-box;
	display: inline-flex;
	height: 100%;
	text-decoration: none;
}
.page-content .partialLoad-frame {
	padding: 0 1em;
	display: block;
}
.page-content .partialLoad-actionLinks__wrapper.noselect {
	width: 100%;
	display: flex;
	justify-content: end;
	border-bottom: 1px solid var(--wds-tab-border-color);
}
.page-content .partialLoad-actionLinks {
	margin: .5em;
	font-size: small;
}
.page-content .partialLoad-separator {
	clear: both;
}
.page-content .partialLoad-spinner {
	justify-content: center;
	display: flex;
	margin: 3em 0;
}
.page-content .partialLoad-loadContent {
	text-align: center;
	display: block;
}
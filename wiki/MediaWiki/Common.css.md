/* <pre> */
/**
 * CSS placed here will be applied to all skins on the entire site.
 *
 * This page is compiled from LESS files listed in [[MediaWiki:Custom-common.less]] and should not be edited directly.
 */

/**
 * The is the root LESS file for [[MediaWiki:Common.css]].
 *
 * Notice for English Hypixel SkyBlock wiki:
 * If you added/removed page imports from here, remember to change [[MediaWiki:Custom-Less.json]]
 *
 * Notice for international wikis of Hypixel SkyBlock Wiki:
 * You are recommended to keep this file up to date with [[:en:MediaWiki:Custom-common.less]]
 *     and change @lang to "/<your wiki's lang code>" (e.g. "/en")
 *     (You may do this step by clicking the "Update Less Source" button)
 * You are recommended to use [[MediaWiki:Custom-common.less/language-local.less]] to override existing rules and add rules locally.
 * Imports prefixed @{local} should exist on your wiki.
 * Imports prefixed @{upstream} already exist on the English wiki.
 * If you *really* want to import another page locally,
 *     remember to add your page to [[MediaWiki:Custom-Less.json]] (see the English page for the format required)
 *
 * To update [[MediaWiki:Common.css]] from this file:
 * - For Oasis users: Click the "Update CSS" button at the top of the page
 * - For Monobook users: Click the "Update CSS" link in your toolbox
 *
 * For more information, see <http://dev.wikia.com/wiki/Less>
 * --------------------------------------------------------------------------------------------------------------------
 * LESS standard library:	<http://lesscss.org/functions/>
 * Non-standard mixins:		<http://dev.wikia.com/wiki/Less/mixins>
 *
 * Available themedesigner values:
 * - @theme-body	-> body background colour
 * - @theme-buttons	-> button colour
 * - @theme-header	-> collapsible footer bar colour
 * - @theme-links	-> link colour
 * - @theme-page	-> article content background
 */
/* Normal CSS import */
@import "https://dev.fandom.com/wiki/MediaWiki:Highlight.css?action=raw&ctype=text/css";
@import "https://dev.fandom.com/wiki/MediaWiki:InterlanguageFlags.css?action=raw&ctype=text/css";
/* directory, used in imports */
/* note: this variable is automatically updated when using Less Source Updater */
/* Custom Fonts */
/* Core Fonting */
/* All Minecraft */
@import 'https://cdn.jsdelivr.net/gh/skyblock-wiki/wiki-assets@1.0/fonts/font-import/lib/wiki-use.css';
/* Article Font */
@import 'https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,700;1,700&display=swap';
@import 'https://fonts.googleapis.com/css2?family=Noto+Sans:ital,wght@0,400;0,600;0,700;1,400;1,600;1,700&display=swap';
@import 'https://fonts.googleapis.com/css2?family=Noto+Sans+Symbols+2&display=swap';
#firstHeading,
.mw-headline,
#filehistory,
#filelinks,
.unified-search__community__content__name,
.unified-search__result__title,
.wds-collapsible-panel__header,
h2.blog-listing__title {
  font-family: var(--fontface-title);
  font-weight: 700;
}
.page,
.page .ve-fd-header,
.community-header-wrapper,
.fandom-sticky-header {
  font-family: var(--fontface-content);
}
/* Variables */
/* Custom CSS variables for this wiki */
/* Theme Style Overrides - Use according to what you need for a certain theme */
.theme-fandomdesktop-dark {
  --theme-link-label-color: #fff;
  --theme-link-decoration: none;
  /* may delete if Fandom fixed it */
}
/* Font */
body {
  --fontface-title: rubik, helvetica, sans-serif;
  --fontface-content: rubik, helvetica, sans-serif;
}
/* Adaptive color palette */
.theme-fandomdesktop-dark {
  --custom-adaptive-extralight: #222349;
  --custom-adaptive-lighter: #424c75;
  --custom-adaptive-light: #384575;
  --custom-adaptive-semidark: #191a2e;
  --custom-adaptive-dark: #121825;
  --custom-adaptive-darker: #1d1b22;
  --custom-adaptive-extradark: #0a090e;
  --custom-adaptive-diffuse: linear-gradient(0.2turn, #1d1b22, #1b2525);
}
.theme-fandomdesktop-light {
  --custom-adaptive-extralight: #adc8d6;
  --custom-adaptive-lighter: #8dbdde;
  --custom-adaptive-light: #6798bb;
  --custom-adaptive-semidark: #4c89b5;
  --custom-adaptive-diffuse: linear-gradient(0.2turn, #ccc, #c7d7d7);
}
/* Other Theme-dependent Styling */
.theme-fandomdesktop-light .discord-widget .widget-logo,
.theme-fandomdesktop-dark .discord-widget .widget-logo {
  filter: invert();
}
.theme-fandomdesktop-dark .color1 a:not(.image) {
  filter: brightness(30%);
}
/* Standard Palette */
/* This section is attributed to: Minecraft Wiki (minecraft.fandom.com) */
.theme-fandomdesktop-dark {
  --custom-background-blue: hsl(215, 25%, 8%);
  --custom-background-blue-highlight: hsl(215, 25%, 12%);
  --custom-background-green: hsl(120, 25%, 8%);
  --custom-background-green-highlight: hsl(120, 25%, 12%);
  --custom-background-grey: hsl(0, 0%, 8%);
  --custom-background-grey-highlight: hsl(0, 0%, 12%);
  --custom-background-magenta: hsl(310, 25%, 8%);
  --custom-background-magenta-highlight: hsl(310, 25%, 12%);
  --custom-background-orange: hsl(40, 25%, 8%);
  --custom-background-orange-highlight: hsl(40, 25%, 12%);
  --custom-background-purple: hsl(260, 25%, 8%);
  --custom-background-purple-highlight: hsl(260, 25%, 12%);
  --custom-background-red: hsl(0, 25%, 8%);
  --custom-background-red-highlight: hsl(0, 25%, 12%);
  --custom-background-yellow: hsl(60, 25%, 8%);
  --custom-background-yellow-highlight: hsl(60, 25%, 12%);
  --custom-border-blue: hsl(215, 15%, 36%);
  --custom-border-blue-highlight: hsl(215, 50%, 30%);
  --custom-border-green: hsl(120, 15%, 36%);
  --custom-border-green-highlight: hsl(120, 50%, 30%);
  --custom-border-grey: hsl(0, 0%, 36%);
  --custom-border-magenta: hsl(310, 15%, 36%);
  --custom-border-magenta-highlight: hsl(310, 50%, 30%);
  --custom-border-orange: hsl(40, 15%, 36%);
  --custom-border-orange-highlight: hsl(40, 50%, 30%);
  --custom-border-purple: hsl(260, 15%, 36%);
  --custom-border-purple-highlight: hsl(260, 50%, 30%);
  --custom-border-red: hsl(0, 15%, 36%);
  --custom-border-red-highlight: hsl(0, 50%, 30%);
  --custom-border-yellow: hsl(60, 15%, 36%);
  --custom-border-yellow-highlight: hsl(60, 50%, 30%);
}
.theme-fandomdesktop-light {
  --custom-background-blue: hsl(215, 75%, 92%);
  --custom-background-blue-highlight: hsl(215, 75%, 85%);
  --custom-background-green: hsl(120, 75%, 92%);
  --custom-background-green-highlight: hsl(120, 75%, 85%);
  --custom-background-grey: hsl(0, 0%, 92%);
  --custom-background-grey-highlight: hsl(0, 0%, 85%);
  --custom-background-magenta: hsl(310, 75%, 92%);
  --custom-background-magenta-highlight: hsl(310, 75%, 85%);
  --custom-background-orange: hsl(40, 75%, 92%);
  --custom-background-orange-highlight: hsl(40, 75%, 85%);
  --custom-background-purple: hsl(260, 75%, 92%);
  --custom-background-purple-highlight: hsl(260, 75%, 85%);
  --custom-background-red: hsl(0, 75%, 92%);
  --custom-background-red-highlight: hsl(0, 75%, 85%);
  --custom-background-yellow: hsl(60, 75%, 92%);
  --custom-background-yellow-highlight: hsl(60, 75%, 85%);
  --custom-border-blue: hsl(215, 25%, 65%);
  --custom-border-blue-highlight: hsl(215, 50%, 68%);
  --custom-border-green: hsl(120, 25%, 65%);
  --custom-border-green-highlight: hsl(120, 50%, 68%);
  --custom-border-grey: hsl(0, 0%, 65%);
  --custom-border-magenta: hsl(310, 25%, 65%);
  --custom-border-magenta-highlight: hsl(310, 50%, 68%);
  --custom-border-orange: hsl(40, 25%, 65%);
  --custom-border-orange-highlight: hsl(40, 50%, 68%);
  --custom-border-purple: hsl(260, 25%, 65%);
  --custom-border-purple-highlight: hsl(260, 50%, 68%);
  --custom-border-red: hsl(0, 25%, 65%);
  --custom-border-red-highlight: hsl(0, 50%, 68%);
  --custom-border-yellow: hsl(60, 25%, 65%);
  --custom-border-yellow-highlight: hsl(60, 50%, 68%);
}
/* Role Styling */
/* For wiki's role styling */
/* Role Colors, URLs */
body {
  /* URLs */
  --custom-rolebadge-bot: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/0/08/Badge-Bot.png/revision/latest");
  --custom-rolebadge-bureaucrat: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/2/27/Badge-Bureaucrat.png/revision/latest");
  --custom-rolebadge-sysop: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/e/e1/Badge-Administrator.png/revision/latest");
  --custom-rolebadge-codeeditor: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/b/b9/Badge-CodeEditor.png/revision/latest");
  --custom-rolebadge-content-moderator: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/0/03/Badge-ContentModerator.png/revision/latest");
  --custom-rolebadge-threadmoderator: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/a/aa/Badge-DiscussionsModerator.png/revision/latest");
  --custom-rolebadge-rollback: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/6/68/Badge-Rollback.png/revision/latest");
  --custom-rolebadge-ard: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/8/8d/Badge-Ard.png/revision/latest");
  --custom-rolebadge-dev: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/7/70/Badge-Dev.png/revision/latest");
  /* Colors */
  --custom-rolecolor-bot: #a9a9a9;
  --custom-rolecolor-bureaucrat: #eb3b40;
  --custom-rolecolor-sysop: #992ceb;
  --custom-rolecolor-codeeditor: #536feb;
  --custom-rolecolor-content-moderator: #31AF84;
  --custom-rolecolor-threadmoderator: #1f9921;
  --custom-rolecolor-rollback: #eb8b23;
  --custom-rolecolor-ard: #ec3b83;
  --custom-rolecolor-dev: #ec593b;
  --custom-rolecolor-abusefilter: #494fa6;
  --custom-rolecolor-wiki-representative: #c0b706;
}
/* Role Styling for Usernames */
/* Bureaucrats */
.user-link-bcrat {
  color: var(--custom-rolecolor-bureaucrat) !important;
}
/* Admins */
.user-link-admin {
  color: var(--custom-rolecolor-sysop) !important;
}
/* Code Editors */
.user-link-codeeditor {
  color: var(--custom-rolecolor-codeeditor) !important;
}
/* Content moderators */
.user-link-mod {
  color: var(--custom-rolecolor-content-moderator) !important;
}
/* Discussion moderators */
.user-link-dmod {
  color: var(--custom-rolecolor-threadmoderator) !important;
}
/* Rollbackers */
.user-link-rollback {
  color: var(--custom-rolecolor-rollback) !important;
}
/* Bots */
.user-link-bot {
  color: var(--custom-rolecolor-bot) !important;
}
/* Username Styling (Specialists) */
/* ARD Specialists */
.user-link-ard {
  color: var(--custom-rolecolor-ard) !important;
}
/* Dev Specialists */
.user-link-dev {
  color: var(--custom-rolecolor-dev) !important;
}
/* Template Styling */
/****************************
 * Navbox
 ****************************/
.navbox {
  /* IGNORE EDITOR CALLING THESE ERRORS! It's valid css, just save anyways */
  --navbox-border: #030101;
  --navbox-outer-border: #151515;
  --navbox-title-background: var(--custom-adaptive-extradark);
  --navbox-title-link-color: #ffffff;
  --navbox-title-color: #dddddd;
  --navbox-header-background: var(--custom-adaptive-darker);
  --navbox-header-link-color: #dddddd;
  --navbox-header-color: #ffffff;
  --navbox-list-background: var(--theme-page-background-color--secondary);
  --navbox-list-link-color: var(--theme-link-color);
  width: 100%;
  background: var(--navbox-border);
  color: white;
  margin: 1em auto;
  font-size: 84%;
  clear: both;
  padding: 2px;
  border-spacing: 0;
  border: 2px solid var(--navbox-outer-border);
  border-radius: 3px;
}
.theme-fandomdesktop-light .navbox {
  --navbox-border: #666;
  --navbox-outer-border: var(--theme-accent-color);
  --navbox-title-background: #555;
  /* using grayscale */
  --navbox-header-background: var(--theme-page-background-color--secondary);
  /* using grayscale */
  --navbox-header-link-color: #222;
  --navbox-header-color: #000;
  --navbox-list-background: white;
}
.navbox .navbox-header a,
.navbox .navbox-group a,
.navbox .mw-collapsible-toggle a:hover {
  color: var(--navbox-header-link-color);
}
.navbox .navbox-title a {
  color: var(--navbox-title-link-color);
  font-weight: bold;
}
.navbox + .navbox {
  margin-top: -16px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
.navbox .navbox-title {
  color: var(--navbox-title-color);
  background: var(--navbox-title-background);
  font-weight: bold;
}
.navbox .navbox-vde {
  float: left;
  width: 65px;
}
.navbox .navbox-title-padright {
  padding-right: 65px;
}
.navbox .navbox-title-padleft {
  padding-left: 65px;
}
.navbox .navbox-subgroup {
  border-spacing: 0;
  width: 100%;
}
.navbox .navbox-gutter {
  height: 2px;
}
.navbox .navbox-subgroup .navbox-gutter {
  background: var(--navbox-border);
}
.navbox .navbox-section-row > td {
  padding: 0;
  height: 100%;
}
.navbox .navbox-section {
  width: 100%;
  border-spacing: 0;
}
.navbox .navbox-above,
.navbox .navbox-below,
.navbox .navbox-image {
  color: var(--theme-page-text-color);
  background: var(--navbox-header-background);
  text-align: center;
}
.navbox .navbox-group,
.navbox .navbox-header {
  background: var(--navbox-header-background);
  color: var(--navbox-header-color);
  font-weight: bold;
  height: 100%;
  padding: 2px 4px;
}
.navbox .navbox-header-collapsible {
  padding-left: 65;
}
.navbox .navbox-group {
  min-width: 150px;
}
.navbox .navbox-group,
.navbox .navbox-image-left {
  border-right: 2px solid var(--navbox-border);
}
.navbox .navbox-image-right {
  border-left: 2px solid var(--navbox-border);
}
.navbox .navbox-list {
  background: var(--navbox-list-background);
  color: var(--theme-page-text-color);
  width: 100%;
  height: 100%;
  padding: 0;
}
.navbox .navbox-list div {
  padding: 0px 4px;
}
.navbox .navbox-list.no-group {
  text-align: center;
}
.navbox .navbox-list a {
  color: var(--navbox-list-link-color);
}
.navbox .navbox-list a.new {
  color: var(--theme-body-text-color) !important;
}
.navbox .mw-collapsible-toggle {
  width: 65px;
}
.hlist ul {
  margin: 0;
  list-style: none;
}
.hlist li,
.hlist ul ul {
  display: inline;
}
.hlist li a {
  white-space: nowrap;
}
.hlist ul ul:before {
  content: "(";
}
.hlist ul ul:after {
  content: ")";
}
.hlist li:after {
  content: "•";
  margin: 0 3px;
}
.hlist ul ul li:after {
  content: "/";
}
.hlist li:last-child:after,
.hlist ul ul li:last-child:after {
  content: none;
}
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
  background-color: rgba(255, 255, 255, 0.5);
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
  background: url(//static.wikia.nocookie.net/hypixel-skyblock/images/3/30/Question.png) no-repeat center / contain;
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
  letter-spacing: 0.2px;
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
.mcui-Chest > *,
.mcui-Crafting_Table > *,
.mcui-Furnace > *,
.mcui-Anvil > * {
  display: inline-block;
  vertical-align: top;
}
.mcui-Chest .mcui-row,
.mcui-Crafting_Table .mcui-row,
.mcui-Anvil .mcui-row {
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
  color: black;
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
#minetip-tooltip,
.minetip-static {
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
}
#minetip-tooltip::before,
.minetip-static::before {
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
#minetip-tooltip::after,
.minetip-static::after {
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
#minetip-tooltip * + .minetip-description,
.minetip-static * + .minetip-description {
  display: block;
  margin-top: 0.25em;
}
/* Element Animator - used in conjunction with JS to cycle through multiple items */
/* Taken from minecraft.gamepedia.com */
#mw-content-text .animated > *:not(.animated-active),
#mw-content-text .animated > .animated-subframe > *:not(.animated-active) {
  display: none;
}
#mw-content-text div.animated.animated-visible,
#mw-content-text span.animated.animated-visible,
#mw-content-text span.animated.animated-visible > *,
#mw-content-text span.animated.animated-visible > .animated-subframe > * {
  display: inline-block;
}
#mw-content-text div.animated.animated-visible > *,
#mw-content-text div.animated.animated-visible > .animated-subframe > * {
  display: block;
}
/* Animator tweaks for this wiki */
#mw-content-text .animated-wrapper {
  position: relative;
  display: inline-block;
  overflow-x: auto;
}
#mw-content-text .animated-wrapper .animated-fakeimage {
  visibility: hidden;
  position: relative;
}
#mw-content-text .animated-wrapper .animated {
  display: flex;
  justify-content: center;
  position: absolute;
  top: 0;
  height: 100%;
  width: 100%;
  align-items: center;
}
#mw-content-text .animated-wrapper .animated.animated-visible {
  display: inline-flex;
  justify-content: left;
  left: 0;
}
#mw-content-text .animated-wrapper .animated.animated-visible .pi-image-thumbnail {
  max-width: none;
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
  letter-spacing: 0.2px;
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
}
.theme-fandomdesktop-light .mcui-text {
  filter: brightness(75%);
  /* global dimming for light theme */
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
  /* Correct bottom padding */
}
.theme-fandomdesktop-light .mcdialogue {
  background-color: rgba(0, 0, 0, 0.58);
}
.mcdialogue + p {
  margin-top: 24px;
}
/* Game font */
.page-content .hsw-gamefont {
  display: inline;
  font-family: minecrafts, minecraft, unifontm, unifont, Rubik, serif, sans-serif;
}
.page-content .hsw-gamefont.cram {
  letter-spacing: -1px;
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
.format-0,
.ace_format-0 {
  color: #000 !important;
  text-shadow: 0.125em 0.125em #000000;
}
.format-0 .format-l,
.ace_format-0.ace_format_bold,
.format-l .format-0 {
  text-shadow: 0.75px 0, 1.5px 0, 1.5px 2px #000000, 2.35px 2px #000000, 3.2px 2px #000000;
}
.format-1,
.ace_format-1 {
  color: #00A !important;
  text-shadow: 0.125em 0.125em #00002A;
}
.format-1 .format-l,
.ace_format-1.ace_format_bold,
.format-l .format-1 {
  text-shadow: 0.75px 0, 1.5px 0, 1.5px 2px #00002A, 2.35px 2px #00002A, 3.2px 2px #00002A;
}
.format-2,
.ace_format-2 {
  color: #0A0 !important;
  text-shadow: 0.125em 0.125em #002A00;
}
.format-2 .format-l,
.ace_format-2.ace_format_bold,
.format-l .format-2 {
  text-shadow: 0.75px 0, 1.5px 0, 1.5px 2px #002A00, 2.35px 2px #002A00, 3.2px 2px #002A00;
}
.format-3,
.ace_format-3 {
  color: #0AA !important;
  text-shadow: 0.125em 0.125em #002A2A;
}
.format-3 .format-l,
.ace_format-3.ace_format_bold,
.format-l .format-3 {
  text-shadow: 0.75px 0, 1.5px 0, 1.5px 2px #002A2A, 2.35px 2px #002A2A, 3.2px 2px #002A2A;
}
.format-4,
.ace_format-4 {
  color: #A00 !important;
  text-shadow: 0.125em 0.125em #2A0000;
}
.format-4 .format-l,
.ace_format-4.ace_format_bold,
.format-l .format-4 {
  text-shadow: 0.75px 0, 1.5px 0, 1.5px 2px #2A0000, 2.35px 2px #2A0000, 3.2px 2px #2A0000;
}
.format-5,
.ace_format-5 {
  color: #A0A !important;
  text-shadow: 0.125em 0.125em #2A002A;
}
.format-5 .format-l,
.ace_format-5.ace_format_bold,
.format-l .format-5 {
  text-shadow: 0.75px 0, 1.5px 0, 1.5px 2px #2A002A, 2.35px 2px #2A002A, 3.2px 2px #2A002A;
}
.format-6,
.ace_format-6 {
  color: #FA0 !important;
  text-shadow: 0.125em 0.125em #2A2A00;
}
.format-6 .format-l,
.ace_format-6.ace_format_bold,
.format-l .format-6 {
  text-shadow: 0.75px 0, 1.5px 0, 1.5px 2px #2A2A00, 2.35px 2px #2A2A00, 3.2px 2px #2A2A00;
}
.format-7,
.ace_format-7 {
  color: #AAA !important;
  text-shadow: 0.125em 0.125em #2A2A2A;
}
.format-7 .format-l,
.ace_format-7.ace_format_bold,
.format-l .format-7 {
  text-shadow: 0.75px 0, 1.5px 0, 1.5px 2px #2A2A2A, 2.35px 2px #2A2A2A, 3.2px 2px #2A2A2A;
}
.format-8,
.ace_format-8 {
  color: #555 !important;
  text-shadow: 0.125em 0.125em #151515;
}
.format-8 .format-l,
.ace_format-8.ace_format_bold,
.format-l .format-8 {
  text-shadow: 0.75px 0, 1.5px 0, 1.5px 2px #151515, 2.35px 2px #151515, 3.2px 2px #151515;
}
.format-9,
.ace_format-9 {
  color: #55F !important;
  text-shadow: 0.125em 0.125em #15153F;
}
.format-9 .format-l,
.ace_format-9.ace_format_bold,
.format-l .format-9 {
  text-shadow: 0.75px 0, 1.5px 0, 1.5px 2px #15153F, 2.35px 2px #15153F, 3.2px 2px #15153F;
}
.format-a,
.ace_format-a {
  color: #5F5 !important;
  text-shadow: 0.125em 0.125em #153F15;
}
.format-a .format-l,
.ace_format-a.ace_format_bold,
.format-l .format-a {
  text-shadow: 0.75px 0, 1.5px 0, 1.5px 2px #153F15, 2.35px 2px #153F15, 3.2px 2px #153F15;
}
.format-b,
.ace_format-b {
  color: #5FF !important;
  text-shadow: 0.125em 0.125em #153F3F;
}
.format-b .format-l,
.ace_format-b.ace_format_bold,
.format-l .format-b {
  text-shadow: 0.75px 0, 1.5px 0, 1.5px 2px #153F3F, 2.35px 2px #153F3F, 3.2px 2px #153F3F;
}
.format-c,
.ace_format-c {
  color: #F55 !important;
  text-shadow: 0.125em 0.125em #3F1515;
}
.format-c .format-l,
.ace_format-c.ace_format_bold,
.format-l .format-c {
  text-shadow: 0.75px 0, 1.5px 0, 1.5px 2px #3F1515, 2.35px 2px #3F1515, 3.2px 2px #3F1515;
}
.format-d,
.ace_format-d {
  color: #F5F !important;
  text-shadow: 0.125em 0.125em #3F153F;
}
.format-d .format-l,
.ace_format-d.ace_format_bold,
.format-l .format-d {
  text-shadow: 0.75px 0, 1.5px 0, 1.5px 2px #3F153F, 2.35px 2px #3F153F, 3.2px 2px #3F153F;
}
.format-e,
.ace_format-e {
  color: #FF5 !important;
  text-shadow: 0.125em 0.125em #3F3F15;
}
.format-e .format-l,
.ace_format-e.ace_format_bold,
.format-l .format-e {
  text-shadow: 0.75px 0, 1.5px 0, 1.5px 2px #3F3F15, 2.35px 2px #3F3F15, 3.2px 2px #3F3F15;
}
.format-f,
.ace_format-f {
  color: #FFF !important;
  text-shadow: 0.125em 0.125em #3F3F3F;
}
.format-f .format-l,
.ace_format-f.ace_format_bold,
.format-l .format-f {
  text-shadow: 0.75px 0, 1.5px 0, 1.5px 2px #3F3F3F, 2.35px 2px #3F3F3F, 3.2px 2px #3F3F3F;
}
.format-l {
  letter-spacing: 1.5px;
}
.format-m,
.ace_format-m {
  text-decoration: line-through;
}
.format-n,
.ace_format-n {
  text-decoration: underline;
}
.format-m .format-n,
.ace_format-m.ace_format-n,
.format-n .format-m {
  text-decoration: line-through underline;
}
.format-o {
  font-style: italic;
}
/* Don't add things below! Add them above! */
/**
* Style sheet for buttons
*/
a.wikia-button,
.wikia-single-button a,
.wikia-menu-button,
.button:not(.carousel-arrow) {
  --w-button-color: #7A320F;
  --w-button-outline-color: #7A320F;
  --w-button-color-hover: #57240A;
  --w-button-outline-color-hover: #57240A;
  --w-button-text-color: #ffffff;
  display: inline-block;
  margin-bottom: 14px;
  padding: 12px;
  background-color: var(--w-button-color);
  border-radius: 4px;
  border: 2px solid var(--theme-page-background-color);
  outline: 1px solid var(--w-button-outline-color);
  color: var(--w-button-text-color);
  line-height: 14px;
  letter-spacing: 0.3px;
  white-space: nowrap;
  cursor: pointer;
  transition: all 0.2s linear;
}
.theme-fandomdesktop-light a.wikia-button,
.theme-fandomdesktop-light .wikia-single-button a,
.theme-fandomdesktop-light .wikia-menu-button,
.theme-fandomdesktop-light .button:not(.carousel-arrow) {
  --w-button-color: #BB3737;
  --w-button-color-hover: #962C2C;
}
a.wikia-button:hover,
.wikia-single-button a:hover,
.wikia-menu-button:hover,
.button:not(.carousel-arrow):hover,
a.wikia-button:active,
.wikia-single-button a:active,
.wikia-menu-button:active,
.button:not(.carousel-arrow):active,
a.wikia-button:focus-visible,
.wikia-single-button a:focus-visible,
.wikia-menu-button:focus-visible,
.button:not(.carousel-arrow):focus-visible {
  background-color: var(--w-button-color-hover);
  outline-color: var(--w-button-outline-color-hover);
  text-decoration: none;
}
a.wikia-button:not(:disabled):focus-visible,
.wikia-single-button a:not(:disabled):focus-visible,
.wikia-menu-button:not(:disabled):focus-visible,
.button:not(.carousel-arrow):not(:disabled):focus-visible {
  box-shadow: rgba(255, 255, 255, 0.8) -1px -2px 0 0 inset, rgba(0, 0, 0, 0.4) -1px -4px 0px 0px inset;
}
a.wikia-button:disabled,
.wikia-single-button a:disabled,
.wikia-menu-button:disabled,
.button:not(.carousel-arrow):disabled {
  cursor: default;
  opacity: 0.5;
}
a.wikia-button.forward-button,
.wikia-single-button a.forward-button,
.wikia-menu-button.forward-button,
.button:not(.carousel-arrow).forward-button {
  --w-button-color: #0f7bd9;
  --w-button-outline-color: #0f7bd9;
  --w-button-color-hover: #014c8c;
  --w-button-outline-color-hover: #014c8c;
}
a.wikia-button.secondary,
.wikia-single-button a.secondary,
.wikia-menu-button.secondary,
.button:not(.carousel-arrow).secondary {
  --w-button-text-color: var(--theme-body-text-color);
  --w-button-color: transparent;
  --w-button-color-hover: transparent;
}
a.wikia-button.big,
.wikia-single-button a.big,
.wikia-menu-button.big,
.button:not(.carousel-arrow).big {
  padding: 22px;
  font-size: 18px;
  font-weight: 700;
}
th a.wikia-button:last-child,
th .wikia-single-button a:last-child,
th .wikia-menu-button:last-child,
th .button:not(.carousel-arrow):last-child,
td a.wikia-button:last-child,
td .wikia-single-button a:last-child,
td .wikia-menu-button:last-child,
td .button:not(.carousel-arrow):last-child {
  margin-bottom: 0;
}
a.wikia-button img,
.wikia-single-button a img,
.wikia-menu-button img,
.button img:not(.carousel-arrow img) {
  vertical-align: text-bottom;
}
/* Button Fixes */
.wikia-menu-button,
.button:not(.carousel-arrow),
a.wikia-button,
.wikia-single-button a,
.wikia-menu-button,
.wikia-chiclet-button {
  box-sizing: content-box !important;
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.mw-ui-button {
  /* more elegant focus glow */
}
.mw-ui-button:not(:disabled):focus {
  box-shadow: none;
}
.mw-ui-button:not(:disabled):focus-visible {
  box-shadow: rgba(255, 255, 255, 0.8) -1px -2px 0 0 inset;
}
/* Button Modifiers */
body .page-content .full-width-button {
  margin-bottom: 24px;
  padding: 8px;
  width: 98%;
  width: -moz-available;
  width: -webkit-fill-available;
  width: fill-available;
  text-align: center;
}
body .page-content .full-width-button + * {
  margin-top: -24px;
  margin-bottom: 4px;
  width: 100%;
}
body .page-content .full-width-button + * .table-wide-inner,
body .page-content .full-width-button + * .wikitable {
  margin-top: 0;
}
body .page-content .full-width-button::before {
  content: '\2261';
  margin: 0 12px 0 4px;
}
body .page-content .forward-button {
  transition: all 0.5s;
}
body .page-content .forward-button:after {
  content: '';
  position: relative;
  opacity: 0;
  top: 0;
  right: -20px;
  color: var(--w-button-text-color);
  display: inline;
  transition: 0.5s;
}
body .page-content .forward-button:hover:after,
body .page-content .forward-button:active:after,
body .page-content .forward-button:focus-visible:after {
  content: '\00bb';
  opacity: 1;
  right: 0;
  padding-left: 12px;
}
body .page-content .tablecollapse-button {
  padding: 5px;
  margin: 1px;
  float: right;
}
/* Page Specific Styling */
/****************************
 * General
 ****************************/
/* Effects widgets on the front page / templates that use this class. */
.widget-title,
.widget-subtitle {
  font-family: var(--fontface-title);
  font-weight: 700;
  line-height: 2.2;
  letter-spacing: 1.1px;
  text-align: center;
  text-transform: uppercase;
  border-radius: 4px;
}
.widget-title .widget-title-h2,
.widget-subtitle .widget-subtitle-h3 {
  border: 0;
  margin: 0;
  padding: 0;
  line-height: 1.25;
}
.widget-title {
  margin: 13px 0 10px 0;
  padding: 12px 4px;
  font-size: 21px;
}
.widget-title h2 {
  font-size: 21px;
}
.widget-subtitle {
  margin: 0 auto 10px auto;
  padding: 7px 4px;
  border: 1px solid var(--theme-border-color);
  font-size: 17px;
  width: 90%;
}
.widget-subtitle h3 {
  font-size: 17px;
}
.color1 {
  background: var(--theme-accent-color);
  color: var(--theme-accent-label-color);
}
.color2 {
  background: #AA4A98;
  color: #fff;
}
.theme-fandomdesktop-light .color2 {
  background: #E88CD7;
  color: #111;
}
.theme-fandomdesktop-light .color2 a {
  color: white;
}
.color3 {
  background: #cc9933;
  color: #fff;
}
.theme-fandomdesktop-light .color3 {
  background: #ecc881;
  color: #111;
}
.theme-fandomdesktop-light .color3 a {
  color: white;
}
/****************************
 * Project:Poll
 ****************************/
/* Changes the color of the bars on polls to fit wiki colors. */
.pollAnswerVotes {
  color: #DDD;
  background: #000000;
}
.pollAnswerVotes div {
  background-color: #3e456c !important;
  background-image: linear-gradient(to right, #22263b, #3e456c) !important;
}
/****************************
 * Project:News/article
 ****************************/
.newsarticle-heading {
  border-bottom: 1px solid #b2af9c;
}
.newsarticle-new {
  color: white;
  background: red;
  padding: 1px 3px;
  border-radius: 5px;
  border: 2px dotted darkred;
}
.newsarticle-date {
  float: right;
}
.newsarticle-content {
  padding: 0 5px 0 25px;
  margin: 3px 0 8px 0;
  background: #151825;
  border: 1px solid #000000;
}
.newsarticle-content:after {
  content: "";
  display: block;
  clear: both;
}
.newsarticle-links {
  float: right;
  border: 1px solid #000000;
  line-height: 1;
  padding: 2px 2px 1px 2px;
  border-radius: 2px;
  background: rgba(0, 0, 0, 0.01);
}
.newsarticle-links:empty {
  display: none;
}
/* Fandomdesktop weirdness*/
p + .darkTable-wrapper,
p + .darkTable {
  margin-top: -1.5em;
}
/* Article of the Month styling */
.article-month-wrapper {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
}
.article-month-picture {
  text-align: center;
}
.article-month-slot {
  margin-top: 2em;
  text-align: center;
  max-width: 200px;
}
.article-month-heading {
  font-family: var(--fontface-title);
  font-weight: bold;
  margin: 18px 0 9px;
  padding: 6px 0;
  border-bottom: 1px solid var(--theme-border-color);
  font-size: 24px;
  line-height: 1.25;
}
.article-month-content {
  width: 70%;
  margin-left: 1.5em;
}
.article-month-wrapper .note {
  font-size: small;
  color: gray;
}
/****************************
 * Front page tabber styling
 ****************************/
.frontpage-tabber .tabber.wds-tabber {
  border: none;
}
.frontpage-tabber .tabber.wds-tabber .wds-tabs__wrapper {
  width: fit-content;
  margin: auto auto;
}
.frontpage-tabber .tabber.wds-tabber .wds-tabs__wrapper.with-bottom-border {
  border-bottom: 1px solid var(--wds-tab-border-color);
  border: 1px solid var(--wds-tab-border-color);
  border-radius: 12px;
  padding: 2px;
}
.frontpage-tabber .tabber.wds-tabber .wds-tabs__tab {
  padding: 0 12px;
  border-radius: 12px;
}
.frontpage-tabber .tabber.wds-tabber .wds-tabs__tab:hover {
  background-color: rgba(var(--theme-link-color--rgb),0.1);
}
.frontpage-tabber .tabber.wds-tabber .wds-tabs__tab.wds-is-current {
  border-color: transparent;
  box-shadow: none;
}
.frontpage-tabber .tabber.wds-tabber .wds-tabs__tab.wds-is-current .wds-tabs__tab-label {
  box-shadow: inset 0 -3px 0 -1px var(--theme-link-color);
}
/****************************
 * Front page gallery styling
 ****************************/
.frontpage-gallery .wikia-gallery {
  position: relative;
  padding: 8px 0;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
.frontpage-gallery .wikia-gallery-item {
  display: flex;
  width: 200px !important;
  margin: 3px;
  padding: 5px 15px 10px 15px;
  border-radius: 12px;
  transition: all 0.2s ease;
  background-color: rgba(255, 255, 255, 0.07);
  box-shadow: rgba(255, 255, 255, 0.1) 0 -5px 0px 0px inset;
}
.theme-fandomdesktop-light .frontpage-gallery .wikia-gallery-item {
  background-color: rgba(0, 0, 0, 0.07);
  box-shadow: rgba(0, 0, 0, 0.2) 0 -5px 0px 0px inset;
}
.frontpage-gallery .wikia-gallery-item a {
  font-size: 14px;
  color: var(--theme-page-text-color);
  word-wrap: anywhere;
  font-weight: 600;
}
.frontpage-gallery .wikia-gallery-item .thumb {
  min-width: 80px;
  min-height: 80px;
  display: flex;
  align-items: center;
}
.frontpage-gallery .wikia-gallery-border-small .thumb .gallery-image-wrapper {
  border-width: 0;
}
.frontpage-gallery .wikia-gallery-item img {
  transform: scale(0.9);
  transition: transform 0.1s ease;
}
.frontpage-gallery .wikia-gallery-item .lightbox-caption {
  width: inherit !important;
  margin: 0;
  align-self: center;
  text-align: right;
}
/* hover/active */
.frontpage-gallery .frontpage-gallery-link:hover .wikia-gallery-item,
.frontpage-gallery .wikia-gallery-item:hover,
.frontpage-gallery .frontpage-gallery-link:focus .wikia-gallery-item,
.frontpage-gallery .wikia-gallery-item:focus {
  transform: scale(0.98);
  opacity: 0.7;
  box-shadow: rgba(255, 255, 255, 0.4) 0px 0px 2px 1px inset;
}
.theme-fandomdesktop-light .frontpage-gallery .frontpage-gallery-link:hover .wikia-gallery-item,
.theme-fandomdesktop-light .frontpage-gallery .wikia-gallery-item:hover,
.theme-fandomdesktop-light .frontpage-gallery .frontpage-gallery-link:focus .wikia-gallery-item,
.theme-fandomdesktop-light .frontpage-gallery .wikia-gallery-item:focus {
  box-shadow: rgba(0, 0, 0, 0.6) 0px 0px 2px 1px inset;
}
/*
.frontpage-gallery .frontpage-gallery-link:active .wikia-gallery-item,
.frontpage-gallery .wikia-gallery-item:active {
	background-color: #fbd78a;
	box-shadow: 0 2px 15px #fbd78a;
	color: black;
	a {
		color: black;
	}
}
*/
/* Site features styling */
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
body .size-small,
body .smalltxt {
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
.article-columns-2 ul,
.article-columns-3 ul,
.article-columns-2 ol,
.article-columns-3 ol {
  margin-top: 0;
  margin-bottom: 0;
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
.page-content table.table-margin-off {
  margin: 0;
}
.page-content table tr td.table-margin-off {
  padding: 0;
}
.page-content table .table-section-separator,
.page-content table .table-section-separator-top {
  border-top: 3px solid var(--theme-border-color);
}
.page-content table .table-section-separator.thick,
.page-content table .table-section-separator-top.thick {
  border-top-width: 5px;
  border-top-color: var(--theme-accent-color);
}
.page-content table .table-section-separator-bottom {
  border-bottom: 3px solid var(--theme-border-color);
}
.page-content table .table-section-separator-bottom.thick {
  border-bottom-width: 5px;
  border-bottom-color: var(--theme-accent-color);
}
.page-content table .table-section-separator-left {
  border-left: 3px solid var(--theme-border-color);
}
.page-content table .table-section-separator-left.thick {
  border-left-width: 5px;
  border-left-color: var(--theme-accent-color);
}
.page-content table .table-section-separator-right {
  border-right: 3px solid var(--theme-border-color);
}
.page-content table .table-section-separator-right.thick {
  border-right-width: 5px;
  border-right-color: var(--theme-accent-color);
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
.oddrow tr:nth-of-type(odd) > td,
tr.oddrow td {
  background: #85858530;
}
.oddrow2 tr:nth-of-type(odd) > td,
tr.oddrow2 td {
  background: #85858548;
}
/* Article Scrollbar Tweaks */
.article-scrollable {
  overflow: auto;
}
.article-scrollable,
.table-wide-inner {
  /* Article Scrollbar Tweaks (Firefox) */
  scrollbar-width: thin;
  /*scrollbar-color: #897e81 #50373a;*/
}
.article-scrollable::-webkit-scrollbar,
.table-wide-inner::-webkit-scrollbar {
  width: 10px;
  height: 10px;
}
.article-scrollable::-webkit-scrollbar-track,
.table-wide-inner::-webkit-scrollbar-track {
  background-color: rgba(80, 55, 58, 0.5);
}
.article-scrollable::-webkit-scrollbar-thumb,
.table-wide-inner::-webkit-scrollbar-thumb {
  background-color: rgba(137, 126, 129, 0.5);
}
.article-scrollable::-webkit-scrollbar-thumb:hover,
.table-wide-inner::-webkit-scrollbar-thumb:hover {
  background-color: rgba(110, 101, 104, 0.5);
}
/* Disables text highlighting on browsers */
.noselect,
.invslot,
.mcui {
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
.desktop-hide,
.hidden {
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
}
th .blankCell:after,
td .blankCell:after {
  content: "∅";
  flex: 1;
  align-self: center;
  color: rgba(185, 185, 185, 0.55);
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
  transition: opacity 0.7s linear 0s;
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
  font-size: 0.8em;
  text-align: right;
  cursor: default;
  text-decoration: none;
  padding: 0.4em 1em;
}
.comment-id-display abbr:hover,
.reply-id-display abbr:hover {
  background-color: rgba(254, 195, 86, 0.1);
  color: var(--theme-link-color);
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
}
.gemstone-slot a {
  color: currentColor;
  cursor: help;
  width: 100%;
  text-align: center;
}
.gemstone-slot .gemstone-slot-lock {
  position: absolute;
  bottom: -2px;
  right: -2px;
  font-size: 10px;
  line-height: 1;
}
.gemstone-slot .gemstone-slot-lock:after {
  content: '🔒';
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
  background-color: rgba(var(--theme-accent-color--rgb), .23);
}
.lighttable tr.highlight-on th {
  background-color: var(--theme-accent-color);
}
.lighttable tr.highlight-on td {
  background-color: rgba(var(--theme-accent-color--rgb), .5);
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
  font-family: Arial, Helvetica, sans-seri;
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
}
#editpage-specialchars a {
  font-family: monospace;
}
#editpage-specialchars hr {
  color: #e6e6e6;
}
#editpage-specialchars .mw-charinsert-item {
  min-width: 1.2em;
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
  border: 0.5px solid #e6e6e6;
}
#recentchange-custom-links hr {
  background-color: #e6e6e6;
  border: 0;
  height: 1px;
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
}
.page-content .treeview .treeview-header {
  padding-left: 3px;
  font-weight: bold;
}
.page-content .treeview .treeview-header:last-child {
  border-color: #636363 !important;
  border-left-style: dotted;
}
.page-content .treeview .treeview-header:not(:last-child):before {
  content: none;
}
.page-content .treeview .treeview-header:last-child:before {
  border-bottom: 0;
}
.page-content .treeview ul,
.page-content .treeview li,
.page-content .treeview ul:last-child,
.page-content .treeview li:last-child {
  margin: 0;
  padding: 0;
  list-style-type: none;
  list-style-image: none;
}
.page-content .treeview li li,
.page-content .treeview li li:last-child {
  position: relative;
  padding-left: 13px;
  margin-left: 7px;
  border-left: 1px solid #636363;
}
.page-content .treeview li li:before {
  content: "";
  position: absolute;
  top: 0;
  left: -0.8px;
  width: 11px;
  height: 11px;
  border-bottom: 1px solid #636363;
}
.page-content .treeview li li:last-child:not(.treeview-continue) {
  border-color: transparent;
}
.page-content .treeview li li:last-child:not(.treeview-continue):before {
  border-left: 1px solid #636363;
  width: 10px;
}
/** Element custom styling **/
/* preformatted text custom styling */
pre.dark,
pre .dark {
  background-color: #002b36;
}
/* horizontal rule custom styling */
hr.tan-line,
hr .tan-line {
  margin: 0.1em 2px;
  border: 0.5px solid tan;
}
hr.weak-line,
hr .weak-line {
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
}
.color-display-table .col-name {
  text-align: right;
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
  padding-bottom: 0.5em;
  margin: 1em 0;
}
.noarticletext-block hr {
  margin-top: 2em;
}
/* Page Header styling */
.article-pageheader {
  margin: 1em 0;
  box-shadow: 0 0 5px #fff;
}
.article-pageheader-title {
  padding: 1em 4em;
  background: rgba(var(--theme-accent-color--rgb),0.7);
}
.article-pageheader-body {
  padding: 1em 4em;
  background-color: rgba(var(--theme-accent-color--rgb),0.2);
}
/* Good article, featured article (Project:GA, Project:AOTM) */
.article-featured-article-icon,
.article-good-article-icon {
  display: inline-block;
  border-radius: 4px;
  padding: 0 6px;
}
.article-featured-article-icon img,
.article-good-article-icon img {
  vertical-align: sub;
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
  margin: 0.5em 0;
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
}
.dual-table-grid table {
  margin: 0;
  height: 100%;
}
.dual-table-grid .seperator-cell {
  border-bottom: 5px solid var(--theme-accent-color);
}
@media screen and (max-width: 800px) {
  .dual-table-grid {
    grid-template-columns: 1fr;
  }
}
/* Enchantment table row */
.article-enchantments-table .enchnamediv {
  display: flex;
  gap: 16px;
}
.article-enchantments-table .enchreqdiv {
  flex: 1;
  text-align: right;
  font-weight: normal;
}
.article-enchantments-table .enchdisctr {
  height: 100%;
}
.article-enchantments-table .enchdisctr > td {
  text-align: left;
  vertical-align: top;
}
.article-enchantments-table .enchaffectsdiv {
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
}
.article-enchantments-table .enchaffectsdiv > div {
  display: flex;
  gap: 0 1ex;
  text-align: center;
}
/* TOC styling */
.article-custom-toc {
  width: 55%;
}
.article-custom-toc p {
  margin-bottom: 0;
}
.article-custom-toc .content {
  border-top: 1px solid #aaa;
  border-bottom: 1px solid #aaa;
  margin: 10px 0;
  padding: 10px 0;
  max-height: 400px;
  overflow: auto;
}
.article-custom-toc .content .inner {
  columns: 100px 3;
}
/* Tutorials */
.tut-nav {
  display: grid;
  margin-top: 32px;
  gap: 16px;
  grid-template-columns: repeat(2, 1fr);
}
.tut-nav a {
  display: block;
  color: var(--theme-accent-color);
  padding: 18px;
  border: 1px solid var(--theme-border-color);
  border-radius: 6px;
  line-height: 1.2;
  transition: border-color 0.2s ease-out;
  font-weight: 700;
}
.tut-nav a::before {
  color: var(--theme-body-text-color);
  font-size: 95%;
  font-weight: 600;
}
.tut-nav a:hover {
  border-color: var(--theme-accent-color);
  text-decoration: none;
}
.tut-nav a:hover .label {
  text-decoration: none;
}
.tut-next a {
  text-align: right;
}
.tut-next a::before {
  content: "Next";
}
.tut-next a .label::after {
  content: " »";
}
.tut-prev a::before {
  content: "Previous";
}
.tut-prev a .label::before {
  content: "« ";
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
}
.tut-browse li a:hover {
  color: black;
  text-decoration: none;
}
.theme-fandomdesktop-light .tut-browse li a:hover {
  color: white;
}
.tut-browse li a:hover .label {
  text-decoration: none;
}
.tut-browse li a::before {
  content: "Tutorial ";
  display: flex;
  align-items: center;
  margin-right: 14px;
  padding: 5px 14px 5px 14px;
  border-radius: 6px 0 0 6px;
  color: black;
}
.theme-fandomdesktop-light .tut-browse li a::before {
  color: white;
}
.tut-browse li a .label {
  align-self: center;
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
.hover-switch .hov,
.hover-switch:hover .nohov {
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
.circled-y:before,
.circled-n:before {
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
.circled-y.centered,
.circled-n.centered {
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
  background-image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij48cGF0aCBkPSJNMjEgMTN2MTBoLTIxdi0xOWgxMnYyaC0xMHYxNWgxN3YtOGgyem0zLTEyaC0xMC45ODhsNC4wMzUgNC02Ljk3NyA3LjA3IDIuODI4IDIuODI4IDYuOTc3LTcuMDcgNC4xMjUgNC4xNzJ2LTExeiIvPjwvc3ZnPg==);
  /* https://iconmonstr.com/share-11-svg/ */
}
.cl-badge.cl-icon:after {
  background-image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij48cGF0aCBkPSJNMjIgNnYxNmgtMTZ2LTE2aDE2em0yLTJoLTIwdjIwaDIwdi0yMHptLTI0LTR2MjBoMnYtMThoMTh2LTJoLTIweiIvPjwvc3ZnPg==);
  /* https://iconmonstr.com/layer-1-svg/ */
}
/* Custom container styling ("boxes") for this wiki */
/* Message Boxes & Text Sections */
/* Coloring impl attributed to Minecraft Wiki (minecraft.fandom.com) */
/* Template:MessageBoxPlus */
.messagebox,
.messagebox-inline,
.messagebox-boxed {
  --box-background-highlight: rgba(var(--theme-accent-color--rgb), .05);
  --box-border-highlight: var(--theme-accent-color);
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1em;
  margin: 1em 0;
  padding: 0.4em 1.6em;
  background-color: var(--box-background-highlight);
  box-shadow: inset 3px 0 0 0 var(--box-border-highlight), inset -3px 0 0 0 var(--box-border-highlight);
  border-radius: 0.5em;
  border: none;
  font-size: 14px;
  text-align: left;
  overflow: auto;
}
.textsection,
.textsection-inline,
.textsection-boxed {
  --box-border-highlight: var(--theme-border-color);
  padding: 0.5em 1.2em;
  border-radius: 0.5em;
  border: 1px solid var(--box-border-highlight);
  border-width: 1px 6px;
}
.wikia-menu-button + .textsection {
  margin-top: -14px;
}
.messagebox-inline,
.textsection-inline {
  display: inline-flex;
  margin: 0 1em;
}
.messagebox-boxed,
.textsection-boxed {
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
.messagebox-warn,
.messagebox-error {
  box-shadow: inset 3px 0 0 0 var(--theme-page-text-color), inset -3px 0 0 0 var(--theme-page-text-color);
  color: #eee;
}
.messagebox-warn a,
.messagebox-error a {
  color: #fec356;
}
.messagebox-warn {
  background-color: #905f00;
}
.messagebox-error {
  background-color: #7F0000;
}
/* Dark Message Box - Template:DarkMessageBox */
.darkmsgbox,
.quotebox {
  display: grid;
  grid-template-columns: auto 1fr auto;
  grid-template-rows: auto;
  grid-template-areas: "im1    text   im2   " "footer footer footer";
}
.darkmsgbox > div,
.quotebox > div {
  display: flex;
  justify-content: center;
  align-content: center;
  flex-direction: column;
}
.darkmsgbox {
  margin: 1em 5px;
}
.darkmsgbox .darkmsgbox-image {
  padding: 15px;
  box-shadow: 0 0 5px var(--box-border-highlight);
  border: 1px solid;
  border-color: var(--box-border-highlight);
  background-color: var(--box-border);
}
.darkmsgbox .darkmsgbox-text {
  padding: 3px 8px;
  box-shadow: 0 0 5px var(--box-border-highlight);
  border: 1px solid;
  border-color: var(--box-border-highlight);
  grid-area: text;
  background-color: var(--box-background-highlight);
}
.darkmsgbox .darkmsgbox-bottom {
  text-align: center;
  box-shadow: 0 0 5px var(--box-border-highlight);
  border: 1px solid;
  border-color: var(--box-border-highlight);
  grid-area: footer;
}
.theme-fandomdesktop-dark .darkmsgbox .darkmsgbox-bottom {
  background-color: var(--custom-adaptive-extradark);
}
.theme-fandomdesktop-light .darkmsgbox .darkmsgbox-bottom {
  background-color: #c9c9c9;
  /* using grayscale */
}
.theme-fandomdesktop-dark .darkmsgbox {
  --box-background-highlight: var(--custom-adaptive-semidark);
  --box-border: var(--custom-adaptive-lighter);
  --box-border-highlight: var(--theme-accent-color);
}
.theme-fandomdesktop-light .darkmsgbox {
  --box-background-highlight: var(--custom-adaptive-lighter);
  --box-border: var(--custom-adaptive-semidark);
  --box-border-highlight: var(--theme-accent-color);
}
/* Quote Box */
.quotebox .quotebox-image-left,
.quotebox .quotebox-image-right,
.quotebox .quotebox-text,
.quotebox .quotebox-bottom {
  padding: 4px 10px;
}
.quotebox .quotebox-image-left,
.quotebox .quotebox-image-right {
  justify-content: flex-end;
}
.quotebox .quotebox-image-left {
  rotate: 180deg;
}
.quotebox .quotebox-bottom {
  grid-area: footer;
  text-align: right;
}
/* AF Warning Styles */
.afwarning-box .afwarning-mark {
  opacity: 75%;
  min-width: fit-content;
}
.theme-fandomdesktop-light .afwarning-box .afwarning-mark {
  filter: invert(1);
}
.afwarning-box .afwarning-title {
  font-size: 2.3em;
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
}
.theme-fandomdesktop-light .widgetbox {
  --widgetbox-border: #a9a9a9;
  --widgetbox-header-background: #ed9a01;
  --widgetbox-header-border: #583900;
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
}
.delete-box a {
  color: #fec356;
}
.delete-box hr {
  margin: 0.1em 3px;
  border: 0.5px solid tan;
}
.delete-box .button {
  padding: 10px;
  font-size: 1em;
  font-weight: bold;
  width: 100%;
  height: 100%;
}
.delete-box .delete-box-buttons {
  margin-left: 2%;
  margin-right: 2%;
  font-size: 14px;
}
.delete-box .delete-box-buttons td:first-of-type {
  text-align: left;
}
.delete-box .delete-box-buttons td:last-of-type {
  margin-right: 2em;
}
.delete-box .delete-box-reason {
  font-size: 14px;
}
/* Rightbox */
.hsw-rightbox.small {
  float: right;
  margin: 5px 2px 2px 5px;
  padding: 14px;
  text-align: center;
  font-size: 75%;
}
.hsw-rightbox.medium {
  float: right;
  width: 240px;
  margin: 0.1em 0.1em 0.5em 0.25em;
  padding: 4px;
}
.hsw-rightbox.small,
.hsw-rightbox.medium {
  border: 1px solid var(--theme-accent-color);
  box-shadow: 0 0 5px var(--theme-accent-color);
}
.theme-fandomdesktop-light .hsw-rightbox.small,
.theme-fandomdesktop-light .hsw-rightbox.medium {
  background-color: #ddd;
  /* using grayscale */
}
.theme-fandomdesktop-dark .hsw-rightbox.small,
.theme-fandomdesktop-dark .hsw-rightbox.medium {
  background-color: var(--custom-adaptive-dark);
}
.hsw-rightbox .hsw-rightbox-sep {
  border-bottom: 1px solid #555;
  padding: 0 3px;
  clear: right;
}
.hsw-rightbox .hsw-rightbox-image {
  border-right: 0;
  padding: 0 12px;
}
.hsw-rightbox .hsw-rightbox-content {
  border-left: 0;
  width: 100%;
  padding: 0 5px 0 0;
}
.hsw-luabox {
  float: right;
  width: 240px;
  margin: 0.1em 0.1em 0.5em 0.25em;
  padding: 4px;
  box-shadow: 0 0 5px var(--theme-accent-color);
  border: 1px solid var(--theme-accent-color);
}
.theme-fandomdesktop-light .hsw-luabox {
  background-color: #ddd;
  /* using grayscale */
}
.theme-fandomdesktop-dark .hsw-luabox {
  background-color: var(--custom-adaptive-dark);
}
.hsw-luabox .hsw-luabox-list {
  list-style-type: disc;
  margin: 0 0 0 15px;
  white-space: nowrap;
}
.hsw-luabox .hsw-luabox-actions {
  font-size: small;
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
  padding: 2.5px;
}
.hsw-shortcut-list {
  font-weight: bold;
}
.hsw-archivebox {
  float: right;
  margin: 7px 0;
  border: 2px solid var(--theme-page-text-color);
  box-shadow: 0 0 15px #000000;
}
.hsw-archivebox .hsw-archivebox-header {
  padding: 1.5px;
}
.hsw-archivebox .hsw-archivebox-content {
  padding: 2px 15px;
  background-color: var(--custom-adaptive-light);
}
.hsw-archivebox .hsw-archivebox-text {
  padding: 0 15px;
  background-color: var(--custom-adaptive-light);
  text-align: center;
}
.hsw-archivebox .hsw-archivebox-list {
  padding: 4px 14px;
  border-top: 2px solid var(--custom-adaptive-extralight);
  border-bottom: 2px solid var(--custom-adaptive-extralight);
}
.hsw-archivebox .hsw-archivebox-search {
  padding: 4px;
}
.hsw-archivebox .mw-ui-input {
  font-size: small;
}
.hsw-archivebox .mw-ui-button {
  height: 32px;
}
.hsw-archivelist .hsw-archivelist-actions {
  font-size: 10px;
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
}
.theme-fandomdesktop-light .cd-ongoing {
  color: #349134;
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
.userbox-retro .userbox-info {
  background-color: var(--custom-adaptive-extralight);
}
.userbox-retro .userbox-id {
  background-color: var(--custom-adaptive-light);
}
/* Documentation Boxes */
.hsw-documentation {
  border: 1.3px solid var(--theme-page-text-color);
  clear: both;
}
.hsw-documentation .hsw-documentation-titlebox {
  padding: 18px 8px 2px 8px;
  margin: 4px 4px 0 4px;
  box-shadow: 0 0 2px var(--theme-page-text-color);
}
.hsw-documentation .hsw-documentation-titlebox .hsw-documentation-icon {
  float: left;
}
.hsw-documentation .hsw-documentation-titlebox .hsw-documentation-header {
  font: bold x-large Arial;
  margin-left: 7px;
  text-align: center;
}
.hsw-documentation .hsw-documentation-titlebox .hsw-documentation-actions {
  font-size: small;
  margin-left: 7px;
}
.hsw-documentation .hsw-documentation-titlebox .hsw-documentation-tnote {
  font-size: small;
  font-style: italic;
}
.hsw-documentation .hsw-documentation-titlebox .page-header__separator {
  background-color: var(--theme-accent-label-color);
  border: 0;
  height: 1px;
  margin-bottom: 3px;
  margin-top: 0;
  width: 100%;
}
.hsw-documentation .hsw-documentation-titlebox p {
  margin: 0;
}
.hsw-documentation .hsw-documentation-body {
  background-color: rgba(120, 120, 120, 0.05);
  box-shadow: 0 0 2px var(--theme-page-text-color);
  padding: 0.5em;
  margin: 0 4px;
  padding: 20px 20px 10px;
  clear: both;
}
.hsw-documentation .hsw-documentation-body .hsw-documentation-main-idk {
  display: none;
}
.hsw-documentation .hsw-documentation-body .hsw-documentation-main-pd {
  clear: both;
  margin-bottom: 5px;
}
.hsw-documentation .hsw-documentation-bottombox {
  padding: 2px 8px;
  margin: 0 4px 4px 4px;
  box-shadow: 0 0 2px var(--theme-page-text-color);
}
.hsw-documentation .hsw-documentation-bottombox .hsw-documentation-hdtw {
  margin: 5px;
  font-weight: bold;
}
.hsw-documentation .hsw-documentation-jtc,
.hsw-documentation .hsw-documentation-btt {
  float: right;
  margin-top: 4px;
  font-style: italic;
  font-size: small;
}
/* Dark Table (Front Page) */
.darkTable-wrapper {
  background: var(--custom-adaptive-dark);
  padding: 0.8em 0.6em;
  margin-bottom: 1em;
  border-radius: 12px;
  border-top: 4px solid #303030;
  border-bottom: 1px solid #303030;
}
.theme-fandomdesktop-light .darkTable-wrapper {
  background: var(--custom-adaptive-extralight);
  border-top-color: #adadad;
  border-bottom-color: #adadad;
}
.darkTable-wrapper table,
.darkTable {
  width: 100%;
  table-layout: fixed;
}
.darkTable-wrapper td,
.darkTable td {
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
.mw-parser-output .boxcol-blue {
  --box-background-highlight: var(--custom-background-blue-highlight);
  --box-border-highlight: var(--custom-border-blue-highlight);
  --box-background: var(--custom-background-blue);
  --box-border: var(--custom-border-blue);
}
.mw-parser-output .boxcol-green {
  --box-background-highlight: var(--custom-background-green-highlight);
  --box-border-highlight: var(--custom-border-green-highlight);
  --box-background: var(--custom-background-green);
  --box-border: var(--custom-border-green);
}
.mw-parser-output .boxcol-orange {
  --box-background-highlight: var(--custom-background-orange-highlight);
  --box-border-highlight: var(--custom-border-orange-highlight);
  --box-background: var(--custom-background-orange);
  --box-border: var(--custom-border-orange);
}
.mw-parser-output .boxcol-purple {
  --box-background-highlight: var(--custom-background-purple-highlight);
  --box-border-highlight: var(--custom-border-purple-highlight);
  --box-background: var(--custom-background-purple);
  --box-border: var(--custom-border-purple);
}
.mw-parser-output .boxcol-red {
  --box-background-highlight: var(--custom-background-red-highlight);
  --box-border-highlight: var(--custom-border-red-highlight);
  --box-background: var(--custom-background-red);
  --box-border: var(--custom-border-red);
}
.mw-parser-output .boxcol-yellow {
  --box-background-highlight: var(--custom-background-yellow-highlight);
  --box-border-highlight: var(--custom-border-yellow-highlight);
  --box-background: var(--custom-background-yellow);
  --box-border: var(--custom-border-yellow);
}
.mw-parser-output .boxcol-magenta {
  --box-background-highlight: var(--custom-background-magenta-highlight);
  --box-border-highlight: var(--custom-border-magenta-highlight);
  --box-background: var(--custom-background-magenta);
  --box-border: var(--custom-border-magenta);
}
.mw-parser-output .boxcol-gray {
  --box-background-highlight: var(--custom-background-grey);
  /* no highlight defined, yet */
  --box-border-highlight: var(--custom-border-grey);
  /* no highlight defined, yet */
  --box-background: var(--custom-background-grey);
  --box-border: var(--custom-border-grey);
}
/* For custom color classes on this wiki */
/* Custom background color */
.cbgh-blue {
  background-color: var(--custom-background-blue-highlight);
}
.cbgh-red {
  background-color: var(--custom-background-red-highlight);
}
/* Minecraft Colors */
.color-black {
  color: #000000;
}
.color-dark_blue {
  color: #0000AA;
}
.color-dark_green {
  color: #00AA00;
}
.color-dark_aqua {
  color: #00AAAA;
}
.color-dark_red {
  color: #AA0000;
}
.color-dark_purple {
  color: #AA00AA;
}
.color-gold {
  color: #FFAA00;
}
.color-gray {
  color: #AAAAAA;
}
.color-dark_gray {
  color: #555555;
}
.color-blue {
  color: #5555FF;
}
.color-green {
  color: #55FF55;
}
.color-aqua {
  color: #55FFFF;
}
.color-red {
  color: #FF5555;
}
.color-light_purple {
  color: #FF55FF;
}
.color-yellow {
  color: #FFFF55;
}
.color-white {
  color: #FFFFFF;
}
/* Other SkyBlock Colors */
.color-dungeon_d {
  color: #fc2803;
}
.color-dungeon_c {
  color: #0373fc;
}
.color-dungeon_b {
  color: #40a40c;
}
.color-dungeon_a {
  color: #b700ff;
}
.color-dungeon_S {
  color: #ffc800;
}
.color-dungeon_splus {
  color: #ffc800;
}
/* Custom colors on this wiki */
/* can use http://auburn.colorcode.is/ to find a suitable name for your color */
.color-silver {
  color: #C0C0C0;
}
.color-turquoise {
  color: #00AAAA;
}
.color-bronze {
  color: #803600;
}
.color-orange {
  color: #FF921E;
}
.color-pink {
  color: #FF55FF;
}
.color-html_red {
  color: red;
}
.color-html_green {
  color: green;
}
.color-html_blue {
  color: blue;
}
.color-html_pink {
  color: pink;
}
.color-alburn {
  color: #A52A2A;
}
.color-blue_violet {
  color: #8A2BE2;
}
/* Animated Colors */
.color-crystal_armor {
  animation: crystal_armor linear 1s infinite alternate;
}
@keyframes crystal_armor {
  0% {
    color: #1F0030;
  }
  6.25% {
    color: #46085E;
  }
  12.5% {
    color: #54146E;
  }
  18.75% {
    color: #5D1C78;
  }
  25% {
    color: #63237D;
  }
  31.25% {
    color: #6A2C82;
  }
  37.5% {
    color: #7E4196;
  }
  43.75% {
    color: #8E51A6;
  }
  50% {
    color: #9C64B3;
  }
  56.25% {
    color: #A875BD;
  }
  62.5% {
    color: #B88BC9;
  }
  68.75% {
    color: #C9A3D4;
  }
  75% {
    color: #D9C1E3;
  }
  81.25% {
    color: #E5D1ED;
  }
  87.5% {
    color: #EFE1F5;
  }
  93.75% {
    color: #FCF3FF;
  }
  100% {
    color: #FFFFFF;
  }
}
/* Light-color-on-light-theme (LCOLT) styling */
.theme-fandomdesktop-light .light-color,
.theme-fandomdesktop-light .color-aqua,
.theme-fandomdesktop-light .color-green,
.theme-fandomdesktop-light .color-yellow,
.theme-fandomdesktop-light .color-white {
  filter: brightness(70%);
}
/* Editor Styling */
/** 
 * @author Thundercraft5 (https://ucp.fandom.com/wiki/User:Thundercraft5)
 * @use Modifies the ACE code editor to make it look like the retro version
 * @version 0.3
 * @file User:Thundercraft5/global.css/AceEditor.css
 *
 * =====CONTENTS=====
 * *Main Code editor
 * *Syntax highlighting
 */
/*
//#============================================================================#
// MAIN CODE EDITOR
//#============================================================================#
*/
.ace_print-margin {
  display: none !important;
}
.ace_editor {
  line-height: 16px;
}
.ace_marker-layer .ace_selected-word {
  border: 1px solid #355e69;
}
.ace-solarized-light .ace_marker-layer .ace_selection {
  background: rgba(157, 176, 199, 0.18) !important;
}
.ace-tm .ace_marker-layer .ace_bracket {
  border: 1px solid #423c3c;
  background-color: #074252ba !important;
}
.ace-tm .ace_marker-layer .ace_selected-word {
  border: 1px solid rgba(98, 88, 88, 0.64);
  border-radius: 4px;
  background-color: #07425269 !important;
}
.ace_print-margin {
  display: none !important;
}
.ace_gutter {
  background: #003e4d !important;
  color: darkgray !important;
}
.ace_marker-layer .ace_active-line {
  background: #1a4049 !important;
}
.ace_gutter-active-line {
  background: #255b68 !important;
}
.ace_cursor {
  color: #ff1a1a !important;
}
.ace_indent-guide {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAEklEQVQImWNg0Db1ZVCxc/sPAAd4AlUHlLenAAAAAElFTkSuQmCC) right repeat-y !important;
}
.ace_content {
  background-color: #002b36 !important;
}
.editor.ace_editor.ace-tm {
  font-size: 14px;
}
span.ace_identifier:not(.ace_declaration),
div.ace_scroller {
  color: #93a1a1;
}
.editor.ace_editor.ace-tm {
  line-height: 18px !important;
}
.ace_scrollbar.ace_scrollbar-h {
  display: normal !important;
}
.ace-tm .ace_marker-layer .ace_selection {
  background: rgba(255, 255, 255, 0.1) !important;
}
.ace-tm .ace_marker-layer .ace_selected-word {
  background-color: unset !important;
  border: rgba(0, 0, 0, 0.4) !important;
}
/*
//#============================================================================#
// CONSOLE
//#============================================================================#
*/
/* General Setting */
.mw-editform #mw-scribunto-console .mw-scribunto-console-fieldset {
  background: #000;
  background: rgba(0, 0, 0, 0.4);
  margin: 0;
}
.mw-editform #mw-scribunto-console .mw-scribunto-console-fieldset legend {
  background: var(--theme-page-background-color);
  border-radius: 5px;
  box-shadow: inset -2px -3px var(--theme-accent-color);
  padding: 0.2em 1em;
  margin-bottom: 0.6em;
}
/* Console Styling */
.mw-editform #mw-scribunto-console #mw-scribunto-input {
  background: #000;
  border-left: 5px solid #aaa;
  font-family: Consolas,monospace;
  color: #bbb;
}
/* Display Line Styling */
#mw-scribunto-console #mw-scribunto-output .mw-scribunto-message {
  background-color: transparent;
  color: var(--theme-page-text-color);
}
#mw-scribunto-console #mw-scribunto-output .mw-scribunto-input,
#mw-scribunto-console #mw-scribunto-output .mw-scribunto-print,
#mw-scribunto-console #mw-scribunto-output .mw-scribunto-normalOutput,
#mw-scribunto-console #mw-scribunto-output .mw-scribunto-error {
  background: #bbb;
  border-left: 5px solid #666;
  border-bottom: 1px solid #555;
  padding: 0 10px;
  font-family: Consolas, monospace;
  color: black;
}
#mw-scribunto-console #mw-scribunto-output .mw-scribunto-print {
  background: #2288a2;
  border-left: 5px solid #5558ff;
}
#mw-scribunto-console #mw-scribunto-output .mw-scribunto-normalOutput {
  background: #2288a2;
  border-left: 5px solid #00c103;
}
#mw-scribunto-console #mw-scribunto-output .mw-scribunto-error {
  background: #2288a2;
  border-left: 5px solid #ff5575;
}
/*
//#============================================================================#
// SYNTAX HIGHLIGHTING
//#============================================================================#
*/
.ace_paren {
  color: #66cc66 !important;
}
.ace_operator {
  color: #269900 !important;
}
.ace_constant.ace_language {
  font-weight: bold !important;
}
.ace_storage {
  color: #7a6bce !important;
  font-weight: bold !important;
}
.ace_paren {
  color: #66cc66 !important;
}
.ace_operator {
  color: #269900 !important;
}
.ace_keyword:not(.ace_operator),
.ace_meta,
.ace_support.ace_class,
.ace_support.ace_type {
  font-weight: bold !important;
}
span.ace_string {
  color: #2AA198 !important;
}
span.ace_string.ace_regexp {
  color: #fc2222 !important;
}
span.ace_keyword:not(.ace_regexp):not(.ace_operator) {
  color: #859900 !important;
}
span.ace_boolean,
span.ace_constant:not(.ace_numeric) {
  color: #B58900 !important;
}
span.ace_numeric {
  color: #D33682 !important;
}
.ace_storage {
  color: #7a6bce !important;
  font-weight: bold !important;
}
.ace_variable.ace_language {
  color: #a84a4a !important;
  font-weight: bold !important;
}
.ace_declaration {
  color: purple !important;
}
.ace_operator {
  color: #269900 !important;
}
span.ace_constant.ace_language.ace_escape {
  color: #a1bff5 !important;
  font-weight: bold !important;
}
.ace_method,
.ace_variable:not(.ace_language) {
  color: #268bd2 !important;
}
span.ace_constant.ace_language.ace_escape {
  color: #a1bff5 !important;
  font-weight: bold !important;
}
.ace_support.ace_type {
  color: #8b4fce !important;
  font-weight: bold !important;
}
.ace_comment {
  color: #646464 !important;
}
span.ace_constant:not(.ace_numeric):not(.ace_support):not(.ace_language) {
  color: #a22e2e !important;
  font-weight: bold !important;
}
.ace_variable.ace_language {
  color: #a84a4a !important;
  font-weight: bold !important;
}
span.ace_support.ace_function {
  color: #268BD2 !important;
}
span.ace_entity.ace_name.ace_function {
  color: #AC885B !important;
}
span.ace_support.ace_constant.ace_color,
span.ace_support.ace_constant {
  color: #B58900 !important;
  font-weight: bold !important;
}
.ace_string.ace_regexp {
  font-style: italic;
}
.ace_comment {
  font-style: italic !important;
}
.ace_invisible {
  color: rgba(255, 255, 255, 0.25) !important;
}
/* Fix Aceeditor Top Spacing */
.wikiEditor-ui .wikiEditor-ui-view.wikiEditor-ui-view-wikitext .wikiEditor-ui-top {
  min-height: inherit;
}
/**
 * This stylesheet contains all CSS for the mediawiki syntax highlighter.
 * It makes the syntax highlighter look like the old retro version FANDOM used to use.
 *
 * You are free to copy any code from this page
 * As long as you attribute it.
 *
 * @author Thundercraft5 (https://ucp.fandom.com/wiki/User:Thundercraft5)
 * @use Modifies the Syntax Highlighter to look like the old version
 * @version 0.4
 * @file User:Thundercraft5/global.css/CodeHighlight.css
 */
.mw-highlight:not(.mw-highlight-lines) > pre {
  display: contents !important;
}
.mw-highlight {
  line-height: 16px;
  background-color: #002b36 !important;
  overflow: auto !important;
  color: #93a1a1;
  word-wrap: normal;
}
code.mw-highlight {
  padding: 2.5px;
}
div.mw-highlight:not(.mw-highlight-lines) {
  padding: 12px;
}
.contents-only {
  display: contents !important;
}
.mw-highlight .c1,
.mw-highlight .cm {
  color: #646464 !important;
}
.mw-highlight .s1,
.mw-highlight .s2 {
  color: #2AA198 !important;
}
.mw-highlight .kr,
.mw-highlight .kd {
  color: #859900 !important;
}
.mw-highlight .o,
.mw-highlight .p {
  color: #269900 !important;
}
.mw-highlight .nf,
.mw-highlight .nb {
  color: #268BD2 !important;
}
.mw-highlight .mi,
.mw-highlight .mf {
  color: #D33682 !important;
}
.mw-highlight .kc {
  color: #B58900 !important;
  font-weight: bold !important;
}
.mw-highlight .l {
  color: #66cc66 !important;
}
.mw-highlight .ow {
  color: #8b4fce !important;
  font-weight: bold !important;
}
.mw-highlight .nc {
  color: #e25773 !important;
}
.mw-highlight .se {
  color: #a1bff5 !important;
}
.mw-highlight .lb {
  color: #a22e2e;
  font-weight: bold;
}
.mw-highlight .f {
  color: #ef8327;
}
/* Used by Module:Minimap */
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
  transform: translate(-50%, -50%);
}
/***************************************
* Map images
* NOTE: When updating this part, one must re-calibrate values on [[Module:Minimap/Data]] !!
****************************************/
.minimap-hub {
  background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/0/03/Hub_Island_(0.24.1)_(Top_View).png");
}
.minimap-hub-0_24_1 {
  /* pre-revamp */
  background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/0/03/Hub_Island_(0.24.1)_(Top_View).png");
}
.minimap-hub-0_24_aura {
  background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/8/87/Hub_Island_(0.24)_(Aura)_(Top_View).png");
}
.minimap-hub-0_11_4 {
  /* was used as the main image for a while */
  background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/d/da/Hub_Island_(0.11.4)_(Top_View).png");
}
.minimap-hub-0_8 {
  /* Retained for [[Warren]] */
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
.minimap-blazing-fort {
  /* retained! */
  background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/f/f1/Blazing_Fortress_(0.1)_(Top_View).png");
}
.minimap-end {
  background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/f/f8/The_End_(0.7)_(Top_View).png");
}
.minimap-stronghold {
  /* note: if no usage, no retain */
  background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/4/4d/Stronghold_(top_view).png");
}
.minimap-stronghold-1 {
  /* note: if no usage, no retain */
  background-image: url("https://static.wikia.nocookie.net/hypixel-skyblock/images/a/a8/Stronghold_(top_view)_1.png");
}
.minimap-stronghold-2 {
  /* note: if no usage, no retain */
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
/* Local Scripts - Imported on this wiki locally */
/* Staff Colors (Updated via a script at [[MediaWiki:Gadget-StaffColorsUpdater.js]]) */
/* Staff Colors

This stylesheet contains the css to color staff member's names.
It is automatically updated, any changes you make will be 
overwritten next time this stylesheet gets updated.
This is configured on MediaWiki:Gadget-StaffColorsUpdater.json
*/
/*** LINKS ***/
/* Bot*/
/* B's with higher ranks are removed

*/
a[href$="ASMCHK"]:not([href*="auth.fandom.com/"]),
a[href$="EejitbutBot"]:not([href*="auth.fandom.com/"]),
a[href$="Hypixel_SkyBlock_Wiki_Bot"]:not([href*="auth.fandom.com/"]),
a[href$="Hypixel SkyBlock Wiki Bot"]:not([href*="auth.fandom.com/"]),
a[href$="ScoutskylarBot"]:not([href*="auth.fandom.com/"]) {
  color: var(--custom-rolecolor-bot) !important;
}
/* Bureaucrat*/
/* BU's with higher ranks are removed
  a[href$="Hypixel_SkyBlock_Wiki_Bot"]:not([href*="auth.fandom.com/"]),
  a[href$="Hypixel SkyBlock Wiki Bot"]:not([href*="auth.fandom.com/"]),
*/
a[href$="Scoutskylar"]:not([href*="auth.fandom.com/"]) {
  color: var(--custom-rolecolor-bureaucrat) !important;
}
/* Administrator*/
/* AD's with higher ranks are removed
  a[href$="EejitbutBot"]:not([href*="auth.fandom.com/"]),
  a[href$="Hypixel_SkyBlock_Wiki_Bot"]:not([href*="auth.fandom.com/"]),
  a[href$="Hypixel SkyBlock Wiki Bot"]:not([href*="auth.fandom.com/"]),
  a[href$="Scoutskylar"]:not([href*="auth.fandom.com/"]),
  a[href$="ScoutskylarBot"]:not([href*="auth.fandom.com/"]),
*/
a[href$="Abuse_filter"]:not([href*="auth.fandom.com/"]),
a[href$="Abuse filter"]:not([href*="auth.fandom.com/"]),
a[href$="Eejit43"]:not([href*="auth.fandom.com/"]),
a[href$="SakurasouShiina"]:not([href*="auth.fandom.com/"]),
a[href$="TheTrueShaman"]:not([href*="auth.fandom.com/"]) {
  color: var(--custom-rolecolor-sysop) !important;
}
/* Code Editor*/
/* CE's with higher ranks are removed
  a[href$="ASMCHK"]:not([href*="auth.fandom.com/"]),
  a[href$="Eejit43"]:not([href*="auth.fandom.com/"]),
  a[href$="EejitbutBot"]:not([href*="auth.fandom.com/"]),
  a[href$="Scoutskylar"]:not([href*="auth.fandom.com/"]),
  a[href$="ScoutskylarBot"]:not([href*="auth.fandom.com/"]),
  a[href$="TheTrueShaman"]:not([href*="auth.fandom.com/"]),
*/
a[href$="Fewfre"]:not([href*="auth.fandom.com/"]),
a[href$="MonkeysHK"]:not([href*="auth.fandom.com/"]) {
  color: var(--custom-rolecolor-codeeditor) !important;
}
/* Content Moderator*/
/* CM's with higher ranks are removed
  a[href$="Fewfre"]:not([href*="auth.fandom.com/"]),
  a[href$="MonkeysHK"]:not([href*="auth.fandom.com/"]),
*/
a[href$="Lunaynx"]:not([href*="auth.fandom.com/"]),
a[href$="Voball"]:not([href*="auth.fandom.com/"]) {
  color: var(--custom-rolecolor-content-moderator) !important;
}
/* Discussions Moderator*/
/* DM's with higher ranks are removed

*/
/*
{
	color: var(--custom-rolecolor-threadmoderator) !important;
}
*/
/* Rollback*/
/* RB's with higher ranks are removed

*/
a[href$="Absterge7s"]:not([href*="auth.fandom.com/"]),
a[href$="CubicC"]:not([href*="auth.fandom.com/"]),
a[href$="Ikethepro18"]:not([href*="auth.fandom.com/"]),
a[href$="TDVoldy"]:not([href*="auth.fandom.com/"]),
a[href$="TheAetherSword"]:not([href*="auth.fandom.com/"]) {
  color: var(--custom-rolecolor-rollback) !important;
}
/* Artist*/
/* ARD's with higher ranks are removed

*/
a[href$="Duowithng"]:not([href*="auth.fandom.com/"]),
a[href$="Ic22487"]:not([href*="auth.fandom.com/"]),
a[href$="Volcanofr"]:not([href*="auth.fandom.com/"]),
a[href$="WaifuWeek"]:not([href*="auth.fandom.com/"]) {
  color: var(--custom-rolecolor-ard) !important;
}
/* Developer*/
/* DEV's with higher ranks are removed

*/
a[href$="BuggyAl"]:not([href*="auth.fandom.com/"]),
a[href$="Pigicial"]:not([href*="auth.fandom.com/"]),
a[href$="Charzard4261"]:not([href*="auth.fandom.com/"]) {
  color: var(--custom-rolecolor-dev) !important;
}
/*** ICONS ***/
/* Bot*/
/* B's with higher ranks are removed

*/
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:ASMCHK"]:not([role]):not(.extiw):not(.external)::before,
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:EejitbutBot"]:not([role]):not(.extiw):not(.external)::before,
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:Hypixel_SkyBlock_Wiki_Bot"]:not([role]):not(.extiw):not(.external)::before,
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:Hypixel SkyBlock Wiki Bot"]:not([role]):not(.extiw):not(.external)::before,
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:ScoutskylarBot"]:not([role]):not(.extiw):not(.external)::before,
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:Abuse Filter"]:not([role]):not(.extiw):not(.external)::before {
  content: " ";
  background: var(--custom-rolebadge-bot) no-repeat center;
  padding: 0 8px;
  margin-right: 2px;
  background-size: 16px 16px;
}
/* Bureaucrat*/
/* BU's with higher ranks are removed
  *:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:Hypixel_SkyBlock_Wiki_Bot"]:not([role]):not(.extiw):not(.external)::before,
  *:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:Hypixel SkyBlock Wiki Bot"]:not([role]):not(.extiw):not(.external)::before,
*/
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:Scoutskylar"]:not([role]):not(.extiw):not(.external)::before {
  content: " ";
  background: var(--custom-rolebadge-bureaucrat) no-repeat center;
  padding: 0 8px;
  margin-right: 2px;
  background-size: 16px 16px;
}
/* Administrator*/
/* AD's with higher ranks are removed
  *:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:EejitbutBot"]:not([role]):not(.extiw):not(.external)::before,
  *:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:Hypixel_SkyBlock_Wiki_Bot"]:not([role]):not(.extiw):not(.external)::before,
  *:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:Hypixel SkyBlock Wiki Bot"]:not([role]):not(.extiw):not(.external)::before,
  *:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:Scoutskylar"]:not([role]):not(.extiw):not(.external)::before,
  *:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:ScoutskylarBot"]:not([role]):not(.extiw):not(.external)::before,
*/
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:Abuse_filter"]:not([role]):not(.extiw):not(.external)::before,
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:Abuse filter"]:not([role]):not(.extiw):not(.external)::before,
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:Eejit43"]:not([role]):not(.extiw):not(.external)::before,
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:SakurasouShiina"]:not([role]):not(.extiw):not(.external)::before,
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:TheTrueShaman"]:not([role]):not(.extiw):not(.external)::before {
  content: " ";
  background: var(--custom-rolebadge-sysop) no-repeat center;
  padding: 0 8px;
  margin-right: 2px;
  background-size: 16px 16px;
}
/* Code Editor*/
/* CE's with higher ranks are removed
  *:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:ASMCHK"]:not([role]):not(.extiw):not(.external)::before,
  *:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:Eejit43"]:not([role]):not(.extiw):not(.external)::before,
  *:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:EejitbutBot"]:not([role]):not(.extiw):not(.external)::before,
  *:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:Scoutskylar"]:not([role]):not(.extiw):not(.external)::before,
  *:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:ScoutskylarBot"]:not([role]):not(.extiw):not(.external)::before,
  *:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:TheTrueShaman"]:not([role]):not(.extiw):not(.external)::before,
*/
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:Fewfre"]:not([role]):not(.extiw):not(.external)::before,
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:MonkeysHK"]:not([role]):not(.extiw):not(.external)::before {
  content: " ";
  background: var(--custom-rolebadge-codeeditor) no-repeat center;
  padding: 0 8px;
  margin-right: 2px;
  background-size: 16px 16px;
}
/* Content Moderator*/
/* CM's with higher ranks are removed
  *:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:Fewfre"]:not([role]):not(.extiw):not(.external)::before,
  *:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:MonkeysHK"]:not([role]):not(.extiw):not(.external)::before,
*/
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:Lunaynx"]:not([role]):not(.extiw):not(.external)::before,
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:Voball"]:not([role]):not(.extiw):not(.external)::before {
  content: " ";
  background: var(--custom-rolebadge-content-moderator) no-repeat center;
  padding: 0 8px;
  margin-right: 2px;
  background-size: 16px 16px;
}
/* Discussions Moderator*/
/* DM's with higher ranks are removed

*/
/*
{
	content: " ";
	background: var(--custom-rolebadge-threadmoderator) no-repeat center;
	padding: 0 8px;
	margin-right: 2px;
	background-size: 16px 16px;
}
*/
/* Rollback*/
/* RB's with higher ranks are removed

*/
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:Absterge7s"]:not([role]):not(.extiw):not(.external)::before,
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:CubicC"]:not([role]):not(.extiw):not(.external)::before,
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:Ikethepro18"]:not([role]):not(.extiw):not(.external)::before,
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:TDVoldy"]:not([role]):not(.extiw):not(.external)::before,
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:TheAetherSword"]:not([role]):not(.extiw):not(.external)::before {
  content: " ";
  background: var(--custom-rolebadge-rollback) no-repeat center;
  padding: 0 8px;
  margin-right: 2px;
  background-size: 16px 16px;
}
/* Artist*/
/* ARD's with higher ranks are removed

*/
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:Duowithng"]:not([role]):not(.extiw):not(.external)::before,
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:Ic22487"]:not([role]):not(.extiw):not(.external)::before,
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:Volcanofr"]:not([role]):not(.extiw):not(.external)::before,
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:WaifuWeek"]:not([role]):not(.extiw):not(.external)::before {
  content: " ";
  background: var(--custom-rolebadge-ard) no-repeat center;
  padding: 0 8px;
  margin-right: 2px;
  background-size: 16px 16px;
}
/* Developer*/
/* DEV's with higher ranks are removed

*/
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:BuggyAl"]:not([role]):not(.extiw):not(.external)::before,
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:Pigicial"]:not([role]):not(.extiw):not(.external)::before,
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:Charzard4261"]:not([role]):not(.extiw):not(.external)::before {
  content: " ";
  background: var(--custom-rolebadge-dev) no-repeat center;
  padding: 0 8px;
  margin-right: 2px;
  background-size: 16px 16px;
}
/*** TAGS ***/
/* Bot*/
/* B's with higher ranks are removed

*/
a[href$="ASMCHK"][class^="EntityHeader_name"]:after,
a[href$="EejitbutBot"][class^="EntityHeader_name"]:after,
a[href$="Hypixel_SkyBlock_Wiki_Bot"][class^="EntityHeader_name"]:after,
a[href$="Hypixel SkyBlock Wiki Bot"][class^="EntityHeader_name"]:after,
a[href$="ScoutskylarBot"][class^="EntityHeader_name"]:after,
a[href$="Abuse Filter"][class^="EntityHeader_name"]:after {
  content: "Bot" !important;
  font: small-caps normal 100% arial !important;
  margin-left: 10px;
  font-size: 13px !important;
}
/* Bureaucrat*/
/* BU's with higher ranks are removed
  a[href$="Hypixel_SkyBlock_Wiki_Bot"][class^="EntityHeader_name"]:after,
  a[href$="Hypixel SkyBlock Wiki Bot"][class^="EntityHeader_name"]:after,
*/
a[href$="Scoutskylar"][class^="EntityHeader_name"]:after {
  content: "Bureaucrat" !important;
  font: small-caps normal 100% arial !important;
  margin-left: 10px;
  font-size: 13px !important;
}
/* Administrator*/
/* AD's with higher ranks are removed
  a[href$="EejitbutBot"][class^="EntityHeader_name"]:after,
  a[href$="Hypixel_SkyBlock_Wiki_Bot"][class^="EntityHeader_name"]:after,
  a[href$="Hypixel SkyBlock Wiki Bot"][class^="EntityHeader_name"]:after,
  a[href$="Scoutskylar"][class^="EntityHeader_name"]:after,
  a[href$="ScoutskylarBot"][class^="EntityHeader_name"]:after,
*/
a[href$="Abuse_filter"][class^="EntityHeader_name"]:after,
a[href$="Abuse filter"][class^="EntityHeader_name"]:after,
a[href$="Eejit43"][class^="EntityHeader_name"]:after,
a[href$="SakurasouShiina"][class^="EntityHeader_name"]:after,
a[href$="TheTrueShaman"][class^="EntityHeader_name"]:after {
  content: "Administrator" !important;
  font: small-caps normal 100% arial !important;
  margin-left: 10px;
  font-size: 13px !important;
}
/* Code Editor*/
/* CE's with higher ranks are removed
  a[href$="ASMCHK"][class^="EntityHeader_name"]:after,
  a[href$="Eejit43"][class^="EntityHeader_name"]:after,
  a[href$="EejitbutBot"][class^="EntityHeader_name"]:after,
  a[href$="Scoutskylar"][class^="EntityHeader_name"]:after,
  a[href$="ScoutskylarBot"][class^="EntityHeader_name"]:after,
  a[href$="TheTrueShaman"][class^="EntityHeader_name"]:after,
*/
a[href$="Fewfre"][class^="EntityHeader_name"]:after,
a[href$="MonkeysHK"][class^="EntityHeader_name"]:after {
  content: "Code Editor" !important;
  font: small-caps normal 100% arial !important;
  margin-left: 10px;
  font-size: 13px !important;
}
/* Content Moderator*/
/* CM's with higher ranks are removed
  a[href$="Fewfre"][class^="EntityHeader_name"]:after,
  a[href$="MonkeysHK"][class^="EntityHeader_name"]:after,
*/
a[href$="Lunaynx"][class^="EntityHeader_name"]:after,
a[href$="Voball"][class^="EntityHeader_name"]:after {
  content: "Content Moderator" !important;
  font: small-caps normal 100% arial !important;
  margin-left: 10px;
  font-size: 13px !important;
}
/* Discussions Moderator*/
/* DM's with higher ranks are removed

*/
/*
{
	content: "Discussions Moderator" !important;
	font: small-caps normal 100% arial !important;
	margin-left: 10px;
	font-size: 13px !important;
}
*/
/* Rollback*/
/* RB's with higher ranks are removed

*/
a[href$="Absterge7s"][class^="EntityHeader_name"]:after,
a[href$="CubicC"][class^="EntityHeader_name"]:after,
a[href$="Ikethepro18"][class^="EntityHeader_name"]:after,
a[href$="TDVoldy"][class^="EntityHeader_name"]:after,
a[href$="TheAetherSword"][class^="EntityHeader_name"]:after {
  content: "Rollbacker" !important;
  font: small-caps normal 100% arial !important;
  margin-left: 10px;
  font-size: 13px !important;
}
/* Artist*/
/* ARD's with higher ranks are removed

*/
a[href$="Duowithng"][class^="EntityHeader_name"]:after,
a[href$="Ic22487"][class^="EntityHeader_name"]:after,
a[href$="Volcanofr"][class^="EntityHeader_name"]:after,
a[href$="WaifuWeek"][class^="EntityHeader_name"]:after {
  content: "Artist" !important;
  font: small-caps normal 100% arial !important;
  margin-left: 10px;
  font-size: 13px !important;
}
/* Developer*/
/* DEV's with higher ranks are removed

*/
a[href$="BuggyAl"][class^="EntityHeader_name"]:after,
a[href$="Pigicial"][class^="EntityHeader_name"]:after,
a[href$="Charzard4261"][class^="EntityHeader_name"]:after {
  content: "Developer" !important;
  font: small-caps normal 100% arial !important;
  margin-left: 10px;
  font-size: 13px !important;
}
/*
 * General Fixes - only css that corrects existing class/element types should go here
 * For classes created for this wiki, please use site.less instead
 */
/***** CSS placed here will be applied to all skins on the entire site. *****/
/* Core Layout */
.page-content,
.page-content p {
  line-height: 1.95;
}
.page-header__bottom {
  align-items: flex-end;
}
/* Shrinked NS Prefix for Project Namespace */
.ns-4 .mw-page-title-namespace,
.ns-4 .mw-page-title-separator {
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
.page-content *:not(.toctitle) > h2:not([class]):not(#mw-previewheader),
.page-content h1:not([class]):not(#firstHeading) {
  padding: 4px;
  text-transform: capitalize;
}
.theme-fandomdesktop-light .page-content *:not(.toctitle) > h2:not([class]):not(#mw-previewheader),
.theme-fandomdesktop-light .page-content h1:not([class]):not(#firstHeading) {
  background-color: #e4e4e4;
  background-color: rgba(0, 0, 0, 0.1);
}
.theme-fandomdesktop-dark .page-content *:not(.toctitle) > h2:not([class]):not(#mw-previewheader),
.theme-fandomdesktop-dark .page-content h1:not([class]):not(#firstHeading) {
  background-color: #2d1616;
  background-color: rgba(0, 0, 0, 0.1);
}
.page-content *:not(.toctitle) > h2:not([class]):not(#mw-previewheader) a:not(.mw-editsection a),
.page-content h1:not([class]):not(#firstHeading) a:not(.mw-editsection a) {
  color: inherit;
}
.page-content *:not(.toctitle) > h2:not([class]):not(#mw-previewheader) a:not(.mw-editsection a):hover,
.page-content h1:not([class]):not(#firstHeading) a:not(.mw-editsection a):hover {
  color: var(--theme-link-color--hover);
  text-decoration: none;
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
}
.page-content h3:not([class]) a:not(.mw-editsection a),
.page-content h4:not([class]) a:not(.mw-editsection a),
.page-content h5:not([class]) a:not(.mw-editsection a),
.page-content h6:not([class]) a:not(.mw-editsection a) {
  color: inherit;
}
.page-content h3:not([class]) a:not(.mw-editsection a):hover,
.page-content h4:not([class]) a:not(.mw-editsection a):hover,
.page-content h5:not([class]) a:not(.mw-editsection a):hover,
.page-content h6:not([class]) a:not(.mw-editsection a):hover {
  color: var(--theme-link-color--hover);
  text-decoration: none;
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
@media (hover: none) and (pointer: coarse) {
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
  }
  .theme-fandomdesktop-light abbr[title]:focus::before,
  .theme-fandomdesktop-light span[title]:focus::before {
    background-color: #5f5f5f;
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
.ooui-theme-fandomooui .mw-rcfilters-ui-filterTagMultiselectWidget.oo-ui-widget-enabled .oo-ui-tagMultiselectWidget-handle + .mw-rcfilters-ui-table {
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
.theme-fandomdesktop-light .wikitable tr th {
  background-color: #e6e6e6;
  /* using grayscale */
}
.theme-fandomdesktop-dark .wikitable tr th {
  background-color: #111;
  /* using grayscale */
}
/* Table fixes */
table[align="center"] {
  margin: auto;
}
/* Fix Collapsed table headers */
table.mw-made-collapsible:not(.mw-collapsed) > thead > tr {
  display: table-row;
}
/* Table Highlighting */
/* Highlighting properties for targetted rows */
.page-content .wikitable,
.page-content .article-table {
  /*
	tr:target:not(@{temp}) {
		#tablerowhighlightingstyl.row();
	}
	*/
}
.page-content .wikitable tr:target td:not(.article-row-before td, .article-row-main:target ~ .article-row-main ~ .article-row-bound td, .article-row-before:target ~ .article-row-main ~ .article-row-main td, .article-row-before:target ~ .article-row-main ~ .article-row-main ~ .article-row-bound td),
.page-content .article-table tr:target td:not(.article-row-before td, .article-row-main:target ~ .article-row-main ~ .article-row-bound td, .article-row-before:target ~ .article-row-main ~ .article-row-main td, .article-row-before:target ~ .article-row-main ~ .article-row-main ~ .article-row-bound td),
.page-content .wikitable tr:target th:not(.article-row-before th, .article-row-main:target ~ .article-row-main ~ .article-row-bound th, .article-row-before:target ~ .article-row-main ~ .article-row-main th, .article-row-before:target ~ .article-row-main ~ .article-row-main ~ .article-row-bound th),
.page-content .article-table tr:target th:not(.article-row-before th, .article-row-main:target ~ .article-row-main ~ .article-row-bound th, .article-row-before:target ~ .article-row-main ~ .article-row-main th, .article-row-before:target ~ .article-row-main ~ .article-row-main ~ .article-row-bound th) {
  /*border-color: rgba(204,0,0,0.5);*/
  border-color: #ff6464;
  border-style: solid;
  border-width: unset;
}
.page-content tr.article-row-main:target ~ tr.article-row-bound,
.page-content tr.article-row-before:target ~ tr.article-row-main,
.page-content tr.article-row-before:target ~ tr.article-row-bound {
  /*
	&:not(@{toexcludetr}) {
		#tablerowhighlightingstyl.row();
	}
	*/
}
.page-content tr.article-row-main:target ~ tr.article-row-bound td:not(.article-row-main:target ~ .article-row-main ~ .article-row-bound td, .article-row-before:target ~ .article-row-main ~ .article-row-main td, .article-row-before:target ~ .article-row-main ~ .article-row-main ~ .article-row-bound td),
.page-content tr.article-row-before:target ~ tr.article-row-main td:not(.article-row-main:target ~ .article-row-main ~ .article-row-bound td, .article-row-before:target ~ .article-row-main ~ .article-row-main td, .article-row-before:target ~ .article-row-main ~ .article-row-main ~ .article-row-bound td),
.page-content tr.article-row-before:target ~ tr.article-row-bound td:not(.article-row-main:target ~ .article-row-main ~ .article-row-bound td, .article-row-before:target ~ .article-row-main ~ .article-row-main td, .article-row-before:target ~ .article-row-main ~ .article-row-main ~ .article-row-bound td),
.page-content tr.article-row-main:target ~ tr.article-row-bound th:not(.article-row-main:target ~ .article-row-main ~ .article-row-bound th, .article-row-before:target ~ .article-row-main ~ .article-row-main th, .article-row-before:target ~ .article-row-main ~ .article-row-main ~ .article-row-bound th),
.page-content tr.article-row-before:target ~ tr.article-row-main th:not(.article-row-main:target ~ .article-row-main ~ .article-row-bound th, .article-row-before:target ~ .article-row-main ~ .article-row-main th, .article-row-before:target ~ .article-row-main ~ .article-row-main ~ .article-row-bound th),
.page-content tr.article-row-before:target ~ tr.article-row-bound th:not(.article-row-main:target ~ .article-row-main ~ .article-row-bound th, .article-row-before:target ~ .article-row-main ~ .article-row-main th, .article-row-before:target ~ .article-row-main ~ .article-row-main ~ .article-row-bound th) {
  /*border-color: rgba(204,0,0,0.5);*/
  border-color: #ff6464;
  border-style: solid;
  border-width: unset;
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
}
.theme-fandomdesktop-dark table.mw-abuselog-details {
  background-color: #2f1616 !important;
}
.theme-fandomdesktop-dark table.mw-abuselog-details th {
  background-color: #2e174b !important;
}
/* DIFF styling */
.diff-context {
  border-color: #4d5065 !important;
}
.diff-deletedline .diffchange.diffchange-inline {
  background-color: #a44d4d !important;
}
.theme-fandomdesktop-dark td.diff-deletedline {
  background-color: #4d2626 !important;
}
.diff-deletedline {
  border-color: #b02d2d !important;
}
.theme-fandomdesktop-dark .diffchange {
  background-color: #0f72a7 !important;
}
.diff-addedline {
  border-color: #2a77bd !important;
}
.theme-fandomdesktop-dark .diff-addedline {
  background-color: #24263a !important;
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
.TablePager_col_ipb_params > ul > li:not(:last-child)::after {
  content: ",";
}
.TablePager_col_ipb_params > ul {
  list-style: none !important;
  margin: 0 !important;
}
.TablePager_col_ipb_reason {
  font-style: italic;
}
.TablePager_col_ipb_reason::before {
  content: "(";
}
.TablePager_col_ipb_reason::after {
  content: ")";
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
.pi-smart-group-head + .pi-smart-group-body {
  border-top: none;
}
.pi-data-value ul li:before {
  color: white;
}
.pi-data-value {
  width: 100%;
}
/* TOC tweaks - styling used is partially from: runescape.wiki */
#toc,
.toc {
  border: none;
  border-left: 1px solid #555;
  padding-left: 8px;
}
#toc ul ul,
.toc ul ul {
  padding-left: 0.5em;
  border-left: 1px dotted var(--theme-border-color);
}
.mw-content-ltr .toc ul ul,
.mw-content-rtl .mw-content-ltr .toc ul ul {
  margin: 0 0 0 2em;
}
#toc .toctogglelabel,
.toc .toctogglelabel {
  color: var(--theme-page-text-color);
}
#toc .toctitle,
.toc .toctitle {
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
  .tocright .toc,
  .tocright #toc {
    margin: 0 0 0.5em 0.5em;
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
#less-content > p {
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
.mw-highlight.mw-content-ltr,
.dark-code-box {
  background-color: #272727 !important;
  border-radius: 6px;
  border: 0;
}
.theme-fandomdesktop-light .mw-highlight.mw-content-ltr,
.theme-fandomdesktop-light .dark-code-box {
  background-color: #cbcbcb !important;
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
  display: none;
  /* hiding it as it currently serves no purpose */
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
}
.theme-fandomdesktop-light #userProfileApp .user-identity-header__tag {
  background-color: #ddd;
}
.theme-fandomdesktop-dark #userProfileApp .user-identity-header__tag {
  background-color: #301212;
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
  transition: margin 0.2s;
}
body.page-Special_ApiHelp h1,
body.page-Special_ApiHelp h2,
body.page-Special_ApiHelp h3,
body.page-Special_ApiHelp h4,
body.page-Special_ApiHelp h5,
body.page-Special_ApiHelp h6 {
  color: white;
}
body.page-Special_ApiHelp a {
  color: #fec356;
}
body.page-Special_ApiHelp .api-pretty-header {
  font-size: 14px;
  font-family: rubik, helvetica, arial, sans-serif;
}
body.page-Special_ApiHelp .mw-highlight {
  background-color: #272727 !important;
  border-radius: 6px;
  border: 0;
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
  padding: 0.5em;
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
  letter-spacing: 0.25px;
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
.page-header__actions > .wds-button,
.page-header__actions > .wds-dropdown {
  color: var(--theme-accent-label-color);
  background-color: var(--theme-accent-color);
  margin-right: 10px;
  transition: all 0.2s ease-in;
}
.page-header__actions > .wds-button:hover,
.page-header__actions > .wds-dropdown:hover {
  background-color: var(--theme-accent-color--hover);
  transition: all 0.2s ease-out;
  color: var(--theme-accent-label-color);
}
.page-header__actions > .wds-dropdown {
  border-radius: 30px;
}
.page-header__actions > .wds-button {
  left: -5px;
}
.page-header__actions > .wds-dropdown > div::before {
  left: -10px;
  margin-right: 10px;
}
.mw-history-subtitle {
  display: inline-block;
}
.page-header__actions .wds-dropdown > .page-header__action-button {
  color: var(--theme-accent-label-color);
  cursor: pointer;
}
/* Also fix article comments button */
#article-comments-button {
  background-color: var(--theme-accent-label-color);
  color: var(--theme-link-label-color);
}
/* Page Action buttons fix */
a.page-header__action-button:first-of-type + a#ca-edit::before {
  left: -8px;
}
a.page-header__action-button:first-of-type + a#ca-edit {
  margin-left: 6px;
}
/* Fix ugly history selection colors */
#pagehistory li {
  border: 0 !important;
}
#pagehistory > li.selected {
  background-color: var(--theme-page-background-color--secondary);
  border: 1px dashed var(--theme-border-color) !important;
  color: inherit !important;
  padding: 1px 0px;
}
/* Fix page subtitle going on new lines */
.page-header__subtitle > div.mw-history-subtitle {
  display: inline !important;
}
/* Disable category dropdown */
.wds-collapsible-panel.page-footer__categories > header {
  display: none !important;
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
.page-footer__categories > div {
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
.mw-changeslist-links > span:not(:first-child):before {
  color: inherit !important;
}
/* Fix positioning and arrow of "My Tools" */
#WikiaBarWrapper .mytools.menu:not(:hover) > svg {
  transform: rotate(180deg);
  transition: 0.25s all ease;
}
#WikiaBarWrapper .mytools.menu:hover > svg {
  transition: 0.25s all ease;
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
.wds-tabber,
.partialLoad-tabber {
  background-color: var(--theme-page-background-color);
  /*border: 1px solid rgba(254, 195, 86, 0.75);*/
  border: 1px solid rgba(var(--theme-link-color--rgb),0.75);
  border-radius: 3px;
}
.wds-tabs__tab,
.partialLoad-tabs__tab {
  border: 1px solid transparent;
  text-decoration: none;
}
.wds-tabs__tab:hover .wds-tabs__tab-label:not(.wds-tabs__tab.wds-is-current .wds-tabs__tab-label),
.wds-tabs__tab:hover a:not(.wds-tabs__tab.wds-is-current a) {
  color: var(--wds-tab-color--hover);
  box-shadow: inset 0 -3px 0 -1px var(--theme-link-color);
}
.partialLoad-tabs__tab:hover .partialLoad-tabs__label:not(.partialLoad-tabs__tab.select .partialLoad-tabs__label),
.partialLoad-tabs__tab:hover a:not(.partialLoad-tabs__tab.select a) {
  color: var(--wds-tab-color--hover);
  box-shadow: inset 0 -3px 0 -1px var(--theme-link-color);
}
.wds-tabs__tab .wds-tabs__tab-label,
.partialLoad-tabs__tab .partialLoad-tabs__label {
  box-shadow: inset 0 -3px 0 -1px transparent;
  transition: all 0.2s;
}
.wds-tabs__tab .wds-tabs__tab-label a,
.partialLoad-tabs__tab .partialLoad-tabs__label a {
  transition: all 0.2s;
}
.wds-tabs__tab .wds-tabs__tab-label a:focus,
.partialLoad-tabs__tab .partialLoad-tabs__label a:focus {
  color: inherit;
}
.wds-tabs__tab .wds-tabs__tab-label a:hover:not(.wds-tabs__tab.wds-is-current .wds-tabs__tab-label, .wds-tabs__tab.wds-is-current a),
.wds-tabs__tab .wds-tabs__tab-label a:active:not(.wds-tabs__tab.wds-is-current .wds-tabs__tab-label, .wds-tabs__tab.wds-is-current a),
.wds-tabs__tab .wds-tabs__tab-label a:focus-visible:not(.wds-tabs__tab.wds-is-current .wds-tabs__tab-label, .wds-tabs__tab.wds-is-current a),
.wds-tabs__tab .wds-tabs__tab-label:hover:not(.wds-tabs__tab.wds-is-current .wds-tabs__tab-label, .wds-tabs__tab.wds-is-current a),
.wds-tabs__tab .wds-tabs__tab-label:active:not(.wds-tabs__tab.wds-is-current .wds-tabs__tab-label, .wds-tabs__tab.wds-is-current a),
.wds-tabs__tab .wds-tabs__tab-label:focus-visible:not(.wds-tabs__tab.wds-is-current .wds-tabs__tab-label, .wds-tabs__tab.wds-is-current a) {
  color: var(--wds-tab-color--hover);
  box-shadow: inset 0 -3px 0 -1px var(--theme-link-color);
}
.partialLoad-tabs__tab .partialLoad-tabs__label a:hover:not(.partialLoad-tabs__tab.selected .partialLoad-tabs__label, .partialLoad-tabs__tab.selected a),
.partialLoad-tabs__tab .partialLoad-tabs__label a:active:not(.partialLoad-tabs__tab.selected .partialLoad-tabs__label, .partialLoad-tabs__tab.selected a),
.partialLoad-tabs__tab .partialLoad-tabs__label a:focus-visible:not(.partialLoad-tabs__tab.selected .partialLoad-tabs__label, .partialLoad-tabs__tab.selected a),
.partialLoad-tabs__tab .partialLoad-tabs__label:hover:not(.partialLoad-tabs__tab.selected .partialLoad-tabs__label, .partialLoad-tabs__tab.selected a),
.partialLoad-tabs__tab .partialLoad-tabs__label:active:not(.partialLoad-tabs__tab.selected .partialLoad-tabs__label, .partialLoad-tabs__tab.selected a),
.partialLoad-tabs__tab .partialLoad-tabs__label:focus-visible:not(.partialLoad-tabs__tab.selected .partialLoad-tabs__label, .partialLoad-tabs__tab.selected a) {
  color: var(--wds-tab-color--hover);
  box-shadow: inset 0 -3px 0 -1px var(--theme-link-color);
}
.wds-tabs__tab.wds-is-current,
.partialLoad-tabs__tab.selected {
  /*border: 1px solid rgba(254, 195, 86, 0.4);*/
  border: 1px solid rgba(var(--theme-link-color--rgb),0.4);
  border-top: none;
  /*background: rgba(254, 195, 86, 0.1);*/
  background-color: rgba(var(--theme-link-color--rgb),0.1);
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
/*
 * Localization for other language wikis
 * on [[MediaWiki:Custom-common.less/language-local.less]]
 */
/* Language Wiki Specific Styling and Overrides - Applies to the Whole Site */
/* Individual User Stylings */
/* Note: Also see automatic generation on staff-colors.less */
/* Current Wiki Representitive */
a[href$="OishiiOnIno"] {
  color: var(--custom-rolecolor-wiki-representative) !important;
}
/* Former Wiki Representitive */
a[href$="Sitb"] {
  color: var(--custom-rolecolor-wiki-representative) !important;
}
/* Abuse Filter */
a[href$="Abuse_filter"] {
  color: var(--custom-rolecolor-abusefilter) !important;
}
a[href$="Abuse_filter"]::before {
  display: none !important;
}
/* For April Fools only */
/*
.fandom-community-header__image,
.fandom-sticky-header__logo {
	transform: rotateX(180deg);
}
@media only screen and (max-width: 1279px) {
	.fandom-community-header__image img {
		object-position: 0 -10px;
	}
}
.fandom-community-header__community-name,
.fandom-sticky-header__sitename {
	visibility: hidden;
	position: relative;
}
.fandom-community-header__community-name {
	width: 350px;
}
.fandom-sticky-header__sitename {
	width: 230px;
}
.fandom-community-header__community-name::after,
.fandom-sticky-header__sitename::after {
	content: "Lowpixel GroundBlock Wiki";
	visibility: visible;
	display: block;
	position: absolute;
	top: 0;
	white-space: nowrap;
}
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href*="/wiki/User:"]:not([role]):not(.extiw):not(.external)::before
{
	content: " ";
	background: url(https://static.wikia.nocookie.net/hypixel-skyblock/images/3/3e/Jerry_Sprite.png/revision/latest) no-repeat center;
	padding: 0 8px;
	margin-right: 2px;
	background-size: 16px 16px;
}
*/

/* Added from Gadget-PartialLoadTool.css */
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
/* CSS for Seria Wiki Infoboxes */
.pi-theme-seria .pi-data-value {
    text-align: center;
}
.pi-theme-seria .pi-data-label {
    text-align: center;
}
.pi-theme-seria .pi-header {
    text-align: center;
}

/* Currency Colors */
.pi-theme-seria [data-source="sell"] .pi-data-value,
.pi-theme-seria [data-source="buy"] .pi-data-value {
    color: #FFAA00;
    font-weight: bold;
}
.pi-theme-seria [data-source="sell_shard"] .pi-data-value,
.pi-theme-seria [data-source="buy_shard"] .pi-data-value {
    color: #A303F9;
    font-weight: bold;
}
.pi-theme-seria [data-source="sell_serium"] .pi-data-value,
.pi-theme-seria [data-source="buy_serium"] .pi-data-value {
    color: #fb4040;
    font-weight: bold;
}

/* Ensure hyperlinks inherit currency colors */
.pi-theme-seria [data-source="sell"] .pi-data-value a,
.pi-theme-seria [data-source="buy"] .pi-data-value a,
.pi-theme-seria [data-source="sell_shard"] .pi-data-value a,
.pi-theme-seria [data-source="buy_shard"] .pi-data-value a,
.pi-theme-seria [data-source="sell_serium"] .pi-data-value a,
.pi-theme-seria [data-source="buy_serium"] .pi-data-value a {
    color: inherit;
    text-decoration: none;
}
.pi-theme-seria [data-source="sell"] .pi-data-value a:hover,
.pi-theme-seria [data-source="buy"] .pi-data-value a:hover,
.pi-theme-seria [data-source="sell_shard"] .pi-data-value a:hover,
.pi-theme-seria [data-source="buy_shard"] .pi-data-value a:hover,
.pi-theme-seria [data-source="sell_serium"] .pi-data-value a:hover,
.pi-theme-seria [data-source="buy_serium"] .pi-data-value a:hover {
    text-decoration: underline;
}

/* Crafting Table Styles */
.mc-crafting-table { display: inline-flex; align-items: center; background-color: #c6c6c6; border: 2px solid #555; padding: 10px; border-radius: 4px; margin: 10px 0; }
.mc-crafting-table.enchanted { background-color: #8b8b8b; border-color: #880088; box-shadow: 0 0 12px #ff55ff; }
.mc-crafting-grid { display: grid; grid-template-columns: repeat(3, 36px); grid-template-rows: repeat(3, 36px); gap: 2px; }
.mc-slot { width: 36px; height: 36px; background-color: #8b8b8b; border: 2px solid #373737; border-top-color: #fff; border-left-color: #fff; display: flex; justify-content: center; align-items: center; }
.mc-crafting-table.enchanted .mc-slot { background-color: #8b8b8b; border-color: #883388; border-top-color: #ff77ff; border-left-color: #ff77ff; }
.mc-crafting-arrow { font-size: 24px; margin: 0 15px; color: #555; }
.mc-crafting-table.enchanted .mc-crafting-arrow { color: #ff77ff; text-shadow: 0 0 5px #ff77ff; }
.output-slot { width: 54px; height: 54px; }
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
@upstream: "https://hypixel-skyblock.fandom.com/wiki/MediaWiki:Custom-common.less";
@lang: ""; /* note: this variable is automatically updated when using Less Source Updater */
@local: "@{lang}/MediaWiki:Custom-common.less";

/* Custom Fonts */
@import "@{local}/fonts.less";

/* Variables */
@import "@{local}/variables.less";

/* Role Styling */
@import "@{local}/roles.less";

/* Template Styling */
@import "@{local}/navbox.less";
@import "@{local}/minecraft.less";
@import "@{local}/buttons.less";

/* Page Specific Styling */
@import "@{local}/mainpage.less";

/* Site features styling */
@import "@{local}/site.less";
@import "@{local}/containers.less";
@import "@{local}/color.less";

/* Editor Styling */
@import "@{local}/AceEditor.less";
@import "@{local}/CodeHighlight.less";

/* Used by Module:Minimap */
@import "@{local}/minimap.less";

/* Local Scripts - Imported on this wiki locally */
/* Staff Colors (Updated via a script at [[MediaWiki:Gadget-StaffColorsUpdater.js]]) */
@import "@{local}/staff-colors.less";


/*
 * General Fixes - only css that corrects existing class/element types should go here
 * For classes created for this wiki, please use site.less instead
 */
@import "@{local}/general.less";
@import "@{local}/ucx.less";
/*
 * Localization for other language wikis
 * on [[MediaWiki:Custom-common.less/language-local.less]]
 */
@import "@{local}/language-local.less";
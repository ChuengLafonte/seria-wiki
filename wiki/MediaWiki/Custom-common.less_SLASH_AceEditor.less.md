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
	border: 1px solid rgb(66, 60, 60);
	background-color:#074252ba !important
}

.ace-tm .ace_marker-layer .ace_selected-word {
	border: 1px solid rgba(98, 88, 88, 0.64);
	border-radius: 4px;
	background-color:#07425269 !important
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

span.ace_identifier:not(.ace_declaration), div.ace_scroller {
	color: #93a1a1;
}

.editor.ace_editor.ace-tm {
	line-height: 18px !important;
}

.ace_scrollbar.ace_scrollbar-h {
	display: normal !important;
}
.ace-tm .ace_marker-layer .ace_selection {
	background: rgba(255,255,255,0.1) !important;
}
.ace-tm .ace_marker-layer .ace_selected-word {
	background-color: unset !important;
	border: rgba(0,0,0,0.4) !important;
}

/*
//#============================================================================#
// CONSOLE
//#============================================================================#
*/
/* General Setting */
.mw-editform #mw-scribunto-console .mw-scribunto-console-fieldset {
	background: #000;
	background: rgba(0,0,0,0.4);
	margin: 0;
}
.mw-editform #mw-scribunto-console .mw-scribunto-console-fieldset legend {
	background: var(--theme-page-background-color);
	border-radius: 5px;
	box-shadow: inset -2px -3px var(--theme-accent-color);
	padding: .2em 1em;
	margin-bottom: .6em;
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

span.ace_boolean, span.ace_constant:not(.ace_numeric) {
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

.ace_method, .ace_variable:not(.ace_language) {
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
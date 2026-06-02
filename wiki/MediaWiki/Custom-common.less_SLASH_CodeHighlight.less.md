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
.mw-highlight .mf{
	color: #D33682 !important
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
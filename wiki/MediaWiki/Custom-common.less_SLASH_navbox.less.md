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
	
	--navbox-title-background: #555; /* using grayscale */
	
	--navbox-header-background: var(--theme-page-background-color--secondary); /* using grayscale */
	--navbox-header-link-color: #222;
	--navbox-header-color: #000;
	
	--navbox-list-background: white;
}
.navbox .navbox-header a, .navbox .navbox-group a, .navbox .mw-collapsible-toggle a:hover {
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
.navbox .navbox-above, .navbox .navbox-below, .navbox .navbox-image {
	 color: var(--theme-page-text-color);
	 background: var(--navbox-header-background);
	 text-align: center;
}
.navbox .navbox-group, .navbox .navbox-header {
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
.navbox .navbox-group, .navbox .navbox-image-left {
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
.hlist li, .hlist ul ul {
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
.hlist li:last-child:after, .hlist ul ul li:last-child:after {
	 content: none;
}
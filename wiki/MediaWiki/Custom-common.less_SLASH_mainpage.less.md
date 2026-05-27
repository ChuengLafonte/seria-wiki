/****************************
 * General
 ****************************/
/* Effects widgets on the front page / templates that use this class. */
.widget-title, .widget-subtitle {
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
	h2 {
		font-size: 21px;
	}
}
.widget-subtitle {
	margin: 0 auto 10px auto;
	padding: 7px 4px;
	border: 1px solid var(--theme-border-color);
	font-size: 17px;
	width: 90%;
	h3 {
		font-size: 17px;
	}
}
.color1 {
	background: var(--theme-accent-color);
	color: var(--theme-accent-label-color);
}
.color2 {
	background: #AA4A98;
	color: #fff;
	.theme-fandomdesktop-light & {
		background: #E88CD7;
		color: #111;
		a {
			color: white;
		}
	}
}
.color3 {
	background: #cc9933;
	color: #fff;
	.theme-fandomdesktop-light & {
		background: #ecc881;
		color: #111;
		a {
			color: white;
		}
	}
}

/****************************
 * Project:Poll
 ****************************/
/* Changes the color of the bars on polls to fit wiki colors. */
.pollAnswerVotes {
	color:#DDD; background:darken(@theme-page, 15%);
}
.pollAnswerVotes div {
	#gradient.horizontal(@theme-buttons, lighten(@theme-buttons, 15%)) !important;
}

/****************************
 * Project:News/article
 ****************************/
.newsarticle-heading {
	border-bottom:1px solid #b2af9c;
}
.newsarticle-new {
	color:white;
	background:red;
	padding:1px 3px;
	border-radius:5px;
	border:2px dotted darkred;
}
.newsarticle-date {
	float:right;
}
.newsarticle-content {
	padding:0 5px 0 25px;
	margin:3px 0 8px 0;
	background:darken(@theme-page, 2%);
	border:1px solid darken(@theme-page, 15%);
	&:after {
		content: "";
		display:block;
		clear:both;
	}
}
.newsarticle-links {
	float:right;
	border: 1px solid darken(@theme-page, 15%);
	line-height: 1;
	padding: 2px 2px 1px 2px;
	border-radius: 2px;
	background: rgba(0,0,0,0.01);
}
.newsarticle-links:empty {
	display: none;
}

/* Fandomdesktop weirdness*/
p + .darkTable-wrapper, p + .darkTable {
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
	background-color: ~"rgba(var(--theme-link-color--rgb),0.1)";
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
	.theme-fandomdesktop-light & {
		background-color: rgba(0, 0, 0, 0.07);
		box-shadow: rgba(0, 0, 0, 0.2) 0 -5px 0px 0px inset;
	}
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
	.theme-fandomdesktop-light & {
		box-shadow: rgba(0, 0, 0, 0.6) 0px 0px 2px 1px inset;
	}
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
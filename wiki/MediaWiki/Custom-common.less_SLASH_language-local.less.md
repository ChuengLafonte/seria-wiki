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
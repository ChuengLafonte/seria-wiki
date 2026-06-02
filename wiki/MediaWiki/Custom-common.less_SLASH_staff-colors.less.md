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
a[href$="ScoutskylarBot"]:not([href*="auth.fandom.com/"])
{
	color: var(--custom-rolecolor-bot) !important;
}

/* Bureaucrat*/
/* BU's with higher ranks are removed
  a[href$="Hypixel_SkyBlock_Wiki_Bot"]:not([href*="auth.fandom.com/"]),
  a[href$="Hypixel SkyBlock Wiki Bot"]:not([href*="auth.fandom.com/"]),
*/
a[href$="Scoutskylar"]:not([href*="auth.fandom.com/"])
{
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
a[href$="TheTrueShaman"]:not([href*="auth.fandom.com/"])
{
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
a[href$="MonkeysHK"]:not([href*="auth.fandom.com/"])
{
	color: var(--custom-rolecolor-codeeditor) !important;
}

/* Content Moderator*/
/* CM's with higher ranks are removed
  a[href$="Fewfre"]:not([href*="auth.fandom.com/"]),
  a[href$="MonkeysHK"]:not([href*="auth.fandom.com/"]),
*/
a[href$="Lunaynx"]:not([href*="auth.fandom.com/"]),
a[href$="Voball"]:not([href*="auth.fandom.com/"])
{
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
a[href$="TheAetherSword"]:not([href*="auth.fandom.com/"])
{
	color: var(--custom-rolecolor-rollback) !important;
}

/* Artist*/
/* ARD's with higher ranks are removed

*/
a[href$="Duowithng"]:not([href*="auth.fandom.com/"]), /* This selector is an override */
a[href$="Ic22487"]:not([href*="auth.fandom.com/"]), /* This selector is an override */
a[href$="Volcanofr"]:not([href*="auth.fandom.com/"]), /* This selector is an override */
a[href$="WaifuWeek"]:not([href*="auth.fandom.com/"]) /* This selector is an override */
{
	color: var(--custom-rolecolor-ard) !important;
}

/* Developer*/
/* DEV's with higher ranks are removed

*/
a[href$="BuggyAl"]:not([href*="auth.fandom.com/"]), /* This selector is an override */
a[href$="Pigicial"]:not([href*="auth.fandom.com/"]), /* This selector is an override */
a[href$="Charzard4261"]:not([href*="auth.fandom.com/"]) /* This selector is an override */
{
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
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:Abuse Filter"]:not([role]):not(.extiw):not(.external)::before /* This selector is an override */
{
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
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:Scoutskylar"]:not([role]):not(.extiw):not(.external)::before
{
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
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:TheTrueShaman"]:not([role]):not(.extiw):not(.external)::before
{
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
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:MonkeysHK"]:not([role]):not(.extiw):not(.external)::before
{
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
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:Voball"]:not([role]):not(.extiw):not(.external)::before
{
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
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:TheAetherSword"]:not([role]):not(.extiw):not(.external)::before
{
	content: " ";
	background: var(--custom-rolebadge-rollback) no-repeat center;
	padding: 0 8px;
	margin-right: 2px;
	background-size: 16px 16px;
}

/* Artist*/
/* ARD's with higher ranks are removed

*/
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:Duowithng"]:not([role]):not(.extiw):not(.external)::before, /* This selector is an override */
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:Ic22487"]:not([role]):not(.extiw):not(.external)::before, /* This selector is an override */
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:Volcanofr"]:not([role]):not(.extiw):not(.external)::before, /* This selector is an override */
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:WaifuWeek"]:not([role]):not(.extiw):not(.external)::before /* This selector is an override */
{
	content: " ";
	background: var(--custom-rolebadge-ard) no-repeat center;
	padding: 0 8px;
	margin-right: 2px;
	background-size: 16px 16px;
}

/* Developer*/
/* DEV's with higher ranks are removed

*/
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:BuggyAl"]:not([role]):not(.extiw):not(.external)::before, /* This selector is an override */
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:Pigicial"]:not([role]):not(.extiw):not(.external)::before, /* This selector is an override */
*:not(.wds-avatar):not(.category-page__member-left):not(.page-header__subtitle-blog-post) > a[href$="/wiki/User:Charzard4261"]:not([role]):not(.extiw):not(.external)::before /* This selector is an override */
{
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
a[href$="Abuse Filter"][class^="EntityHeader_name"]:after /* This selector is an override */
{
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
a[href$="Scoutskylar"][class^="EntityHeader_name"]:after
{
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
a[href$="TheTrueShaman"][class^="EntityHeader_name"]:after
{
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
a[href$="MonkeysHK"][class^="EntityHeader_name"]:after
{
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
a[href$="Voball"][class^="EntityHeader_name"]:after
{
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
a[href$="TheAetherSword"][class^="EntityHeader_name"]:after
{
	content: "Rollbacker" !important;
	font: small-caps normal 100% arial !important;
	margin-left: 10px;
	font-size: 13px !important;
}

/* Artist*/
/* ARD's with higher ranks are removed

*/
a[href$="Duowithng"][class^="EntityHeader_name"]:after, /* This selector is an override */
a[href$="Ic22487"][class^="EntityHeader_name"]:after, /* This selector is an override */
a[href$="Volcanofr"][class^="EntityHeader_name"]:after, /* This selector is an override */
a[href$="WaifuWeek"][class^="EntityHeader_name"]:after /* This selector is an override */
{
	content: "Artist" !important;
	font: small-caps normal 100% arial !important;
	margin-left: 10px;
	font-size: 13px !important;
}

/* Developer*/
/* DEV's with higher ranks are removed

*/
a[href$="BuggyAl"][class^="EntityHeader_name"]:after, /* This selector is an override */
a[href$="Pigicial"][class^="EntityHeader_name"]:after, /* This selector is an override */
a[href$="Charzard4261"][class^="EntityHeader_name"]:after /* This selector is an override */
{
	content: "Developer" !important;
	font: small-caps normal 100% arial !important;
	margin-left: 10px;
	font-size: 13px !important;
}
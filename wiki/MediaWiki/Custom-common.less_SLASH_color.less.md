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
.light-color, .color-aqua, .color-green, .color-yellow, .color-white {
	.theme-fandomdesktop-light & {
		filter: brightness(70%);
	}
}
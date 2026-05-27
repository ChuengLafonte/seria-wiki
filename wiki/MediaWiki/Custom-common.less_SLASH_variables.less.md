/* Custom CSS variables for this wiki */


/* Theme Style Overrides - Use according to what you need for a certain theme */
.theme-fandomdesktop-dark {
	--theme-link-label-color: #fff;
	--theme-link-decoration: none; /* may delete if Fandom fixed it */
}
.theme-fandomdesktop-light {
	
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
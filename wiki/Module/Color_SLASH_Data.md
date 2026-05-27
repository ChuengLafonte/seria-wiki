-- <pre>
-- Tooltips colors are not defined here. Please check [[Module:UIText/Data]].

local colorClasses = {
	--Minecraft Vanilla
	['black'] = 'color-black',
	['dark_blue'] = 'color-dark_blue',
	['dark_green'] = 'color-dark_green',
	['dark_aqua'] = 'color-dark_aqua',
	['dark_red'] = 'color-dark_red',
	['dark_purple'] = 'color-dark_purple',
	['gold'] = 'color-gold',
	['gray'] = 'color-gray',
	['dark_gray'] = 'color-dark_gray',
	['blue'] = 'color-blue',
	['green'] = 'color-green',
	['aqua'] = 'color-aqua',
	['red'] = 'color-red',
	['light_purple'] = 'color-light_purple',
	['yellow'] = 'color-yellow',
	['white'] = 'color-white',
}

local hexColors = {
	--Minecraft Vanilla
	['black'] = '#000000',
	['dark_blue'] = '#0000AA',
	['dark_green'] = '#00AA00',
	['dark_aqua'] = '#00AAAA',
	['dark_red'] = '#AA0000',
	['dark_purple'] = '#AA00AA',
	['gold'] = '#FFAA00',
	['gray'] = '#AAAAAA',
	['dark_gray'] = '#555555',
	['blue'] = '#5555FF',
	['green'] = '#55FF55',
	['aqua'] = '#55FFFF',
	['red'] = '#FF5555',
	['light_purple'] = '#FF55FF',
	['yellow'] = '#FFFF55',
	['white'] = '#FFFFFF',
	--Wiki Custom
	['silver'] = '#C0C0C0',
	['turquoise'] = '#00AAAA',
	['bronze'] = '#803600',
	['orange'] = '#FF921E',
	['pink'] = '#FF55FF',
}

local shadowColors = {
	['cyan'] = true,
	['aqua'] = true,
	['green'] = true,
	['yellow'] = true,
	['orange'] = true,
	['white'] = true,
	['#fcffbd'] = true,
	['#eeeeee'] = true,
}

local MCColors = {
	--[[
	In Minecraft Namespace ID order
		For copying:
	'White','Orange','Magenta','Light Blue','Yellow','Lime','Pink','Gray','Light Gray','Cyan','Purple','Blue','Brown','Green','Red','Black',
	--]]
	'White',
	'Orange',
	'Magenta',
	'Light Blue',  
	'Yellow',
	'Lime',
	'Pink',
	'Gray',
	'Light Gray', 
	'Cyan',
	'Purple',
	'Blue',
	'Brown',
	'Green',
	'Red',
	'Black',
}

return {
	colorClasses = colorClasses,
	hexColors = hexColors,
	shadowColors = shadowColors,
	hexLightModeColors = hexLightModeColors,
	MCColors = MCColors,
}
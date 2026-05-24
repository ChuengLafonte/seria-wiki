-- Please make use of get functions from Module:UIText to get this page's data.
-- For rarity/stat colors/characters, please use get functions from Module:RarityTier and Module:Statname

local conversions = {
	black = '0',
	dark_blue = '1',
	dark_green = '2',
	dark_aqua = '3',
	dark_red = '4',
	dark_purple = '5',
	gold = '6',
	gray = '7',
	dark_gray = '8',
	blue = '9',
	green = 'a',
	aqua = 'b',
	red = 'c',
	light_purple = 'd',
	pink = 'd',
	yellow = 'e',
	white = 'f',
	-- Non-color formatting
	bold = 'l',
	underline = 'n',
	strikethrough = 'm',
	italic = 'o',
	reset = 'r',
}

local custom = {}

return {
	conversions = conversions,
	custom = custom,
}

local statName = require('Module:Statname').getStatName
local string = require('Module:String')
local statData = mw.loadData('Module:Statname/Data')

return function(item, noStatsValue)
	local t = {}
	
	local statFormat1 = '<li>%s: %s</li>'
	local statFormat2 = '<li>%s: %s&#32;(%s)</li>'
	local function parseStat(val, stat, percent)
		if not val or val == '' then return end
		percent = percent and '%' or ''
		
		if type(val) == 'number' and val > 0 then
			 t[#t+1] = string.format('<li>%s: +%s</li>', statName{stat}, val..percent)
			
		elseif type(val) ~= "table" and string.match(val, '^([^%D]+)$') and not val[2] then
			 t[#t+1] = string.format('<li>%s: %s</li>', statName{stat}, val..percent)
			
		elseif type(val) == 'table' and string.match(val[1] or '', '^([^%D]+)$') then
			 t[#t+1] = string.format('<li>%s: +%s&#32;(%s)</li>', statName{stat}, val[1]..percent, val[2])
				
		elseif type(val) == "table" and val.lower then
			t[#t+1] = string.format('<li>%s: %s-%s</li>', statName{stat}, (val.lower > 0 and '+' or '')..val.lower..percent, val.upper..percent)
			
		elseif type(val) == "table" and type(val[2]) ~= "string" then
			 t[#t+1] = string.format('<li>%s: %s&#32;(%s)</li>', statName{stat}, val[1]..percent, val[2])
			
		elseif tostring(val):match('([%+%-]?)(%d+)%-(%d+)') then
			t[#t+1] = string.format('<li>%s: %s%s</li>', statName{stat}, not val:match('^[%-%+]') and '+' or '', val:gsub('%%$', '')..percent)
		else
			t[#t+1] = string.format('<li>%s: %s</li>', statName{stat}, val..percent)
		end
	end
	
	for k,v in pairs(statData) do
		parseStat(item[v.shortcode], v.shortcode, v.percent)
	end
	
	if #t == 0 then return noStatsValue end
	return string.wrapHtml{ 
		t,
		'<ul>', {
			style="list-style-type:square;";
		}
	}
end
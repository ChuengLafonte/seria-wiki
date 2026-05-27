-- <pre>
--NOTE: For Tooltip Colors, please use Module:UIText

local p = {}

local getArgs = require('Module:Arguments').getArgs
local string = require('Module:String')
local table = require('Module:Table')
local yesno = require('Module:Yesno')
local libU = require('Module:LibU')

local aliases = mw.loadData('Module:Color/Aliases')
local colorData = mw.loadData('Module:Color/Data')

-----------------------------------------------------------------------------
-- Category:Single Color templates
--
-- Changes text color to a fixed color
-- Aliases: p.makeColor, p.colorText, p.wrapColor, p.ct
-----------------------------------------------------------------------------
function p.colorTemplates(frame)
	local args = getArgs(frame)
	local text = args[1] or ''
	local color = args['color']
	return string.pcall(p._colorTemplates, color, text)
end
-- p._colorTemplates(color : string/number/table, text : string/number/table)
function p._colorTemplates(color, text)
	if type(color) == 'table' and #color >= 3 then
		color = table.concat{ #color == 3 and 'rgb(' or 'rgba(', table.concat(color, ', ') , ')' }
	end
	
	local colorID = string.gsub(aliases[string.lower(color)] or string.lower(color), ' ', '_');
	local lightcolor = not not colorData.shadowColors[colorID]
	local colorClass = colorData.colorClasses[colorID]
	local colorHex = colorData.hexColors[colorID] or color
	
	local appliedClass = (lightcolor and 'light-color ' or '') .. (colorClass or '')
	local appliedStyle = colorClass and '' or 'color:' .. tostring(colorHex)
	return string.wrapHtml(type(text) == 'table' and table.concat(text, text.seperator or text.sep or text.s or '') or text, 'span', {
		class = appliedClass ~= '' and appliedClass or nil,
		style = appliedStyle ~= '' and appliedStyle or nil,
	})
end
p.makeColor = p._colorTemplates
p.colorText = p._colorTemplates
p.wrapColor = p._colorTemplates
p.ct = p._colorTemplates

---------------------------------------------------------------------------------
-- p.getColor(color?: string | table<number>) 
---------------------------------------------------------------------------------
function p.getColor(color)
	if type(color) == 'table' and #color >= 3 then
		color = table.concat{ #color == 3 and 'rgb(' or 'rgba(', table.concat(color, ', ') , ')' }
	end
	return colorData.hexColors[string.gsub(aliases[string.lower(color)] or string.lower(color), ' ', '_')] or nil
end

-----------------------------------------------------------------------------
-- Template:Color Conversion
--
-- Converts input between different coding techniques
-- Can also be used in modules
-----------------------------------------------------------------------------
function p.color_conversion(frame)
	local args = getArgs(frame)
	local output_type = args[1]
	local color = args[2]
	return mw.getCurrentFrame():preprocess(string.pcall(p._color_conversion, output_type, color, true))
end

function p._color_conversion(output_type, color, on_page)
	--Local variables
	local color_output = ''
	local color_digit = ''
	-- Categorization based on output_type
	-- Hex
	if string.lower(output_type) == 'hex' then
		local letters = { [10] = 'A', [11] = 'B', [12] = 'C', [13] = 'D', [14] = 'E', [15] = 'F' }
		-- Delete everything except numbers and commas
		color = string.gsub(color, 'rgba?%((.*)%)', '%1')
		-- Split the numbers apart
		color = mw.text.split( color, '%s*,%s*')
		-- Check if input is valid
		if tonumber(color[1]) < 0 or tonumber(color[1]) > 255 or tonumber(color[2]) < 0 or tonumber(color[2]) > 255 or tonumber(color[3]) < 0 or tonumber(color[3]) > 255 then
			color_output = string.error('color was invalid \"rgb(%q, %q, %q)', color[1], color[2], color[3])
		else
			for i = 3, 1, -1 do
				-- Repeat this for all 3 numbers
				for j = 1, 2, 1 do
					-- Repeat this 2 times for every number
					color_digit = color[i] % 16
					color_digit = letters[color_digit] or color_digit
					color[i] = math.floor(color[i] / 16)
					color_output = color_digit .. color_output
				end
			end
			-- Add # to the front
			if on_page then
				color_output = mw.text.nowiki('#') .. color_output
			else color_output = '#' .. color_output
			end
		end
	-- RGB
	elseif string.match(string.lower(output_type), 'rgba?') then
		local letters = { ['A'] = 10, ['B'] = 11, ['C'] = 12, ['D'] = 13, ['E'] = 14, ['F'] = 15 }
		-- Set color_output to base value
		if string.lower(output_type) == 'rgba' then
			color_output = 'rgba('
		else
			color_output = 'rgb('
		end
		-- Convert all letters to uppercase
		color = string.upper(color)
		-- Remove # character
		color = string.gsub(color, '#', '')
		-- Check if input is valid
		if string.match(color, '%x') then
			if #color == 3 then
				for i = 1, 3, 1 do
					local color_help = {}
					color_help[i] = string.sub(color, i, i)
					color_help[i] = letters[color_help[i]] or color_help[i]
					color_output = color_output .. color_help[i] + color_help[i] * 16
					if i ~= 3 then color_output = color_output .. ',' end
				end
			else
				local color_storage
				for i = 1, 6, 1 do
					local color_help = {}
					color_help[i] = string.sub(color, i, i)
					color_help[i] = letters[color_help[i]] or color_help[i]
					if i % 2 == 1 then
						color_storage = color_help[i] * 16
					end
					if i % 2 == 0 then
						color_storage = color_storage + color_help[i]
						color_output = color_output .. color_storage
					end
					if i == 3 or i == 5 then
						color_output = color_output .. ','
					end
				end
			end
			-- Close the bracket
			if string.lower(output_type) == 'rgba' then
				color_output = color_output .. ',1)'
			else
				color_output = color_output .. ')'
			end
		else 
			color_output = '<strong class="error">Template Error: color code was invalid \"' .. color .. '\"</strong>[[Category:Pages with template errors]]'
		end
	-- Int
	elseif string.match(string.lower(output_type), 'int') then
		local letters = { ['A'] = 10, ['B'] = 11, ['C'] = 12, ['D'] = 13, ['E'] = 14, ['F'] = 15 }
		if color:lower():match('rgb?') then
			-- Delete everything except numbers and commas
			color = string.gsub(color, 'rgba?%((.*)%)', '%1')
			-- Split the numbers apart
			color = mw.text.split(color, '%s*,%s*')
		
			-- Check if input is valid
			if tonumber(color[1]) < 0 or tonumber(color[1]) > 255 or tonumber(color[2]) < 0 or tonumber(color[2]) > 255 or tonumber(color[3]) < 0 or tonumber(color[3]) > 255 then
				color_output = '<strong class="error">Template Error: Invalid RGB color \"rgb(' .. color[1] .. ',' .. color[2] .. ',' .. color[3] .. ')\"</strong>[[Category:Pages with template errors]]'
			else
				color_output = tonumber(color[1]) * 65536 + tonumber(color[2]) * 256 + tonumber(color[3])
			end
		else
			-- Convert all letters to uppercase
			color = string.upper(color)
			if string.match(color, '(#)(%x)') then
				-- Remove # character
				color = string.gsub(color, '#', '')
				if #color == 3 then
					local color_help = {}
					for i = 1, 3, 1 do
						color_help[i] = string.sub(color, i, i)
						color_help[i] = letters[color_help[i]] or color_help[i]
					end
					color_output = color_help[1] * 65536 * 17 + color_help[2] * 256 * 17 + color_help[3] * 17
				else
					local color_help = {}
					for i = 1, 6, 1 do
						color_help[i] = string.sub(color, i, i)
						color_help[i] = letters[color_help[i]] or color_help[i]
						if i % 2 == 1 then
							color_help[i] = color_help[i] * 16
						end
					end
					color_output = (color_help[1] + color_help[2]) * 65536 + (color_help[3] + color_help[4]) * 256 + (color_help[5] + color_help[6])
				end
			else
				color_output = color
			end
		end
	else -- arg[1] is invalid
		color_output = string.error('Invalid Color Output %q', output_type)
	end
	return color_output
end

-----------------------------------------------------------------------------
-- Template:Color
--
-- Changes text color
-----------------------------------------------------------------------------
-- p.color(color : string/number/table, text : string/number/table)
function p.color(frame)
	local args = getArgs(frame)
	local text = args[2] or ''
	local color = args['color'] or args['c'] or args[1]
	return string.pcall(p._colorTemplates, color, text)
end
function p._color(color, text)
	return string.wrapHtml(text, '<font>', { style = { color = color } })
end

-----------------------------------------------------------------------------
-- Template:Color Display
--
-- Displays input color as HEX code and a small preview
-----------------------------------------------------------------------------
function p.colorDisplay(frame)
	local args = getArgs(frame)
	local color = args[1]
	local preserveCase = yesno(args['preserve_case'] or args['preservecase'] or args['case'] or args['pc'] or args['c'])
	return p._colorDisplay(color, preserveCase)
end
function p._colorDisplay(color, preserveCase)
	if color:find('rgb') then
		color = p._color_conversion('hex', color)
	end
	-- Remove all "#"
	if color:find('#') then
		color = color:gsub('#', '')
	end
	if color:match('^%x%x%x%x?$') or color:match('^%x%x%x%x%x%x$') then -- allows 3, 4, or 6 hex decimals
		color = '#' .. color
	end
	if not preserveCase then color = color:upper() end
	return string.wrapHtml('', 'span', {
		style = { ['background-color'] = color },
		class = 'color-display-block'
	}) .. libU.pipeline(
		table.concat{ '&nbsp;' .. color }, 'code', string.wrapTag
	)
end
p.color_display = p.colorDisplay -- deprecated; may still have usages outside this code
p._color_display = p._colorDisplay -- deprecated; may still have usages outside this code

-----------------------------------------------------------------------------
-- Template:Armor Colors
--
-- Creates an invisible table with armor colors. Used by {{Infobox armor}}
-----------------------------------------------------------------------------
function p.armorColors(frame)
	local function makeCell(htmlObj, piece, text)
		if text then
			htmlObj:tag('tr')
				:tag('td'):css{ style = 'align:right;' }
					:tag('b'):wikitext(piece):done()
				:done()
				:tag('td')
					:wikitext(p._colorDisplay(text))
				:done()
			:done()
		end
	end
	
	local args = getArgs(frame)
	local inputs = string.lower(args[1])
	local all_the_same = yesno(args['all'])
	
	-- Store preformated strings
	local preformated = {
		['fairy'] = string.wrapTag(table.map({
				{'A', '<font>', { style = { color = '#FF66B2' }}},
				{'N', '<font>', { style = { color = '#FF3399' }}},
				{'I', '<font>', { style = { color = '#FF33FF' }}},
				{'M', '<font>', { style = { color = '#FF66FF' }}},
				{'A', '<font>', { style = { color = '#9933FF' }}},
				{'T', '<font>', { style = { color = '#FF99FF' }}},
				{'E', '<font>', { style = { color = '#FF66B2' }}},
				{'D', '<font>', { style = { color = '#FF99CC' }}},
			}, string.wrapHtml), 'b'),
		['crystal'] = string.wrapTag(table.map({
				{ 'C', '<font>', { style = { color = '#FCF3FF' }}},
				{ 'H', '<font>', { style = { color = '#E5D1ED' }}},
				{ 'A', '<font>', { style = { color = '#C9A3D4' }}},
				{ 'N', '<font>', { style = { color = '#A875BD' }}},
				{ 'G', '<font>', { style = { color = '#8E51A6' }}},
				{ 'I', '<font>', { style = { color = '#6A2C82' }}},
				{ 'N', '<font>', { style = { color = '#5D1C78' }}},
				{ 'G', '<font>', { style = { color = '#46085E' }}}
			}, string.wrapHtml), 'b'),
	}
	
	if preformated[inputs] then 
		return preformated[inputs]
	else
		inputs = mw.text.split(inputs, ',')
		if all_the_same then
			return p._colorDisplay(inputs[1])
		else
			local ret = mw.html.create('table')
			local t = { 'Helmet:', 'Chestplate:', 'Leggings:', 'Boots:' }
			for i, v in ipairs(t) do
				makeCell(ret, v, inputs[i])
			end
			return tostring(ret:done())
		end
	end
end

--Finish Module
return p
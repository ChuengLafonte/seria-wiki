--<pre>
local p = {}

local loader = require('Module:Loader')
local string, table, arguments = loader.require('String', 'Table', 'Arguments')
local historyDatasheet, historyAliases = loader.loadData('History/Datasheet', 'History/Aliases')

local changelogs, versionmap = historyDatasheet.changelogs, historyDatasheet.versionmap
local update_aliases, month_index, long_months, short_months = historyAliases.update, historyAliases.month_index, historyAliases.long_month, historyAliases.short_month

-----------------------------------------------------------------------------------------------------
-- Template:History
--
-- Displays a row of history description with changelog link
-----------------------------------------------------------------------------------------------------
function p.history(frame)
	args = arguments.getArgs(frame)
 
	local input_date = args[1]
	local version = args["version"] or args["ver"]
	local link = args["link"] or args["l"]

	-- get technically infinite amount of arguments for text
	local rows = 2
	local text = {}
	while args[rows] do
		text[rows-1] = args[rows]
		rows = rows + 1
	end
	rows = rows - 2
 
	return string.pcall(p._history, input_date, text, rows, version, link)
end

-- Module access point
function p._history(input_date, text, rows, version, link)
	-- Remove whitespace from the beginning and the back of input_date
	input_date = string.trim(input_date)
	local input_date_l = input_date:lower()
	local unknown = input_date_l:match('unknown')

	-- Decide display, date, version
	local display, date
	if unknown then
		-- if input_date is set to unknown, then display it
		local alt = input_date:match('[Uu]nknown%s*;%s*(.*)')
		display = alt or "Unknown Date"
		version = nil
	else
		local index = changelogs[input_date] and input_date or (versionmap[input_date_l] or update_aliases[input_date_l])
		if not index and not input_date:lower():find('%d%d%d%d/%a%a%a+%s%d%d?') then
			error(string.format('Invalid date or version %q', input_date))
		end
		if not index then
			-- split the date into parts
			local year = input_date:match("^(%d*)/.* %d%d?")
			local month = input_date:match("^%d*/(.*) %d%d?")
			local day = input_date:match("^%d*/.* (%d%d?)")
			
			year = tonumber(year)
			month = tonumber(month) or month_index[month:lower()]
			day = tonumber(day)
			
			-- check for errors in date
			if not year then error('Invalid year "' .. year .. '"', 2) end
			if not month then error('Invalid month "' .. month .. '"', 2) end
			if not day then error('Invalid day "' .. day .. '"', 2) end

			local idx = ('%s:%s:%s:0'):format(year, month, day)
			if changelogs[idx] then
				index = idx
			else
				-- corresponding data not found - assemble date instead
				date = year .. "/" .. long_months[month] .. " " .. day
				display = short_months[month] .. "&nbsp;" .. day .. ",&nbsp;" .. year
			end
		end
		if index then
			local dt = changelogs[index]
			if not dt then error('Invalid index "' .. index .. '"') end
			date = dt.page
			version = version or dt.version
			display = short_months[dt.m] .. "&nbsp;" .. dt.d .. ",&nbsp;" .. dt.y
		end
	end
	
	-- Determine link
	-- Check if link is set to none. If true, don't display any link, just text
	if (link or ''):lower() ~= 'none' then
		if link and (link:find('%[%[') and link:find('%]%]')) then
			display = table.concat{'[[', link:gsub('[%[%]]', ''), '|', display, ']]'}
		elseif link then
			display = table.concat{'[', link, ' ', display, ']'}
		elseif date then
			-- default for existing date: changelog link
			display = string.makeLink({ 'Changelog/', date }, display)
		end
	end
	
	-- Construct the history table
	local table_str = {}
	-- if version is not set to "none"
	if version and version:lower() ~= "none" then 
		table.push(table_str, '<tr>'..string.wrapHtml(display, '<th>', { rowspan=rows }))
		table.push(table_str, string.wrapHtml(version, 'th', { rowspan=rows }))
	-- if version is either not present or set to "none"
	else
		table.push(table_str, '<tr>'..string.wrapHtml(display, '<th>', { rowspan=rows, colspan=2 }))
	end
	-- display error if no text is specified
	if not text or not text[1] then error("No text specified") end
	-- always display the first text
	table.push(table_str, string.wrapTag(text[1], "td").."</tr>")
	-- display the following texts, if applicable
	for i = 2, rows, 1 do
		table.push(table_str, string.wrapTag(text[i], { "td", 'tr' }))
	end
	
	if unknown then
		table.push(table_str, string.makeLink('Category:Pages with unknown history dates'))
	end
	
	-- Concatenate the string
	return table.concat(table_str, '')
end

function p.changelog(frame)
	local args = arguments.getArgs(frame)
	local inp = args.version or args[1]
	local alt = args.alt
	local rstr = (inp or ''):lower()
	local idx = changelogs[rstr] and rstr or (versionmap[rstr] or update_aliases[rstr])
	if not (idx or inp) then
		return ('[[Changelog|%s]]'):format(alt or 'Changelog')
	end
	local link = idx and changelogs[idx].page or inp
	local disp = alt or (idx and changelogs[idx].name) or inp
	return ('[[Changelog/%s|%s]]'):format(link, disp)
end
 
-- Finish Module
return p
local makeClass = require("Module:Class")
local table = require("Module:Table")
local getArgs = require("Module:Arguments").getArgs
local number = require("Module:Number")
local string = require("Module:String")
local libU = require("Module:LibU")
local Parameter = { static = {} }

function Parameter.static.main(frame)
	local args = getArgs(frame, { removeBlanks = false })
	
	return Parameter:createBlockParameterDoc(args[1] or mw.title.getCurrentTitle().baseText, table.filterEntriesByKey(args, { 1 }))
end

function Parameter.static:createBlockParameterDoc(...)
	Parameter:checkSelfStatic(self)
	
	local name, params = libU.checkArgs({
		{ "string",  },
		{ "table" }
	}, ...)

	local tLen = table.length(params)
	local maxIndentLength = 1
	local sequentialParamsCount = #params
	local str = {}
	table.push(str, 
		"<pre>\n",
		"{{", string.makeLink({"Template:", name}, name), tLen > 0 and "\n" or ""
	)
	
	for k, v in pairs(params) do
		if not (type(k) == "number" and number.inRange(0, sequentialParamsCount, k)) and not (k == "...") then
			maxIndentLength = #k > maxIndentLength and #k + 1 or maxIndentLength	
		end
	end
	
	for k, v in pairs(params) do
		if v == "" then v = "..." end
		
		if type(k) == "number" and number.inRange(0, sequentialParamsCount, k) then
			table.push(str, "|", tostring(v), "\n")
		elseif k == "..." then
			table.push(str, "| ... \n", "|", tostring(v), "\n| ... \n")
		else		
			maxIndentLength = #k > maxIndentLength and #k + 1 or maxIndentLength
			table.push(str, 
				"|", 
				string.makeLink({ "#", "t-param-", k }, string.wrapHtml(tostring(k), "b", { id = "t-param-" .. k })), 
				(" "):rep(maxIndentLength - #k), "=", " ", tostring(v), 
				"\n"
			)
		end
	end
	
	table.push(str, 
		"}}",
		"\n</pre>"
	)
	
	return table.concat(str)
end

Parameter = makeClass(Parameter)

return Parameter

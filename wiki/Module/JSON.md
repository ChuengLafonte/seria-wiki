-- <pre>
local json = {}
local libU = require('Module:LibU')

function json.encode(val)
	return mw.text.jsonEncode(val)
end

function json.decode(str)
	libU.checkType(1, str, "string")
	return mw.text.jsonDecode(str)
end

return json
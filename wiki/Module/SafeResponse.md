local loader = require('Module:Loader')
local stringTemplates, json = loader.lazy.require('String/Templates', 'JSON')
local moduleData = loader.lazy.loadData('SafeResponse/Data')
local ES = moduleData.ErrorSignatures
local uES = moduleData.UnknownErrorSignature

local p = {}

-- Standard Error Format (callee_function): calling an error in a typical function
-- error({ type='', format={} })
-- Please add <SafeResponse:enabled> before functions with SEF

-- Standard (Top-level) Handling Format (caller_function): calling a Frame object receiving function that uses the Standard Error Format
-- local success, result = safeResponse.call(callee_function)
-- if not success then return result end

function p.StandardError(errorObject)
	local typeName, formatTable, message, category
	if type(errorObject) == 'table' then
		typeName, formatTable = errorObject.type, errorObject.format
	end
	if ES[typeName] then
		message, category = ES[typeName].message, ES[typeName].category
	else
		-- If your code reached here,
		-- you probably want to add an Error Signature and embed your error information in the Standard Error Format!
		message, category = uES.message, uES.category
		formatTable = { ((errorObject ~= nil) and json.encode(errorObject) or 'No further information is provided') }
	end
	for k, v in ipairs(formatTable or {}) do
		local success, result = pcall(string.gsub, message, '{' .. k .. '}', v)
		if success then message = result end
	end
	return stringTemplates.nocircle(message) .. (category and '[[Category:' .. category .. ']]' or '')
end

function p.callWithHandler(handler)
	return function(fn, ...)
		local params = {...}
		local function makecall()
			return fn(unpack(params))
		end
		return xpcall(makecall, handler)
	end
end

-- Hey there!
-- If you are tracing an error to this line, please probe later in the trace stack to see what's wrong.
-- This function only relays that error information!
-- You probably want to add an Error Signature and embed your error information in the Standard Error Format!
p.call = p.callWithHandler(p.StandardError)

-- Uncomment to test!
-- function p.callee(a)
-- 	error(a)
-- 	error('foo')
-- 	error({ type='', format={} })
-- end
-- function p.caller(frame)
-- 	local success, result = p.call(p.callee, 'test')
-- 	if not success then return result end
-- 	mw.log(1)
-- end

return p
local getArgs = require('Module:Arguments').getArgs
local Documentation = require('Module:Documentation/Core')

-- Begin Exports
local Doc = {}
local titleObj = mw.title.getCurrentTitle()

function Doc.main(frame)
	local args = getArgs(frame)
	
	return Documentation(args[1], args[2], args[3] or false)
end

function Doc.module(title, noNotices)
	checkType(1, title, 'string', true)
	checkType(2, noNotices, 'boolean', true)
	
	return Documentation(title or titleObj.text, 'Module', noNotices)
end

function Doc.template(title, noNotices)
	checkType(1, title, 'string', true)
	checkType(2, noNotices, 'boolean', true)
	
	return Documentation(title or titleObj.text, 'Template', noNotices)
end

function Doc._module(frame)
	local args = getArgs(frame)
	
	return Documentation(args[1] or titleObj.text, 'Module', args['nonotices'] or args['nonotice'] or args['nonoti'] or args['nn'])
end

function Doc._template(frame)
	local args = getArgs(frame)
	
	return Documentation(args[1] or titleObj.text, 'Template', args['nonotices'] or args['nonotice'] or args['nonoti'] or args['nn'])
end

return Doc
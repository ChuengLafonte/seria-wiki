local p = {}

local loader = require('Module:Loader')
local string, table, yesno, lu, makeClass, colorMdl, arguments = loader.require('String', 'Table', 'Yesno', 'LibraryUtil', 'Class', 'Color', 'Arguments')
local getArgs, mergeArgsSyntax = arguments.getArgs, arguments.mergeArgsSyntax
local addColor = colorMdl._colorTemplates

local valTypes = {
	['number'] = 'num',
	['num'] = 'num',
	['n'] = 'num',
	
	['hexadecimal'] = 'hex',
	['hex'] = 'hex',
	['h'] = 'hex',
	
	['red green blue'] = 'rgb',
	['rgb'] = 'rgb',
		
	['string'] = 'string',
	['s']= 'string',
	['string'] = 'string',
	['text'] = 'string',
	['str'] = 'string',
	['t'] = 'string',
	
	['boolean'] = 'bool',
	['yes/no'] = 'bool',
	['yesno'] = 'bool',
	['bool'] = 'bool',
	['y/n'] = 'bool',
	['yn'] = 'bool',
	['b'] = 'bool',
	
	['t'] = 'table',
	['table'] = 'table',
	['tab'] = 'table',
	['tbl'] = 'table',
	['tabl'] = 'table',
	['arr'] = 'table',
	['array'] = 'table',
	['ob'] = 'table',
	['object'] = 'table',
	['o'] = 'table',
	['obj'] = 'table',
	['ar'] = 'table',
	
	['f'] = 'function',
	['func'] = 'function',
	['funct'] = 'function',
	['function'] = 'function',
	['fun'] = 'function',
	
	['nr']='not required';
	['nt r']='not required';
	['not r']='not required';
	['n req']='not required';
	['nt req']='not required';
	['nt requir']='not required';
	['nt require']='not required';
	['nt required']='not required';
	['not r']='not required';
	['notreq']='not required';
	['not req']='not required';
	['not requir']='not required';
	['not required']='not required';
	
	['fr']='frame';
	['fa']='frame';
	['fra']='frame';
	['fram']='frame';
	['frme']='frame';
	['frame']='frame';
	
	['ni']='nil';
	['nil']='nil';
	['null']='nil';
	['undefined']='nil';
	['undef']='nil';
	['nll']='nil';
	
	['any']='any';
	['an']='any';
	['a']='any';
	['al']='any';
	['all']='any';
	
}
local valFormats = {
	['num'] = addColor('LightPurple', 'number'),
	['hex'] = addColor('LightPurple', 'hex'),
	['rgb'] = table.concat{ addColor('Red', 'R'), addColor('Green', 'G'), addColor('Blue', 'B') },
	['string'] = addColor('Aqua', 'string'),
	['bool'] = addColor('Orange', 'boolean'),
	['table'] = addColor('Green', 'table'),
	['frame'] = addColor('#b52a2a', 'frame'),
	['function'] = addColor('White', 'function'),
	['not required'] = addColor('#8972e5', 'NR'),
	['nil'] = addColor('#f9b3b3', 'nil'),
	['any'] = table.concat{ 
		addColor('LightPurple', 'a'),
		addColor('Aqua', 'n'),
		addColor('Green', 'y'),
	},
}

local valAbbrs = {
	['num'] = 'Number value. Can only contain numbers from 0 to 9. Can also be a string value but with just numbers.',
	['hex'] = 'Hexadecimal value (String/Number). Can only contain numbers from 0 to 9 and letters from A to F. If the number is not a string value, it\'s format should be written in 0x{...}',
	['rgb'] = 'Red Green Blue value (String).',
	['string'] = 'String or text value.',
	['bool'] = 'Boolean value. Put simply, a yes/no or a true/false value.',
	['table'] = 'Table value. This table can contain other values of any type, or even other tables.',
	['frame'] = 'Frame (Table) value. This value is generated automatically when the function is called from wikitext via #invoke, or can be called manually by passing a frame object to it by using mw.getCurrentFrame()',
	['function'] = 'Function value. This function is likely a callback function in the module.',
	['not required'] = 'This field is not required, meaning this parameter doesn\'t need to be passed to the function.',
	['nil'] = 'Nil value. This parameter may be omitted from the function call.',
	['any'] = 'Any value is allowed, the parameter may also be omitted from the function call.',
}


local function combineFormat(val)
	local html = mw.html.create('font')
	local comma = string.wrapHtml(',&nbsp;', 'font', {style="color: #269900"})
	
	if val:match('(.*)%s*,%s*(.+)') then
		val = string.split(val, '%s*,%s*')
		
		for j = 1, #val, 1 do
			local v = val[j]
			v = v:lower()
			v = valTypes[v] or 'all'
			
			v = table.concat{ string.makeTitle(valFormats[v], valAbbrs[v]), (j ~= #val and comma or '') }
			val[j] = v
		end
		
		val = table.concat(val)
	else
		val = val:lower()
		val = valTypes[val] or 'all'
		
		val = string.makeTitle(valFormats[val], valAbbrs[val])
	end
	 
	local html = html:attr({ color="#AAA" })
		:tag('sup')
			:wikitext('(', val, ')')
		:done()
	:done()
	
	return tostring(html)
end

---------------------------------------------------------------------------------
-- Template: LuaFunction
-- 
-- Generates a list of parameters for documentation/examples on lua functions
---------------------------------------------------------------------------------
function p.luaFunction(frame)
	local args = getArgs(frame, {removeBlanks = false})
	
	local link = args["l"] or args["lin"] or args["link"]
	local params = mergeArgsSyntax(args)
		
	local multiline = yesno(args["m"] or args["mult"] or args["multil"] or args["multiline"], false)
	local _table = yesno(args["t"] or args["tab"] or args["table"], false)
	local useBg = yesno(args["bg"] or args["back"] or args["backg"] or args["backgr"] or args["background"], true)
	local lineBreak = yesno(args["b"] or args["lb"] or args["linebreak"] or args["break"], false)
	
	return string.pcall(p._luaFunction, params, link, {
		multiline=multiline,
		usebg=useBg,
		table=_table,
		linebreak=lineBreak,
	})
end


--Module Access Point
function p._luaFunction(params, link, options)
	if not params or params[1] == "" or params == ''
		then return ''
	end
	
	local params = type(params) == 'string' and {params} or params
	funcName = params[1]
	
	assertTrue(funcName, 'Function name must be provided', 2)
	assertFalse(funcName:match('([^%_%w%.%:%(%)]+)'), 'Function name contains illegal characters \"%s\"', 2, params[1]:match('([^%_%.%w%:%(%)]+)'))
	table.remove(type(params) == 'string' and {} or params, 1)
	
	local options = options or {}
	local fName = '_luaFunction'
	local multiline, _table, useBg, lineBreak = 
		options.multiline or options.ml,
		options.table or options.t,
		options.usebg or options.bg,
		options.linebreak or options.lb or options.b;
	
	--check for errors
	checkType(fName, 1, params, 'table')
	checkType(fName, 2, link, 'string', true)
	checkType(fName, 1, options, 'table')
	
	local comma = string.wrapHtml(
		',&nbsp;', 
		'font', 
		{style="color: #269900"}
	)
	
	local funcName = funcName
		:gsub('([%(%)])', '<font style="color: #66cc66;">%1</font>')
		:gsub('([%.%:])([^%s])', '<font style="color: #269900;">%1</font>%2')
	
	for i = 1, #params do
		local function err(msg, ...)
			return error(string.format('Invalid list entry #%s: %s', i, msg, ...), 2)
		end
		
		if type(params[i]) ~= "string"
			then err('string expected, got %s', type(params[i]))
		end
		
		params[i]:gsub(mw.text.nowiki('='), '=', 1)
		
		if params[i]:match('%s*;%s*.') then
			params[i], endTag = params[i]:match('(.*)%s*;%s*(.+)')
			
			endTag = endTag or 'all'
			
			endTag = combineFormat(endTag, i)
		elseif params[i]:match('%s*;%s*$') then
			params[i] = params[i]:gsub('%s*;%s*$', '')
			endTag = ''
		else
			endTag = combineFormat('all', i)
		end
		
		
		local function colorVal(val, color)
			return string.wrapHtml(val, 'font', {style={ color=color }});
		end
		
		if params[i]:match('^(.+)%s*=%s*(.*)$') and _table then
			name, params[i] = params[i]:match('^(.+)%s*=%s*(.*)$')
			name = string.format('%s%s', 
					colorVal(name
						:gsub('([%[%]])', 
						colorVal('%1', "#66cc66")
					), '#93a1a1'), 
					colorVal('&nbsp;=&nbsp;', '#269900')
				)
			
			else 
				name = ''
		end
		
		params[i] = table.concat{
			name, 
			(params[i] ~= ""
			and string.wrapHtml(
				table.concat{
					mw.text.nowiki('<'),
					params[i],
					mw.text.nowiki('>')
				}, 
				'font', 
			   {style="opacity: 0.65"}) 
			or '')
		}
			
		--[[
		local matchPatterns = {
			'([\'\"])(.-)([\'\"])',
			'([%{%}%(%)%[%]%=%,%.%%%+%-%/%*%^])',
			'true',
			'false',
			'nil',
			
		}
		
		local function matchAll(k, t)
			for i, v in ipairs(t) do
				if k:match(v) then return true end
			end
		end
		
		if matchAll(params[i], matchPatterns) then
			local formatTable1 = {
					['{']=colorKey('{', "#66cc66");
					['}']=colorKey('}', "#66cc66");
					['(']=colorKey('(', "#66cc66");
					[')']=colorKey(')', "#66cc66");
					[',']=colorKey(',', "#269900");
					['[']=colorKey('[', "#66cc66");
					[']']=colorKey(']', "#66cc66");
					['.']=colorKey('.', "#269900");
					['%']=colorKey('%', "#269900");
					['+']=colorKey('+', "#269900");
					['-']=colorKey('-', "#269900");
					['/']=colorKey('/',"#269900");
					['*']=colorKey('*', "#269900");
					['^']=colorKey('^', "#269900");
					--[':']=colorKey(':', "#269900");
					
				}
				
			local formatTable2 = {
					['nil']=colorKey('nil', '#b58900');
					['true']=colorKey('true', '#b58900');
					['false']=colorKey('false', '#b58900');
				}
				
			
			
			--Subsitution must be in this order to avoid html screw ups
			params[i] = params[i]:gsub(matchPatterns[1], colorKey('%1%2%3', '#2AA198'))
			params[i] = params[i]:gsub(matchPatterns[2], formatTable1 )
			params[i] = params[i]:gsub(matchPatterns[3], formatTable2)
			params[i] = params[i]:gsub(matchPatterns[4], formatTable2)
			params[i] = params[i]:gsub(matchPatterns[5], formatTable2)
			
		end
		]] --Syntax highlighter Disabled due to issues with parsing, might make a template that does that
		if params[i] == "" then params[i] = string.wrapHtml("...", 'font', {style="color: #859900"}) end
		
		--Append Commas
		
		params[i] = params[i]..endTag
		
		if #params ~= i 
			then params[i] = params[i]..comma
		end
	end
	
   local function wrap(z)
		local str = (_table and '({' or '(')
		return string.wrapHtml(z and string.reverseSymbol(str, true) or str, 'font', {style='color: #66cc66'})
	end
	
	ret = string.wrapHtml{
		string.format(
			'%s%s%s%s',
			string.wrapHtml(funcName, 'font', {style="color: #268bd2"}),
			wrap(false)..(_table and '&nbsp;' or ''),
			table.concat(params, ""), 
			(_table and '&nbsp;' or '')..wrap(true)
		),
		'font', 
		{
			style={
				["font-family"]="monospace";
				["background"]=useBg and "rgba(0, 0, 0, 0.35)" or nil;
				["padding"]=useBg and "1.5px" or nil; 
				["border-radius"]=useBg and "3px" or nil;
			}
		}
	}..(lineBreak and '<br>' or '')
	
	return link and table.concat{'[[', link, '|', ret, ']]'} or ret
end


local LuaFunction = makeClass('LuaFunction', {
	constructor = function(name, params, options)
		checkType(true, 1, name, { 'string' })
		checkType(true, 2, params, { 'table', 'string' }, true)
		checkType(true, 3, options, { 'table' }, true)
		
		assertTrue(name ~= '', 'Function name must not be empty', 3)
		
		params = type(params) == 'string' and {params} or params or {}
		options = options or {}
		
		self.funcName = name
		self.paramsLength = #params
		self.useTable = Boolean(options.useTable, false)
		self.link = options.link
		self.params = params
		self.useBg = Boolean(options.useBg, true)
		
		self:parseParams()
		
		if self.useTable then
			self.close = self.paramsLength > 1 and '&nbsp;}' or '}'
			self.open = self.paramsLength > 1 and '{&nbsp;' or '{'
		else
			self.close = ')'
			self.open = '('
		end
	end,
	parseParams = function()
		local _ = self.params and table.mapWith(self.params, function(k, param)
			param = param:gsub(mw.text.nowiki('='), '=')
			
			local name, label = param:match("^(.-)%s*=%s*(.*)$")
			local _, types = param:match('^(.-)%s*;%s*(.*)$')
			
			if _ and not label then
				label = _
			elseif not label 
				then label = param 
			end
			
			if types then
				if types == "" then
					types = false
				else
					types = string.split(types, '%s*,%s*')
				end
			end
			
			return {
				types = types or {},
				label = label,
				name = name,
			}
		end)
	end,
	tostringParam = function(_, t)
		local ret = {}
		
		if t.name then
			table.push(ret, string.bold(t.name), '&nbsp;=&nbsp;')
		end
		
		if string.startsWith(t.label, '...') and t.label ~= "..." then
			table.push(ret, addColor(LuaFunction.colors.varArgs, '...'))
			t.label = t.label:gsub('^%.%.%.', '')
		elseif t.label == "..." then
			t.label = ""
		end
		
		return table.concat(table.merge(ret, {
			t.label == "" and addColor(LuaFunction.colors.varArgs, '...') or string.styleString('&lt;'..t.label..'&gt;', {
				opacity=0.65;
				['font-family']='monospace';
			}),
		}))
	end,
	__tostring = function()
		self.funcName = pipeline(
			LuaFunction.colors.fname,
			self.funcName:gsub('([%(%)%.%:])', function(char)
				return string.wrapHtml(char, 'font', { style={ color=table.includes({ '.', ':' }, char) and LuaFunction.colors.index or LuaFunction.colors.paren } })
			end),
			addColor
		)
		
		self.open = addColor(LuaFunction.colors.paren, self.open)
		self.close = addColor(LuaFunction.colors.paren, self.close)
		
		local ret = string.wrapHtml{
			{
				self.funcName,
				self.open,
				table.concat(table.mapWith(self.params, bind(self.tostringParam, self)), tostring(LuaFunction.commaElement)),
				self.close,
			}, 'span', {
				style=self.useBg and {
					["font-family"]="monospace";
					["background"]=self.useBg and "rgba(0, 0, 0, 0.35)" or nil;
					["padding"]=self.useBg and "1.5px" or nil; 
					["border-radius"]=self.useBg and "3px" or nil;
				} or {}
			}
		}
		
		if self.link then
			if self.link:match('%/%/') or self.link:match('%?') then
				local url = mw.uri.new(self.link)
				
				return string.externalUrl({ url.protocol or 'https', '://', url.host or 'hypixel-skyblock.fandom.com', url.path or '/wiki/' }, url.query, ret)
			else
				return string.makeLink(self.link, ret)
			end
		else
			return ret
		end
	end,
	__concat = function(a, b)
		if a == self then
			return tostring(a)..b;
		else 
			return tostring(b)..a;
		end
	end,
	static = {
		commaElement = mw.html.create('font'):css{ color="#269900" }:wikitext(',&nbsp;'):done(),
		colors = {
			paren='#66cc66';
			index='#269900';
			fname='#268bd2';
			varArgs='#859900';
		},
		main = function(frame)
			return LuaFunction(table.unpackRaw(getArgs(frame, { removeBlanks=false })))
		end
	}
})

p.bind = bind
p.main = LuaFunction.main
p.LuaFunction = LuaFunction
return p

-- <pre>
local loader = require('Module:Loader')

local makeClass, yesno, inventorySlot, random =
	loader.require('Class', 'Yesno', 'Inventory slot', 'Random')
local colorData = loader.loadData('Color/Data')
local slot = inventorySlot.slot

local fillmode = function(s)
	if s == 'border' then -- all valid fill modes here
		return s
	else
		return yesno(s, true)
	end
end
local backslashSubstitute = function(s)
	-- substitute every '\<char>' but those that have special meaning for tooltips generation, e.g. '\&'
	s = s:gsub('\\\\', '\254'):gsub('\\([^&/])', '%1'):gsub('\254', '\\\\')
	return s
end
local backslashSubstituteStrict = function (s)
	-- substitute all '\<char>'
	s = s:gsub('\\\\', '\254'):gsub('\\(.)', '%1'):gsub('\254', '\\\\')
	return s
end
local makeGotoClass = function (id)
	return (id and id ~= 'none') and 'goto-' .. id:gsub('^goto%-', '')
end
---------------------------------------------------------------------------------
-- Main Interface Class
---------------------------------------------------------------------------------
local Interface = makeClass('Interface', {
	aprilFools = false,
	---------------------------------------------------------------------------------
	-- constructor(topText: string, id?: string, goBack?: table, hide?: boolean, fill?: boolean, rows?: number, cols?: number)
	-- 
	-- Constructor function for the methods provided. Creates the actual UI.
	---------------------------------------------------------------------------------
	constructor = function (self, ...)
		local topText, id, goBack, hide, fill, rows, cols, noarrow, noclose, arrow_, close_, inline
		if type(({...})[1]) == 'table' then
			local u = ({...})[1]
			topText, id, goBack, hide, fill, rows, cols, noarrow, noclose, arrow_, close_, inline =
				u.topText or u[1],
				u.id,
				type(u.goBack) == 'table' and u.goBack or {
					text = u.return_text or u.goback_text or u['return'] or u.goback,
					link = u.return_link or u.goback_link,
					id = u.return_id or u.goback_id,
				},
				u.hide,
				u.fill,
				u.rows,
				u.cols,
				u.noarrow,
				u.noclose,
				u.arrow or u.arrow_,
				u.close or u.close_,
				u.inline
		else
			topText, id, goBack, hide, fill, rows, cols, noarrow, noclose, arrow_, close_, inline = ...
		end
		goBack = goBack or {}
		rows, cols = tonumber(rows) or 6, tonumber(cols) or 9
		fill, noarrow, noclose, inline = fillmode(fill), yesno(noarrow, false), yesno(noclose, false), yesno(inline, false)
		local arrowX, arrowY, closeX, closeY
		self.randomColor = colorData.MCColors[random.number{16}] -- for april fools only
		self.hide = yesno(hide)
		self.id = id
		self.slots = {}
		self.custom = {}
		self.html = mw.html.create('div')
			:attr{ class='mcui mcui-Chest pixel-image' .. (inline and '' or ' mcui-centered') }
		if topText then
			self.html:tag('div'):attr{ class = 'mcui-header' }
				:wikitext(backslashSubstituteStrict(topText))
		end
		
		if arrow_ then
			if arrow_:match('^%d+%s*,%s*%d+$') then
				arrowX, arrowY = arrow_:match('^(%d+)%s*,%s*(%d+)$')
			elseif not yesno(arrow_) or arrow_:match('[Nn]one') then
				noarrow = true
			end
		end
		arrowX = tonumber(arrowX) or rows
		arrowY = tonumber(arrowY) or 4
		
		if close_ then
			if close_:match('^%d+%s*,%s*%d+$') then
				closeX, closeY = close_:match('^(%d+)%s*,%s*(%d+)$')
			elseif not yesno(close_) or close_:match('[Nn]one') then
				noclose = true
			end
		end
		closeX = tonumber(closeX) or rows
		closeY = tonumber(closeY) or 5
		
		for x = 1, rows, 1 do
			self.slots[x] = {}
			self.custom[x] = {}
			for y = 1, cols, 1 do
				if not noarrow and x == arrowX and y == arrowY then
					self:setSlot(x, y, {
						'Go Back',
						text = goBack.text and '&7' .. goBack.text or 'none',
						link = goBack.link or 'none',
						title = '&aGo Back',
						class = makeGotoClass(goBack.id),
					})
				elseif not noclose and x == closeX and y == closeY then
					self:setSlot(x, y, { 'Close' })
				else
					if fill == 'border' then
						if x == 1 or x == rows or y == 1 or y == cols then
							self:setBlankSlot(x, y)
						else
							self:setEmptySlot(x, y)
						end
					elseif not fill then
						self:setEmptySlot(x, y)
					else
						self:setBlankSlot(x, y)
					end
				end
			end
		end
	end,
	---------------------------------------------------------------------------------
	-- setSlot(x: number, y: number, args: table, isCustom?: boolean)
	-- 
	-- Sets a slot according to the `x` and `y` parameters provided, with the arguments
	-- to the parser as `args`.
	---------------------------------------------------------------------------------
	setSlot = function (self, x, y, args, isCustom)
		checkType(1, x, 'number')
		checkType(2, y, 'number')
		checkType(3, args, { 'table', 'string' })
		
		local tp = type(args)
		
		if tp == 'table' or (tp == 'string' and args:match('<.->.-</.->')) then
			self.slots[x] = self.slots[x] or {}
			self.custom[x] = self.custom[x] or {}
			self.slots[x][y] = args
			self.custom[x][y] = not not isCustom
		elseif tp == 'string' then
			assertTrue(self.slots[x] and self.slots[x][y], 'slot in posistion (%d, %d) does not exist', 2, x, y)[args] = isCustom
		end
		
		return self
	end,
	---------------------------------------------------------------------------------
	-- getSlot(x: number, y: number, prop?: string)
	-- 
	-- Gets a slot according to the `x` and `y` parameters provided, with an option parameter
	-- of `prop` to get a particular slot property.
	---------------------------------------------------------------------------------
	getSlot = function (self, x, y, prop)
		if prop then
			return assertTrue(self.slots[x] and self.slots[x][y], 'slot in posistion (%d, %d) does not exist', 2, x, y)[prop]
		else
			return self.slots[x][y]
		end
	end,
	---------------------------------------------------------------------------------
	-- hasSlot(x: number, y: number)
	-- 
	-- Checks if the UI has a specific slot based on `x` and `y`.
	-- NOTICE: THIS IS CURRENTLY UNUSABLE
	---------------------------------------------------------------------------------
	hasSlot = function (self, x, y)
		return not not self.slots[x][y]
	end,
	---------------------------------------------------------------------------------
	-- isEmptySlot(x: number, y: number)
	-- 
	-- Checks if a slot based on `x` and `y` is not blank.
	---------------------------------------------------------------------------------
	isEmptySlot = function (self, x, y)
		return self.slots[x][y][1] == '' or self.slots[x][y][1] == 'Blank'
	end,
	---------------------------------------------------------------------------------
	-- setBlankSlot(x: number, y: number)
	-- 
	-- Sets a blank slot according to the `x` and `y` parameters provided.
	---------------------------------------------------------------------------------
	setBlankSlot = function (self, x, y)
		if self.aprilFools then
			return self:setSlot(x, y, { ('Blank (%s)'):format(self.randomColor) })
		end
		return self:setSlot(x, y, { 'Blank' })
	end,
	---------------------------------------------------------------------------------
	-- setEmptySlot(x: number, y: number)
	-- 
	-- Sets a empty slot according to the `x` and `y` parameters provided.
	---------------------------------------------------------------------------------
	setEmptySlot = function (self, x, y)
		return self:setSlot(x, y, { '' })
	end,
	---------------------------------------------------------------------------------
	-- __tostring()
	-- 
	-- __tostring metamethod for the class. Parses the `slots` to an acual string.
	---------------------------------------------------------------------------------
	__tostring = function (self)
		for x, xValue in ipairs(self.slots) do
			local row = self.html:tag('div'):addClass('mcui-row')
			for y, yValue in ipairs(xValue) do
				row:wikitext(backslashSubstitute(self.custom[x][y] and yValue or slot(yValue)))
			end
		end
		return self.id
			and tostring(mw.html.create('div')
				:node(self.html)
				:attr{ 
					id = self.id and 'ui-' .. self.id:gsub('^ui%-', ''), 
					class = self.id and 'sbw-ui-tab-content', 
					style = self.hide and 'display: none;' or nil,
				} 
			:done())
			or tostring(self.html)
	end,
	static = {
		makeGotoClass = makeGotoClass
	},
})

return Interface

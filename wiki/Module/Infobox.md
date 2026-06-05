local getArgs = require('Module:Arguments').getArgs
local loader = require('Module:Loader')
local lu, table, makeClass = loader.require('LibU', 'Table', 'Class')

-- Infobox Core. Test cases moved to Module:Infobox/Test
-- TODO (probably not by me):
-- Restrict tags according to actual constraints
-- according to https://community.fandom.com/wiki/Help:Infoboxes/Tags
-- using self.mastertag

-- Set exports
local p = {}

--Variables
local curTitle = mw.title.getCurrentTitle()

local InfoboxCompound = makeClass('InfoboxCompound', {
	constructor = function(self, tag, attrsTable, parentcompound, opts)
		lu.checkType(1, tag, 'string')
		lu.checkType(2, attrsTable, 'table', true)
		lu.checkType(4, opts, 'table', true)
		attrsTable = attrsTable or {}
		self.mastertag = tag
		self.htmlnode = parentcompound and parentcompound.htmlnode:tag(tag) or mw.html.create(tag)
		self.htmlnode:attr(attrsTable)
		self.parentcompound = parentcompound
		if opts then
			-- handle extra options
			if opts.header then
				self.htmlnode
					:tag('header')
						:wikitext(table.format(opts.header))
					:done()
			end
			if opts.label then
				self.htmlnode:tag('label')
					:wikitext(table.format(opts.label))
			end
		end
		return self
	end,
})

local Infobox = makeClass('Infobox', {
	parent = InfoboxCompound,
	constructor = function(self, attrs)
		attrs = attrs or {}
		self:super('infobox', {
			["theme"] = attrs["theme"],
			["theme-source"] = attrs["theme-source"],
			["type"] = attrs["type"],
			["accent-color-source"] = attrs["accent-color-source"],
			["accent-color-default"] = attrs["accent-color-default"],
			["accent-color-text-source"] = attrs["accent-color-text-source"],
			["accent-color-text-default"] = attrs["accent-color-text-default"],
			["layout"] = attrs["layout"],
			["name"] = attrs["name"],
		})
		return self
	end,
})

local Panel = makeClass('Panel', {
	parent = InfoboxCompound,
	constructor = function(self, opts, parentcompound)
		self:super('panel', {
			layout = opts.layout,
			show = opts.show,
			collapse = opts.collapse,
			['row-items'] = tonumber(opts['row-items']),
			name = table.format(opts.name),
		}, parentcompound, {
			header = opts.header,
		})
		self._fromSection = opts._fromSection
		return self
	end,
	done = function(self)
		return self._fromSection and self.parentcompound:done() or self.parentcompound
	end,
})

local Section = makeClass('Section', {
	parent = InfoboxCompound,
	constructor = function(self, opts, parentcompound)
		self:super('section', {
			layout = opts.layout,
			show = opts.show,
			collapse = opts.collapse,
			['row-items'] = tonumber(opts['row-items']),
			name = table.format(opts.name),
		}, parentcompound, {
			label = opts.label,
		})
	end,
	-- Shorthand for "section:addGroup():addPanel() <...> :done():done()"
	addPanel = function(self, opts)
		lu.checkType(1, opts, 'table', true)
		opts = opts or {}
		opts._fromSection = true
		return self:addGroup():addPanel(opts)
	end,
})

local Group = makeClass('Group', {
	parent = InfoboxCompound,
	constructor = function(self, opts, parentcompound)
		self:super('group', {
			layout = opts.layout,
			show = opts.show,
			collapse = opts.collapse,
			['row-items'] = tonumber(opts['row-items']),
			name = table.format(opts.name),
		}, parentcompound, {
			header = opts.header,
		})
	end,
})

InfoboxCompound.prototype = {
	-- Static Types
	addTitle = function(self, opts)
		lu.checkType(1, opts, 'table', true)
		opts = opts or {}
		local inst = self.htmlnode
			:tag('title')
				:attr({
					source = opts.source or nil,
					name = opts.name,
				})
				:tag('default')
					:wikitext(table.format(opts.title or opts[1] or opts.default))
				:done()
		if opts.format then
			inst:tag('format')
				:wikitext(table.format(opts.format))
			:done()
		end
		inst:done()
		return self
	end,
	addData = function(self, opts)
		lu.checkType(1, opts, 'table', true)
		opts = opts or {}
		local data = opts.data or opts[1] or opts.default
		if data ~= nil and data ~= '' then
			local inst = self.htmlnode:tag('data')
				:attr({ 
					name = table.format(opts.name),
					layout = table.format(opts.layout),
					span = tonumber(opts.span),
				})
				:tag('default')
					:wikitext(table.format(data))
					:done()
			if opts.label then
				inst:tag('label')
					:wikitext(table.format(opts.label))
				:done()
			end
			if opts.format then
				inst:tag('format')
					:wikitext(table.format(opts.format))
				:done()
			end
			inst:done()
		end
		return self
	end,
	addImage = function(self, opts)
		lu.checkType(1, opts, 'table', true)
		opts = opts or {}
		local inst = self.htmlnode
			:tag('image')
				:attr({
					source = opts.source or ((not opts.default and not opts[1]) and error('infobox:addImage(): No image source or default specified', 2) or nil),
					name = opts.name,
				})
				:tag('default')
					:wikitext(table.format(opts.image or opts[1] or opts.default or curTitle.text..'.png'))
				:done()
		if opts.caption then
			local captionInst = inst:tag('caption')
				:attr({
					source = opts.caption.source or 'caption',
				})
				:tag('default')
					:wikitext(
						table.includes({ 'string', 'number' }, type(opts.caption))
							and opts.caption
							or table.format(opts.caption.text or opts.caption[1] or opts.caption.default)
					)
				:done()
			if opts.caption.format then
				captionInst:tag('format')
					:wikitext(table.format(opts.caption.format))
				:done()
			end
		end
		if opts.alt then
			local altInst = inst:tag('alt')
				:attr({
					source = opts.alt.source,
				})
				:tag('default')
					:wikitext(table.format(opts.alt.text or opts.alt[1] or opts.alt.default or opts.alt))
				:done()
		end
		inst:done()
		return self
	end,
	addNavigation = function(self, opts)
		lu.checkType(1, opts, 'table', true);
		opts = opts or {}
		self.htmlnode
			:tag('navigation')
				:wikitext(table.format(opts[1]))
				:attr{
					name = opts.name
				}
			:done()
		return self
	end,
	addHeader = function(self, opts)
		lu.checkType(1, opts, 'table', true);
		opts = opts or {}
		self.htmlnode
			:tag('header')
				:wikitext(table.format(opts[1]))
				:attr{
					name = opts.name
				}
			:done()
		return self
	end,
	-- Compound Types
	addPanel = function(self, opts)
		lu.checkType(1, opts, 'table', true)
		opts = opts or {}
		return Panel(opts, self)
	end,
	addGroup = function(self, opts)
		lu.checkType(1, opts, 'table', true)
		opts = opts or {}
		return Group(opts, self)
	end,
	addSection = function(self, opts)
		lu.checkType(1, opts, 'table', true)
		opts = opts or {}
		return Section(opts, self)
	end,
	-- Helpers
	done = function(self)
		return self.parentcompound or self.htmlnode:done()
	end,
	__tostring = function(self)
		return tostring(self.htmlnode:allDone())
	end,
	tostring = function(self)
		return self:__tostring()
	end,
	__concat = function(self, a, b)
		if tostring(a) == tostring(self.htmlnode) then
			return tostring(a) .. tostring(b)
		else
			return tostring(b) .. tostring(a)
		end
	end,
	preprocess = function(self, args, title)
		local f = mw.getCurrentFrame()
		local p = f:getParent()
		if p then f = p end
		return f:newChild{ title = title or curTitle.fullText, args = args or getArgs(f) }:preprocess(self:__tostring())
	end,
}

return Infobox
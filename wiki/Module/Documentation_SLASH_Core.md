local loader = require('Module:Loader')

local string, table, makeClass, lu = loader.require('String', 'Table', 'Class', 'LibraryUtil')
local config = loader.loadData('Documentation/Config')

local nowiki = mw.text.nowiki
local lb, rb = nowiki('['), nowiki(']')
local sep = ' <span class="bull-c"></span> '
local titleObj = mw.title.getCurrentTitle()

local notices = {
	protected = '{{Protected|type=template}}',
}
local noticePatterns = {
	protected = '{{[Pp]rotected%|?.-}}',
}

local Documentation = makeClass('Documentation', {
	config = config,
	constructor = function (self, title, _type, noNotices)
		lu.checkType(true, 1, title, 'string', true)
		lu.checkType(true, 2, _type, 'string', true)
		lu.checkType(true, 3, noNotices, 'boolean', true)
		
		self._title, self._type = title, string.ucfirst(_type or self:msg('type-module') )
		self._noNotices = noNotices
		
		if self:checkSkipDocumentation() then
			self.ret = ''
			return self
		end
		
		self:renderVariables()
		self.html = mw.html.create('div')
			
		self:generateData()
		self:renderNotices()
		
		self.ret, _ = tostring(self:buildMainBox())
			:gsub('__TYPE__', self.type)
			:gsub('__DIR__', self.type == self:msg('type-module') and self:msg('dir-module') or self:msg('dir-template'))
			:gsub('__PRELOAD__', self:msg('dir-preload'))
			:gsub('__EDITINTRO__', self:msg('dir-editintro'))
			
		return self
	end,
	
	linksToList = function (self, t, ignoreBrackets)
		local ret = {}
		local t2 = {}
	
		for i, v in ipairs(t) do
			table.push(ret, self:parseLinkEntry(v, ignoreBrackets or t.main))
		end
		
		ret = table.concat(ret, sep)
		
		if t.main then
			ret = table.concat{ 
				t.prepend and self:parseLinkEntry(t.prepend, true)..' ' or '', 
				self:parseLinkEntry(t.main, true),
				' <small>', 
				#t ~= 0 and '(' or '', 
				ret, 
				#t ~= 0 and ')' or '', 
				'</small>',
			}
		end
		
		return ret
	end,
	
	exists = function (self, title)
		return mw.title.new(title).exists
	end,
	
	existsWithoutWanted = function (self, title)
		return existsWithoutWanted(title)
	end,
	
	newTitleWithoutWanted = function (self, title)
		local exists = self:existsWithoutWanted(title)
		return exists
			and mw.title.new(title)
			-- if it doesn't exist we don't want to create a title object, as that would mark it as wanted
			or { exists=false, fullText=title, talkPageTitle={ exists=false } }
	end,
	
	msg = function (self, name, ...)
		lu.checkType(1, name, 'string')
		lu.assertTrue(self.config[name], 'Message %q does not exist', 2, name)
		
		return (tostring(self.config[name]):gsub('%$%d', '%%%s')):format(...)
	end,
	
	parseLinkEntry = function (self, t2, isMain)
		t2[1] = string.parseDualArg(t2[1])
		
		local val
		local title = string.makeTitle(t2[2] or '', t2[3], { disableAbbr=true })
		
		if t2.query then
			val = string.fullUrl(t2[1], t2.query or {}, title)
		else
			val = string.makeLink(t2[1], title)
		end
		
		return isMain and (t2.alt or val) or table.concat{ lb, val, rb }
	end,
	
	renderNotices = function (self)
		self.noticeStr = {}
		
		if self.subpageExists and not self._noNotices then
			for id, pattern in pairs(noticePatterns) do 
				local notice = notices[id]
				
				if not self.subpageContent:match(pattern) and self.noticeConditions[id] then
					table.push(self.noticeStr, notice)
				end
			end
		end
		self.noticeStr = table.concat(self.noticeStr, '\n')..'\n'
		
		return self.noticeStr
	end,
	
	renderVariables = function (self)
		self.ns = mw.site.namespaces[mw.title.getCurrentTitle().namespace].canonicalName;
		self.type = string.ucfirst(self._type or self:msg('type-module'))
		-- Since ns is set to the current page's type, if ns is set to module but the type isn't, set ns to type instead
		if self.ns == self:msg('type-module') and self.type ~= self:msg('type-module') then
			self.ns = self.type
		end
		self.title = self._title or self:msg('default-title')
		self.title = self.title:find(':') and self.title or table.concat{ self.ns, ':', self.title }
		self.title = self.title:gsub('^:', ''):gsub('%/doc$', '')
		self.sandbox = table.concat{ self.title, '/', self:msg('subpage-sandbox') }
		self.testcases = table.concat{ self.title, '/', self:msg('subpage-testcases') }
		self.doc = table.concat{ self.title, '/', self:msg('subpage-documentation') }
		mw.log(self.invokedTitle)
		
		self.titleObj = lu.assertTrue(mw.title.new(self.title), 'Bad module title %q', 4, self.title)
		self.titleExists = self.titleObj.exists
		
		-- We don't want these to show up as wanted - as such we have to reconstruct the talk page link manually
		self.talk = table.concat{ mw.site.namespaces[self.titleObj.namespace].talk.name, ':', self.titleObj.text }
		self.talkObj = self:newTitleWithoutWanted(self.talk)
		self.sandboxObj = self:newTitleWithoutWanted(self.sandbox)
		self.testcasesObj = self:newTitleWithoutWanted(self.testcases)
		self.invokedTitleObj = titleObj
		
		self.docObj = mw.title.new(self.doc)
		self.subpageExists = self.docObj.exists
		self.subpageContent = self.subpageExists and self.docObj:getContent() or nil
		
		return self
	end,
	
	generateData = function (self)
		self.createDocQuery = {
			action='edit',
			redlink=1,
			minor=1,
			useeditor='source',
			preload='Template:__DIR__/__PRELOAD__',
			editintro='Template:__DIR__/__EDITINTRO__',
			summary=self:msg('doc-edit-summary', self.doc);
		}
		
		self.createSandbox = {
			self.sandbox,
			string.makeTitle(self:msg('sandbox-create-text'), self:msg('sandbox-create-title'), { disableAbbr=true }),
			query = {
				action='edit',
				redlink=1,
				minor=1,
				useeditor='source',
				preload=self.title,
				summary=self:msg('sandbox-create-summary', self.doc);
			}
		}
		
		self.links = {}
		self.links.pageTools = {
			{
				{ self.doc, self:msg('main-view-text'), self:msg('main-view-title'), },
				{ self.doc, self:msg('main-edit-text'), self:msg('main-edit-title'), query={ action='edit' }},
				{ self.doc, self:msg('main-curdiff-text'), self:msg('main-curdiff-title'), query={ diff='cur' }},
				{ self.doc, self:msg('main-hist-text'), self:msg('main-hist-title'), query={ action='history' }},
				{ self.title, self:msg('main-purge-text'), self:msg('main-purge-title'), query={ action='purge' }},
			},
			{
				{ self.doc, self:msg('main-create-text'), self:msg('main-create-title'), query=self.createDocQuery },
				{ self.title, self:msg('main-purge-text'), self:msg('main-purge-title'), query={ action='purge' }},
			}
		}
		
		self.links.sandbox = {
			main={ self.sandbox, self:msg('sandbox-main-text') },
			{ self.sandbox, self:msg('sandbox-edit-text'), self:msg('sandbox-edit-title'), query={ action='edit' }},
			{ self.sandbox, self:msg('sandbox-curdiff-text'), self:msg('sandbox-curdiff-title'), query={ diff='cur' }},
			{ self.sandbox, self:msg('sandbox-hist-text'), self:msg('sandbox-hist-title'), query={ action='history' }},
			{ 
				alt=string.wrapHtml{ 
					self:msg('sandbox-reset-text'), '<span>', attrs={ 
						title=self:msg('sandbox-reset-title'),
						id='re-mirror-sandbox',
						style={ cursor='pointer'; }
					}
				}, 
			},
		}
		
		self.links.tools = {
			{ { 'Special:PrefixIndex/', self.title, '/' }, self:msg('tool-subpages-text'),  self:msg('tool-subpages-title') },
			{ { 'Special:WhatLinksHere/', self.title, }, self:msg('tool-whl-text'), self:msg('tool-whl-title') },
		}
		
		self.links.talk = {
			{
				main={ self.talk, self:msg('talk-main-text') },
				prepend={ self.talk, '+', self:msg('talk-newsec-title'), query={ action='edit', section='new' }},
				{ self.talk, self:msg('talk-edit-text'), self:msg('talk-edit-title'), query={ action='edit' }},
				{ self.talk, self:msg('talk-curdiff-text'), self:msg('talk-curdiff-title'), query={ diff='cur' }},
				{ self.talk, self:msg('talk-hist-text'), self:msg('talk-hist-title'), query={ action='history' }},
			},
			{
				main={ 
					self.talk, 
					self:msg('talk-create-text'), 
					self:msg('talk-create-title'), 
					query={ 
						action='edit',
						redlink=1,
						minor=1,
						useeditor='source',
						section='new',
						summary=self:msg('talk-create-summary', self.title),
					}
				},
			},
		}
		
		self.links.pageLinks = {
			{ alt=self:linksToList(self.links.talk[self.talkObj.exists and 1 or 2]) },
			{ self.title, self:msg('page-curdiff-text'), self:msg('page-curdiff-title'), query={ diff='cur' }},
			{ { 'Special:Log/', self.title }, 'Page Logs', 'View the logs for this page', },
		}
		
		self.links.testcases = {
			{
				 main={ self.testcases, self:msg('test-main-text'), self:msg('test-main-title') },
				 { self.testcases, self:msg('test-edit-text'), self:msg('test-edit-title') },
				 { self.testcases, self:msg('test-curdiff-text'), self:msg('test-curdiff-title') },
				 self.testcasesObj.talkPageTitle.exists
					and { self.testcasesObj.talkPageTitle.fullText, self:msg('test-run-text'), self:msg('test-run-title') }
					or { 
						self.testcasesObj.talkPageTitle.fullText, 
						self:msg('test-results-create-text'), 
						self:msg('test-results-create-title'), 
						query={ 
							action='edit',
							redlink=1,
							minor=1,
							useeditor='source',
							preload='Template:__DIR__/__PRELOAD__/' .. self:msg('testcases-results-name'),
							editintro='Template:__DIR__/__EDITINTRO__/' .. self:msg('testcases-results-name'),
							summary=self:msg('test-results-create-summary', self.title),
						},
					},
			},
			{ 
				self.testcases, 
				self:msg('test-create-text'), 
				self:msg('test-create-title'), 
				query={
					action='edit',
					redlink=1,
					minor=1,
					useeditor='source',
					preload='Template:__DIR__/__PRELOAD__/' .. self:msg('testcases-name'),
					editintro='Template:__DIR__/__EDITINTRO__/' .. self:msg('testcases-name'),
					summary=self:msg('test-create-summary', self.title),
				}
			}
		}
		
		self.noticeConditions = {
			protected = self.invokedTitleObj.protectionLevels.edit and self.invokedTitleObj.protectionLevels.edit[1] == 'sysop',
		}
	end,
	
	buildMainBox = function (self)
		local inst = self.html
			:addClass('hsw-documentation')
			:tag('div')
				:addClass('color1 hsw-documentation-titlebox')
		
		if self.type == self:msg('type-module') then
			inst:tag('span')
				:addClass('hsw-documentation-jtc')
				:wikitext('(', 
					string.makeLink('#code', string.makeTitle(self:msg('jump-text'), self:msg('jump-title'), { disableAbbr=true })),
				')')
			:done()
		end
		
			inst:tag('span')
					:addClass('hsw-documentation-icon')
					:wikitext(string.makeImage(self:msg('doc-image'), { link='', size=60 }))
				:done()
				:tag('span')
					:attr{ id='header' }
					:addClass('hsw-documentation-header')
					:wikitext(self:msg('header-text'))
				:done()
				:tag('span')
					:addClass('hsw-documentation-actions')
					:wikitext(self:linksToList(self.subpageExists and self.links.pageTools[1] or self.links.pageTools[2]))
				:done()
		
		if self.type == self:msg('type-template') then
			inst:tag('div')
				:addClass('hsw-documentation-tnote')
				:tag('b'):wikitext(self:msg('note'), ':&nbsp;'):done()
				:wikitext(self:msg('template-note'))
			:done()
		end
		
			inst = inst:tag('hr')
					:addClass('page-header__separator')
				:done()
				:tag('div')
					:addClass('hsw-documentation-tools')
					:tag('p')
						:wikitext(
							string.wrapTag({ self:msg('page-tools'), ': '} , 'b'), 
							(table.concat(table.merge({
								self.sandboxObj.exists 
									and self:linksToList(self.links.sandbox) 
									or self:parseLinkEntry(self.createSandbox, true),
							}, self:linksToList(self.links.tools, true)), sep))
						)
					:done()
				:done()
				:tag('hr')
					:addClass('page-header__separator')
				:done()
				:tag('div')
					:addClass('hsw-documentation-links')
					:tag('p')
						:wikitext(
							string.wrapTag({ self:msg('page-links'), ': '}, 'b'), 
							self:linksToList(self.links.pageLinks, true)
						)
					:done()
				:done()
			:done()
			:tag('div')
				:addClass('hsw-documentation-body')
				:wikitext(
					self.subpageExists and
						mw.getCurrentFrame():newChild{ title=self.doc }:preprocess(self.noticeStr..self.subpageContent)
					or
						table.concat{ 
							string.wrapHtml(
								{
									self:msg('no-exist-message'), '&nbsp;',
								},
								'<strong>', {
									class='error'
								}
							),
							string.wrapTag({ '(', string.fullUrl(self.doc, self.createDocQuery, self:msg('main-create-text')), ')', }, 'strong'),
						}
				)
				:wikitext(not self.subpageExists and table.concat{ '[[', self:msg('no-exist-cat'), ']]' }  or '')
				:tag('span')
					:addClass('hsw-documentation-main-idk')
					:wikitext('[[', self.doc, ']]')
				:done()
				-- To Make sure the contents of the box does not overflow
				:tag('div')
					:addClass('hsw-documentation-main-pd')
				:done()
			:done()
			:tag('div')
				:addClass('color1 hsw-documentation-bottombox')
				:tag('span')
					:addClass('hsw-documentation-hdtw')
					:wikitext(string.makeLink({ self:msg('hdtw-name') }, self:msg('hdtw-text')))
				:done()
				:tag('span')
					:addClass('hsw-documentation-otls')
					:css{
						['margin-left']=self.titleObj.exists and '13%' or '23%';
					}
					:wikitext(self.type == self:msg('type-module') and string.wrapTag({ self:msg('other-tools'), ': ' }, 'b') or '')
					:wikitext(
						self.type == self:msg('type-module') and (
							self.testcasesObj.exists
								and self:linksToList(self.links.testcases[1]) 
								or self:parseLinkEntry(self.links.testcases[2], true)
						) or ''
					)
				:done()
				:tag('span')
					:addClass('hsw-documentation-btt')
					:wikitext('(', string.makeLink('#header', self:msg('back-to-top')), ')')
				:done()
			:done()
		:allDone()
		
		return inst
	end,
	
	-- Some subpages shouldn't show documentation, since it's never needed and causes needless red links
	checkSkipDocumentation = function (self)
		local skip = false
		-- Only module documentation is automatically shown, so only do the skip check for modules
		if self._type == self:msg('type-module') then
			-- sandboxes / testcases are standardized subpages each module can have, but never need documentation
			if self._title:find('/sandbox$')
				or self._title:find('/testcases$')
				-- These pages only contain data tables - any info about them should just be included on the parent module
				or self._title:find('/Aliases$')
				or self._title:find('/Data$')
				or self._title:find('^Sandbox/') -- don't add doc pages for sandbox module subpages
			then
				skip = true
			end
		end
		
		if skip then
			-- if it has a documentation page show it anyways (to allow bypassing the skip)
			local docTitle = table.concat{ self._type, ':', self._title, '/', self:msg('subpage-documentation') }
			skip = not existsWithoutWanted(docTitle)
		end
		
		return skip
	end,
	
	__tostring = function (self)
		return self.ret
	end,
	
	__concat = function (a, b)
		if a == self then
			return self.ret..b
		else
			return b..self.ret
		end
	end,
})

return Documentation
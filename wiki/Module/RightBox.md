local loader = require('Module:Loader')

local string, table, yesno, lu, arguments = loader.require('String', 'Table', 'Yesno', 'LibU', 'Arguments')

local getArgs = arguments.getArgs
local mapNamedArgs = arguments.mapNamedArgs
local mergeArgsSyntax = arguments.mergeArgsSyntax

local p = {}

local fullurl = mw.uri.fullUrl
local currentTitleObj = mw.title.getCurrentTitle()
local fullpagename = currentTitleObj.fullText

local dot = '<span class=\"bull-c\"></span>'

local function createBox(...)
	local variant, content, options = lu.checkArgs({ 'string', 'table', { 'table', nilOk = true } }, ...)
	options = options or {}
	options.top = options.top or {}
	
	if variant == 'small' then
		local separator = mw.html.create('div')
			:addClass('hsw-rightbox-sep')
			:css(options.top.style or {})
			:wikitext(string.parseDualArg(content.top))
		
		local box = mw.html.create('div')
			:addClass('noprint hsw-rightbox small')
			:node(separator)
			:wikitext(
				options.listTable and string.wrapHtml(table.map(content.list, function(v)
					return string.wrapHtml(v, 'li', options.listRow)
				end), 'ul', options.list) or string.parseDualArg(content.body)
			)
		
		return box
		
	elseif variant == 'medium' then
		local box = mw.html.create('table')
			:attr({ 
				cellpadding = 0;
				cellspacing = 0;
			})
			:addClass('wikitable hsw-rightbox medium')
		
		local row = box:tag('tr')
			if content.image then
				row:tag('td')
					:addClass(type(options.top.class) == 'table' and table.concat(options.top.class) or options.top.class)
					:addClass('hsw-rightbox-image')
					:css(options.top.style)
					:wikitext(string.makeImage(content.image, { size = content.imageSize or 30 }))
				:done()
			end
			
			row:tag('td')
				:addClass('hsw-rightbox-content')
				:wikitext(options.listTable and content.top .. string.wrapHtml(table.map(content.list, function(v)
					return string.wrapHtml(v, 'li', { style = options.listRow.style, class = options.listRow.style })
				end), 'ul', { style = options.list.style, class = options.list.style }) or string.parseDualArg(content.body))
			:done()
		row:done()
		
		return box
	end
end
p.createBox = createBox

function p.luaBox(frame)
	local args = getArgs(frame)
	
	local list = {}
	local l = mergeArgsSyntax(args)
	for i = 1, #l, 1 do
		list[#list+1] = string.wrapHtml(
			{
				string.makeLink({ 'Module:', l[i] }),
				'&nbsp;(',
				string.fullUrl({ 'Module:', l[i]:gsub(' ', '_'), '' }, { action = 'edit' }, string.wrapHtml('e', 'abbr', { title = 'Edit' })),
				dot,
				string.fullUrl({ 'Module:', l[i]:gsub(' ', '_'), '/sandbox' }, nil, string.wrapHtml('s', 'abbr', { title = 'Sandbox' })),
				')',
			}, 'li', { class = 'hsw-luabox-actions' }
		)
	end
	
	
	list = table.concat{
		'Invokes ',
		string.makeLink('Help:Lua', 'Lua'),
		':',
		string.wrapHtml(list, 'ul', {
			class = 'hsw-luabox-list'
		}),
	}
	
	local box = mw.html.create('table')
		:attr({ 
			cellpadding = 0,
			cellspacing = 0,
			class = 'hsw-luabox',
			role = 'note',
		})
	
		local row = box:tag('tr')
			row:tag('td')
				:addClass('hsw-luabox-icon')
				:wikitext(string.makeImage('Lua icon.png', { size = '35px' }))
			:done()
		
			row:tag('td')
				:addClass('hsw-luabox-content')
				:wikitext(list)
			:done()
		row:done()
	box:done()
	
	return frame:preprocess(tostring(box))
end

function p.userboxList(frame)
	local args = getArgs(frame)
	
	local list = {}
	local l = mergeArgsSyntax(args)
	for i = 1, #l, 1 do
		list[i] = string.wrapHtml{
			{
				string.wrapHtml{ l[i], 'td', { class = 'hsw-userbox-list' } }
			},
			'tr',
		}
	end
	
	return table.concat(list, '')
end

function p.shortcut(frame)
	local args = getArgs(frame)
	local list = mergeArgsSyntax(args)
	
	return p._shortcut(list)
end

function p.templateShortcut(frame)
	local args = getArgs(frame)
	local list = mergeArgsSyntax(args)
	
	return p._shortcut(list, true)
end

function p._shortcut(list, isTemplate)
	lu.checkType(1, list, 'table')
	
	for i = 1, #list, 1 do
		title = mw.title.new(isTemplate and 'Template:' .. list[i] or list[i])
		pagename = title.fullText
		local exists = title.exists
		
		list[i] = string.wrapHtml{
			{
				isTemplate and mw.text.nowiki('{{') or '',
				string.fullUrl(title.fullText, exists and {
					redirect = 'no',
				} or {
					action = 'edit',
					redlink = 1,
					preload = 'Template:Shortcut/preload', 
					['preloadparams[]'] = isTemplate and fullpagename:gsub('/doc$', '') or fullpagename:gsub('^Project Seria Caveblock Wiki:', 'Project:'),
				}, string.wrapHtml{
					list[i],
					'font', { 
						style = { color = not exists and '#e81a3f' or nil }, 
						title = exists and pagename or pagename .. ' (page does not exist)',
					},
				}),
				isTemplate and mw.text.nowiki('}}') or '',
			}, 'div', {
				class = 'hsw-shortcut-list',
			}
		}
		
	end
	
	local box = createBox('small', {
		top = string.makeLink(isTemplate and 'Template:Template shortcut' or 'Template:Shortcut', { '<b>', isTemplate and 'Template Shortcut' or 'Shortcut', #list > 1 and 's' or '', '</b>' }),
		list = list,
	}, {
		listTable = true,
		listRow = {
			style = {
				margin = 0,
			},
		},
		list = {
			style = {
				margin = 0,
				['list-style-type'] = 'none',
			},
		},
	})
	
	return tostring(box)
end

function p.archivesBox(frame)
	local args = getArgs(frame, { removeBlanks = false })
	
	local titles = mapNamedArgs(args, 'title')
	local list = mapNamedArgs(args)
	local showSearchBox = yesno(args['searchbox'], args['search'] or args['s'] or args['shows'], false)
	
	local floatAliases = {
		['r'] = 'right';
		['ri'] = 'right';
		['rig'] = 'right';
		['righ'] = 'right';
		['right'] = 'right';
		
		['l'] = 'left';
		['le'] = 'left';
		['lef'] = 'left';
		['left'] = 'left';
	}
	
	local ret = mw.html.create('table')
		:attr({
			cellspacing = '0';
			cellpadding = '5px';
		})
		:addClass('hsw-archivebox')
		:css('float', floatAliases[(args['float'] or args['f'] or args['flo'] or ''):lower()] or 'right')
		:tag('tr')
			:tag('th')
				:addClass('hsw-archivebox-header')
				:wikitext(string.wrapHtml{
					{
						string.wrapHtml{
							'Archives',
							'big',
						},
						string.wrapHtml{
							'[[HSW:Archives|?]]',
							'sup',
						},
					},
					'div',
					{ class = 'hsw-archivebox-content' }
				})
			:done()
		:done()
	
	for i = 1, #list, 1 do
		local title = titles['title' .. i] ~= '' and titles['title' .. i] or nil
		local archivesText = table.concat{
			(title 
				and string.wrapHtml{
					{ '<b>', title, '</b>' },
					'div',
					{ class = 'hsw-archivebox-text' }
				}
				or ''
			),
			args[i],
		}
		
		ret:tag('tr')
			:tag('td')
				:addClass('hsw-archivebox-list')
				:wikitext(archivesText)
			:done()
		:done()
		
		if i == #list and showSearchBox then
			ret:tag('tr')
				:tag('td')
					:addClass('hsw-archivebox-search')
					:wikitext(frame:preprocess([[<inputbox>
bgcolor=transparent
type=fulltext
prefix={{FULLPAGENAMEE}}
break=no
width=11
searchbuttonlabel=Search
placeholder=Search archives
</inputbox>]]))
				:done()
			:done()
		end
	end
	
	return ret:done()
end

function p.archivesList(frame)
	local args = getArgs(frame);
	local i = 1;
	local list = {};
	local sep = args['sep'] or args['s']
	local pagename = args[1] or args['page'] or args['p'] or fullpagename
	
	local titles = {}
	local currentTitle = table.concat{ pagename, '/Archive ', i }
	
	while lu.existsWithoutWanted(currentTitle) do
		table.push(titles, mw.title.new(currentTitle))
		i = i + 1
		currentTitle = table.concat{ pagename, '/Archive ', i }
	end
	
	local limit = tonumber(args[2] or i-1);
	
	--Errors
	if limit == 0 then
		return string.error('No Archives Found')
	elseif limit >= i then 
		return string.error('Limit must not be greater that the number of archives, got %d', limit) 
	elseif limit <= 0 then
		return string.error('Limit must not be less than 1, got %d', limit) 
	end
	
	for j = (limit ~= 0 and i-limit or 1), i-1, 1 do
		list[#list+1] = string.wrapHtml{
			{
				'[[',
				table.concat{ pagename, '/Archive ', j },
				'|Archive ',
				j,
				']]',
				string.wrapHtml{
					{
						' (',
						string.fullUrl(
							{ pagename, '/Archive ', j }, 
							{ ['action'] = 'edit' }, 
							string.wrapHtml{
								'edit',
								'span',
								{
									title = { 'Edit the Talk Archive #', j, ' of ', pagename}
								}
							}
						),
						dot,
						string.fullUrl(
							{ pagename, '/Archive ', j }, 
							{ ['action'] = 'history' }, 
							string.wrapHtml{
								'hist',
								'span',
								{
									title = { 'View the history for the Talk Archive #', j, ' of ', pagename}
								}
							}
						),
						')',
					},
					'span',
					{
						class = 'hsw-archivelist-actions'
					}
				},
			},
			'<span>',
			{
				style = args['style' .. j] or args['s' .. j];
				class = (args['class' .. j] or args['c' .. j] or '') .. ' hsw-archivelist-content';
				id = args['id' .. j];
			}
		}
	end
	
	return string.wrapHtml{table.concat(list, sep or '<br>'), 'span', { class = 'hsw-archivelist' }}
end

function p.archiveNav(frame)
	local function link(name, n)
		local f = name .. '/Archive ' .. n
		if lu.existsWithoutWanted(f) then
			return ('[[%s|Archive %s]]'):format(f, n)
		end
	end
	local args = getArgs(frame)
	local name, i = fullpagename:match('^(.-)/Archive (%d+)$')
	i = tonumber(i)
	if not i then
		return '\'\'It seems that this page is not an archive.\'\''
	end
	local links = { (': < [[%s|Back to the Current Talk Page]]'):format(name) }
	local pg = link(name, i - 1)
	if pg then table.push(links, '< ' .. pg) end
	pg = link(name, i + 1)
	if pg then table.push(links, '> ' .. pg) end
	return table.concat(links, '<br>')
end

return p
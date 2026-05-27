local table, Class, libU = require('Module:Table'), require('Module:Class'), require('Module:LibU')
local require, pcall, type, _G, debug, mw = require, pcall, type, _G, debug, mw
local checkType, checkArgs, assertTrue, assertFalse, makeCheckSelfFunction =
	libU.checkType, libU.checkArgs, libU.assertTrue, libU.assertFalse, libU.makeCheckSelfFunction
local makeCheckSelfFunction, forEachArgs = libU.makeCheckSelfFunction, libU.forEachArgs

local dpl, json

local p = {}
_G.loader = p
p.registry = _G.loader.registry or {}
p.proxyregistry = _G.loader.proxyregistry or {}
local loadable = table.Set{
	'bit32',
	'libraryUtil',
	'ustring',
	'luabit.hex',
	'luabit.bit',
}
local stack, moduleName = _G.loader.stack, _G.loader.moduleName
p.stack = stack
if not _G.loader.stack then
	_G.loader.stack = table.slice(mw.text.split(debug.traceback(''), '\n\t'), 2)
	_G.loader.moduleName = (not loader.stack[2]:match('mw.lua:487:') and loader.stack[3] or loader.stack[1]):match('^(.+):%d+:.+')
	stack, moduleName = _G.loader.stack, _G.loader.moduleName
end

local function formatError(e, module, path)
	if type(e) ~= 'string' then return nil end
	
	if e:match('not found') then return ('Module %q was not found (in path %q)'):format(module, path)
	elseif e:match('loop') then return ('Loop or previous error loading module %q'):format(module)
	elseif e:match('^[Mm]odule:') then return ('Exception in loading module %q at line %s: %s'):format(module,  e:match('^%w+:%w+:(%d+)'), e:gsub('^%w+:%w+:%d+:%s*', ''))
	else return e
	end
end
local function formatDataLoadError(e, module, path)
	if type(e) ~= 'string' then return nil end
	
	if e:match('not found') then 
		return ('Module %q was not found (in path %q)'):format(module, path)
	elseif e:match('unsupported') then
		return ('The data from module %q contains an unsupported data type %q'):format(module, e:match('unsupported data type [\"\'](.-)[\"\']'))
	elseif e:match('metatable') then
		return ('The data from module %q contains a table with a metatable'):format(module, e:match('unsupported data type [\"\'](.-)[\"\']'))
	elseif e:match('loop') then 
		return ('Loop or previous error loading module %q'):format(module)
	end
end

---------------------------------------------------------------------------------
-- For lazy loading modules
-- Thanks to Pythians for helping figure this out. Code referenced:
-- https://pythians.github.io/blogs/2020-12-28-lua-lazy-loader/
---------------------------------------------------------------------------------
local proxyId = {}
local makeProxy
do -- scope for proxy function
	local checkIndex = function(t)
		local pIndex = rawget(t, proxyId)
		if type(pIndex) == 'table' and pIndex.__need_load__ then
			local chunk
			if p.registry[pIndex.__path__] then
				chunk = p.registry[pIndex.__path__]
			else
				chunk = pIndex.__method__(pIndex.__path__)
				p.registry[pIndex.__path__] = chunk
			end
			if (type(chunk) == 'table' or type(chunk) == 'function') then
				rawset(t, proxyId, chunk)
			else
				rawset(t, proxyId, { value = chunk })
			end
		end
	end
	local function for_iter(a, i)
		i = i + 1
		local v = a[i]
		if v then return i, v end
	end
	local mt = {
		__index = function(t, k)
			checkIndex(t)
			local imt = getmetatable(rawget(t, proxyId))
			if imt and imt.__index then
				return imt.__index(rawget(t, proxyId), k)
			else
				return rawget(t, proxyId)[k]
			end
		end,
		__newindex = function(t, k, v)
			checkIndex(t)
			local imt = getmetatable(rawget(t, proxyId))
			if imt and imt.__newindex then
				imt.__newindex(rawget(t, proxyId), k, v)
			else
				rawget(t, proxyId)[k] = v
			end
		end,
		__pairs = function(t)
			checkIndex(t)
			local imt = getmetatable(rawget(t, proxyId))
			if imt and imt.__pairs then
				return imt.__pairs(rawget(t, proxyId))
			else
				return next, rawget(t, proxyId), nil
			end
		end,
		__ipairs = function(t)
			checkIndex(t)
			local imt = getmetatable(rawget(t, proxyId))
			if imt and imt.__ipairs then
				return imt.__ipairs(rawget(t, proxyId))
			else
				return for_iter, rawget(t, proxyId), 0
			end
		end,
		__call = function(t, ...)
			checkIndex(t)
			local imt = getmetatable(rawget(t, proxyId))
			if imt and imt.__call then
				return imt.__call(rawget(t, proxyId), ...)
			else
				return rawget(t, proxyId)(...)
			end
		end,
	}
	-- function export from scope
	makeProxy = function(path, method)
		return setmetatable({
			[proxyId] = {
				__need_load__ = true,
				__path__ = path,
				__method__ = method,
			}
		}, mt)
	end
end

---------------------------------------------------------------------------------
-- Helper function to create a require function
---------------------------------------------------------------------------------
local function createRequireFunc(basePath, isData, lazy)
	local function requireSingle(i, path, args)
		local oldPath = path
		assertTrue(path ~= '', 'Path may not be empty (in argument #%d)', 4, i)
		path = p.resolvePath(path, basePath or moduleName)
		if lazy then
			if p.proxyregistry[path] then
				args[i] = p.proxyregistry[path]
			else
				args[i] = makeProxy(path, isData and mw.loadData or require)
				p.proxyregistry[path] = args[i]
			end
		else
			if p.registry[path] then
				args[i] = p.registry[path]
			else
				args[i] = (isData and mw.loadData or require)(path)
				p.registry[path] = args[i]
			end
		end
	end
	return function(...)
		local args = { ... }
		local ret = {}
		local options
		local doUnpack = true
		if type(args[1]) == 'table' then 
			args = args[1] 
			doUnpack = false
		end
		if type(args[2]) == 'table' then options = args[2] end
		options = options or {}
		
		if i ~= 1 then
			for i, path in forEachArgs({ 'string', 'table', required=1 }, unpack(args)) do
				requireSingle(i, path, args)
			end
		else
			requireSingle(1, ..., args)
		end
		if doUnpack then
			return unpack(args)
		else
			return args
		end
	end
end

---------------------------------------------------------------------------------
-- Loading Functions
--
-- Loads a list of modules. Accepts relative paths
---------------------------------------------------------------------------------
-- function: .require(...modules: table<string>|string[])
p.require = createRequireFunc(nil, false, false)
-- function: .loadData(...dataModules: table<string>|string[])
p.loadData = createRequireFunc(nil, true, false)
-- Lazyloader:
-- If used on table-like exports (packages or data tables) or function exports, the usage is the same as .require and .loadData.
-- If used on other exports types, the loaded data will be loaded in the "value" field.
p.lazy = {
	-- function: .lazy.require(...modules: table<string>|string[])
	['require'] = createRequireFunc(nil, false, true),
	-- function: .lazy.loadData(...dataModules: table<string>|string[])
	['loadData'] = createRequireFunc(nil, true, true)
}

-- p.load = p.require
-- _G.loadData = p.loadData
---------------------------------------------------------------------------------
-- function: .resolveRelativePath(relativePath: string, basePath: string)
-- 
-- Resolves a relative path based on `basePath`.
---------------------------------------------------------------------------------
function p.resolvePath(relativePath, basePath)
	checkType(1, relativePath, 'string')
	checkType(2, basePath, 'string', true)
	basePath = basePath or moduleName:gsub('^[Mm]odule:', '')
	assertTrue(relativePath ~= '', 'Path may not be empty', 3)
	
	local _ = (basePath:match('^(%w+:)') or relativePath:match('^(%w+:)'))
	local isOtherPrefix = _ ~= 'Module:'
	-- local isOther = loadable[relativePath] or loadable[basePath] or isOtherPrefix
	local prefix = 
		(loadable[relativePath] or loadable[basePath])
			and ''
		or isOtherPrefix 
			and _
		or 'Module:'
	
	relativePath = relativePath:gsub('^'..prefix, '')
	basePath = basePath:gsub('^'..prefix, '')
	
	local stack = mw.text.split(basePath, "/")
	local parts = mw.text.split(relativePath, "/")
	local base = table.deepCopy(stack)
	
	if parts[1]:match"~" or (not table.some(parts, function(_, v) return v == '.' or v == '..' end) and parts[1] ~= '') then 
		parts[1] = parts[1]:gsub("~", '')
		return prefix..table.concat(parts, '/')
	end
	
	for i = 1, #parts, 1 do
		local v = parts[i]:gsub('^%$$', base[1])
		if v ~= "." then
			assertFalse((i > 1 and i < #parts) and v == "", "Invalid path %q: Path level/name must not be empty", 2, relativePath)
			if v == ".." then
				table.pop(stack)
			elseif v ~= "" then
				table.push(stack, v) 
			end
		elseif #base > 1 then
			table.pop(stack)
		end
	end
	
	return prefix..table.concat(table.map(stack, function(v, i)
		return v:gsub('^#$', stack[i-1] or stack[1])
	end), '/');
end

---------------------------------------------------------------------------------
-- function: getModuleNames(namespace?: string)
-- 
-- Lists all the availble modules to load.
---------------------------------------------------------------------------------
function p.getModuleNames(namespace)
	if not dpl then dpl = p.require('Module:DPL') end -- lazy-load
	
	return dpl.list{
		namespace=namespace or 'Module',
	}
end

---------------------------------------------------------------------------------
-- function: getRegistry(lazy: boolean)
-- 
-- Gets the loader's registry
---------------------------------------------------------------------------------
function p.getRegistry(lazy)
	return p.registry
end

---------------------------------------------------------------------------------
-- Helper class for manually registered modules
---------------------------------------------------------------------------------
do
	local Module = {}
	local checkSelf = makeCheckSelfFunction(Module, namespace or 'module')
	
	function Module:addExport(...)
		checkSelf(self)
		local name, payload = checkArgs({ 'string', { 'any' } }, ...)
		self.exports[name] = payload
		return payload
	end
	
	function Module:addExports(...)
		checkSelf(self)
		local exports = checkArgs({ 'table' }, ...)
		
		for name, value in pairs(exports) do
			self:addExport(name, value)
		end
		
		return exports
	end
	
	function Module:constructor(path)
		self.path = path
		self.exports = {}
	end
	
	p.Module = Class.makeClass(Module)
end

---------------------------------------------------------------------------------
-- function: register(path: string, payload: function)
-- 
-- Registers a module to the registry.
---------------------------------------------------------------------------------
function p.register(...)
	local path, payload, namespace = checkArgs({ 'string', 'function', { 'string', nilOk=true } }, ...)
	
	path = path:gsub('^[Mm]odule:', '')
	local oldPath = path
	path = p.resolvePath(path)
	local module = p.Module(path)
	
	local success, res = pcall(payload, createRequireFunc(path), module)
	if res == nil then res = 'unknown error' else res = tostring(res) end
	
	assertTrue(success, 'Exception in registring module %q%s: %s', 2, path, res:match('^%w:%d+:') and (' in %s at line %s'):format(res:match('^(.-):%d+:'), res:match('^.-:(%d+):')) or '', res:gsub('^(.-):%d+:%s*', ''))
	p.registry[path] = module.exports
	return module.exports
end

loader.titleCache = {}

---------------------------------------------------------------------------------
-- function: getSubfiles(dir: string, recurse?: boolean)
-- 
-- Reads a directory.
---------------------------------------------------------------------------------
function p.getSubfiles(...)
	if not dpl then dpl = p.require('Module:DPL') end -- Lazy-load
	
	local dir, recurse = checkArgs({ 'string', { 'boolean', nilOk=true } }, ...)
	assertTrue(dir ~= '', 'path may not be empty', 2)
	
	local oldDir = dir
	dir = p.resolvePath(dir)
	local results = table.filter(dpl.getSubpages(dir, recurse), function(v) return v ~= '' end)
	local titleObj = loader.titleCache[dir] or mw.title.new(dir)
	loader.titleCache[dir] = titleObj
	
	assertTrue(#results ~= 0 or titleObj.exists, 'Directory "%s/" not found (in path %q)', 2, dir, oldDir)
	
	return results
end

---------------------------------------------------------------------------------
-- function: readDir(dir: string, options?: table)
-- 
-- Get's the directories subfiles and reads all of them.
---------------------------------------------------------------------------------
function p.readDir(...)
	local dir, recurse, includeFilenames = checkArgs({ 'string', { 'table', nilOk=true } }, ...)
	local ret = {}
	dir = p.resolvePath(dir)
	
	for _, fname in ipairs(p.getSubfiles(dir, recurse)) do
		ret[fname] = p.readFile(fname)
	end
	
	return ret
end

---------------------------------------------------------------------------------
-- function: readFile(...directories: string)
-- 
-- Gets the contents of a file (Already existing on-wiki).
---------------------------------------------------------------------------------
function p.readFile(...)
	local doUnpack = true
	local args = { ... }
	
	if type(args[1]) == 'table' then 
		args = args[1] 
		doUnpack = false
	end
	
	for i, path in forEachArgs({ 'string', required=1 }, unpack(args)) do
		path = p.resolvePath(path)
		local title = loader.titleCache[path] or mw.title.new(path)
		loader.titleCache[path] = title
		
		assertTrue(title.exists, 'Module %q not found', 2, path)
		
		args[i] = title:getContent()
	end
	
	if doUnpack then
		return unpack(args)
	else
		return args
	end
end

---------------------------------------------------------------------------------
-- function: loadFile(...directories: string)
-- 
-- Loads a number of files on wiki. 
--  *If the file is a .json file, it parses it.
--  *if the file is a lua module, it runs it.
---------------------------------------------------------------------------------
function p.loadFile(...)
	local args = { ... }
	local oldPaths = { ... }
	local doUnpack = true
	local t = table.mapWith({ ... }, function(_, v) return p.resolvePath(v) end)
	
	if type(args[1]) == 'table' then 
		args = args[1] 
		doUnpack = false
	end
	
	for i, path in forEachArgs({ 'string', required=1 }, unpack(t)) do
		if path:match('%.json$') then
			if not json then json = p.require('Module:JSON') end -- Lazy-load
			
			local success, res = pcall(json.decode, p.readFile(path))
			
			assertTrue(success, 'Invalid file json from file %q: %s', 2, path, tostring(res):gsub('^Module:%w+:%d+:%s*', ''))
			args[i] = res
		elseif path:match('^Module:') then
			local success, res = pcall(p.require, oldPaths[i])
			
			assertTrue(success, res, 2)
		else
			local title = loader.titleCache[path] or mw.title.new(path)
			loader.titleCache[path] = title
			
			assertTrue(title.exists, 'File %q not found', 2, path)
			args[i] = title:getContent()
		end
		p.registry[path] = args[i]
	end
	
	if doUnpack then
		return unpack(args)
	else
		return args
	end
end

---------------------------------------------------------------------------------
-- function: loadDir(dir: string, options?: table)
-- 
-- Loads and evaluates a directory.
---------------------------------------------------------------------------------
function p.loadDir(...)
	local dir, recurse, includeFilenames = checkArgs({ 'string', { 'table', nilOk=true } }, ...)
	local ret = {}
	dir = p.resolvePath(dir)
	
	for _, fname in ipairs(p.getSubfiles(dir, recurse)) do
		ret[fname] = p.loadFile(fname)
	end
	
	return ret
end

---------------------------------------------------------------------------------
-- function: removeModule(...paths: string)
-- 
-- Removes modules from the registry.
---------------------------------------------------------------------------------
function p.removeModule(...)
	local removed = {}
	for _, path in forEachArgs({ 'string', required=1 }, ...) do
		path = p.resolvePath(path)
		
		assertTrue(p.registry[path], 'Module %q not found in module registry', 2, path)
		
		removed[path] = p.registry[path]
		p.registry[path] = nil
	end
	return removed
end

---------------------------------------------------------------------------------
-- function: requireDir(dir: string, recurse?: boolean)
-- 
-- Loads a directory.
---------------------------------------------------------------------------------
function p.requireDir(...)
	local dir, recurse = checkArgs({ 'string', { 'boolean', nilOk=true } }, ...)
	
	assertTrue(dir ~= '', 'path may not be empty', 2)
	local results = p.getSubfiles(dir, recurse)
	return p.require(unpack(results))
end

return p
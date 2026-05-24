---------------------------------------------------------------------------------
-- From MediaWiki source file
-- and https://hypixel-skyblock.fandom.com/wiki/Module:LibraryUtil
-- 
-- On import, this script exposes all functions to the global table (_G)
-- so that the following functions are accessible everywhere solely through the function name:
-- function: getCodeLocation(level)
-- function: makeArgNumber(val)
-- function: getParentName(level) [alias: getStackName]
-- function: typeMatches(valType, val, types, nilOk, numberOk)
-- function: generateMsg(name, index, msg, types)
-- function: validateTypes(types)
-- function: checkType(name?: string, pos: number, value: any, types: string|table, nilOk?: boolean)
-- function: checkType(name: 'no value', pos: number, types?: string|table, level?: number)
-- function: checkTypeLight(name, argIdx, arg, expectTypes, nilOk)
-- function: checkArgs(types: table<table<string> | string>, ...arguments?: any) [alias: checkTypeArgs]
-- function: checkTypeMulti(t, types)
-- function: alertDeprecation(name: string, useInstead?: string, level?: number)
-- function: forEachArgs(types: string, ...arguments?: string)
-- function: makeCheckSelfFunction(libraryName: string, varName: string, selfObj?: table, selfObjDesc?: string)
-- function: formattedError(formatStr?: string, level?: number, ...substitions?: string | number)
-- function: formattedAssert(v?: any, formatStr?: string, level?: number, ...substitions?: string | number) [alias: assertTrue]
-- function: assertFalse(v, formatStr, level, ...)
-- function: existsWithoutWanted(title: string) [alias: mw.title.existsWithoutWanted]
-- function: inexpensivePageExists(title: string) [alias: pageExists]
-- function: pipeline(...)
-- function: bind(targetFn: function, ...items?: any)
-- 
-- The following methods are modified to a custom one:
-- function: mw.log(...)
-- function: mw.logObject(...)
-- function: mw.oldLog(...)
-- function: mw.oldLogObject(...)
---------------------------------------------------------------------------------
local libU = require('Module:LibU')

-- Push methods into global table
-- Please refer to Module:LibU for impmlementation
for _, v in ipairs({
	'getCodeLocation',
	'makeArgNumber',
	'getParentName',
	'typeMatches',
	'generateMsg',
	'validateTypes',
	'checkType',
	'checkTypeLight',
	'checkArgs',
	'checkTypeMulti',
	'alertDeprecation',
	'forEachArgs',
	'makeCheckSelfFunction',
	'formattedError',
	'formattedAssert',
	'assertFalse',
	'existsWithoutWanted',
	'inexpensivePageExists',
	'pipeline',
	'bind',
	'getStackName',
	'checkTypeArgs',
	'assertTrue',
	'pageExists',
}) do
	_G[v] = libU[v]
end

return libU

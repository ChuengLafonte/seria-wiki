-- Error signatures should be formatted with keys 'Module/Signature'
-- Formatting: Follow {1} where 1 is the key name. Can use positional keys starting from 1, or string keys,
-- according to what you pass in the 'format' field during exceptions

-- Please provide information on the source of error in your message!
local ErrorSignatures = {
	['Minimap/BadLocation'] = { message='Invalid minimap location: {1}', category='Pages with Invalid Minimap Location' },
	['Minimap/BadCoordinates'] = { message='Invalid minimap coordinates', category='Pages with Invalid Minimap Location' },
	['Statname/BadStat'] = { message='Invalid stat name', category='Pages with Invalid Statname' },
	['Statname/BadType'] = { message='Stat must be a string', category='Pages with Invalid Statname' },
	['Item/ApiDataNotFound'] = { message='Invalid item key: {1}. Aliases can be added to Module:Item/ApiAliases', category='Pages with Invalid Item' },
	['Minion/BadName'] = { message='Invalid minion: {1}', category='Pages with Invalid Minion' },
	['Minion/NotEnoughData'] = { message='Minion missing {type} data: {name}', category='Pages with Invalid Minion' },
}

return {
	ErrorSignatures = ErrorSignatures,
	UnknownErrorSignature = { message='[SafeResponse Unknown]: {1}', category='Pages with script errors' }
}

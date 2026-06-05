local loader = require('Module:Loader')
local table, UIText = loader.lazy.require('Table', 'UIText')
local petItemData = loader.lazy.loadData('Pet Item/Data')

local p = {}

-- Transform all stats based on an op table using the 'statops' field
--[[
	Terms defined for description follows.
	[stable] := a supplied pet stat list
	[sfield] := a particular stat field key representable in a pet stat list
	
	Description of all available ops follows.
	[add sfield val] := add val to sfield
	[mul sfield val] := multiply val to sfield
	[mul_all val] := for all existing field F in stable, multiply val to F
	[add_every_lv sfield val] := add (1 per val levels reached) to sfield
]]
function p._transformStatTable(statTable, petItemName, params)
	local function assignTo(field, value)
		statTable[field] = value
	end
	local params = params or {}
	local level = params.level
	
	local statops = petItemData[petItemName] and petItemData[petItemName].statops or {}
	for _, op in pairs(statops) do
		local opname = op[1]
		if opname == 'add' then
			assignTo(op[2], (statTable[op[2]] or 0) + op[3])
		elseif opname == 'mul' then
			assignTo(op[2], (statTable[op[2]] or 0) * op[3])
		elseif opname == 'mul_all' then
			for k, v in pairs(statTable) do
				assignTo(k, v * 1.333)
			end
		elseif opname == 'add_every_lv' then
			assignTo(op[2], (statTable[op[2]] or 0) + math.floor(level / op[3]))
		end
	end
end

function p.heldItemTooltip(petItemName)
	local petItem = petItemData[petItemName]
	
	local str = '&6Held Item: &' .. UIText.getRarityColor(petItem.rarity, false) .. (petItem['name'] or petItemName)
	
	str = str .. '/&r' .. petItem.tooltip .. '//'
	
	return str
end

function p.getName(petItemName)
	local petItem = petItemData[petItemName]
	return petItem['name'] or petItemName
end

function p.getDescription(petItemName)
	local petItem = petItemData[petItemName]
	return petItem['description']
end

return p
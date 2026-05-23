-- Module:Random — minimal implementation for use in Module:UI and Module:Inventory slot

local p = {}

math.randomseed(mw.site.stats.edits + mw.site.stats.pages + os.time() + math.floor(os.clock() * 1000000000))

-- p.number{min, max} or p.number{max}
-- Called as: random.number{100000000, 999999999}
function p.number(args)
	local first = tonumber(args[1])
	local second = tonumber(args[2])
	if first and second then
		if first > second then first, second = second, first end
		return math.random(first, second)
	elseif first then
		return math.random(1, first)
	else
		return math.random()
	end
end

return p

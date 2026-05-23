-- Module:Currency — minimal stub untuk Module:Inventory slot
-- Hanya menyediakan _newCurrencySlot() yang dibutuhkan

local p = {}

local loader = require('Module:Loader')
local string = loader.require('String')

-- Digunakan oleh Module:Inventory slot untuk mendeteksi slot mata uang
-- Mengembalikan nil jika bukan string mata uang, atau frame table jika ya
function p._newCurrencySlot(s, m, noLink)
	-- Hanya parse jika dimulai dengan angka
	if type(s) ~= 'string' or not s:find('^%s*%d') then return nil end

	local currency, name, img
	if s:find('[Cc]oins?%s*$') then
		s = s:gsub('[Cc]oins?%s*$', '')
		name = 'Coin'; img = 'Coin'
	elseif s:find('[Gg]ems?%s*$') then
		s = s:gsub('[Gg]ems?%s*$', '')
		name = 'Gem'; img = 'Gem'
	elseif s:find('[Bb]its?%s*$') then
		s = s:gsub('[Bb]its?%s*$', '')
		name = 'Bit'; img = 'Bit'
	else
		return nil
	end

	local n = string._toNumber and string._toNumber(string.trim(s)) or tonumber(string.trim(s))
	if not n then return nil end

	return {
		name  = img,
		link  = noLink and '' or name,
		title = tostring(n) .. ' ' .. name .. (n ~= 1 and 's' or ''),
		text  = '',
		num   = n,
		num2  = m and (string._toNumber and string._toNumber(m) or tonumber(m)) or nil,
	}
end

return p

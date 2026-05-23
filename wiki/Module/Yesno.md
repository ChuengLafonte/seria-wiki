-- <pre>
-- Modul untuk memproses input teks boolean-like secara konsisten.


local list_t = {
    true, 'true', 't', 'tru',
    'yes', 'y',
    'on',
    'valid',
    '1', 1
}

local list_f = {
    false, 'false', 'f',
    'no', 'n',
    'not',
    'off',
    '0', 0
}


local function contains(array, value)
    for i=1,#array do
        if array[i] == value then return true end
    end
    return false
end

return function (val, default, nil_default)
    -- If your wiki uses non-ascii characters for any of "yes", "no", etc., you
    -- should replace "val:lower()" with "mw.ustring.lower(val)" in the
    -- following line.

    if not nil_default and default then nil_default = default end
    val = type(val) == 'string' and val:lower() or val

    if val == nil then
        if nil_default then return nil_default else return nil end
    elseif contains(list_t, val) then return true
    elseif contains(list_f, val) then return false
    else return default
    end
end

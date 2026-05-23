-- <pre>
local getArgs = require('Module:Arguments').getArgs
local loader = require('Module:Loader')

local string, table, yesno, color, libU = loader.require('String', 'Table', 'Yesno', 'Color', 'LibU')

-- Converts Aliases into ID's
local skills, aliases = loader.loadData('Skillname/Data', 'Skillname/Aliases')

local pageName = mw.title.getCurrentTitle().text

local p = {}

function p.getSkillName(frame)
	local args = getArgs(frame)
	local skill = args[1]
	local text = args[2]
	
	return p._getSkillName(skill, text, {
		isShort = args.short,
		textOnly = args.textOnly,
		iconOnly = args.iconOnly
	})
end

function p.getSkillNameShort(frame)
	local args = getArgs(frame)
	local skill = args[1]
	local text = args[2]
	
	return p._getSkillName(skill, text, {
		isShort = true,
		textOnly = args.textOnly,
		iconOnly = args.iconOnly
	})
end

function p._getSkillName(skill, text, opts)
	local function _getLink(link)
		local rtName = mw.title.makeTitle(0, link or '') or false
		rtName = rtName and rtName.redirectTarget and rtName.redirectTarget.text or false
		local unfragmentedLink = (link or ''):gsub('^(.-)#.-$', '%1')
		if not (unfragmentedLink == pageName or rtName == pageName or link == 'none') then
			return link
		end -- else return nil
	end
	
	libU.checkType(1, skill, 'string')
	-- libU.checkType(2, text, 'string')
	local isShort, textOnly, iconOnly =
		opts.isShort,
		opts.textOnly,
		opts.iconOnly
	
	local oldSkill = skill
	local skill, tier = skill:match('^(.+) ([%divxIVX]+)$')
	skill = (skill or oldSkill):lower()
	tier = string._toRoman(string._toArabic(tier))
	
	skill = skill:lower():gsub('_', ' ')
	skill = aliases[skill] or skill
	local skill = skills[skill]
	
	if not skill
		then return string.error('Invalid Skill name %q', skill)
	end
	
	local out = {}
	if not yesno(textOnly, false) then
		table.push(out, string.makeImage(skill.icon, {
			size = skill.size or '24x24px',
			link = _getLink(skill.name) or '',
		}))
	end
	if not yesno(iconOnly, false) then
		table.push(out, string.makeLink(skill.name, string.wrapHtml{ {
				color.colorText(skill.color, skill[yesno(isShort, false) and 'nameshort' or 'name']),
				color.colorText(skill.color, text and ('&nbsp;' .. text) or (tier ~= 0 and '&nbsp;' .. tier or ''))
			}, '<span>', {
				class = 'hsw-gamefont',
			}
		}))
	end
	
	return string.wrapHtml{
		table.concat(out, string.wrapHtml{ '&nbsp;', '<span>', { class = 'font-initial' } }),
		'<span>', {
			class = 'txt-nowrap';
		}
	}
end

--------------------------------------------------------------------------------
-- Template: Skill XP
--------------------------------------------------------------------------------
function p.skillXP (frame)
	local args = getArgs(frame)
	
	return p._skillXP(args[1], {
		iconOnly = args.iconOnly,
		textOnly = args.textOnly,
		isShort = args.isShort,
		additive = args.additive
	})
end

function p._skillXP(str, opts)
	str = tostring(str):gsub('[%[%],]', '')
	local num, skill, isPercent
	
	if str:match('%+?(%d[%d%.%-]*)(%%?)%s(.*)') then
		isPercent = str:match('(%%)')
		num, skill = str:match('%+?(%d[%d%.%-]*)%%?%s(.*)')
	else 
		return string.error('Invalid syntax %q', str)
	end
	
	skill = skill:gsub('%sXP$', '')
	
	local showPlus = yesno(opts.additive, true)
	
	local formattedNum
	if num:find("%-") then
		local num1, num2 = num:match("^(%d[%d%.]*)%-(%d[%d%.]*)$")
		if num1 and num2 then
			formattedNum = string._formatNum(num1) .. '-' .. string._formatNum(num2)
		else
			formattedNum = num
		end
	else
		formattedNum = string._formatNum(num)
	end
	
	local sign = ""
	if showPlus and not num:find("%-") then
		local numVal = tonumber(num)
		if numVal and numVal >= 0 then
			sign = "+"
		end
	end
	
	return table.concat{
		color.colorText(
			'Green',
			sign .. formattedNum .. (isPercent and '%' or '')
		),
		'&nbsp;',
		p._getSkillName(skill, 'XP', opts),
	}
end

return p

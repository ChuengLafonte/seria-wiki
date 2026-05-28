import yaml
import re

with open(r"e:\dev\seria-cave\plugins\SeriaCollection\collections\farming.yml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

collections = data["farming"]["collections"]

def strip_tags(s):
    return re.sub(r'<[^>]+>', '', s).strip()

def process_reward(reward_str):
    clean = strip_tags(reward_str).replace('☘', '').replace('🌾', '').strip()
    
    if "Recipe" in clean:
        name = re.sub(r'\s*Recipes?$', '', clean).strip()
        return f"{{ '{name}', type = 'Recipe' }}"
        
    if "Trade" in clean:
        name = re.sub(r'\s*Trade$', '', clean).strip()
        return f"{{ '{name}', type = 'Trade' }}"
        
    if "EXP" in clean:
        match = re.search(r'\+?([\d\.]+)\s+(.*?)\s+EXP', clean)
        if match:
            amt = match.group(1).replace('.', '')
            ctype = match.group(2).strip()
            return f"{{ {amt}, type = '{ctype} Experience' }}"
            
    if "Fortune" in clean:
        match = re.search(r'\+?(\d+)\s+(.*?)\s+Fortune', clean)
        if match:
            amt = match.group(1)
            ftype = match.group(2).strip()
            return f"{{ '{{{{Gold|+{amt}}}}} {{{{G|{ftype} Fortune}}}}', type = 'Custom', nolink = true, rewardstr = '&6+{amt}~~ {ftype} Fortune' }}"
            
    if "Bundle" in clean:
        name = re.sub(r'\s*\[.*?\]', '', clean).strip()
        return f"{{ '{name}', type = 'Reward' }}"
        
    # fallback to Custom
    return f"{{ '{clean}', type = 'Custom', nolink = true, rewardstr = '&7{clean}' }}"

out_lines = []
for cid, cdata in collections.items():
    name = cdata["name"]
    out_lines.append(f"\t['{name}'] = {{")
    
    out_lines.append(f"\t\tminion = '{name}',")
    
    tiers = cdata.get("tiers", {})
    for tier, tdata in sorted(tiers.items(), key=lambda x: int(x[0])):
        req = tdata["requirement"]
        out_lines.append(f"\t\t[{tier}] = {{")
        out_lines.append(f"\t\t\trequired = {req},")
        out_lines.append(f"\t\t\treward = {{")
        
        for r_str in tdata.get("display-rewards", []):
            out_lines.append("\t\t\t\t" + process_reward(r_str) + ",")
            
        out_lines.append(f"\t\t\t}},")
        out_lines.append(f"\t\t}},")
    out_lines.append(f"\t}},")

with open(r"e:\Project Wiki\farming_parsed.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out_lines))

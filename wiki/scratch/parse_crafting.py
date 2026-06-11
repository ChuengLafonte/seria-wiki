import os
import glob
import yaml
import json

def to_title_case(s):
    return ' '.join(word.capitalize() for word in s.split('_'))

def parse_slot_item(item_str):
    item_str = item_str.strip()
    if item_str.startswith('v AIR') or not item_str:
        return None
    
    parts = item_str.split(' ')
    amount = "1"
    name = "Unknown"
    
    try:
        if item_str.startswith('v '):
            material = parts[1]
            name = to_title_case(material)
            # Find the element ending with '..'
            for p in parts:
                if '..' in p:
                    amount = p.split('.')[0]
        elif item_str.startswith('m '):
            if '-' in parts:
                idx = parts.index('-')
                id_part = parts[idx-1]
            else:
                id_part = parts[2]
            name = to_title_case(id_part)
            for p in parts:
                if '..' in p:
                    amount = p.split('.')[0]
    except Exception as e:
        print("Error parsing:", item_str, e)
        
    if amount.isdigit() and int(amount) > 1:
        return f"{name},{amount}"
    return name

lua_table = {}

yaml_files = glob.glob(r"e:\Project Wiki\crafting data\*.yml")
for yml_file in yaml_files:
    try:
        with open(yml_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
    except Exception as e:
        print("YAML error in", yml_file, e)
        continue
    
    if not data: continue
        
    for root_key, items in data.items():
        if not isinstance(items, dict): continue
        for item_key, item_data in items.items():
            if not isinstance(item_data, dict): continue
            
            craft_amount = item_data.get('craft-amount', 1)
            output_name = to_title_case(item_key)
            if str(craft_amount) != '1':
                output_val = f"{output_name},{craft_amount}"
            else:
                output_val = output_name
                
            crafting = item_data.get('crafting', {})
            shaped = crafting.get('shaped', {})
            
            frames = []
            
            for shape_key in sorted(shaped.keys(), key=lambda x: int(x) if str(x).isdigit() else str(x)):
                shape_data = shaped[shape_key]
                inputs = shape_data.get('input', [])
                
                rows = inputs + ['v AIR 0 1..|v AIR 0 1..|v AIR 0 1..'] * (3 - len(inputs))
                
                frame_qrs = []
                row_letters = ['A', 'B', 'C']
                for r_idx in range(3):
                    cols = rows[r_idx].split('|')
                    cols = cols + ['v AIR 0 1..'] * (3 - len(cols))
                    for c_idx in range(3):
                        slot_id = f"{row_letters[r_idx]}{c_idx+1}"
                        item_name = parse_slot_item(cols[c_idx])
                        if item_name:
                            frame_qrs.append(f'{slot_id} "{item_name}"')
                
                if frame_qrs:
                    frames.append(" ".join(frame_qrs))
            
            if frames:
                qrs_string = " // ".join(frames)
                if output_val == output_name:
                    lua_table[output_name] = [qrs_string]
                else:
                    lua_table[output_name] = [qrs_string, {"Output": output_val}]

lua_lines = ["return {"]
for k, v in lua_table.items():
    if len(v) == 1:
        lua_lines.append(f"    ['{k}'] = '{v[0]}',")
    else:
        out_val = v[1]["Output"]
        lua_lines.append(f"    ['{k}'] = {{ '{v[0]}', Output = '{out_val}' }},")
lua_lines.append("}")

with open(r"e:\Project Wiki\wiki\Module\Crafting_SLASH_Data.md", "w", encoding='utf-8') as f:
    f.write("\n".join(lua_lines))
print(f"Parsed {len(lua_table)} items.")

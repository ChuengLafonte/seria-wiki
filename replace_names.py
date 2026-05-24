import os
from pathlib import Path

wiki_dir = Path('wiki')
files = list(wiki_dir.glob('**/*.md'))

changed_count = 0

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    # Replace specifically in order
    new_content = new_content.replace('Hypixel SkyBlock', 'Project Seria Caveblock')
    new_content = new_content.replace('Hypixel Skyblock', 'Project Seria Caveblock')
    new_content = new_content.replace('hypixel skyblock', 'Project Seria Caveblock')
    
    new_content = new_content.replace('SkyBlock', 'Project Seria Caveblock')
    new_content = new_content.replace('Skyblock', 'Project Seria Caveblock')
    new_content = new_content.replace('skyblock', 'Project Seria Caveblock')
    
    new_content = new_content.replace('Hypixel', 'Project Seria Caveblock')
    new_content = new_content.replace('hypixel', 'Project Seria Caveblock')
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Modified: {file_path}')
        changed_count += 1

print(f'Done. Changed {changed_count} files.')

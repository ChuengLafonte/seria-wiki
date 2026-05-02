import os
import mwclient
from pathlib import Path

def sync_wiki():
    # Load credentials from environment variables
    username = os.environ.get('FANDOM_USERNAME')
    password = os.environ.get('FANDOM_PASSWORD')
    site_url = 'seria.fandom.com' # Base URL
    
    if not username or not password:
        print("Error: FANDOM_USERNAME or FANDOM_PASSWORD not set.")
        return

    # Connect to Fandom
    site = mwclient.Site(site_url, path='/', clients_useragent='SeriaWikiBot/1.0 (GitHub Action)')
    
    try:
        site.login(username, password)
        print(f"Logged in as {username}")
    except Exception as e:
        print(f"Login failed: {e}")
        return

    # Path to the wiki content
    wiki_dir = Path('wiki')
    if not wiki_dir.exists():
        print("Wiki directory not found.")
        return

    # Iterate through files in the wiki directory
    for file_path in wiki_dir.glob('**/*.md'):
        # Determine page title from filename
        # Example: wiki/Seria_Wiki.md -> Seria Wiki
        relative_path = file_path.relative_to(wiki_dir)
        page_title = str(relative_path.with_suffix('')).replace('_', ' ').replace('\\', '/')
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        print(f"Syncing page: {page_title}...")
        
        page = site.pages[page_title]
        
        # Check if content has changed to avoid unnecessary edits
        if page.text() == content:
            print(f"No changes for {page_title}. Skipping.")
            continue
            
        # Save the page
        page.save(content, summary='Automated sync from GitHub via Antigravity')
        print(f"Successfully updated {page_title}")

if __name__ == "__main__":
    sync_wiki()

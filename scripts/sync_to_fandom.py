import os
import mwclient
from pathlib import Path
import sys

def sync_wiki():
    # Load credentials from environment variables
    username = os.environ.get('FANDOM_USERNAME')
    password = os.environ.get('FANDOM_PASSWORD')
    site_url = 'seria.fandom.com'
    
    print("--- Starting Wiki Sync ---")
    
    if not username or not password:
        print("❌ Error: FANDOM_USERNAME or FANDOM_PASSWORD not set.")
        sys.exit(1)

    # Connect to Fandom
    print(f"Connecting to {site_url}...")
    site = mwclient.Site(site_url, path='/', clients_useragent='SeriaWikiBot/1.0 (GitHub Action)')
    
    try:
        site.login(username, password)
        print(f"✅ Logged in as {username}")
    except Exception as e:
        print(f"❌ Login failed: {e}")
        sys.exit(1)

    wiki_dir = Path('wiki')
    if not wiki_dir.exists():
        print("❌ Wiki directory not found.")
        return

    files_found = list(wiki_dir.glob('**/*.md'))
    print(f"Found {len(files_found)} files to sync.")

    has_errors = False

    for file_path in files_found:
        # Determine page title
        relative_path = file_path.relative_to(wiki_dir)
        # Use underscores as spaces for the title, but clean up path
        page_title = str(relative_path.with_suffix('')).replace('_', ' ').replace('\\', '/')
        
        # If it's in a subdirectory like 'Features/Mining.md', title becomes 'Features/Mining'
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            print(f"🔄 Syncing: [{page_title}]...")
            
            page = site.pages[page_title]
            
            # Get remote content
            remote_content = page.text()
            
            if remote_content == content:
                print(f"⏩ No changes for '{page_title}'. Skipping.")
                continue
                
            # Save the page
            page.save(content, summary='Automated sync from GitHub via Antigravity')
            print(f"✨ Successfully updated '{page_title}'")
            
        except Exception as e:
            print(f"❌ Failed to sync '{page_title}': {e}")
            has_errors = True

    print("--- Sync Finished ---")
    if has_errors:
        sys.exit(1)

if __name__ == "__main__":
    sync_wiki()

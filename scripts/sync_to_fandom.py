import os
import mwclient
from pathlib import Path
import sys
import subprocess

def get_git_modified_files():
    try:
        # Get modified tracked files
        diff_files = subprocess.check_output(['git', 'diff', '--name-only'], text=True).splitlines()
        # Get staged files
        cached_files = subprocess.check_output(['git', 'diff', '--cached', '--name-only'], text=True).splitlines()
        # Get untracked files
        status_files = subprocess.check_output(['git', 'status', '--porcelain'], text=True).splitlines()
        
        untracked_files = []
        for line in status_files:
            if line.startswith('?? '):
                untracked_files.append(line[3:])
                
        all_changed = set(diff_files + cached_files + untracked_files)
        
        # Filter to only include files under 'wiki/' and ending in '.md' and existing
        wiki_changed = []
        for f in all_changed:
            p = Path(f)
            if p.suffix == '.md' and p.exists():
                try:
                    p.relative_to(Path('wiki'))
                    wiki_changed.append(p)
                except ValueError:
                    pass
        return wiki_changed
    except Exception as e:
        print(f"⚠️ Warning: Could not detect changed files via Git ({e}).")
        return None

def sync_wiki():
    # Load credentials from environment variables
    username = os.environ.get('FANDOM_USERNAME')
    password = os.environ.get('FANDOM_PASSWORD')
    site_url = 'seria.fandom.com'
    
    print("--- Starting Wiki Sync ---")
    
    if not username or not password:
        print("❌ Error: FANDOM_USERNAME or FANDOM_PASSWORD not set.")
        sys.exit(1)

    wiki_dir = Path('wiki')
    if not wiki_dir.exists():
        print("❌ Wiki directory not found.")
        sys.exit(1)

    # Determine files to sync
    files_to_sync = []
    args = sys.argv[1:]
    is_ci = os.environ.get('GITHUB_ACTIONS') == 'true'

    if args:
        if '--all' in args:
            print("Mode: Sync all files")
            files_to_sync = list(wiki_dir.glob('**/*.md'))
        else:
            print("Mode: Sync specific files passed as arguments")
            for arg in args:
                p = Path(arg)
                # Ensure it's a markdown file inside wiki directory and exists
                if p.suffix == '.md' and p.exists():
                    try:
                        p.relative_to(wiki_dir)
                        files_to_sync.append(p)
                    except ValueError:
                        pass
    else:
        # No arguments passed
        if is_ci:
            print("Mode: CI (No changed wiki files detected)")
            print("⏩ Nothing to sync. Exiting.")
            sys.exit(0)
        else:
            print("Mode: Local (Detecting modified files via Git...)")
            changed_files = get_git_modified_files()
            if changed_files is not None:
                if changed_files:
                    print(f"Found {len(changed_files)} modified files in Git.")
                    files_to_sync = changed_files
                else:
                    print("No modified wiki files detected in Git.")
                    print("💡 Use 'python scripts/sync_to_fandom.py --all' to sync all files.")
                    sys.exit(0)
            else:
                # Fallback to all files if Git check failed
                print("Falling back to syncing all files.")
                files_to_sync = list(wiki_dir.glob('**/*.md'))

    if not files_to_sync:
        print("⏩ No files to sync. Exiting.")
        sys.exit(0)

    print(f"Syncing {len(files_to_sync)} file(s)...")
    for f in files_to_sync:
        print(f" - {f}")

    # Connect to Fandom
    print(f"Connecting to {site_url}...")
    site = mwclient.Site(site_url, path='/', clients_useragent='SeriaWikiBot/1.0 (GitHub Action)')
    
    try:
        site.login(username, password)
        print(f"✅ Logged in as {username}")
    except Exception as e:
        print(f"❌ Login failed: {e}")
        sys.exit(1)

    has_errors = False

    for file_path in files_to_sync:
        # Determine page title
        relative_path = file_path.relative_to(wiki_dir)
        # Determine namespace from the first folder level
        parts = relative_path.parts
        namespace = ""
        valid_namespaces = ['Template', 'Category', 'Help', 'Project']
        if parts[0] in valid_namespaces:
            namespace = f"{parts[0]}:"
            
        # Determine title purely from the filename (ignoring other local subfolders)
        filename = file_path.stem
        # Restore slashes and spaces
        page_title = filename.replace('_SLASH_', '/').replace('_', ' ')
        page_title = namespace + page_title
        
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

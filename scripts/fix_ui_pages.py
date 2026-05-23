"""
fix_ui_pages.py - Fix Template:UI and upload missing Collection UI sub-pages to Fandom.
Run: python scripts/fix_ui_pages.py
"""
import os
import sys
import mwclient
from pathlib import Path

# ── Config ────────────────────────────────────────────────────────────────────
SITE_URL   = 'seria.fandom.com'
WIKI_DIR   = Path(__file__).parent.parent / 'wiki'

# Exactly which pages to create/update and where to find them locally.
# key   = Fandom page title
# value = path relative to WIKI_DIR
PAGES_TO_FIX = {
    # Fix the broken template (render -> ui)
    'Template:UI': 'Template/Format/UI.md',

    # Missing Collection UI sub-pages
    'Farming/Collection UI':     'Caveblock/Farming_SLASH_Collection UI.md',
    'Mining/Collection UI':      'Caveblock/Mining_SLASH_Collection UI.md',
    'Combat/Collection UI':      'Caveblock/Combat_SLASH_Collection UI.md',
    'Foraging/Collection UI':    'Caveblock/Foraging_SLASH_Collection UI.md',
    'Fishing/Collection UI':     'Caveblock/Fishing_SLASH_Collection UI.md',
    'Bosses/Collection UI':      'Caveblock/Bosses_SLASH_Collection UI.md',
    'Rift/Collection UI':        'Caveblock/Rift_SLASH_Collection UI.md',
    'Crafted Minions/UI':        'Caveblock/Crafted Minions_SLASH_UI.md',

    # Main Collections/UI page (also resync to be safe)
    'Collections/UI':            'Caveblock/Collections_SLASH_UI.md',
}

# ── Helpers ───────────────────────────────────────────────────────────────────

def log_ok(msg):   print(f"[OK]   {msg}", flush=True)
def log_skip(msg): print(f"[SKIP] {msg}", flush=True)
def log_err(msg):  print(f"[ERR]  {msg}", flush=True, file=sys.stderr)
def log_info(msg): print(f"[INFO] {msg}", flush=True)

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    username = os.environ.get('FANDOM_USERNAME')
    password = os.environ.get('FANDOM_PASSWORD')

    if not username or not password:
        log_err("Environment variables FANDOM_USERNAME and FANDOM_PASSWORD are required.")
        log_err("Set them and re-run:  set FANDOM_USERNAME=... && set FANDOM_PASSWORD=...")
        sys.exit(1)

    log_info(f"Connecting to {SITE_URL} ...")
    site = mwclient.Site(SITE_URL, path='/', clients_useragent='SeriaWikiBot/1.0')

    try:
        site.login(username, password)
        log_ok(f"Logged in as {username}")
    except Exception as e:
        log_err(f"Login failed: {e}")
        sys.exit(1)

    errors = []

    for page_title, rel_path in PAGES_TO_FIX.items():
        local_file = WIKI_DIR / rel_path
        if not local_file.exists():
            log_err(f"Local file not found: {local_file}")
            errors.append(page_title)
            continue

        try:
            content = local_file.read_text(encoding='utf-8')
        except Exception as e:
            log_err(f"Cannot read {local_file}: {e}")
            errors.append(page_title)
            continue

        try:
            page = site.pages[page_title]
            remote = page.text()
            if remote == content:
                log_skip(f"'{page_title}' - no changes.")
                continue

            page.save(content, summary='Fix: render->ui + create missing Collection UI sub-pages')
            log_ok(f"Updated '{page_title}'")
        except Exception as e:
            log_err(f"Failed to update '{page_title}': {e}")
            errors.append(page_title)

    print()
    if errors:
        log_err(f"Finished with {len(errors)} error(s): {errors}")
        sys.exit(1)
    else:
        log_ok("All pages updated successfully!")

if __name__ == '__main__':
    main()

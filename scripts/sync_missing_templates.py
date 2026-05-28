import json
import urllib.request
from urllib.error import HTTPError
import os
import mwclient

def get_red_links():
    url = 'https://seria.fandom.com/api.php?action=parse&page=Template:UI&prop=links&format=json'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    res = urllib.request.urlopen(req)
    data = json.loads(res.read().decode('utf-8'))
    links = data['parse']['links']
    red_links = [link['*'] for link in links if 'exists' not in link]
    return red_links

def fetch_from_hypixel(title):
    url = f'https://hypixel-skyblock.fandom.com/api.php?action=query&prop=revisions&titles={urllib.parse.quote(title)}&rvprop=content&rvslots=main&format=json'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        res = urllib.request.urlopen(req)
        data = json.loads(res.read().decode('utf-8'))
        pages = data['query']['pages']
        for page_id in pages:
            if page_id == '-1':
                return None
            return pages[page_id]['revisions'][0]['slots']['main']['*']
    except Exception as e:
        print(f"Error fetching {title} from hypixel: {e}")
        return None

def main():
    username = os.environ.get('FANDOM_USERNAME')
    password = os.environ.get('FANDOM_PASSWORD')

    if not username or not password:
        print("FANDOM_USERNAME or FANDOM_PASSWORD environment variables not set.")
        return

    print("Connecting to Seria Wiki...")
    site = mwclient.Site('seria.fandom.com', path='/')
    site.login(username, password)
    
    red_links = get_red_links()
    targets = [link for link in red_links if link.startswith('Template:') or link.startswith('Module:')]
    
    print(f"Found {len(targets)} templates/modules to copy.")
    
    for title in targets:
        print(f"Fetching {title} from Hypixel...")
        content = fetch_from_hypixel(title)
        
        if content is None:
            print(f"-> {title} does not exist on Hypixel.")
            continue
            
        print(f"-> Found {len(content)} bytes. Uploading to Seria...")
        page = site.pages[title]
        
        for attempt in range(3):
            try:
                # Check if it already has this content
                if page.text() == content:
                    print(f"-> {title} is already up to date.")
                    break
                page.edit(content, summary="Copied from Hypixel Wiki")
                print(f"-> Successfully copied {title}!")
                import time
                time.sleep(3) # Delay between edits
                break
            except Exception as e:
                if 'ratelimited' in str(e):
                    print(f"-> Rate limited. Waiting 60s... (Attempt {attempt+1}/3)")
                    import time
                    time.sleep(60)
                else:
                    print(f"-> Error uploading {title}: {e}")
                    break

if __name__ == '__main__':
    main()

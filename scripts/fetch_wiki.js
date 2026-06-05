const https = require('https');
const fs = require('fs');
const path = require('path');

const WIKI_DIR = path.join(__dirname, '..', 'wiki');
const BASE_URL = 'https://hypixel-skyblock.fandom.com/api.php';

function fetchPage(title) {
    const url = `${BASE_URL}?action=query&prop=revisions&rvprop=content&rvslots=main&format=json&titles=${encodeURIComponent(title)}`;
    
    return new Promise((resolve, reject) => {
        https.get(url, { headers: { 'User-Agent': 'Mozilla/5.0' } }, (res) => {
            let data = '';
            res.on('data', chunk => data += chunk);
            res.on('end', () => {
                try {
                    const json = JSON.parse(data);
                    const pagesData = json.query.pages;
                    for (const pageId in pagesData) {
                        if (pagesData[pageId].revisions) {
                            resolve(pagesData[pageId].revisions[0].slots.main['*']);
                        } else {
                            resolve(null);
                        }
                    }
                } catch (e) {
                    reject(e);
                }
            });
        }).on('error', reject);
    });
}

function categorizeTemplate(title) {
    const rules = [
        { prefix: 'Template:Infobox/', category: 'Infobox' },
        { prefix: 'Template:Navbox', category: 'Navbox' },
        { prefix: 'Template:Nav/', category: 'Navbox' },
        { prefix: 'Template:Cite ', category: 'Cite' },
        { match: (t) => t.endsWith('/doc') || t.includes('Documentation') || t === 'Template:Doc', category: 'Documentation' },
        { match: (t) => ['Template:!', 'Template:=', 'Template:-', 'Template:*', 'Template:Cols', 'Template:Clear', 'Template:Space', 'Template:Trim', 'Template:UI', 'Template:T', 'Template:Tl', 'Template:Tlx'].includes(t), category: 'Format' },
        { match: (t) => ['Template:Ambox', 'Template:MessageBox', 'Template:LicenseBox', 'Template:CC-BY-SA', 'Template:GFDL', 'Template:PD', 'Template:MIT', 'Template:LGPL', 'Template:Fairuse'].includes(t), category: 'Bawaan' }
    ];

    for (const rule of rules) {
        if (rule.prefix && title.startsWith(rule.prefix)) return rule.category;
        if (rule.match && rule.match(title)) return rule.category;
    }
    return 'Lainnya';
}

function getSafeFilePath(title) {
    let safeTitle = title;
    let folder;
    
    if (title.startsWith('Template:')) {
        let category = categorizeTemplate(title);
        folder = path.join(WIKI_DIR, 'Template', category);
        safeTitle = safeTitle.replace(/^Template:/i, '');
    } else if (title.startsWith('Module:')) {
        folder = path.join(WIKI_DIR, 'Module');
        safeTitle = safeTitle.replace(/^Module:/i, '');
    } else if (title.startsWith('MediaWiki:')) {
        folder = path.join(WIKI_DIR, 'MediaWiki');
        safeTitle = safeTitle.replace(/^MediaWiki:/i, '');
    } else if (title.startsWith('Project:')) {
        folder = path.join(WIKI_DIR, 'Project');
        safeTitle = safeTitle.replace(/^Project:/i, '');
    } else {
        // Assume Main namespace, place in root or a specific folder if needed
        // For simplicity, we'll put it in Lainnya if not caught by a graph algorithm
        folder = path.join(WIKI_DIR, 'Lainnya'); 
    }
    
    // Replace colons and slashes
    safeTitle = safeTitle.replace(/:/g, '_COLON_').replace(/\//g, '_SLASH_');
    safeTitle = safeTitle.replace(/\*/g, '_ASTERISK_');
    safeTitle = safeTitle.replace(/[<>:"\\|?*]/g, '_');
    
    return path.join(folder, safeTitle + '.md');
}

async function run() {
    const titles = process.argv.slice(2);
    
    if (titles.length === 0) {
        console.log("Usage: node fetch_wiki.js <PageTitle1> <PageTitle2> ...");
        console.log("Example: node fetch_wiki.js \"Template:Infobox/Item\" \"Module:Zone\"");
        process.exit(1);
    }
    
    for (let title of titles) {
        try {
            console.log(`Fetching ${title}...`);
            const content = await fetchPage(title);
            if (content !== null) {
                const filepath = getSafeFilePath(title);
                fs.mkdirSync(path.dirname(filepath), { recursive: true });
                fs.writeFileSync(filepath, content, 'utf8');
                console.log(`\u2713 Saved to ${filepath}`);
            } else {
                console.log(`\u2717 Failed to fetch ${title} (page not found or no revisions)`);
            }
        } catch (e) {
            console.error(`\u2717 Error fetching ${title}:`, e.message);
        }
    }
}

run();

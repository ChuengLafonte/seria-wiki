const fs = require('fs');
const path = require('path');
const https = require('https');

const WIKI_URL = 'https://seria.fandom.com/api.php';
const WIKI_DIR = path.join(__dirname, '..', 'wiki');

function fetchAPI(params) {
    return new Promise((resolve, reject) => {
        const url = new URL(WIKI_URL);
        const allParams = {
            ...params,
            format: 'json',
            formatversion: 2
        };
        for (const key in allParams) {
            url.searchParams.append(key, allParams[key]);
        }

        https.get(url.toString(), (res) => {
            let data = '';
            res.on('data', (chunk) => { data += chunk; });
            res.on('end', () => {
                try {
                    resolve(JSON.parse(data));
                } catch (e) {
                    reject(e);
                }
            });
        }).on('error', reject);
    });
}

async function getAllPages(namespace) {
    let pages = [];
    let gapcontinue = null;
    
    do {
        const params = {
            action: 'query',
            generator: 'allpages',
            gapnamespace: namespace,
            gaplimit: 50,
            prop: 'revisions',
            rvprop: 'content'
        };
        if (gapcontinue) params.gapcontinue = gapcontinue;
        
        const data = await fetchAPI(params);
        if (data.query && data.query.pages) {
            pages = pages.concat(data.query.pages);
        }
        gapcontinue = data.continue ? data.continue.gapcontinue : null;
    } while (gapcontinue);
    
    return pages;
}

function extractLinks(text) {
    const links = [];
    const regex = /\[\[([^|\]]+)(?:\|[^\]]+)?\]\]/g;
    let match;
    while ((match = regex.exec(text)) !== null) {
        let link = match[1].trim();
        // Capitalize first letter to match wiki title conventions
        if (link.length > 0) {
            link = link.charAt(0).toUpperCase() + link.slice(1);
            links.push(link);
        }
    }
    return links;
}

function categorizeTemplates(pages) {
    const categories = {
        'Infobox': [],
        'Navbox': [],
        'Cite': [],
        'Documentation': [],
        'Format': [],
        'Bawaan': [],
        'Lainnya': []
    };
    
    const rules = [
        { prefix: 'Template:Infobox/', category: 'Infobox' },
        { prefix: 'Template:Navbox', category: 'Navbox' },
        { prefix: 'Template:Cite ', category: 'Cite' },
        { match: (t) => t.endsWith('/doc') || t.includes('Documentation') || t === 'Template:Doc', category: 'Documentation' },
        { match: (t) => ['Template:!', 'Template:=', 'Template:-', 'Template:*', 'Template:Cols', 'Template:Clear', 'Template:Space', 'Template:Trim', 'Template:UI', 'Template:T', 'Template:Tl', 'Template:Tlx'].includes(t), category: 'Format' },
        { match: (t) => ['Template:Ambox', 'Template:MessageBox', 'Template:LicenseBox', 'Template:CC-BY-SA', 'Template:GFDL', 'Template:PD', 'Template:MIT', 'Template:LGPL', 'Template:Fairuse'].includes(t), category: 'Bawaan' }
    ];

    const assignments = {};
    for (const page of pages) {
        let title = page.title;
        let assigned = 'Lainnya';
        for (const rule of rules) {
            if (rule.prefix && title.startsWith(rule.prefix)) {
                assigned = rule.category;
                break;
            }
            if (rule.match && rule.match(title)) {
                assigned = rule.category;
                break;
            }
        }
        assignments[title] = assigned;
    }
    return assignments;
}

function buildGraph(pages) {
    const linksTo = {}; // adjacency list
    const pageMap = {};
    
    for (const page of pages) {
        const title = page.title;
        const text = page.revisions && page.revisions[0] && page.revisions[0].content ? page.revisions[0].content : '';
        const links = extractLinks(text);
        
        linksTo[title] = links;
        pageMap[title] = page;
    }
    
    return { linksTo, pageMap };
}

function categorizeMain(graph) {
    const categories = ['MMORPG', 'Caveblock', 'Survival', 'Skyforge'];
    const assignments = {};
    const { linksTo, pageMap } = graph;
    
    const rootNodes = {
        'MMORPG': ['Bosses & Dungeons', 'Common Weapon Manuscript', 'NPC', 'RPG Crate', 'Aurelium Skill', 'Quest'],
        'Caveblock': ['Cave Block', 'Caveblock', 'Collections', 'Minions', 'Features', 'SeriaCollection', 'SeriaCrafting', 'The Farm'],
        'Survival': ['Survival', 'SURVIVAL'],
        'Skyforge': ['Skyforge']
    };
    
    // Initialize BFS queue
    const queue = [];
    
    for (const cat in rootNodes) {
        for (const root of rootNodes[cat]) {
            if (pageMap[root] || root === 'Collections') {
                assignments[root] = cat;
                queue.push({ node: root, cat });
            }
        }
    }
    
    // Assignments map title to category
    while (queue.length > 0) {
        const { node, cat } = queue.shift();
        const neighbors = linksTo[node] || [];
        
        for (const neighbor of neighbors) {
            if (pageMap[neighbor] && !assignments[neighbor]) {
                assignments[neighbor] = cat;
                queue.push({ node: neighbor, cat });
            }
        }
    }
    
    for (const title in pageMap) {
        if (!assignments[title]) {
            assignments[title] = 'Lainnya';
        }
    }
    
    return assignments;
}

function writePage(title, content, category, isTemplate, namespaceName) {
    let safeTitle = title;
    let folder;
    
    if (isTemplate) {
        let subFolder = category;
        folder = path.join(WIKI_DIR, 'Template', subFolder);
        safeTitle = safeTitle.replace(/^Template:/i, '');
    } else if (namespaceName === 'Module') {
        folder = path.join(WIKI_DIR, 'Module');
        safeTitle = safeTitle.replace(/^Module:/i, '');
    } else if (namespaceName === 'MediaWiki') {
        folder = path.join(WIKI_DIR, 'MediaWiki');
        safeTitle = safeTitle.replace(/^MediaWiki:/i, '');
    } else if (namespaceName === 'Project') {
        folder = path.join(WIKI_DIR, 'Project');
        safeTitle = safeTitle.replace(/^(Project Seria Wiki|Project):/i, '');
    } else {
        folder = path.join(WIKI_DIR, category);
    }
    
    // Replace colons and slashes
    safeTitle = safeTitle.replace(/:/g, '_COLON_').replace(/\//g, '_SLASH_');
    // Replace invalid windows characters
    safeTitle = safeTitle.replace(/[<>:"\\|?*]/g, '_');
    
    if (!fs.existsSync(folder)) {
        fs.mkdirSync(folder, { recursive: true });
    }
    
    const filePath = path.join(folder, safeTitle + '.md');
    fs.writeFileSync(filePath, content || '', 'utf8');
}

async function run() {
    console.log("Fetching Main pages...");
    const mainPages = await getAllPages(0);
    console.log("Fetching Template pages...");
    const templatePages = await getAllPages(10);
    console.log("Fetching Project pages...");
    const projectPages = await getAllPages(4);
    console.log("Fetching MediaWiki pages...");
    const mediawikiPages = await getAllPages(8);
    console.log("Fetching Module pages...");
    const modulePages = await getAllPages(828);
    
    console.log(`Found ${mainPages.length} Main pages, ${templatePages.length} Template pages, ${projectPages.length} Project pages, ${mediawikiPages.length} MediaWiki pages, and ${modulePages.length} Module pages.`);
    
    // Categorize Templates
    const templateAssignments = categorizeTemplates(templatePages);
    
    // Categorize Main Pages
    const mainGraph = buildGraph(mainPages);
    const mainAssignments = categorizeMain(mainGraph);
    
    // Ensure SeriaCollection redirect logic
    const seriaCollection = mainPages.find(p => p.title === 'SeriaCollection');
    if (seriaCollection) {
        seriaCollection.revisions[0].content = '#REDIRECT [[Collections]]';
    }
    
    console.log("Wiping and recreating wiki directory...");
    if (fs.existsSync(WIKI_DIR)) {
        fs.rmSync(WIKI_DIR, { recursive: true, force: true });
    }
    fs.mkdirSync(WIKI_DIR);
    
    console.log("Writing files...");
    
    for (const page of mainPages) {
        const text = page.revisions && page.revisions[0] && page.revisions[0].content ? page.revisions[0].content : '';
        writePage(page.title, text, mainAssignments[page.title], false, 'Main');
    }
    
    for (const page of templatePages) {
        const text = page.revisions && page.revisions[0] && page.revisions[0].content ? page.revisions[0].content : '';
        writePage(page.title, text, templateAssignments[page.title], true, 'Template');
    }
    
    for (const page of projectPages) {
        const text = page.revisions && page.revisions[0] && page.revisions[0].content ? page.revisions[0].content : '';
        writePage(page.title, text, null, false, 'Project');
    }
    
    for (const page of mediawikiPages) {
        const text = page.revisions && page.revisions[0] && page.revisions[0].content ? page.revisions[0].content : '';
        writePage(page.title, text, null, false, 'MediaWiki');
    }
    
    for (const page of modulePages) {
        const text = page.revisions && page.revisions[0] && page.revisions[0].content ? page.revisions[0].content : '';
        writePage(page.title, text, null, false, 'Module');
    }
    
    console.log("Done!");
}

run().catch(console.error);

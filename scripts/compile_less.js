const fs = require('fs');
const path = require('path');
const less = require('less');

const lessFile = path.join(__dirname, '..', 'wiki', 'MediaWiki', 'Custom-common.less.md');
const cssFile = path.join(__dirname, '..', 'wiki', 'MediaWiki', 'Common.css.md');

let content = fs.readFileSync(lessFile, 'utf8');

// Prepend Fandom's built-in theme variables
const themeFallbacks = `
@theme-body: #0d0f19;
@theme-page: #191c2b;
@theme-buttons: #22263b;
@theme-header: #141724;
@theme-links: #4c89b5;

#gradient {
    .horizontal(@startColor; @endColor) {
        background-color: @endColor;
        background-image: linear-gradient(to right, @startColor, @endColor);
    }
}
`;
content = themeFallbacks + content;

// Replace local imports
content = content.replace(/@import\s+["']@{local}\/(.+?)\.less["']/g, '@import "./Custom-common.less_SLASH_$1.less.md"');

console.log('Compiling LESS...');
less.render(content, {
    paths: [path.dirname(lessFile)],
    filename: lessFile
}).then(output => {
    // MediaWiki:Common.css usually starts with /* <pre> */
    const header = '/* <pre> */\n/**\n * CSS placed here will be applied to all skins on the entire site.\n *\n * This page is compiled from LESS files listed in [[MediaWiki:Custom-common.less]] and should not be edited directly.\n */\n\n';
    fs.writeFileSync(cssFile, header + output.css, 'utf8');
    console.log('Successfully compiled LESS and saved to Common.css.md!');
}).catch(err => {
    console.error('Compilation failed:', err);
    process.exit(1);
});

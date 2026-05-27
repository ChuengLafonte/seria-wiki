--<pre>
local title =  mw.title.getCurrentTitle() 
local pagename = title.prefixedText:gsub(' ', '_')

return {
    
        ['delete'] = {
            action={'action', 'delete'}, display_text='Delete',
            title='Delete this page',
        };
        
        ['protect'] = {
            action={'action', 'protect'}, display_text='Protect',
            title='Protect this page', urlExtras={
                {'mwProtect-level-edit', 'sysop'},
                {'mwProtect-level-move', 'sysop'},
                {'mwProtect-level-upload', 'sysop'},
            },
        };
    
        ['unprotect'] = {
            action={'action', 'unprotect'}, display_text='Unprotect',
            title='Remove the protection for this page', urlExtras={
                {'mwProtect-level-edit', ''},
                {'mwProtect-level-move', ''},
                {'mwProtect-level-upload', ''},
                {'mwProtect-reason', 'Removing Protection'},
            },
        };
    
        ['change protection'] = {
            action={'action', 'unprotect'}, display_text='Change Protection',
            title='Change the protection levels for this page',
        };
        
        
        ['move'] = {
            specialPageAction='MovePage', display_text='Move',
            title='Rename this page to a new title', page=pagename
        };
        
        ['logs'] = {
            specialPageAction='Log', display_text='Page logs',
            title='View logs for this page', page=pagename
        };
        
        ['block'] = {
            specialPageAction='Block', display_text='Block',
            title='Block this user', page=title.text
        };
    
        ['unblock'] = {
            specialPageAction='Unblock', display_text='Unblock',
            title='Unblock this user', page=title.text,
        };
    
        ['change block'] = {
            specialPageAction='Block', display_text='Change block',
            title='Change the block settings for this user', page=title.text
        };
    
        ['deleted contributions'] = {
            specialPageAction='DeletedContributions', display_text='Del. Contribs',
            title='View this user\'s deleted contributions', page=pagename,
        };
        
        ['what links here'] = {
            specialPageAction='WhatLinksHere', display_text='What links here',
            title='View what pages link to this page', page=pagename
        };
        
        ['subpages'] = {
            specialPageAction='PrefixIndex', display_text='Subpages',
            title='View the subpages of this page', page=pagename..'/',
        };
        
        ['latest edit'] = {
            action={'diff', 'curr'}, display_text='Latest Edit',
            title='View the latest edit\'s diff on this page',
        };
        
        ['deleted revisions'] = {
            specialPageAction='Undelete', display_text='Deleted revisons',
            title='View this page\'s deleted revisions', page=pagename
        };
        
        ['block log'] = {
            specialPageAction='Log', action={'type', 'block'}, display_text='Block log',
            title='View this user\'s block log', urlExtras = {{'page', pagename}}
        };
        
        ['protection log'] = {
            specialPageAction='Log', action={'type', 'protect'}, display_text='Protection log',
            title='View this page\'s protection log', urlExtras = {{'page', pagename}}
        };
        
        ['deletion log'] = {
            specialPageAction='Log', action={'type', 'delete'}, display_text='Deletion log',
            title='View this page\'s deletion log', urlExtras = {{'page', pagename}}
        };
        
        ['move log'] = {
            specialPageAction='Log', action={'type', 'move'}, display_text='Move log',
            title='View this page\'s move log', urlExtras = {{'page', pagename}}
        };
        
        ['template type log'] = {
            specialPageAction='Log', action={'type', 'templateclassification'}, display_text='Template type log',
            title='View this page\'s log of template type changes', urlExtras = {{'page', pagename}}
        };
    
        ['user rights log'] = {
            specialPageAction='Log', action={'type', 'rights'}, display_text='User rights log',
            title='View the log of user rights changes to this user', urlExtras = {{'page', pagename}}        
        };

        ['abuse filter log'] = {
            specialPageAction='AbuseLog', action={'wpSearchTitle', pagename}, display_text='Filter log',
            title='View the filter log for this page',
        };
    
        ['abuse log'] = {
            specialPageAction='AbuseLog', action={'wpSearchUser', title.text}, display_text='Abuse Log',
            title='View the abuse logs for this user',
        };
        
        ['user logs'] = {
            specialPageAction='Log', page=title.text, display_text='User Logs',
            title='View this user\'s logs',
        };
    };
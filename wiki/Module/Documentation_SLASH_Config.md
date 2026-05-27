----------------------------------------------------------------------------------------------------
--
--                               Configuration for Module:Documentation
--
-- Here you can set the values of the parameters and messages used in Module:Documentation to
-- localise it to your wiki and your language. Unless specified otherwise, values given here
-- should be string values.
----------------------------------------------------------------------------------------------------

local cfg = {} -- Do not edit this line.

----------------------------------------------------------------------------------------------------
-- Index
-- 
-- The suffix `-summary` means an edit summary.
-- The suffix `-text` means actual text displayed to the user.
-- The suffix `-text` means hover text displayed to the user when an element is hovered over.
--
-- The variable `__TYPE__` means the type of documentation that was used. 
-- This can be 'Module' or 'Template'. This will default to 'Module' if no type is specified.
-- Any variables starting with `$` and end in a number indicate message arguments.
----------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------------------
-- Main parameters
-- 
-- `__TYPE__` stands for the type of documentation that was inputted, this can be "Module" or "Template".
-- The text for this can be changed in the `type-` parameters.
----------------------------------------------------------------------------------------------------
-- Summary for creating the documentation subpage
cfg['doc-edit-summary'] = "Creating __TYPE__ Documentation for \"[[:$1]]\""

-- Text to display on the create sandbox link
cfg['sandbox-create-text'] = 'Create Sandbox'

-- Hover text to display on the create sandbox link
cfg['sandbox-create-title'] = 'Create the sandbox subpage for this __TYPE__'

-- Summary for creating the sandbox
cfg['sandbox-create-summary'] = "Creating Sandbox __TYPE__ for \"[[:%s]]\""

----------------------------------------------------------------------------------------------------
-- Main links
-- 
-- These links are the links that are displayed at the top of the module documentation
----------------------------------------------------------------------------------------------------
-- Text to display on the "view" main documentation link
cfg['main-view-text'] = 'view'

-- Hover text to display on the "view" main documentation link
cfg['main-view-title'] = 'View the Documentation subpage for this __TYPE__'

-- Text to display on the "edit" main documentation link
cfg['main-edit-text'] = 'edit'

-- Hover text to display on the "edit" main documentation link
cfg['main-edit-title'] = 'Edit the Documentation subpage for this __TYPE__'

-- Text to display on the "latest diff" main documentation link
cfg['main-curdiff-text'] = 'latest diff'

-- Hover text to display on the "latest diff" main documentation link
cfg['main-curdiff-title'] = 'View the diff on the latest Edit to the Documentation subpage for this __TYPE__'

-- Text to display on the "hist" main documentation link
cfg['main-hist-text'] = 'hist'

-- Hover text to display on the "hist" main documentation link
cfg['main-hist-title'] = 'View the history of this __TYPE__\'s documentation subpage'

-- Text to display on the "purge" main documentation link
cfg['main-purge-text'] = 'purge'

-- Hover text to display on the "purge" main documentation link
cfg['main-purge-title'] = 'Purge this page'

-- Text to display on the "create" main documentation link
cfg['main-create-text'] = 'create'

-- Hover text to display on the "create" main documentation link
cfg['main-create-title'] = 'Create the Documentation for this __TYPE__'


----------------------------------------------------------------------------------------------------
-- Sandbox links
-- 
-- These messages here repersent the links for the sandbox subpage.
----------------------------------------------------------------------------------------------------
-- Text to display on the "Sandbox" sandbox link
cfg['sandbox-main-text'] = 'Sandbox'

-- Text to display on the "edit" sandbox link
cfg['sandbox-edit-text'] = 'edit'

-- Hover text to display on the "edit" sandbox link
cfg['sandbox-edit-title'] = 'Edit the sandbox __TYPE__'

-- Text to display on the "latest edit" sandbox link
cfg['sandbox-curdiff-text'] = 'latest diff'

-- Hover text to display on the "latest edit" sandbox link
cfg['sandbox-curdiff-title'] = 'View the latest edit\'s diff on the sandbox __TYPE__'

-- Text to display on the "hist" sandbox link
cfg['sandbox-hist-text'] = 'hist'

-- Hover text to display on the "hist" sandbox link
cfg['sandbox-hist-title'] = 'View the history on the sandbox __TYPE__'

-- Text to display on the "reset" sandbox link
cfg['sandbox-reset-text'] = 'reset'

-- Hover text to display on the "reset" sandbox link
cfg['sandbox-reset-title'] = 'Reset the sandbox __TYPE__ to match the main __TYPE__'

----------------------------------------------------------------------------------------------------
-- Tools links
-- 
-- These messages here repersent the links to tools for the module.
----------------------------------------------------------------------------------------------------
-- Text to display on the "View subpages" tool link
cfg['tool-subpages-text'] = 'View subpages'

-- Hover text to display on the "View subpages" tool link
cfg['tool-subpages-title'] = 'View the subpages of this __TYPE__'

-- Text to display on the "View links" tool link
cfg['tool-whl-text'] = 'View links'

-- Hover text to display on the "View links" tool link
cfg['tool-whl-title'] = 'View what links here to this __TYPE__'

----------------------------------------------------------------------------------------------------
-- Talk links
-- 
-- These messages here repersent the links to the module's talk page.
----------------------------------------------------------------------------------------------------
-- Text to display on the "Talk" talk link
cfg['talk-main-text'] = 'Talk'

-- Hover text to display on the "+" talk link
cfg['talk-newsec-title'] = 'Add a new section to the __TYPE__\'s talk page'

-- Text to display on the "edit" talk link
cfg['talk-edit-text'] = 'edit'

-- Hover text to display on the "edit" talk link
cfg['talk-edit-title'] = 'Edit the __TYPE__\'s talk page'

-- Text to display on the "latest diff" talk link
cfg['talk-curdiff-text'] = 'latest diff'

-- Hover text to display on the "latest diff" talk link
cfg['talk-curdiff-title'] = 'View the latest edit\'s diff on the __TYPE__\'s talk page'

-- Text to display on the "hist" talk link
cfg['talk-hist-text'] = 'hist'

-- Hover text to display on the "hist" talk link
cfg['talk-hist-title'] = 'View the history on the __TYPE__\'s talk page'

-- Text to display on the "Create talk" talk link
cfg['talk-create-text'] = 'Create talk'

-- Hover text to display on the "Create talk" talk link
cfg['talk-create-title'] = 'Create the talk page for this __TYPE__'

-- Summary for creating the talk page
cfg['talk-create-summary'] = 'Creating talk page for __TYPE__ \"[[:$1]]\"'


----------------------------------------------------------------------------------------------------
-- Page links
-- 
-- These messages here repersent any other links to the module.
----------------------------------------------------------------------------------------------------
-- Text to display on the "Latest Diff" page link
cfg['page-curdiff-text'] = 'Latest Diff'

-- Hover text to display on the "Latest Diff" page link
cfg['page-curdiff-title'] = 'View the latest edit\'s diff on the __TYPE__'

-- Text to display on the "Page logs" page link
cfg['page-logs-text'] = 'Page logs'

-- Hover text to display on the "Page logs" page link
cfg['page-logs-title'] = 'View the logs for this page'

----------------------------------------------------------------------------------------------------
-- Testcases links
-- 
-- These messages here repersent the links to the module's testcases page.
----------------------------------------------------------------------------------------------------
-- Text to display on the "Testcases" testcases link
cfg['test-main-text'] = 'Testcases'

-- Hover text to display on the "Testcases" testcases link
cfg['test-main-title'] = 'View the testcases subpage for this __TYPE__'

-- Text to display on the "edit" testcases link
cfg['test-edit-text'] = 'edit'

-- Hover text to display on the "edit" testcases link
cfg['test-edit-title'] = 'View the testcases subpage for this __TYPE__'

-- Text to display on the "latest diff" testcases link
cfg['test-curdiff-text'] = 'latest diff'

-- Hover text to display on the "latest diff" testcases link
cfg['test-curdiff-title'] = 'Edit the testcases subpage for this __TYPE__'

-- Text to display on the "run" testcases link
cfg['test-run-text'] = 'run'

-- Hover text to display on the "run" testcases link
cfg['test-run-title'] = 'Run the testcases subpage for this __TYPE__'

-- Text to display on the "create" testcases link
cfg['test-results-create-text'] = 'create'

-- Hover text to display on the "create" testcases link
cfg['test-results-create-title'] = 'Create the testcases results subpage for this __TYPE__'

-- Summary for creating the testcases results subpage
cfg['test-results-create-summary'] = 'Creating testcases results page for __TYPE__ \"[[:$1]]\"'

-- Text to display on the "create testcases" testcases link
cfg['test-create-text'] = 'Create testcases'

-- Hover text to display on the "create testcases" testcases link
cfg['test-create-title'] = 'Create the testcases subpage for this __TYPE__'

-- Summary for creating the testcases subpage
cfg['test-create-summary'] = 'Creating testcases results page for __TYPE__ \"[[:$1]]\"'

----------------------------------------------------------------------------------------------------
-- Other messages
-- 
-- These messages here repersent any other messages.
----------------------------------------------------------------------------------------------------
-- Text for the 'Module' option
cfg['type-module'] = 'Module'

-- Text for the 'Template' option
cfg['type-template'] = 'Template'

-- Text for the "jump to code" link
cfg['jump-text'] = 'Jump to code'

-- Hover text for the "jump to code" link
cfg['jump-title'] = "Jump to the code of this __TYPE__"

-- Documentation image
cfg['doc-image'] = 'Template Info Icon.svg'

-- Documention image size
cfg['doc-image-size'] = 60

-- Header text
cfg['header-text'] = '__TYPE__ Documentation'

-- Header text
cfg['header-text-general'] = 'Documentation'

-- Note
cfg['note'] = 'Note'

-- Template note
cfg['template-note'] = 'Some or whole parts of the template may not be visible due to some parameters not being provided.'

-- Page tools
cfg['page-tools'] = 'Page Tools'

-- Page links
cfg['page-links'] = '__TYPE__ Links'

-- Page links (general use)
cfg['page-links-general'] = 'Page Links'

-- Text for when the documentation does not exist
cfg['no-exist-message'] = 'The documentation for this __TYPE__ does not exist. Please create it if you are familiar with this __TYPE__.'

-- Text for when the documentation does not exist (non-specific namespace)
cfg['no-exist-message-general'] = 'The documentation for this page does not exist. Please create it if you are familiar with this page.'

-- Category for when the documentation does not exist
cfg['no-exist-cat'] = 'Category:__TYPE__s without documentation subpages'

-- Category for when the documentation does not exist (general use)
cfg['no-exist-cat-general'] = 'Category:Pages without documentation subpages'

-- "How does this work" page name
cfg['hdtw-name'] = '__TYPE__:Documentation'

-- "How does this work" page name (general use)
cfg['hdtw-name-general'] = 'Template:Documentation'

-- "How does this work" link text
cfg['hdtw-text'] = 'About Documentations'

-- "Other tools"
cfg['other-tools'] = 'Other Tools'

-- "Back to top" link text
cfg['back-to-top'] = 'Back to top'

-- Default title if was not provided
cfg['default-title'] = 'Sandbox'

-- Sandbox subpage
cfg['subpage-sandbox'] = 'Sandbox'

-- Testcases subpage
cfg['subpage-testcases'] = 'testcases'

-- Documentation subpage
cfg['subpage-documentation'] = 'doc'

-- End template directory (where preloads are stored)
cfg['dir-module'] = 'LuaDocumentation'

-- End template directory (where preloads are stored)
cfg['dir-template'] = 'Documentation'

-- End template directory (general use)
cfg['dir-general'] = 'Documentation'

-- Edit intro directory
cfg['dir-editintro'] = 'editintro'

-- Preloads directory
cfg['dir-preload'] = 'newdocpage'

-- Testcases preload
cfg['testcases-name'] = 'testcases'

-- Testcases results preload
cfg['testcases-results-name'] = 'testcasesResults'

-- Default "Documentation" header text
cfg['doc'] = 'Documentation'
----------------------------------------------------------------------------------------------------
-- End configuration
--
-- Don't edit anything below this line.
----------------------------------------------------------------------------------------------------
return cfg
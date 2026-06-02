{{TextSection
|text='''This Module Requires Cache Refresh After Changes'''<br>
Module Page Name(s): {{#switch:{{{1|}}}
|invslot=Module:Inventory slot/Datasheet
|item_variants=Module:Item/Variants
|item_api=Module:Item/ApiData, Module:Item/ApiAliases
|crafting=Module:Crafting/Aliases
|minion=Module:Minion/Data
|#default={{Red|Invalid}}
}}<br>
Prerequisite: Option ''RefreshLuaCache'' in [[Special:Preferences#mw-prefsection-gadgets|your gadget settings]] must be enabled.<br>
Instruction: If prerequisite is met, button(s) for [[Project:Modules#Caching|refreshing cache entries]] will load below.<br>
<hr>
{{#switch:{{{1|}}}
|invslot=<div class="refresh-lua-cache button" data-cache-id="invslot" style="display:none;">Refresh Inventory Slot Cache</div>
|item_variants=<div class="refresh-lua-cache button" data-cache-id="item_variants" style="display:none;">Refresh Item Variants Cache</div>
|item_api=<div class="refresh-lua-cache button" data-cache-id="item_api_data" style="display:none;">Refresh Data Cache</div>
<div class="refresh-lua-cache button" data-cache-id="item_api_aliases" style="display:none;">Refresh Aliases Cache</div>
|crafting=<div class="refresh-lua-cache button" data-cache-id="crafting_aliases" style="display:none;">Refresh Aliases Cache</div>
|minion=<div class="refresh-lua-cache button" data-cache-id="minion_data" style="display:none;">Refresh Data Cache</div>
|#default={{Red|Error: Please specify a valid cache type}}
}}
}}
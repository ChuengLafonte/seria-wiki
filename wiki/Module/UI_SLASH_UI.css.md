.mcui {
    background: #c6c6c6;
    border: 2px solid #000;
    border-top-color: #fff;
    border-left-color: #fff;
    border-bottom-color: #555;
    border-right-color: #555;
    padding: 6px;
    display: inline-block;
    image-rendering: pixelated;
    font-family: sans-serif; /* You can change this to a Minecraft font */
}

.mcui-centered {
    margin: 0 auto;
    display: table;
}

.mcui-header {
    color: #3f3f3f;
    padding: 2px 4px 6px;
}

.mcui-row {
    display: flex;
    flex-wrap: nowrap;
}

.invslot {
    width: 36px;
    height: 36px;
    background: #8b8b8b;
    border: 2px solid #373737;
    border-bottom-color: #fff;
    border-right-color: #fff;
    display: inline-block;
    margin: 1px;
    position: relative;
}

.invslot-item {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 32px;
    height: 32px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.invslot-item-image img {
    max-width: 32px;
    max-height: 32px;
    image-rendering: pixelated;
}

/* Tabber support */
.sbw-ui-tabber {
    display: block;
}

.sbw-ui-tab-content {
    /* Initially hide tab contents if managed by JS, but block if active */
    display: block; 
}
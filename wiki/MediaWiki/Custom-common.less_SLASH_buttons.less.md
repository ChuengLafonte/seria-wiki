/**
* Style sheet for buttons
*/

@buttonClass: ~".button:not(.carousel-arrow)";
@buttonClassImg: ~".button img:not(.carousel-arrow img)";

a.wikia-button,
.wikia-single-button a,
.wikia-menu-button,
@{buttonClass} {
	--w-button-color: #7A320F;
	--w-button-outline-color: #7A320F;
	--w-button-color-hover: #57240A;
	--w-button-outline-color-hover: #57240A;
	--w-button-text-color: #ffffff;
	display: inline-block;
	margin-bottom: 14px;
	padding: 12px;
	background-color: var(--w-button-color);
	border-radius: 4px;
	border: 2px solid var(--theme-page-background-color);
	outline: 1px solid var(--w-button-outline-color);
	color: var(--w-button-text-color);
	line-height: 14px;
	letter-spacing: .3px;
	white-space: nowrap;
	cursor: pointer;
	transition: all .2s linear;
	.theme-fandomdesktop-light & {
		--w-button-color: #BB3737;
		--w-button-color-hover: #962C2C;
	}
	&:hover, &:active, &:focus-visible {
		background-color: var(--w-button-color-hover);
		outline-color: var(--w-button-outline-color-hover);
		text-decoration: none;
	}
	&:not(:disabled):focus-visible {
		box-shadow: rgba(255,255,255,0.8) -1px -2px 0 0 inset, rgba(0,0,0,0.4) -1px -4px 0px 0px inset;
	}
	&:disabled {
		cursor: default;
		opacity: .5;
	}
	&.forward-button {
		--w-button-color: rgb(15,123,217);
		--w-button-outline-color: rgb(15,123,217);
		--w-button-color-hover: rgb(1,76,140);
		--w-button-outline-color-hover: rgb(1,76,140);
	}
	&.secondary {
		--w-button-text-color: var(--theme-body-text-color);
		--w-button-color: transparent;
		--w-button-color-hover: transparent;
	}
	&.big {
		padding: 22px;
		font-size: 18px;
		font-weight: 700;
	}
	th &:last-child,
	td &:last-child {
		margin-bottom: 0;
	}
}
a.wikia-button img,
.wikia-single-button a img,
.wikia-menu-button img,
@{buttonClassImg} {
	vertical-align: text-bottom;
}

/* Button Fixes */
.wikia-menu-button,
@{buttonClass},
a.wikia-button,
.wikia-single-button a,
.wikia-menu-button,
.wikia-chiclet-button {
	box-sizing: content-box !important;
	-webkit-touch-callout: none;
	-webkit-user-select: none;
	-khtml-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}
.mw-ui-button { /* more elegant focus glow */
	&:not(:disabled):focus {
		box-shadow: none;
	}
	&:not(:disabled):focus-visible {
		box-shadow: rgba(255,255,255,0.8) -1px -2px 0 0 inset;
	}
}

/* Button Modifiers */
body .page-content .full-width-button {
	margin-bottom: 24px;
	padding: 8px;
	width: 98%;
	width: -moz-available;
	width: -webkit-fill-available;
	width: fill-available;
	text-align: center;
	+* {
		margin-top: -24px;
		margin-bottom: 4px;
		width: 100%;
		.table-wide-inner, .wikitable {
			margin-top: 0;
		}
	}
	&::before {
		content: '\2261';
		margin: 0 12px 0 4px;
	}
}
body .page-content .forward-button {
	transition: all 0.5s;
	&:after {
		content: '';
		position: relative;
		opacity: 0;
		top: 0;
		right: -20px;
		color: var(--w-button-text-color);
		display: inline;
		transition: 0.5s;
	}
	&:hover, &:active, &:focus-visible {
		&:after {
			content: '\00bb';
			opacity: 1;
			right: 0;
			padding-left: 12px;
		}
	}
}
body .page-content .tablecollapse-button {
	padding: 5px;
	margin: 1px;
	float: right;
}
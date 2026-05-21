{{Documentation/Header}}
Used to display Descriptions with formatting for source and title.

==Syntax==
* {{F|1}} &mdash; Description text
* {{F|2}} &mdash; Source of description
* {{F|title}} &mdash; Title of description
* {{F|italic}} &mdash; Transform description into italic

==Example==
{{T|Description|Lore description|_Ybr_=1}}
<hr />
{{T|Description|Feeling defeated, it dawned on the Skyrider that there are things that swordsmanship cannot achieve. So instead of believing in his swordsmanship, he turned to the sword itself. "Bigger is always better, and swords are no exception," he thought. In the grand Guyun Stone Forest, he embraced his grand ending. His dream of flight came to an end, but his sword and story would never fade...|block=1|_Ybr_=1}}
<hr />
{{T|Description|Code name: Beth. A high-purity Anemo entity.<br />Elemental [[hypostases]] are life forms which have completely abandoned their former appearance and biological structure, making them able to reach the highest level of elemental purity.<br />Research into hypostases is mainly led by scholars of [[Sumeru Akademiya]], but due to the level of danger that they pose, little of substance is known about hypostases beyond their scientific name and code name.|[[Adventurer Handbook]]|block=1|_Ybr_=1}}
<hr />
{{T|Description|p1=This Description has a title|p2=title=Description Title|p3=italic=1|_Ybr_=1}}

==Template Data==
<templatedata>
{
	"params": {
		"1": {
			"label": "Text",
			"type": "string",
			"default": "Description",
			"description": "Description Text.",
			"required": true
		},
		"2": {
			"label": "Source",
			"type": "string",
			"description": "Source of Description below text right aligned (Italics)."
		},
		"title": {
			"label": "Title",
			"type": "string",
			"description": "Title of Description above text (Bold)."
		},
		"italic": {
			"label": "Italic Description",
			"description": "Transform the description into italic text",
			"type": "boolean"
		}
	},
	"description": "Used to display Descriptions with formatting for source and title.",
	"paramOrder": [
		"1",
		"2",
		"title",
		"italic"
	],
	"format": "inline"
}
</templatedata>

<noinclude>[[id:Templat:Description/doc]]
[[ja:テンプレート:Description/doc]]
[[pt-br:Predefinição:Description/doc]]
[[th:แม่แบบ:Description/doc]]
[[vi:Bản mẫu:Description/doc]]
</noinclude>
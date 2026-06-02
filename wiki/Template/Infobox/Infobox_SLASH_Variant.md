{| class="infobox" style="width: 300px; border: 1px solid {{{color|#729B27}}}; border-radius: 5px; background: #f0f0f0; margin-bottom: 1em; margin-left: 1em; float: right; clear: right;"
|-
| colspan="2" style="background-color: {{{color|#729B27}}}; color: white; text-align: center; font-weight: bold; font-size: 18px; padding: 8px; border-radius: 4px 4px 0 0; text-shadow: 1px 1px 0px rgba(0,0,0,0.5);" | {{{title|{{PAGENAME}}}}}
|-
| colspan="2" style="text-align: center; padding: 10px;" |
{{#if:{{{content|}}} | {{{content}}} | [[File:{{{image|{{PAGENAME}}}}}.png|150px]] }}
{{#if:{{{slot|}}}|
{{!}}-
{{!}} colspan="2" style="text-align: center; padding: 8px; border-top: 1px solid #b8b8b8;" {{!}}
{{Slot|{{{slot}}}}}
}}
{{#if:{{{gallery|}}}|
{{!}}-
{{!}} colspan="2" style="text-align: center; padding: 8px; border-top: 1px solid #b8b8b8;" {{!}}
{{{gallery}}}
}}
|}
<noinclude>
[[Category:Templates]]
Template ini digunakan untuk membuat Infobox bergaya Minecraft Wiki klasik dengan dukungan '''Tabber''' maupun Slot tunggal (seperti Seeds).

== Parameter ==
* `title`: Judul infobox (default PAGENAME)
* `color`: Warna kotak dan border (default #729B27, hijau alam)
* `content`: Gunakan ini jika ingin memasukkan `<tabber>` kompleks. Jika diisi, parameter `image` akan diabaikan.
* `image`: Nama file gambar 3D jika tidak menggunakan tabber. Otomatis diberi ekstensi .png. (default PAGENAME)
* `slot`: Nama item untuk memunculkan ikon item di dalam Inventory Slot (kotak kecil) di bawah gambar utama.
* `gallery`: Untuk menaruh deretan ikon jika kamu memiliki banyak varian.

== Contoh Penggunaan ==
<pre>
{{Infobox Variant
| title = Seeds
| color = #3887b5
| image = Seeds
| slot = Seeds
}}
</pre>
</noinclude>
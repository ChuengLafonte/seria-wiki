{{Documentation subpage}}
{{Lua|List|Item}}

'''Image List''' adalah sebuah templat yang digunakan untuk dengan cepat membuat daftar yang hanya berisi tautan beserta gambar. Menggunakan {{T|Plainlist}} dan {{T|LinkImage}}.
{{Tc}}

==Sintaks==
{{T|Image List|1|...|list_type|image|nolink|noerror|ignoreodds|noimgpad|list_style}}, di mana:
*{{S|1}} bisa berupa:
** Nama item, misal: {{Code|Coal}}
** Sebagai daftar, di mana setiap item berada di baris baru, dan baris diawali dengan {{Code|*}}.
** Informasi lebih lanjut tentang sintaks item dapat ditemukan di [[Template:Resource Display/doc|Resource Display/doc]].
* {{S|...}} - Sebagai alternatif, daftar item dapat disediakan dalam parameter-parameter berikutnya, misal: {{Code|{{((}}Image List{{!}}Item 1{{!}}Item 2{{!}}Item 3{{))}}}}
*{{S|list_type}} - Tipe daftar. Input yang diizinkan: {{Code|circle}} {{Code|square}} {{Code|disc}} {{Code|none}}. Bawaan: {{Code|none}}.
*{{S|image}} atau {{S|img}} atau {{S|i}} - Menentukan apakah gambar harus ditampilkan atau tidak. Bawaan: {{Code|true}}.
*{{s|nolink}} atau {{s|nl}} - Menonaktifkan tautan untuk keseluruhan daftar. Bawaan: {{Code|false}}.
*{{S|noerror}} atau {{S|ne}} - Untuk menampilkan konten meskipun ada beberapa kesalahan (error) yang terjadi. Bawaan: {{Code|false}}.
*{{S|ignoreodds}} - Jika diaktifkan, peluang (odds) tidak akan ditampilkan meskipun bernilai. Bawaan: tidak aktif (off).
*{{S|noimgpad}} - Jika diaktifkan, nama item tanpa berkas gambar tidak akan diberi ruang kosong (padding) di depannya. Bawaan: tidak aktif (off).
*{{S|list_style}} - Gaya HTML yang diterapkan pada setiap item daftar ({{Code|&lt;li&gt;&lt;/li&gt;}}).

Teks yang ditampilkan di dekat setiap item dapat diubah menggunakan sintaks berikut: {{Code|item;text}}. Teks bawaan yang ditampilkan adalah nama item tersebut. Misal: {{Code|Coal;Dirt}}

==Contoh Penggunaan==
;Contoh 1
<pre>
{{Image List|Cobblestone|Stone|Dirt|Glass}}
</pre>
menghasilkan

{{Image List|Cobblestone|Stone|Dirt|Glass}}
;Contoh 2
<pre>
{{Image List|*Coal
*Iron Ingot
*Gold Ingot
*Lapis Lazuli
}}
</pre>
menghasilkan

{{Image List|*Coal
*Iron Ingot
*Gold Ingot
*Lapis Lazuli
}}

<includeonly>
[[Category:List templates]]
</includeonly>
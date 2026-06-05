{{Documentation subpage}}
{{Lua|List|Item}}

'''Resource List''' adalah sebuah templat yang digunakan untuk menampilkan jumlah material yang dibutuhkan untuk mendapatkan item tertentu. Templat ini menampilkan jumlah item dengan format khusus: angka berwarna hijau dan dapat menampilkan format *stack* (selalu 64 item/stack) saat kursor diarahkan ke atasnya (*hover*).
{{Tc}}

==Sintaks==
{{Ts|RL}}
{{T|Resource List|1|...|list_type|image|nolink|noerror|ignoreodds|noimgpad|list_style}}, di mana:
*{{S|1}} bisa berupa:
** Item input. Sintaksnya: {{Code|[jumlah item] [nama item]}} (jika kamu ingin memasukkan koin, gunakan sintaks berikut: {{Code|[jumlah] coins}}).
** Sebagai daftar, di mana setiap item berada di baris baru, dan baris diawali dengan {{Code|*}}.
** Informasi lebih lanjut tentang sintaks item dapat ditemukan di [[Template:Resource Display/doc|Resource Display/doc]].
* {{S|...}} - Sebagai alternatif, daftar sumber daya dapat disediakan dalam parameter-parameter berikutnya, misal: {{Code|{{((}}Resource List{{!}}Item 1{{!}}Item 2{{!}}Item 3{{))}}}}
*{{S|list_type}} - Tipe daftar. Input yang diizinkan: {{Code|circle}} {{Code|square}} {{Code|disc}} {{Code|none}}. Bawaan: {{Code|none}}.
*{{S|image}} atau {{S|img}} atau {{S|i}} - Menentukan apakah gambar harus ditampilkan atau tidak. Bawaan: {{Code|true}}.
*{{s|nolink}} atau {{s|nl}} - Menonaktifkan tautan untuk keseluruhan daftar. Bawaan: {{Code|false}}.
*{{S|noerror}} atau {{S|ne}} - Untuk menampilkan konten meskipun ada beberapa kesalahan (error) yang terjadi. Bawaan: {{Code|false}}.
*{{S|ignoreodds}} - Jika diaktifkan, peluang (odds) tidak akan ditampilkan meskipun bernilai. Bawaan: tidak aktif (off).
*{{S|noimgpad}} - Jika diaktifkan, nama item tanpa berkas gambar tidak akan diberi ruang kosong (padding) di depannya. Bawaan: tidak aktif (off).
*{{S|list_style}} - Gaya HTML yang diterapkan pada setiap item daftar ({{Code|&lt;li&gt;&lt;/li&gt;}}).

==Contoh Penggunaan==
;Contoh 1
:Menggunakan sintaks daftar dengan pemisah baris vertikal.
<pre>
{{Resource List|500x Dirt|256x Coal}}
</pre>
menghasilkan

{{Resource List|500x Dirt|256x Coal}}
;Contoh 2
:Menggunakan sintaks item majemuk, dan juga {{C}}.
<pre>
{{Resource List|
*500 Dirt
*256 Coal
*20000 Coins
}}
</pre>
menghasilkan

{{Resource List|
*500 Dirt
*256 Coal
*20000 Coins
}}

<includeonly>
[[Category:List templates]]
</includeonly>
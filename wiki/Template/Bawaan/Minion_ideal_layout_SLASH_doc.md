{{Documentation subpage}}
{{Lua|Minion/UI}}
Menampilkan tata letak ideal minion.

== Sintaks ==
{{T|Minion ideal layout|minion|ideal|border|A1..E5}}
* {{S|minion}} -  Nama lengkap minion (tanpa tingkat di akhir)
* {{S|ideal}} -  Area tengah diisi dengan blok/item apa
* {{S|border}} - (opsional) bahan pinggiran layout (jika ada)
* {{S|A1...E5}} -  Dalam beberapa kasus, bagian 'ideal' tidak selalu blok solid; kamu bisa menggunakan parameter A1-E5 untuk mengatur setiap blok layaknya membuat tata letak di meja pembuatan.
* Jika minion tersebut membutuhkan udara kosong (air), maka nilainya harus: "<code>Air (minion)</code>".

== Contoh Penggunaan ==
<pre>
{{Minion ideal layout|minion=Cocoa Beans Minion|ideal=Air (minion)
|A1=Jungle Wood|C1=Jungle Wood|E1=Jungle Wood
|A3=Jungle Wood               |E3=Jungle Wood
|A5=Jungle Wood|C5=Jungle Wood|E5=Jungle Wood
}}
</pre>
{{Minion ideal layout|minion=Cocoa Beans Minion|ideal=Air (minion)
|A1=Jungle Wood|C1=Jungle Wood|E1=Jungle Wood
|A3=Jungle Wood               |E3=Jungle Wood
|A5=Jungle Wood|C5=Jungle Wood|E5=Jungle Wood
}}

<pre>{{Minion ideal layout|minion=Spider Minion|ideal=Air (minion)|border=Oak Fence}}</pre>
{{Minion ideal layout|minion=Spider Minion|ideal=Air (minion)|border=Oak Fence}}

<includeonly>[[Category:General wiki templates]]</includeonly>
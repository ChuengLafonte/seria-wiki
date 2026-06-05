const fs = require('fs');
const path = require('path');

const replacements = {
    // Module:Minion/UI
    "Highest tier has been reached!": "Tingkat tertinggi telah dicapai!",
    "The highest tier of this minion/has been reached": "Tingkat tertinggi dari minion ini/telah dicapai",
    "This minion has reached the/maximum tier.": "Minion ini telah mencapai/tingkat maksimum.",
    "Highest craftable tier has been/&areached!": "Tingkat tertinggi yang bisa dibuat telah/&adicapai!",
    "The highest craftable tier of/&7this minion has been reached": "Tingkat tertinggi yang bisa dibuat dari/&7minion ini telah dicapai",
    "Time Between Actions:": "Waktu Antar Aksi:",
    "Time Between Action:": "Waktu Antar Aksi:",
    "Max Storage:": "Penyimpanan Maksimal:",
    "View the items required to/&7upgrade this minion to the/&7next tier.": "Lihat item yang dibutuhkan untuk/&7meningkatkan minion ini ke/&7tingkat berikutnya.",
    "Click to view!": "Klik untuk melihat!",
    "Click to upgrade!": "Klik untuk meningkatkan!",
    "Storage unlocked at tier ": "Penyimpanan terbuka pada tingkat ",
    "Ideal Layout": "Tata Letak Ideal",
    "View the most effecient spot for/&7this minion to be placed in.": "Lihat letak paling efisien untuk/&7menempatkan minion ini.",
    "Next Tier": "Tingkat Berikutnya",
    "Minion Skin Slot": "Slot Skin Minion",
    "You can insert a Minion Skin/&7here to change the appearance of/&7your minion.": "Kamu bisa memasukkan Skin Minion/&7di sini untuk mengubah penampilan/&7dari minion milikmu.",
    "Fuel": "Bahan Bakar",
    "Increase the speed of your/&7minion by adding minion fuel/&7items here.": "Tingkatkan kecepatan/&7minion kamu dengan menambahkan item bahan bakar/&7di sini.",
    "Note: &7You can\\'t take/&7fuel back out after you/&7place it here!": "Catatan: &7Kamu tidak bisa mengambil/&7bahan bakar kembali setelah/&7kamu meletakkannya di sini!",
    "Automated Shipping": "Pengiriman Otomatis",
    "Add a &bBudget Hopper&7\\,/&bEnchanted Hopper&7 or a/&bPerfect Hopper&7 here to make/&7your minion automatically sell/&7generated items after its/&7inventory is full.": "Tambahkan &bBudget Hopper&7\\,/&bEnchanted Hopper&7 atau/&bPerfect Hopper&7 di sini agar/&7minion kamu otomatis menjual/&7item yang dihasilkan setelah/&7inventarisnya penuh.",
    "Upgrade Slot": "Slot Peningkatan",
    "You can improve your minion by/&7adding a minion upgrade item/&7here.": "Kamu bisa meningkatkan minion kamu dengan/&7menambahkan item peningkatan minion/&7di sini.",
    "Collect All": "Kumpulkan Semua",
    "Click to Collect all items!": "Klik untuk Mengumpulkan semua item!",
    "Quick-Upgrade Minion": "Peningkatan Cepat Minion",
    "Click here to upgrade your/&7minion to the next tier.": "Klik di sini untuk meningkatkan/&7minion kamu ke tingkat berikutnya.",
    "Pickup Minion": "Ambil Minion",
    "Click to pickup!": "Klik untuk mengambil!",
    "Resources Generated:": "Sumber Daya Dihasilkan:",
    "Talk to ": "Bicara dengan ",
    " in the/": " di/",
    "to unlock the/next tier!": "untuk membuka/tingkat berikutnya!",

    // Module:Minion/Templates
    "No Description": "Tidak ada deskripsi",

    // Docs
    "Displays a minion's ideal layout.": "Menampilkan tata letak ideal minion.",
    "Full minion name (without the tier at the end)": "Nama lengkap minion (tanpa tingkat di akhir)",
    "What the center area is filled with": "Area tengah diisi dengan blok/item apa",
    "(optional) what the border is made of (if there is one)": "(opsional) bahan pinggiran layout (jika ada)",
    "In some cases the \"ideal\" isn't just a solid type; in these cases, A1-A5 to E1-E5 can be used in the same manor as a crafting table template to display an item there": "Dalam beberapa kasus, bagian 'ideal' tidak selalu blok solid; kamu bisa menggunakan parameter A1-E5 untuk mengatur setiap blok layaknya membuat tata letak di meja pembuatan.",
    "In the case of a minion requiring air, the value should be": "Jika minion tersebut membutuhkan udara kosong (air), maka nilainya harus:",
    "Syntax": "Sintaks",
    "Examples": "Contoh Penggunaan",
    "Displays a table of items a minion drops.": "Menampilkan tabel item yang dijatuhkan/dihasilkan oleh minion.",
    "minion name (e.g. Clay Minion)": "nama minion (misal: Clay Minion)",
    "Item names dropped. The order determines the amount.": "Nama item yang dihasilkan. Urutan memengaruhi tabel.",
    "Base amount per harvest.": "Jumlah dasar yang dihasilkan per panen.",
    "Displays a table of the speed a minion takes per tier.": "Menampilkan tabel kecepatan minion pada tiap tingkatan (tier).",
    "Displays a table of the profits a minion makes per tier.": "Menampilkan tabel keuntungan (profit) yang dihasilkan minion per tingkatan.",
    "Bazaar pricing. Use a 1 for true, 0 for false.": "Harga Bazaar. Gunakan 1 untuk benar (aktif), 0 untuk salah.",
    "Default is": "Standarnya adalah",
    "Calculates Diamond Spreading. Same values as above.": "Menghitung efek Diamond Spreading. Nilainya sama seperti di atas (1 atau 0).",
    "Custom drops. For the name parameter drop1 to drop4. e.g.": "Hasil drop kustom. Untuk parameter nama, gunakan drop1 sampai drop4. misal:"
};

function translateFile(filepath) {
    if (!fs.existsSync(filepath)) {
        console.log(`Not found: ${filepath}`);
        return;
    }
    let content = fs.readFileSync(filepath, 'utf8');
    for (const [k, v] of Object.entries(replacements)) {
        content = content.split(k).join(v);
    }
    fs.writeFileSync(filepath, content, 'utf8');
    console.log(`Translated ${filepath}`);
}

translateFile(path.join(__dirname, '../wiki/Module/Minion_SLASH_UI.md'));
translateFile(path.join(__dirname, '../wiki/Module/Minion_SLASH_Templates.md'));
translateFile(path.join(__dirname, '../wiki/Template/Bawaan/Minion_ideal_layout_SLASH_doc.md'));
translateFile(path.join(__dirname, '../wiki/Template/Bawaan/Minion_Drops_Table_SLASH_doc.md'));
translateFile(path.join(__dirname, '../wiki/Template/Bawaan/Minion_profit_table_SLASH_doc.md'));
translateFile(path.join(__dirname, '../wiki/Template/Bawaan/Minion_stats_table_SLASH_doc.md'));

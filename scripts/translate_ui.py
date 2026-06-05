import os

replacements = {
    # Module:Minion/UI
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

    # Module:Minion/Templates
    "No Description": "Tidak ada deskripsi",
}

def translate_file(filepath):
    if not os.path.exists(filepath):
        print(f"Not found: {filepath}")
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for k, v in replacements.items():
        content = content.replace(k, v)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Translated {filepath}")

translate_file('e:/Project Wiki/wiki/Module/Minion_SLASH_UI.md')
translate_file('e:/Project Wiki/wiki/Module/Minion_SLASH_Templates.md')

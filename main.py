"""
Semua bahasa pemrograman terdiri dari 3 blok dasar:
1. Sequencing (urutan)
2. Percabangan (Branching)
3. Perulangan (Looping)
"""

# Sequential (Urutan)

print('Ibu memerintah budi,"Pergi ke toko."')
print('Budi menjawab,"Baik, apa yg harus saya lakukan di toko?"')
print('Ibu menjawab,"Beli 1 botol susu, dan jika ada telor beli 6"')
print('Maka Budi berangkat ke toko')
print('Budi mulai belanja')

# Branching (Percabangan)

jumlah_botol_susu = 173
jumlah_telor = 11
print(f"Jumlah Botol Susu:{jumlah_botol_susu} botol")
print(f"Jumlah Telor:{jumlah_telor} butir")

if jumlah_botol_susu > 0:
    print('Budi mengecek harga susu dan uangnya cukup')
    print('Budi mebeli 1 botol susu')
else:
    print('Budi tidak jadi beli susu')

print('Budi lanjut belanja')

if jumlah_telor >= 6:
    print('Budi beli telor 6 butir')
else:
    print(f'Budi beli telor {jumlah_telor}')

print('Budi pulang ke rumah')
print('Budi menyampaikan hasil belanja ke Ibu')

"""
Looping - while, program baca buku sampai paham
"""

jumlah_buku = 10
print(f'Jumlah buku: {jumlah_buku}')
print('Ibu menyuruh, "Baca semua bukumu sampai paham"')

total_baca = 0
jumlah_buku_dibaca_paham = 0
print(f'Total buku sudah dibaca: {total_baca}')
print(f'Jumlah buku yg sudah dibaca dan dipahami: {jumlah_buku_dibaca_paham}')

while total_baca < jumlah_buku*2:
    total_baca = total_baca+1
    if jumlah_buku_dibaca_paham < jumlah_buku-1:
       jumlah_buku_dibaca_paham = jumlah_buku_dibaca_paham + 1
       print(f'Buku ke {jumlah_buku_dibaca_paham} sudah dibaca dan paham')
    else:
        print(f'Buku ke {jumlah_buku_dibaca_paham+1} belum paham')

print(f'Total baca: {total_baca}')



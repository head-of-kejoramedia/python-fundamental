daftar_buku = ['Seven Habits', 'How to Influence People', 'First Thing First']
print('Tampilkan Variable')
print (daftar_buku)

print('\nProses semua dengan for in')
for buku in daftar_buku:
    print(buku)

print ('\nTampilkan indeks tertentu dari daftar buku')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nTampilkan dengan for in range')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Thing First','4DX',101]
print(daftar_buku[0:2])

for i in range(0,len(daftar_buku)):
    print (i)

print('\n')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
print('\nTambahkan 1 Buku Baru')
print(daftar_buku.append('Dunia Matematika'))

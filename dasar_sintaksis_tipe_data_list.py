"""
Dasar Sintaksi Tipe Data List
"""

daftar_buku = ['Seven Habits','How to Influence People','First Thing First']

print('\n1# Membuat List, Print Standar dan Print for-in ')
print(daftar_buku)
print('\n')
for i in daftar_buku:
    print(i)

for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\n2# Print Index Tertentu Dari List')
print(daftar_buku[1])
print(daftar_buku[0])
print(daftar_buku[0:1])
print(daftar_buku[1:3])

print('\n3#Menambahkan List Dengan .append')
daftar_buku.append('4DX')
print(daftar_buku)

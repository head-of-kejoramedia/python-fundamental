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
for i in daftar_buku:
    print(i)

print('\n4#List Python Bisa Campur (Integer - String) dan Dinamis (Bisa Didefinisikan Ulang)')
daftar_buku = [12,'Kenji Volume 3',-313,3.14]
print(daftar_buku)

print('\n5# Menghapus List')
daftar_buku.clear()
print(daftar_buku)
for i in daftar_buku:
    print(i)

print('\n6# Mengganti Elemen List')
daftar_buku = ['Seven Habits','How to Influence People','First Thing First', '4DX','Dunia Matematika']
daftar_buku[0] = 'Eight Habits'
print(daftar_buku)

print('\n7# Mengambil dan Menaruh di Variable Baru Elemen List Menggunakan Pop')
buku = daftar_buku.pop(0)
print(buku)
print(daftar_buku)

daftar_buku = ['Seven Habits','How to Influence People','First Thing First', '4DX','Dunia Matematika']
print(daftar_buku.pop())

daftar_buku = ['Seven Habits','How to Influence People','First Thing First', '4DX','Dunia Matematika']
print(daftar_buku.pop(-2))

print('\n8# Menghapus Dengan Perintah Del + List Comprehension')

daftar_buku = ['Seven Habits','How to Influence People','First Thing First', '4DX','Dunia Matematika']
del daftar_buku[0]
print(daftar_buku)
del daftar_buku[0:2]
print(daftar_buku)
print('\n#List Comprehension')
del daftar_buku[:]
print(daftar_buku)
daftar_buku = ['Seven Habits','How to Influence People','First Thing First', '4DX','Dunia Matematika']
del daftar_buku[0:]
print(daftar_buku)

print('\n9# Membuat List Baru Dengan List Comprehension')

daftar_buku = ['Seven Habits','How to Influence People','First Thing First', '4DX','Dunia Matematika']
buku_favoritku = daftar_buku[0:3]

print(buku_favoritku)

print('\n10# Simpel Code Menggunakan List Comprehension')

# Without List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# Using List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)

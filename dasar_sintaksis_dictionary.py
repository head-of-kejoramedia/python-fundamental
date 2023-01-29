"""
Memahami Tipe Data Dictionary
"""
print('\n#1. Dasar Type Data Dictionary')
users = {"id": 1,
"name": "Leanne Graham",
"username": "Bret",
"email": "Sincere@april.biz"}

print(users["email"])

print('\n')

print(users)
print(users["id"])
print(users["name"])
print(users["username"])
print(users["email"])

print('\n#2. Type Data Dictionary Lebih Kompleks')
users = {"id": 1,
"name": "Leanne Graham",
"username": "Bret",
"email": "Sincere@april.biz",
"Adress": {
    "Street" : "Jl. Doar Selatan",
    "No." : 1,
    "District" : "Liangjulang - Kadipaten",
    "City" : "Majalengka",
    "Zip Code" : 45452,
    "Geo" : {"Lat" : -37.654, "Long" : 67.234}}
         }
print(users)
print(users["name"])
print(users["username"])
print(users["email"])
print(users["Adress"])
print(users["Adress"]["Street"])
print(users["Adress"]["Geo"]["Lat"])
print(users["Adress"]["Geo"]["Long"])

print('\n#3. Mengubah Type Data Dictionary ke JSON')
# Mengubah ke JSON Sting json.dumps

print(users)
print(type(users))

import json
result = json.dumps(users)
print(result)
print(type(result))

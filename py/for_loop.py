# list sebagai iterable
gorengan = ['bakwan','cireng','tahu isi','tempe goreng','ubi goreng']

for g in gorengan:
    print(g)
    print(len(g))

print("===========================")
# string sebagai iterable

bakwan = 'bakwan'

for i in bakwan:
    print(i)

print("===========================")
# for dalam for

buah = ['semangka','jeruk','apel','angur']
sayur = ['kangkung','wortel','tomat','kentang']

daftar_belanja = [gorengan,buah,sayur]

for subdaftarbelanja in daftar_belanja:
    print(subdaftarbelanja)
    for komponen in subdaftarbelanja:
        print(komponen)

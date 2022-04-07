barang = ['kunci','ember','jaket','ban','mobil']
print(barang)

## beberapa method yang bisa digunakan untuk menipulasi list
# method untuk menambahkan data kedalam list
barang.append('sepeda')
print(barang)

barang.extend('dompet')
print(barang)

barang.insert(3,'sepeda')
print(barang)

# method untuk menghitung anggota
jumlahsepeda = barang.count('sepeda')
print("jumlah sepeda adalah:", jumlahsepeda)

# meremove data
barang.remove('sepeda')
print(barang)

barang.reverse()
print(barang)

stuff = barang.copy()
stuff.append('gelas')
print(stuff)
print(barang)
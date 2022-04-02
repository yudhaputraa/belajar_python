# operasi dalam bentuk methods

## merubah case dari string

# merubah semua ke upper case

salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lower case
alay = "aKu keCe AbieezZzZZZ"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

## pengecekan dengan isX method

# contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() # hasilnya bool
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper()  # hasilnya bool
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <-- utk mengecek semuanya huruf
# isalnum() <-- huruf dan angka
# isdecimal() <-- angka saja
# isspace() <-- spasi, tab, newline \n
# istitle() <-- semua kata dimulai dgn huruf besar

judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle() # hasil bool
print(judul + "is title = " + str(cek_judul))

## ngecek komponen startswith() dan endswith() <--keren
cek_start = "sangjangnim oppa".startswith("sangjangnim")
print("start = " + str(cek_start))

cek_end = "sangjangnim oppak".endswith("oppa")
print("end = " + str(cek_end))

## penggabungan komponen join() split()
pisah = ['aku','saya','kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = 'em'.join(pisah)
print(gabungan)

gabungan = "akuemsayaemkamu"
print(gabungan.split('em'))

## alokasi karakter rjust(), ljust(), center()

kanan = "kanan".rjust(10)
print("'" + kanan + "'")

center = "tengah".center(10)
print("'" + center + "'")

kiri = "kiri".ljust(10)
print("'" + kiri + "'")

center = "tengah".center(20,"-")
print("'" + center + "'")

# keblikannya -> strip()
center = "tengah".strip("-") # menghilangan kan tanda -
print("'" + center + "'")

kanan = "kanan".strip()
print("'" + kanan + "'")


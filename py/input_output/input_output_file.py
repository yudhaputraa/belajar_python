# input output file

# membuat fie text
"""
w = write mode / mode menulis dan menghapus file lama, jika file tdk ada maka akan dibuat file baru
r = read only / hanya bisa baca
a = appending mode / menambahkan data di akhir baris
r+ = write and read mode
"""
# membuat file txt
file = open("data.txt",'w')

file.write("ini adalah data text yang dibuat dengan mengguakan python")
file.write("\nini baris kedua")
file.write("\nini baris ketiga")
file.write("\nini baris keempat")
file.close()

# membaca file text

file2 = open("data.txt",'r')

# ini hanya menampilkan 10 huruf
#print(file2.read(10))

# ini akan hanya menampilkan satu baris
print(file2.readline())
file2.close()

# appending mode

file3 = open("data.txt",'a')
file3.write('\nbaris ini di buat dengan menggunakan mode append')

file.close()
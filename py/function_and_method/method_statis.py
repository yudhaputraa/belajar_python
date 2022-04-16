"""
    Static method di dalam python adalah sebuah fungsi atau method pada sebuah kelas yang bersifat statis. 
Bersifat statis di sini berarti kita bisa memanggil fungsi tersebut secara langsung tanpa harus membuat 
instan dari kelas yang bersangkutan
"""

class aritmetika:

    @staticmethod
    def tambah(a,b):
        hasil = a + b
        print(a,'+',b,'=', hasil)

    @staticmethod
    def kurang(a,b):
        hasil = a - b
        print(a,'-',b,'=', hasil)

    @staticmethod
    def kali(a,b):
        hasil = a * b
        print(a,'*',b,'=', hasil)

    @staticmethod
    def bagi(a,b):
        hasil = a / b
        print(a,'/',b,'=', hasil)


# memangilan metode tanpa membuat objek
# dari kelas aritmetika
print("memangilan metode tanpa membuat objek")
aritmetika.tambah(10,5)
aritmetika.kurang(10,5)
aritmetika.kali(10,5)
aritmetika.bagi(10,5)


# membuat objek dari kelas aritmatika
obj = aritmetika()

# memangil method statis melalui objek
print('memangil method statis melalui objek')
obj.tambah(3,4) 
obj.kurang(3,4) 
obj.kali(3,4) 
obj.bagi(3,4) 

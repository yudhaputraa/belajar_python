class induk:
    def metode1(self):
        print("induk.metode1()")
    def metode2(self):
        print('induk.metode2()')

class anak(induk):
    # melakukan override terhadap induk.metode2()
    def metode2(self):
        print('anak.metode2()')

# membuat objek dari class anak
obj = anak()

# memanggil metode induk.metode1()
obj.metode1()

# memanggil metode anak.metode2()
obj.metode2()

"""
jika anda ingin tetep mempertahankan perilaku metode 
milik class induk dan anda hanya ingin menambah kode 
ke dalam method tersebut. maka anda dapat menggunakan 
metode super() untuk memanggil metode milik class induk 
dari class anak.

"""

class induk1:
    def contohmetode(self):
        print('implementasidi dalam class induk')


class ana1k(induk1):
    # override metode contohmetode()
    def contohmetode(self):
        # mempertahankan perilaku dari class induk
        super().contohmetode()
        # tambah kode di dalam class anak
        print('implementasi tambahan di dalam class anak')


# membuat objek dari class anak
obj1 = ana1k()

# memanggil method contohmethod()
obj1.contohmetode()
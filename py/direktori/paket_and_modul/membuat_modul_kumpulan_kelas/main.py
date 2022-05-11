# mengimpor modul myclasses
import myclasses

"""
TODO: Utk Alias
- import myclasses as mc
jika mau mengakses myclasses, maka tdk bisa, sudah digantikan mc

TODO: Mengimport Semua Anggota Modul
- from myclasses import *
tanda asterisk (*) yg terdapat pada perintah from..import menandakan
bahwa kita mengimport semua anggota yg terdapat pd file myclasses.py,
jika ingin hanya beberapa aja yg akan diimport maka tanda (*) di ganti
dgn nama modul
"""

def main():
    # membuat objek dari Kelas A
    a = myclasses.A()
    
    # membuat objek dari Kelas B
    b = myclasses.B()
    
    # membuat objek dari Kelas C
    c = myclasses.C()
    
    # memanggil metode dalam Kelas A,B, dan C
    a.metode()
    b.metode()
    c.metode()
    
if __name__ == "__main__":
    main()
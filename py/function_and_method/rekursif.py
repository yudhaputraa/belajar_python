def faktorial(n):
    if n == 0:
        print('if', n)
        return 1
    else:
        print('else', n)
        return n + faktorial(n-1)

t = faktorial(5)
print(t)

"""
fungsi rekursif merupakan sebuah metode perulangan yang bersifat non-iterasi. Sebenarnya 
fungsi rekursif hanyalah sebuah fungsi biasa seperti fungsi def pada umumnya. Dia bisa dipanggil, 
bisa menerima parameter, bisa mengembalikan nilai, dan lain sebagainya.

Rekursif adalah proses pemanggilan dirinya sendiri (fungsi atau prosedur). - Fungsi maupun 
prosedur yang memanggil dirinya disebut fungsi atau prosedur rekursif. - Fungsi antuk suatu 
bagian program yang mengembalikan (menghasilkan) hanya satu nilai.
"""
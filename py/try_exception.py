print("ini adalah program pembagian")

while True:
    try:
        #import panda
        penyebut = int(input("masukan angka penyebut:"))
        pembilang = int(input("masukan angka pembilang"))
        break
    except ValueError:
        print("yang anda masukan bukan angka\n")
    except ZeroDivisionError:
        print("angka pembilangan yang anda masukan adalah nol, pilih yang lain ya bro")
    except ImportError:
        print("gak ada modul bro")
    except Exception as gg:
        print(gg)

"""
    type of exception errors:
    1, IOError
    2, ImportError
    4, ValueError
    5, Division by zero
    6, EOFError
"""
# print("berhasil, hasil pembagian adalah: ", hasil)
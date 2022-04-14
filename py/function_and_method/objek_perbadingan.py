print(' ')
print("==== Metode ===|=== Keterangan ========================================")
print("| __eq__()     |Metode untuk melakukan overload terhadap operasi ==   |")
print("| __ne__()     |Metode untuk melakukan overload terhadap operasi !=   |")
print("| __lt__()     |Metode untuk melakukan overload terhadap operasi <    |")
print("| __le__()     |Metode untuk melakukan overload terhadap operasi <=   |")
print("| __gt__()     |Metode untuk melakukan overload terhadap operasi >    |")
print("| __ge__()     |Metode untuk melakukan overload terhadap operasi >=   |")
print("=======================================================================")

class Lingkaran:

    def __init__(self, r):
        self.__jarijari = r
    
    # oeverload operasi ==
    def __eq__(self, objek):
        return self.__jarijari == objek.__jarijari
    
    # oeverload operasi !=
    def __ne__(self, objek):
        return self.__jarijari != objek.__jarijari

    # oeverload operasi <
    def __lt__(self, objek):
        return self.__jarijari < objek.__jarijari

    # oeverload operasi <=
    def __le__(self, objek):
        return self.__jarijari <= objek.__jarijari

    # oeverload operasi >
    def __gt__(self, objek):
        return self.__jarijari > objek.__jarijari
    
    # oeverload operasi >=
    def __ge__(self, objek):
        return self.__jarijari >= objek.__jarijari

    # menghitung luas
    def luas(self):
        import math
        return math.pi * pow(self.__jarijari,2)

    # menghitung keliling
    def keliling(self):
        import math
        return 2 * math.pi * self.__jarijari

# objek pertama
objek1 = Lingkaran(3)

# objek kedua
objek2 = Lingkaran(5)

# objek ketiga
objek3 = Lingkaran(3)
    


# membandingkan objek

## menggunakan operasi ==
a =  objek1 == objek2
print(a)
b = objek1 == objek3
print(b)

## menggunakan operasi <
c = objek1 < objek2
print(c)

## menggunakn operasi >
d = objek2 > objek3
print(d)

## menggunakan operasi >=
e = objek1 >= objek3
print(e)
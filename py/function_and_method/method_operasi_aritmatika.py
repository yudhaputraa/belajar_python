class Bilangan:

    def __init__(self, nilai):
        if isinstance(nilai, int) or isinstance(nilai, float):
            self.nilai = nilai
        else:
            raise TypeError('Parameter harus bertipe numeric')
    
    # overload opera +
    def __add__(self, x):
        if isinstance(x, Bilangan):
            return self.nilai + x.nilai
        elif isinstance(x,int):
            return int(self.nilai) + x
        elif isinstance(x, float):
            return float(self.nilai) + x
        else:
            raise TypeError('Objek harus bertipe numerik')
    
    # overload opera -
    def __sub__(self, x):
        if isinstance(x, Bilangan):
            return self.nilai - x.nilai
        elif isinstance(x,int):
            return int(self.nilai) - x
        elif isinstance(x, float):
            return float(self.nilai) - x
        else:
            raise TypeError('Objek harus bertipe numerik')
    
    # overload opera *
    def __mul__(self, x):
        if isinstance(x, Bilangan):
            return self.nilai * x.nilai
        elif isinstance(x,int):
            return int(self.nilai) * x
        elif isinstance(x, float):
            return float(self.nilai) * x
        else:
            raise TypeError('Objek harus bertipe numerik')

    # overload opera /
    def __truediv__(self, x):
        if isinstance(x, Bilangan):
            return self.nilai / x.nilai
        elif isinstance(x, int):
            return int(self.nilai) / x
        elif isinstance(x, float):
            return float(self.nilai) / x
        else:
            raise TypeError('Objek harus bertipe numerik')

# membuat objek dari class Bilangan
nilai1 = Bilangan(10)
nilai2 = Bilangan(3)

# operasi antara objek bilangan dgn  objek bilangan
print('operasi antara objek bilangan dgn  objek bilangan')
a = nilai1 + nilai2
print(a)
b = nilai1 - nilai2
print(b)
c = nilai1 * nilai2
print(c)
d = nilai1 / nilai2
print(d) 


# operasi antaraobjek bilangan dengan objek int
print('operasi antaraobjek bilangan dengan objek int')
e = nilai1 + 2
print(e)
f = nilai1 - 6
print(f)
g = nilai2 * 3 
print(g)
h = nilai1 / 2
print(h) 


# operasi antaraobjek bilangan dengan objek float
print('operasi antaraobjek bilangan dengan objek float')
i = nilai1 + 3.5
print(i)
j = nilai1 - 2.5
print(j)
k = nilai1 * 2.0
print(k)
l = nilai1 / 2.5
print(l)

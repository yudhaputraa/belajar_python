class aritmetika:

    def tambah(self, *daftarnilai):

        total = 0

        for i in daftarnilai:
            total += i

        return total


# membuat objekdari class aritmatik
obj = aritmetika()

# memanggil method tambah() dengan dua parameter
a = obj.tambah(1,2)
print(a)

# memanggil method tambah() dengan tiga parameter
b = obj.tambah(20,5,10)
print(b)

# memanggil method tambah() dengan empat parameter
b = obj.tambah(20,5,10,50)
print(b)
# membuka file
f = open('C:\python\direktori\data\data.txt','r')

# membaca per karakter mengunakan while
karakter = f.read()
print(karakter)
#while karakter:
#    print(karakter, end=' ')
#    karakter = f.read()


# membaca per karakter mengunakan for
#for ikarakter in f.read():
#    print(ikarakter, end=' ')

# menutup file
#f.close()
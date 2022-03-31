angka = 0 

#while angka < 5:
#    print('nilai angka adalah : ',angka)
#    angka = angka + 1
#print("di luar while")

start = True
angka = 0

while start:
    print("di dalam while")
    if angka == 10:
        start = False
        print('oke angka 10 diketemukan')
    angka += 1
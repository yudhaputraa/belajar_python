# mendefinisikan fungsi
#def fungsi():
#    print('ini adalah fungsi')
# memanggil fungsi
#fungsi()
#==============================
# membuat fungsi sederhana

def suaraayam():
    print('kukuruyuk')

def hargaayam():
    suaraayam()
    print("hargaayam per 1 kg adalah Rp. 20.000")

# membuat fungsi dengan input argumen
def hargatotalayam(kg):
    harga = 20000
    hargatotal = kg*harga
    print('harga',kg,'ayam adalah',hargatotal)

hargaayam()
hargatotalayam(2)
hargatotalayam(0.5)
hargatotalayam(1)
hargatotalayam(9)
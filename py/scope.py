# scope variable : local

#namakucing = 'cassandra' # <-- ini variabel global 

#def rubahnamakucing(namabaru):
#    namakucing = namabaru # <--- ini variabel local
#    print('saya rubah nama kucing menjadi',namakucing)

#rubahnamakucing('ketie')
#print('nama kucing saya menjadi',namakucing)

# scope variable : cara menjadikan variable local menjadi variable global

namakucing = 'cassandra' # <-- ini variabel global 
makanankucing = 'royal canin'

def rubahnamakucing(namabaru):
    global namakucing # <-- ini adalah untuk menjadikan variabel global
    namakucing = namabaru # <--- ini variabel local
    print('saya rubah nama kucing menjadi',namakucing)

def kasihmakankucing(makan,nama):
    global namakucing,makanankucing
    namakucing = nama
    makanankucing = makan

rubahnamakucing('ketie')
kasihmakankucing('universal','alex')
print('nama kucing saya menjadi',namakucing,'dan makan',makanankucing)

 # teknik looping

nama_band = ['aku sama mu',
             'sendiri lagi',
             'kesepian',
             'bersama sebentar',
             'kenapa jomblo',
             'anak kemarin']

kumpulan_lagu = ['akad',
                 'zona nyaman',
                 'rumahku',
                 'sang filsuf',
                 'sindoro',
                 'mawang']

# di bawah ini adalah cara lama
#iterasi=0
#for band in nama_band:
#    print('no:',iterasi,'nama band:',band)
#    iterasi+=1

# enumerate

for i,band in enumerate(nama_band):
    print(i,':',band)

print("="*20)
# zip

for band,lagu in zip(nama_band,kumpulan_lagu):
    print(band,'menyanyikan lagu yang berjudul:',lagu)

print("="*20)

playlist ={'baby baby','ada apa dengan cinta','cenat-cenut','jaran goyang','gorgom','kuda','kucing'}

for lagu in sorted(playlist):
    print(lagu)

print("="*20)

# dictionary
playlist2 = {'aku sama mu':'akad',
             'sendiri lagi':'zona nyaman',
             'kesepian':'rumah ku'}

for k,v in playlist2.items():  # items() bisa di ganti dengan value(),keys()
    print(k,'lagunya:',v)

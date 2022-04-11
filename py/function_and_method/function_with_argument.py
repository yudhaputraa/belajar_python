# fungsi dengan menggunakan argumen sederhana
def siswa(nama):
    print('siswa ini bersama : ',nama)

#siswa('mario')

# fungsi dengan menggunakan keywords  arguments

def guru(nama,pelajaran):
    print('guru ini bernama',nama)
    print('mengajar',pelajaran)

#guru(nama='popong',pelajaran='seni rupa')
#guru(pelajaran='olahraga',nama='endang')
#guru('Tik','pangga') <-- ini conto yang salah

# fungsi dengan  menggunakan  default arduments

def penjagasekolah(nama,shift='siang',galak='tidak'):
    print('penjaga sekolah ini bernama:',nama)
    print('shiftnya:',shift)
    print('galak?:',galak)

penjagasekolah('entis') 
print('==================')
penjagasekolah('mamang',shift='malam') 
print('==================')
penjagasekolah('asep',galak='sangat') 
print('==================')
# dibawa ini akan menyebabkan error
#penjagasekolah(shift='pagi','bule') 
#penjagasekolah(shift='pagi',galak='IYA') 

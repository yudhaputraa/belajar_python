# class
class mahasiswa():
#   nama = 'yudha'
    def __init__(self, input_nama, input_nim):
        self.nama = input_nama
        self.nim = input_nim
    def belajar(self, kondisi):
        print(self.nama,'sedang belajar', kondisi)
    def tidur(self):
        print(self.nama,'tidur di kelas')

## main programmer

# otong adalah sebuah instanes dan mahasiwa() adalah sebuah class
#otong = mahasiswa()
#mamang = mahasiswa()

#print(otong)
#print('='*20)

#otong.nama = "surotong"
#mamang.nama = "emak"

#print(otong.nama)
#print(mamang.nama)
#print('='*20)

#otong.belajar("dengan semangat")
#mamang.tidur()

# dibawah ini adalah intenses
otong = mahasiswa("surotong", 243534)


print(otong.nama)
print(otong.nim)

otong.belajar('gdfth')
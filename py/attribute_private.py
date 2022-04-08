# class
class mahasiswa():
    __nilai = 0 # <-- ini adalah variabel/attribute private

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama  # <-- ini adalah variabel/attribute public
        self.nim = input_nim  # <-- ini adalah variabel/attribute public

    def uts(self,input_nilai):
        self.__nilai += input_nilai
        print(self.nama, 'nilai uts anda :', input_nilai)

    def uas(self,input_nilai):
        self.__nilai += input_nilai
        print(self.nama, 'nilai uas anda :', input_nilai)

    def check_status(self):
        if self.__nilai <= 50:
            print(self.nama,'anda tidak lulus')
        else:
            print(self.nama, 'lulus')
    

ucup = mahasiswa("michael ucup", 243534)
print(ucup.nama)
print(ucup.nim)
ucup.uts(20)
ucup.uas(20)
ucup.check_status()
print("="*20)

otong = mahasiswa("surotong", 243534)
print(otong.nama)
print(otong.nim)
otong.uts(50)
otong.uas(20)
otong.check_status()
print("="*20)

# class
class mahasiswa():
    
    jurusan = "ekonomi" # <-- ini adalah namanya variabel class 
    jumlah_mahasiswa = 0

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama  # public
        self.nim = input_nim  # public
        mahasiswa.jumlah_mahasiswa += 1


ucup = mahasiswa("michael ucup", 243534)
print(mahasiswa.jumlah_mahasiswa)
otong = mahasiswa("surotong", 243534)

otong.jurusan = "ekonomi mikro" # <-- ini adalah variabel intenses

print(mahasiswa.jurusan)
print(otong.jurusan)
print(ucup.jurusan)

print(mahasiswa.jumlah_mahasiswa)
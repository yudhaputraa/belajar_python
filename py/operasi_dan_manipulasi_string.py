data_garis = "====="*5

# operasi dan manipulasi string

# 1. manyambung string (concatenate)
nama_pertama = "yudha"
nama_tengah = "D"
nama_akhir = "Fame"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

# 2. menghitung panjang string
panjang = len(nama_lengkap)
print(panjang)

# 3. operator untuk string

# mengecek apakah ada komponen char atau string di string

d = "d"
status = d in nama_lengkap
print(d + "tdk ada di " + nama_lengkap + " = " + str(status))

# mengulangan string
print("wk"*5)
print(5*"wk")

# indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-6 : " + nama_lengkap[6])
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-(-2) : " + nama_lengkap[-2])
print("index ke-[0:3] : " + nama_lengkap[0:4])
print("index ke-[3:7] : " + nama_lengkap[3:8])
print("index ke-[0,2,4,6,8,10] : " + nama_lengkap[0:11:2])

# item paling kecil
print("paling kecil : " + min(nama_lengkap))
# item paling besar
print("paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code utk spasi adalah " + str(ascii_code))
data = 177
print("char utk ASCII ",data ," adalah " + chr(data))

# 4. operasi dalam bentuk method
data = "otong surotong paraotong"
jumlah = data.count("o")
print("jumlah o pd " + data + " = " +str(jumlah))
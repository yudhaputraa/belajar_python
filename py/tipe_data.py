from ctypes import c_double
print("-------------------Contoh TIPE DATA-----------------")


print("----------(INTEGER)----------")
print("TIPE DATA : angka satuan yang gak ada komanya")
print("Contoh :")
data_integer = 11
print("Data : ", data_integer, " Bertipe : ", type(data_integer))


print("----------(Float)----------")
print("TIPE DATA : angka dengan koma")
print("Contoh :")
data_float = 1.5
print("Data : ", data_float, " Bertipe : ", type(data_float))


print("----------(STRING)----------")
print("TIPE DATA : kumpulan karakter")
print("Contoh :")
data_string = "ucup"
print("Data : ", data_string, " Bertipe : ", type(data_string))


print("----------(BOOLEAN)----------")
print("TIPE DATA : biner atau true/false")
print("Contoh :")
data_bool = True
print("Data : ", data_bool, " Bertipe : ", type(data_bool))


print("----------(BILANGAN KOMPLEKS)----------")
print("TIPE DATA KHUSUS : bilangan kompleks")
print("Contoh :")
data_complex = complex(5,6)
print("Data : ", data_complex, " Bertipe : ", type(data_complex))


print("----------(C_DOUBLE)----------")
print("TIPE DATA KHUSUS : tipe data dari bahasa C sebelum")
print("memakai harus impor dulu contoh:")
print("- from ctypes import c_double")
print("Contoh :")
data_c_double = c_double(10.5)
print("Data : ", data_c_double, " Bertipe : ", type(data_c_double))

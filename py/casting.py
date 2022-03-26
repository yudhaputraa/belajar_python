# KIta Belajar Casting
# Merubah dari satu tipe ke tipe lain
# Tipe data = int, float, str, bool

print("======integer========")
data_int = 11
print("Data : ", data_int, " Bertipe : ", type(data_int))
data_float = float(data_int)
print("Data : ", data_float, " Bertipe : ", type(data_float))
data_str = str(data_int)
print("Data : ", data_str, " Bertipe : ", type(data_str))
data_bool = bool(data_int)  # akan false jika nilainya  int = 0
print("Data : ", data_bool, " Bertipe : ", type(data_bool))


print("======float========")
data_float = 9.6
print("Data : ", data_float, " Bertipe : ", type(data_float))
data_int = int(data_float) #akan dibulatkan ke bawah
print("Data : ", data_int, " Bertipe : ", type(data_int))
data_str = str(data_float)
print("Data : ", data_str, " Bertipe : ", type(data_str))
data_bool = bool(data_float) #akan false jika nilainya  float = 0
print("Data : ", data_bool, " Bertipe : ", type(data_bool))


print("======boolean========")
data_bool = True
print("Data : ", data_bool, " Bertipe : ", type(data_bool))
data_int = int(data_bool) #akan dibulatkan ke bawah
print("Data : ", data_int, " Bertipe : ", type(data_int))
data_str = str(data_bool)
print("Data : ", data_str, " Bertipe : ", type(data_str))
data_float = float(data_bool)
print("Data : ", data_float, " Bertipe : ", type(data_float))


print("======string========")
data_str = "10"; #jika di isi dengan angka maka tidk error dan kalok di isi dengan huruf maka error
print("Data : ", data_str, " Bertipe : ", type(data_str))
data_int = int(data_str) #string harus angka
print("Data : ", data_int, " Bertipe : ", type(data_int))
data_float = float(data_str)  #string harus angka
print("Data : ", data_float, " Bertipe : ", type(data_float))
data_bool = bool(data_str) #juka nilai dari data_str kosong akan bernilai false jika di isi makan true
print("Data : ", data_bool, " Bertipe : ", type(data_bool))

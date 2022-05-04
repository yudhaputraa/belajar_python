import os
import math

# untuk mendapatkan ukuran file
a = os.path.getsize('C:\\Users\\ASUS\\OneDrive\\Dokumen\\python\\direktori\\data\\data.txt')
print(a)

# utk menampilkan ukuran dalam satuan kb
b = math.ceil(os.path.getsize('C:\\Users\\ASUS\\OneDrive\\Dokumen\\python\\direktori\\membaca_read.py') / 1024)
print(b,'KB')

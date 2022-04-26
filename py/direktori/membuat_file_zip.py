"""
Permasalahan seperti ini dapat diselesaikan dengan 
memanfaatkan modul zipfile 
"""

import os

# mengaktifkan direktori
os.chdir('C:\\Users\\ASUS\\OneDrive\\Dokumen\\python\\direktori\\data')

# menentukan daftar file yang akan ditambakan ke dalam file .zip
files = ['data.json','data.txt','pencipta.csv','test.txt']

# membuat file .zip
import zipfile
zf = zipfile.ZipFile("C:\\Users\\ASUS\\OneDrive\\Dokumen\\python\\direktori\\data\\test.zip","w", compression=zipfile.ZIP_DEFLATED)

# memasukan file ke dalam file .zip
for file in files:
    zf.write(file)
    
# menutup file .zip
zf.close()

# memeriksa keberadaan  file test.zip
cek = os.path.exists("C:\\Users\\ASUS\\OneDrive\\Dokumen\\python\\direktori\\data\\test.zip")
print(cek)
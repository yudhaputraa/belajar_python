import zipfile

zf = zipfile.ZipFile("C:\\Users\\ASUS\\OneDrive\\Dokumen\\python\\direktori\\data\\test.zip","r")

# menampilkan daftar file di dalam file .zip
for filename in zf.namelist():
    print(filename)
    

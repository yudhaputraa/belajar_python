import shutil

# memindahkan file
shutil.move("C:\\Users\\ASUS\\OneDrive\\Dokumen\\python\\direktori\\data\\test.zip", "C:\\Users\\ASUS\\OneDrive\\Dokumen\\python\\direktori\\test\\test.zip")

# memeriksa keberadaan  file yg di copy
import os
cek = os.path.exists("C:\\Users\\ASUS\\OneDrive\\Dokumen\\python\\direktori\\test\\test.zip")
print(cek)
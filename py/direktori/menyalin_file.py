def copyfile(sourcefile, destfile):
    f1 = open(sourcefile, 'r') # mode baca
    f2 = open(destfile, 'w') # mode tulis
    for data in f1.read():
        # menulis data ke f2
        f2.write(data)
    f2.close()
    f1.close()


copyfile("C:\\python\\direktori\\data\\data.txt",
         "C:\\python\\direktori\\test\\data.txt")

# atau dengan menggunaan shutil

# import shutil

# menyalin file
# shutil.copy()
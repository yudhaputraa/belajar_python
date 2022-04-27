"""
Untuk menghapus direktori kosong (tidak berisi file), anda perlu menggunakan 
fungsi rmdir() yg terdapat di dalam modulos. utk menghapus direktori yg sudah
berisi file maupun sub-direktori lain, gunakan fungsi rmtree() yg terdapat di 
dalam modul shutil
"""
import os

os.rmdir("C:\\python\\direktori\\data\\coba")

"""
#    PENJELASAN
* os.remove(), digunakan utk menghapus file.
* os.rmdir(), digunakan utk menghapus direktori kosong.
* shutil.rmtree, digunakan utk menghapus direktori beserta
  semua isi yg terdapat di dalam direktori tersebut.
"""
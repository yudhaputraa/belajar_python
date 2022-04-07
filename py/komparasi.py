# latihan logika komparasi
"""
TODO: 
    Operator perbandingan (comparison operators) digunakan untuk membandingkan suatu nilai 
dari masing-masing operan. bernilai True Jika masing-masing operan memiliki nilai yang sama, 
maka kondisi bernilai benar atau True. bernilai False Akan menghasilkan nilai kebalikan dari 
kondisi sebenarnya.
"""

# membuat gabungan area rentang dari angka

# +++++++3------10++++++++

inputuser = float(input("masukan yg bernilai kurang dari 3\natau\nlebih besar dari 10 :  "))

# +++++++3---------
# memeriksa angka kurang dari 3
iskurangdari = (inputuser < 3 )
print("kurang dari 3 : ",iskurangdari)
# ---------10+++++++++
# memeriksa angka lebih dari 10
islebihdari = (inputuser > 10 )
print("lebih dari 10 : ",islebihdari)

# +++++++3------10++++++++
isgabung = iskurangdari or islebihdari
print("angka yg ada masukan adalah : ",isgabung)

# --------3+++++++10-------
iskebalikan = not isgabung
print("angka yg ada masukan adalah : ",iskebalikan)
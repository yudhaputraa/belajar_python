# latihan logika komparasi

# membuat gabungan area rentang dari angka

# +++++++3------10++++++++

inputuser = float(input("masukan yg bernilai kurang dari 3\natau\nlebih besar dari 10 :  "))

# +++++++3---------
# memeriksa angka kurang dari 3
iskurangdari = (inputuser < 3 )
print("kurang dari 3 : ",iskurangdari)
# ---------3+++++++++
# memeriksa angka lebih dari 3
islebihdari = (inputuser > 3 )
print("lebih dari 3 : ",islebihdari)
print("")

# +++++++10---------
# memeriksa angka kurang dari 10
iskurangdari = (inputuser < 10 )
print("kurang dari 10 : ",iskurangdari)
# ---------10+++++++++
# memeriksa angka lebih dari 10
islebihdari = (inputuser > 10 )
print("lebih dari 10 : ",islebihdari)
print("")

# +++++++3------10++++++++
isgabung = iskurangdari or islebihdari
print("angka yg ada masukan adalah : ",isgabung)

# --------3+++++++10-------
iskebalikan = not isgabung
print("angka yg ada masukan adalah : ",iskebalikan)

# cara Sulitnya
# --------3+++++++10-------

# ---------3+++++++++
# memeriksa angka lebih dari 3
islebihdari = (inputuser > 3 )

# +++++++10---------
# memeriksa angka kurang dari 10
iskurangdari = (inputuser < 10 )

IsCorrect = iskurangdari and islebihdari
print("angka yg ada masukan adalah : ",IsCorrect)
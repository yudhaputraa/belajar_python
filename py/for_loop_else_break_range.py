#for i in range(0,40,5):
#  print(i)

#======================
# catatan untuk else di for
# else akan di eskusi/jalankan ketika for selesai di kerjakan
#for i in range(0,5):
#    print(i)
#else:
#    print("hallo")

#======================
# catatan untuk else di for ada break
# jika didalam ada break, dan break di jalankan maka else tidak dijalankan

number = int(input("masukan nilai 1 sampai 10 :"))

for i in range(0, 11):
  print(i)
  if i is number:
      print('angka di temukan',i)
      break
else:
    print('angka tidak ditemukan')
print("space di luar for")
# else, break, continue, pass di while

angka = 0

while angka < 10:
    if angka == 5:
        print('nilai sama dgn 5')
        # break : fungsinya utk mengakhiri while (terminasi)
        #angka += 1
        #continue
        """
        continue : fungsinya utk melanjutkan ke step berikutnya, jika
        di while akan terjadi loop tak terbatas maka di atas continue
        diberi parameter lagi contoh seperti di atas : angka += 1 
        """
        # pass : tdk pengaruh apa apa
    print('nilai angka adalah : ', angka)
    angka = angka + 1
else:
    print('nilai angka diakhirwhile adalah',angka)
print('diluar while')

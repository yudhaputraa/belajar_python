# membuat file
f = open('C:\python\direktori\data\data.txt', 'w')

# data yang akan ditulis ke file
data = [
    'mengunakan writelines \n',
    'baris pertama \n',
    'baris kedua \n',
    'baris ketiga \n',
    'baris keempat \n',
    'baris kelima \n'
]

# menulis data ke file
f.writelines(data)

# penutup
f.close()

print("######## OPERASI ARITMATIKA ########")
# prioritas operasi, operasional precedence
'''
    1.()
    2.exponen **
    3.perkalian dan teman-teman * / ** %  //
    4.pertambahan dan pengurangan
'''
a = 10
b = 3

# Oprasi tambah +
hasil = a + b
print(a, '+', b, '=', hasil)

# Oprasi pengurangan -
hasil = a - b
print(a, '-', b, '=', hasil)

# Oprasi perkalian *
hasil = a * b
print(a, '*', b, '=', hasil)

# Oprasi pembagian /
hasil = a / b
print(a, '/', b, '=', hasil)

# Oprasi eksponen(pangkat) **
hasil = a ** b
print(a, '**', b, '=', hasil)

# Oprasi modulus(Sisa pembagian) %
hasil = a % b
print(a, '%', b, '=', hasil)

# Oprasi floor division //
hasil = a // b
print(a, '//', b, '=', hasil)

x = 3
y = 2
z = 4
# Kurung akan mengambil langkah paling pertama
hasil = x ** y * (z + x) / y - y % z // x
print(x,'**',y,'* (',z,'+',x,') /',y,'-',y,'%',z,'//',x,'=',hasil)

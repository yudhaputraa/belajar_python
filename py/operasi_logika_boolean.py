# operasi logika atau boolean

# not,or, and, xor

#NOT
#not adalah nilai kebalikan/negasi
print('======Not============================')
a = True
b = False
c = not a
d = not b
print('data c dari data a hasilnya = ',c)
print('data d dari data b hasilnya = ',d)

# OR
# jika salah satu true, maka hasilnya adalah true
print('======OR==============')
a = False
b = False
e = a or b
print(a,'OR',b,'=',e)
a = False
b = True
e = a or b
print(a,'OR',b,' =',e)
a = True
b = False
e = a or b
print(a, ' OR', b, '=', e)
a = True
b = True
e = a or b
print(a, ' OR', b, ' =', e)

# AND
# jika salah satu false, maka hasilnya adalah false
print('======AND==============')
a = False
b = False
e = a and b
print(a,'AND',b,'=',e)
a = False
b = True
e = a and b
print(a,'AND',b,' =',e)
a = True
b = False
e = a and b
print(a, ' AND', b, '=', e)
a = True
b = True
e = a and b
print(a, ' AND', b, ' =', e)

# XOR
# akan true jika salah satu true, sisanya false
print('======XOR==============')
a = False
b = False
e = a ^ b
print(a,'XOR',b,'=',e)
a = False
b = True
e = a ^ b
print(a,'XOR',b,' =',e)
a = True
b = False
e = a ^ b
print(a, ' XOR', b, '=', e)
a = True
b = True
e = a ^ b
print(a, ' XOR', b, ' =', e)

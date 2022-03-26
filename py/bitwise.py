# operasi operator bitwise, operasi biner, binery
a = 9
b = 5
print('nilai :',a,'binary :',format(a,'08b'))
print('nilai :',b,'binary :',format(b,'08b'))
# bitwise or  (|)
print("=========OR========")
c = a | b
print('nilai :',c,'binary :',format(c,'08b'))
print("===================")
# bitwise and  (&)
print("=========AND=======")
d = a & b
print('nilai :',d,'binary :',format(d,'08b'))
print("===================")
# bitwise xor  (^)
print("=========XOR=======")
e = a ^ b
print('nilai :',e,'binary :',format(e,'08b'))
print("===================")
# bitwise NOT  (~)
print("=========NOT=======")
f = ~a
print('nilai :',f,'binary :',format(f,'08b'))
print("===================")

g = 0b0000001001
h = 0b1111111111
print('nilai :', g ^ h, 'binery :', format(g^h, '08b'))

# shifting

# shift right (>>)
print("=========>>========")
i = a >> 2
print('nilai :', i, 'binary :', format(i, '08b'))
print("===================")

# shift left (<<)
print("=========<<========")
j = a << 2
print('nilai :', j, 'binary :', format(j, '08b'))
print("===================")

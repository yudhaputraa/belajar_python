# fungsi dengan return value
def kuadrat(argumen):
    total = argumen**2
    print('nilai kuadrat dari',argumen,'adalah',total)
    return total

a = kuadrat(3)
print(a)
# print(kuadrat(5))
print('='*15)

# fungsi dengan reirn value dan multiple argumen
def tambah(argumen1,argumen2):
    total = argumen1 + argumen2
    print('penambahan')
    print(argumen1,'+',argumen2,'=',total)
    return total
a = tambah(3,4)
print(a)

print('='*15)

def kali(argumen1, argumen2):
    total = argumen1 * argumen2
    print('perkalian')
    print(argumen1, 'x', argumen2, '=', total)
    return total
a = kali(3, 4)
print(a)

print('='*15)

a = tambah(3,4)
b = kali(3,a)
print(b)

print('='*15)

c = kali(3,tambah(3,4))
print(c)
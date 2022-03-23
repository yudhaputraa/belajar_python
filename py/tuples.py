import sys
import timeit

# list
ganjil = [1,3,5,7,9]

# tuple
genap = (2,4,6,8,10)

print(type(ganjil))
print(type(genap))

# ini untuk mengetahui apa saja bisa di gunakan dengan dir
#print(dir(ganjil))
#print(dir(genap))
print('='*15)

data_list = [1,2,3,4,5,"pisang goreng","syahrini","via vallen", False,3.14]
data_tuple = (1,2,3,4,5,"pisang goreng","syahrini","via vallen", False,3.14)

besar_datalist = sys.getsizeof(data_list)
besar_datatuple = sys.getsizeof(data_tuple)

print("besar data list:",besar_datalist)
print("besar data tuple:",besar_datatuple)

print('='*15)

data_list = timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9]",number=1000000)
data_tuple = timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9)",number=1000000)


print("waktu untuk memproses list:",data_list)
print("waktu untuk memproses tuple:",data_tuple)


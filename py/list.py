data = [1,4,9,16,25,36,49,64]

#mengakses list
subdata1 = data[3]
subdata2 = data[-3]

# memotong list
subdata3 = data[2:4]
subdata4 = data[:4]

data2 = [100,200,300,400,500,600,700,800]

# menambah list
data3 = data + data2

# merubah content dari list

print(data)
a = data[:]
a[4] = 87
print(a)

# mengubah content list dgn menggunakn metode slicing
data[3:5] = [11,12]

# list dala list
x = [data,data2]

# mengakses list dalam multidimensional list
y = x[1][4]

# methods utk list
data.append(30)

# function yg bisa kita gunakan kpd list

panjang_list = len(data)

print(data)
print(panjang_list)
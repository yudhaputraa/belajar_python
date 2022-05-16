def bubblesort(alist):
    for i in range(0, len(alist)-1):
        print('langkah ke-%d \n' % (i+1), end='')
        for j in range(len(alist)-1, i, -1):
            print("nilai j :",j)
            if alist[j] < alist[j-1]:
                temp = alist[j]
                alist[j] = alist[j-1]
                alist[j-1] = temp
            print(alist)


data = [12,10,6,11,5,4,7,9,8]
b = len(data)
print(b)

a = bubblesort(data)
print(a)
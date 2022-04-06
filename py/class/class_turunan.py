# membuat class turunan dari class turunan
class IntList(list):
    
    # membatasi jumlah elemen list
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
    
    # memeriksa jumlah elemen list, kosong atau tidak?
    def isempty(self):
        return self.size == 0

    # memeriksa jumblah elemen list, penuh atau tidak?
    def isfull(self):
        return self.size == self.capacity

    # memeriksa tipe objek yang akan ditambahkan
    def checktype(self, obj):
        if not isinstance(obj, int):
            raise TypeError('Elemen harus bilanagn bulat')

    # override metode list.append()
    def append(self, obj):
        if self.isfull(): raise Exception('List penuh')
        self.checktype(obj)
        super().append(obj)
        self.size += 1

    # override metode list.insert()
    def insert(self, index, obj):
        if self.isfull(): raise Exception('List penuh')
        self.checktype(obj)
        super().insert(index, obj)
        self.size += 1

    # override metode list.extend()
    def extend(self, lst):
        for obj in lst:
            self.append(obj)

    # override metode list.remove()
    def remove(self, obj):
        if not self.isempty():
            super().remove(obj)
            self.size -= 1

    # override metode list.pop()
    def pop(self, index=None):
        if index == None:
            index = self.size - 1
        if not self.isempty():
            temp = super().pop(index)
            self.size -= 1
            return temp

    # override metode list.clear()
    def clear(self):
        if not self.isempty():
            super().clear()
            self.size = 0



# membuat objek dari class IntList
a = IntList(10)

# memanggil metode append()
print("=="*25)
print("nilai yg dimakukan dgn append()")
a.append(1)
a.append(2)
a.append(3)
print(a)
#print("=="*25)
#print("contoh error")
#print("=="*25)
#a.append('python')
print("=="*25)


# memanggil metode insert()
print("nilai yg dimakukan dgn insert()")
a.insert(1,4)
print(a)
#print("=="*25)
#print("contoh error")
#print("=="*25)
#a.insert(2,'python')
print("=="*25)


# memanggil metode extend()
print("nilai yg dimakukan dgn extend()")
a.extend([5,6,7])
print(a)
#print("=="*25)
#print("contoh error")
#print("=="*25)
#a.extend([8,'python',9])
print("=="*25)

print('nilai a : ', a)
print("=="*25)

# memanggil metode remove()
a.remove(4)
print(a)

# memanggil metode pop()
a.pop()
print(a)
a.pop(3)
print(a)

# memanggil metode clear()
a.clear()
print(a)
# class induk / super class
class induk:

    def __init__(self, x):
        self.x = x

    def printx(self):
        print('Nilai x : %d' % self.x)


# class turunan / subclass
class anak(induk):

    def __init__(self, x,y):
        # Pemanggilan induk.__init__()
        super().__init__(x)
        self.y = y

    def printy(self):
        print('Nilai y : %d' % self.y)

    def printxy(self):
        # memanggil induk.printx()
        super().printx()
        # memanggil method anak.printy()
        self.printy()

# membuat objek dari class anak/subclass
obj = anak(100,200)

# memanggil method printxy()
obj.printxy()
print('=========')
print("x")
obj.printx()
print('=========')
print("y")
obj.printy()

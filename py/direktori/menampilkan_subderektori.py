import os
import math

penyimpanan = ''
a = os.listdir("C:\\python\\direktori\\")
print('==============')
for name in a:
    print(name, end='')
    if os.path.isdir(name):
        print('\t\t\t[DIR]')
    else:
        import math
        size = math.ceil(os.path.getsize(name) / 1024)
        if len(name) < 8:
            print('\t\t\t', end='')
        else:
            print('\t\t', end='')
        print('%3d KB' % size)

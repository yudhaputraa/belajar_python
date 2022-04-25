import os

# memeriksa keberadaan direktori
a = os.path.exists('C:\python')
print(a)
b = os.path.exists('C:\python\direktori')
print(b)
c = os.path.exists('C:\python\direktori\data')
print(c)

# memeriksa keberadaan direktori
d = os.path.exists('C:\python\direktori\data\data.txt')
print(d)

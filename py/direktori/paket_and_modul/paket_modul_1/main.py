# mengimport mymodule
from mymodule import *

def main():
    # menampilkan variabel di dalam modul
    print(var1)
    print(var2)
    
    # memanggil fungsi di dalam modul
    f1()
    f2()
    
    # membuat objek dari kelas c1 dan c2
    # yang terdapat di dalam modul
    a = c1()
    b = c2()
    
    # memanggil metode m() melalui objek a dan b
    a.m()
    b.m()
    
if __name__ == "__main__":
    main()
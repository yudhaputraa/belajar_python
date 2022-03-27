#data yang di masukan pasti string
data = input("masukan data :")
print("data = ", data ,",tipe =",type(data))
#jika kita ingin mengambil int, maka
data_int = int(input("masukan angka integer:"))
data_float = float(input("masukan angka float :"))
print("data = ", data_int ,",tipe =",type(data_int))
print("data = ", data_float ,",tipe =",type(data_float))
#bagaimana dengan boolean
data_bool = bool(int(input("masukan nilai boolean : ")))
print("data = ", data_bool ,",tipe =",type(data_bool))
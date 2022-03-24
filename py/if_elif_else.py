nilai = 90

if nilai == 75: # equal eksplisit
    print("nilai anda : ",nilai)

if nilai == 60: # equal | is atau ==
    print("nilai anda : ",nilai)

if nilai != 60: # not equal | is not atau !=
    print("nilai anda bukan : 60")

print("===========================")

if 80 <= nilai <= 100:
    print("nilai anda adalah A")
elif 70 <= nilai < 80:
    print("nilai anda adalah B")
elif 60 <= nilai < 70:
    print("nilai anda adalah C")
elif 50 <= nilai < 60:
    print("nilai anda adalah T, lakukan perbaikan")
else:
    print("maaf anda tidak lulus mata kuliah ini")

print("===========================")
# operasi logika untuk list dan string
print("operasi logika untuk list dan string")
print("")

gorengan = ["bakwan","cireng","bala-bala","gehu","combro","pisang goreng","pukis","risoles"]
beli = "es"

if beli in gorengan:
    print('mamang bilang," ya, saya jual',beli,'"')
else:
    print('"saya tidak jual',beli,'"')
# atau else diganti dengan if lagi
# if not beli is gorengan:
#   print('"saya tidak jual',beli,'"')
print("===========================")
karakter = "z"
if karakter is beli:
    print("ada ",karakter," di ",beli)
else:
    print("tidak ada ", karakter, " di ", beli)

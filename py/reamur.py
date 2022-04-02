#latihan konversi satuan temperature

# program konversi reamur ke satuan lain
print("\n PROGRAM KONVERSI TEMPERATUR \n")

reamur = float(input("masukan suhu reamur : "))
print("suhu anda :",reamur)

# celcius
# rumus 5/4*reamur
celcius = (5/4)*reamur
print("suhu dalam celcius adalah : ", celcius, " celcius")


# fahrenheit
# rumus 9/5*reamur+32
fahrenheit = (9/5)*reamur+32
print("suhu dalam fahrenheit adalah : ", fahrenheit, " fahrenheit")

# kelvin
# rumus 5/4*reamur+273
kelvin = (5/4)*reamur+273
print("suhu dalam kelvin adalah : ", kelvin, " kelvin")

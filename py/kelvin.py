#latihan konversi satuan temperature

# program konversi kelvin ke satuan lain
print("\n PROGRAM KONVERSI TEMPERATUR \n")

kelvin = float(input("masukan suhu kelvin : "))
print("suhu anda :", kelvin)


# celcius
# rumus kelvin - 273
celcius = kelvin - 273
print("suhu dalam celcius adalah : ", celcius, " celcius")

# reamur
# rumus 4/5*(kelvin - 273)
reamur = 4/5*(kelvin-273)
# atau 4/5*celcius
print("suhu dalam reamur adalah : ", reamur, " reamur")


# fahrenheit
# rumus ((kelvin -273.15)*9/5)+32
fahrenheit = ((kelvin - 273.15)*9/5)+32
print("suhu dalam fahrenheit adalah : ", fahrenheit, " fahrenheit")

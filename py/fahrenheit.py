#latihan konversi satuan temperature

# program konversi fahrenheit ke satuan lain
print("\n PROGRAM KONVERSI TEMPERATUR \n")

fahrenheit = float(input("masukan suhu fahrenheit : "))
print("suhu anda :", fahrenheit)

# celcius
# rumus 5/9*(fahrenheit-32)
celcius = 5/9*(fahrenheit-32)
print("suhu dalam celcius adalah : ", celcius, " celcius")


# reamur
# rumus 4/9*(fahrenheit-32)
reamur = 4/9*(fahrenheit-32)
print("suhu dalam reamur adalah : ", reamur, " reamur")


# kelvin
# rumus ((fahrenheit - 32)*5/9)+273,15
kelvin = ((fahrenheit - 32)*5/9)+273.15
print("suhu dalam kelvin adalah : ", kelvin, " kelvin")


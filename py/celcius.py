#latihan konversi satuan temperature

# program konversi celcius ke satuan lain
print("\n PROGRAM KONVERSI TEMPERATUR \n")

celcius = float(input("masukan suhu celcius : "))
print("suhu anda : ", celcius,"celcius")

# reamur
# rumus 4/5*celcius
reamur = (4/5)*celcius
print("suhu dalam reamur adalah : ",reamur," reamur")

# fahrenhelt
# rumus 9/5*celcius+32
fahrenhelt = (9/5)*celcius+32
print("suhu dalam fahrenhelt adalah : ", fahrenhelt ," fahrenhelt")

# kelvin
# rumus celcius + 273
kelvin = celcius + 273
print("suhu dalam kelvin adalah : ", kelvin ,"kelvin")
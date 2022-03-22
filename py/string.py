data_garis = "====="*5

print("==========STRING===========")
data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string

'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''

print(data_garis)
data = 'menggunakan single quote'
print(data)

print(data_garis)
data = "menggunakan single quote"
print(data)

print(data_garis)
print('"halo, apa kabar?"')
print("'halo, apa kabar?'")
print("ini adalah hari jum'at")

# 2. mengunakan tanda \

#membuat tanda ' menjadi sring
print(data_garis)
print('mari shalat juma\'at')
print('d\'day, isn\'t it?')

# backlash
print(data_garis)
print("c:\\user\\ucup")

# tab
print(data_garis)
print("ucup\t\t\totong, semakin jauhan")

# backspace
print(data_garis)
print("ucup \botong, jadi deket")

# newline
print(data_garis)
    # LF -> line feed -> unix, macos, linux
print("baris pertama.\nbaris kedua.")
print('')
    # CR -> carriage return -> commodore, acorn, list
print("baris pertama.\rbaris kedua.")
print('')
    # CRLF -> line feed carriage return -> dipakai oleh windows
print("baris pertama.\r\nbaris kedua.")

# 3. string literal atau raw

# hati-hati
print(data_garis)
print('c:\new folder') # akan salah pathnya

# menggunakan raw string
print(data_garis)
print(r'c:\new folder')

# multiline literal string
print(data_garis)
print("""
nama : ucup
kelas : 3 SD
""")


# multiline literal string dan raw
print(data_garis)
print(r"""
nama : yudha
kelas : 3 SD\new normal
website : wwww.yudha.com/newID
""")



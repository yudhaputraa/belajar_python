f = 0
# print(f)

# f = "abc"
# print(f)

# # syntak di bawah ini membuat erorr
# # print("this is a string" + 123)
# # yang benar dibawah ada dua tipe
# print("this is a string", 123)
# print("this is a string " + str(123))

# global vs. local variables in function
def someFunction():
    global f
    f = "def"
    print(f)
    
someFunction()
print(f)
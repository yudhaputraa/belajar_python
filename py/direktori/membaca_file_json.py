import json

# membuka file json
f = open("C:\\Users\\ASUS\\OneDrive\\Dokumen\\python\\direktori\\data\\data.json",'r')

# membaca data dan menampungnta ke dalam variabel
json_str = ''.join(f.readlines())
f.close()

print(json_str)

print("#"*40)

# megnversi string dgn format JSON ke objek dictionary
data = json.loads(json_str)
print(data)

"""
TODO :  -json_str bertipe string
        -data bertipe dict
"""
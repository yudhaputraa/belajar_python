import json

data = {
    'karyawan': [
        {'nip':'1001','nama':'akbar','gaji':'1000000'},
        {'nip':'1002','nama':'ali','gaji':'95000000'},
        {'nip':'1003','nama':'andi','gaji':'90000000'}
    ]
}


# mengubah dictionary ke string dengan format JSON
json_str = json.dumps(data)

#print(json_str)

# membuat file JSON
f = open("C:\\python\\direktori\\data\\data.json", 'w')
f.writelines(json_str)
f.close()

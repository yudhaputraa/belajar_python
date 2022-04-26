import csv

data = [(1, "Dennis Ritchie", "C"),
        (2, "Bjarne Stroustrup","C++"),
        (3, "James Gosling","JAVA"),
        (4, "Larry Wall","Perl"),
        (5, "Guido Van Rossum","Python"),
        (6, "Yukihiro Matsumoto","Ruby")
]

# menulis data ke file csv
with open('C:\\Users\\ASUS\\OneDrive\\Dokumen\\python\\direktori\\data\\pencipta.csv','w',newline='',encoding='utf-8') as csvfile:
    # membuat objek write
    w = csv.writer(csvfile, delimiter=';')
    w.writerows(data)
    csvfile.close()

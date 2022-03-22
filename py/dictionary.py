# dictionary

member1 = {"id":101,
           "nama":"yudha mukhlist",
           "pekerjaan":"mahasiswa",
           "status member":"gold"}
member2 = {"id":102,
           "nama":"ana alis",
           "pekerjaan":"tata alis",
           "status member":"berlian"}

print(member1["pekerjaan"])
print(member1.keys())
print(member1.values())
print(member1.items())
print(type(member1))
print("="*20)

memberlist = {101:member1,102:member2}
print(memberlist[101])
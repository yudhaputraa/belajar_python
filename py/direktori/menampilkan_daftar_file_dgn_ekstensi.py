# mendefinisikan fungsi listfile()
def listfile(path, extension):
    temp = []
    import os
    names = os.listdir(path)
    for name in names:
        if name.endswith(extension):
            temp.append(name)
    return temp

files = listfile('C:\\Users', '.dll')
#print(files)
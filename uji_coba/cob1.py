def sequentialsearch(alist, value):
    pos = 0 
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == value:
            found = True
        else:
            pos += 1
    if found:
        return pos # jika di temukan
    else:
        return "tidak di temukan"

data = [900,300,400,500,100]

a = sequentialsearch(data, 800)
print(a)
l=[1,8,2,4]
def traverse(l):
    i=0
    for val in l:
        if val>i:
            i=val

    return i
k=traverse(l)
print(k)
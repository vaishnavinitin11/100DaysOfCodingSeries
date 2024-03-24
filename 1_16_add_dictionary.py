d1 = {'key1': 50, 'key2': 100, 'key3':200}
d2 = {'key1': 200, 'key2': 100, 'key4':300}

dict3= {}

for key, value in d1.items():
    if key in dict3:
        dict3[key]=[dict3[key],value]
    else:
        dict3[key]=value

for key, value in d2.items():
    if key in dict3:
        dict3[key]=[dict3[key],value]
    else:
        dict3[key]=value

print(dict3)
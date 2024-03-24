strin="hello"
new=""
r=-1
for i in range(1,len(strin)+1):
    new+=strin[r]
    r-=1

# print(new)

'''OR'''

print(strin[::-1])
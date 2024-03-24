a=list(map(int,(input("Enter array:  ").split())))

r=-1
a1=[]

# print(a[:])

for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if(a[i]>=a[j]):
            a[i],a[j]=a[j],a[i]
print(a)
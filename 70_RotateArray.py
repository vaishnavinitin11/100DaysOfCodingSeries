# Day 70 coding Statement: Given an array, rotate the array by one position in clock-wise direction.

def RotateArray(a):
    a1=[]
    i1=0
    for i in range(len(a)+1):
        if i==0:
            a1.append(a[-1])
        elif i==(len(a)-1):
            continue
        else:
            a1.append(a[i1])
            i1+=1
    print(a1)

n=int(input('Enter length of list: '))
a=[]

for elem in range(n):
    elem=int(input('Enter number: '))
    a.append(elem)

RotateArray(a)
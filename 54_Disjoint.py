# Day 54 coding Statement : Given an integer array of size N. Write Program to find whether Arrays are disjoint or not. Two arrays are said to be disjoint if they have no elements in common.


def DynamicArray():
    narr=int(input('Enter size of an array: '))
    array=[]
    for i in range(narr):
        enternum=int(input('Enter items of an array: '))
        array.append(enternum)
    return array

n1=DynamicArray()
n2=DynamicArray()

n1_com=[]

for i in n1:
    if i in n2:
        n1_com.append(i)

for j in n2:
    if j in n1:
        if j not in n1_com:
            n1_com.append(j)

if len(n1_com)>0:   
    print('Not disjoint',n1_com,'- common')
else:
    print('Disjoint')


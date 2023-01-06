# Day 46 coding Statement: Write Program to find sum of elements in an array

def DynamicArray():
    narr=int(input('Enter size of an array: '))
    array=[]
    for i in range(narr):
        enternum=int(input('Enter items of an array: '))
        array.append(enternum)
    return array

array=DynamicArray()
sum=0
for element in array:
    sum+=element

print(sum)

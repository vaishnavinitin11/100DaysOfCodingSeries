# Day 56 coding Statement: Write Program to find whether the numbers of an array be made equal

def CanEquallyMade():
    def DynamicArray():
        narr=int(input('Enter size of an array: '))
        array=[]
        for i in range(narr):
            enternum=int(input('Enter items of an array: '))
            array.append(enternum)
        return array

    n=DynamicArray()

    for i,val in enumerate(n):
        if val%2==0:
            n[i]=n[i]/2
        if val%3==0:
            n[i]=n[i]/3
    count=0
    for item in n:
        if item == n[0]:
            count+=1
    if count==(len(n)):
        print('Yes,Elements are made equal')
    else:
        print('No,Elements could not be made equal')

CanEquallyMade()
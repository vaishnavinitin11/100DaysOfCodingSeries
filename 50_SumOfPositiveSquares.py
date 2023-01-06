# Day 50 coding Statement : Given an integer array of size N. Write Program to find sum of positive square elements in the array.

def SumPostitveSquares():
    def DynamicArray():
        narr=int(input('Enter size of an array: '))
        array=[]
        for i in range(narr):
            enternum=int(input('Enter items of an array: '))
            array.append(enternum)
        return array

    array=DynamicArray()
    array1=[]
    arr1=[]

    # Converting elements into positive array
    for i in array:
        if i<0:
            i*=-1
            array1.append(i)
        else:
            array1.append(i)

    # collect unique elements from original array
    for item in array1:
        if item not in arr1:
            arr1.append(item)

    # Sum of Square elements
    sum=0
    for i in arr1:
        sum+=i**2

    return sum

print(SumPostitveSquares())
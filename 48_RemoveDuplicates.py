# Day 48 coding Statement: Write Program to remove duplicate elements in an array


def RemoveDuplicates():
    def DynamicArray():
        narr=int(input('Enter size of an array: '))
        array=[]
        for i in range(narr):
            enternum=input('Enter items of an array: ')
            array.append(enternum)
        return array
    array=DynamicArray()
    arr=[]
    for element in array:
        if element not in arr:
            print(element)
            arr.append(element)
    return arr

print(RemoveDuplicates())
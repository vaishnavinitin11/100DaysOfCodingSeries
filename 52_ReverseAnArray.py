# Day 52 coding Statement : Given an integer array of size N, write a program to reverse the array;

def ReverseArray():
    def DynamicArray():
        narr=int(input('Enter size of an array: '))
        array=[]
        for i in range(narr):
            enternum=int(input('Enter items of an array: '))
            array.append(enternum)
        return array

    array=DynamicArray()

    g=-1
    reverse_array=[]
    for i in array:
        reverse_array.append(array[g])
        g-=1

    print(reverse_array)

ReverseArray()
# Day 51 coding Statement : Given an integer array of size N, write a program to sort the array

def SortArray():
    def DynamicArray():
            narr=int(input('Enter size of an array: '))
            array=[]
            for i in range(narr):
                enternum=int(input('Enter items of an array: '))
                array.append(enternum)
            return array

    def CountInterger(array):
        count=0
        for i in array:
            count+=1
        return count


    array=DynamicArray()
    temp=0
    for i,val in enumerate(array):
        for j,val1 in enumerate(array):
            if i!=j and i<j:
                if array[i]<array[j]:
                    j+=1
                else:
                    temp=array[i]
                    array[i]=array[j]
                    array[j]=temp
            elif i!=j and j<i:
                if array[i]>array[j]:
                    j+=1
                else:
                    temp=array[i]
                    array[i]=array[j]
                    array[j]=temp

    for item in array:
        count=CountInterger(array)

    print(array)

SortArray()
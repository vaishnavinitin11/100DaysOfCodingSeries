# Day 42 coding Statement: Write Program to check if two arrays are the same or not

def isArraySame():
    def DynamicArray():
        narr=int(input('Enter size of an array: '))
        array=[]
        for i in range(narr):
            enternum=int(input('Enter items of an array: '))
            array.append(enternum)
        return array

    firstArray=DynamicArray()
    secondArray=DynamicArray()

    firstArray=sorted(firstArray)
    secondArray=sorted(secondArray)
    count=0
    if len(firstArray)==len(secondArray):
        for ind,item in enumerate(firstArray):
            if firstArray[ind]==secondArray[ind]:
                count+=1
                if count==len(firstArray):
                    print('Same')
        else:
            print('Not Same')         
    else:
        print('Not Same')

isArraySame()
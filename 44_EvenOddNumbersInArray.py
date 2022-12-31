# Day 44 coding Statement: Write Program to find number of even and odd elements in an array

def CountEvenOddElements():
    def DynamicArray():
        narr=int(input('Enter size of an array: '))
        array=[]
        for i in range(narr):
            enternum=int(input('Enter items of an array: '))
            array.append(enternum)
        return array

    array=DynamicArray()

    count1,count2=0,0
    for ind,item in enumerate(array):
        if item%2==0:
            count1+=1
        elif item%2!=0:
            count2+=1
    print('Number of even elements:',count1)
    print('Number of odd elements:',count2)
 

CountEvenOddElements()
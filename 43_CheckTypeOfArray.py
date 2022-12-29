# Day 43 coding Statement: Write Program to find the array type

def ArrayType():
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
            if count1==(len(array)):
                print('Even')
                break
        elif item%2!=0:
            count2+=1
            if count2==(len(array)):
                print('Odd')
                break
    if count1!=0 and count2!=0 and (count1+count2)==len(array):
        print('Mixed Type')

ArrayType()

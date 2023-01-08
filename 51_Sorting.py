# Day 51 coding Statement : Given an integer array of size N, write a program to sort the array

def SortArray():
    def DynamicArray():
        narr=int(input('Enter size of an array: '))
        array=[]
        for i in range(narr):
            enternum=int(input('Enter items of an array: '))
            array.append(enternum)
        return array

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

                    
    print(array)

SortArray()





# if number occurs more thn one time then it will print (n-1)times that number
    # count_item=[]
    # for ind,item in enumerate(array):
    #     count=0
    #     for ind1,item1 in enumerate(array):
    #         if item == item1:
    #             count+=1

    #     if item not in count_item and count>1:
    #         for i in range(count-1):
    #             count_item.append(item)
    #     elif count==1:
    #         count_item.append(item)

    # print(count_item)


# Day 55 coding Statement : Given 2 integer arrays X and Y of same size. Consider both arrays as vectors and print the sum of maximum scalar product (Dot product) of 2 vectors.

def MaximumScalarProduct():
    def DynamicArray():
        narr=int(input('Enter size of an array: '))
        array=[]
        for i in range(narr):
            enternum=int(input('Enter items of an array: '))
            array.append(enternum)
        return array

    def SortArray(array):
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
        return array

    n1=DynamicArray()
    n2=DynamicArray()

    sort_n1=SortArray(n1)
    sort_n2=SortArray(n2)

    iterate,sum=0,0

    while iterate<len(n1):
        sum+=sort_n1[iterate]* sort_n2[iterate]
        iterate+=1

    return sum

print('Maximum Scalar Product of given 2 vectors is:',MaximumScalarProduct())
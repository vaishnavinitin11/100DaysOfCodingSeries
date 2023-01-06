# Day 49 coding Statement: Given 2 integer arrays X and Y of same size. Consider both arrays as vectors and print the minimum scalar product (Dot product) of 2 vectors.
import math

def minimumScalar():
    def DynamicArray():
        narr=int(input('Enter size of an array: '))
        array=[]
        for i in range(narr):
            enternum=int(input('Enter items of an array: '))
            array.append(enternum)
        return array

    def minimum(scalar_values):
        minimum=scalar_values[0]
        for i in scalar_values:
            if i<minimum:
                minimum=i

        return (minimum)

    def isSimilar():
        similar=[]
        for i1 in arr:
            for j1 in arr:
                if -i1==j1:
                    if j1 not in similar:
                        similar.append(j1)
        return (similar)

    array=DynamicArray()
    arr=array.copy()

    arr.sort()

    sim=isSimilar()

    if len(sim)>0:
        scalar_values=[]
        for simi in arr:
            for similar in sim:
                if similar in arr:
                    arr.remove(similar)

        for item in sim:
            arr.append(item)
            final=[]
            sum=0
            for i in arr:
                for j in arr:
                    if (abs(i)+abs(j))==len(array):
                        if i not in final and j not in final:
                            final.append(i);final.append(j)
                            a=i*j
                            sum+=a
            arr.remove(item)
            scalar_values.append(sum)
        minimum_scalar=minimum(scalar_values)
        return (minimum_scalar)

    else:
        final=[]
        sum=0
        for i in array:
            for j in array:
                if (abs(i)+abs(j))==len(array):
                    if i not in final and j not in final:
                        final.append(i);final.append(j)
                        a=i*j
                        sum+=a

        return (sum)

input1=minimumScalar()
input2=minimumScalar()

print('minimum scalar of input1 =',input1)
print('minimum scalar of input2 =',input2)
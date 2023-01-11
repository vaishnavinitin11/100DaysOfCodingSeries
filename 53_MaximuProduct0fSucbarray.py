# # Day 53 coding Statement : Given an integer array of size N. Write Program to find maximum product subarray in a given array.

def DynamicArray():
    narr=int(input('Enter size of an array: '))
    array=[]
    for i in range(narr):
        enternum=int(input('Enter items of an array: '))
        array.append(enternum)
    return array

# # for i in array:
# #     for j in array:
# #         if i!=j and i not in arr1 and j not in arr1:
# #             print(i,j)
# #             arr1.append(i);arr1.append(j)

# for item in range(len(array)):
#     for item1 in range(item,len(array)):
#         if array[item]!=array[item1]:
#             print(array[item],array[item1])
#         for item2 in range(item1,len(array)):
#             if array[item]!=array[item1]!=array[item2]:
#                 print(array[item],array[item1],array[item2])




# item3=0
# while item3<len(array):
#     # print(array[item3])
#     if (array[item3] and array[item3-2]):
#         print(array[item3],array[item3-2])
#     item3+=1

# item4=0
# while item4<len(array):
#     # print(array[item4])
#     if (array[item4] and array[item4-3]):
#         print(array[item4],array[item4-3])
#     item4+=1
# print('--------------------')
# for val in range(len(array)):
#     for val1 in array:
#         if val1==array[val-1]:
#             continue
#         print(val1,end=' ')
#     print()

# for val in range(len(array)):
#     for val1 in array:
#         if val1==array[val-2]:
#             continue
#         print(val1,end=' ')
#     print()
# print('-----')
# for gap in range(len(array)-2):
#     for gal in range(len(array)):
#         for gal1 in array:
#             if gal1==array[gal-gap]:
#                 continue
#             print(gal1,end=' ')
#         print('--length-wise iteration--')

array=DynamicArray()
arr1=[]

for item in range(len(array)):
    for item1 in range(item,len(array)):
        arr1.append(array[item:item1+1])
mul_arr=[]

for i in arr1:
    mul=1

    for it in i:
        mul*=it
    mul_arr.append(mul)
    

maximum=mul_arr[0]

for max in mul_arr:
    if max>maximum:
        maximum=max

for isval in range(len(mul_arr)):
    if maximum==mul_arr[isval]:
        ind=isval

print('Maximum product of a subarray:')
print(maximum,'=',arr1[ind])
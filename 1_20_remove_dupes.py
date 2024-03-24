# Remove duplicates from sorted array

def remove_dupes(arr):
    # arr1=[]
    # for i in arr:
    #     if i not in arr1:
    #         arr1.append(i)
    # return arr1

    '''OR'''
    return list(set(arr))

array_1 = [1,2,2,3,3,4]
print(remove_dupes(array_1))


array_2 = [1,1,3,4,5,6,6]
print(remove_dupes(array_2))

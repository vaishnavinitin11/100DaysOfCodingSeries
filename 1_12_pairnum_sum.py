# Write a program to check and return the pairs of a given array A whose sum value is equal to a target value N.

# def funct(arr, n):
    # for i in range(1,len(arr)):
    #     if(arr[i]<len(arr)):
    #         if(arr[i]+arr[i+1])==n:
    #             return  True
            
# print(funct([1,2,4,6,84],3))

def print_pairs(arr, N):
    for i in range(0, len(arr)):
        for j in range(i,len(arr)):
            val = arr[i]+arr[j]
            if val==N: #check if N-x is there in set, print the pair
                print("Pairs " + str(arr[i]) + ", " + str(arr[j]))

'''Alternate method'''

def freq(arr,N):
    # hash_set={}
    hash_set=set()
    for x in arr:
        if N-x in arr:
            hash_set.add((x, N-x))
            # hash_set[x]=([x, N-x])
    print(f"Pairs: {hash_set}")

# driver code
arr = [1, 2, 40, 3, 9, 4]
N = 4
freq([1, 2, 40, 3, 2, 4], 4)
def binary_search(arr, target):

    f=0
    l = len(arr) - 1
    while f <= l:
        mid=f+(l-f)//2
        # Check if the element is present at mid
        if arr[mid] == target:  
            return mid
        elif arr[mid]<target:
            f=mid+1
        else:
            l=mid-1
    return -1

    # If we reach here, then the element
    # was not present
    return -1

# Driver Code
arr = [2, 3, 4, 10, 18, 20, 29]
x = 18


# Function call
result = binary_search(arr,x)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")

    
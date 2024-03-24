# Bubble sort

def sort_array(arr):
    n=0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
            n+=1

                
    return n
    
    
arr = [3, 2, 4, 6, 5]
print(sort_array(arr))
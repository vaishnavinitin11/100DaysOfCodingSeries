
def missing_nums(n):
    missing_sum=sum(n)
    
    num=len(n)+1
    actual_sum=(num*(num+1))/2
    
    return (actual_sum-missing_sum)
    
    
list_1 = [1,5,6,3,4]

print(missing_nums(list_1))

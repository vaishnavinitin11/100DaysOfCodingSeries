# Max or min number

def min_or_max(tp, nums):
    ind=nums[0]
    for i in nums:
        if(tp=='min'):
            if ind>i:
                ind=i
        elif(tp=='max'):
            if ind<i:
                ind=i
    return ind
    
nums=[1,2,34,5,2,1000,23]
print(min_or_max('max',nums))
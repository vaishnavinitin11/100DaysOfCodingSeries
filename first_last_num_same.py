
# WAP to check whether start and stop num are same or not
def solve(l,r):
    count=0
    for i in range(l,r+1):
        a=str(i)
        if len(a)>1:
            if a[0]==a[-1]:
                # print(a)
                count+=1
                
    return count
    
print(solve(5,55))

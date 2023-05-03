# Day 87 coding Statement: Jumping Frog 
for i in range(int(input('Enter test cases: '))):
    n=int(input('Enter number of stones: '))
    l=list(map(int,input('Enter stones with Ai value: ').split()))
    i,j=0,0
    energy=0
    while j<n:
        if(l[j]>=l[i]):
            j+=1
        else:
            energy+=(j-i+1)*l[i]-l[j]
            i=j
    energy+=(n-i)*l[i]-l[n-1]
    if energy<=0:
        print(0)
    else:
        print(energy)

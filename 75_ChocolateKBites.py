# Day 75 coding Statement: 

tc=int(input('Enter number of testcases: '))

while tc!=0:
    n,k=list(map(int,input('Enter N & K: ').split()))
    if n>k:
        if n%k==0:
            print(int(n/k))
        else:
            print(-1)
    else:
        print(0)
    tc-=1
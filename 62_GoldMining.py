# Day 62 coding Statement: Gold Mining

tc=int(input('Enter number: '))

for i in range(tc):
    n,x,y=list(map(int,input('Enter number for N, X, Y:').split()))

    if ((n+1)*y)>=x:
        print('YES')
    else:
        print('NO')
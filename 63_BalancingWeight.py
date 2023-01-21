# Day 63 coding Statement : Balancing Weight

tc=int(input('Enter testcases: '))

for i in range(tc):
    w1,w2,x1,x2,m=list(map(int,input('Enter w1,w2,x1,x2,m: ').split()))

    if (x1*m)<=(w2-w1)<=(x2*m):
        print(1)
    else:
        print(0)
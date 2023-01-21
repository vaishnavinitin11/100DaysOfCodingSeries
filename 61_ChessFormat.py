# Day 61 coding Statement: Chess Format 

tc=int(input('Enter number of testcases: '))

for i in range(tc):
    a,b=list(map(int,input('Enter a and b:').split()))
    if (a+b)<3:
        print(1)
    elif 3<=(a+b)<=10:
        print(2)
    elif 11<=(a+b)<=60:
        print(3)
    elif 60<(a+b):
        print(4)
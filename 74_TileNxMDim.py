# Day 74 coding Statement : You have a grid with N rows and M columns. You have two types of tiles — one of dimensions 2×2 and the other of dimensions 1×1. You want to cover the grid using these two types of tiles in such a way that:
tc=int(input('Enter number of testcases: '))

for i in range(tc):
    n,m=list(map(int,input('Enter N & M:').split()))
    if n%2==0 and m%2==0:
        print(0)
    elif n%2==0 and m%2!=0:
        print(n)
    elif n%2!=0 and m%2==0:
        print(m)
    else:
        print((m+n)-1)

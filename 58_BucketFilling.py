# Day 58 coding Statement: Bucket Filling

tc=int(input('Enter number of testcases: '))
print('K indicates the capacity of bucket and it is already filled with X litres')
for i in range(tc):
    A,B=list(map(int,input('Enter K and X: ').split()))
    print(A-B)
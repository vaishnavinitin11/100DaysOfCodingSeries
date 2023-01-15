# Day 60 coding Statement: Good Weather
# sunny>rainy(1>0)
# 1=sunny day; 0=rainy day

tc=int(input('Enter number of testcases: '))

for i in range(tc):
    arr=[]
    count_0,count_1=0,0
    for val in range(7):
        n=int(input('Enter day: '))
        arr.append(n)
    for j in arr:
        if j==0:
            count_0+=1
        elif j==1:
            count_1+=1
    if count_0<count_1:
        print('YES')
    elif count_1<count_0:
        print('NO')
# Day 65 coding Statement: New Tablet

tc=int(input('Enter number of testcases: '))

for i in range(tc):
    n,b=list(map(int,input('Enter N & B: ').split()))
    li=[]
    for j in range(1,n+1):
        w,h,p=list(map(int,input('Enter w,h, and p of tablet: ').split()))
        if p<=b:
            li.append(w*h)
        else:
            continue
    if li:
        maxi=max(li)
        print(maxi)
    else:
        print('no tablet')


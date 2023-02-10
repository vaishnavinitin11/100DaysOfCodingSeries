t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    a=input().split()
    for i in range(0,n):
        a[i]=int(a[i])
    a.sort()
    print(a)
    a1=(a[-2]-a[0])*a[-1]
    a2=(a[-1]-a[0])*a[-2]
    print(a1,a2)
    print(max(a1,a2))
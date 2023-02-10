# Day 80 coding Statement : 


t=int(input('Enter testcases: '))

while t!=0:
    n=int(input('Enter strength of animals: '))
    s=list(map(int,input().split()))
    if n%2==0:
        type_dict={}
        for type in s:
            if type in type_dict:
                type_dict[type]+=1
            else:
                type_dict[type]=1
        for j in type_dict:
            if type_dict[j]%2==0:
                a=type_dict[j]//2
            else:
                break
        if type_dict[j]%2!=0:
            print('NO')
        else:
            print('YES')
    else:
        print('NO')
    t-=1

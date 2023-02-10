# Day 68 coding Statement : you will be given queries. Each query is of one of the following three types: :

tc=int(input('Enter number of testcases: '))
a=[]

def add1(n):
    a.append(n)
    return a

def delete(n):
    a.remove(n)
    return a

for n in range(tc):
    type,num=list(map(int,input('Enter type & number: ').split()))
    if type==1:
        an=add1(num)
    elif type==2:
        an=delete(num)
    elif type==3:
        if num in a:
            print('yes')
        else:
            print('no')

print(a)
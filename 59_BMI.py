# Day 59 coding Statement : Body Mass Index

tc=int(input('Enter number of testcases: '))
li=[]
for i in range(tc):
    sli=[]
    M,H=list(map(int,input().split()))
    sli.append(M);sli.append(H)
    li.append(sli)
    
for j in li:
    bmi=j[0]/(j[1]**2)
    if bmi<=18:
        print(1)
    elif 19<=bmi<=24:
        print(2)
    elif 25<=bmi<=29:
        print(3)
    elif bmi>=30:
        print(4)

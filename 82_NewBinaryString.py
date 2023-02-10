# Day 82 coding Statement: You are given N binary strings of length N each. You need to find a binary string of length N which is different from all of the given strings.

import random
t=int(input('Enter number of test cases: '))

while t!=0:
    n=int(input('Enter length of binary strings: '))
    li=(input('Enter binary strings: ').split())
    strings=[]
    print(li)

    for i in range(0,n+1):
        string=''
        for j in range(n-i):
            string+='0'
        for s in range(i):
            if s==0:
                string+='1'
            else:
                string+='0'
        strings.append(string)

    for i1 in range(0,n+1):
        string=''
        for j1 in range(n-i1):
            string+='1'
        for s in range(i1):
            if s==0:
                string+='0'
            else:
                string+='1'
        strings.append(string)

    for it in li:
        if it in strings:
            strings.remove(it)

    print(random.choice(strings))
    t-=1
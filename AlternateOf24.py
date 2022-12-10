# Day 24 coding Statement: Write a program to print Pyramid pattern using stars

n=int(input('Enter a number: '))

def PyramidPattern(n):
    oddnum=[]
    for odd in range(1,2*n):
        if odd%2!=0:
            oddnum.append(odd)
    ind=0
    for i in range(1,n+1):
        for space in range(n-i):
            print(' ',end='')
        while ind<i:
            print('*'*oddnum[ind])
            ind+=1
    
PyramidPattern(n)
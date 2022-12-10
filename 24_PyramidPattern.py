# Day 24 coding Statement: Write a program to print Pyramid pattern using stars

n=int(input('Enter n: '))

for i in range(1,n+1):
    j=0
    for space in range(n-i):
        print(' ',end='')
    while(j!=2*i-1):
        print('*',end='')
        j+=1 
    print('\n')

#My approach
#odd numbers printing on every line as stars
#for spaces if n is 4 then * should print at i=4 th position
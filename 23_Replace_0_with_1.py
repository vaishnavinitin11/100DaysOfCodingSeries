# Day 23 coding Statement : Write a program to Replace all 0’s with 1 in a given integer

n=input('Enter a number: ')
l=list(n)
for i,val in enumerate(l):
    if val=='0':
        l[i]='1'
l=''.join(l)
print(l)
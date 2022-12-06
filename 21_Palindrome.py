# Day 14 coding Statement : Write a program to reverse a given number

n=input('Enter a number: ')

def Palindrome(n):
    l=[]
    e=-1
    for letter in n:
        l.append(n[e])
        e-=1
    l=''.join(l)
    if n==l:
        print('Palindrome')
    else:
        print('Not a Palindrome')

Palindrome(n)

# Alternate way:
'''
n=int(input('Enter a number: '))
new_n=n
reversed_no=0
while n!=0:
    temp=n%10
    reversed_no=reversed_no*10+temp
    n=n//10

print(reversed_no)
if new_n==reversed_no:
    print('Palindrome')
else:
    print('Not a Palindrome')
'''
# Day 14 coding Statement : Write a program to reverse a given number

n=input('Enter a number: ')

def ReverseNumber(n):
    l=[]
    e=-1
    for letter in n:
        l.append(n[e])
        e-=1
    l=''.join(l)
    print(l)
    if n==l:
        print('Palindrome')
    else:
        print('Not a Palindrome')

ReverseNumber(n)
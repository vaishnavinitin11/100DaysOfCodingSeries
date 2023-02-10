# Day 28 coding Statement : Write a Program to reverse a string.

n=input('Enter String: ')

def reverseString(n):
    r=-1
    r1=''
    for i in n:
        r1+=n[r]
        r-=1
    return(r1)
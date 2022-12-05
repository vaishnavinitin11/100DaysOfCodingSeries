# Day 12 coding Statement:  Write a program to find Sum of digits of a number

n=input('Enter a number: ')
def SumOfDigits(n):
    count=0
    for i in n:
        count+=1
    n=int(n)
    i=0
    sum=0
    while i<count:
        temp=n%10
        sum+=temp
        n=n//10
        i+=1
    print('Sum of digits in a number:', sum)

SumOfDigits(n)
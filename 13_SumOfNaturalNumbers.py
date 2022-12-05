# Day 13 coding Statement:  Write a program to find Sum of N natural numbers

n=int(input('Enter number: '))

def SumOfNaturalNumbers(n):
    sum=0
    for i in range(n+1):
        sum+=i
    print(sum)

SumOfNaturalNumbers(n)
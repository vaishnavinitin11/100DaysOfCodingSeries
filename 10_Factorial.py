# Day 10 coding Statement:  Write a program to find Factorial of a number

n=int(input('Enter number: '))
def factorial(n):
    fact=1
    while n!=0:
        fact*=n
        n-=1
    print(fact)

temp=factorial(n)

# Day 17 coding Statement : Write a program to find the Factors of a number
n=int(input('Enter n: '))

def Factors(n):
    i=1
    while i<=n:
        if n%i==0:
            print(i)
        i+=1

Factors(n)

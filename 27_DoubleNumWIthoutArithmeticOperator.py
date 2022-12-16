# Day 27 coding Statement: Write a program to find the double of the given number without using arithmetic operator

n=int(input('Enter a number: '))

def DoubleWithoutArithemticOperator(n):
    sum=0
    for i in range(n+1):
        if i==0:
            sum+=n
        elif i>=1:
            sum+=1
    return sum

print(DoubleWithoutArithemticOperator(n))
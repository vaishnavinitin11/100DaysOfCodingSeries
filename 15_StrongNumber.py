# Day 15 coding Statement : Write a program to identify if the number is Strong number or not
n=int(input('Enter number: '))
n1=n
def factorial(n):
    fact=1
    while n!=0:
        fact*=n
        n-=1
    return fact

def StrongNumber(n):
    sum=0
    while n>0:
        temp=n%10
        each_fact=factorial(temp)
        sum+=each_fact
        n=n//10
    if n1==sum:
        print('Strong Number')
    else:
        print('Not a Strong Number')

StrongNumber(n)


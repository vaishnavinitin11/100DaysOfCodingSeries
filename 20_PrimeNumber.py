# Day 20 coding Statement: Write a program to identify if the number is Prime number or not

n=int(input('Enter number: '))
def PrimeNumber(n):
    sum=0
    if n==1:
        print('is neither a prime number nor a composite number')
    else:
        for i in range(1,n+1):
            if n%i==0:
                sum+=i
    if sum==n+1:
        print('Prime Number')
    else:
        print('Not a Prime Number')

PrimeNumber(n)
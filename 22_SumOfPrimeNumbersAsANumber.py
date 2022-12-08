# Day 22 coding Statement : Write a program to express a number as a sum of two prime numbers

n=int(input('Enter number: '))
def PrimeNumber(n):
    sum=0
    for i in range(1,n+1):
        if n%i==0:
            sum+=i
    if sum==n+1:
        return True
    else:
        return False

# if number is even and half of the number is prime number
# number=PrimeNumber(int(n/2))
# if (n/2)==number:
#     print(n,'can be expressed as sum of',number,'&',number)
def SumOfPrimeNumbersToGetTheNumber(n):
    def ToFindPrime(n):
        for i in range(n-1,0,-1):
            if PrimeNumber(i):
                if (n-i)!=1:
                    grtnum=i
                    return grtnum
                
    grt1num=ToFindPrime(n)
    m=n-grt1num
    if PrimeNumber(m)==False:
        another=ToFindPrime(m)
        another1=m-another
    # if PrimeNumber(another)!=True:
    #     print('Number cannot be expressed as sum of prime numbers')
    if PrimeNumber(m)==False:           
        print('No pair of two Prime numbers can give sum of',n)
        # Can uncomment below line if you want to show sum of three prime numbers
        # print(n,'can be expressed as sum of',grt1num,'&',another,'&',another1)
    else:
        print(n,'can be expressed as sum of',grt1num,'&',(n-grt1num))

SumOfPrimeNumbersToGetTheNumber(n)

#Enter number: 383
#383 can be expressed as sum of 379 & 4
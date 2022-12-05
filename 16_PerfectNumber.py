# Day 16 coding Statement: Write a program to identify if the number is Perfect number or not

# E.g. Let number is 28, factors of 28 are 1,2,4,7,14. 
# Now the sum of all these factors are 28 itself.

n=int(input('Enter number: '))

def PerfectNumber(n):
    i,sum=1,0
    while i<n:
        if n%i==0:
            sum+=i
        i+=1       
    if n==sum:
        print('Perfect Number')
    else:
        print('Not a Perfect Number')

PerfectNumber(n)

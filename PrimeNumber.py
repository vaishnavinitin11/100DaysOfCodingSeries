n=int(input('Enter n: '))
i,sum=1,0
while i<=n:
    if n%i==0:
        print(i)
        sum+=i
    i+=1
if n==1:
    print('1 is neither a prime number nor a composite number')
if sum==n+1:
    print('Prime Number')
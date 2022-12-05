# Day 19 coding Statement : Write a program to identify if the number is Armstrong number or not

# E.g. Let the number be 1634,
# Here 1^4 + 6^4 + 3 ^4 + 4^4 = 1634

n=int(input('Enter number: '))
v=n
def ArmstrongNumber(n):
    def countintegers(n):
        s=str(n)
        count=0
        for i in s:
            count+=1
        return count
    sum=0
    count=countintegers(n)  
    while n!=0:
        temp=n%10
        m=temp**count
        sum+=m
        n=n//10
    if v==sum:
        print('Armstrong Number')
    else:
        print('Not a Armstrong Number')

ArmstrongNumber(n)
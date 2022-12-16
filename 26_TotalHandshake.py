# Day 26 coding Statement : Write a program to calculate Maximum number of handshakes

n=int(input('Enter number of people: '))

def handshake(n):
    sum=0
    for i in range(1,n+1):
        sum+=(i-1)
    return sum

print(handshake(n))


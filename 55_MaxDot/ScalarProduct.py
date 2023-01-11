# Day 55 coding Statement : Given 2 integer arrays X and Y of same size. Consider both arrays as vectors and print the sum of maximum scalar product (Dot product) of 2 vectors.

# n1=[-1, -2, -3, -4]
n1=[1, 2, 3, 4]

n2=[5, 6, 7, 8]
iterate,sum=0,0

while iterate<len(n1):
    sum+=n1[iterate]*n2[iterate]
    print(n1[iterate],n2[iterate])
    iterate+=1
    print(sum)

print(sum,(8*4 + 7*3 + 6*2 + 1*5))
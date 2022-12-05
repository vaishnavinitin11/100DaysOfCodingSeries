#Day 6 coding Statement:  Write a program to find the Quadrants in which coordinates lie

n,m=input('Enter X and Y Coordinates: ').split()
n=int(n)
m=int(m)

def coordinate(n,m):
    if (n>0 and m>0):
        print('This point lies in first quadrant')
    elif (n<0 and m>0):
        print('This point lies in second quadrant')
    elif (n<0 and m<0):
        print('This point lies in third quadrant')
    elif (n>0 and m<0):
        print('This point lies in fourth quadrant')
    else:
        print('This point lies in origin')

coordinate(n,m)
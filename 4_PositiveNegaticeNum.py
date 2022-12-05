# Day 4 coding Statement:  Write a program to identify of the a number is positive or negative

v=int(input('Enter a number: '))

if v==0:
    print('Neither positive nor negative')
elif v<0:
    print('Negative Number')
elif v>0:
    print('Positive Number')
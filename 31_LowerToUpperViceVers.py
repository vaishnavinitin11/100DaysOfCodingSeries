# Day 31 coding Statement: Write a Program to Toggle each character in a string

n=input('Enter string: ')

for i in n:
    if i.islower():
        s=i.upper()
        print(s,end='')
    elif i.isupper():
        v=i.lower()
        print(v,end='')
    
# Day 32 coding Statement : Write a Program to Remove vowels from a string

n=input('Enter string: ')

for i in n:
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        continue
    print(i,end='')
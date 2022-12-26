# Day 38 coding Statement : Write a Program to print Non-repeating characters in a string

n=input('Enter string: ')

for character in n:
    sum=0
    for letter in n:
        if character==letter:
            sum+=1
    if sum==1:
        print(character,end=' ')

# Day 35 coding Statement : Write a Program to Count the sum of numbers in a string

n=input('Enter String: ')
sum=0
for i in n:
    if i>='0' and i<='9':
        v=int(i)
        sum+=v
    else:
        continue

print(sum)

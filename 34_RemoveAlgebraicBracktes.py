# Day 34 coding Statement : Write a Program to Remove brackets from an algebraic expression

n=input('Enter expression:')

for bracket in n:
    if bracket=='(' or bracket==')':
        continue
    else:
        print(bracket,end='')
# Day 9 coding Statement : Write a program to find Number of digits in an integer

n=(input('Enter n: '))
def countintegers(n):
    sum=0
    if n.isdigit():
        for i in n:
            sum+=1
        return sum
    else:
        print('Enter digit only')

d=countintegers(n)
print(type(d))
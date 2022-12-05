# Day 14 coding Statement : Write a program to reverse a given number

n=input('Enter a number: ')
'''
i=0
l=[]
while i<n:
    temp=n%10
    print(temp)
    n=n//10
    l.append(temp)
    i+=1
    
    print(n)
    
    print(l)
# temp=''.join(l)

# print(temp)
'''
# l='123'
# l=list(n)
# i=0
# s,e=0,-1
# while i<len(n):
#     # if n%2==0:
#         temp=l[s]
#         l[s]=l[e]
#         l[e]=temp
#         i+=1
# print(l[0],l)
def ReverseNumber(n):
    l=[]
    e=-1
    for letter in n:
        l.append(n[e])
        e-=1
    l=''.join(l)
    print(l)

ReverseNumber(n)
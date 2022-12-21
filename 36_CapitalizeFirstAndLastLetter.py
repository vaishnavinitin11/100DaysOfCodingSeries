# Day 36 coding Statement : Write a Program to Capitalize the first and last letter of each word of a string

n=input('Enter string: ')
n1=n.split()    
def CapitalizeLetters(n):
    l=[]
    count=0
    for i in n:
        count+=1
    for ind,value in enumerate(n):
        if ind==0 or ind==(count-1):
            updated=value.upper()
            l.append(updated)
            # print(value.upper(),end='')
        else:
            l.append(value)
    l1=''.join(l)
    return l1

for word in n1:
    word1=CapitalizeLetters(word)
    print(word1,end=' ')

# Day 39 coding Statement: Write a Program to check if two strings are Anagram or not

a,b=input('Enter two strings: ').split()

def isAnagram(a,b):
    def CountString(a):
        count=0
        for i in a:
            count+=1
        return count
    counta=CountString(a)
    countb=CountString(b)
    check=''
    if counta==countb:
        for letter in a:
            if letter in b:
                check+=letter
        if CountString(check)==counta:
            print('Anagram')
        else:
            print('Not Anagram')   
    else:
        print('Not Anagram')

isAnagram(a,b)

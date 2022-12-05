#Write a program to identify if the character is a vowel or consonant.

n=input('Enter character: ')
l=['a','e','i','o','u']
l2=''
l3=l2.join(l)
l4=l3.upper()
if len(n)==1 or n.isdigit():
    if n in l4 or n in l:
        print('Vowel')
    elif n not in l and n.isalpha():
        print('Consonant')
    else:
        print('Invalid Input')
else:
    print('Invalid enter only single character')


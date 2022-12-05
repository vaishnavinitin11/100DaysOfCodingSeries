# Day 2 coding Statement: Write a program to identify if the character is an alphabet or not.

n=input('Enter input: ')

'''
if n.isalpha():
    print('Alphabet')
else:
    print('Not an alphabet')
'''

# OR

if ((n>='A' and n<='Z') or (n>='a' and n<='z')):
    print('Alphabet')
else:
    print('Not an alphabet')


# c=ord(n)

# if (c>=65 and c<=95) or (c>=97 and c<=122):
#     print('Alphabet')
# else:
#     print('Not an alphabet')
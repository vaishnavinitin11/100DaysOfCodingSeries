# Day 40 coding Statement : Write a Program to Replace substring in a string

string=input('Enter a string: ')
replacing_substring=input('Enter a substring to be replaced: ')
new_substring=input('Enter new substring: ')

def ReplaceSubString(string,replacing_substring,new_substring):
    def CountString(a):
            count=0
            for i in a:
                count+=1
            return count
    countoldsubstring=CountString(replacing_substring)
    nstring=''
    if string[0]==replacing_substring[0] and string[countoldsubstring-1]==replacing_substring[-1]:
        nstring+=new_substring
        nstring+=string[countoldsubstring:]
    elif string[-1]==replacing_substring[-1] and string[-countoldsubstring]==replacing_substring[0]:
        nstring+=string[:-countoldsubstring]
        nstring+=new_substring
    else:
        for ind,initial in enumerate(string):
            if initial==replacing_substring[0]:
                v=ind
                if replacing_substring[-1]==string[(v+countoldsubstring)-1]:
                    nstring+=string[:ind]
                    nstring+=new_substring
                    nstring+=string[(v+countoldsubstring):]
                    break
    return nstring

print(ReplaceSubString(string,replacing_substring,new_substring))


# for i,n in enumerate(string):
#     if n==replacing_substring[0]:
#         first=i
#         while n==replacing_substring[-1]:
#             last=i
#             first+=1
#             last+=1
#             testcount=(last-first)+1
#             print(first,last,testcount)
#             countsubstring=CountString(replacing_substring)
#             if countsubstring==testcount:
#                 print('True')

# print('first-',first,'last-',last)

# testcount=(last-first)+1
# print(testcount)
# countsubstring=CountString(replacing_substring)

# if replacing_substring in string:
#     print(string(replacing_substring))
# if countsubstring==testcount:
#     print('True')
# string1=string.replace(replacing_substring,new_substring)

# print(string1)


# for i,n in enumerate(string):
#     if n==replacing_substring[0]:
#         first=i
#     if n==replacing_substring[-1]:
#         last=i
        
# first+=1
# last+=1

# Day 41 coding Statement : Check if two strings match where one string contains wildcard characters

wild_string=input('Enter string with wild characters: ')

normal_string=input('Enter string without wild characters: ')
def CountString(a):
            count=0
            for i in a:
                count+=1
            return count
for ind,val in enumerate(wild_string):
    if '*'==val:
        firstwild=ind
        break
firstwild+=1
# print(firstwild)
count=0
for i,v in enumerate(wild_string):
    if '*'==v:
        count+=1
# print(count)
lastwild=(firstwild+count)-1
# print(firstwild,lastwild)

count_wildstring=CountString(wild_string)
count_normalstring=CountString(normal_string)

# print(wild_string[:firstwild])
# print(normal_string[:firstwild])

wildsubstring=wild_string[(firstwild-1):lastwild]
# print('wildsubstring =',wildsubstring)

if count_wildstring==count_normalstring:
    if count==CountString(wildsubstring):
        
        if wild_string[:(firstwild-1)]==normal_string[:firstwild-1]:
            if wild_string[lastwild:]:
                print('Yes they match')
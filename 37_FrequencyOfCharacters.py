# Day 37 coding Statement : Write a Program to calculate the Frequency of characters in a string

n=input('Enter string: ')

def FrequencyOfCharacters(n):
    string=''
    for character in n:
        if character not in string:
            string+=character
            for letter in string:
                sum=0
                for frequency in n:
                    if letter==frequency:
                        sum+=1
            print('Frequency of character',letter,'is:',sum)

FrequencyOfCharacters(n)
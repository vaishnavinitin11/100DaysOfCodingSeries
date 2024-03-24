# Write a program for counting the number of every character of a given text file.
import collections
import pprint
with open("/Users/vaishnaviuttarkar/masterclass/100DaysOfCodingSeries/test.py",'r') as data:
    count_data = collections.Counter(data.read().upper())
    count_value=pprint.pformat(count_data)
    
print("Character Counts are :")
print(count_value)
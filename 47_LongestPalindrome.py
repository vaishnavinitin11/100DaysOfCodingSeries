# Day 47 coding Statement: Write Program to find longest palindrome in an array

def DynamicArray():
    narr=int(input('Enter size of an array: '))
    array=[]
    for i in range(narr):
        enternum=input('Enter items of an array: ')
        array.append(enternum)
    return array
array=DynamicArray()
def Palindrome(n):
    l=[]
    e=-1
    for letter in n:
        l.append(n[e])
        e-=1
    l=''.join(l)
    if n==l:
        return True
    else:
        return False
def CountString(a):
    count=0
    for i in a:
        count+=1
    return count
palArray=[]
PalCount=[]
for palindrome in array:
    if Palindrome(palindrome)==True:
        palArray.append(palindrome)
        countPal=CountString(palindrome)
        PalCount.append(countPal)
i1=0
for i in PalCount:
    if i>i1:
        i1=i
for ind,grtnum in enumerate(PalCount):
    if i1==grtnum:
        print(palArray[ind])
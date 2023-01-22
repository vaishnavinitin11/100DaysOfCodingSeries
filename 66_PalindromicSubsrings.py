# Day 66 coding Statement : Palindromic substrings

def substring(a):
    a1=[]
    for ind1,i in enumerate(a):
        for ind,j in enumerate(a):
            a1.append(a[ind1:ind+1])
    return a1
        
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


# to remove empty substrings / to filter non-empty substrings
def filterSubStr(a1):
    a2=[]
    for ss in a1:
        if len(ss)>0:
            a2.append(ss)
    return a2

tc=int(input('Enter number of testcases: '))
for t in range(tc):
    a=input('Enter a: ')
    b=input('Enter b: ')

    a1=substring(a)       
    b1=substring(b)

    a2=filterSubStr(a1)       
    b2=filterSubStr(b1)

    result=[]
    for sub in a2:
        for sub1 in b2:
            sum=sub+sub1
            if Palindrome(sum)==True:
                result.append('True')
            else:
                result.append('False')

    if 'True' in result:
        print('Yes')
    else:
        print('No')
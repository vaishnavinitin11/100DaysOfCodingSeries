# Day 81 coding Statement : 

def reverseString(n):
    r=-1
    r1=''
    for i in n:
        r1+=n[r]
        r-=1
    return(r1)

# to check whether string is sorted
def isBinarySort(s):
    for ind,i in enumerate(s):
        if i=='1':
            ss=s[ind:]
            break
        else:
            continue
    count=0
    for j in ss:
        if j=='1':
            count+=1
    if count==len(ss):
        return True
    else:
        return False

def change(s):
    global mincount
    if isBinarySort(s)==True:
        return
    
    l=[]
    mincount+=1
    for ine,id in enumerate(s):
        if id=='1':
            num=ine
            break
    for inv,v in enumerate(s[num+1:]):
        l.append(v)
        if (v=='1') and ('0' in l):
            num1=inv+num
            break
    revsub=reverseString(s[num:num1+1])
    s=s[:num]+revsub+s[num1+1:]
    print(s)
    change(s)

t=int(input('Enter number of test cases: '))
while t!=0:
    n=int(input('Enter length of binary string: '))
    s=input('Enter binary string: ')
    s+='1'
    mincount=0
    q=len(s)-1

    change(s)
    print(mincount)
    t-=1
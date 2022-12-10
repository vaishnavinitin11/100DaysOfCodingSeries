
n=int(input('Enter a number: '))
oddnum=[]
for odd in range(1,2*n):
    if odd%2!=0:
        oddnum.append(odd)
ind=0
for i in range(1,n+1):
    for space in range(n-i):
        print(' ',end='')
    while ind<i:
        print('*'*oddnum[ind])
        ind+=1
    
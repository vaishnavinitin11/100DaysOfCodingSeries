# Day 79 coding Statement : 

# You are given a binary string S of length N. You can perform the following operation on S:

# Pick any set of indices such that no two picked indices are adjacent.
# Flip the values at the picked indices (i.e. change 0 to 1 and 1 to 0).
# For example, consider the string S=1101101.
# If we pick the indices {1,3,6}, then after flipping the values at picked indices, we will get 1?10?110?1→0111111.
# Note that we cannot pick the set {2,3,5} since 2 and 3 are adjacent indices.
t=int(input('Enter test cases:'))
while t!=0:
    n1=int(input('Enter length: '))
    S=input('Enter binary string: ')
    a=[]
    count=0
    for ind,itt in enumerate(S):
        count+=1
        if itt=='1':
            a.append(ind)
    o=[]
    e=[]
    for j in a:
        if j%2==0:
            e.append(j)
        else:
            o.append(j)

        # print(a)
    sp=[]
    for j in o:
        if (j-1)in e:
            if (j-1) not in sp:
                sp.append(j-1)
        if (j+1) in e:
            if (j+1) not in sp:
                sp.append(j+1)
    if len(a)==0:
        print(0)
    elif len(sp)>0:
        print(2)
    else:
        print(1)

    t-=1


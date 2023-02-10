# Day 73 coding Statement : A string is called boring if all the characters of the string are same.

t=int(input('Enter test cases: '))

while t!=0:
    leng=int(input('Enter length of string: '))
    s=input('Enter String: ')

    def substring(a):
        a1=[]
        for ind1,i in enumerate(a):
            for ind,j in enumerate(a):
                a1.append(a[ind1:ind+1])
        return a1

    s1=substring(s)

    same=[]
    for item in s1:
        countw=0
        wo=[]
        for it in item:
            countw+=1
        if countw==1:
            same.append(item)
        else:
            for itt in item:
                if itt not in wo:
                    wo.append(itt)
            if len(wo)==1:
                same.append(item)

    sub_dict={}
    max_l=0
    for substr in same:
        if substr in sub_dict:
            sub_dict[substr]+=1
        else:
            sub_dict[substr]=1

    for ss in sub_dict:
        if sub_dict[ss]>1 and len(ss)>max_l:
            max_l=len(ss)

    print(max_l)
    t-=1

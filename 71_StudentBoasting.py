# Day 71 coding Statement : There are N students in a class, where the i-th student has a score of Ai?.
tc=int(input('Enter testcases: '))
l=[]
for iter in range(tc):
    numStds=int(input('Enter number of students: '))
    score=(input('Enter score: '))
    l1=[]
    for item in score.split(' '):
        l1.append(int(item))
    l.append(l1)

    c1=0
    for ind,i in enumerate(l1):
        count=0
        for ind1,j in enumerate(l1):
            if ind==ind1:
                # print(i,j)
                continue
            elif i>=j:
                count+=1
        if count>=1:
            c1+=1

    print(c1)
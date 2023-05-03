# You are given N integers. In each step you can choose some K of the remaining numbers and delete them, if the following condition holds: Let the K numbers you've chosen be a1, a2, a3, ..., aK in sorted order. Then, for each i ≤ K - 1, ai+1 must be greater than or equal to ai * C.
for t in range(int(input('Enter test cases: '))):
    n,k,c=list(map(int,input('Enter N, K & C: ').split()))
    l=list(map(int,input('Enter elements of array: ').split()))
    count1=0
    def removeKelements(l):
        global count1
        count=0
        l1=l[:k]
        l1.sort()
        for i,val in enumerate(l1):
            if (i+1)<k:
                if l1[i+1]>=(l1[i]*c):
                    count+=1
        if count==(k-1):
            for j in l[:k]:
                l.remove(j)
        else: 
            return
        count1+=1
        removeKelements(l)
    removeKelements(l)
    print(count1)

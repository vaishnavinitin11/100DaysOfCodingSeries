# Day 67 coding Statement: Bricks Breaking

tc=int(input('Enter number of testcases: '))

for i in range(tc):
    sum=0
    s,w1,w2,w3=list(map(int,input('Enter  s, w1, w2, w3: ').split()))
    if (w1+w2+w3)%s==0:

        sum+=(w1+w2+w3)//s
    else:
        sum+=(w1+w2+w3)//s
        sum+=1

    print(sum)
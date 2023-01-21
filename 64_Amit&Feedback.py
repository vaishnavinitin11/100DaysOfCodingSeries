# Day 64 coding Statement: Amit and Feedback

tc=int(input('Enter number of testcases: '))

for i in range(tc):
    ss_arr=[]
    fb=input('Enter your geeky feedback: ')
    f,l=0,3
    for j in range(len(fb)):
        ss=fb[f:l]
        ss_arr.append(ss)
        f+=1;l+=1
    if ('010' or '101') in ss_arr:
        print('GOOD')
    else:
        print('BAD')
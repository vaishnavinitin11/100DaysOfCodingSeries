# Day 57 coding Statement :
#  "Is Anusree Pass or Fail"
# First Test case:
# 5 * 3 =15
# 2 * 3 = 6 but -3 coz 3 Q were incorrect So = 3
# Passing Marks = 3 So Anusree passed 
print('For each test case you need to provide N,X,P line-wise')
# Test case
n=int(input('Enter number of test cases: '))
l=[]
for i in range(n):
    subl=[]
    for j in range(3):
        N=int(input('Enter Number: '))
        subl.append(N)
    l.append(subl)
    
for lis in l:
    N=lis[0]
    X=lis[1]
    P=lis[2]
    correct_marks=X*3
    incorr_marks=N-X
    Obtained_marks=correct_marks-incorr_marks
    if Obtained_marks>=P:
        print('PASS')
    else:
        print('FAIL')
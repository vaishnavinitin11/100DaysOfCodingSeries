num = int(input('Enter a number :'))
arr = []
for i in range(2,num):
    flag = 0
    for j in range(2,i):
        if i % j == 0:
            flag = 1
    if flag == 0:
        arr.append(i)
flag = 0
for i in range(len(arr)):
    for j in range(i,len(arr)):
        if(arr[i] + arr[j] == num):
            flag = 1
            print(str(num) + " can be expressed as the sum of " + str(arr[i]) + " and " + str(arr[j]))
            break
print(arr)
if(flag == 0):
 print('No Prime numbers can give sum of ' + str(num))
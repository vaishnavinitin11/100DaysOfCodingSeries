
n=int(input('Enter a number: '))

for i in range(n):
    for j in range(i+1):
        print('v',end='')
    print('\n')

# Reverse form
'''
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print('*',end='')
    print('\n')
'''
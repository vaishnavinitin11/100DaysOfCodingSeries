# Day 11 coding Statement:  Write a program to find Fibonacci series up to n

# n=int(input('Enter Length of series: '))
# def fibonacci(n):
#     n1=0
#     n2=1
#     n3=n1+n2
#     series=[0,1]
#     for i in range(2,n):
#         n3=n1+n2
#         series.append(n3)
#         n1=n2
#         n2=n3
#     print(series) 
   
# fibonacci(n)

num = int(input("Enter the Number:"))
a, b = 0, 1
print("Fibonacci Series:", a,",", b, end=" , ")
for i in range(2, num):
    c = a + b
    a = b
    b = c
    print(c,",", end=" ")
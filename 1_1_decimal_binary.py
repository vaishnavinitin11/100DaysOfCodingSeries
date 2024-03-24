n=int(input("Enter Input: "))
bin_str=""
while (n/2.0)!=0:
    bin_str+=str(n%2)
    n=n//2

print(bin_str[::-1])

# # n = int(input("Enter Input: "))

# while n > 0:
#     print(n % 2,end='')
#     n = n >> 1
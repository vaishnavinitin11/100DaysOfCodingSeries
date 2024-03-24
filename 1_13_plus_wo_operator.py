def add_without_plus(a,b):
    while(b!=0):
        num=a&b
        a=a^b
        b=num<<1
    print(a)

def subtract(a,b):
    print(a+~b+1)

subtract(18,1)
add_without_plus(9,120)
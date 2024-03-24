def funct(a):
    '''Lambda Function'''
    x=lambda a:a*2
    return x

x = lambda a, b: a * b * 0.5
print(x(5, 6))

# print(funct(2))

is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
for item in is_even_list:
	print(item())

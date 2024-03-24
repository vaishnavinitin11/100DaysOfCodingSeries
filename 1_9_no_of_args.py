# Write python function which takes a variable number of arguments.
def funct(*args):
    print(f"Args: {args}")
    # print(list(args))

funct(1,2,3,4,5,6)
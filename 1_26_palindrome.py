# Palindrome

def is_palindrome(string):
    e,r=-1,1
    for i in range(len(string)):
        if(string[i]==string[e]):
            e-=1
        else:
            r*=0
    if(r!=0):
        return True
    else:
        return False

print(is_palindrome('1210121'))
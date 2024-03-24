# WAP (Write a program) which takes a sequence of numbers and check if all numbers are unique.

def unique_arr_validtn(arr):
    if(len(arr)==len(set(arr))):
        return True
    else:
        return False
    

print(unique_arr_validtn([1,2,7,7,8,9,9,2,4])) 

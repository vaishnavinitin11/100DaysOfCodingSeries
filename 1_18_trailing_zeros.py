import time
def trailing_zeros(n):
    count=0
    if(n==0):
        count=1
    else:
        while n>0:
            n=int(n/5)
            count+=n
    return count
    
def test_trailing_zeros():
    test_cases = [5, 10, 20,54454553232333434445084758475578535454]
    for n in test_cases:
        start_time = time.time()
        result = trailing_zeros(n)
        end_time = time.time()
        print(f"Input: {n}, Output: {result}, Time: {end_time - start_time} seconds")
def factorial_trailing_zeros(n):
    fact = n
    while n > 1:
        fact *= n - 1
        n -= 1
    result = 0
    for i in str(fact)[::-1]:
        if i == "0":
            result += 1
        else:
            break
    return result
    
print(trailing_zeros(5000000000000847584755785000))
test_trailing_zeros()
# print(factorial_trailing_zeros(5000000))
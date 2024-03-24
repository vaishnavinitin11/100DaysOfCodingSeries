#linear search

def linear_search(arr,n):
    for ind,i in enumerate(arr):
        if i==n:
            return ind

# arr=[1,2,3,4,86,32]
# n=4

arr=list(map(int,input("Enter array: ").split()))
n=int(input("Enter number: "))
print(linear_search(arr,n))

# select * from EmployeeInfo where first_name not in ('Sanjay','Sonia')
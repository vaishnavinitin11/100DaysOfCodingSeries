def compute(arr):
    n = len(arr);total = 0
    for i in range(n - 2):
        j = i + 1
        for k in range(i + 2, n):
            mid = (arr[i] + arr[k]) / 2
            while (j < (k - 1)) and abs(arr[j + 1] - mid) <= abs(arr[j] - mid):j += 1
            total += (arr[i] - arr[j]) * (arr[j] - arr[k])
    return total
for t in range(int(input())):n = int(input());print(compute(list(map(int, input().split()))))
def minDistance(word1, word2):
    m = len(word1)
    n = len(word2)
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        dp[i][0] = 1 + dp[i - 1][0]
    
    for i in range(1, m + 1):
        dp[0][i] = 1 + dp[0][i - 1]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if word2[i - 1] == word1[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
        # print(len(dp))
    
    return dp[n][m]

# Example usage
word1 = "vaishnavi"
word2 = "vaishu"
print(minDistance(word1, word2))  # Output: 3

'''
[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
 [1, 0, 1, 2, 3, 4, 5, 6, 7, 8], 
 [2, 1, 0, 1, 2, 3, 4, 5, 6, 7], 
 [3, 2, 1, 0, 1, 2, 3, 4, 5, 6], 
 [4, 3, 2, 1, 0, 1, 2, 3, 4, 5], 
 [5, 4, 3, 2, 1, 0, 1, 2, 3, 4], 
 [6, 5, 4, 3, 2, 1, 1, 2, 3, 4]]
 '''
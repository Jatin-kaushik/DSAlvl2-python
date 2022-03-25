def goldmine(r,c,arr):
    dp = [[None]*(c) for i in range(r)]
    for j in range(c-1, -1, -1):
        for i in range(r):
            if j == c-1:#last column choti problem jaha se khi ni jaa skte'
                dp[i][j] = arr[i][j]
            elif i == 0: # first row
                dp[i][j] = arr[i][j] + max(dp[i][j+1], dp[i+1][j+1])
            elif i == r-1: # last row
                dp[i][j] = arr[i][j] + max(dp[i][j+1], dp[i-1][j+1])
            else:
                dp[i][j] = arr[i][j] + max(dp[i][j+1], max(dp[i-1][j+1], dp[i+1][j+1]))
    maxpro = -1
    for i in range(r):
        if dp[i][0] > maxpro:
            maxpro = dp[i][0]
    
    return maxpro
                

r = int(input())
c = int(input())
arr = []
for i in range(r):
    arr.append(list(map(int, input().split(" "))))
print(arr)
# print(goldmine(r,c,arr))
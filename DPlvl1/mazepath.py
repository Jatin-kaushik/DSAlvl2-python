def maze(r,c, arr, dp):
    for i in range(r-1, -1, -1):
        for j in range(c-1,-1,-1):
            if i == r-1 or j == c-1: #corner cases
                if i==r-1 and j == c-1:
                    dp[i][j] = arr[i][j]
                elif i==r-1 and j<c-1:
                    dp[i][j] = arr[i][j] + dp[i][j+1]
                elif i<r-1 and j == c-1:
                    dp[i][j] = arr[i][j] + dp[i+1][j]
            else: # mid cases
                dp[i][j] = arr[i][j] + min(dp[i+1][j], dp[i][j+1])
    return dp[r-1][c-1]

r = int(input())
c = int(input())
arr = []
dp = []
for i in range(r):
    ls = list(map(int, input().split()))
    arr.append(ls)
    dp.append([None]*(c))
print(maze(r,c, arr, dp))
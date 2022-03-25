n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

dp = []
dp.append([0]*n)
dp.append([0]*n)
dp[0][0] = arr[0]
dp[1][0] = 0
for i in range(1,n):
    dp[0][i] = dp[1][i-1]+arr[i] #inclusive
    dp[1][i] = max(dp[0][i-1], dp[1][i-1]) #exclude

print(max(dp[0][n-1], dp[1][n-1]))
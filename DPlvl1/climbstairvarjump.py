def climbstairvar(n, vjmp):
    dp = [0]*(n+1)
    dp[n] = 1
    for i in range(n-1, -1, -1):
        dp[i] = 0
        for j in range(i+1, i+1+vjmp[i]):
            if j<len(dp):
                dp[i] = dp[i]+dp[j]
    return dp[0]

n = int(input())
vjmp = [int(input()) for i in range(n)]
print(climbstairvar(n,vjmp))
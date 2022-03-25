def ccp(n, arr):
    dp = [0]*(target+1)
    dp[0] = 1
    for i in range(1, target+1):
        for coin in arr:
            if coin >= i:
                dp[i] += dp[i-coin]
    return dp[-1]
            

n = int(input())
arr = [int(input()) for i in range(n)]
target = int(input())
print(ccp(n, arr, target))
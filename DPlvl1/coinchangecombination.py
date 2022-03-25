def ccc(n, arr):
    dp = [0]*(target+1)
    dp[0] = 1
    for i in arr:
        for j in range(i, target+1):
            coin = i
            dp[j]+= dp[j -coin]
    return dp[-1]
            

n = int(input())
arr = [int(input()) for i in range(n)]
target = int(input())
print(ccc(n, arr, target))
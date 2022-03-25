# 2^n subset is possible for n length array
def tabu_tss(idx, arr, target):
    dp = [[False]*(target+1) for i in range(len(arr)+1)]
    for i in range(len(dp)):
        dp[i][0] = True
    for i in range(1,len(dp)):
        for j in range(1, len(dp[0])):
            ele = arr[i-1]
            if j >= ele:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-ele]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[len(arr)][target]
        
n = int(input())
arr = [int(input()) for i in range(n)]
target = int(input())
print(tabu_tss(0,arr,target))
def minmove(n, arr):
    dp = [None]*(n+1)
    dp[n] = 0
    print(n, arr, dp)
    for i in range(n-1, -1, -1):
        print(arr[i])

        if arr[i]>0:
            minway = 9999999
            print(arr[i])
            for j in range(i+1, i+1+arr[i]):
                # print(i,j)
                if j<len(dp) and dp[j] != None:
                    minway = min(minway, dp[j])
                    # print(minway)
            
            if minway != 9999999:
                dp[i] = minway+1
        # return dp[0]
            
    
    
n = int(input())
arr = [int(input()) for i in range(n)]
print(n, arr)
minmove(n, arr)
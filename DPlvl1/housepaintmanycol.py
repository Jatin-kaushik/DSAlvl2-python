def housemanycol(arr, dp):
    mi = 9999999
    smi = 9999999
    for i in range(len(dp[0])):
        dp[0][i] = arr[0][i]
        if dp[0][i] <= mi:
            smi = mi
            mi = dp[0][i]
        elif dp[0][i] < smi:
            smi = dp[0][i]
    
    # print(dp)
    for i in range(1, len(dp)):
        nmi = 9999999
        snmi = 9999999
        for j in range(len(dp[0])):
            if dp[i-1][j] == mi:
                dp[i][j] = smi + arr[i][j]
            else:
                dp[i][j] = mi + arr[i][j]
            
            if dp[i][j] <= nmi:
                snmi = nmi
                nmi = dp[i][j]
            elif dp[i][j] < snmi :
                snmi = dp[i][j]
        mi = nmi
        smi =snmi
    
    ans  = 9999999
    for i in range(len(dp[0])):
        if dp[len(dp)-1][i] < ans:
            ans = dp[len(dp)-1][i]
    return(ans)

nh, c = list(map(int, input().split()))
# print(c,h)
dp =[]
arr = []
for i in range(nh):
    dp.append([0]*c)
    b= []
    inp = list(map(int, input().split()))
    arr.append(inp)
print(housemanycol(arr, dp))


n = int(input())
values = list(map(int, input().split(" ")))
wts = list(map(int, input().split(" ")))
bc = int(input())

dp = []
for i in range(n+1):
    dp.append([0]*(bc+1))

for i in range(1, n+1):
    for j in range(1, bc+1):
        idx = i-1
        wt = wts[idx]
        val = values[idx]
        if j>= wt: 
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-wt]+val)
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][bc])
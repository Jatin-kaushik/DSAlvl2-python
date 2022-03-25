n = int(input())
dp = []
dp.append([None]*(n+1))
dp.append([None]*(n+1))
dp[0][1] = 1
dp[1][1] = 1

for i in range(2, n+1):
    dp[0][i] = dp[1][i-1] #i-1 me  1 wa6lei h unke peeche 0 lagado
    dp[1][i] = dp[0][i-1] + dp[1][i-1] # i-1 me 1 or 0  walei dono ke peeche 1 lagado
    # print(dp)
print(dp[0][n] + dp[1][n])
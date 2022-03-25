def pf(n,k):
    dp = []
    for i in range(3):
        dp.append([0]*(n+1))
    dp[0][1] = 0 # first fence with same as prev color = 0
    dp[1][1] = k # first fence with diff. as prev color = 3 , R,G,B (if col = 3)
    dp[2][1] = k # total 
    for i in range(2, n+1):
        dp[0][i] = dp[0+1][i-1] # jab last 2 diff honge tbhi unke aage same laga ke 2 duplicacy ka bana skte h
        dp[1][i] = dp[1+1][i-1]*(k-1) # j total ke peeche rem 2 colo laga do diff gen ho jayenge
        dp[2][i] = dp[0][i] + dp[1][i]
    return dp[2][n]
n = int(input())
k = int(input())
print(pf(n,k))
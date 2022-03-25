n = int(input())
values = list(map(int, input().split()))
wts = list(map(int, input().split()))
cap = int(input())

dp = [0]*(cap+1)

for i in range(1, len(dp)):
    for j in range(len(wts)):
        wt = wts[j]
        val = values[j]
        if wt <= i:
            dp[i] = max(dp[i-wt] +val, dp[i])
print(dp)

n = int(input())

h_arr = []
h_arr.append([0]*n)
h_arr.append([0]*n)
h_arr.append([0]*n)


for i in range(n):
    arr = list(map(int, input().split(" ")))
    # print(arr)
    h_arr[0][i] = arr[0]
    h_arr[1][i] = arr[1]
    h_arr[2][i] = arr[2]

dp = []
dp.append([0]*n)
dp.append([0]*n)
dp.append([0]*n)

dp[0][0] = h_arr[0][0]
dp[1][0] = h_arr[1][0]
dp[2][0] = h_arr[2][0]

for i in range(1,n):
    dp[0][i] = arr[0][i] + min(dp[1][i-1], dp[2][i-1]) #red se krna hi to red + min of last blue and green house
    dp[1][i] = arr[1][i] + min(dp[0][i-1], dp[2][i-1])
    dp[2][i] = arr[2][i] + min(dp[0][i-1], dp[1][i-1])


print(min(dp[0][n-1], min(dp[1][n-1], dp[2][n-1])))
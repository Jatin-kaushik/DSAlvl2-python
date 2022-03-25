from readline import append_history_file


n = int(input()) #799leet
#lets solve for single lane it's same like 01 subs problem jaha 2 00 ek sath ni aa skte
dp = []
dp.append([None]*(n))
dp.append([None]*(n))

dp[0][0] = 1 #jo building se khtm hui
dp[1][0] = 1 # jo space se khtm hui
for i in range(1, n):
    dp[0][i] = dp[1][i-1] #jo B se khtm honge uske lie last me jo space se khtm hue the vo chaie
    dp[1][i] =  dp[0][i-1] + dp[1][i-1] # jo S se khtm honge uske lie ham last se space Buil dono use kr skte h

tot_ways = dp[0][n-1] + dp[1][n-1]
print(tot_ways*tot_ways)
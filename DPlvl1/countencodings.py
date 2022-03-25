def encoding(n):
    dp = [0]*(len(n)+1)
    if n[0] == 0:
        return 0
    dp[0] = 1
    for i in range(1, len(dp)):
        if i == 1:
            dp[i] = dp[i-1]
        else:
            # print("1here")

            ele =n[i-1]
            lele = n[i-2]
            if ele == "0" and lele != "0":
                # print("2here")
                if int(lele+ele)>0 and int(lele+ele) <=26:
                    dp[i] = dp[i-2]
                else:
                    dp[i] = 0
            elif ele != "0" and lele == "0":
                # print("3here")
                dp[i] = dp[i-1]
            else:
                # print("4here")
                if int(lele+ele) >0 and int(lele+ele) <=26:
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1]
    return dp

# def encoding(n):
#     dp = [0]*(len(n)+1)
#     if n[0] == 0:
#         return 0
#     dp[0] = 1
#     dp[1] = 1
#     for i in range(2, len(dp)):
#         ele =n[i-1]
#         lele = n[i-2]
#         num = int(lele + ele)
#         if ele != 0:
#             dp[i] = dp[i-1]
#         if lele !=0 and num <=26:
#             dp[i] += dp[i-2]

#     return dp[len(n)] 
 

n = input()
print(encoding(n))
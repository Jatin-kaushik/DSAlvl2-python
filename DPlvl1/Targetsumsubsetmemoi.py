# 2^n subset is possible for n length array
def memoi_tss(idx, arr, target,dp):
    # print(idx, target)
    if target == 0:
        return True
    if idx == len(arr):
        return False
    
    if dp[idx][target] != None:
        return dp[idx][target]
    excluder = memoi_tss(idx+1, arr, target,dp)
    includer = memoi_tss(idx+1, arr, target-arr[idx],dp)
    
    ans = excluder or includer
    dp[idx][target] = ans
    return ans
n = int(input())
arr = [int(input()) for i in range(n)]
target = int(input())
dp = [[None]*(target+1) for i in range(n+1)]
print(memoi_tss(0,arr,target, dp))

''' Memoization ke lie ab 2 tareeke hain ya to Array banao ya dict
in Array : size = Arr[len(arr)][Target] isme kis index ke baad utna target bana skte h? ye store hoga yes nd No
dict me direct key pass krdenge idxwithtarget agr vo true hogi to direct true else false(isme Doubt hain)'''
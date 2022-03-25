# 2^n subset is possible for n length array
def recursion_tss(idx, arr, target):
    if target == 0:
        return True
    if idx == len(arr):
        return False
    excluder = recursion_tss(idx+1, arr, target)
    includer = recursion_tss(idx+1, arr, target-arr[idx])
    ans =  excluder or includer
    return ans
n = int(input())
arr = [int(input()) for i in range(n)]
target = int(input())
print(recursion_tss(0,arr,target))


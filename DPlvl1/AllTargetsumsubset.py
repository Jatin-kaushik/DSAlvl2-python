# 2^n subset is possible for n length array
def all_tss(idx, arr, target):
    if target == 0:
        bres = [" "]
        return bres
    if idx == len(arr):
        bres = []
        return bres
    excluders = all_tss(idx+1, arr, target)
    includers = all_tss(idx+1, arr, target-arr[idx])
    
    res = []
    for i in excluders:
        res.append(i)
    for i in includers:
        res.append(i +" " + arr[idx])
    return res
        
n = int(input())
arr = [int(input()) for i in range(n)]
target = int(input())
print(all_tss(0,arr,target))
def solve(n ,arr):
    res = [0,0,0]
    dict1 = {}
    mf = -1
    for i in range(n):
        ele = arr[i]
        if ele in dict1:
            dict1[ele].append(i)
        else:
            dict1[ele] = [i]
        
        f = dict1[ele]
        if len(f) > mf:
            mf = len(f)
            res[0], res[1], res[2] = ele, f[0], f[-1]
    return res
 
n = int(input())
arr = list(map(int, input().split()))
a = solve(n,arr)
for i in a:
    print(i)
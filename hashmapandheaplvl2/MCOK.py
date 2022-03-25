def solve(n, arr,k):
    ir = -1
    dict1 = {}
    l = -1
    for i in range(len(arr)):
        ele = arr[i]
        if ele in dict1:
            dict1[ele]+=1
        else:
            dict1[ele] = 1
        if ele == 1:
            if (i - (ir+1) +1)>l: 
                l = (i - (ir+1) +1)
        else:
            if dict1[ele] <=k:
                if (i - (ir+1) +1)>l: 
                    l = (i - (ir+1) +1)
            if dict1[ele] >k:
                while(ir<i):
                    if dict1[0] <= k:
                        break
                    ele = arr[ir+1]
                    dict1[ele] -=1
                    ir+=1
                if (i - (ir+1) +1)> l:
                    l = (i - (ir+1) +1)
    return l

n = int(input())
arr = list(map(int, input().split()))
k = int(input())
print(solve(n, arr, k))
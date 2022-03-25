def checkap(n, arr):
    fmin = arr[0]
    smin = 9999999
    for i in range(1, n):
        if arr[i] <= fmin:
            smin = fmin
            fmin = arr[i]
        elif arr[i] <smin:
            smin = arr[i]
    diff = smin-fmin
    dict1 = {}
    for i in arr:
        if i in dict1:
            return("No")
        else:
            dict1[i] = 1
    t = smin + diff
    for i in range(n-2):
        if t not in dict1:
            return ("No")
        t+=diff
    return ("Yes")
n = int(input())
arr= list(map(int, input().split()))
print(checkap(n, arr))
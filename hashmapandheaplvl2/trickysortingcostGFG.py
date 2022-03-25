def solve(arr):
    dict1 = {}
    for i in arr:
        if dict1[i-1] in dict1:
            dict1[i] = dict1[i-1] +1
        else:
            dict1[i] = 1
    lonsubs= 0 
    for k,v in dict1.items():
        if v>lonsubs:
            lonsubs = v
    return len(arr)-lonsubs
arr =list(map(int, input().split()))
print(solve(arr))
def sol(n,arr,k):
    dict1 = {}
    i = 0
    while i<k:
        if arr[i] in dict1:
            dict1[arr[i]] +=1
        else:
            dict1[arr[i]] = 1
        i+=1
    print(len(dict1), end = " ")

    while i<n:
        ele = arr[i]
        if arr[i-k] in dict1:
            if dict1[arr[i-k]] == 1:
                dict1.pop(arr[i-k])
            else:
                dict1[arr[i-k]]-=1
        if ele in dict1:
            dict1[ele] +=1
        else:
            dict1[ele] = 1
        print(len(dict1), end = " ")
        i+=1
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

sol(n,arr,k)
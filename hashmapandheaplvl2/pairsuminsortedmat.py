def solve(arr1, arr2, tar):
    dict1 = {}
    for i in arr1:
        for j in i:
            if j in dict1:
                dict1[j] +=1
            else:
                dict1[j] = 1
    c = 0
    for i in arr2:
        for j in i:
            fele = tar-j
            if fele in dict1:
                c += dict1[fele]
    return c
n = int(input())
arr1 = []
arr2 = []
for i in range(n):
    ls= list(map(int, input().split()))
    arr1.append(ls)
for i in range(n):
    ls= list(map(int, input().split()))
    arr2.append(ls)
tar = int(input())
print(solve(arr1, arr2, tar))
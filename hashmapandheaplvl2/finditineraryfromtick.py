def solve(arr):
    dict1 = {}
    set1 = set()
    res = []
    for i in arr:
        dict1[i[0]] = i[1]
        set1.add(i[0])
    for i in arr:
        val = dict1[i[0]]
        if val in set1:
            set1.remove(val)
    # print(list(set1))
    src = list(set1)[0]
    res.append(src)
    # print(src, end = " -> ")
    while True:
        if src in dict1:
            res.append(dict1[src])
            src = dict1[src]
        else:
            break;
    return res
n = int(input())
arr = []
for i in range(n):
    arr.append(input().split())
a = solve(arr)
for i in range(len(a)-1):
    print(a[i], end = " -> ")
print(a[len(a)-1] + ".")
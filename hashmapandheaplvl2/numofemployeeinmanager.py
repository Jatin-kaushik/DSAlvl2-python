
def sizeoftree(graph, root , res):
    if root not in graph:
        res[root] = 0
        return 1
    sz = 0
    child = graph[root]
    for i in child:
        cs = sizeoftree(graph, i, res)
        sz+=cs
    res[root] = sz
    return sz+1

def solve(n,arr):
    dict1 = {}
    root = None
    for i in range(n):
        emp, man = arr[i][0], arr[i][1]
        if man == emp:
            root= man
            continue
        if man in dict1:
            dict1[man].append(emp)
        else:
            dict1[man] = [emp]
    res = {}
    sizeoftree(dict1, root, res)
    for k,v in res.items():
        print(k + " " + str(v))
n = int(input())
arr = []
for i in range(n):
    arr.append(input().split())
solve(n,arr)
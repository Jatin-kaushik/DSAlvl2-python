class Node:
    def __init__(self, src, nbr, wt):
        self.src = src
        self.nbr = nbr
        self.wt = wt
        
def solve(src,graph, visited, ls):
    visited.add(src)
    ls.append(src)
    # print(src, end = " ")
    for child in graph[src]:
        # print(child.nbr)
        if child.nbr not in visited:
            solve(child.nbr,graph, visited, ls)

vtc = int(input())
edges = int(input())
graph = {}
for i in range(vtc):
    graph[i] = []
    
for i in range(edges):
    values = input().split()
    v1 = int(values[0])
    v2 = int(values[1])
    wt = int(values[2])
    e1 = Node(v1, v2, wt)
    e2 = Node(v2, v1, wt)
    graph[e1.src].append(e1)
    graph[e2.src].append(e2)

# src = int(input())
visited = set() 
res = []
for i in range(vtc):
    if i not in visited:
        ls = []
        solve(i,graph, visited, ls)
        # print(ls)
        res.append(ls)
print(res)

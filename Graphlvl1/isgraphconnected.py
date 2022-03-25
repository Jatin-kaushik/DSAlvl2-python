class Edge:
    def __init__(self, src, nbr, wt):
        self.src = src
        self.nbr = nbr
        self.wt = wt

def solve(src, graph, visited, ls):
    visited.add(src)
    ls.append(src)
    
    for child in graph[src]:
        if child.nbr not in visited:
            solve(child.nbr, graph, visited, ls)

vtc = int(input())
edges = int(input())
graph = {}
for i in range(vtc):
    graph[i] = []

for i in range(edges):
    val = input().split()
    v1 = int(val[0])
    v2 = int(val[1])
    wt = int(val[2])
    e1 = Edge(v1,v2,wt)
    e2 = Edge(v2,v1,wt)
    graph[e1.src].append(e1)
    graph[e2.src].append(e2)

visited = set()
res = []
bool = True
for i in range(vtc):
    if i not in visited:
        ls = []
        solve(i, graph, visited, ls)
        res.append(ls)
        if len(res)>1:
            bool = False
            break
if bool: print("true")
else: print("false")
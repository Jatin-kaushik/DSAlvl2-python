class Edge:
    def __init__(self, src, nbr):
        self.src = src
        self.nbr = nbr
        
def solve(i, graph, visited, ls):
    visited.add(i)
    ls.append(i)
    for child in graph[i]:
        if child.nbr not in visited:
            solve(child.nbr, graph, visited, ls)
vtc = int(input())
edges =  int(input())
graph = {}
for i in range(vtc):
    graph[i] = []

for i in range(edges):
    val = input().split()
    v1 = int(val[0])
    v2 = int(val[1])
    e1 = Edge(v1, v2)
    e2 = Edge(v2, v1)
    
    graph[e1.src].append(e1)
    graph[e2.src].append(e2)

visited = set()
res = []
for i in range(vtc):
    if i not in visited:
        ls = []
        solve(i, graph, visited, ls)
        res.append(ls)
c = 0
for i in range(len(res)):
    for j in range(i, len(res)):
        c+= len(i)*len(j)
print(c)
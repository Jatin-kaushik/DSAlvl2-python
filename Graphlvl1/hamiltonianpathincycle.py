class Edge:
    def __init__(self, src, nbr, wt):
        self.src = src
        self.nbr = nbr
        self.wt = wt
def solve(vtc, src, graph, visited, res, count, psf):
    # print(src, count)
    if count == vtc-1:
        res.append(psf)
    visited.add(src)
    count+=1
    for child in graph[src]:
        # print(child)
        if child.nbr not in visited:
            solve(vtc, child.nbr, graph, visited, res, count, psf+ str(child.nbr))
    visited.remove(src)
    count-=1
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
# print(graph[0].nbr)
visited = set()
res = []
src= int(input())
solve(vtc, src, graph, visited, res, 0, str(src))   
for i in res:
    fele = int(i[0])
    lele = int(i[-1])
    flag = False
    for child in graph[fele]:
        if child.nbr == lele:
            flag = True
    if flag: print(i+"*")
    else: print(i+".")
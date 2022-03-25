def solve(graph, src, dest, visited, psf):
    if src == dest:
        print(psf)
        return
    visited.add(src)
    for childweight in graph[src]:
        if childweight[0] not in visited:
            solve(graph, childweight[0], dest, visited, psf + str(childweight[0]))
    visited.remove(src)
    
vtc = int(input())
edges = int(input())
graph = {}
for i in range(vtc):
    graph[i] = []

for i in range(edges):
    parts = list(map(int, input().split()))
    graph[parts[0]].append([parts[1], parts[2]])
    graph[parts[1]].append([parts[0], parts[2]]) #bidirectional
    
src = int(input())
dest = int(input())
visited = set() # isse backtrack krenge
solve(graph, src, dest, visited, psf = str(src))
# 7
# 8
# 0 1 10
# 1 2 10
# 2 3 10
# 0 3 10
# 3 4 10
# 4 5 10
# 5 6 10
# 4 6 10
# 0
# 6
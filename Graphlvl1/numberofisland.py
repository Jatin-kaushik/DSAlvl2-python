def solve(i,j,graph, visited):
    if i<0 or i>= len(graph) or j<0 or j <=len(graph[0]) or graph[i][j] == 1 or visited[i][j] == True:
        return
    visited[i][j] = True
    solve(i,j+1,graph, visited)
    solve(i-1,j,graph, visited)
    solve(i,j-1,graph, visited)
    solve(i+1,j,graph, visited)    

r = int(input())
c = int(input())
graphmatrix = []
visited = []
for i in range(r):
    ls = list(map(int, input().split()))
    graphmatrix.append(ls)
    visited.append([None]*c)
count = 0
for i in range(r):
    for j in range(c):
        if graphmatrix[i][j] != 1 and  visited[i][j] != False:
            solve(i,j,graphmatrix, visited)
            count+=1


from logging import critical


class Edge:
    def __init__(self, src, nbr, wt):
        self.src = src
        self.nbr = nbr
        self.wt = wt
spath = ""
swt = 999999

lpath = ""
lwt = -999999

cpath = "" #just larger badei walo me sbse chota
cwt = 999999

fpath ="" #just smaller chotei walo me sbse bda
fwt = -999999

ls = []
def solve(graph, src, dest,comprtr, visited, psf, wsf):
    global spath,swt,lpath,lwt,cpath,cwt,fpath,fwt,ls
    if src == dest:
        ls.append([wsf,psf])
        if wsf<swt:
            swt = wsf
            spath = psf
        
        if wsf>lwt:
            lwt = wsf
            lpath = psf
            
        if wsf>comprtr and wsf<cwt:
            cwt = wsf
            cpath = psf
        
        if wsf<comprtr and wsf>fwt:
            fwt = wsf
            fpath = psf
        return
    
    visited.add(src)
    for child in graph[src]:
        if child.nbr not in visited:
            solve(graph, child.nbr, dest,comprtr, visited, psf + str(child.nbr), wsf+child.wt)
    visited.remove(src)

vtces = int(input())
edges = int(input())
graph = {}
for i in range(vtces):
    graph[i] = []
for i in range(edges):
    values = input().split()
    v1 = int(values[0])
    v2 = int(values[1])
    wt = int(values[2])
    e1 = Edge(v1,v2,wt)
    e2 = Edge(v2,v1,wt)
    graph[e1.src].append(e1)
    graph[e2.src].append(e2)
src = int(input())
dest = int(input())
comprtr = int(input()) #for ceil and floor value
k = int(input())
visited = set()
solve(graph, src, dest,comprtr, visited, psf=str(src), wsf = 0)

ls = sorted(ls)
# print(ls)
print(f"Smallest Path = {spath}@{swt}")
print(f"Largest Path = {lpath}@{lwt}")
print(f"Just Larger Path than {comprtr} = {cpath}@{cwt}")
print(f"Just Smaller Path than {comprtr} = {fpath}@{fwt}")
print(f"{k}th largest path = {ls[len(ls)-k][1]}@{ls[len(ls)-k][0]}")
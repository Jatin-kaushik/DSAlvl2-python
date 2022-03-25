def solve(n,a,b,c,d):
    c = 0
    dictab = {}
    for i in a:
        for j in b:
            v = i+j
            if v in dictab:
                dictab[v].append([i,j])
            else:
                dictab[v] = [[i,j]]
    
    for i in c:
        for j in d:
            v = i+j
            f = -v
            if f in dictab:
                c+= len(dictab[f])
    return c

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))
print(solve(n,a,b,c,d))
def solve():
    min = 999999
    max = -999999
    for i in range(n):
        for j in range(n):
            

n = int(input())
arr = list(map(int, input().split()))
print(solve(n, arr))
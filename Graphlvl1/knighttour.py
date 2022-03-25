def solve(chess, r,c, visited, move):
    if r<0 or r>=len(chess) or c<0 or c>= len(chess[0]) or (r,c) in visited:
        return
    # print(len(visited))
    if len(visited)+1 == len(chess)*len(chess):
        print(chess)
    visited.add((r,c))
    chess[r][c]=move
    solve(chess, r-2,c+1, visited, move+1)
    solve(chess, r-1,c+2, visited, move+1)
    solve(chess, r+1,c+2, visited, move+1)
    solve(chess, r+2,c+1, visited, move+1)
    solve(chess, r+2,c-1, visited, move+1)
    solve(chess, r+1,c-2, visited, move+1)
    solve(chess, r-1,c-2, visited, move+1)
    solve(chess, r-2,c-1, visited, move+1)
    visited.remove((r,c))
    chess[r][c] -=1


n = int(input())
r= int(input())
c = int(input())
chess = [[0]*n for i in range(n)]
visited = set()
solve(chess, r,c, visited, 1)
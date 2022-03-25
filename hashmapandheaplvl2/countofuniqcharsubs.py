def solve(inp):
    set1 = set()
    release_i = 0
    count = 0
    for i in inp:
        if i not in set1:
            set1.add(i)
            n = len(set1)
            # print(n, set1)
            count += n
        else:
            while(release_i<len(inp)):
                if inp[release_i] != i:
                    set1.remove(inp[release_i])
                    release_i+=1
                else:
                    set1.remove(inp[release_i])
                    release_i+=1
                    break
            set1.add(i)
            n = len(set1)
            # print(n, set1)
            count += n

    return count
        
inp = input()
print(solve(inp))
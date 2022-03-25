def solve(n, ls):
    dict1 = {}
    for i in ls:
        diff = ''
        for j in range(1,len(i)):
            pele = i[j-1]
            cele = i[j]
            d = ord(cele) - ord(pele)
            diff = diff + str(d)
        if diff in dict1:
            dict1[diff].append(i)
        else:
            dict1[diff] = [i]
    
    for k,v in dict1.items():
        for j in v:
            print(v, end ="")
        print()
            

n = int(input())
ls = input().split()
solve(n,ls)


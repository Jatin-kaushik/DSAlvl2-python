def c1(ls):
    a1 = []
    a2 = []
    i = 0
    j = len(ls)-1
    while(i>j):
        a1.append(ls[i])
        a2.append(ls[j])
        i+=1
        j-=1
    diff = sum(a1)-sum(a2)
    return diff


# n = int(input())
# ls = list(map(int(input().split())))

print(c1([2, -7, 8, -1, 20]))
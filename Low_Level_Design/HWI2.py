def maxele(A):
    dict1 = {}
    for i in A:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    ls = []
    for k,v in dict1.items():
      if v<2:
        ls.append(k)
    for i in ls:
      dict1.pop(i)
    # print(dict1)
    mx = 2
    hero = -1
    for k,v in dict1.items():
        if v >= mx and hero <= k:
            hero = k
            mx = v
    return hero


def Solve(N,A):
    while True:
        hero = maxele(A)
        if hero > -1:
            p1 = A.index(hero)
            A.remove(hero)
            p2 = A.index(hero)
            A[p2] = A[p2]//2
            # print(A)
        else:
            break;
    return A
    # if len(A)>0:
    #     for i in A:
    #         print(i)
    # else:
    #     print(0)
    
    
                
                
ls = Solve(6, [2,1,5,10,10,1])
for i in ls:
    print(i)
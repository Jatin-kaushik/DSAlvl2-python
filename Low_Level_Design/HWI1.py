def Solve(N,A):
    mi = 0
    for i in range(2,int(max(A)**0.5)):
        cnt = 0

        for ele in A:
            if (ele/i == int(ele/i)):
                cnt +=1
            # print(cnt)
        if cnt> mi:
            mi = cnt
        
    if mi >0:
        mi = len(A) - mi
        
    return mi

print(Solve(4, [12,4,5,2]))
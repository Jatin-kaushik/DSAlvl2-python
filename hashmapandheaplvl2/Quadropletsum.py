def solve(n, arr, t):
    res = set()
    arr.sort()
    for i in range(n-4):
        for j in range(i+1, n-3):
            # print(t,i,j)
            val = t-(arr[i]+ arr[j])
            # print(val)
            l = j+1
            r = n-1
            while(l<r):
                # print(l,r)
                if val < (arr[l]+arr[r]):
                    r-=1
                elif val>(arr[l] + arr[r]):
                    l+=1
                else:
                    st = f"{arr[i]} {arr[j]} {arr[l]} {arr[r]}"
                    if st not in res:
                        print(st)
                        res.add(st)
                    l+=1
                    r-=1
n = int(input())
arr = list(map(int, input().split()))
t = int(input())
solve(n, arr, t)
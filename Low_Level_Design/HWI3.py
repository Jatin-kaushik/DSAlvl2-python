def Solve(N,A):
    s_arr = sorted(A)
    mid = len(A)//2
    fmid = mid-1
    r = s_arr[mid] - s_arr[fmid]
    return r
                
    
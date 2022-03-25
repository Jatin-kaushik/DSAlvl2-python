def solve(arr):
    ans  = 0
    set1 = set()
    ind_release = 0
    for i in arr:
        if i not in set1: #aquire
            set1.add(i)
        else:#release
            while ind_release < len(arr):
                if i!=arr[ind_release]:
                    set1.remove(arr[ind_release])
                    ind_release+=1
                else:
                    set1.remove(arr[ind_release])
                    ind_release+=1
                    break
        set1.add(i)
        print(set1)
        if len(set1)>ans:
            ans = len(set1)
    return(ans)
                    
arr = input()
print(solve(arr))
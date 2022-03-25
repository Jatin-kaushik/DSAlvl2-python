def solve(arr1, arr2):
    dict1 = {}
    for i in range(arr2):
        ele = arr2[i]
        if ele in dict1:
            dict1[ele].append(i)
        else:
            dict1[ele] = [i]
    for i in arr1:
        ls = dict1[i]
        fi = ls[0]
        ls.pop(0)
        print(fi, end = "")

#o(n)  me krne ke lie arr2 ke index ke lie stack banao or last se freq map banao
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
print(solve(arr1,arr2))
#https://codeforces.com/contest/1520/problem/D

def cp(n,arr):
    dict1 ={}
    for i in range(len(arr)):
        val = arr[i]
        if val-i in dict1:
            dict1[val-i] +=1
        else:
            dict1[val-i] = 1
    
    count = 0
    for k,v in dict1.items():
        if v>=2:
            count+= int((v*(v-1))/2)
    return count
n = int(input())
arr = list(map(int, input().split()))
print(cp(n, arr))
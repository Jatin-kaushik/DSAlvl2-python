from math import ceil


def rinforest(arr):
    dict1 = {}
    for i in arr:
        if i in dict1:
            dict1[i] +=1
        else:
            dict1[i] = 1
    tot_rab = 0
    for k,v in dict1.items():
        sz = k+1
        rabb = v
        tot_rab += ceil(rabb/sz) * sz
    return tot_rab
        
arr= list(map(int, input().split()))
print(rinforest(arr))
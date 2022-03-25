def canReorderDoubled(arr):
    dict1 = {}
    for i in arr:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i] = 1
    arr = sorted(arr)
    print(arr)
    for i in arr:
        if i == 0:
            continue
        if i in dict1 and 2*i in dict1:
            if dict1[i] == 1:
                dict1.pop(i)
            else:
                dict1[i] -=1
                
            if dict1[2*i] == 1:
                dict1.pop(2*i)
            else:
                dict1[2*i] -=1
    
    if 0 in dict1:
        dict1.pop(0)
    if len(dict1) == 0:
        return True
    else: return False
    
print(canReorderDoubled([-33,0]))
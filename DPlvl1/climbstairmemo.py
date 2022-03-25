from ast import Store


def climb_stair(n, storage):
    if n<0:
        return 0
    if n == 0:
        return 1
    
    if storage[n] != 0:
        return storage[n]
    
    jmp1 = climb_stair(n-1, storage)
    jmp2 = climb_stair(n-2, storage)
    jmp3 = climb_stair(n-3, storage)
    
    tot_p = jmp1+jmp2+jmp3
    storage[n] = tot_p
    return tot_p

n = int(input())
storage = [0]*(n+1)
print(climb_stair(n, storage))
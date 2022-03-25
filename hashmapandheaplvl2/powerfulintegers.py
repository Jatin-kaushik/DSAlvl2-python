import math


def solve(x,y,b):
    set1 = set()
    if x == 1: bx = 1
    else: bx = x
    if y == 1: by = 1
    else: by = x

    for i in range(b):
        for j in range(b):
            pf = (x**i + y**j)
            if pf <=b:
                if pf not in set1:
                    set1.add(pf)
            else:
                break
    return list(set1)
                
x = int(input())
y = int(input())
b = int(input())
print(solve(x,y,b))
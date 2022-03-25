def GCD(n1, n2):
    while(n1%n2 != 0):
        rem = n1%n2
        n1 = n2
        n2 = rem
    return n2

def hcf(size, arr):
    gcd = arr[0]
    for i in range(1, size):
        a = GCD(gcd, arr[i])
        gcd = a
    return gcd

size = int(input()) # input1 = 3
arr = list(map(int, input().split())) #input2 = 2 4 8
print(hcf(size, arr)) # output = 2
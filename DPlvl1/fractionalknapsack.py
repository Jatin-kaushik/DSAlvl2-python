def fracs(n, price, weight, caps):
    pbywt = [0]*(n)

    for i in range(n):
        pbywt[i] = (round(price[i]/weight[i], 2), price[i], weight[i])
    pbywt = sorted(pbywt, reverse = True)
    ans = 0
    for i in range(len(pbywt)):
        if pbywt[i][2] <= caps:
            caps -= pbywt[i][2]
            ans += pbywt[i][1]
        else:
            ans  += pbywt[i][0] * caps
            caps -= caps/pbywt[i][2] * pbywt[i][2]
    return ans

n = int(input())
p = input().split(" ")
w = input().split(" ")
price = []
weight = []
caps = int(input())
for i in range(n):
    price.append(int(p[i]))
    weight.append(int(w[i]))
    
# print(price)
print(fracs(n, price, weight, caps))
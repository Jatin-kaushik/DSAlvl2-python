
arr = list(map(int, input().split()))
k = int(input())
dict1 = {}
dict1[0] = 1
sum = 0
count  = 0
for i in arr:
    sum+=i
    modu = sum%k
    print(modu)
    if modu<0:
        modu +=k
    if modu in dict1:
        count += dict1[modu]
        dict1[modu] +=1
    else:
        dict1[modu] = 1
print(count)


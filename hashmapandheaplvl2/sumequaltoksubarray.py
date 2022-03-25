arr = list(map(int, input().split()))
k = int(input())
dict1 = {}
sum = 0
count = 0
dict1[0] = 1
for i in arr:
    sum +=i
    if (sum-k) in dict1:
        count += dict1[sum-k]
    if sum in dict1:
        dict1[sum] +=1
    else:
        dict1[sum] =1
print(count)
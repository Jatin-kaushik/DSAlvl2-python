n = int(input())
arr = list(map(int, input().split()))

sum = 0
ans  = 0
dict1 = {}
dict1[0] = 1
for i in arr:
    if i == 0:
        sum+=-1
    else:
        sum+=1
    
    if sum in dict1:
        ans += dict1[sum]
        dict1[sum]+=1
    else:
        dict1[sum] = 1
    
print(ans)
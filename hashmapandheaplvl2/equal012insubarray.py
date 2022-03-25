str1 = input()
c0 = 0
c1 = 0
c2 = 0
key = "0#0"
dict1 = {}
dict1[key] = 1
ans = 0
for i in range(len(str1)):
    ele = str1[i]
    if ele == "0":
        c0+=1
    elif ele == "1":
        c1 +=1
    else:
        c2+=1
    key = str(c1-c0) +"#" + str(c2-c1)
    
    if key in dict1:
        ans += dict1[key]
        dict1[key]+=1
    else:
        dict1[key] = 1

print(ans)
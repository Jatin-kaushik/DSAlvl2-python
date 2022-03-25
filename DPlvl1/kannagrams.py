def kanna(inp1, inp2, k):
    dict1 = {}
    dict2 = {}
    for i in inp1:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] =1
    
    for i in inp2:
        if i in dict1:
            if dict1[i] == 1:
                dict1.pop(i)
            else:
                dict1[i] -=1
    gap = 0
    if " " in dict1:
        dict1.pop(" ")
    
    for key,v in dict1.items():
        gap+=v
    # print(gap,k)
    if gap>int(k):
        print("false")
    else:
        print("true")
inp1 = input()
inp2 = input()
k = int(input())
kanna(inp1, inp2, k)
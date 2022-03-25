def solve(inp1, inp2): # x1 and y1 pe infinte case handle
    if len(inp2)>len(inp1):
        return ""
    dict1 = {}
    dict2 = {}
    res = ""
    ir = -1 #released index
    uc = len(inp2) #unmatched character
    for i in inp2:
        if i in dict2:
            dict2[i]+=1
        else:
            dict2[i] = 1
    
    for i in range(len(inp1)):
        ele = inp1[i]
        if ele in dict1:
            dict1[ele] +=1
        else:
            dict1[ele] = 1
        
        if ele in dict2:
            if dict1[ele]<= dict2[ele]:
                uc-=1
        # if uc ==0 : print(uc, inp1[ir+1:i+1])
        # if i ==10: print(uc, dict1)
                
        while uc == 0 and ir<i:
            path = inp1[ir+1:i+1]
            # print(uc, ir, i, path)
            if len(res) == 0:
                res = path
            else:
                if len(path)<len(res):
                    res = path
            ir+=1
            release = inp1[ir]
            dict1[release] -=1 
            # print(release, dict1)
            if release in dict2:
                if dict1[release] < dict2[release]:
                    uc+=1
            # print(uc, ir, i, path)

    return res
inp1 = input()
inp2 = input()
print(solve(inp1, inp2))
def solve(inp1, inp2):
    dict1 = {}
    for i in range(len(inp1)):
        v1 = inp1[i]
        v2 = inp2[i]
        if v1 not in dict1 and v2 not in dict1:
            dict1[v1] = v2
            dict1[v2] = v1
        elif v1 in dict1 and v2 not in dict1:
            val = dict1[v1]
            if v2 == val:
                dict1[v2] = v1
            else:
                return False
        elif v1 not in dict1 and v2 in dict1:
            val = dict1[v2]
            if val == v1:
                dict1[v1] = v2
            else:
                return False
        else:
            # print(1)
            if dict1[v1] != v2 and dict1[v2] != v1:
                return False
    return True
                
            
                    
inp1 = input()
inp2 = input()
a = solve(inp1, inp2)
if a:
    print("true")
else: print("false")
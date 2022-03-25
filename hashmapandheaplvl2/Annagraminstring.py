def annagram(inp1, inp2):
    dictofinp2 = {}
    for i in inp2:
        if i in dictofinp2:
            dictofinp2[i] +=1
        else:
            dictofinp2[i] = 1
    
    i = 0
    dictofinp1 = {}
    while i<len(inp2):
        if inp1[i] in dictofinp1:
            dictofinp1[inp1[i]] += 1
        else:
            dictofinp1[inp1[i]] = 1
        i+=1
        
    res = []
    if dictofinp1== dictofinp2:
        res.append(0)
        
    while i <len(inp1):
        ele = inp1[i]
        pele = inp1[i-len(inp2)]
         
        if ele in dictofinp1:
            dictofinp1[ele] += 1
        else:
            dictofinp1[ele] = 1
            
        if dictofinp1[pele] ==1:
            dictofinp1.pop(pele)
        else:
            dictofinp1[pele] -=1
        # print(dictofinp1 == dictofinp2)
        if dictofinp1 == dictofinp2:
            res.append(i-len(inp2)+1)
        i+=1
    print(len(res))
    for i in res:
        print(i, end = " ")
         
         
inp1 = input()
inp2 = input()
annagram(inp1, inp2)

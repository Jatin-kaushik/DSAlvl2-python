def cpsk(arr, n, k):
    #code here
    t = k
    dict1 ={}
    for i in arr:
        modu = i%t
        if modu in dict1:
            dict1[modu] +=1
        else:
            dict1[modu] = 1
    
    # freqeunce array of modulus ban gaya ab pair bnaane h
    count = 0
    if t%2 == 0:
        for k,v in dict1.items():
            if k == 0 or k==t/2 and v >0:
                count += int((dict1[k]*(dict1[k]-1))/2)
            else:
                if k < t-k and k in dict1 and t-k in dict1:
                    if dict1[k] > dict1[t-k]:
                        count+= dict1[k]
                    else:
                        count+= dict1[t-k]
    else:
        # print("odd")
        for k,v in dict1.items():
            if k == 0  and v >0:
                count += int((dict1[k]*(dict1[k]-1))/2)
            else:
                if k < t-k and k in dict1 and t-k in dict1:
                    if dict1[k] > dict1[t-k]:
                        count+= dict1[k]
                    else:
                        count+= dict1[t-k]
    return count
n = int(input())
arr = list(map(int, input().split()))
k = int(input())
print(cpsk(arr, n, k))
#https://pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/hashmap-and-heaps/check-if-an-array-cab-be-divided-into-pairs-whose-sum-is-divisible-by-k-official/ojquestion

def ispair(n, arr, tar):
    dict1 = {}
    for i in arr:
        modu = i%tar
        if modu in dict1:
            dict1[modu]+=1
        else:
            dict1[modu] = 1
        resbool = True
    if tar%2 == 0:
        for k,v in dict1.items():
            if k == 0 or k == int(tar/2):
                if v%2 != 0:
                    resbool = False
                    return resbool
            else:
                if tar-k not in dict1:
                    resbool = False
                    return resbool
                else:
                    if dict1[k] != dict1[tar-k]:
                        resbool = False
                        return resbool
    else:
        for k,v in dict1.items():
            if k == 0:
                if v%2 != 0:
                    resbool = False
                    return resbool
            else:
                if tar-k not in dict1:
                    resbool = False
                    return resbool
                else:
                    if dict1[k] != dict1[tar-k]:
                        resbool = False
                        return resbool
    return resbool
n = int(input())
arr = list(map(int, input().split()))
tar = int(input())
ans = ispair(n,arr, tar)
if ans == True: print("true")
else: print("false")
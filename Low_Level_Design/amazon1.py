def getEncryptedNumber(numbers):
    arr =numbers
    while(len(arr)>2):
        res = [arr[i]+arr[i+1] for i in range(0,len(arr)-1)]
        for i in range(len(res)):
            ele= str(res[i])
            if len(ele)>1:
                ele = ele[len(ele)-1]
                ele = int(ele)
                res[i] = ele

        arr = res
    arr = [str(i) for i in arr]
    return (''.join(arr))



print(getEncryptedNumber([1,2,3,4]))
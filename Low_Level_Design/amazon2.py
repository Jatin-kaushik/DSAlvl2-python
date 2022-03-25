# def minimumGroups(awards,k):
#     arr = sorted(awards)
#     # print(arr)
#     m = 0
#     i = 0
#     while (i<len(arr)):
#         j = i+1
#         while True:
#             if j>=len(arr):
#                 break
#             if(arr[j]-arr[i]<=k):
#                 j+=1
#             else:
#                 break
#         m+=1
#         i=j
#     return m
          
def minimumGroups(awards,k):
    # print(arr)
    arr = awards
    m = 0
    i = 0
    while (i<len(arr)):
        m1 = min(awards)
        j = i+1
        awards.remove(m1)
        while True:
            m2 = min(awards)
            awards.remove(m2)
            if j>=len(arr):
                break
            if(m2-m1<=k):
                j+=1
            else:
                break
        m+=1
        i=j
    return m     
        
print(minimumGroups([1,13,6,8,9,3,5],4))
print(minimumGroups([3,1,4,3,9],10))
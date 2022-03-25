def findMaxConsecutiveOnes(nums):
    t1 = 0
    m1 = 0
    for i in nums:
        if i == 1:
            t1+=1
            if t1 > m1:
                m1 = t1
        else:
            if t1 > m1:
                m1 = t1
            t1 = 0
    return m1
print(findMaxConsecutiveOnes([0,1,1,0,1,1,1,1]))
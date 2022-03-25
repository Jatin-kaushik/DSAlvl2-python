def solve1(key, val, dict1, rearrange_arr, k):
    # print(key, val, dict1, k, len(rearrange_arr), rearrange_arr)
    if len(rearrange_arr)<k:
        dict1[key] = val
        rearrange_arr.append(key)
    else:
        if key in dict1:
            if rearrange_arr[0] ==key:
                idx  = 0     
            elif rearrange_arr[k-1] == key:
                idx =  k-1
            else:
                idx = rearrange_arr.index(key)
                
            rearrange_arr.pop(idx)
            rearrange_arr.append(key)
            dict1[key] = val
        else:
            v = rearrange_arr[0]
            rearrange_arr.pop(0)
            dict1.pop(v)
            dict1[key] = val
            rearrange_arr.append(key)
    # print(key, val, dict1, k, len(rearrange_arr), rearrange_arr)

def solve2(key, dict1, rearrange_arr):
    if key in dict1:
        idx = rearrange_arr.index(key)
        rearrange_arr.pop(idx)
        rearrange_arr.append(key)
        return dict1[key]
    else:
        return -1
    
    
inp = input().split()
k = int(inp[1])
dict1 = {}
rearrange_arr = []
while True:
    inp1 = input().split()
    if inp1[0] == "put":
        key = int(inp1[1])
        val = int(inp1[2])
        solve1(key, val, dict1, rearrange_arr, k)
    elif inp1[0] == "get":
        key = int(inp1[1])
        ans = solve2(key, dict1, rearrange_arr)
        print(ans)
    else: # Stop
        break          
inp1 = input()
inp2 = input()
ls = inp1.split(" ")
print(len(ls))
count = 0
for i in ls:
    if i==inp2:
        count+=1
print(count)
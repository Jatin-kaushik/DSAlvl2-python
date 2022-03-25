c = 1
for i in range(1,5):
    for j in range(i+1,5):
        for k in range(j+1, 5):
            c = c*(i+j+k)

print(c)
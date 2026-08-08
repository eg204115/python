val = 9 
for i in range(5):
    for j in range(2,3,1):
        val +=1
        if (val%2==0):
            continue
            val += 2
        else:
            val += 2
print(val)

for j in range(2, 6, 2):
    print(j)
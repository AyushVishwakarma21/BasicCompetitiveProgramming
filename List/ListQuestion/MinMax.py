A = [1,2,3,4,5]
min =0
max = 0
for i in A:
    if min>i:
        min=i
    if max<i:
        max=i

print("min:",min,"max:",max)
n = int(input())
arr = []
for i in range(n):
    eele = int(input())
    arr.append(eele)
max=0
for i in arr:
    if max<i:
        max=i

print(max)
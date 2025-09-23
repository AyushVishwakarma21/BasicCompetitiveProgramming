n = int(input())
emp_IDs = list(map(int, input().split()))
even_IDs = []
for id in emp_IDs:
    if id % 2 == 0:
        even_IDs.append(id)

if even_IDs:
    for id in even_IDs:
        print(id,end=" ")
else:
    print(-1)

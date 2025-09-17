n = int(input())
employee_ids = list(map(int, input().split()))
even_ids = []
for id in employee_ids:
    if id % 2 == 0:
        even_ids.append(id)

if even_ids:
    for i in range(len(even_ids)):
        if i != len(even_ids) - 1:
            print(even_ids[i], end=" ")
        else:
            print(even_ids[i])
else:
    print(-1)

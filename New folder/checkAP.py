lst = [3,5,1]
lst.sort()
d = lst[1] - lst[0]
if len(lst)==1:
    print(1)
for i in range(1,len(lst)-1):
    if lst[i + 1] - lst[i] != d:
        print(0)
    else:
        print(1)
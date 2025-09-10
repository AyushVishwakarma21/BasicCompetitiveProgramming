arr = list(map(int,input("enter elements: ").split()))

filteredArr = []

for i in arr:
    if i%2==0:
        filteredArr.append(i)

print(filteredArr)
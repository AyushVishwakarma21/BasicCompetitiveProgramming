n =int(input())
lst = list(map(int,input().split()))
sums= []
for i in range(n):
    for j in range(i,n):
        sum = 0
        for k in range(i,j+1):
            sum+=lst[k]
            sums.append(sum)
print(max(sums))
n = int(input())
lst = list(map(int,input().split()))
first,sesond = map(int,input().split())

sum = 0
for i in range(first-1,sesond):
    sum+=lst[i]
print(sum)
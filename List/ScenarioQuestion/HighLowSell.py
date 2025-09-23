n = int(input())
sales = list(map(int,input().split()))

high = sales[0]
low = sales[0]

for i in sales:
    if high<i:
        high=i
    if low>i:
        low=i

print(high,low)
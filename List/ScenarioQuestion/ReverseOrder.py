n = int(input())
order_IDs = list(map(int,input().split()))
order_IDs.reverse()

for i in order_IDs:
    if i%5==0:
        print(i,end=" ")
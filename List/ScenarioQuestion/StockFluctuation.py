n = int(input())
stk_prices = list(map(int,input().split()))
count=0
for i in range(1,n):
    if stk_prices[i]>stk_prices[i-1]:
        count =count+1

print(count)
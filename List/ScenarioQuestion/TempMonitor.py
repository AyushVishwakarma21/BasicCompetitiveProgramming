n = int(input())
temps = list(map(int,input().split()))
avg = sum(temps)/len(temps)
count = 0
for i in temps:
    if i>avg:
        count = count+1
print(count)
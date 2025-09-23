N = int(input())

arr = []
for i in range(N):
    ele = int(input())
    arr.append(ele)
    
M = int(input())
for i in range(len(arr)):
    if M==arr[i]:
        print(i)
if M not in arr:
    print(-1)
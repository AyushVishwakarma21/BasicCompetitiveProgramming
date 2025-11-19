# arr = [16,17,4,3,5,2]
arr = [2,-1,0,1,2,8]


req_arr = []
last = arr[-1]
req_arr.append(last)
for i in range(len(arr)-2,0,-1):
    if arr[i]>last:
        req_arr.append(arr[i])
        last = arr[i]
req_arr.reverse()
print(req_arr)
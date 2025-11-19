arr = [6,9,6,10,9]
se = set()

for ele in arr:
    if ele in se:
        se.remove(ele)
    else:
        se.add(ele)

print(se)



ans =0 
for i in range(len(arr)):
    ans = ans^arr[i]
print(ans)
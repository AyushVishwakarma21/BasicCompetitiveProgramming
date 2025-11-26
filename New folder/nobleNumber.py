lst = [1,-5,3,5,-10,4]

# n = len(lst)
# noble = []
# for i in range(n):
#     count = 0
#     for j in range(n):
#         if lst[i]>lst[j]:
#             count+=1
#     if count==lst[i]:
#         noble.append(lst[i])
# print(noble,"number of noble elements: ",len(noble))

lst.sort()
print(lst)
noble = []
for i in range(len(lst)):
    if i==lst[i]:
        noble.append(lst[i])
print(noble,"number fo noble elements: ",len(noble))

# Q. given an array A of size n. find the maximum value of j-i such that A[i]<=A[j]
# e.g. 
lst = [34, 8, 10, 3, 2, 80, 30, 33, 1]
n = len(lst)
max_diff = -1

for i in range(n):
    for j in range(i + 1, n):
        if lst[i] <= lst[j]:
            max_diff = max(max_diff, j - i)

print(max_diff)
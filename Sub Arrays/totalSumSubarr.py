"""Consider an array arr of size N.
Take an element at index i (0-based).

How many subarrays include arr[i]?

Number of choices for starting point = (i + 1)

Number of choices for ending point = (N - i)

Therefore, the total number of subarrays containing arr[i] is:
    (i+1)×(N−i)

Contribution of element i=arr[i]×(i+1)×(N−i)

    Total=i=0∑N−1​arr[i]×(i+1)×(N−i)
"""

n = int(input())
lst = list(map(int,input().split()))
total = 0
for i in range(n):
    total += lst[i]*(i+1)*(n-i)
print(total)
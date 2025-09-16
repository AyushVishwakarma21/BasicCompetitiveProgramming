A = [3,5,1,2,1,2]

n = len(A)
for i in range(n//2):
    A[i], A[n-1-i] = A[n-1-i], A[i]

print(A)    
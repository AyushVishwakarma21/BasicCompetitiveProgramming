n = int(input())
lst = list(map(int,input().split()))

# n = 5
# lst = [10,20,30,40,50]

for i in range(n):
    for j in range(i,n):
        for k in range(i,j+1):
            print(lst[k],end=" ")
        print()




# alternate (chatgpt)
def print_all_subarrays(arr):
    n = len(arr)
    # Outer loop for starting index
    for start in range(n):
        # Inner loop for ending index
        for end in range(start, n):
            # Print the subarray from start to end
            print(arr[start:end+1])

# Example usage:
arr = [1, 2, 3]
print_all_subarrays(arr)
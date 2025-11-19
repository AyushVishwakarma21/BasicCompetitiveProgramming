n = int(input())

for i in range(n):
    num1 = input()

even_sum = 0
for i in range(len(num1)):
    if num1[i]%2==0:
        even_sum+=num1[i]
    
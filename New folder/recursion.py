# n = 5
# sum = 0
# for i in range(1,n+1):
#     sum+=i
# print(sum)

def addition(n):
    if n==0:
        return 0
    return n + addition(n-1)

print(addition(5))


def facto(n):
    if n==0:
        return 1
    return facto(n-1)*n

print(facto(5))
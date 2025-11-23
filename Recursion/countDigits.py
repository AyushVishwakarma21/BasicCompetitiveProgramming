def countdigits(n):
    if n==0:
        return 0
    return 1+ countdigits(n//10)

print(countdigits(103))
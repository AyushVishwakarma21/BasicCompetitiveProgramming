def suma(n):
    if n<1:
        return 0
    return n+ suma(n-1)

print(suma(5))
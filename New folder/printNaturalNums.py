def natural(n):
    if n==0:
        return
    natural(n-1)
    print(n)

natural(5)

print("="*50)

def naturalreverse(n):
    if n==0:
        return
    print(n)
    naturalreverse(n-1)

naturalreverse(5)


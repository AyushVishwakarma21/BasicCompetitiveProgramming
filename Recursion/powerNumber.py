x=2
n=5
powered = 1
for i in range(1,n+1):
    powered *=x
print(powered)

def powerNum(x,n):
    if n==0:
        return 1
    return x*powerNum(x,n-1)
print(powerNum(2,5))
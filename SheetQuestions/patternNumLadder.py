n = 4
a=1
for i in range(n+1):
    for j in range(i):
        print(a,end="   ")
        a+=1
    print()
n  = int(input("Enter number:"))

for i in range(1,n+1):
    for j in range(1,n+1-i):
        if(i%2==0):
            print(j,"*",j+1,end="")
        else:
            print(j)    
row = int(input("Enter rows: "))
col = int(input("Enter columns: "))

for i in range(1,row+1):
    for j in range(1,col+1):
        print("* ",end="")
    print()
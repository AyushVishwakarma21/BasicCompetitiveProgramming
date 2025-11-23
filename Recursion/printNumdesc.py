def printNums(n):
    if n==0:
        return
    print(n,end=" ")
    printNums(n-1)

printNums(5)
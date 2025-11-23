def printNums(n):
    if n==0:
        return
    printNums(n-1)
    print(n,end=" ")    

printNums(5)
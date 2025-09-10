arr = list(map(int,input("enter elements: ").split()))

increment = int(input("Enter number added to elemets in list:"))

incrementedArr = []
for i in arr:
    i=i+increment
    incrementedArr.append(i)

print(incrementedArr)
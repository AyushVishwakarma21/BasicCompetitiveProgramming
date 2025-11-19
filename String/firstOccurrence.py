A = input("A = ")
B = int(input("B = "))

char  =chr(B)
index = A.find(char)
print(index if index!=-1 else "it does not exist")

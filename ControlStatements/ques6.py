a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

if(a>b and a>c):
    print("A is Maximum")
elif(b>c and b>a):
    print("B is Maximum")
else:
    print("C is Maximum")
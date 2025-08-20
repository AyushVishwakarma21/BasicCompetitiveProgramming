print(range(0,6))

print(list(range(0,6)))

for i in range(1,10,2):
    print(i)

for i in range(1,10,2):
    print(i*i,end=" ")

print()
n  =int(input("Enter number: "))

for i in range(1,n+1):
    print(i)

n2  =int(input("Enter number: "))
for i in range(1,n2+1,2):
    print(i)

num1  =int(input("Enter number: "))
num2 = int(input("Enter number: "))
po = 1
for i in range(num2):
    po = po *num1

print(po)
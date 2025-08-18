num = int(input("Enter number: "))
digits =0
while(num>0):
    num = num//10
    digits+=1
print(digits)
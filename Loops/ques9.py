num = int(input("Enter number: "))
sum = 0
while(num>0):
    rem = num%10
    num = num//10
    sum+=rem
print(sum)

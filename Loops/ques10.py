old_num = int(input("Enter number: "))
num_copy = old_num
reverse = 0

while(old_num > 0):
    rem = old_num % 10
    reverse =  rem + reverse * 10
    old_num = old_num // 10

print(reverse)
if(reverse==num_copy):
    print("yes")
else:
    print("no")
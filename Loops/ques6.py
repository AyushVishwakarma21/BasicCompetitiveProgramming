n= int(input("enter number: "))

count = 1
sum =0
while count<=n:
    if(count%2==0):
        sum+=count
    count+=1

print(sum)
arr = list(map(int,input("Enter elements:").split()))

target = int(input("Enter the Target:"))
count=0
for i in arr:
    if i== target:
        count+=1
print("Occurred:",count)
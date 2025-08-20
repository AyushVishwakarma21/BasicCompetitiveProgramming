for i in range(100):
    print(i)
    if(i==6):
        break

print("-"*100)

for i in range(10):
    if(i%3==0):
        continue
    print(i)
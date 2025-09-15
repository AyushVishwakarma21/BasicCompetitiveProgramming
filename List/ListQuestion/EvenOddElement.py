A = [1,2,3,4]
OddCount = 0
EvenCount = 0
for i in A:
    if i%2==0:
        EvenCount=+1
    else:
        OddCount=+1
    
diff = abs(EvenCount-OddCount)
print(diff)
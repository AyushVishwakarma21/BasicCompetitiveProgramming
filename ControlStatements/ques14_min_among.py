a = int(input("Enter A Number: "))
b =  int(input("Enter B Number: "))
c = int(input("Enter C Number: "))

if(a<b and a<c):
    print('A',a)
elif(b<a and b<c):
    print('B',b)
else:
    print('C',c)
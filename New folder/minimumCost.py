lst = ['a','b','c','d']
suma = 0
for i in range(len(lst)):
    cost =0
    for j in range(i,len(lst)):
        cost+= ord(lst[j])
    suma+=cost
    lst.pop(i)
print(suma)

lst2 =[3,5,1,-3]
suma = 0
for i in range(len(lst2)):
    cost =0
    for j in range(i,len(lst2)):
        cost+= lst2[j]
    suma+=cost
    lst2.remove(lst2[i])
print(suma)

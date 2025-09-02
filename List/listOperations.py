List = [1,2,3,45,6,78]

List.append(101)

list2= [1,3,25,647,578,68]
List.append(list2)

List.insert(3,404)
List.insert(3213457654324676,100)

List.extend([8,'qwerty',True])

List.remove(100)

print(List)

list3 = [12,14,24,56,12,43]

list3.remove(12)
list3.pop()

print(list3)

list4=  [1,2,3,4,5]
n = len(list4)
# for i in range(0,n//2):
#     list4[i], list4[n-1-i] = list4[n-1-i], list4[i]
    

left =0 
right =len(list4)-1
while(left<right):
    list4[left], list4[right] = list4[right], list4[left]
    left+=1
    right-=1
print(list4)
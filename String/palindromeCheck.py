T = int(input())
lst = []
for i in range(T):
    word = input()
    lst.append(word.lower())
print(lst)

for word in lst:
    if word ==word[::-1]:
        print(1)
    else:
        print(0)
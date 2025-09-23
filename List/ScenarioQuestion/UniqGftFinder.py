n = int(input())
gifts = list(map(int, input().split()))

unique_gifts = []

for gift in gifts:
    if gifts.count(gift) == 1 and gift not in unique_gifts:
        unique_gifts.append(gift)

if unique_gifts:
    for gift in unique_gifts:
        print(gift, end=" ")
else:
    print(-1)

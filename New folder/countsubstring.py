stringg = "abc"
count = 0
for i in range(len(stringg)):
    for j in range(i + 1, len(stringg) + 1):
        substr = stringg[i:j]
        if substr == substr[::-1]:
            count += 1

print(count)
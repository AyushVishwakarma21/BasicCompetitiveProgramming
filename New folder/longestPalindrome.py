stringg =  "abcba is a aba"

lst = stringg.split()
print(lst)

longest = []
for st in lst:
    if st==st[::-1]:
        longest.append(st)
long = max(longest)
print(long)


string2 = "abacab"
pl = []
# for i in range(len(string2)):
#     for j in range(len(string2)-i):
        


ans = 1
for i in range(len(string2)):
    for j in range(i,len(string2)):
        if palindrome:
            
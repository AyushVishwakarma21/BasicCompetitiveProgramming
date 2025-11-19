T = int(input())
lst = []
for i in range(T):
    word = input()
    lst.append(word.lower())

vowels = 'AEIOUaeiou'
for i in lst:
    vowels_count = 0
    consonant_count=0
    for j in i:
        if j in vowels:
            vowels_count+=1
    consonant_count= abs(len(i)-vowels_count)
    print(vowels_count,consonant_count)
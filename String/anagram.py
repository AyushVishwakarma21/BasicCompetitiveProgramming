word1 ="abcd"
word2 = "bcda"

word1 = word1.lower()
word2 = word2.lower()

if sorted(word1) == sorted(word2):
    print("anagram")
else:
    print("not anagram.")
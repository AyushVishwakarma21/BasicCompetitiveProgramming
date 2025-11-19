A = "aeiOUz"
A = A + A
taggedword = ""
vowels = "aeiou"
for char in A:
    if char.isupper():
        continue
    if char in vowels:
        taggedword+="#"
    else:
        taggedword +=char

print(taggedword)
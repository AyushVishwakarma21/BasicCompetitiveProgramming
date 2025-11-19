stringg= input()
words = stringg.split()
print(words)
reversed_order=  [word[::-1] for word in words]
print(reversed_order)
print(' '.join(reversed_order))
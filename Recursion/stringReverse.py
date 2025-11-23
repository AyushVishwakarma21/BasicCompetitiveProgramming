def stringReverse(s):
    if len(s)==0:
        return 0
    print(s[-1],end="")
    stringReverse(s[:-1])

stringReverse('hello')


# s = 'hello'
# for i in range(len(s)-1,-1,-1):
#     print(''.join(s[i]),end="")
